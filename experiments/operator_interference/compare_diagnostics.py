from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import pandas as pd

from evaluate import pair_frame, parse_and_score, read_jsonl, summarize


def paths(patterns: list[str]) -> list[Path]:
    result = []
    for pattern in patterns:
        result.extend(Path(path) for path in (glob.glob(pattern) or [pattern]))
    return sorted(set(result))


def keyed(records: list[dict]) -> dict[tuple, dict]:
    return {
        (r["model_id"], r["pack"], r["condition"], r["id"]): r
        for r in records
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--primary", nargs="+", required=True)
    parser.add_argument("--replay", nargs="+", required=True)
    parser.add_argument("--template", nargs="+", required=True)
    parser.add_argument("--unconstrained", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    truth = {r["id"]: r for r in read_jsonl(args.data)}
    primary_records = [r for path in paths(args.primary) for r in read_jsonl(path)]
    replay_records = [r for path in paths(args.replay) for r in read_jsonl(path)]
    primary = keyed(primary_records)
    replay_rows = []
    for key, rerun in keyed(replay_records).items():
        original = primary.get(key)
        if original is None:
            continue
        replay_rows.append(
            {
                "model_id": key[0],
                "pack": key[1],
                "condition": key[2],
                "id": key[3],
                "token_match": original.get("output_token_ids") == rerun.get("output_token_ids"),
                "answer_text_match": original.get("text") == rerun.get("text"),
            }
        )
    replay_frame = pd.DataFrame(replay_rows)
    replay_summary = (
        replay_frame.groupby("model_id")
        .agg(items=("id", "size"), token_match_rate=("token_match", "mean"), text_match_rate=("answer_text_match", "mean"))
        .reset_index()
    )

    diagnostic_records = []
    for source, patterns_arg in (("plain", args.template), ("unconstrained", args.unconstrained)):
        for path in paths(patterns_arg):
            for prediction in read_jsonl(path):
                if prediction["id"] in truth:
                    row = parse_and_score(truth[prediction["id"]], prediction)
                    row["diagnostic_source"] = source
                    diagnostic_records.append(row)
    items = pd.DataFrame(diagnostic_records)
    pairs = pair_frame(items)
    diagnostic_summary = summarize(items, pairs)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    replay_frame.to_csv(args.output_dir / "replay_items.csv", index=False)
    replay_summary.to_csv(args.output_dir / "replay_summary.csv", index=False)
    diagnostic_summary.to_csv(args.output_dir / "format_template_summary.csv", index=False)
    print(replay_summary.to_string(index=False))
    print(diagnostic_summary.to_string(index=False))


if __name__ == "__main__":
    main()
