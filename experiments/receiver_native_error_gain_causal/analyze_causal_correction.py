#!/usr/bin/env python3
"""Apply the frozen paired causal error-gain analysis and binding gate."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.endogenous_failure_conditioning.common import read_jsonl, sha256_file, write_jsonl
from experiments.moe_route_noncompositionality.stage_d_common import verify_gsm8k


def paired_rows(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in rows:
        grouped[str(row["pair_id"])][str(row["condition"])] = row
    pairs = []
    for pair_id, conditions in grouped.items():
        if set(conditions) != {"high_native", "low_native"}:
            raise RuntimeError(f"Incomplete treatment pair: {pair_id}")
        high = conditions["high_native"]
        low = conditions["low_native"]
        pairs.append({
            "pair_id": pair_id,
            "problem_key": high["problem_key"],
            "corrector_key": high["corrector_key"],
            "difference": float(high[key]) - float(low[key]),
        })
    return pairs


def paired_cluster_bootstrap(
    pairs: list[dict[str, Any]], repetitions: int, seed: int
) -> dict[str, Any]:
    by_problem: dict[str, list[float]] = defaultdict(list)
    for row in pairs:
        by_problem[str(row["problem_key"])].append(float(row["difference"]))
    keys = sorted(by_problem)
    point = float(np.mean([row["difference"] for row in pairs]))
    rng = np.random.default_rng(seed)
    draws = []
    for _ in range(repetitions):
        sample = rng.choice(keys, size=len(keys), replace=True)
        values = [value for key in sample for value in by_problem[str(key)]]
        draws.append(float(np.mean(values)))
    return {
        "high_native_minus_low_native": point,
        "ci95": list(map(float, np.quantile(draws, [0.025, 0.975]))),
        "pairs": len(pairs),
        "problem_clusters": len(keys),
    }


def continuous_nll_model(df: pd.DataFrame) -> dict[str, Any]:
    formula = (
        "retained_source_error ~ mean_nll_z + C(problem_key) + "
        "C(corrector_key) + C(generator_key)"
    )
    result = smf.glm(formula, data=df, family=sm.families.Binomial()).fit(
        maxiter=200, cov_type="cluster", cov_kwds={"groups": df["problem_key"]}
    )
    if not result.converged:
        raise RuntimeError("Continuous-NLL GLM failed to converge")
    coefficient = float(result.params["mean_nll_z"])
    standard_error = float(result.bse["mean_nll_z"])
    if not np.isfinite(coefficient) or not np.isfinite(standard_error):
        raise RuntimeError("Non-finite continuous-NLL inference")
    return {
        "coefficient": coefficient,
        "cluster_problem_se": standard_error,
        "ci95": [
            coefficient - 1.96 * standard_error,
            coefficient + 1.96 * standard_error,
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=Path, required=True)
    parser.add_argument("--manipulation-gate", type=Path, required=True)
    parser.add_argument("--correction-dir", type=Path, required=True)
    parser.add_argument("--parent-config", type=Path, required=True)
    parser.add_argument("--frozen", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    final_path = args.output_dir / "FINAL_GATE.json"
    if final_path.exists():
        raise RuntimeError("Refusing to overwrite an existing causal final gate")

    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    parent = json.loads(args.parent_config.read_text(encoding="utf-8"))
    manipulation = json.loads(args.manipulation_gate.read_text(encoding="utf-8"))
    if manipulation["status"] != "MANIPULATION_PASS_AUTHORIZE_CORRECTION":
        raise RuntimeError("Manipulation gate did not authorize correction")
    if sha256_file(args.selected) != manipulation["selected_sha256"]:
        raise RuntimeError("Selected-pair hash mismatch")
    selected = {str(row["pair_id"]): row for row in read_jsonl(args.selected)}

    raw = []
    output_hashes = {}
    expected_per_model = int(frozen["expected_selected_cells"]) // len(parent["models"]) * 2
    for model_key, spec in parent["models"].items():
        path = args.correction_dir / "outputs" / f"{model_key}.jsonl"
        manifest = json.loads(path.with_suffix(".manifest.json").read_text(encoding="utf-8"))
        if manifest["status"] != "CAUSAL_CORRECTION_MODEL_COMPLETE":
            raise RuntimeError(f"Incomplete correction manifest for {model_key}")
        if manifest["model_revision"] != spec["revision"]:
            raise RuntimeError(f"Revision mismatch for {model_key}")
        if manifest["total_cases"] != expected_per_model:
            raise RuntimeError(f"Unexpected row count for {model_key}")
        if sha256_file(path) != manifest["output_sha256"]:
            raise RuntimeError(f"Correction output hash mismatch for {model_key}")
        output_hashes[model_key] = manifest["output_sha256"]
        raw.extend(read_jsonl(path))
    if len(raw) != int(frozen["expected_selected_cells"]) * 2:
        raise RuntimeError(f"Expected 960 correction rows, got {len(raw)}")

    scored = []
    bad_count = 0
    for row in raw:
        pair = selected[str(row["pair_id"])]
        correct, extracted = verify_gsm8k(row["response"], pair["gold_answer"])
        parsed = extracted is not None
        bad = (not parsed) or bool(row["hit_token_limit"])
        source_answers = {str(value) for value in pair["source_extracted_answer"]}
        scored.append({
            **row,
            "gold_answer": pair["gold_answer"],
            "correct": bool(correct),
            "parsed": parsed,
            "extracted_answer": None if extracted is None else extracted.value,
            "bad_parse_or_truncation": bad,
            "retained_source_error": bool(
                extracted is not None and str(extracted.value) in source_answers
            ),
        })
        bad_count += int(bad)

    results = {}
    for key in ("retained_source_error", "correct"):
        pairs = paired_rows(scored, key)
        overall = paired_cluster_bootstrap(
            pairs, int(frozen["bootstrap_repetitions"]), int(frozen["seed"])
        )
        by_corrector = {}
        for model_key in sorted(parent["models"]):
            subset = [row for row in pairs if row["corrector_key"] == model_key]
            by_corrector[model_key] = float(np.mean([row["difference"] for row in subset]))
        results[key] = {"overall": overall, "by_corrector": by_corrector}

    frame = pd.DataFrame(scored)
    frame["retained_source_error"] = frame["retained_source_error"].astype(int)
    frame["mean_nll_z"] = frame.groupby("corrector_key")["mean_nll"].transform(
        lambda values: (values - values.mean()) / values.std(ddof=0)
    )
    nll_model = continuous_nll_model(frame)
    bad_rate = bad_count / len(scored)
    primary = results["retained_source_error"]["overall"]
    correctors_positive = sum(
        value > 0 for value in results["retained_source_error"]["by_corrector"].values()
    )
    if bad_rate > float(frozen["maximum_parser_or_truncation_rate"]):
        decision = "NO_GO_ENGINEERING"
    elif not (
        primary["high_native_minus_low_native"]
        >= float(frozen["minimum_primary_retention_contrast"])
        and primary["ci95"][0] > 0
        and correctors_positive >= int(frozen["minimum_correctors_positive"])
        and nll_model["ci95"][1] < 0
    ):
        decision = "KILL_NO_CAUSAL_ERROR_GAIN"
    else:
        decision = "ADVANCE_CROSS_PROVIDER_CAUSAL_REPLICATION"

    final = {
        "status": decision,
        "scope": "WHITESPACE_ONLY_CAUSAL_KILL_TEST",
        "rows": len(scored),
        "parser_or_truncation_rate": bad_rate,
        "correctors_with_positive_retention_contrast": correctors_positive,
        "outcomes": results,
        "continuous_nll_model": nll_model,
        "input_hashes": {
            "frozen": sha256_file(args.frozen),
            "selected": sha256_file(args.selected),
            "manipulation_gate": sha256_file(args.manipulation_gate),
            "correction_outputs": output_hashes,
        },
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.output_dir / "SCORED_CORRECTIONS.jsonl", scored)
    final_path.write_text(json.dumps(final, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(final, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

