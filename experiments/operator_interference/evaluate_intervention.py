from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    records = []
    for pattern in args.predictions:
        for path in glob.glob(pattern) or [pattern]:
            records.extend(json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip())
    rows = []
    for record in records:
        try:
            payload = json.loads(record["text"])
            prediction = payload["final_action"]
        except (json.JSONDecodeError, KeyError, TypeError):
            prediction = None
        rows.append({**record, "prediction": prediction, "correct": prediction == record["optimal_action"]})
    columns = [
        "case_id",
        "intervention_pair_id",
        "source_id",
        "model_id",
        "kind",
        "variant",
        "optimal_action",
        "prediction",
        "correct",
    ]
    frame = pd.DataFrame(rows)
    if frame.empty:
        frame = pd.DataFrame(columns=columns)
        summary = pd.DataFrame(
            columns=[
                "model_id",
                "kind",
                "pairs",
                "original_accuracy",
                "modified_accuracy",
                "modified_minus_original",
                "rescued",
                "damaged",
            ]
        )
        args.output_dir.mkdir(parents=True, exist_ok=True)
        frame.to_csv(args.output_dir / "intervention_items.csv", index=False)
        summary.to_csv(args.output_dir / "intervention_summary.csv", index=False)
        print("No intervention cases.")
        return
    summaries = []
    for (model, kind), group in frame.groupby(["model_id", "kind"]):
        pivot = group.pivot_table(index="intervention_pair_id", columns="variant", values="correct", aggfunc="first").dropna()
        if pivot.empty:
            continue
        summaries.append(
            {
                "model_id": model,
                "kind": kind,
                "pairs": len(pivot),
                "original_accuracy": float(pivot.original.mean()),
                "modified_accuracy": float(pivot.modified.mean()),
                "modified_minus_original": float((pivot.modified.astype(float) - pivot.original.astype(float)).mean()),
                "rescued": int((~pivot.original & pivot.modified).sum()),
                "damaged": int((pivot.original & ~pivot.modified).sum()),
            }
        )
    summary = pd.DataFrame(summaries)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output_dir / "intervention_items.csv", index=False)
    summary.to_csv(args.output_dir / "intervention_summary.csv", index=False)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
