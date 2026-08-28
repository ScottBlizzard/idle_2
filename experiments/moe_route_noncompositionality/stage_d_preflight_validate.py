#!/usr/bin/env python3
"""Outcome-blind structural validation for Stage D preflight shards."""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
from transformers import AutoTokenizer

from stage_d_acquire import MODEL_ID, response_token_boundaries
from stage_d_common import h3_for_problem, matched_null_for_problem, sha256_file
from stage_d_predictors import cross_fitted_joint_predictions, model_factories


STAGE_E_HASHES = {
    "results/stage_e/conditions.csv": "71e2510334e0f58d731b84ac074fa6004b0ec4c6f50b8499d6e0baab1d994972",
    "results/stage_e/diagnostics.json": "b98f360ef5e171240a8d0bfd2ccfc3bf7a46a9bf850859b5d8d17cb25ff7e48e",
    "results/stage_e/stage_e_summary.json": "39d60089ac72691e3fd004d7248b92f3b93000534ed59722c2588bbd02ff5c59",
    "results/stage_e_generation/generation_records.jsonl": "88068e018be15e4e723fa0569298d4e2b56ce96ac46f5018d2366f1c22a7c56e",
    "results/stage_e_generation/stage_e_generation_summary.json": "1c06e76d3656fb7f021c78cd07aa2bc66fcd7b7603f5a6195ac7d0617a486d25",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-dir", type=Path, required=True)
    parser.add_argument("--stage-root", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def synthetic_records() -> list[dict[str, Any]]:
    records = []
    rng = np.random.default_rng(20260828)
    for problem_index in range(10):
        hidden = rng.normal(size=32).astype(np.float32).tolist()
        routes_i = [list(range(index, index + 8)) for index in range(6)]
        routes_j = [list(range(16 + index, 24 + index)) for index in range(6)]
        standard_i = list(range(32, 40))
        standard_j = list(range(40, 48))
        single_i = [0.05 * index + 0.01 * problem_index for index in range(6)]
        single_j = [-0.03 * index + 0.005 * problem_index for index in range(6)]
        for i in range(6):
            for j in range(6):
                summary_i = {
                    "sum": float(i), "mean": i / 8, "minimum": -0.1,
                    "maximum": 0.2 + i / 10, "rank_mean": 5 + i, "rank_maximum": 10 + i,
                }
                summary_j = {
                    "sum": float(j), "mean": j / 8, "minimum": -0.2,
                    "maximum": 0.3 + j / 10, "rank_mean": 6 + j, "rank_maximum": 11 + j,
                }
                interaction = 0.02 * np.sin((i + 1) * (j + 1) + problem_index)
                records.append(
                    {
                        "dataset": "synthetic",
                        "problem_id": f"p{problem_index:02d}",
                        "problem_ordinal": problem_index,
                        "fold": problem_index % 5,
                        "regime": "medium",
                        "layer_i": 3,
                        "layer_j": 8,
                        "route_i_index": i,
                        "route_j_index": j,
                        "route_i": routes_i[i],
                        "route_j": routes_j[j],
                        "standard_route_i": standard_i,
                        "standard_route_j": standard_j,
                        "single_effect_i": single_i[i],
                        "single_effect_j": single_j[j],
                        "joint_effect": single_i[i] + single_j[j] + interaction,
                        "router_summary_i": summary_i,
                        "router_summary_j": summary_j,
                        "standard_overlap_i": 0.0,
                        "standard_overlap_j": 0.0,
                        "pair_overlap": 0.0,
                        "normalized_layer_separation": 5 / 15,
                        "hidden_projection": hidden,
                    }
                )
    return records


def main() -> int:
    args = parse_args()
    checks: dict[str, Any] = {}
    checks["stage_e_hashes"] = {
        relative: sha256_file(args.stage_root / relative) == expected
        for relative, expected in STAGE_E_HASHES.items()
    }
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, cache_dir=args.cache_dir)
    shards = sorted((args.preflight_dir / "shards").rglob("*.json.gz"))
    counts = {"gsm8k": 0, "math500": 0}
    shard_checks = []
    for shard_path in shards:
        payload = json.loads(gzip.decompress(shard_path.read_bytes()).decode("utf-8"))
        dataset = payload["dataset"]
        counts[dataset] += 1
        selected = payload["selected_token"]
        response, surfaces, ends = response_token_boundaries(
            tokenizer, selected["response_ids"]
        )
        selected_index = int(selected["selected_response_index"])
        token_filter_ok = (
            response == selected["response"]
            and surfaces[selected_index] == selected["selected_token_surface"]
            and ends[selected_index] <= int(payload["answer_span_start"])
            and float(selected["selected_probability"]) <= 0.50
        )
        intervention = payload["interventions"]
        regimes_ok = True
        deterministic_matching_ok = True
        for regime in intervention["regimes"].values():
            pairs = regime["pairs"]
            regimes_ok = regimes_ok and (
                len(pairs) == 36
                and len(regime["singles_i"]) == 6
                and len(regime["singles_j"]) == 6
                and all(len(record["route_i"]) == 8 and len(record["route_j"]) == 8 for record in pairs)
                and all(len(record["hidden_projection"]) == 32 for record in pairs)
            )
            first = matched_null_for_problem(pairs)
            second = matched_null_for_problem(pairs)
            deterministic_matching_ok = deterministic_matching_ok and first == second
            h3_for_problem(pairs)
        shard_checks.append(
            {
                "token_filter": token_filter_ok,
                "route_grids": regimes_ok,
                "matched_null_deterministic": deterministic_matching_ok,
                "standard_replay": intervention["standard_replay_error"] <= 1e-4,
                "cached_uncached": intervention["maximum_cached_uncached_error"] <= 1e-4,
                "deterministic_rerun": intervention["deterministic_rerun_error"] <= 1e-6,
            }
        )
    checks["preflight_counts"] = counts
    checks["shards"] = shard_checks
    factories, parameter_count = model_factories()
    checks["predictor_parameter_matching"] = {
        "parameter_count": parameter_count,
        "models": sorted(factories),
        "pass": True,
    }
    fitted = cross_fitted_joint_predictions(synthetic_records())
    checks["synthetic_cross_fitting"] = {
        "rows": len(fitted.targets),
        "all_finite": all(np.all(np.isfinite(values)) for values in fitted.predictions.values()),
        "parameter_count": fitted.parameter_count,
    }
    passed = (
        all(checks["stage_e_hashes"].values())
        and counts == {"gsm8k": 2, "math500": 2}
        and len(shard_checks) == 4
        and all(all(item.values()) for item in shard_checks)
        and checks["synthetic_cross_fitting"]["all_finite"]
    )
    result = {
        "status": "STAGE_D_PREFLIGHT_PASS" if passed else "NO_GO_STAGE_D_PREFLIGHT",
        "scientific_interpretation_allowed": False,
        "checks": checks,
    }
    if args.output.exists():
        raise FileExistsError(args.output)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"status": result["status"]}))
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
