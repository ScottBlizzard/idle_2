from __future__ import annotations

import argparse
import glob
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Sequence

import pandas as pd


FINAL_PATTERN = re.compile(r"FINAL\s*:\s*([A-Z][A-Z_-]*)", re.IGNORECASE)


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def parse_choice(text: str, actions: tuple[str, str]) -> tuple[str | None, str]:
    matches = FINAL_PATTERN.findall(text)
    normalized = {action.upper(): action for action in actions}
    for candidate in reversed(matches):
        if candidate.upper() in normalized:
            return normalized[candidate.upper()], "final"
    occurrences: list[tuple[int, str]] = []
    upper = text.upper()
    for action in actions:
        for match in re.finditer(rf"\b{re.escape(action.upper())}\b", upper):
            occurrences.append((match.start(), action))
    if occurrences:
        occurrences.sort()
        return occurrences[-1][1], "fallback_last_mention"
    return None, "unparsed"


def bootstrap_ci(values: list[float], seed: int = 20260826, rounds: int = 5000) -> tuple[float, float]:
    if not values:
        return float("nan"), float("nan")
    rng = random.Random(seed)
    samples = []
    for _ in range(rounds):
        draw = [rng.choice(values) for _ in values]
        samples.append(sum(draw) / len(draw))
    samples.sort()
    return samples[int(0.025 * rounds)], samples[int(0.975 * rounds)]


def evaluate_group(group: pd.DataFrame) -> tuple[dict, list[dict]]:
    pair_rows: list[dict] = []
    for pair_id, pair in group.groupby("pair_id"):
        indexed = {row.controller: row for row in pair.itertuples()}
        if set(indexed) != {"self", "opponent"}:
            continue
        self_row = indexed["self"]
        opp_row = indexed["opponent"]
        self_ok = bool(self_row.correct)
        opp_ok = bool(opp_row.correct)
        both_parsed = self_row.prediction is not None and opp_row.prediction is not None
        flipped = both_parsed and self_row.prediction != opp_row.prediction
        if not both_parsed:
            error_type = "unparsed"
        elif self_ok and opp_ok:
            error_type = "correct_flip"
        elif self_row.prediction == self_row.branching_action and opp_row.prediction == opp_row.branching_action:
            error_type = "branching_both"
        elif self_row.prediction == self_row.safe_action and opp_row.prediction == opp_row.safe_action:
            error_type = "safe_both"
        elif flipped:
            error_type = "reversed_flip"
        else:
            error_type = "other"
        pair_rows.append(
            {
                "pair_id": pair_id,
                "pair_correct": float(self_ok and opp_ok),
                "self_correct": float(self_ok),
                "opponent_correct": float(opp_ok),
                "flipped": float(flipped),
                "same_action": float(both_parsed and not flipped),
                "both_parsed": float(both_parsed),
                "error_type": error_type,
                "domain": self_row.domain,
                "difficulty": self_row.difficulty,
                "self_prediction": self_row.prediction,
                "opponent_prediction": opp_row.prediction,
                "safe_action": self_row.safe_action,
                "branching_action": self_row.branching_action,
            }
        )
    pair_df = pd.DataFrame(pair_rows)
    pair_values = pair_df["pair_correct"].tolist() if not pair_df.empty else []
    low, high = bootstrap_ci(pair_values)
    metrics = {
        "items": int(len(group)),
        "pairs": int(len(pair_df)),
        "parse_rate": float(group["parsed"].mean()),
        "final_parse_rate": float((group["parse_method"] == "final").mean()),
        "fallback_parse_rate": float((group["parse_method"] == "fallback_last_mention").mean()),
        "item_accuracy": float(group["correct"].mean()),
        "self_accuracy": float(group.loc[group.controller == "self", "correct"].mean()),
        "opponent_accuracy": float(group.loc[group.controller == "opponent", "correct"].mean()),
        "pair_accuracy": float(pair_df["pair_correct"].mean()),
        "pair_accuracy_ci_low": low,
        "pair_accuracy_ci_high": high,
        "flip_rate": float(pair_df["flipped"].mean()),
        "same_action_rate": float(pair_df["same_action"].mean()),
        "branching_choice_self": float(
            (group.loc[group.controller == "self", "prediction"] == group.loc[group.controller == "self", "branching_action"]).mean()
        ),
        "branching_choice_opponent": float(
            (group.loc[group.controller == "opponent", "prediction"] == group.loc[group.controller == "opponent", "branching_action"]).mean()
        ),
    }
    for key, value in Counter(pair_df["error_type"]).items():
        metrics[f"errors_{key}"] = int(value)
    return metrics, pair_rows


