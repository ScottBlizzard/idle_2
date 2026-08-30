#!/usr/bin/env python3
"""Score the complete crossed matrix and apply the frozen automatic pilot gate."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import load_config, read_jsonl, sha256_file
from experiments.moe_route_noncompositionality.stage_d_common import (
    extract_gsm8k_prediction,
    extract_math_prediction,
    verify_gsm8k,
    verify_math500,
)


def score(response: str, error: dict[str, Any]) -> tuple[bool, bool, str | None]:
    if error["domain"] == "gsm8k":
        correct, extracted = verify_gsm8k(response, error["gold_answer"])
    elif error["domain"] == "math500":
        correct, extracted = verify_math500(response, {"answer": error["gold_answer"]})
    else:
        raise ValueError(error["domain"])
    return bool(correct), extracted is not None, None if extracted is None else extracted.value


def mean(rows: list[dict[str, Any]], predicate: Callable[[dict[str, Any]], bool]) -> float:
    values = [float(row["correct"]) for row in rows if predicate(row)]
    return float(np.mean(values)) if values else float("nan")


def family_interaction(rows: list[dict[str, Any]], domain: str, wrapper: str) -> float:
    subset = [row for row in rows if row["domain"] == domain and row["wrapper"] == wrapper]
    families = sorted({row["generator_family"] for row in subset} | {row["corrector_family"] for row in subset})
    if len(families) != 2:
        raise RuntimeError(f"Interaction requires exactly two families/lineages: {families}")
    first, second = families
    ff = mean(subset, lambda row: row["generator_family"] == first and row["corrector_family"] == first)
    fs = mean(subset, lambda row: row["generator_family"] == first and row["corrector_family"] == second)
    sf = mean(subset, lambda row: row["generator_family"] == second and row["corrector_family"] == first)
    ss = mean(subset, lambda row: row["generator_family"] == second and row["corrector_family"] == second)
    return float((ff - fs) - (sf - ss))


def clustered_interval(
    rows: list[dict[str, Any]], domain: str, wrapper: str, repetitions: int, seed: int
) -> tuple[float, float]:
    subset = [row for row in rows if row["domain"] == domain and row["wrapper"] == wrapper]
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in subset:
        groups[row["problem_key"]].append(row)
    keys = sorted(groups)
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(repetitions):
        sampled = rng.choice(keys, size=len(keys), replace=True)
        draw = [row for key in sampled for row in groups[str(key)]]
        values.append(family_interaction(draw, domain, wrapper))
    return tuple(float(value) for value in np.quantile(values, [0.025, 0.975]))


def size_delta(rows: list[dict[str, Any]], domain: str, family: str, diagonal: bool) -> float:
    subset = [
        row
        for row in rows
        if row["domain"] == domain
        and row["wrapper"] == "external_neutral"
        and row["corrector_family"] == family
        and (not diagonal or row["generator_key"] == row["corrector_key"])
    ]
    large = mean(subset, lambda row: int(row["corrector_size_rank"]) == 1)
    small = mean(subset, lambda row: int(row["corrector_size_rank"]) == 0)
    return float(large - small)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--outputs", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()

    config = load_config(args.config)
    bank = {row["error_id"]: row for row in read_jsonl(args.bank)}
    expected = len(bank) * len(config["models"]) * len(config["wrappers"])
    generated: list[dict[str, Any]] = []
    for model_key in config["models"]:
        path = args.outputs / f"{model_key}.jsonl"
        if not path.exists():
            raise RuntimeError(f"Missing corrector output: {path}")
        generated.extend(read_jsonl(path))
    if len(generated) != expected:
        raise RuntimeError(f"Incomplete matrix: {len(generated)} rows, expected {expected}")
    if len({row["case_id"] for row in generated}) != expected:
        raise RuntimeError("Duplicate case IDs in crossed matrix")

    scored: list[dict[str, Any]] = []
    for row in generated:
        error = bank[row["error_id"]]
        correct, parsed, extracted = score(str(row["response"]), error)
        scored.append(
            {
                **{key: row[key] for key in (
                    "case_id", "error_id", "domain", "problem_key", "generator_key",
                    "generator_family", "corrector_key", "corrector_family",
                    "corrector_size_rank", "wrapper", "generated_tokens", "hit_token_limit"
                )},
                "correct": correct,
                "parsed": parsed,
                "extracted_answer": extracted,
            }
        )

    gates = config["gates"]
    interaction: dict[str, Any] = {}
    for domain_index, domain in enumerate(config["domains"]):
        interaction[domain] = {}
        for wrapper_index, wrapper in enumerate(config["wrappers"]):
            point = family_interaction(scored, domain, wrapper)
            low, high = clustered_interval(
                scored,
                domain,
                wrapper,
                int(gates["bootstrap_repetitions"]),
                int(config["seed"]) + 100 * domain_index + wrapper_index,
            )
            interaction[domain][wrapper] = {"point": point, "ci95": [low, high]}

    size_effects: dict[str, Any] = {}
    reversal = False
    positive_standardized = True
    families = sorted({model["family"] for model in config["models"].values()})
    if len(families) != 2:
        raise RuntimeError(f"Frozen pilot requires exactly two families/lineages: {families}")
    for domain in config["domains"]:
        size_effects[domain] = {}
        for family in families:
            diagonal = size_delta(scored, domain, family, True)
            standardized = size_delta(scored, domain, family, False)
            size_effects[domain][family] = {
                "diagonal_large_minus_small": diagonal,
                "standardized_large_minus_small": standardized,
                "standardization_shift": standardized - diagonal,
            }
            reversal |= (
                diagonal * standardized < 0
                and abs(standardized - diagonal) >= float(gates["selection_reversal_points"])
            )
            positive_standardized &= standardized > 0

    bad_rate = float(
        np.mean([not row["parsed"] or bool(row["hit_token_limit"]) for row in scored])
    )
    external = [interaction[domain]["external_neutral"] for domain in config["domains"]]
    external_replicates = (
        all(abs(cell["point"]) >= float(gates["family_interaction_points"]) for cell in external)
        and external[0]["point"] * external[1]["point"] > 0
        and all(cell["ci95"][0] * cell["ci95"][1] > 0 for cell in external)
    )
    assistant = [interaction[domain]["assistant_history"] for domain in config["domains"]]
    assistant_only = (
        not external_replicates
        and all(abs(cell["point"]) >= float(gates["family_interaction_points"]) for cell in assistant)
        and assistant[0]["point"] * assistant[1]["point"] > 0
    )

    if not reversal:
        decision = "KILL_NO_SELECTION_REVERSAL"
    elif assistant_only:
        decision = "KILL_ROLE_ONLY"
    elif not external_replicates:
        decision = "AUDIT_ONLY_NO_RELATIONAL_DEPTH"
    elif bad_rate > float(gates["maximum_parser_or_truncation_rate"]):
        decision = "KILL_ENGINEERING_QUALITY"
    elif not positive_standardized:
        decision = "AUDIT_ONLY_NONMONOTONE_CORRECTOR_SKILL"
    else:
        decision = "ADVANCE_ROUTER_TEST"

    args.result.mkdir(parents=True, exist_ok=False)
    scored_path = args.result / "scored_matrix.jsonl"
    with scored_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in scored:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    summary = {
        "status": "PILOT_GATE_COMPLETE",
        "decision": decision,
        "expected_cases": expected,
        "bad_parse_or_truncation_rate": bad_rate,
        "size_effects": size_effects,
        "family_interactions": interaction,
        "scored_matrix_sha256": sha256_file(scored_path),
        "config_sha256": sha256_file(args.config or Path(__file__).with_name("FROZEN_CONFIG.json")),
        "bank_sha256": sha256_file(args.bank),
    }
    (args.result / "FINAL_GATE.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    with (args.result / "cell_rates.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["domain", "wrapper", "generator", "corrector", "n", "accuracy"])
        for domain in config["domains"]:
            for wrapper in config["wrappers"]:
                for generator in config["models"]:
                    for corrector in config["models"]:
                        cell = [row for row in scored if row["domain"] == domain and row["wrapper"] == wrapper and row["generator_key"] == generator and row["corrector_key"] == corrector]
                        writer.writerow([domain, wrapper, generator, corrector, len(cell), mean(cell, lambda _: True)])
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
