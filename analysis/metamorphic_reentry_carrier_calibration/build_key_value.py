#!/usr/bin/env python3
"""Capability-only calibration for a possible Stage 0 v2 carrier.

Do not use this file to inspect transformation effects. It exists only to determine
whether Pythia-410M can perform the base lookup task in both representations.
"""

import hashlib
import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
RNG = random.Random(2026083102)
VALUES = [
    " red", " blue", " green", " black", " white", " orange", " purple", " yellow",
    " apple", " lemon", " chair", " table", " river", " ocean", " horse", " tiger",
]
KEYS = list("ABCDEFGHJKLMNPQRSTUVWXYZ")


def render(pairs, query, template):
    if template == "discovery":
        body = "; ".join(f"{k}={v.strip()}" for k, v in pairs)
        return (
            "Read the dictionary and complete the lookup.\n"
            "Dictionary: A=red; B=blue; C=green. Lookup B:\nAnswer: blue\n"
            "Dictionary: D=chair; E=table; F=river. Lookup F:\nAnswer: river\n"
            f"Dictionary: {body}. Lookup {query}:\nAnswer:"
        )
    body = ", ".join(f"{k} -> {v.strip()}" for k, v in pairs)
    return (
        "Use the mappings to return the requested value.\n"
        "Mappings [A -> red, B -> blue, C -> green]. Value for C:\nAnswer: green\n"
        "Mappings [D -> chair, E -> table, F -> river]. Value for D:\nAnswer: chair\n"
        f"Mappings [{body}]. Value for {query}:\nAnswer:"
    )


rows = []
for split, count in (("discovery", 128), ("confirmation", 128)):
    for index in range(count):
        keys = RNG.sample(KEYS, 6)
        values = RNG.sample(VALUES, 6)
        query_index = RNG.randrange(6)
        query = keys[query_index]
        correct = values[query_index]
        distractor = values[(query_index + RNG.randrange(1, 6)) % 6]
        mapping = list(zip(keys, values))
        target = mapping[query_index]
        rest = [pair for i, pair in enumerate(mapping) if i != query_index]
        RNG.shuffle(rest)
        first = [target] + rest
        last = rest + [target]
        rows.append({
            "item_id": f"key_value_order_{split}_{index:04d}",
            "family": "key_value_order",
            "split": split,
            "prompt_original": render(first, query, split),
            "prompt_transformed": render(last, query, split),
            "correct_continuation": correct,
            "incorrect_continuation": distractor,
            "equivalence_witness": {"mapping": {k: v.strip() for k, v in mapping}, "query": query},
        })

payload = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows).encode()
(OUT / "candidate_items.jsonl").write_bytes(payload)
base_config = json.loads((ROOT / "experiments/metamorphic_reentry_dynamics/FROZEN_CONFIG.json").read_text())
base_config.update({
    "study_id": "metamorphic_reentry_v2_carrier_calibration",
    "items_per_family": 256,
    "families": ["key_value_order"],
    "minimum_accuracy_each_representation": 0.70,
})
(OUT / "candidate_config.json").write_text(json.dumps(base_config, indent=2, sort_keys=True) + "\n")
print(json.dumps({"records": len(rows), "sha256": hashlib.sha256(payload).hexdigest()}, indent=2))
