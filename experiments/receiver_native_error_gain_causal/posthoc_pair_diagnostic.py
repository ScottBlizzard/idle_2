#!/usr/bin/env python3
"""Transparent post-hoc decomposition of the passed manipulation and failed paired effect."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import statsmodels.api as sm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scored", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise RuntimeError("Refusing to overwrite a post-hoc diagnostic")

    frame = pd.read_json(args.scored, lines=True)
    wide = frame.pivot(index="pair_id", columns="condition", values="retained_source_error")
    high_only = int(((wide.high_native == 1) & (wide.low_native == 0)).sum())
    low_only = int(((wide.high_native == 0) & (wide.low_native == 1)).sum())
    metadata = (
        frame[frame.condition == "high_native"]
        [["pair_id", "problem_key", "corrector_key", "mean_nll"]]
        .set_index("pair_id")
        .rename(columns={"mean_nll": "nll_high_native"})
    )
    metadata["nll_low_native"] = (
        frame[frame.condition == "low_native"].set_index("pair_id")["mean_nll"]
    )
    metadata["outcome_difference"] = (
        wide.high_native.astype(int) - wide.low_native.astype(int)
    )
    metadata["nll_gap"] = metadata.nll_low_native - metadata.nll_high_native
    fit = sm.OLS(
        metadata.outcome_difference, sm.add_constant(metadata.nll_gap)
    ).fit(cov_type="cluster", cov_kwds={"groups": metadata.problem_key})
    interval = fit.conf_int().loc["nll_gap"]
    metadata["gap_quartile"] = pd.qcut(metadata.nll_gap, 4, duplicates="drop")
    quartiles = []
    for label, group in metadata.groupby("gap_quartile", observed=True):
        quartiles.append({
            "interval": str(label),
            "pairs": len(group),
            "mean_retention_difference": float(group.outcome_difference.mean()),
        })
    result = {
        "status": "POST_HOC_DOES_NOT_CHANGE_BINDING_GATE",
        "discordance": {
            "high_native_only_retains": high_only,
            "low_native_only_retains": low_only,
            "same_outcome": int((wide.high_native == wide.low_native).sum()),
            "discordant_pairs": high_only + low_only,
            "net_discordance": high_only - low_only,
        },
        "gap_dose_model": {
            "ols_slope_per_nat_token": float(fit.params["nll_gap"]),
            "problem_cluster_ci95": [float(interval.iloc[0]), float(interval.iloc[1])],
            "median_nll_gap": float(metadata.nll_gap.median()),
            "quartiles": quartiles,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
