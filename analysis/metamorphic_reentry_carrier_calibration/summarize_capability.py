#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--items", type=Path, required=True)
parser.add_argument("--scores", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

item_split = {}
for line in args.items.read_text().splitlines():
    row = json.loads(line)
    item_split[row["item_id"]] = row["split"]

groups = defaultdict(list)
rows = [json.loads(line) for line in args.scores.read_text().splitlines() if line]
for row in rows:
    groups[(item_split[row["item_id"]], row["representation"])].append(bool(row["correct_choice"]))

accuracies = {}
for split in ("discovery", "confirmation"):
    accuracies[split] = {}
    for representation in ("original", "transformed"):
        values = groups[(split, representation)]
        accuracies[split][representation] = sum(values) / len(values)

passed_floor = all(value >= 0.70 for split in accuracies.values() for value in split.values())
passed_balance = all(abs(split["original"] - split["transformed"]) <= 0.10 for split in accuracies.values())
passed = passed_floor and passed_balance
gate = {
    "records": len(rows),
    "expected_records": 512,
    "accuracies": accuracies,
    "passed_floor": passed_floor,
    "passed_balance": passed_balance,
    "maximum_allowed_within_split_gap": 0.10,
    "decision": "CARRIER_CAPABILITY_PASS" if passed and len(rows) == 512 else "CARRIER_CAPABILITY_FAIL",
}
args.output.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
