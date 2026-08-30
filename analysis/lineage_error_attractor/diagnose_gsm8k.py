#!/usr/bin/env python3
"""Post-hoc GSM8K diagnosis of lineage-conditioned wrong-answer retention."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from experiments.moe_route_noncompositionality.stage_d_common import (  # noqa: E402
    extract_gsm8k_prediction,
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def classify(row: dict[str, Any], source_answer: str) -> str:
    if not row["parsed"]:
        return "unparsed"
    if row["correct"]:
        return "correct"
    if str(row["extracted_answer"]) == source_answer:
        return "retained_source_error"
    return "changed_to_other_wrong"


def rates(rows: list[dict[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["outcome"]] += 1
    n = len(rows)
    changed = counts["correct"] + counts["changed_to_other_wrong"]
    return {
        "n": n,
        "accuracy": counts["correct"] / n,
        "source_error_retention": counts["retained_source_error"] / n,
        "changed_answer": changed / n,
        "accuracy_given_changed": counts["correct"] / changed if changed else None,
        "counts": dict(sorted(counts.items())),
    }


def paired_contrast(rows: list[dict[str, Any]], metric: str) -> float:
    same = [row[metric] for row in rows if row["relation"] == "same_lineage"]
    cross = [row[metric] for row in rows if row["relation"] == "cross_lineage"]
    return float(np.mean(same) - np.mean(cross))


def clustered_interval(
    rows: list[dict[str, Any]], metric: str, repetitions: int, seed: int
) -> list[float]:
    by_problem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_problem[row["problem_key"]].append(row)
    keys = sorted(by_problem)
    rng = np.random.default_rng(seed)
    draws = []
    for _ in range(repetitions):
        sampled = rng.choice(keys, size=len(keys), replace=True)
        draw = [row for key in sampled for row in by_problem[str(key)]]
        draws.append(paired_contrast(draw, metric))
    return [float(value) for value in np.quantile(draws, [0.025, 0.975])]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bank",
        type=Path,
        default=ROOT / "experiments/endogenous_failure_conditioning/results/error_bank_v2_1_qwen_lineages/error_bank.jsonl",
    )
    parser.add_argument(
        "--scored",
        type=Path,
        default=ROOT / "experiments/endogenous_failure_conditioning/results/pilot_v2_1_qwen_lineages/results/scored_matrix.jsonl",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("DIAGNOSTIC_SUMMARY.json"),
    )
    parser.add_argument("--bootstrap-repetitions", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20260831)
    args = parser.parse_args()

    bank = {row["error_id"]: row for row in read_jsonl(args.bank)}
    enriched = []
    for row in read_jsonl(args.scored):
        if row["domain"] != "gsm8k":
            continue
        error = bank[row["error_id"]]
        extracted = extract_gsm8k_prediction(error["error_response"])
        if extracted is None:
            raise RuntimeError(f"Frozen GSM8K source error did not parse: {row['error_id']}")
        outcome = classify(row, str(extracted.value))
        enriched.append(
            {
                **row,
                "relation": (
                    "same_lineage"
                    if row["generator_family"] == row["corrector_family"]
                    else "cross_lineage"
                ),
                "outcome": outcome,
                "is_correct": float(outcome == "correct"),
                "retained_source_error": float(outcome == "retained_source_error"),
            }
        )

    summary: dict[str, Any] = {
        "status": "POST_HOC_DIAGNOSTIC_NOT_A_NEW_GATE",
        "scope": "gsm8k_only",
        "n": len(enriched),
        "groups": {},
        "clustered_same_minus_cross": {},
        "exact_model_matrix_external_neutral": {},
    }
    for wrapper in sorted({row["wrapper"] for row in enriched}):
        subset = [row for row in enriched if row["wrapper"] == wrapper]
        summary["groups"][wrapper] = {}
        for relation in ("same_lineage", "cross_lineage"):
            summary["groups"][wrapper][relation] = rates(
                [row for row in subset if row["relation"] == relation]
            )
        summary["clustered_same_minus_cross"][wrapper] = {}
        for metric in ("is_correct", "retained_source_error"):
            summary["clustered_same_minus_cross"][wrapper][metric] = {
                "point": paired_contrast(subset, metric),
                "ci95": clustered_interval(
                    subset, metric, args.bootstrap_repetitions, args.seed
                ),
            }

    external = [row for row in enriched if row["wrapper"] == "external_neutral"]
    models = sorted({row["generator_key"] for row in external})
    for generator in models:
        summary["exact_model_matrix_external_neutral"][generator] = {}
        for corrector in models:
            cell = [
                row
                for row in external
                if row["generator_key"] == generator and row["corrector_key"] == corrector
            ]
            summary["exact_model_matrix_external_neutral"][generator][corrector] = rates(cell)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
