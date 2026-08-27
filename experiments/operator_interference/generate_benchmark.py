from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


SKINS = {
    "abstract": "A decision system must select one of two stochastic root actions.",
    "routing": "A routing controller must select one of two stochastic route plans.",
    "scheduling": "A scheduler must select one of two stochastic execution plans.",
    "allocation": "A resource manager must select one of two stochastic allocation plans.",
    "game": "A game agent must select one of two stochastic moves.",
    "tool": "A tool-using agent must select one of two stochastic procedures.",
}

ACTION_LABELS = ("ACTION_P", "ACTION_Q")
ROLE_LABELS = ("ROLE_A", "ROLE_B")
OPERATOR_LABELS = ("OP_X", "OP_Y")

PROBABILITIES = {
    1: ((Fraction(1, 2), Fraction(1, 2)),),
    2: (
        (Fraction(1, 3), Fraction(2, 3)),
        (Fraction(1, 4), Fraction(3, 4)),
    ),
    3: (
        (Fraction(2, 5), Fraction(3, 5)),
        (Fraction(3, 8), Fraction(5, 8)),
        (Fraction(1, 6), Fraction(5, 6)),
    ),
}

MIN_MARGIN = {1: Fraction(2), 2: Fraction(3, 2), 3: Fraction(1)}


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _selected(values: tuple[Fraction, ...], semantic: str) -> Fraction:
    if semantic == "larger":
        return max(values)
    if semantic == "smaller":
        return min(values)
    raise ValueError(f"unknown semantic: {semantic}")


def _root_value(action: dict, semantic: str) -> Fraction:
    return sum(
        (Fraction(outcome["probability"]) * _selected(tuple(Fraction(v) for v in outcome["values"]), semantic) for outcome in action["outcomes"]),
        Fraction(0),
    )


def _sample_values(rng: random.Random, difficulty: int) -> tuple[Fraction, ...]:
    count = difficulty + 1
    if difficulty < 3:
        values = rng.sample(range(-9, 19), count)
        return tuple(Fraction(value) for value in values)
    pool = [Fraction(value, denominator) for denominator in (1, 2) for value in range(-16, 33)]
    values = rng.sample(pool, count)
    if len(set(values)) != count:
        return _sample_values(rng, difficulty)
    return tuple(values)


def _sample_numeric_actions(rng: random.Random, difficulty: int) -> tuple[dict, dict]:
    probabilities = rng.choice(PROBABILITIES[difficulty])
    for _ in range(50_000):
        actions = []
        for _action_index in range(2):
            outcomes = []
            for probability in probabilities:
                outcomes.append(
                    {
                        "probability": frac_text(probability),
                        "values": [frac_text(v) for v in _sample_values(rng, difficulty)],
                    }
                )
            actions.append({"outcomes": outcomes})
        large_values = [_root_value(action, "larger") for action in actions]
        small_values = [_root_value(action, "smaller") for action in actions]
        if large_values[0] == large_values[1] or small_values[0] == small_values[1]:
            continue
        if (large_values[0] > large_values[1]) == (small_values[0] > small_values[1]):
            continue
        if abs(large_values[0] - large_values[1]) < MIN_MARGIN[difficulty]:
            continue
        if abs(small_values[0] - small_values[1]) < MIN_MARGIN[difficulty]:
            continue
        return actions[0], actions[1]
    raise RuntimeError("failed to sample a symmetric control-flip tree")


def _assign_action_labels(
    numeric_actions: tuple[dict, dict], desired_large_label: str
) -> dict[str, dict]:
    large_values = [_root_value(action, "larger") for action in numeric_actions]
    large_winner = 0 if large_values[0] > large_values[1] else 1
    other_label = ACTION_LABELS[1] if desired_large_label == ACTION_LABELS[0] else ACTION_LABELS[0]
    labels = [None, None]
    labels[large_winner] = desired_large_label
    labels[1 - large_winner] = other_label
    return {labels[index]: numeric_actions[index] for index in range(2)}


def _oracle(actions: dict[str, dict], semantic: str, operator_label: str) -> dict:
    root_values: dict[str, str] = {}
    nodes: dict[str, dict] = {}
    for action_label in ACTION_LABELS:
        action = actions[action_label]
        root_values[action_label] = frac_text(_root_value(action, semantic))
        for outcome_index, outcome in enumerate(action["outcomes"], start=1):
            node = f"NODE_{action_label[-1]}{outcome_index}"
            values = tuple(Fraction(value) for value in outcome["values"])
            nodes[node] = {
                "operator": operator_label,
                "selected_value": frac_text(_selected(values, semantic)),
            }
    values = {label: Fraction(value) for label, value in root_values.items()}
    optimal = max(ACTION_LABELS, key=lambda label: values[label])
    margin = abs(values[ACTION_LABELS[0]] - values[ACTION_LABELS[1]])
    return {
        "semantic": semantic,
        "operator": operator_label,
        "nodes": nodes,
        "root_values": root_values,
        "optimal_action": optimal,
        "margin": frac_text(margin),
    }


def render_task(record: dict) -> str:
    lines = [
        SKINS[record["skin"]],
        "Your objective is to choose the root action with the larger expected final score.",
        "At every terminal-choice node, the active controller applies its assigned operator to select exactly one listed value.",
        f"Active controller: <ACTIVE_CONTROLLER>{record['active_controller']}</ACTIVE_CONTROLLER>",
        "After those selections, use the stated chance probabilities to compute each root action's expected score.",
    ]
    for action_label in record["action_order"]:
        lines.append(f"{action_label}:")
        for outcome_index, outcome in enumerate(record["actions"][action_label]["outcomes"], start=1):
            node = f"NODE_{action_label[-1]}{outcome_index}"
            values = ", ".join(outcome["values"])
            lines.append(
                f"- {node} has probability {outcome['probability']} and candidate values [{values}]."
            )
    lines.append(f"Choose exactly one final action: {ACTION_LABELS[0]} or {ACTION_LABELS[1]}.")
    return "\n".join(lines)


