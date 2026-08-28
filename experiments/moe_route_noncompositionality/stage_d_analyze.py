#!/usr/bin/env python3
"""Automatic, problem-clustered Stage D analysis and gate generation."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import tempfile
import time
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np
import pandas as pd

from stage_d_common import (
    BASE_SEED,
    OLMOE_LAYER_PAIRS,
    benjamini_hochberg,
    bootstrap_mean,
    centered_bootstrap_p_value,
    h3_for_problem,
    matched_null_for_problem,
    percentile_interval,
    problem_weighted_reversal_effect,
    sha256_file,
)
from stage_d_predictors import cross_fitted_joint_predictions, problem_spearman


DATASET_CODES = {"gsm8k": 0, "math500": 1}
RESAMPLES = 10_000
FAMILY_SIZE = 32


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--maximum-cumulative-hours", type=float, default=6.0)
    parser.add_argument("--minimum-per-dataset", type=int, default=48)
    return parser.parse_args()


def write_json_new(path: Path, payload: Any) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite result: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False, suffix=".tmp"
    ) as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.flush()
        temporary = Path(handle.name)
    temporary.replace(path)


def load_shards(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    shards = sorted((root / "shards").glob("*/*.json.gz"))
    if not shards:
        raise RuntimeError("No acquisition shards found")
    trajectories = []
    records = []
    for shard in shards:
        checksum_path = shard.with_suffix(shard.suffix + ".sha256")
        expected = json.loads(checksum_path.read_text(encoding="utf-8"))["sha256"]
        observed = sha256_file(shard)
        if expected != observed:
            raise RuntimeError(f"Shard checksum mismatch: {shard}")
        payload = json.loads(gzip.decompress(shard.read_bytes()).decode("utf-8"))
        trajectories.append(
            {
                "dataset": payload["dataset"],
                "problem_id": payload["problem_id"],
                "problem_ordinal": payload["problem_ordinal"],
                "fold": payload["fold"],
                "sample_index": payload["sample_index"],
                "response_token_count": payload["response_token_count"],
                "selected_probability": payload["selected_token"]["selected_probability"],
            }
        )
        for regime, regime_payload in payload["interventions"]["regimes"].items():
            for record in regime_payload["pairs"]:
                item = dict(record)
                item["source_shard_sha256"] = observed
                records.append(item)
    return trajectories, records


def bootstrap_summary(
    values: Mapping[str, float], seed: int, null_boundary: float
) -> dict[str, Any]:
    estimate = float(np.mean(list(values.values())))
    samples = bootstrap_mean(values, RESAMPLES, seed)
    low, high = percentile_interval(samples)
    return {
        "estimate": estimate,
        "confidence_interval_95": [low, high],
        "null_boundary": null_boundary,
        "p_value_one_sided": centered_bootstrap_p_value(estimate, samples, null_boundary),
    }


def analyze_reversal(
    records_by_problem: Mapping[str, Sequence[Mapping[str, Any]]],
    hypothesis: str,
    seed: int,
) -> dict[str, Any]:
    matched = {
        problem: matched_null_for_problem(records)
        for problem, records in records_by_problem.items()
    }
    effect, per_problem, pair_count = problem_weighted_reversal_effect(matched, hypothesis)
    balances = np.asarray(
        [result["balance_mean_abs_by_coordinate"] for result in matched.values()], dtype=float
    )
    admissible = len(per_problem) >= 10 and pair_count >= 32 and np.isfinite(effect)
    if admissible:
        summary = bootstrap_summary(per_problem, seed, 0.10)
    else:
        summary = {
            "estimate": None,
            "confidence_interval_95": [None, None],
            "null_boundary": 0.10,
            "p_value_one_sided": 1.0,
        }
    summary.update(
        {
            "eligible_problem_clusters": len(per_problem),
            "eligible_route_pairs": pair_count,
            "admissible": admissible,
            "balance_mean_abs_by_coordinate": balances.mean(axis=0).tolist(),
            "per_problem": per_problem,
        }
    )
    low = summary["confidence_interval_95"][0]
    summary["threshold_pass_before_multiplicity"] = bool(
        admissible
        and summary["estimate"] is not None
        and summary["estimate"] >= 0.10
        and low is not None
        and low >= 0.10
    )
    return summary


def analyze_h3(
    records_by_problem: Mapping[str, Sequence[Mapping[str, Any]]], seed: int
) -> dict[str, Any]:
    problem_results = {
        problem: h3_for_problem(records) for problem, records in records_by_problem.items()
    }
    effects = {
        problem: float(result["success_difference"])
        for problem, result in problem_results.items()
    }
    summary = bootstrap_summary(effects, seed, 0.10)
    margin_gaps = [result["margin_gap"] for result in problem_results.values()]
    summary.update(
        {
            "problem_clusters": len(problem_results),
            "mean_margin_gap": float(np.mean(margin_gaps)),
            "median_margin_gap": float(np.median(margin_gaps)),
            "per_problem": problem_results,
        }
    )
    low = summary["confidence_interval_95"][0]
    summary["threshold_pass_before_multiplicity"] = bool(
        summary["estimate"] >= 0.10 and low > 0
    )
    return summary


def analyze_h4(records: Sequence[Mapping[str, Any]], seed: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    fitted = cross_fitted_joint_predictions(records)
    correlations = {
        name: problem_spearman(fitted.problem_ids, fitted.targets, predictions)
        for name, predictions in fitted.predictions.items()
    }
    compatibility = correlations["compatibility"]
    mlp_difference = {
        problem: compatibility[problem] - correlations["mlp"][problem]
        for problem in compatibility
    }
    gru_difference = {
        problem: compatibility[problem] - correlations["gru"][problem]
        for problem in compatibility
    }
    correlation_summary = bootstrap_summary(compatibility, seed, 0.40)
    mlp_summary = bootstrap_summary(mlp_difference, seed + 1, 0.0)
    gru_summary = bootstrap_summary(gru_difference, seed + 2, 0.0)
    component_p_values = [
        correlation_summary["p_value_one_sided"],
        mlp_summary["p_value_one_sided"],
        gru_summary["p_value_one_sided"],
    ]
    summary = {
        "parameter_count_each_neural_model": fitted.parameter_count,
        "compatibility_spearman": correlation_summary,
        "compatibility_minus_mlp_spearman": mlp_summary,
        "compatibility_minus_gru_spearman": gru_summary,
        "all_model_mean_problem_spearman": {
            name: float(np.mean(list(values.values()))) for name, values in correlations.items()
        },
        "p_value_one_sided": max(component_p_values),
        "problem_clusters": len(compatibility),
    }
    summary["threshold_pass_before_multiplicity"] = bool(
        correlation_summary["estimate"] >= 0.40
        and correlation_summary["confidence_interval_95"][0] >= 0.40
        and mlp_summary["confidence_interval_95"][0] > 0
        and gru_summary["confidence_interval_95"][0] > 0
    )
    prediction_rows = []
    for index, record in enumerate(records):
        prediction_rows.append(
            {
                "dataset": record["dataset"],
                "regime": record["regime"],
                "problem_id": record["problem_id"],
                "route_i_index": record["route_i_index"],
                "route_j_index": record["route_j_index"],
                "target_joint_effect": fitted.targets[index],
                **{name: values[index] for name, values in fitted.predictions.items()},
            }
        )
    return summary, prediction_rows


def scalar_route_row(record: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "dataset": record["dataset"],
        "problem_id": record["problem_id"],
        "problem_ordinal": record["problem_ordinal"],
        "fold": record["fold"],
        "regime": record["regime"],
        "layer_i": record["layer_i"],
        "layer_j": record["layer_j"],
        "route_i_index": record["route_i_index"],
        "route_j_index": record["route_j_index"],
        "route_i": record["route_i"],
        "route_j": record["route_j"],
        "standard_route_i": record["standard_route_i"],
        "standard_route_j": record["standard_route_j"],
        "single_effect_i": record["single_effect_i"],
        "single_effect_j": record["single_effect_j"],
        "joint_effect": record["joint_effect"],
        "interaction_residual": record["interaction_residual"],
        "joint_margin": record["joint_metrics"]["margin"],
        "joint_log_probability": record["joint_metrics"]["log_probability"],
        "joint_probability": record["joint_metrics"]["probability"],
        "joint_kl_from_standard": record["joint_metrics"]["kl_from_standard"],
        "joint_final_residual_norm": record["joint_final_residual_norm"],
        "standard_overlap_i": record["standard_overlap_i"],
        "standard_overlap_j": record["standard_overlap_j"],
        "pair_overlap": record["pair_overlap"],
        "selected_standard_probability": record["selected_standard_probability"],
        "source_shard_sha256": record["source_shard_sha256"],
    }


def main() -> int:
    args = parse_args()
    analysis_start = time.perf_counter()
    resolved = json.loads((args.input_dir / "config_resolved.json").read_text(encoding="utf-8"))
    acquisition_seconds = float(resolved["elapsed_seconds"])
    trajectories, records = load_shards(args.input_dir)
    counts = {
        dataset: sum(trajectory["dataset"] == dataset for trajectory in trajectories)
        for dataset in DATASET_CODES
    }
    if any(count < args.minimum_per_dataset for count in counts.values()):
        raise RuntimeError(f"Inadmissible retained counts: {counts}")
    route_path = args.input_dir / "route_effects.parquet"
    if route_path.exists():
        raise FileExistsError(route_path)
    pd.DataFrame([scalar_route_row(record) for record in records]).to_parquet(
        route_path, index=False
    )

    cells: dict[str, Any] = {}
    p_value_entries: list[tuple[str, str, str, float]] = []
    all_prediction_rows = []
    problem_summary_rows = []
    for dataset, dataset_code in DATASET_CODES.items():
        for regime_index, regime in enumerate(OLMOE_LAYER_PAIRS):
            cell_records = [
                record
                for record in records
                if record["dataset"] == dataset and record["regime"] == regime
            ]
            records_by_problem: dict[str, list[Mapping[str, Any]]] = {}
            for record in cell_records:
                records_by_problem.setdefault(str(record["problem_id"]), []).append(record)
            if any(len(group) != 36 for group in records_by_problem.values()):
                raise RuntimeError(f"Incomplete route grid in {dataset}/{regime}")
            seed = BASE_SEED + 1_000_003 * dataset_code + 101 * regime_index
            h1 = analyze_reversal(records_by_problem, "h1", seed)
            h2 = analyze_reversal(records_by_problem, "h2", seed)
            h3 = analyze_h3(records_by_problem, seed)
            h4, prediction_rows = analyze_h4(cell_records, seed)
            all_prediction_rows.extend(prediction_rows)
            cell_key = f"{dataset}/{regime}"
            cells[cell_key] = {"H1": h1, "H2": h2, "H3": h3, "H4": h4}
            for hypothesis, result in cells[cell_key].items():
                p_value_entries.append(
                    (dataset, regime, hypothesis, float(result["p_value_one_sided"]))
                )
            for problem, group in records_by_problem.items():
                problem_summary_rows.append(
                    {
                        "dataset": dataset,
                        "regime": regime,
                        "problem_id": problem,
                        "route_pairs": len(group),
                        "h1_effect": h1["per_problem"].get(problem),
                        "h2_effect": h2["per_problem"].get(problem),
                        "h3_success_difference": h3["per_problem"][problem]["success_difference"],
                        "h3_margin_gap": h3["per_problem"][problem]["margin_gap"],
                    }
                )

    if len(p_value_entries) != FAMILY_SIZE:
        raise RuntimeError(f"Expected {FAMILY_SIZE} p-values, found {len(p_value_entries)}")
    adjusted = benjamini_hochberg([entry[3] for entry in p_value_entries])
    for entry, q_value in zip(p_value_entries, adjusted):
        dataset, regime, hypothesis, _ = entry
        result = cells[f"{dataset}/{regime}"][hypothesis]
        result["q_value_benjamini_hochberg"] = q_value
        result["pass"] = bool(
            result["threshold_pass_before_multiplicity"] and q_value <= 0.05
        )

    passing_regimes = []
    for regime in OLMOE_LAYER_PAIRS:
        if all(
            cells[f"{dataset}/{regime}"][hypothesis]["pass"]
            for dataset in DATASET_CODES
            for hypothesis in ("H1", "H2", "H3", "H4")
        ):
            passing_regimes.append(regime)

    analysis_seconds = time.perf_counter() - analysis_start
    cumulative_seconds = acquisition_seconds + analysis_seconds
    compute_pass = cumulative_seconds <= args.maximum_cumulative_hours * 3600.0
    discovery_pass = len(passing_regimes) >= 3 and compute_pass
    status = "GO_STAGE_C_ELIGIBLE" if discovery_pass else "NO_GO_NO_INTERACTION_LAW"
    predictions_path = args.input_dir / "h4_predictions.parquet"
    pd.DataFrame(all_prediction_rows).to_parquet(predictions_path, index=False)
    with (args.input_dir / "problem_summary.csv").open(
        "x", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(problem_summary_rows[0]))
        writer.writeheader()
        writer.writerows(problem_summary_rows)
    gates = {
        "status": status,
        "counts": counts,
        "passing_regimes_on_both_datasets": passing_regimes,
        "passing_regime_count": len(passing_regimes),
        "required_passing_regime_count": 3,
        "compute": {
            "acquisition_seconds": acquisition_seconds,
            "analysis_seconds": analysis_seconds,
            "cumulative_seconds": cumulative_seconds,
            "maximum_seconds": args.maximum_cumulative_hours * 3600.0,
            "pass": compute_pass,
        },
        "multiple_testing": {
            "method": "Benjamini-Hochberg",
            "family_size": FAMILY_SIZE,
            "false_discovery_rate": 0.05,
        },
        "cells": cells,
    }
    write_json_new(args.input_dir / "gates.json", gates)
    final = {
        "status": status,
        "stage_c_authorized": False,
        "scientific_interpretation_allowed": True,
        "passing_regimes_on_both_datasets": passing_regimes,
        "required_passing_regimes": 3,
        "compute_pass": compute_pass,
        "artifact_sha256": {
            "route_effects.parquet": sha256_file(route_path),
            "h4_predictions.parquet": sha256_file(predictions_path),
            "problem_summary.csv": sha256_file(args.input_dir / "problem_summary.csv"),
            "gates.json": sha256_file(args.input_dir / "gates.json"),
        },
    }
    write_json_new(args.input_dir / "FINAL_GATE.json", final)
    print(json.dumps({"status": status, "passing_regime_count": len(passing_regimes)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
