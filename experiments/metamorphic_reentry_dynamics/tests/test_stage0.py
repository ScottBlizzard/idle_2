import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analyze_stage0 import find_discovery_patterns, sign
from build_items import build, validate


class Stage0Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT / "FROZEN_CONFIG.json").read_text(encoding="utf-8"))

    def test_items_are_deterministic_and_valid(self):
        first = build(self.config)
        second = build(self.config)
        self.assertEqual(first, second)
        validate(first, self.config)
        self.assertEqual(len(first), 288)

    def test_sign_requires_accuracy_and_magnitude(self):
        good = {"mean_delta": 0.2, "accuracy_original": 0.7, "accuracy_transformed": 0.7}
        weak = {"mean_delta": 0.2, "accuracy_original": 0.59, "accuracy_transformed": 0.9}
        self.assertEqual(sign(good, self.config), 1)
        self.assertEqual(sign(weak, self.config), 0)

    def test_detects_only_reentrant_consensus(self):
        summary = {}
        for family in self.config["families"]:
            for seed in self.config["discovery_seeds"]:
                for checkpoint in self.config["checkpoints"]:
                    summary[(seed, checkpoint, family)] = {
                        "mean_delta": 0.0,
                        "accuracy_original": 0.8,
                        "accuracy_transformed": 0.8,
                    }
        family = self.config["families"][0]
        for checkpoint, delta in zip(self.config["checkpoints"][:3], [0.2, -0.2, 0.2]):
            for seed in self.config["discovery_seeds"][:4]:
                summary[(seed, checkpoint, family)]["mean_delta"] = delta
        candidates = find_discovery_patterns(summary, self.config)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["signs"], [1, -1, 1])


if __name__ == "__main__":
    unittest.main()