def make_breakdown(pair_errors: pd.DataFrame, column: str) -> pd.DataFrame:
    return (
        pair_errors.groupby(["model_id", "prompt_mode", column])
        .agg(
            pairs=("pair_correct", "size"),
            pair_accuracy=("pair_correct", "mean"),
            self_accuracy=("self_correct", "mean"),
            opponent_accuracy=("opponent_correct", "mean"),
            flip_rate=("flipped", "mean"),
            same_action_rate=("same_action", "mean"),
        )
        .reset_index()
        .sort_values(["model_id", "prompt_mode", column])
    )


def make_gap_table(summary: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model_id, group in summary.groupby("model_id"):
        indexed = group.set_index("prompt_mode")
        if "direct" not in indexed.index:
            continue
        direct = float(indexed.loc["direct", "pair_accuracy"])
        for mode in ("cot", "bellman", "local_operator", "positive_operator"):
            if mode not in indexed.index:
                continue
            score = float(indexed.loc[mode, "pair_accuracy"])
            denominator = 1.0 - direct
            rows.append(
                {
                    "model_id": model_id,
                    "prompt_mode": mode,
                    "direct_pair_accuracy": direct,
                    "scaffold_pair_accuracy": score,
                    "absolute_gain": score - direct,
                    "remaining_gap_closed": (score - direct) / denominator if denominator else 0.0,
                }
            )
    return pd.DataFrame(rows)


def make_prompt_comparisons(pair_errors: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model_id, group in pair_errors.groupby("model_id"):
        modes = sorted(group.prompt_mode.unique())
        by_mode = {
            mode: group.loc[group.prompt_mode == mode, ["pair_id", "pair_correct"]].set_index("pair_id")
            for mode in modes
        }
        for left_index, left_mode in enumerate(modes):
            for right_mode in modes[left_index + 1 :]:
                paired = by_mode[left_mode].join(
                    by_mode[right_mode],
                    how="inner",
                    lsuffix="_left",
                    rsuffix="_right",
                )
                differences = (
                    paired["pair_correct_left"] - paired["pair_correct_right"]
                ).tolist()
                low, high = bootstrap_ci(differences)
                rows.append(
                    {
                        "model_id": model_id,
                        "prompt_left": left_mode,
                        "prompt_right": right_mode,
                        "pairs": len(paired),
                        "accuracy_left": float(paired["pair_correct_left"].mean()),
                        "accuracy_right": float(paired["pair_correct_right"].mean()),
                        "paired_difference_left_minus_right": float(sum(differences) / len(differences)),
                        "difference_ci_low": low,
                        "difference_ci_high": high,
                        "left_only_correct": int((paired["pair_correct_left"] > paired["pair_correct_right"]).sum()),
                        "right_only_correct": int((paired["pair_correct_right"] > paired["pair_correct_left"]).sum()),
                        "same_outcome": int((paired["pair_correct_right"] == paired["pair_correct_left"]).sum()),
                    }
                )
    return pd.DataFrame(rows)


def write_report(
    summary: pd.DataFrame,
    pair_errors: pd.DataFrame,
    domain_breakdown: pd.DataFrame,
    difficulty_breakdown: pd.DataFrame,
    gap_table: pd.DataFrame,
    prompt_comparisons: pd.DataFrame,
    output: Path,
) -> None:
    lines = [
        "# Control-Flip Diagnostic Results",
        "",
        "## Main metrics",
        "",
        summary[
            [
                "model_id",
                "prompt_mode",
                "pairs",
                "item_accuracy",
                "pair_accuracy",
                "pair_accuracy_ci_low",
                "pair_accuracy_ci_high",
                "flip_rate",
                "same_action_rate",
                "parse_rate",
                "final_parse_rate",
            ]
        ].to_markdown(index=False, floatfmt=".3f"),
        "",
        "Pair accuracy is the primary metric: both members must be answered correctly. Random item choice yields 25% expected pair accuracy; always choosing the same root action yields 0% pair accuracy.",
        "",
        "## Pre-registered decision",
        "",
    ]
    cot = summary[summary.prompt_mode.str.startswith("cot")]
    bellman = summary[summary.prompt_mode.str.startswith("bellman")]
    bellman_closure = gap_table.loc[gap_table.prompt_mode == "bellman", "remaining_gap_closed"] if not gap_table.empty else pd.Series(dtype=float)
    if not cot.empty and float(cot.pair_accuracy.max()) >= 0.90:
        decision = "**NO-GO:** an ordinary compact chain-of-thought baseline reaches at least 90% pair accuracy."
    elif not bellman.empty and (float(bellman.pair_accuracy.max()) >= 0.90 or (not bellman_closure.empty and float(bellman_closure.max()) >= 0.80)):
        decision = "**NO-GO as a robust reasoning failure:** explicit Bellman scaffolding solves at least one strong baseline."
    else:
        direct = summary[summary.prompt_mode == "direct"]
        non_direct = summary[summary.prompt_mode != "direct"]
        best_direct = float(direct.pair_accuracy.max()) if not direct.empty else float("nan")
        best_scaffold = float(non_direct.pair_accuracy.max()) if not non_direct.empty else float("nan")
        if best_scaffold >= 0.90:
            decision = "**NO-GO as a robust reasoning failure:** scaffolding solves the diagnostic. Retain only as a prompting/evaluation observation."
        elif best_direct < 0.70 and best_scaffold < 0.85:
            decision = "**PROVISIONAL GO:** a controller-conditioned failure survives explicit reasoning; realistic-environment validation is required."
        else:
            decision = "**BORDERLINE:** the effect exists but is not yet strong enough for a paper claim."
    lines.extend([decision, "", "## Error taxonomy", ""])
    taxonomy = (
        pair_errors.groupby(["model_id", "prompt_mode", "error_type"])
        .size()
        .reset_index(name="pairs")
        .sort_values(["model_id", "prompt_mode", "pairs"], ascending=[True, True, False])
    )
    lines.append(taxonomy.to_markdown(index=False))
    lines.extend(["", "## Prompt gains", ""])
    lines.append(gap_table.to_markdown(index=False, floatfmt=".3f") if not gap_table.empty else "No paired prompt comparisons available.")
    lines.extend(["", "Paired prompt differences are available in `prompt_comparisons.csv`."])
    lines.extend(["", "## Difficulty breakdown", ""])
    lines.append(difficulty_breakdown.to_markdown(index=False, floatfmt=".3f"))
    lines.extend(["", "## Domain breakdown", ""])
    lines.append(domain_breakdown.to_markdown(index=False, floatfmt=".3f"))
    lines.extend(["", "## Interpretation guardrails", ""])
    lines.extend(
        [
            "- High item accuracy with low pair accuracy indicates controller-insensitive answers, not arithmetic inability alone.",
            "- A large `safe_both` count indicates global uncertainty aversion; `branching_both` indicates global option/variance seeking.",
            "- If Bellman scaffolding removes the effect, the result does not support a fundamental planning limitation.",
            "- Synthetic success is only a diagnostic. It cannot by itself support an ICLR main-track claim.",
        ]
    )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--predictions", nargs="+", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    truth = {record["id"]: record for record in read_jsonl(args.data)}
    paths: list[Path] = []
    for pattern in args.predictions:
        matched = glob.glob(pattern)
        paths.extend(Path(path) for path in (matched or [pattern]))
    predictions = []
    for path in paths:
        predictions.extend(read_jsonl(path))
    rows = []
    for prediction in predictions:
        record = truth.get(prediction["id"])
        if record is None:
            continue
        choice, parse_method = parse_choice(
            prediction.get("text", ""),
            (record["safe_action"], record["branching_action"]),
        )
        rows.append(
            {
                **record,
                "model_id": prediction["model_id"],
                "prompt_mode": prediction["prompt_mode"],
                "prediction": choice,
                "parse_method": parse_method,
                "parsed": choice is not None,
                "correct": choice == record["optimal_action"],
                "raw_text": prediction.get("text", ""),
            }
        )
    frame = pd.DataFrame(rows)
    if frame.empty:
        raise SystemExit("no matching predictions")
    summary_rows = []
    all_pair_rows = []
    for (model_id, prompt_mode), group in frame.groupby(["model_id", "prompt_mode"]):
        metrics, pair_rows = evaluate_group(group)
        summary_rows.append({"model_id": model_id, "prompt_mode": prompt_mode, **metrics})
        all_pair_rows.extend(
            {"model_id": model_id, "prompt_mode": prompt_mode, **row} for row in pair_rows
        )
    summary = pd.DataFrame(summary_rows).sort_values(["model_id", "prompt_mode"])
    pair_errors = pd.DataFrame(all_pair_rows)
    domain_breakdown = make_breakdown(pair_errors, "domain")
    difficulty_breakdown = make_breakdown(pair_errors, "difficulty")
    gap_table = make_gap_table(summary)
    prompt_comparisons = make_prompt_comparisons(pair_errors)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output_dir / "summary.csv", index=False)
    pair_errors.to_csv(args.output_dir / "pair_results.csv", index=False)
    domain_breakdown.to_csv(args.output_dir / "domain_breakdown.csv", index=False)
    difficulty_breakdown.to_csv(args.output_dir / "difficulty_breakdown.csv", index=False)
    gap_table.to_csv(args.output_dir / "prompt_gains.csv", index=False)
    prompt_comparisons.to_csv(args.output_dir / "prompt_comparisons.csv", index=False)
    frame.to_json(args.output_dir / "item_results.jsonl", orient="records", lines=True, force_ascii=False)
    write_report(
        summary,
        pair_errors,
        domain_breakdown,
        difficulty_breakdown,
        gap_table,
        prompt_comparisons,
        args.output_dir / "REPORT.md",
    )
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
