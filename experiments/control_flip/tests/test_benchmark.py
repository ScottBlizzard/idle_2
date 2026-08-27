from __future__ import annotations

import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from generate_benchmark import make_records  # noqa: E402


class BenchmarkInvariantTests(unittest.TestCase):
    def test_pairs_differ_only_in_controller_fields_and_prompt(self) -> None:
        records = make_records(24, 123)
        by_pair: dict[str, list[dict]] = {}
        for record in records:
            by_pair.setdefault(record["pair_id"], []).append(record)
        self.assertEqual(len(by_pair), 24)
        ignored = {
            "id",
            "controller",
            "branching_value",
            "optimal_action",
            "margin",
            "prompt",
        }
        for pair in by_pair.values():
            self.assertEqual({item["controller"] for item in pair}, {"self", "opponent"})
            left, right = pair
            for key in left:
                if key not in ignored:
                    self.assertEqual(left[key], right[key], key)

    def test_exact_optimum_flips_for_every_pair(self) -> None:
        records = make_records(90, 456)
        for record in records:
            if record["controller"] == "self":
                self.assertEqual(record["optimal_action"], record["branching_action"])
                self.assertGreater(record["branching_value"], record["safe_value"])
            else:
                self.assertEqual(record["optimal_action"], record["safe_action"])
                self.assertLess(record["branching_value"], record["safe_value"])
            self.assertGreaterEqual(record["margin"], 1.0)

    def test_balanced_domains_and_difficulties(self) -> None:
        records = make_records(180, 789)
        domains = {record["domain"] for record in records}
        difficulties = {record["difficulty"] for record in records}
        self.assertEqual(len(domains), 6)
        self.assertEqual(difficulties, {1, 2, 3})
        cells = Counter((record["domain"], record["difficulty"]) for record in records)
        self.assertEqual(len(cells), 18)
        self.assertEqual(set(cells.values()), {20})


if __name__ == "__main__":
    unittest.main()
