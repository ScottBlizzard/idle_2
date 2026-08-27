from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


ACTION_NAMES = [
    "EMBER",
    "KITE",
    "LANTERN",
    "ORBIT",
    "QUARTZ",
    "RAVEN",
    "SUMMIT",
    "TIDAL",
    "VELVET",
    "WILLOW",
    "ZENITH",
    "CIPHER",
]

DOMAINS = {
    "abstract_game": (
        "You are choosing a move in a turn-based stochastic game.",
        "utility points",
    ),
    "cyber_defense": (
        "You control a defensive agent protecting a shared computer network.",
        "defender utility points",
    ),
    "tool_agent": (
        "You control an AI agent deciding whether to invoke a stochastic software tool.",
        "task utility points",
    ),
    "logistics": (
        "You control a logistics planner routing a time-critical shipment.",
        "delivery utility points",
    ),
    "exploration": (
        "You control an exploration agent at a branching transit gate.",
        "mission utility points",
    ),
    "resource_game": (
        "You control a player allocating a contested energy reserve.",
        "your utility points",
    ),
}


@dataclass(frozen=True)
class Branch:
    probability: float
    choices: tuple[int, ...]


@dataclass(frozen=True)
class GameSpec:
    pair_id: str
    domain: str
    difficulty: int
    safe_action: str
    branching_action: str
    safe_value: float
    branching_cost: float
    branches: tuple[Branch, ...]


def branching_value(spec: GameSpec, controller: str) -> float:
    if controller not in {"self", "opponent"}:
        raise ValueError(f"unknown controller: {controller}")
    selector = max if controller == "self" else min
    return -spec.branching_cost + sum(
        branch.probability * selector(branch.choices) for branch in spec.branches
    )


def optimal_action(spec: GameSpec, controller: str) -> tuple[str, float, float]:
    branch_value = branching_value(spec, controller)
    safe_value = spec.safe_value
    if math.isclose(branch_value, safe_value, abs_tol=1e-9):
        raise ValueError("benchmark construction produced a tie")
    action = spec.branching_action if branch_value > safe_value else spec.safe_action
    return action, safe_value, branch_value


def _probabilities(rng: random.Random, count: int, difficulty: int) -> list[float]:
    if difficulty == 1:
        return [0.5, 0.5]
    if difficulty == 2:
        candidates = ([0.2, 0.3, 0.5], [0.25, 0.25, 0.5], [0.1, 0.4, 0.5])
        probs = list(rng.choice(candidates))
        rng.shuffle(probs)
        return probs[:count]
    weights = [rng.randint(1, 6) for _ in range(count)]
    total = sum(weights)
    return [weight / total for weight in weights]


def _sample_spec(rng: random.Random, pair_index: int, difficulty: int, domain: str) -> GameSpec:
    for _ in range(10_000):
        safe_action, branching_action = rng.sample(ACTION_NAMES, 2)
        branch_count = {1: 2, 2: 3, 3: rng.choice([3, 4])}[difficulty]
        choice_count = {1: 2, 2: 3, 3: rng.choice([3, 4])}[difficulty]
        probs = _probabilities(rng, branch_count, difficulty)
        branches: list[Branch] = []
        for probability in probs:
            low = rng.randint(-8, 2)
            high = rng.randint(7, 18)
            middle = [rng.randint(low + 1, high - 1) for _ in range(choice_count - 2)]
            choices = [low, high, *middle]
            rng.shuffle(choices)
            branches.append(Branch(probability=probability, choices=tuple(choices)))

        branching_cost = float(rng.randint(0, 4) if difficulty >= 2 else 0)
        provisional = GameSpec(
            pair_id=f"cf_{pair_index:04d}",
            domain=domain,
            difficulty=difficulty,
            safe_action=safe_action,
            branching_action=branching_action,
            safe_value=0.0,
            branching_cost=branching_cost,
            branches=tuple(branches),
        )
        v_self = branching_value(provisional, "self")
        v_opp = branching_value(provisional, "opponent")
        lower = math.ceil(v_opp + 1.5)
        upper = math.floor(v_self - 1.5)
        if lower > upper:
            continue
        safe_value = float(rng.randint(lower, upper))
        spec = GameSpec(**{**asdict(provisional), "safe_value": safe_value})
        # asdict recursively converts Branch objects; restore them.
        spec = GameSpec(
            pair_id=spec.pair_id,
            domain=spec.domain,
            difficulty=spec.difficulty,
            safe_action=spec.safe_action,
            branching_action=spec.branching_action,
            safe_value=spec.safe_value,
            branching_cost=spec.branching_cost,
            branches=tuple(branches),
        )
        if branching_value(spec, "opponent") < safe_value < branching_value(spec, "self"):
            return spec
    raise RuntimeError("failed to sample a valid control-flip game")


