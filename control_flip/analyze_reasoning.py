from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path
from typing import Sequence

import pandas as pd

from evaluate import parse_choice, read_jsonl


OPERATOR_CALLS = {
    "max": re.compile(r"\bmax(?:imum)?\s*\(", re.IGNORECASE),
    "min": re.compile(r"\bmin(?:imum)?\s*\(", re.IGNORECASE),
}


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--predictions", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args(argv)


def safe_mean(series: pd.Series) -> float:
    return float(series.mean()) if len(series) else float("nan")


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    truth = {record["id"]: record for record in read_jsonl(args.data)}
    paths: list[Path] = []
    for pattern in args.predictions:
        matched = glob.glob(pattern)
        paths.extend(Path(path) for path in (matched or [pattern]))

    rows = []
    for path in paths:
        for prediction in read_jsonl(path):
            record = truth.get(prediction["id"])
            if record is None:
                continue
            text = prediction.get("text", "")
            has_max = bool(OPERATOR_CALLS["max"].search(text))
            has_min = bool(OPERATOR_CALLS["min"].search(text))
            expected = "max" if record["controller"] == "self" else "min"
            unexpected = "min" if expected == "max" else "max"
            choice, _ = parse_choice(text, (record["safe_action"], record["branching_action"]))
            rows.append(
                {
                    "id": record["id"],
                    "pair_id": record["pair_id"],
                    "model_id": prediction["model_id"],
                    "prompt_mode": prediction["prompt_mode"],
                    "controller": record["controller"],
                    "domain": record["domain"],
                    "difficulty": record["difficulty"],
                    "correct": choice == record["optimal_action"],
                    "has_max_call": has_max,
                    "has_min_call": has_min,
                    "has_expected_call": has_max if expected == "max" else has_min,
                    "has_unexpected_call": has_min if unexpected == "min" else has_max,
                    "has_mixed_calls": has_max and has_min,
                }
            )

    frame = pd.DataFrame(rows)
    if frame.empty:
        raise SystemExit("no matching predictions")

    summaries = []
    for (model_id, prompt_mode), group in frame.groupby(["model_id", "prompt_mode"]):
        bad = group[group.has_unexpected_call]
        clean = group[~group.has_unexpected_call]
        errors = group[~group.correct]
        summaries.append(
            {
                "model_id": model_id,
                "prompt_mode": prompt_mode,
                "items": len(group),
                "item_accuracy": safe_mean(group.correct),
                "expected_operator_call_rate": safe_mean(group.has_expected_call),
                "unexpected_operator_call_rate": safe_mean(group.has_unexpected_call),
                "mixed_operator_call_rate": safe_mean(group.has_mixed_calls),
                "accuracy_when_unexpected": safe_mean(bad.correct),
                "accuracy_when_clean": safe_mean(clean.correct),
                "error_share_with_unexpected": safe_mean(errors.has_unexpected_call),
            }
        )
    summary = pd.DataFrame(summaries).sort_values(["model_id", "prompt_mode"])

    args.output_dir.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output_dir / "operator_items.csv", index=False)
    summary.to_csv(args.output_dir / "operator_summary.csv", index=False)
    report = [
        "# Generated-Reasoning Operator Audit",
        "",
        summary.to_markdown(index=False, floatfmt=".3f"),
        "",
        "An unexpected operator call is an explicit `min(...)` in a self-controlled item or "
        "`max(...)` in an adversary-controlled item. The audit inspects generated text only; "
        "prompt tokens are not included.",
    ]
    (args.output_dir / "OPERATOR_AUDIT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
