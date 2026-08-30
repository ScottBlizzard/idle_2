#!/usr/bin/env python3
"""Score frozen GSM8K error traces under one receiver model."""

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

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from experiments.endogenous_failure_conditioning.common import (
    canonical_json,
    read_jsonl,
    sha256_file,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--model-key", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    visible = [x for x in os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",") if x.strip()]
    if len(visible) != 1:
        raise RuntimeError("Exactly one explicitly selected GPU is required")
    config = json.loads(args.config.read_text(encoding="utf-8"))
    spec = config["models"][args.model_key]
    rows = [row for row in read_jsonl(args.bank) if row["domain"] == "gsm8k"]
    if len(rows) != 240:
        raise RuntimeError(f"Expected 240 GSM8K traces, got {len(rows)}")

    completed = set()
    if args.output.exists():
        completed = {row["error_id"] for row in read_jsonl(args.output)}
    pending = [row for row in rows if row["error_id"] not in completed]
    if not pending:
        print("No pending traces")
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
            trace_ids = tokenizer.encode(row["error_response"], add_special_tokens=False)
            all_ids = prefix_ids + trace_ids
            if len(all_ids) > 8192:
                raise RuntimeError(f"Sequence exceeds 8192 tokens: {row['error_id']} {len(all_ids)}")
            input_ids = torch.tensor([all_ids], dtype=torch.long, device="cuda:0")
            attention_mask = torch.ones_like(input_ids)
            with torch.inference_mode():
                logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
                selected = logits[0, len(prefix_ids)-1:-1, :].float()
                targets = input_ids[0, len(prefix_ids):]
                losses = F.cross_entropy(selected, targets, reduction="none")
            total_nll = float(losses.sum().item())
            mean_nll = float(losses.mean().item())
            output = {
                "error_id": row["error_id"],
                "problem_key": row["problem_key"],
                "generator_key": row["generator_key"],
                "generator_family": row["generator_family"],
                "receiver_key": args.model_key,
                "receiver_family": spec["family"],
                "same_lineage": row["generator_family"] == spec["family"],
                "prefix_tokens": len(prefix_ids),
                "trace_tokens": len(trace_ids),
                "total_nll": total_nll,
                "mean_nll": mean_nll,
                "perplexity": float(math.exp(min(mean_nll, 20.0))),
                "model_hf_id": spec["hf_id"],
                "model_revision": spec["revision"],
            }
            handle.write(canonical_json(output) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            del logits, selected, losses, input_ids, attention_mask
            if index % 10 == 0 or index == len(pending):
                print(f"progress model={args.model_key} completed={len(completed)+index}/240", flush=True)

    manifest = {
        "status": "LIKELIHOOD_MODEL_COMPLETE",
        "model_key": args.model_key,
        "model_hf_id": spec["hf_id"],
        "model_revision": spec["revision"],
        "rows": len(completed) + len(pending),
        "elapsed_seconds": time.time() - started,
        "output_sha256": sha256_file(args.output),
        "bank_sha256": sha256_file(args.bank),
        "hostname": platform.node(),
        "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
    }
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

