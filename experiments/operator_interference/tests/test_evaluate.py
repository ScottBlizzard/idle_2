from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluate import make_contrasts, pair_frame, parse_and_score, process_metrics, summarize, write_report  # noqa: E402
from generate_benchmark import make_records  # noqa: E402


def oracle_payload(record: dict) -> dict:
    nodes = []
    for action in record["action_order"]:
        for index, _ in enumerate(record["actions"][action]["outcomes"], start=1):
            node = f"NODE_{action[-1]}{index}"
            nodes.append({"node": node, **record["oracle"]["nodes"][node]})
    actions = [
        {"action": action, "expected_value": record["oracle"]["root_values"][action]}
        for action in record["action_order"]
    ]
    return {
        "controller": record["active_controller"],
        "nodes": nodes,
        "actions": actions,
        "final_action": record["oracle"]["optimal_action"],
    }


class EvaluateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = make_records(6, 11, "engineering")[0]
        self.base_prediction = {
            "model_id": "toy",
            "pack": "A",
            "condition": "C",
            "template_mode": "native",
            "structured": True,
            "stop_reason": "eos",
        }

    def test_oracle_payload_is_fully_correct(self) -> None:
        prediction = {**self.base_prediction, "text": json.dumps(oracle_payload(self.record))}
        scored = parse_and_score(self.record, prediction)
        self.assertTrue(scored["task_correct"])
        self.assertTrue(scored["full_trace_correct"])
        self.assertEqual(scored["error_category"], "correct")

    def test_wrong_operator_is_localized(self) -> None:
        payload = oracle_payload(self.record)
        payload["nodes"][0]["operator"] = (
            "OP_Y" if payload["nodes"][0]["operator"] == "OP_X" else "OP_X"
        )
        prediction = {**self.base_prediction, "text": json.dumps(payload)}
        scored = parse_and_score(self.record, prediction)
        self.assertTrue(scored["inactive_operator"])
        self.assertEqual(scored["error_category"], "inactive_operator")

    def test_invalid_json_counts_wrong(self) -> None:
        prediction = {**self.base_prediction, "text": "not json"}
        scored = parse_and_score(self.record, prediction)
        self.assertFalse(scored["schema_valid"])
        self.assertFalse(scored["task_correct"])

    def test_perfect_matrix_reaches_pair_pipeline(self) -> None:
        records = make_records(6, 23, "engineering")
        rows = []
        for pack, conditions in {"A": "ABCDE", "B": "CD"}.items():
            for condition in conditions:
                for record in records:
                    prediction = {
                        "model_id": "toy",
                        "pack": pack,
                        "condition": condition,
                        "template_mode": "native",
                        "structured": True,
                        "stop_reason": "eos",
                        "text": json.dumps(oracle_payload(record)),
                    }
                    rows.append(parse_and_score(record, prediction))
        items = pd.DataFrame(rows)
        pairs = pair_frame(items)
        summary = summarize(items, pairs)
        contrasts = make_contrasts(pairs)
        process = process_metrics(items)
        self.assertEqual(len(summary), 7)
        self.assertEqual(len(contrasts), 4)
        self.assertEqual(len(process), 1)
        self.assertTrue((summary["pair_accuracy"] == 1).all())

    def test_report_writer_has_no_optional_dependency_requirement(self) -> None:
        frame = pd.DataFrame([{"model_id": "toy", "pair_accuracy": 1.0}])
        gate = {"status": "TEST", "note": "test report"}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "REPORT.md"
            write_report(frame, frame, frame, gate, output)
            text = output.read_text(encoding="utf-8")
        self.assertIn("# Competing-Operator Interference Smoke Test", text)
        self.assertIn("toy", text)
        self.assertNotIn("\n\n\ntoy", text)


if __name__ == "__main__":
    unittest.main()
