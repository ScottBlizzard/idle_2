#!/usr/bin/env python3
"""Outcome-blind engineering/capability gate for the final-checkpoint preflight."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("FROZEN_CONFIG.json"))
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    rows = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines() if line]
    expected = config["items_per_family"] * len(config["families"]) * 2
    grouped = defaultdict(lambda: defaultdict(list))
    for row in rows:
        grouped[row["family"]][row["representation"]].append(bool(row["correct_choice"]))
    cells = {}
    capable = []
    for family in config["families"]:
        cells[family] = {}
        for representation in ("original", "transformed"):
            values = grouped[family][representation]
            cells[family][representation] = sum(values) / len(values) if values else None
        if all(cells[family][rep] is not None and cells[family][rep] >= config["minimum_accuracy_each_representation"] for rep in cells[family]):
            capable.append(family)
    passed = len(rows) == expected and bool(capable)
    gate = {
        "study_id": config["study_id"],
        "records": len(rows),
        "expected_records": expected,
        "accuracies": cells,
        "capable_families": capable,
        "decision": "PREFLIGHT_PASS" if passed else "NO_GO_PREFLIGHT_CAPABILITY_OR_COMPLETENESS",
    }
    args.output.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(gate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
