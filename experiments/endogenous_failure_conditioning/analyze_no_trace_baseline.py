#!/usr/bin/env python3
"""Apply the frozen no-trace baseline gate without altering the parent pilot."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import read_jsonl, sha256_file
from experiments.moe_route_noncompositionality.stage_d_common import verify_gsm8k


def mean(rows: list[dict[str, Any]], key: str, same: bool) -> float:
    values = [float(row[key]) for row in rows if row["same_lineage"] is same]
    return float(np.mean(values)) if values else float("nan")


def contrast(rows: list[dict[str, Any]], key: str) -> float:
    return mean(rows, key, True) - mean(rows, key, False)


def clustered_ci(
    rows: list[dict[str, Any]], key: str, repetitions: int, seed: int
) -> tuple[float, list[float]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row["problem_key"]].append(row)
    keys = sorted(groups)
    point = contrast(rows, key)
    rng = np.random.default_rng(seed)
    draws = []
    for _ in range(repetitions):
        sampled = rng.choice(keys, size=len(keys), replace=True)
        replicate = [row for problem in sampled for row in groups[str(problem)]]
        draws.append(contrast(replicate, key))
    low, high = np.quantile(draws, [0.025, 0.975])
    return point, [float(low), float(high)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--baseline-dir", type=Path, required=True)
    parser.add_argument("--parent-scored", type=Path, required=True)
    parser.add_argument("--parent-config", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    parent = json.loads(args.parent_config.read_text(encoding="utf-8"))
    if sha256_file(args.bank) != frozen["error_bank_sha256"]:
        raise RuntimeError("Error-bank hash mismatch")
    if sha256_file(args.parent_scored) != frozen["parent_scored_matrix_sha256"]:
        raise RuntimeError("Parent scored-matrix hash mismatch")

    baseline = []
    for model_key, spec in parent["models"].items():
        path = args.baseline_dir / "outputs" / f"{model_key}.jsonl"
        manifest_path = path.with_suffix(".manifest.json")
        if not path.exists() or not manifest_path.exists():
            raise RuntimeError(f"Incomplete baseline output for {model_key}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest["status"] != "NO_TRACE_MODEL_COMPLETE" or manifest["total_cases"] != 60:
            raise RuntimeError(f"Invalid manifest for {model_key}: {manifest}")
        if manifest["model_revision"] != spec["revision"]:
            raise RuntimeError(f"Revision mismatch for {model_key}")
        if sha256_file(path) != manifest["output_sha256"]:
            raise RuntimeError(f"Output hash mismatch for {model_key}")
        baseline.extend(read_jsonl(path))
    if len(baseline) != frozen["call_count"]:
        raise RuntimeError(f"Expected {frozen['call_count']} baseline rows, got {len(baseline)}")

    baseline_map = {}
    baseline_bad = 0
    scored_baseline = []
    for row in baseline:
        correct, extracted = verify_gsm8k(row["response"], row["gold_answer"])
        parsed = extracted is not None
        bad = (not parsed) or bool(row["hit_token_limit"])
        baseline_bad += int(bad)
        key = (row["corrector_key"], row["problem_key"])
        if key in baseline_map:
            raise RuntimeError(f"Duplicate baseline pair: {key}")
        item = {
            **row,
            "correct": bool(correct),
            "parsed": parsed,
            "extracted_answer": None if extracted is None else extracted.value,
            "bad_parse_or_truncation": bad,
        }
        baseline_map[key] = item
        scored_baseline.append(item)

    bank = {row["error_id"]: row for row in read_jsonl(args.bank) if row["domain"] == "gsm8k"}
    exposed = []
    for row in read_jsonl(args.parent_scored):
        if row["domain"] != "gsm8k":
            continue
        base = baseline_map[(row["corrector_key"], row["problem_key"])]
        source_answers = {str(value) for value in bank[row["error_id"]]["source_extracted_answer"]}
        exposed.append({
            **row,
            "baseline_correct": base["correct"],
            "same_lineage": row["generator_family"] == row["corrector_family"],
            "damage": not bool(row["correct"]),
            "retained_source_error": row.get("extracted_answer") in source_answers,
        })
    if len(exposed) != 1920:
        raise RuntimeError(f"Expected 1920 GSM8K exposed rows, got {len(exposed)}")

    solvable_pairs = sum(int(row["correct"]) for row in scored_baseline)
    by_wrapper = {}
    for wrapper in ("external_neutral", "assistant_history"):
        subset = [
            row for row in exposed
            if row["wrapper"] == wrapper and row["baseline_correct"]
        ]
        wrapper_result = {"n": len(subset), "baseline_solvable_pairs": solvable_pairs}
        for key in ("damage", "retained_source_error"):
            point, ci = clustered_ci(
                subset, key, int(frozen["bootstrap_repetitions"]), int(frozen["seed"])
            )
            wrapper_result[key] = {
                "same_lineage": mean(subset, key, True),
                "cross_lineage": mean(subset, key, False),
                "same_minus_cross": point,
                "ci95": ci,
            }
        by_wrapper[wrapper] = wrapper_result

    bad_rate = baseline_bad / len(scored_baseline)
    external = by_wrapper["external_neutral"]
    assistant = by_wrapper["assistant_history"]
    if bad_rate > frozen["maximum_parser_or_truncation_rate"] or solvable_pairs < frozen["minimum_baseline_solvable_pairs"]:
        decision = "NO_GO_ENGINEERING"
    elif (
        external["damage"]["same_minus_cross"] < frozen["minimum_excess_damage"]
        or external["damage"]["ci95"][0] <= 0
    ):
        decision = "KILL_SHARED_BLIND_SPOTS"
    elif (
        external["retained_source_error"]["same_minus_cross"] < frozen["minimum_excess_retention"]
        or external["retained_source_error"]["ci95"][0] <= 0
    ):
        decision = "KILL_NO_ATTRACTOR_RETENTION"
    elif assistant["damage"]["same_minus_cross"] <= 0:
        decision = "KILL_NOT_ROLE_ROBUST"
    else:
        decision = "ADVANCE_STYLE_CONTENT_SEPARATION"

    result = {
        "status": decision,
        "scope": "POST_HOC_NEW_EXPERIMENT_DOES_NOT_CHANGE_PARENT_GATE",
        "parent_gate": "KILL_NO_SELECTION_REVERSAL",
        "baseline_rows": len(scored_baseline),
        "baseline_solvable_pairs": solvable_pairs,
        "baseline_parse_or_truncation_rate": bad_rate,
        "by_wrapper": by_wrapper,
        "input_hashes": {
            "error_bank": sha256_file(args.bank),
            "parent_scored_matrix": sha256_file(args.parent_scored),
            "frozen_protocol": sha256_file(args.frozen),
        },
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "BASELINE_SCORED.jsonl").write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in scored_baseline),
        encoding="utf-8",
    )
    (args.output_dir / "FINAL_GATE.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

