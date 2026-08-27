from __future__ import annotations

import argparse
import glob
import json
import math
import random
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Sequence

import pandas as pd
from scipy.stats import binomtest, wilcoxon


PRIMARY_CONTRASTS = ("D-C", "interaction", "E-C")


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def resolve_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        matches = glob.glob(pattern)
        paths.extend(Path(match) for match in (matches or [pattern]))
    return sorted(set(paths))


def as_fraction(value) -> Fraction | None:
    if not isinstance(value, str):
        return None
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError):
        return None


def expected_node_order(record: dict) -> list[str]:
    nodes = []
    for action in record["action_order"]:
        for index, _ in enumerate(record["actions"][action]["outcomes"], start=1):
            nodes.append(f"NODE_{action[-1]}{index}")
    return nodes


def parse_and_score(record: dict, prediction: dict) -> dict:
    base = {
        "id": record["id"],
        "pair_id": record["pair_id"],
        "skin": record["skin"],
        "difficulty": record["difficulty"],
        "active_controller": record["active_controller"],
        "optimal_action": record["oracle"]["optimal_action"],
        "model_id": prediction["model_id"],
        "pack": prediction["pack"],
        "condition": prediction["condition"],
        "template_mode": prediction.get("template_mode", "native"),
        "structured": bool(prediction.get("structured", True)),
        "stop_reason": prediction.get("stop_reason", "unknown"),
        "output_tokens": prediction.get("output_tokens"),
        "prompt_sha256": prediction.get("prompt_sha256"),
    }
    try:
        payload = json.loads(prediction.get("text", ""))
    except json.JSONDecodeError:
        return {
            **base,
            "schema_valid": False,
            "controller_correct": False,
            "operator_correct": False,
            "selected_values_correct": False,
            "action_values_correct": False,
            "final_correct": False,
            "task_correct": False,
            "full_trace_correct": False,
            "inactive_operator": False,
            "inactive_operator_nodes": 0,
            "error_category": "schema_format",
            "prediction": None,
        }

    required = {"controller", "nodes", "actions", "final_action"}
    schema_valid = (
        isinstance(payload, dict)
        and set(payload) == required
        and isinstance(payload.get("nodes"), list)
        and isinstance(payload.get("actions"), list)
        and len(payload.get("nodes", [])) == 4
        and len(payload.get("actions", [])) == 2
        and all(isinstance(item, dict) and set(item) == {"node", "operator", "selected_value"} for item in payload.get("nodes", []))
        and all(isinstance(item, dict) and set(item) == {"action", "expected_value"} for item in payload.get("actions", []))
    )
    if not schema_valid:
        return {
            **base,
            "schema_valid": False,
            "controller_correct": False,
            "operator_correct": False,
            "selected_values_correct": False,
            "action_values_correct": False,
            "final_correct": False,
            "task_correct": False,
            "full_trace_correct": False,
            "inactive_operator": False,
            "inactive_operator_nodes": 0,
            "error_category": "schema_format",
            "prediction": payload.get("final_action") if isinstance(payload, dict) else None,
        }

    controller_correct = payload["controller"] == record["active_controller"]
    expected_nodes = record["oracle"]["nodes"]
    node_map = {item["node"]: item for item in payload["nodes"]}
    node_complete = set(node_map) == set(expected_node_order(record)) and len(node_map) == 4
    expected_operator = record["oracle"]["operator"]
    inactive_operator_nodes = sum(
        item.get("operator") in {"OP_X", "OP_Y"} and item.get("operator") != expected_operator
        for item in payload["nodes"]
    )
    operator_correct = node_complete and all(
        node_map[node].get("operator") == expected_nodes[node]["operator"] for node in expected_nodes
    )
    selected_values_correct = node_complete and all(
        as_fraction(node_map[node].get("selected_value"))
        == Fraction(expected_nodes[node]["selected_value"])
        for node in expected_nodes
    )

    action_map = {item["action"]: item for item in payload["actions"]}
    action_complete = set(action_map) == {"ACTION_P", "ACTION_Q"} and len(action_map) == 2
    action_values_correct = action_complete and all(
        as_fraction(action_map[action].get("expected_value"))
        == Fraction(record["oracle"]["root_values"][action])
        for action in ("ACTION_P", "ACTION_Q")
    )
    prediction_action = payload["final_action"]
    final_correct = prediction_action == record["oracle"]["optimal_action"]
    task_correct = schema_valid and final_correct
    full_trace_correct = (
        task_correct
        and controller_correct
        and operator_correct
        and selected_values_correct
        and action_values_correct
    )

    if not controller_correct:
        category = "controller_copy"
    elif inactive_operator_nodes:
        category = "inactive_operator"
    elif operator_correct and not selected_values_correct:
        category = "selected_value"
    elif selected_values_correct and not action_values_correct:
        category = "chance_arithmetic"
    elif action_values_correct and not final_correct:
        category = "root_comparison"
    elif not node_complete or not action_complete:
        category = "semantic_structure"
    elif task_correct:
        category = "correct"
    else:
        category = "unclassifiable"

    return {
        **base,
        "schema_valid": schema_valid,
        "controller_correct": controller_correct,
        "operator_correct": operator_correct,
        "selected_values_correct": selected_values_correct,
        "action_values_correct": action_values_correct,
        "final_correct": final_correct,
        "task_correct": task_correct,
        "full_trace_correct": full_trace_correct,
        "inactive_operator": bool(inactive_operator_nodes),
        "inactive_operator_nodes": int(inactive_operator_nodes),
        "error_category": category,
        "prediction": prediction_action,
    }


