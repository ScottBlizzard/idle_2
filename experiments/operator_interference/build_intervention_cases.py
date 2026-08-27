from __future__ import annotations

import argparse
import glob
import json
from fractions import Fraction
from pathlib import Path

from evaluate import parse_and_score, read_jsonl


def resolve(patterns: list[str]) -> list[Path]:
    result = []
    for pattern in patterns:
        result.extend(Path(path) for path in (glob.glob(pattern) or [pattern]))
    return sorted(set(result))


def node_candidates(record: dict, node: str) -> list[Fraction]:
    action = "ACTION_P" if node.startswith("NODE_P") else "ACTION_Q"
    outcome_index = int(node[-1]) - 1
    return [Fraction(value) for value in record["actions"][action]["outcomes"][outcome_index]["values"]]


def selected_for_semantic(values: list[Fraction], semantic: str) -> Fraction:
    return max(values) if semantic == "larger" else min(values)


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def stage2_prompt(record: dict, table: list[dict]) -> str:
    lines = [
        "Use the binding selected-value table below to finish the root decision.",
        "The table is an input state: do not replace, reselect, or reinterpret any selected value.",
        "Probability-weight the binding selected values for each root action, then choose the larger expected value.",
    ]
    for action in record["action_order"]:
        lines.append(f"{action}:")
        for index, outcome in enumerate(record["actions"][action]["outcomes"], start=1):
            lines.append(f"- NODE_{action[-1]}{index} probability {outcome['probability']}.")
    lines.append("Binding table: " + json.dumps(table, separators=(",", ":")))
    lines.append(
        "Return compact JSON with keys actions and final_action. actions must follow displayed action order and contain action and expected_value strings."
    )
    return "\n".join(lines)


def stage2_regex(record: dict) -> str:
    number = "(-?[0-9]{1,6}|-?[0-9]{1,6}/[1-9][0-9]{0,5})"
    action_parts = [
        r'\{"action":"' + action + r'","expected_value":"' + number + r'"\}'
        for action in record["action_order"]
    ]
    return (
        r'\{"actions":\['
        + ",".join(action_parts)
        + r'\],"final_action":"(ACTION_P|ACTION_Q)"\}'
    )


def add_twins(cases: list[dict], record: dict, model_id: str, source_id: str, kind: str, left: list[dict], right: list[dict]) -> None:
    pair_id = f"{model_id}.{source_id}.{kind}"
    for variant, table in (("original", left), ("modified", right)):
        cases.append(
            {
                "case_id": f"{pair_id}.{variant}",
                "intervention_pair_id": pair_id,
                "source_id": source_id,
                "model_id": model_id,
                "kind": kind,
                "variant": variant,
                "optimal_action": record["oracle"]["optimal_action"],
                "prompt": stage2_prompt(record, table),
                "regex": stage2_regex(record),
                "table": table,
            }
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--predictions", nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    truth = {record["id"]: record for record in read_jsonl(args.data)}
    by_model: dict[str, list[tuple[dict, dict, dict]]] = {}
    for path in resolve(args.predictions):
        for prediction in read_jsonl(path):
            if prediction.get("pack") != "A" or prediction.get("condition") != "D":
                continue
            record = truth.get(prediction.get("id"))
            if not record:
                continue
            try:
                payload = json.loads(prediction["text"])
            except json.JSONDecodeError:
                continue
            score = parse_and_score(record, prediction)
            if not score["schema_valid"]:
                continue
            by_model.setdefault(prediction["model_id"], []).append((record, payload, score))

    cases = []
    for model_id, rows in by_model.items():
        wrong = sorted((row for row in rows if row[2]["inactive_operator"]), key=lambda row: row[0]["id"])
        clean = sorted(
            (row for row in rows if row[2]["operator_correct"] and row[2]["task_correct"]),
            key=lambda row: row[0]["id"],
        )[: len(wrong)]
        for record, payload, _score in wrong:
            original = payload["nodes"]
            corrected = []
            for item in original:
                expected = record["oracle"]["nodes"][item["node"]]
                corrected.append(
                    {
                        "node": item["node"],
                        "operator": expected["operator"],
                        "selected_value": expected["selected_value"],
                    }
                )
            add_twins(cases, record, model_id, record["id"], "correction", original, corrected)

        for record, payload, _score in clean:
            original = payload["nodes"]
            injected = [dict(item) for item in original]
            target = injected[0]
            inactive_operator = "OP_Y" if record["oracle"]["operator"] == "OP_X" else "OP_X"
            inactive_semantic = record["operator_semantics"][inactive_operator]
            target["operator"] = inactive_operator
            target["selected_value"] = frac_text(
                selected_for_semantic(node_candidates(record, target["node"]), inactive_semantic)
            )
            add_twins(cases, record, model_id, record["id"], "injection", original, injected)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for case in cases:
            handle.write(json.dumps(case, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps({"cases": len(cases), "models": len(by_model), "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
