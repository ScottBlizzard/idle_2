#!/usr/bin/env python3
"""Build a capability-only bank for addition-associativity truth evaluation."""

import hashlib
import json
import random
from pathlib import Path


OUT = Path(__file__).resolve().parent
RNG = random.Random(2026083104)
DEMO_ROWS = [
    (1, 2, 3, 6), (2, 1, 4, 8), (0, 3, 2, 5), (4, 1, 1, 7),
    (2, 2, 1, 5), (3, 0, 4, 8), (1, 4, 2, 7), (3, 2, 2, 6),
]


def label(a, b, c, target):
    return "yes" if a + b + c == target else "no"


def demos():
    lines = ["Decide whether each addition statement is true. Reply yes or no."]
    for a, b, c, target in DEMO_ROWS:
        lines.append(f"Is {a} + {b} + {c} equal to {target}?\nAnswer: {label(a,b,c,target)}")
    return "\n".join(lines) + "\n"


triples = [(a, b, c) for a in range(7) for b in range(7) for c in range(7) if 2 <= a + b + c <= 12]
RNG.shuffle(triples)
rows = []
yes_count = no_count = 0
for index, (a, b, c) in enumerate(triples[:96]):
    truth = index % 2 == 0
    total = a + b + c
    if truth:
        target = total
        yes_count += 1
    else:
        direction = 1 if (index // 2) % 2 == 0 or total == 0 else -1
        target = total + direction
        no_count += 1
    correct = " yes" if truth else " no"
    incorrect = " no" if truth else " yes"
    prefix = demos()
    rows.append({
        "item_id": f"addition_associativity_preflight_{index:04d}",
        "family": "addition_associativity",
        "split": "preflight",
        "prompt_original": prefix + f"Is (({a} + {b}) + {c}) equal to {target}?\nAnswer:",
        "prompt_transformed": prefix + f"Is ({a} + ({b} + {c})) equal to {target}?\nAnswer:",
        "correct_continuation": correct,
        "incorrect_continuation": incorrect,
        "equivalence_witness": {"a": a, "b": b, "c": c, "target": target, "truth": truth},
    })

assert yes_count == no_count == 48
payload = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows).encode()
(OUT / "associativity_items.jsonl").write_bytes(payload)
config = {
    "study_id": "addition_associativity_carrier_calibration",
    "model_repositories": {"1": "EleutherAI/pythia-410m-seed1"},
    "checkpoints": ["step143000"],
    "families": ["addition_associativity"],
    "items_per_family": 96,
    "batch_size": 64,
    "dtype": "float16",
    "max_prompt_tokens": 256,
}
(OUT / "associativity_config.json").write_text(json.dumps(config, indent=2, sort_keys=True) + "\n")
print(json.dumps({"records": len(rows), "yes": yes_count, "no": no_count, "sha256": hashlib.sha256(payload).hexdigest()}, indent=2))
