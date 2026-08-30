#!/usr/bin/env python3
"""Analyze the frozen receiver-likelihood diagnostic with clustered inference."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from experiments.endogenous_failure_conditioning.common import read_jsonl, sha256_file


def logistic(df: pd.DataFrame, formula: str) -> dict[str, Any]:
    robust = smf.logit(formula, data=df).fit(
        disp=False, cov_type="cluster", cov_kwds={"groups": df["problem_key"]}
    )
    names = list(robust.params.index)
    params = dict(zip(names, map(float, robust.params)))
    ses = dict(zip(names, map(float, robust.bse)))
    cis = {
        name: [params[name] - 1.96 * ses[name], params[name] + 1.96 * ses[name]]
        for name in names
    }
    return {"n": len(df), "params": params, "se_cluster_problem": ses, "ci95": cis}


def cluster_bootstrap_nll_difference(
    df: pd.DataFrame, repetitions: int, seed: int
) -> dict[str, Any]:
    def statistic(frame: pd.DataFrame) -> float:
        return float(
            frame.loc[frame.same_lineage, "mean_nll_z"].mean()
            - frame.loc[~frame.same_lineage, "mean_nll_z"].mean()
        )

    unique = sorted(df.problem_key.unique())
    grouped = {key: df[df.problem_key == key] for key in unique}
    rng = np.random.default_rng(seed)
    draws = []
    for _ in range(repetitions):
        sample = rng.choice(unique, size=len(unique), replace=True)
        draws.append(statistic(pd.concat([grouped[str(key)] for key in sample], ignore_index=True)))
    return {
        "same_minus_cross_z_nll": statistic(df),
        "ci95": list(map(float, np.quantile(draws, [0.025, 0.975]))),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--likelihood-dir", type=Path, required=True)
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--scored", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    likelihood_rows = []
    output_hashes = {}
    for model_key, spec in config["models"].items():
        path = args.likelihood_dir / "outputs" / f"{model_key}.jsonl"
        manifest_path = path.with_suffix(".manifest.json")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest["status"] != "LIKELIHOOD_MODEL_COMPLETE" or manifest["rows"] != 240:
            raise RuntimeError(f"Incomplete likelihood manifest for {model_key}")
        if manifest["model_revision"] != spec["revision"]:
            raise RuntimeError(f"Revision mismatch for {model_key}")
        if sha256_file(path) != manifest["output_sha256"]:
            raise RuntimeError(f"Hash mismatch for {model_key}")
        likelihood_rows.extend(read_jsonl(path))
        output_hashes[model_key] = manifest["output_sha256"]
    if len(likelihood_rows) != 960:
        raise RuntimeError(f"Expected 960 likelihood cells, got {len(likelihood_rows)}")

    likelihood = {
        (row["error_id"], row["receiver_key"]): row for row in likelihood_rows
    }
    bank = {row["error_id"]: row for row in read_jsonl(args.bank) if row["domain"] == "gsm8k"}
    joined = []
    for row in read_jsonl(args.scored):
        if row["domain"] != "gsm8k":
            continue
        score = likelihood[(row["error_id"], row["corrector_key"])]
        source_answers = {str(x) for x in bank[row["error_id"]]["source_extracted_answer"]}
        joined.append({
            **row,
            "same_lineage": bool(score["same_lineage"]),
            "mean_nll": float(score["mean_nll"]),
            "trace_tokens": int(score["trace_tokens"]),
            "retained_source_error": row.get("extracted_answer") in source_answers,
        })
    df = pd.DataFrame(joined)
    if len(df) != 1920:
        raise RuntimeError(f"Expected 1920 joined rows, got {len(df)}")
    df["mean_nll_z"] = df.groupby("corrector_key")["mean_nll"].transform(
        lambda x: (x - x.mean()) / x.std(ddof=0)
    )
    df["log_trace_tokens"] = np.log(df["trace_tokens"])
    df["retained_source_error"] = df["retained_source_error"].astype(int)

    results: dict[str, Any] = {
        "status": "POST_HOC_DIAGNOSTIC",
        "rows": len(df),
        "input_hashes": {
            "bank": sha256_file(args.bank),
            "parent_scored": sha256_file(args.scored),
            "config": sha256_file(args.config),
            "likelihood_outputs": output_hashes,
        },
        "wrappers": {},
    }
    base_formula = (
        "retained_source_error ~ same_lineage + C(problem_key) + "
        "C(corrector_key) + C(generator_key) + log_trace_tokens"
    )
    full_formula = base_formula + " + mean_nll_z"
    for wrapper in ("external_neutral", "assistant_history"):
        sub = df[df.wrapper == wrapper].copy()
        base = logistic(sub, base_formula)
        full = logistic(sub, full_formula)
        base_same = base["params"]["same_lineage[T.True]"]
        full_same = full["params"]["same_lineage[T.True]"]
        attenuation = (base_same - full_same) / base_same if base_same != 0 else float("nan")
        leave_one_out = {}
        for corrector in sorted(sub.corrector_key.unique()):
            reduced = sub[sub.corrector_key != corrector].copy()
            leave_one_out[corrector] = logistic(reduced, full_formula)["params"]["mean_nll_z"]
        results["wrappers"][wrapper] = {
            "same_vs_cross_likelihood": cluster_bootstrap_nll_difference(
                sub.drop_duplicates(["error_id", "corrector_key"]), 10000, 20260830
            ),
            "base_model": base,
            "nll_model": full,
            "same_coefficient_attenuation_fraction": float(attenuation),
            "leave_one_corrector_out_nll_coefficients": leave_one_out,
        }

    external = results["wrappers"]["external_neutral"]
    nll_ci = external["nll_model"]["ci95"]["mean_nll_z"]
    same_nll_ci = external["same_vs_cross_likelihood"]["ci95"]
    passes = (
        nll_ci[1] < 0
        and same_nll_ci[1] < 0
        and external["same_coefficient_attenuation_fraction"] >= 0.25
    )
    results["decision"] = (
        "PROMISING_REQUIRES_CAUSAL_INTERVENTION"
        if passes else "KILL_NATIVE_LIKELIHOOD_EXPLANATION"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
