#!/usr/bin/env python3
"""Apply the frozen outcome-blind manipulation gate and select treatment pairs."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np

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
from experiments.receiver_native_error_gain_causal.rendering import non_whitespace


def choose_pair(rows: list[dict[str, Any]], maximum_token_delta: int):
    eligible = []
    for index, left in enumerate(rows):
        for right in rows[index + 1:]:
            token_delta = abs(int(left["trace_tokens"]) - int(right["trace_tokens"]))
            if token_delta > maximum_token_delta:
                continue
            if float(left["mean_nll"]) <= float(right["mean_nll"]):
                low, high = left, right
            else:
                low, high = right, left
            gap = float(high["mean_nll"]) - float(low["mean_nll"])
            eligible.append((gap, str(low["variant_id"]), str(high["variant_id"]), low, high))
    if not eligible:
        return None
    eligible.sort(key=lambda item: (-item[0], item[1], item[2]))
    return eligible[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", type=Path, required=True)
    parser.add_argument("--scores-dir", type=Path, required=True)
    parser.add_argument("--parent-config", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--gate", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.gate.exists():
        raise RuntimeError("Refusing to overwrite an existing manipulation result")

    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    parent = json.loads(args.parent_config.read_text(encoding="utf-8"))
    library_manifest = json.loads(
        args.library.with_suffix(".manifest.json").read_text(encoding="utf-8")
    )
    if sha256_file(args.library) != library_manifest["output_sha256"]:
        raise RuntimeError("Candidate-library hash mismatch")
    library_rows = list(read_jsonl(args.library))
    library = {str(row["candidate_id"]): row for row in library_rows}

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    score_hashes = {}
    for model_key, spec in parent["models"].items():
        path = args.scores_dir / "outputs" / f"{model_key}.jsonl"
        manifest = json.loads(path.with_suffix(".manifest.json").read_text(encoding="utf-8"))
        if manifest["status"] != "CANDIDATE_LIKELIHOOD_MODEL_COMPLETE":
            raise RuntimeError(f"Incomplete score manifest for {model_key}")
        if manifest["model_revision"] != spec["revision"]:
            raise RuntimeError(f"Revision mismatch for {model_key}")
        if manifest["rows"] != len(library_rows) or sha256_file(path) != manifest["output_sha256"]:
            raise RuntimeError(f"Score count/hash mismatch for {model_key}")
        score_hashes[model_key] = manifest["output_sha256"]
        for row in read_jsonl(path):
            grouped[(str(row["error_id"]), model_key)].append(row)

    selected = []
    missing = []
    maximum_delta = int(frozen["maximum_selected_token_delta"])
    for error_id in sorted({str(row["error_id"]) for row in library_rows}):
        for receiver_key in sorted(parent["models"]):
            pair = choose_pair(grouped[(error_id, receiver_key)], maximum_delta)
            if pair is None:
                missing.append([error_id, receiver_key])
                continue
            gap, _, _, high_native, low_native = pair
            high_record = library[str(high_native["candidate_id"])]
            low_record = library[str(low_native["candidate_id"])]
            if high_record["non_whitespace_sha256"] != low_record["non_whitespace_sha256"]:
                raise RuntimeError("Selected pair violates non-whitespace hash identity")
            if non_whitespace(high_record["rendered_trace"]) != non_whitespace(low_record["rendered_trace"]):
                raise RuntimeError("Selected pair violates non-whitespace text identity")
            selected.append({
                "pair_id": sha256_text(canonical_json([error_id, receiver_key, "whitespace_v1"])),
                "error_id": error_id,
                "problem_key": high_record["problem_key"],
                "generator_key": high_record["generator_key"],
                "generator_family": high_record["generator_family"],
                "receiver_key": receiver_key,
                "receiver_family": parent["models"][receiver_key]["family"],
                "question": high_record["question"],
                "gold_answer": high_record["gold_answer"],
                "source_extracted_answer": high_record["source_extracted_answer"],
                "non_whitespace_sha256": high_record["non_whitespace_sha256"],
                "nll_gap_low_minus_high_native": float(gap),
                "selected_token_delta": abs(
                    int(high_native["trace_tokens"]) - int(low_native["trace_tokens"])
                ),
                "high_native": {
                    "candidate_id": high_native["candidate_id"],
                    "variant_id": high_native["variant_id"],
                    "rendered_trace": high_record["rendered_trace"],
                    "rendered_sha256": high_record["rendered_sha256"],
                    "mean_nll": float(high_native["mean_nll"]),
                    "trace_tokens": int(high_native["trace_tokens"]),
                },
                "low_native": {
                    "candidate_id": low_native["candidate_id"],
                    "variant_id": low_native["variant_id"],
                    "rendered_trace": low_record["rendered_trace"],
                    "rendered_sha256": low_record["rendered_sha256"],
                    "mean_nll": float(low_native["mean_nll"]),
                    "trace_tokens": int(low_native["trace_tokens"]),
                },
            })

    gaps = np.array([float(row["nll_gap_low_minus_high_native"]) for row in selected])
    conditions = {
        "all_cells_selected": len(selected) == int(frozen["expected_selected_cells"]),
        "no_missing_pairs": not missing,
        "candidate_minimum_pass": (
            int(library_manifest["minimum_unique_candidates"])
            >= int(frozen["minimum_unique_candidates"])
        ),
        "median_gap_pass": bool(
            len(gaps) and np.median(gaps) >= float(frozen["minimum_median_nll_gap"])
        ),
        "fraction_gap_pass": bool(
            len(gaps) and np.mean(gaps >= 0.05) >= float(frozen["minimum_fraction_gap_005"])
        ),
        "token_delta_pass": all(
            int(row["selected_token_delta"]) <= maximum_delta for row in selected
        ),
    }
    passed = all(conditions.values())
    write_jsonl(args.output, selected)
    gate = {
        "status": "MANIPULATION_PASS_AUTHORIZE_CORRECTION" if passed else "KILL_INSUFFICIENT_WHITESPACE_ACTUATION",
        "conditions": conditions,
        "selected_cells": len(selected),
        "missing_pairs": missing,
        "median_nll_gap": None if not len(gaps) else float(np.median(gaps)),
        "fraction_gap_at_least_005": None if not len(gaps) else float(np.mean(gaps >= 0.05)),
        "minimum_nll_gap": None if not len(gaps) else float(np.min(gaps)),
        "maximum_nll_gap": None if not len(gaps) else float(np.max(gaps)),
        "input_hashes": {
            "frozen": sha256_file(args.frozen),
            "library": sha256_file(args.library),
            "score_outputs": score_hashes,
        },
        "selected_sha256": sha256_file(args.output),
    }
    args.gate.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(gate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
