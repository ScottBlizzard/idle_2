#!/usr/bin/env python3
"""Run the frozen high-native/low-native correction pair for one receiver."""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EF_ROOT = REPO_ROOT / "experiments" / "endogenous_failure_conditioning"
for path in (str(REPO_ROOT), str(EF_ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from common import SYSTEM_PROMPT, canonical_json, read_jsonl, sha256_file, sha256_text
from run_corrector import transformers_generate_batches


def build_messages(question: str, trace: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "Problem:\n" + question + "\n\n"
                "Proposed solution from an unspecified source:\n" + trace + "\n\n"
                "Check the proposed solution, repair every error you find, and give "
                "the final answer in the required format."
            ),
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=Path, required=True)
    parser.add_argument("--manipulation-gate", type=Path, required=True)
    parser.add_argument("--parent-config", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    parser.add_argument("--model-key", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=2)
    args = parser.parse_args()

    visible = [x for x in os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",") if x.strip()]
    if len(visible) != 1:
        raise RuntimeError("Exactly one explicitly selected GPU is required")
    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    parent = json.loads(args.parent_config.read_text(encoding="utf-8"))
    gate = json.loads(args.manipulation_gate.read_text(encoding="utf-8"))
    if gate["status"] != "MANIPULATION_PASS_AUTHORIZE_CORRECTION":
        raise RuntimeError(f"Correction is unauthorized: {gate['status']}")
    if sha256_file(args.selected) != gate["selected_sha256"]:
        raise RuntimeError("Selected-pair hash mismatch")
    if args.model_key not in parent["models"]:
        raise KeyError(args.model_key)
    spec = parent["models"][args.model_key]

    completed = set()
    if args.output.exists():
        completed = {str(row["case_id"]) for row in read_jsonl(args.output)}
    cases = []
    selected_pairs = 0
    for pair in read_jsonl(args.selected):
        if pair["receiver_key"] != args.model_key:
            continue
        selected_pairs += 1
        for condition in ("high_native", "low_native"):
            variant = pair[condition]
            case_id = sha256_text(canonical_json([pair["pair_id"], condition]))
            if case_id in completed:
                continue
            messages = build_messages(str(pair["question"]), str(variant["rendered_trace"]))
            cases.append({
                "case_id": case_id,
                "pair": pair,
                "condition": condition,
                "variant": variant,
                "messages": messages,
            })
    expected_pairs = int(frozen["expected_selected_cells"]) // int(frozen["expected_receivers"])
    if selected_pairs != expected_pairs:
        raise RuntimeError(f"Expected {expected_pairs} selected pairs, got {selected_pairs}")
    if not cases:
        print("No pending correction cases")
        return

    args.output.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    processed = 0
    with args.output.open("a", encoding="utf-8", newline="\n") as handle:
        for batch, texts, token_counts in transformers_generate_batches(
            spec, cases, int(frozen["max_new_tokens"]), int(args.batch_size)
        ):
            for case, text, token_count in zip(batch, texts, token_counts):
                pair = case["pair"]
                variant = case["variant"]
                row = {
                    "case_id": case["case_id"],
                    "pair_id": pair["pair_id"],
                    "error_id": pair["error_id"],
                    "problem_key": pair["problem_key"],
                    "generator_key": pair["generator_key"],
                    "generator_family": pair["generator_family"],
                    "corrector_key": args.model_key,
                    "corrector_family": spec["family"],
                    "condition": case["condition"],
                    "candidate_id": variant["candidate_id"],
                    "variant_id": variant["variant_id"],
                    "rendered_sha256": variant["rendered_sha256"],
                    "mean_nll": variant["mean_nll"],
                    "trace_tokens": variant["trace_tokens"],
                    "response": text,
                    "generated_tokens": token_count,
                    "hit_token_limit": token_count >= int(frozen["max_new_tokens"]),
                    "prompt_sha256": sha256_text(canonical_json(case["messages"])),
                    "model_hf_id": spec["hf_id"],
                    "model_revision": spec["revision"],
                }
                handle.write(canonical_json(row) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            processed += len(batch)
            print(
                f"progress model={args.model_key} "
                f"completed={len(completed)+processed}/{selected_pairs*2}", flush=True
            )

    manifest = {
        "status": "CAUSAL_CORRECTION_MODEL_COMPLETE",
        "model_key": args.model_key,
        "model_hf_id": spec["hf_id"],
        "model_revision": spec["revision"],
        "total_cases": len(completed) + len(cases),
        "new_cases": len(cases),
        "elapsed_seconds": time.time() - started,
        "output_sha256": sha256_file(args.output),
        "selected_sha256": sha256_file(args.selected),
        "hostname": platform.node(),
        "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
    }
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

