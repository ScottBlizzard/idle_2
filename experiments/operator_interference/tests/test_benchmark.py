from __future__ import annotations

import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from generate_benchmark import make_records, metadata_probe_accuracy, validate_records  # noqa: E402
from prompts import ALL_PACKS, output_regex, output_schema, rule_card, unpadded_user_prompt  # noqa: E402


class BenchmarkTests(unittest.TestCase):
    def test_confirmatory_design_and_flip(self) -> None:
        records = make_records(54, 20260827, "confirmatory")
        audit = validate_records(records)
        self.assertEqual(audit["pairs"], 54)
        self.assertLessEqual(audit["metadata_probe_accuracy"], 0.55)
        cells = Counter((record["skin"], record["difficulty"]) for record in records)
        self.assertEqual(len(cells), 18)
        self.assertEqual(set(cells.values()), {6})

        by_pair: dict[str, list[dict]] = {}
        for record in records:
            by_pair.setdefault(record["pair_id"], []).append(record)
            self.assertGreaterEqual(Fraction(record["oracle"]["margin"]), 1)
        for pair in by_pair.values():
            self.assertNotEqual(pair[0]["oracle"]["optimal_action"], pair[1]["oracle"]["optimal_action"])

    def test_metadata_probe_is_near_chance(self) -> None:
        records = make_records(54, 99173, "confirmatory")
        self.assertLessEqual(metadata_probe_accuracy(records), 0.55)

    def test_prompt_matrix_and_schema(self) -> None:
        records = make_records(6, 17, "engineering")[:2]
        for record in records:
            for pack, conditions in ALL_PACKS.items():
                for condition in conditions:
                    text = unpadded_user_prompt(record, condition, pack)
                    self.assertIn("Output contract", text)
                    self.assertNotIn("Bellman", text)
                    if condition != "E":
                        self.assertNotIn("never apply", text)
                    self.assertTrue(rule_card(record, condition, pack))
            schema = output_schema(record)
            self.assertEqual(schema["properties"]["nodes"]["minItems"], 4)
            regex = output_regex(record)
            self.assertIn('"final_action"', regex)

            active = record["active_controller"]
            active_assignment_a = next(
                line for line in rule_card(record, "A", "A").splitlines() if line.startswith(active + " is assigned")
            )
            self.assertIn(active_assignment_a, rule_card(record, "B", "A").splitlines())
            active_assignment_c = next(
                line.split(": ", 1)[1]
                for line in rule_card(record, "C", "A").splitlines()
                if active + " is assigned" in line
            )
            self.assertTrue(any(active_assignment_c in line for line in rule_card(record, "D", "A").splitlines()))


if __name__ == "__main__":
    unittest.main()
