#!/usr/bin/env python3
"""Run one frozen corrector over every error/wrapper cell, with resumable output."""

from __future__ import annotations

import argparse
import json
import os
import platform
import time
from pathlib import Path
from typing import Any

from common import (
    build_messages,
    canonical_json,
    case_id,
    load_config,
    prompt_payload_hash,
    read_jsonl,
    sha256_file,
)


def existing_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {str(row["case_id"]) for row in read_jsonl(path)}


def build_cases(bank: list[dict[str, Any]], model_key: str, wrappers: list[str]) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for record in bank:
        for wrapper in wrappers:
            cases.append(
                {
                    "case_id": case_id(record["error_id"], model_key, wrapper),
                    "error": record,
                    "wrapper": wrapper,
                    "messages": build_messages(record, wrapper),
                }
            )
    return cases


def vllm_generate(
    model: dict[str, Any], cases: list[dict[str, Any]], max_new_tokens: int
) -> tuple[list[str], list[int], str]:
    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    tokenizer = AutoTokenizer.from_pretrained(model["hf_id"], revision=model["revision"])
    prompts = [
        tokenizer.apply_chat_template(
            case["messages"], tokenize=False, add_generation_prompt=True,
            **model.get("chat_template_kwargs", {}),
        )
        for case in cases
    ]
    engine = LLM(
        model=model["hf_id"],
        revision=model["revision"],
        dtype="half",
        tensor_parallel_size=1,
        trust_remote_code=False,
        max_model_len=8192,
        gpu_memory_utilization=0.90,
    )
    outputs = engine.generate(
        prompts,
        SamplingParams(temperature=0.0, max_tokens=max_new_tokens),
        use_tqdm=True,
    )
    texts = [output.outputs[0].text for output in outputs]
    counts = [len(output.outputs[0].token_ids) for output in outputs]
    return texts, counts, "vllm"


def transformers_generate(
    model_spec: dict[str, Any],
    cases: list[dict[str, Any]],
    max_new_tokens: int,
    batch_size: int,
) -> tuple[list[str], list[int], str]:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        model_spec["hf_id"], revision=model_spec["revision"]
    )
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        model_spec["hf_id"],
        revision=model_spec["revision"],
        torch_dtype=torch.float16,
        device_map={"": 0},
        low_cpu_mem_usage=True,
    ).eval()
    texts: list[str] = []
    counts: list[int] = []
    for start in range(0, len(cases), batch_size):
        batch = cases[start : start + batch_size]
        rendered = [
            tokenizer.apply_chat_template(
                case["messages"], tokenize=False, add_generation_prompt=True,
                **model_spec.get("chat_template_kwargs", {}),
            )
            for case in batch
        ]
        encoded = tokenizer(rendered, return_tensors="pt", padding=True, add_special_tokens=False)
        prompt_length = int(encoded["input_ids"].shape[1])
        if prompt_length + max_new_tokens > 8192:
            raise RuntimeError(f"Prompt overflow: {prompt_length}+{max_new_tokens}>8192")
        encoded = {key: value.to("cuda:0") for key, value in encoded.items()}
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                do_sample=False,
                max_new_tokens=max_new_tokens,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
        for row in generated:
            continuation = row[prompt_length:].tolist()
            if tokenizer.eos_token_id in continuation:
                continuation = continuation[: continuation.index(tokenizer.eos_token_id) + 1]
            texts.append(tokenizer.decode(continuation, skip_special_tokens=True))
            counts.append(len(continuation))
    return texts, counts, "transformers"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--model-key", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--backend", choices=("auto", "vllm", "transformers"), default="auto")
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()

    if "CUDA_VISIBLE_DEVICES" not in os.environ:
        raise RuntimeError("CUDA_VISIBLE_DEVICES must explicitly select one authorized GPU")
    visible = [value for value in os.environ["CUDA_VISIBLE_DEVICES"].split(",") if value.strip()]
    if len(visible) != 1:
        raise RuntimeError("Exactly one physical GPU must be visible to each corrector")

    config = load_config(args.config)
    if args.model_key not in config["models"]:
        raise KeyError(args.model_key)
    model_spec = config["models"][args.model_key]
    bank = list(read_jsonl(args.bank))
    cases = build_cases(bank, args.model_key, list(config["wrappers"]))
    completed = existing_ids(args.output)
    cases = [case for case in cases if case["case_id"] not in completed]
    if args.limit is not None:
        cases = cases[: args.limit]
    if not cases:
        print("No pending cases")
        return

    started = time.time()
    backend = args.backend
    if backend == "auto":
        try:
            import vllm  # noqa: F401

            backend = "vllm"
        except ImportError:
            backend = "transformers"
    if backend == "vllm":
        texts, token_counts, resolved_backend = vllm_generate(
            model_spec, cases, int(config["max_new_tokens"])
        )
    else:
        texts, token_counts, resolved_backend = transformers_generate(
            model_spec,
            cases,
            int(config["max_new_tokens"]),
            int(args.batch_size),
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8", newline="\n") as handle:
        for case, text, token_count in zip(cases, texts, token_counts):
            error = case["error"]
            row = {
                "case_id": case["case_id"],
                "error_id": error["error_id"],
                "domain": error["domain"],
                "problem_key": error["problem_key"],
                "generator_key": error["generator_key"],
                "generator_family": error["generator_family"],
                "corrector_key": args.model_key,
                "corrector_family": model_spec["family"],
                "corrector_size_rank": model_spec["size_rank"],
                "wrapper": case["wrapper"],
                "prompt_payload_sha256": prompt_payload_hash(error, case["wrapper"]),
                "response": text,
                "generated_tokens": token_count,
                "hit_token_limit": token_count >= int(config["max_new_tokens"]),
                "backend": resolved_backend,
                "model_hf_id": model_spec["hf_id"],
                "model_revision": model_spec["revision"],
            }
            handle.write(canonical_json(row) + "\n")
            handle.flush()
            os.fsync(handle.fileno())

    manifest = {
        "status": "CORRECTOR_PART_COMPLETE" if args.limit else "CORRECTOR_COMPLETE",
        "model_key": args.model_key,
        "model_hf_id": model_spec["hf_id"],
        "model_revision": model_spec["revision"],
        "backend": resolved_backend,
        "new_cases": len(cases),
        "total_cases": len(completed) + len(cases),
        "elapsed_seconds": time.time() - started,
        "output_sha256": sha256_file(args.output),
        "hostname": platform.node(),
        "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
    }
    manifest_path = args.output.with_suffix(".manifest.json")
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