def _format_probability(value: float) -> str:
    percent = value * 100
    if math.isclose(percent, round(percent), abs_tol=1e-9):
        return f"{int(round(percent))}%"
    return f"{percent:.1f}%"


def render_prompt(spec: GameSpec, controller: str) -> str:
    intro, units = DOMAINS[spec.domain]
    actor = (
        "After the chance outcome is publicly observed, YOU choose the listed continuation. "
        "You choose the continuation that maximizes your utility."
        if controller == "self"
        else "After the chance outcome is publicly observed, YOUR ADVERSARY chooses the listed "
        "continuation. The adversary observes the outcome and chooses the continuation that "
        "minimizes your utility."
    )
    lines = [
        intro,
        "Your objective is to maximize the final utility shown from your perspective.",
        "Choose exactly one root action:",
        f"- {spec.safe_action}: the process ends immediately with {spec.safe_value:g} {units}.",
        f"- {spec.branching_action}: pay an immediate cost of {spec.branching_cost:g} points, "
        "then Nature selects one public outcome:",
    ]
    for index, branch in enumerate(spec.branches, start=1):
        choices = ", ".join(str(choice) for choice in branch.choices)
        lines.append(
            f"  - Outcome {index} with probability {_format_probability(branch.probability)}: "
            f"available terminal utilities are [{choices}]."
        )
    lines.extend(
        [
            actor,
            "The immediate cost applies once and all listed terminal utilities are before that cost.",
            f"Which root action should you choose: {spec.safe_action} or {spec.branching_action}?",
        ]
    )
    return "\n".join(lines)


def make_records(pairs: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    domains = list(DOMAINS)
    records: list[dict] = []
    for index in range(pairs):
        # Cycle through the full domain x difficulty product. Keeping both on
        # index modulo cycles would silently confound each domain with one difficulty.
        domain = domains[index % len(domains)]
        difficulty = 1 + ((index // len(domains)) % 3)
        spec = _sample_spec(rng, index, difficulty, domain)
        v_self = branching_value(spec, "self")
        v_opp = branching_value(spec, "opponent")
        for controller in ("self", "opponent"):
            answer, safe_value, branch_value = optimal_action(spec, controller)
            record = {
                "id": f"{spec.pair_id}.{controller}",
                "pair_id": spec.pair_id,
                "controller": controller,
                "domain": domain,
                "difficulty": difficulty,
                "safe_action": spec.safe_action,
                "branching_action": spec.branching_action,
                "safe_value": safe_value,
                "branching_cost": spec.branching_cost,
                "branches": [asdict(branch) for branch in spec.branches],
                "self_branching_value": v_self,
                "opponent_branching_value": v_opp,
                "branching_value": branch_value,
                "optimal_action": answer,
                "margin": abs(branch_value - safe_value),
                "prompt": render_prompt(spec, controller),
            }
            records.append(record)
    return records


def write_jsonl(records: Iterable[dict], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pairs", type=int, default=180)
    parser.add_argument("--seed", type=int, default=20260826)
    parser.add_argument("--output", type=Path, default=Path("data/control_flip.jsonl"))
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    records = make_records(args.pairs, args.seed)
    write_jsonl(records, args.output)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "pairs": args.pairs,
                "records": len(records),
                "seed": args.seed,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
