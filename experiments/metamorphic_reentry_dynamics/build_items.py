#!/usr/bin/env python3
"""Build deterministic, executable-equivalence pairs for Stage 0."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import deque
from pathlib import Path


BOOL_DEMOS = (
    "Evaluate the expression under the assignment. Reply yes if it is true, otherwise no.\n"
    "Assignment: A=yes, B=no. Expression: A and B.\nAnswer: no\n"
    "Assignment: A=no, B=no. Expression: (not A) or B.\nAnswer: yes\n"
    "Assignment: A=yes, B=yes. Expression: not (A and (not B)).\nAnswer: yes\n"
)

GRAPH_DEMOS = (
    "Decide whether a directed path exists. Reply yes or no.\n"
    "Edges: A->B, B->C. Query: path A->C?\nAnswer: yes\n"
    "Edges: A->B, C->A. Query: path B->C?\nAnswer: no\n"
)

ARITH_DEMOS = (
    "Compute the requested integer. Reply with only the integer.\n"
    "Given x=3, compute 2*x+1.\nAnswer: 7\n"
    "Given x=4, compute 3*x-2.\nAnswer: 10\n"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bool_item(rng: random.Random, index: int) -> dict:
    a, b, c = (rng.choice([False, True]) for _ in range(3))
    pattern = index % 4
    if pattern == 0:
        original = "not (A and B)"
        transformed = "(not A) or (not B)"
        value = not (a and b)
    elif pattern == 1:
        original = "not (A or B)"
        transformed = "(not A) and (not B)"
        value = not (a or b)
    elif pattern == 2:
        original = "not (A and (B or C))"
        transformed = "(not A) or ((not B) and (not C))"
        value = not (a and (b or c))
    else:
        original = "not ((A or B) and C)"
        transformed = "((not A) and (not B)) or (not C)"
        value = not ((a or b) and c)
    assignment = f"A={'yes' if a else 'no'}, B={'yes' if b else 'no'}, C={'yes' if c else 'no'}"
    stem = f"Assignment: {assignment}. Expression: {{expr}}.\nAnswer:"
    answer = " yes" if value else " no"
    distractor = " no" if value else " yes"
    return {
        "item_id": f"boolean_demorgan_{index:04d}",
        "family": "boolean_demorgan",
        "prompt_original": BOOL_DEMOS + stem.format(expr=original),
        "prompt_transformed": BOOL_DEMOS + stem.format(expr=transformed),
        "correct_continuation": answer,
        "incorrect_continuation": distractor,
        "semantic_value": value,
        "equivalence_witness": {"assignment": {"A": a, "B": b, "C": c}, "rule": "de_morgan"},
    }


def reachable(edges: list[tuple[str, str]], source: str, target: str) -> bool:
    graph: dict[str, list[str]] = {}
    for left, right in edges:
        graph.setdefault(left, []).append(right)
    queue = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def graph_item(rng: random.Random, index: int) -> dict:
    nodes = list("ABCDE")
    all_edges = [(a, b) for a in nodes for b in nodes if a != b]
    rng.shuffle(all_edges)
    edges = sorted(all_edges[: rng.randint(4, 7)])
    source, target = rng.sample(nodes, 2)
    value = reachable(edges, source, target)
    permutation = nodes[:]
    while permutation == nodes:
        rng.shuffle(permutation)
    mapping = dict(zip(nodes, permutation))
    transformed_edges = sorted((mapping[a], mapping[b]) for a, b in edges)
    transformed_source, transformed_target = mapping[source], mapping[target]

    def prompt(es: list[tuple[str, str]], s: str, t: str) -> str:
        rendered = ", ".join(f"{a}->{b}" for a, b in es)
        return GRAPH_DEMOS + f"Edges: {rendered}. Query: path {s}->{t}?\nAnswer:"

    answer = " yes" if value else " no"
    distractor = " no" if value else " yes"
    return {
        "item_id": f"graph_bijection_{index:04d}",
        "family": "graph_bijection",
        "prompt_original": prompt(edges, source, target),
        "prompt_transformed": prompt(transformed_edges, transformed_source, transformed_target),
        "correct_continuation": answer,
        "incorrect_continuation": distractor,
        "semantic_value": value,
        "equivalence_witness": {"mapping": mapping, "edges": edges, "query": [source, target]},
    }


def arithmetic_item(rng: random.Random, index: int) -> dict:
    scale = rng.choice([2, 3])
    quotient = rng.choice([2, 3, 4])
    coefficient = scale * quotient
    x_value = rng.randint(2, 9)
    offset = rng.choice([-5, -3, -1, 1, 3, 5])
    value = coefficient * x_value + offset
    y_value = scale * x_value
    sign = "+" if offset >= 0 else "-"
    abs_offset = abs(offset)
    original_expr = f"Given x={x_value}, compute {coefficient}*x{sign}{abs_offset}."
    transformed_expr = f"Let y={scale}*x. Given y={y_value}, compute {quotient}*y{sign}{abs_offset}."
    distractor_value = value + (1 if index % 2 == 0 else -1)
    return {
        "item_id": f"linear_reparameterization_{index:04d}",
        "family": "linear_reparameterization",
        "prompt_original": ARITH_DEMOS + original_expr + "\nAnswer:",
        "prompt_transformed": ARITH_DEMOS + transformed_expr + "\nAnswer:",
        "correct_continuation": f" {value}",
        "incorrect_continuation": f" {distractor_value}",
        "semantic_value": value,
        "equivalence_witness": {
            "x": x_value,
            "scale": scale,
            "coefficient": coefficient,
            "quotient": quotient,
            "offset": offset,
        },
    }


def build(config: dict) -> list[dict]:
    rng = random.Random(config["item_seed"])
    n = config["items_per_family"]
    items = []
    for i in range(n):
        items.extend((bool_item(rng, i), graph_item(rng, i), arithmetic_item(rng, i)))
    return sorted(items, key=lambda row: row["item_id"])


def validate(items: list[dict], config: dict) -> None:
    expected = config["items_per_family"] * len(config["families"])
    assert len(items) == expected
    assert len({x["item_id"] for x in items}) == expected
    for item in items:
        assert item["prompt_original"] != item["prompt_transformed"]
        assert item["correct_continuation"] != item["incorrect_continuation"]
        assert item["family"] in config["families"]
        if item["family"] == "linear_reparameterization":
            w = item["equivalence_witness"]
            assert w["coefficient"] * w["x"] + w["offset"] == item["semantic_value"]
            assert w["quotient"] * (w["scale"] * w["x"]) + w["offset"] == item["semantic_value"]
        elif item["family"] == "graph_bijection":
            w = item["equivalence_witness"]
            edges = [tuple(edge) for edge in w["edges"]]
            source, target = w["query"]
            mapped = [(w["mapping"][a], w["mapping"][b]) for a, b in edges]
            assert reachable(edges, source, target) == reachable(
                mapped, w["mapping"][source], w["mapping"][target]
            ) == item["semantic_value"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("FROZEN_CONFIG.json"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("items.jsonl"))
    args = parser.parse_args()
    config_bytes = args.config.read_bytes()
    config = json.loads(config_bytes)
    items = build(config)
    validate(items, config)
    payload = "".join(json.dumps(x, sort_keys=True, ensure_ascii=False) + "\n" for x in items).encode()
    args.output.write_bytes(payload)
    manifest = {
        "study_id": config["study_id"],
        "config_sha256": sha256_bytes(config_bytes),
        "items_sha256": sha256_bytes(payload),
        "n_items": len(items),
        "families": {family: sum(x["family"] == family for x in items) for family in config["families"]},
    }
    args.output.with_suffix(".manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
