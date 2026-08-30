#!/usr/bin/env python3
"""Build the frozen outcome-blind whitespace candidate library."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.endogenous_failure_conditioning.common import (
    canonical_json,
    read_jsonl,
    sha256_file,
    sha256_text,
    write_jsonl,
)
from experiments.receiver_native_error_gain_causal.rendering import (
    non_whitespace,
    render_variants,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    frozen = json.loads(args.config.read_text(encoding="utf-8"))
    if sha256_file(args.bank) != frozen["error_bank_sha256"]:
        raise RuntimeError("Frozen error-bank hash mismatch")
    source = [row for row in read_jsonl(args.bank) if row["domain"] == frozen["domain"]]
    problem_keys = sorted(
        {str(row["problem_key"]) for row in source}, key=lambda key: (sha256_text(key), key)
    )[: int(frozen["problem_count"])]
    selected = [row for row in source if str(row["problem_key"]) in set(problem_keys)]
    if len(selected) != int(frozen["expected_source_traces"]):
        raise RuntimeError(f"Expected 120 selected traces, got {len(selected)}")

    output = []
    unique_counts = {}
    for row in sorted(selected, key=lambda item: str(item["error_id"])):
        variants = render_variants(str(row["error_response"]))
        unique_counts[str(row["error_id"])] = len(variants)
        for variant in variants:
            rendered = variant["rendered_trace"]
            output.append({
                "candidate_id": sha256_text(canonical_json([
                    row["error_id"], variant["variant_id"], sha256_text(rendered)
                ])),
                "error_id": row["error_id"],
                "problem_key": row["problem_key"],
                "generator_key": row["generator_key"],
                "generator_family": row["generator_family"],
                "question": row["question"],
                "gold_answer": row["gold_answer"],
                "source_extracted_answer": row["source_extracted_answer"],
                "variant_id": variant["variant_id"],
                "rendered_trace": rendered,
                "rendered_sha256": sha256_text(rendered),
                "non_whitespace_sha256": sha256_text(non_whitespace(rendered)),
            })
    write_jsonl(args.output, output)
    manifest = {
        "status": "CANDIDATE_LIBRARY_COMPLETE",
        "selected_problem_keys": problem_keys,
        "problem_count": len(problem_keys),
        "source_trace_count": len(selected),
        "candidate_count": len(output),
        "minimum_unique_candidates": min(unique_counts.values()),
        "maximum_unique_candidates": max(unique_counts.values()),
        "output_sha256": sha256_file(args.output),
        "bank_sha256": sha256_file(args.bank),
        "config_sha256": sha256_file(args.config),
    }
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
