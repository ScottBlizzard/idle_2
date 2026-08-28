from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from stage_d_predictors import (  # noqa: E402
    FEATURE_DIMENSION,
    joint_feature,
    model_factories,
    problem_spearman,
    trainable_parameter_count,
)


class PredictorTests(unittest.TestCase):
    def test_parameter_matching(self) -> None:
        factories, expected = model_factories()
        self.assertGreater(expected, 0)
        for factory in factories.values():
            self.assertEqual(trainable_parameter_count(factory()), expected)

    def test_joint_feature_schema(self) -> None:
        summary_i = {
            "sum": 1.0,
            "mean": 0.1,
            "minimum": -0.2,
            "maximum": 0.4,
            "rank_mean": 3.0,
            "rank_maximum": 7.0,
        }
        record = {
            "problem_id": "p",
            "layer_i": 3,
            "layer_j": 8,
            "normalized_layer_separation": 5 / 15,
            "hidden_projection": [0.0] * 32,
            "route_i": list(range(8)),
            "route_j": list(range(8, 16)),
            "standard_route_i": list(range(16, 24)),
            "standard_route_j": list(range(24, 32)),
            "router_summary_i": summary_i,
            "router_summary_j": dict(summary_i),
            "standard_overlap_i": 0.0,
            "standard_overlap_j": 0.0,
            "pair_overlap": 0.0,
            "route_i_index": 0,
            "route_j_index": 0,
        }
        predictions = {("p", "i", 0): 0.2, ("p", "j", 0): -0.1}
        feature = joint_feature(record, predictions)
        self.assertEqual(feature.shape, (FEATURE_DIMENSION,))
        self.assertTrue(np.all(np.isfinite(feature)))

    def test_problem_spearman(self) -> None:
        correlations = problem_spearman(
            ["a", "a", "a", "b", "b", "b"],
            np.asarray([1, 2, 3, 1, 2, 3], dtype=float),
            np.asarray([1, 2, 3, 3, 2, 1], dtype=float),
        )
        self.assertAlmostEqual(correlations["a"], 1.0)
        self.assertAlmostEqual(correlations["b"], -1.0)


if __name__ == "__main__":
    unittest.main()
