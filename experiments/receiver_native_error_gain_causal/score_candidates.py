#!/usr/bin/env python3
"""Score whitespace rendering candidates under one frozen receiver."""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import sys
import time
from pathlib import Path

import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.endogenous_failure_conditioning.common import (
    canonical_json,
    read_jsonl,
    sha256_file,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", type=Path, required=True)
    parser.add_argument("--parent-config", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    parser.add_argument("--model-key", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    visible = [x for x in os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",") if x.strip()]
    if len(visible) != 1:
        raise RuntimeError("Exactly one explicitly selected GPU is required")
    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    parent = json.loads(args.parent_config.read_text(encoding="utf-8"))
    if sha256_file(args.parent_config) != frozen["parent_config_sha256"]:
        raise RuntimeError("Parent-config hash mismatch")
    library_manifest_path = args.library.with_suffix(".manifest.json")
    library_manifest = json.loads(library_manifest_path.read_text(encoding="utf-8"))
    if sha256_file(args.library) != library_manifest["output_sha256"]:
        raise RuntimeError("Candidate-library hash mismatch")
    if library_manifest["source_trace_count"] != frozen["expected_source_traces"]:
        raise RuntimeError("Unexpected source-trace count")
    if args.model_key not in parent["models"]:
        raise KeyError(args.model_key)
    spec = parent["models"][args.model_key]
    candidates = list(read_jsonl(args.library))

    completed = set()
    if args.output.exists():
        completed = {str(row["candidate_id"]) for row in read_jsonl(args.output)}
    pending = [row for row in candidates if str(row["candidate_id"]) not in completed]
    if not pending:
        print("No pending candidates")
        return

    tokenizer = AutoTokenizer.from_pretrained(spec["hf_id"], revision=spec["revision"])
    model = AutoModelForCausalLM.from_pretrained(
        spec["hf_id"], revision=spec["revision"], torch_dtype=torch.float16,
        device_map={"": 0}, low_cpu_mem_usage=True,
    ).eval()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    with args.output.open("a", encoding="utf-8", newline="\n") as handle:
        for index, row in enumerate(pending, 1):
            prefix = f"Problem:\n{row['question']}\n\nProposed solution:\n"
            prefix_ids = tokenizer.encode(prefix, add_special_tokens=False)
            trace_ids = tokenizer.encode(row["rendered_trace"], add_special_tokens=False)
            all_ids = prefix_ids + trace_ids
            if len(all_ids) > 8192:
                raise RuntimeError(f"Sequence exceeds 8192 tokens: {row['candidate_id']}")
            input_ids = torch.tensor([all_ids], dtype=torch.long, device="cuda:0")
            attention_mask = torch.ones_like(input_ids)
            with torch.inference_mode():
                logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
                selected = logits[0, len(prefix_ids)-1:-1, :].float()
                targets = input_ids[0, len(prefix_ids):]
                losses = F.cross_entropy(selected, targets, reduction="none")
            mean_nll = float(losses.mean().item())
            output = {
                "candidate_id": row["candidate_id"],
                "error_id": row["error_id"],
                "problem_key": row["problem_key"],
                "variant_id": row["variant_id"],
                "rendered_sha256": row["rendered_sha256"],
                "non_whitespace_sha256": row["non_whitespace_sha256"],
                "receiver_key": args.model_key,
                "receiver_family": spec["family"],
                "trace_tokens": len(trace_ids),
                "total_nll": float(losses.sum().item()),
                "mean_nll": mean_nll,
                "perplexity": float(math.exp(min(mean_nll, 20.0))),
                "model_hf_id": spec["hf_id"],
                "model_revision": spec["revision"],
            }
            handle.write(canonical_json(output) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            del logits, selected, losses, input_ids, attention_mask
            if index % 25 == 0 or index == len(pending):
                print(
                    f"progress model={args.model_key} "
                    f"completed={len(completed)+index}/{len(candidates)}", flush=True
                )

    manifest = {
        "status": "CANDIDATE_LIKELIHOOD_MODEL_COMPLETE",
        "model_key": args.model_key,
        "model_hf_id": spec["hf_id"],
        "model_revision": spec["revision"],
        "rows": len(completed) + len(pending),
        "elapsed_seconds": time.time() - started,
        "output_sha256": sha256_file(args.output),
        "library_sha256": sha256_file(args.library),
        "hostname": platform.node(),
        "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
    }
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