def bootstrap_interval(
    values: list[float], confidence: float, seed: int = 20260827, rounds: int = 20_000
) -> tuple[float, float]:
    if not values:
        return math.nan, math.nan
    rng = random.Random(seed)
    estimates = []
    for _ in range(rounds):
        estimates.append(sum(rng.choice(values) for _ in values) / len(values))
    estimates.sort()
    alpha = (1 - confidence) / 2
    low_index = max(0, int(alpha * rounds))
    high_index = min(rounds - 1, int((1 - alpha) * rounds) - 1)
    return estimates[low_index], estimates[high_index]


def pair_frame(items: pd.DataFrame) -> pd.DataFrame:
    rows = []
    group_keys = ["model_id", "pack", "condition", "template_mode", "structured", "pair_id"]
    for keys, group in items.groupby(group_keys):
        if len(group) != 2:
            continue
        row = dict(zip(group_keys, keys))
        row.update(
            {
                "pair_correct": bool(group.task_correct.all()),
                "pair_trace_correct": bool(group.full_trace_correct.all()),
                "pair_schema_valid": bool(group.schema_valid.all()),
                "pair_truncated": bool((group.stop_reason == "length").any()),
                "inactive_operator": bool(group.inactive_operator.any()),
                "inactive_operator_items": int(group.inactive_operator.sum()),
                "skin": group.skin.iloc[0],
                "difficulty": int(group.difficulty.iloc[0]),
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def summarize(items: pd.DataFrame, pairs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    keys = ["model_id", "pack", "condition", "template_mode", "structured"]
    for key_values, group in items.groupby(keys):
        filters = pd.Series(True, index=pairs.index)
        for key, value in zip(keys, key_values):
            filters &= pairs[key] == value
        pair_group = pairs.loc[filters]
        p95 = bootstrap_interval(pair_group.pair_correct.astype(float).tolist(), 0.95)
        rows.append(
            {
                **dict(zip(keys, key_values)),
                "items": len(group),
                "pairs": len(pair_group),
                "schema_valid_rate": float(group.schema_valid.mean()),
                "truncation_rate": float((group.stop_reason == "length").mean()),
                "item_accuracy": float(group.task_correct.mean()),
                "pair_accuracy": float(pair_group.pair_correct.mean()),
                "pair_ci95_low": p95[0],
                "pair_ci95_high": p95[1],
                "full_trace_accuracy": float(group.full_trace_correct.mean()),
                "inactive_operator_rate": float(group.inactive_operator.mean()),
            }
        )
    return pd.DataFrame(rows).sort_values(keys)


def paired_contrast(pairs: pd.DataFrame, model: str, pack: str, left: str, right: str) -> dict | None:
    subset = pairs[
        (pairs.model_id == model)
        & (pairs.pack == pack)
        & (pairs.template_mode == "native")
        & (pairs.structured)
    ]
    by_left = subset[subset.condition == left].set_index("pair_id")
    by_right = subset[subset.condition == right].set_index("pair_id")
    joined = by_left[["pair_correct"]].join(
        by_right[["pair_correct"]], how="inner", lsuffix="_left", rsuffix="_right"
    )
    if joined.empty:
        return None
    differences = (
        joined.pair_correct_left.astype(float) - joined.pair_correct_right.astype(float)
    ).tolist()
    ci90 = bootstrap_interval(differences, 0.90)
    ci95 = bootstrap_interval(differences, 0.95)
    left_only = int((joined.pair_correct_left & ~joined.pair_correct_right).sum())
    right_only = int((~joined.pair_correct_left & joined.pair_correct_right).sum())
    discordant = left_only + right_only
    pvalue = binomtest(min(left_only, right_only), discordant, 0.5).pvalue if discordant else 1.0
    return {
        "model_id": model,
        "pack": pack,
        "contrast": f"{left}-{right}",
        "pairs": len(joined),
        "left_accuracy": float(joined.pair_correct_left.mean()),
        "right_accuracy": float(joined.pair_correct_right.mean()),
        "difference": float(sum(differences) / len(differences)),
        "ci90_low": ci90[0],
        "ci90_high": ci90[1],
        "ci95_low": ci95[0],
        "ci95_high": ci95[1],
        "left_only_correct": left_only,
        "right_only_correct": right_only,
        "pvalue": pvalue,
    }


def interaction_contrast(pairs: pd.DataFrame, model: str) -> dict | None:
    subset = pairs[
        (pairs.model_id == model)
        & (pairs.pack == "A")
        & (pairs.template_mode == "native")
        & (pairs.structured)
        & (pairs.condition.isin(["A", "B", "C", "D"]))
    ]
    pivot = subset.pivot_table(index="pair_id", columns="condition", values="pair_correct", aggfunc="first")
    if not set("ABCD").issubset(pivot.columns):
        return None
    pivot = pivot.dropna(subset=list("ABCD"))
    values = ((pivot.D.astype(float) - pivot.C.astype(float)) - (pivot.B.astype(float) - pivot.A.astype(float))).tolist()
    ci90 = bootstrap_interval(values, 0.90)
    ci95 = bootstrap_interval(values, 0.95)
    try:
        pvalue = (
            float(wilcoxon(values, alternative="two-sided", zero_method="wilcox").pvalue)
            if any(value != 0 for value in values)
            else 1.0
        )
    except ValueError:
        pvalue = 1.0
    return {
        "model_id": model,
        "pack": "A",
        "contrast": "interaction",
        "pairs": len(values),
        "left_accuracy": math.nan,
        "right_accuracy": math.nan,
        "difference": float(sum(values) / len(values)),
        "ci90_low": ci90[0],
        "ci90_high": ci90[1],
        "ci95_low": ci95[0],
        "ci95_high": ci95[1],
        "left_only_correct": math.nan,
        "right_only_correct": math.nan,
        "pvalue": pvalue,
    }


def holm_adjust(rows: list[dict]) -> None:
    ordered = sorted(enumerate(rows), key=lambda item: item[1]["pvalue"])
    running = 0.0
    total = len(rows)
    for rank, (index, row) in enumerate(ordered):
        adjusted = min(1.0, (total - rank) * row["pvalue"])
        running = max(running, adjusted)
        rows[index]["pvalue_holm"] = running


def make_contrasts(pairs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model in sorted(pairs.model_id.unique()):
        primary = []
        dc = paired_contrast(pairs, model, "A", "D", "C")
        interaction = interaction_contrast(pairs, model)
        ec = paired_contrast(pairs, model, "A", "E", "C")
        for row in (dc, interaction, ec):
            if row:
                primary.append(row)
        if len(primary) == 3:
            holm_adjust(primary)
        else:
            for row in primary:
                row["pvalue_holm"] = math.nan
        rows.extend(primary)
        pack_b = paired_contrast(pairs, model, "B", "D", "C")
        if pack_b:
            pack_b["pvalue_holm"] = math.nan
            rows.append(pack_b)
    return pd.DataFrame(rows)


def process_metrics(items: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model in sorted(items.model_id.unique()):
        subset = items[
            (items.model_id == model)
            & (items.pack == "A")
            & (items.condition.isin(["C", "D"]))
            & (items.template_mode == "native")
            & (items.structured)
        ]
        pivot = subset.groupby("condition").agg(
            items=("id", "size"),
            inactive_operator_rate=("inactive_operator", "mean"),
            errors=("task_correct", lambda x: int((~x).sum())),
            inactive_operator_errors=(
                "inactive_operator",
                lambda x: int(x[~subset.loc[x.index, "task_correct"]].sum()),
            ),
        )
        if not {"C", "D"}.issubset(pivot.index):
            continue
        excess_errors = int(pivot.loc["D", "errors"] - pivot.loc["C", "errors"])
        excess_inactive_errors = int(
            pivot.loc["D", "inactive_operator_errors"] - pivot.loc["C", "inactive_operator_errors"]
        )
        rows.append(
            {
                "model_id": model,
                "C_inactive_operator_rate": float(pivot.loc["C", "inactive_operator_rate"]),
                "D_inactive_operator_rate": float(pivot.loc["D", "inactive_operator_rate"]),
                "inactive_operator_rate_change": float(
                    pivot.loc["D", "inactive_operator_rate"] - pivot.loc["C", "inactive_operator_rate"]
                ),
                "excess_D_errors": excess_errors,
                "excess_inactive_operator_errors": excess_inactive_errors,
                "excess_error_fraction": (
                    excess_inactive_errors / excess_errors if excess_errors > 0 else math.nan
                ),
            }
        )
    return pd.DataFrame(rows)


def preliminary_gate(summary: pd.DataFrame, contrasts: pd.DataFrame, manifest: dict) -> dict:
    roles = {entry["family"]: entry["role"] for entry in manifest["models"]}
    model_to_role = {}
    for entry in manifest["models"]:
        model_to_role[entry["family"]] = entry["role"]
    results = {}
    for model in sorted(summary.model_id.unique()):
        cell = summary[
            (summary.model_id == model)
            & (summary.pack == "A")
            & (summary.condition.isin(["C", "D"]))
            & (summary.template_mode == "native")
            & (summary.structured)
        ].set_index("condition")
        if not {"C", "D"}.issubset(cell.index):
            continue
        c_errors = int(cell.loc["C", "pairs"] * (1 - cell.loc["C", "pair_accuracy"]))
        basic = (
            cell.loc["C", "schema_valid_rate"] >= 0.99
            and cell.loc["D", "schema_valid_rate"] >= 0.99
            and cell.loc["C", "truncation_rate"] <= 0.005
            and cell.loc["D", "truncation_rate"] <= 0.005
            and abs(cell.loc["D", "truncation_rate"] - cell.loc["C", "truncation_rate"]) <= 0.01
            and cell.loc["C", "pair_accuracy"] >= 0.65
            and c_errors >= 3
        )
        results[model] = {
            "basic_admissibility": bool(basic),
            "diagnostics_pending": ["exact_replay", "template_stability"],
        }
    return {
        "status": "PRIMARY_RESULTS_ONLY_DIAGNOSTICS_PENDING",
        "models": results,
        "note": "No scientific GO can be issued until replay, template, wording, process intervention, and reverse injection are complete.",
    }


def write_report(summary: pd.DataFrame, contrasts: pd.DataFrame, process: pd.DataFrame, gate: dict, path: Path) -> None:
    lines = [
        "# Competing-Operator Interference Smoke Test",
        "",
        f"**Gate status:** `{gate['status']}`",
        "",
        gate["note"],
        "",
        "## Primary cells",
        "",
        summary.to_markdown(index=False, floatfmt=".3f"),
        "",
        "## Paired contrasts",
        "",
        contrasts.to_markdown(index=False, floatfmt=".3f") if not contrasts.empty else "No complete contrasts.",
        "",
        "## Operator-process diagnostics",
        "",
        process.to_markdown(index=False, floatfmt=".3f") if not process.empty else "No complete process comparison.",
        "",
        "## Interpretation",
        "",
        "These are smoke-gate results, not a paper claim. The binding thresholds are in `PREREGISTRATION.md`. Missing diagnostics cannot be treated as passed conditions.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--predictions", nargs="+", required=True)
    parser.add_argument("--model-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    truth = {record["id"]: record for record in read_jsonl(args.data)}
    predictions = []
    for path in resolve_paths(args.predictions):
        predictions.extend(read_jsonl(path))
    scored = []
    seen = set()
    for prediction in predictions:
        identity = (
            prediction.get("model_id"),
            prediction.get("pack"),
            prediction.get("condition"),
            prediction.get("template_mode"),
            prediction.get("structured"),
            prediction.get("id"),
        )
        if identity in seen:
            raise SystemExit(f"duplicate prediction identity: {identity}")
        seen.add(identity)
        record = truth.get(prediction.get("id"))
        if record:
            scored.append(parse_and_score(record, prediction))
    items = pd.DataFrame(scored)
    if items.empty:
        raise SystemExit("no matching predictions")
    pairs = pair_frame(items)
    summary = summarize(items, pairs)
    contrasts = make_contrasts(pairs)
    process = process_metrics(items)
    manifest = json.loads(args.model_manifest.read_text(encoding="utf-8"))
    gate = preliminary_gate(summary, contrasts, manifest)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    items.to_json(args.output_dir / "item_results.jsonl", orient="records", lines=True, force_ascii=False)
    pairs.to_csv(args.output_dir / "pair_results.csv", index=False)
    summary.to_csv(args.output_dir / "summary.csv", index=False)
    contrasts.to_csv(args.output_dir / "contrasts.csv", index=False)
    process.to_csv(args.output_dir / "process_metrics.csv", index=False)
    (args.output_dir / "gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_report(summary, contrasts, process, gate, args.output_dir / "REPORT.md")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
