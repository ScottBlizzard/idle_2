#!/usr/bin/env python3
"""Outcome-gated analysis for the re-entrant sign scan."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def load_records(paths: list[Path]) -> list[dict]:
    rows = []
    for path in paths:
        rows.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
    return rows


def summarize(rows: list[dict]) -> dict:
    paired = defaultdict(dict)
    for row in rows:
        key = (row["seed"], row["checkpoint"], row["family"], row["item_id"])
        paired[key][row["representation"]] = row
    cells = defaultdict(list)
    for (seed, checkpoint, family, _), pair in paired.items():
        if set(pair) != {"original", "transformed"}:
            raise ValueError("incomplete representation pair")
        delta = pair["transformed"]["margin"] - pair["original"]["margin"]
        cells[(seed, checkpoint, family)].append((delta, pair["original"]["correct_choice"], pair["transformed"]["correct_choice"]))
    summary = {}
    for key, values in cells.items():
        n = len(values)
        summary[key] = {
            "n": n,
            "mean_delta": sum(v[0] for v in values) / n,
            "accuracy_original": sum(v[1] for v in values) / n,
            "accuracy_transformed": sum(v[2] for v in values) / n,
        }
    return summary


def sign(cell: dict, config: dict) -> int:
    if min(cell["accuracy_original"], cell["accuracy_transformed"]) < config["minimum_accuracy_each_representation"]:
        return 0
    delta = cell["mean_delta"]
    threshold = config["effect_lobe_min_abs_logit"]
    return 1 if delta >= threshold else (-1 if delta <= -threshold else 0)


def find_discovery_patterns(summary: dict, config: dict) -> list[dict]:
    checkpoints = config["checkpoints"]
    discovery = config["discovery_seeds"]
    candidates = []
    for family in config["families"]:
        checkpoint_signs = []
        for checkpoint in checkpoints:
            signs = [sign(summary[(seed, checkpoint, family)], config) for seed in discovery]
            pos, neg = signs.count(1), signs.count(-1)
            consensus = 1 if pos >= config["minimum_discovery_seed_support"] else (-1 if neg >= config["minimum_discovery_seed_support"] else 0)
            checkpoint_signs.append((checkpoint, consensus, signs))
        active = [entry for entry in checkpoint_signs if entry[1] != 0]
        for i in range(len(active)):
            for j in range(i + 1, len(active)):
                for k in range(j + 1, len(active)):
                    trio = [active[i], active[j], active[k]]
                    if trio[0][1] == trio[2][1] and trio[0][1] == -trio[1][1]:
                        candidates.append({
                            "family": family,
                            "checkpoints": [x[0] for x in trio],
                            "signs": [x[1] for x in trio],
                            "discovery_seed_signs": [x[2] for x in trio],
                        })
                        break
                if candidates and candidates[-1]["family"] == family:
                    break
            if candidates and candidates[-1]["family"] == family:
                break
    return candidates


def confirmation_support(candidate: dict, summary: dict, config: dict) -> dict:
    support_by_checkpoint = []
    for checkpoint, expected in zip(candidate["checkpoints"], candidate["signs"]):
        signs = [sign(summary[(seed, checkpoint, candidate["family"])], config) for seed in config["confirmation_seeds"]]
        support_by_checkpoint.append({"checkpoint": checkpoint, "expected": expected, "signs": signs, "support": signs.count(expected)})
    passed = all(x["support"] >= config["minimum_confirmation_seed_support"] for x in support_by_checkpoint)
    return {"passed": passed, "cells": support_by_checkpoint}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("FROZEN_CONFIG.json"))
    parser.add_argument("--discovery-dir", type=Path, required=True)
    parser.add_argument("--confirmation-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    discovery_paths = sorted(args.discovery_dir.glob("*.jsonl"))
    discovery_summary = summarize(load_records(discovery_paths))
    candidates = find_discovery_patterns(discovery_summary, config)
    gate = {
        "study_id": config["study_id"],
        "discovery_files": len(discovery_paths),
        "discovery_candidates": candidates,
        "confirmation_inspected": False,
        "decision": "NO_GO_NO_REENTRANT_DISCOVERY" if not candidates else "DISCOVERY_PASS_CONFIRMATION_REQUIRED",
    }
    if candidates and args.confirmation_dir:
        confirmation_paths = sorted(args.confirmation_dir.glob("*.jsonl"))
        confirmation_summary = summarize(load_records(confirmation_paths))
        results = [confirmation_support(candidate, confirmation_summary, config) for candidate in candidates]
        gate["confirmation_inspected"] = True
        gate["confirmation_files"] = len(confirmation_paths)
        gate["confirmation_results"] = results
        gate["decision"] = (
            "ANOMALY_DISCOVERY_PASS_NEEDS_SECOND_SCALE"
            if any(result["passed"] for result in results)
            else "NO_GO_CONFIRMATION_FAILED"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(gate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