def _pair_record(
    *,
    pair_index: int,
    split: str,
    skin: str,
    difficulty: int,
    rng: random.Random,
) -> list[dict]:
    # Eight-way cycling balances controller label, optimal action label, and display order.
    desired_large_label = ACTION_LABELS[(pair_index // 1) % 2]
    larger_role = ROLE_LABELS[(pair_index // 2) % 2]
    larger_operator = OPERATOR_LABELS[(pair_index // 4) % 2]
    action_order = list(ACTION_LABELS)
    if (pair_index // 8) % 2:
        action_order.reverse()

    numeric_actions = _sample_numeric_actions(rng, difficulty)
    actions = _assign_action_labels(numeric_actions, desired_large_label)
    role_semantics = {
        larger_role: "larger",
        ROLE_LABELS[1] if larger_role == ROLE_LABELS[0] else ROLE_LABELS[0]: "smaller",
    }
    operator_semantics = {
        larger_operator: "larger",
        OPERATOR_LABELS[1] if larger_operator == OPERATOR_LABELS[0] else OPERATOR_LABELS[0]: "smaller",
    }
    role_to_operator = {
        role: next(op for op, semantic in operator_semantics.items() if semantic == role_semantic)
        for role, role_semantic in role_semantics.items()
    }
    pair_id = f"oi_{'eng' if split == 'engineering' else 'conf'}_{pair_index:04d}"
    records = []
    for active_controller in ROLE_LABELS:
        semantic = role_semantics[active_controller]
        oracle = _oracle(actions, semantic, role_to_operator[active_controller])
        record = {
            "id": f"{pair_id}.{active_controller}",
            "pair_id": pair_id,
            "split": split,
            "skin": skin,
            "difficulty": difficulty,
            "active_controller": active_controller,
            "role_semantics": role_semantics,
            "operator_semantics": operator_semantics,
            "role_to_operator": role_to_operator,
            "action_order": action_order,
            "actions": actions,
            "oracle": oracle,
        }
        record["task"] = render_task(record)
        records.append(record)
    return records


def make_records(pairs: int, seed: int, split: str) -> list[dict]:
    if split not in {"engineering", "confirmatory"}:
        raise ValueError(split)
    if pairs % 3:
        raise ValueError("pair count must be divisible by three difficulty levels")
    rng = random.Random(seed)
    skins = list(SKINS)
    records: list[dict] = []
    for index in range(pairs):
        if split == "confirmatory" and pairs == 54:
            skin = skins[index // 9]
            difficulty = 1 + ((index // 3) % 3)
        else:
            skin = skins[index % len(skins)]
            difficulty = 1 + (index % 3)
        records.extend(
            _pair_record(
                pair_index=index,
                split=split,
                skin=skin,
                difficulty=difficulty,
                rng=rng,
            )
        )
    return records


def task_pair_diff_is_valid(left: dict, right: dict) -> bool:
    marker_start = "<ACTIVE_CONTROLLER>"
    marker_end = "</ACTIVE_CONTROLLER>"

    def normalize(text: str) -> str:
        start = text.index(marker_start) + len(marker_start)
        end = text.index(marker_end)
        return text[:start] + "<ROLE>" + text[end:]

    return normalize(left["task"]) == normalize(right["task"])


def metadata_probe_accuracy(records: list[dict]) -> float:
    # Best deterministic lookup using only active role and action display order.
    counts: dict[tuple[str, tuple[str, ...]], dict[str, int]] = {}
    for record in records:
        key = (record["active_controller"], tuple(record["action_order"]))
        bucket = counts.setdefault(key, {label: 0 for label in ACTION_LABELS})
        bucket[record["oracle"]["optimal_action"]] += 1
    correct = sum(max(bucket.values()) for bucket in counts.values())
    return correct / len(records)


def validate_records(records: list[dict]) -> dict:
    by_pair: dict[str, list[dict]] = {}
    for record in records:
        by_pair.setdefault(record["pair_id"], []).append(record)
    for pair_id, pair in by_pair.items():
        if len(pair) != 2 or {r["active_controller"] for r in pair} != set(ROLE_LABELS):
            raise ValueError(f"invalid pair membership: {pair_id}")
        if not task_pair_diff_is_valid(pair[0], pair[1]):
            raise ValueError(f"task payload differs outside active controller: {pair_id}")
        if pair[0]["oracle"]["optimal_action"] == pair[1]["oracle"]["optimal_action"]:
            raise ValueError(f"optimal action does not flip: {pair_id}")
        for record in pair:
            if Fraction(record["oracle"]["margin"]) < MIN_MARGIN[record["difficulty"]]:
                raise ValueError(f"margin too small: {record['id']}")
    probe = metadata_probe_accuracy(records)
    if probe > 0.55:
        raise ValueError(f"metadata-only probe exceeds threshold: {probe:.3f}")
    return {
        "pairs": len(by_pair),
        "records": len(records),
        "metadata_probe_accuracy": probe,
        "sha256": hashlib.sha256(
            "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in records).encode("utf-8")
        ).hexdigest(),
    }


def write_jsonl(records: Iterable[dict], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--split", choices=("engineering", "confirmatory"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    records = make_records(args.pairs, args.seed, args.split)
    audit = validate_records(records)
    write_jsonl(records, args.output)
    print(json.dumps({"output": str(args.output), "seed": args.seed, **audit}, sort_keys=True))


if __name__ == "__main__":
    main()
