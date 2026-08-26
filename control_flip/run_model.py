from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Iterable, Sequence

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


PROMPT_SUFFIXES = {
    "direct": (
        "\n\nReturn only one line in the exact form `FINAL: ACTION`, replacing ACTION with "
        "one of the two root-action names."
    ),
    "cot": (
        "\n\nSolve with a compact scratchpad, not prose. Write one short line per chance "
        "outcome stating MAX or MIN and the selected value; then one line containing only the "
        "probability-weighted branching calculation; then one comparison line; then end with "
        "`FINAL: ACTION`. Do not restate the problem and do not exceed 120 words."
    ),
    "bellman": (
        "\n\nUse this Bellman scaffold explicitly: at a successor controlled by you, replace "
        "its listed utilities by their MAXIMUM; at a successor controlled by the adversary, "
        "replace them by their MINIMUM. Probability-weight those selected values, subtract "
        "the one-time cost, and compare against the immediate utility. Show the calculation "
        "and end with one line in the exact form `FINAL: ACTION`. Be concise: use at most six short "
        "lines and 120 words."
    ),
}


def prompt_suffix(mode: str, controller: str) -> str:
    if mode not in {"local_operator", "positive_operator"}:
        return PROMPT_SUFFIXES[mode]
    if controller == "self":
        operator, actor, forbidden = "MAXIMUM", "you control every continuation", "MINIMUM"
    else:
        operator, actor, forbidden = "MINIMUM", "the adversary controls every continuation", "MAXIMUM"
    if mode == "positive_operator":
        return (
            f"\n\nIn this problem, {actor}. At EVERY chance outcome, select the {operator} of "
            "the listed utilities. Write one short line per outcome, one probability-weighted "
            "calculation line, one comparison line, and end with `FINAL: ACTION`. Do not restate "
            "the problem."
        )
    return (
        f"\n\nIn this problem, {actor}. Therefore apply the {operator} to the listed utilities "
        f"at EVERY chance outcome; never apply the {forbidden}. Write one short line per outcome, "
        "one probability-weighted calculation line, one comparison line, and end with "
        "`FINAL: ACTION`. Do not restate the problem."
    )


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    ids: set[str] = set()
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                ids.add(json.loads(line)["id"])
            except (json.JSONDecodeError, KeyError):
                continue
    return ids


def batched(items: list[dict], size: int) -> Iterable[list[dict]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def apply_chat_template(tokenizer, prompt: str, thinking: bool) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a careful decision analyst. All utilities are from the focal agent's "
                "perspective. Follow the stated move order exactly."
            ),
        },
        {"role": "user", "content": prompt},
    ]
    kwargs = dict(tokenize=False, add_generation_prompt=True)
    try:
        return tokenizer.apply_chat_template(messages, enable_thinking=thinking, **kwargs)
    except TypeError:
        return tokenizer.apply_chat_template(messages, **kwargs)


def load_model(model_path: str):
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        local_files_only=True,
        trust_remote_code=False,
    )
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"
    config_path = Path(model_path) / "config.json"
    quantized = False
    if config_path.exists():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        quantized = bool(config.get("quantization_config"))
    kwargs = dict(
        local_files_only=True,
        trust_remote_code=False,
        low_cpu_mem_usage=True,
        device_map={"": 0},
    )
    if not quantized:
        kwargs["dtype"] = torch.bfloat16
        kwargs["attn_implementation"] = "sdpa"
    model = AutoModelForCausalLM.from_pretrained(model_path, **kwargs)
    model.eval()
    return tokenizer, model


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument(
        "--prompt-mode",
        choices=sorted([*PROMPT_SUFFIXES, "local_operator", "positive_operator"]),
        required=True,
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--max-new-tokens", type=int)
    parser.add_argument("--thinking", action="store_true")
    parser.add_argument("--limit", type=int)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is unavailable")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    done = completed_ids(args.output)
    records = [record for record in read_jsonl(args.data) if record["id"] not in done]
    if args.limit is not None:
        records = records[: args.limit]
    if not records:
        print(json.dumps({"status": "already_complete", "output": str(args.output)}))
        return

    tokenizer, model = load_model(args.model)
    max_new_tokens = args.max_new_tokens
    if max_new_tokens is None:
        max_new_tokens = 48 if args.prompt_mode == "direct" else 384
    started = time.time()
    generated_count = 0

    with args.output.open("a", encoding="utf-8", buffering=1) as handle:
        for batch in batched(records, args.batch_size):
            prompts = [
                apply_chat_template(
                    tokenizer,
                    record["prompt"] + prompt_suffix(args.prompt_mode, record["controller"]),
                    thinking=args.thinking,
                )
                for record in batch
            ]
            inputs = tokenizer(prompts, return_tensors="pt", padding=True).to("cuda:0")
            batch_started = time.time()
            with torch.inference_mode():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id,
                    use_cache=True,
                )
            input_width = inputs["input_ids"].shape[1]
            decoded = tokenizer.batch_decode(outputs[:, input_width:], skip_special_tokens=True)
            elapsed = time.time() - batch_started
            for record, text in zip(batch, decoded):
                result = {
                    "id": record["id"],
                    "pair_id": record["pair_id"],
                    "controller": record["controller"],
                    "model_id": args.model_id,
                    "model_path": args.model,
                    "prompt_mode": args.prompt_mode + ("_thinking" if args.thinking else ""),
                    "text": text.strip(),
                    "batch_seconds": elapsed,
                    "generated_tokens": len(tokenizer.encode(text, add_special_tokens=False)),
                }
                handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
                generated_count += 1
            del inputs, outputs

    print(
        json.dumps(
            {
                "status": "ok",
                "generated": generated_count,
                "elapsed_seconds": time.time() - started,
                "model_id": args.model_id,
                "prompt_mode": args.prompt_mode,
                "output": str(args.output),
                "max_memory_mib": round(torch.cuda.max_memory_allocated() / 2**20, 1),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
