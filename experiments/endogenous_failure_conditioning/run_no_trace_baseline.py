#!/usr/bin/env python3
"""Run the frozen no-trace GSM8K baseline for one corrector."""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import canonical_json, read_jsonl, sha256_file, sha256_text
from run_corrector import transformers_generate_batches


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--model-key", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--parent-config", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    args = parser.parse_args()

    visible = [x for x in os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",") if x.strip()]
    if len(visible) != 1:
        raise RuntimeError("Exactly one explicitly selected GPU is required")

    parent = json.loads(args.parent_config.read_text(encoding="utf-8"))
    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    if sha256_file(args.bank) != frozen["error_bank_sha256"]:
        raise RuntimeError("Frozen error-bank hash mismatch")
    if args.model_key not in parent["models"]:
        raise KeyError(args.model_key)
    model_spec = parent["models"][args.model_key]

    by_problem = {}
    for row in read_jsonl(args.bank):
        if row["domain"] != frozen["domain"]:
            continue
        by_problem.setdefault(row["problem_key"], row)
    if len(by_problem) != frozen["problem_count"]:
        raise RuntimeError(f"Expected {frozen['problem_count']} problems, got {len(by_problem)}")

    completed = set()
    if args.output.exists():
        completed = {row["case_id"] for row in read_jsonl(args.output)}
    cases = []
    for problem_key, row in sorted(by_problem.items()):
        case_id = sha256_text(canonical_json(["no_trace", args.model_key, problem_key]))
        if case_id in completed:
            continue
        user = frozen["user_template"].format(question=row["question"])
        cases.append({
            "case_id": case_id,
            "problem_key": problem_key,
            "question": row["question"],
            "gold_answer": row["gold_answer"],
            "messages": [
                {"role": "system", "content": frozen["system_prompt"]},
                {"role": "user", "content": user},
            ],
        })
    if not cases:
        print("No pending cases")
        return

    started = time.time()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    processed = 0
    with args.output.open("a", encoding="utf-8", newline="\n") as handle:
        for batch, texts, token_counts in transformers_generate_batches(
            model_spec, cases, int(frozen["max_new_tokens"]), args.batch_size
        ):
            for case, text, token_count in zip(batch, texts, token_counts):
                row = {
                    "case_id": case["case_id"],
                    "condition": "no_trace",
                    "problem_key": case["problem_key"],
                    "question_sha256": sha256_text(case["question"]),
                    "gold_answer": case["gold_answer"],
                    "corrector_key": args.model_key,
                    "corrector_family": model_spec["family"],
                    "model_hf_id": model_spec["hf_id"],
                    "model_revision": model_spec["revision"],
                    "response": text,
                    "generated_tokens": token_count,
                    "hit_token_limit": token_count >= int(frozen["max_new_tokens"]),
                    "prompt_sha256": sha256_text(canonical_json(case["messages"])),
                }
                handle.write(canonical_json(row) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            processed += len(batch)
            print(f"progress model={args.model_key} completed={len(completed)+processed}/60", flush=True)

    manifest = {
        "status": "NO_TRACE_MODEL_COMPLETE",
        "model_key": args.model_key,
        "model_hf_id": model_spec["hf_id"],
        "model_revision": model_spec["revision"],
        "new_cases": len(cases),
        "total_cases": len(completed) + len(cases),
        "elapsed_seconds": time.time() - started,
        "output_sha256": sha256_file(args.output),
        "hostname": platform.node(),
        "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
    }
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

