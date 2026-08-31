#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--scores", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
groups = defaultdict(list)
rows = [json.loads(line) for line in args.scores.read_text().splitlines() if line]
for row in rows:
    groups[row["representation"]].append(bool(row["correct_choice"]))
accuracies = {key: sum(values) / len(values) for key, values in groups.items()}
passed_floor = set(accuracies) == {"original", "transformed"} and all(value >= 0.70 for value in accuracies.values())
gap = abs(accuracies.get("original", 0) - accuracies.get("transformed", 0))
passed_balance = gap <= 0.10
gate = {
    "records": len(rows),
    "expected_records": 192,
    "accuracies": accuracies,
    "absolute_gap": gap,
    "minimum_accuracy": 0.70,
    "maximum_gap": 0.10,
    "decision": "CARRIER_CAPABILITY_PASS" if len(rows) == 192 and passed_floor and passed_balance else "CARRIER_CAPABILITY_FAIL",
}
args.output.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
