from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import time
from pathlib import Path
from typing import Sequence

import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

from prompts import ALL_PACKS, SYSTEM_PROMPT, output_regex, output_schema, render_user_prompt


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    completed: set[str] = set()
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                completed.add(json.loads(line)["id"])
            except (json.JSONDecodeError, KeyError):
                continue
    return completed


def stable_hash(value) -> str:
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def render_chat(tokenizer, user_prompt: str, template_mode: str) -> str:
    if template_mode == "plain":
        return f"System: {SYSTEM_PROMPT}\n\nUser: {user_prompt}\n\nAssistant:"
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
    kwargs = {"tokenize": False, "add_generation_prompt": True}
    try:
        return tokenizer.apply_chat_template(messages, enable_thinking=False, **kwargs)
    except TypeError:
        return tokenizer.apply_chat_template(messages, **kwargs)


def load_model(path: str):
    tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True, trust_remote_code=False)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        path,
        local_files_only=True,
        trust_remote_code=False,
        low_cpu_mem_usage=True,
        device_map={"": 0},
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
    )
    model.eval()
    return tokenizer, model


def strict_prefix_function(tokenizer, regex: str):
    try:
        # lm-format-enforcer 0.11.2 imports this class from the Transformers 4.x
        # module path. Transformers 5 exposes it at package level. The alias is
        # a compatibility shim only; no generation behavior is changed.
        import transformers.tokenization_utils as tokenization_utils

        if not hasattr(tokenization_utils, "PreTrainedTokenizerBase"):
            tokenization_utils.PreTrainedTokenizerBase = transformers.PreTrainedTokenizerBase
        from lmformatenforcer import RegexParser
        from lmformatenforcer.integrations.transformers import (
            build_transformers_prefix_allowed_tokens_fn,
        )
    except ImportError as exc:
        raise SystemExit(
            "lm-format-enforcer is required for primary inference; install the frozen dependency"
        ) from exc
    return build_transformers_prefix_allowed_tokens_fn(
        tokenizer, RegexParser(regex)
    )


def structurally_valid(text: str) -> bool:
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return False
    return (
        isinstance(value, dict)
        and set(value) == {"controller", "nodes", "actions", "final_action"}
        and isinstance(value.get("nodes"), list)
        and isinstance(value.get("actions"), list)
    )


def environment_snapshot(args: argparse.Namespace, tokenizer) -> dict:
    return {
        "python": platform.python_version(),
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "cuda": torch.version.cuda,
        "gpu_name": torch.cuda.get_device_name(0),
        "gpu_visible": os.environ.get("CUDA_VISIBLE_DEVICES"),
        "model_path": str(Path(args.model).resolve()),
        "model_revision": args.model_revision,
        "tokenizer_class": tokenizer.__class__.__name__,
        "chat_template_sha256": stable_hash(tokenizer.chat_template or ""),
        "template_mode": args.template_mode,
        "structured": not args.unconstrained,
        "max_new_tokens": args.max_new_tokens,
        "decoding": "greedy",
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", default="local-unpinned")
    parser.add_argument("--pack", choices=sorted(ALL_PACKS), required=True)
    parser.add_argument("--condition", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-new-tokens", type=int, default=192)
    parser.add_argument("--max-context-tokens", type=int, default=2048)
    parser.add_argument("--template-mode", choices=("native", "plain"), default="native")
    parser.add_argument("--unconstrained", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--ids-file", type=Path)
    parser.add_argument("--reverse-order", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    if args.condition not in ALL_PACKS[args.pack]:
        raise SystemExit(f"condition {args.condition} is not defined in Pack {args.pack}")
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is unavailable")

    records = read_jsonl(args.data)
    if args.ids_file:
        wanted = {line.strip() for line in args.ids_file.read_text(encoding="utf-8").splitlines() if line.strip()}
        records = [record for record in records if record["id"] in wanted]
    if args.reverse_order:
        records.reverse()
    if args.limit is not None:
        records = records[: args.limit]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    done = completed_ids(args.output)
    records = [record for record in records if record["id"] not in done]
    if not records:
        print(json.dumps({"status": "already_complete", "output": str(args.output)}))
        return

    tokenizer, model = load_model(args.model)
    environment = environment_snapshot(args, tokenizer)
    started = time.time()
    torch.cuda.reset_peak_memory_stats()
    generated = 0

    with args.output.open("a", encoding="utf-8", buffering=1, newline="\n") as handle:
        for record in records:
            user_prompt, balance = render_user_prompt(
                record, args.condition, args.pack, tokenizer
            )
            rendered = render_chat(tokenizer, user_prompt, args.template_mode)
            encoded = tokenizer(rendered, return_tensors="pt", add_special_tokens=False)
            input_ids = encoded["input_ids"]
            input_tokens = int(input_ids.shape[1])
            if input_tokens + args.max_new_tokens > args.max_context_tokens:
                raise RuntimeError(
                    f"context limit exceeded for {record['id']}: {input_tokens}+{args.max_new_tokens}"
                )
            encoded = {key: value.to("cuda:0") for key, value in encoded.items()}
            schema = output_schema(record)
            regex = output_regex(record)
            generation_kwargs = {}
            if not args.unconstrained:
                generation_kwargs["prefix_allowed_tokens_fn"] = strict_prefix_function(
                    tokenizer, regex
                )

            item_started = time.time()
            with torch.inference_mode():
                output = model.generate(
                    **encoded,
                    max_new_tokens=args.max_new_tokens,
                    do_sample=False,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id,
                    use_cache=True,
                    **generation_kwargs,
                )
            continuation = output[0, input_tokens:].detach().cpu().tolist()
            text = tokenizer.decode(continuation, skip_special_tokens=True).strip()
            eos_ids = tokenizer.eos_token_id
            eos_set = {eos_ids} if isinstance(eos_ids, int) else set(eos_ids or [])
            ended_eos = bool(continuation and continuation[-1] in eos_set)
            stop_reason = "eos" if ended_eos else (
                "length" if len(continuation) >= args.max_new_tokens else "other"
            )
            result = {
                "id": record["id"],
                "pair_id": record["pair_id"],
                "split": record["split"],
                "model_id": args.model_id,
                "pack": args.pack,
                "condition": args.condition,
                "template_mode": args.template_mode,
                "structured": not args.unconstrained,
                "text": text,
                "structurally_valid": structurally_valid(text),
                "input_tokens": input_tokens,
                "output_tokens": len(continuation),
                "stop_reason": stop_reason,
                "elapsed_seconds": time.time() - item_started,
                "prompt_balance": balance,
                "user_prompt": user_prompt,
                "rendered_prompt": rendered,
                "input_token_ids": input_ids[0].tolist(),
                "output_token_ids": continuation,
                "prompt_sha256": stable_hash(rendered),
                "schema_sha256": stable_hash(schema),
                "regex_sha256": stable_hash(regex),
                "environment": environment,
            }
            handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
            generated += 1
            del encoded, output

    print(
        json.dumps(
            {
                "status": "ok",
                "generated": generated,
                "elapsed_seconds": time.time() - started,
                "model_id": args.model_id,
                "pack": args.pack,
                "condition": args.condition,
                "max_memory_mib": round(torch.cuda.max_memory_allocated() / 2**20, 1),
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
