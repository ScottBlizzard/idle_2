from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import pandas as pd


def one(frame: pd.DataFrame, **filters) -> pd.Series | None:
    subset = frame
    for key, value in filters.items():
        subset = subset[subset[key] == value]
    if len(subset) != 1:
        return None
    return subset.iloc[0]


def finite(value) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--contrasts", type=Path, required=True)
    parser.add_argument("--process", type=Path, required=True)
    parser.add_argument("--pair-results", type=Path, required=True)
    parser.add_argument("--replay-summary", type=Path, required=True)
    parser.add_argument("--diagnostic-summary", type=Path, required=True)
    parser.add_argument("--intervention-summary", type=Path, required=True)
    parser.add_argument("--benchmark-audit", type=Path, required=True)
    parser.add_argument("--model-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    summary = pd.read_csv(args.summary)
    contrasts = pd.read_csv(args.contrasts)
    process = pd.read_csv(args.process)
    pair_results = pd.read_csv(args.pair_results)
    replay = pd.read_csv(args.replay_summary)
    diagnostics = pd.read_csv(args.diagnostic_summary)
    intervention = pd.read_csv(args.intervention_summary) if args.intervention_summary.stat().st_size else pd.DataFrame()
    benchmark = json.loads(args.benchmark_audit.read_text(encoding="utf-8"))
    manifest = json.loads(args.model_manifest.read_text(encoding="utf-8"))
    primary_models = [model["family"] for model in manifest["models"] if model["role"] == "primary"]

    model_results = {}
    negative_candidates = []
    positive_candidates = []
    for model in primary_models:
        c = one(summary, model_id=model, pack="A", condition="C", template_mode="native", structured=True)
        d = one(summary, model_id=model, pack="A", condition="D", template_mode="native", structured=True)
        dc = one(contrasts, model_id=model, pack="A", contrast="D-C")
        interaction = one(contrasts, model_id=model, pack="A", contrast="interaction")
        pack_b = one(contrasts, model_id=model, pack="B", contrast="D-C")
        proc = one(process, model_id=model)
        rep = one(replay, model_id=model)
        plain_c = one(diagnostics, model_id=model, pack="A", condition="C", template_mode="plain", structured=True)
        plain_d = one(diagnostics, model_id=model, pack="A", condition="D", template_mode="plain", structured=True)
        unconstrained_c = one(
            diagnostics,
            model_id=model,
            pack="A",
            condition="C",
            template_mode="native",
            structured=False,
        )
        unconstrained_d = one(
            diagnostics,
            model_id=model,
            pack="A",
            condition="D",
            template_mode="native",
            structured=False,
        )
        if any(
            value is None
            for value in (
                c,
                d,
                dc,
                interaction,
                pack_b,
                proc,
                rep,
                plain_c,
                plain_d,
                unconstrained_c,
                unconstrained_d,
            )
        ):
            model_results[model] = {"complete": False, "reason": "missing required result cell"}
            continue

        c_pair_errors = int(round(c["pairs"] * (1 - c["pair_accuracy"])))
        plain_effect = float(plain_d["pair_accuracy"] - plain_c["pair_accuracy"])
        unconstrained_effect = float(
            unconstrained_d["pair_accuracy"] - unconstrained_c["pair_accuracy"]
        )
        primary_effect = float(dc["difference"])
        template_stable = primary_effect == 0 or plain_effect == 0 or (primary_effect > 0) == (plain_effect > 0)
        format_stable = (
            primary_effect == 0
            or unconstrained_effect == 0
            or (primary_effect > 0) == (unconstrained_effect > 0)
        )
        admissible = bool(
            c["schema_valid_rate"] >= 0.99
            and d["schema_valid_rate"] >= 0.99
            and c["truncation_rate"] <= 0.005
            and d["truncation_rate"] <= 0.005
            and abs(c["truncation_rate"] - d["truncation_rate"]) <= 0.01
            and c["pair_accuracy"] >= 0.65
            and c_pair_errors >= 3
            and benchmark["metadata_probe_accuracy"] <= 0.55
            and rep["token_match_rate"] >= 0.995
            and template_stable
            and format_stable
        )

        difficulty_effects = []
        model_pairs = pair_results[
            (pair_results.model_id == model)
            & (pair_results.pack == "A")
            & (pair_results.condition.isin(["C", "D"]))
            & (pair_results.template_mode == "native")
            & (pair_results.structured)
        ]
        for difficulty in (1, 2, 3):
            block = model_pairs[model_pairs.difficulty == difficulty]
            pivot = block.pivot_table(index="pair_id", columns="condition", values="pair_correct", aggfunc="first").dropna()
            difficulty_effects.append(float((pivot.D.astype(float) - pivot.C.astype(float)).mean()) if not pivot.empty else math.nan)

        correction = one(intervention, model_id=model, kind="correction") if not intervention.empty else None
        injection = one(intervention, model_id=model, kind="injection") if not intervention.empty else None
        if correction is not None:
            eligible = correction["pairs"] * (1 - correction["original_accuracy"])
            rescue_fraction = correction["rescued"] / eligible if eligible else 0.0
        else:
            rescue_fraction = 0.0
        process_pass = bool(
            proc["inactive_operator_rate_change"] >= 0.08
            and finite(proc["excess_error_fraction"])
            and proc["excess_error_fraction"] >= 0.30
            and correction is not None
            and correction["modified_minus_original"] >= 0.20
            and rescue_fraction >= 0.50
            and injection is not None
            and injection["modified_minus_original"] < 0
        )
        wording_negative = bool(
            pack_b["difference"] <= -0.07
            and abs(pack_b["difference"]) >= 0.70 * abs(primary_effect)
            or (primary_effect <= -0.20 and pack_b["difference"] <= -0.10)
        )
        wording_positive = bool(pack_b["difference"] > 0)
        negative = bool(
            admissible
            and primary_effect <= -0.10
            and dc["ci90_high"] < 0
            and dc["pvalue_holm"] < 0.10
            and wording_negative
            and interaction["difference"] < 0
            and process_pass
            and sum(effect < 0 for effect in difficulty_effects if finite(effect)) >= 2
        )
        positive = bool(
            admissible
            and primary_effect >= 0.08
            and dc["ci90_low"] > 0
            and wording_positive
        )
        if negative:
            negative_candidates.append(model)
        if positive:
            positive_candidates.append(model)
        model_results[model] = {
            "complete": True,
            "admissible": admissible,
            "D_minus_C": primary_effect,
            "pack_B_D_minus_C": float(pack_b["difference"]),
            "interaction": float(interaction["difference"]),
            "plain_template_D_minus_C": plain_effect,
            "unconstrained_D_minus_C": unconstrained_effect,
            "difficulty_D_minus_C": difficulty_effects,
            "process_pass": process_pass,
            "rescue_fraction": rescue_fraction,
            "negative_family_pass": negative,
            "positive_family_pass": positive,
        }

    strong_negative = [
        model
        for model in negative_candidates
        if (
            one(contrasts, model_id=model, pack="A", contrast="D-C")["ci95_high"] < 0
            and one(contrasts, model_id=model, pack="A", contrast="D-C")["pvalue_holm"] < 0.05
        )
    ]
    complete = all(model_results.get(model, {}).get("complete") for model in primary_models)
    go = bool(
        complete
        and len(negative_candidates) >= 2
        and len(strong_negative) >= 1
        and len(positive_candidates) >= 1
    )
    result = {
        "verdict": "GO_TO_GAMEBENCH" if go else "NO_GO_STOP_CURRENT_SEED",
        "all_required_results_complete": complete,
        "negative_families": negative_candidates,
        "strong_negative_families": strong_negative,
        "positive_families": positive_candidates,
        "models": model_results,
        "binding_note": (
            "A GO authorizes only the preregistered GameBench state-level stage."
            if go
            else "Do not expand models, prompts, subgroups, or benchmarks to rescue this seed."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
