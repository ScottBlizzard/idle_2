from __future__ import annotations

import math
import importlib.util
import sys
import unittest
from pathlib import Path

import numpy as np


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from stage_d_common import (  # noqa: E402
    OLMOE_LAYER_PAIRS,
    benjamini_hochberg,
    build_alternatives,
    centered_bootstrap_p_value,
    extract_gsm8k_prediction,
    extract_math_prediction,
    generation_seed,
    h3_for_problem,
    matched_null_for_problem,
    percentile_interval,
    resolve_layer_pairs,
    select_fragile_token,
    stable_sort_rows,
    token_surface_is_eligible,
    verify_gsm8k,
    verify_math500,
)


def synthetic_grid() -> list[dict[str, float | int]]:
    rows = []
    for i in range(6):
        for j in range(6):
            single_i = 0.1 * (i - 2)
            single_j = 0.1 * (j - 2)
            interaction = 0.05 * math.sin(i * 7 + j * 11)
            rows.append(
                {
                    "route_i_index": i,
                    "route_j_index": j,
                    "single_effect_i": single_i,
                    "single_effect_j": single_j,
                    "joint_effect": single_i + single_j + interaction,
                    "router_score_sum_i": float(i),
                    "router_score_sum_j": float(j),
                    "standard_overlap_i": i / 10,
                    "standard_overlap_j": j / 10,
                    "pair_overlap": abs(i - j) / 10,
                    "single_residual_norm_i": 1 + i / 10,
                    "single_residual_norm_j": 1 + j / 10,
                    "normalized_layer_separation": 0.5,
                }
            )
    return rows


class IdentifierAndSeedTests(unittest.TestCase):
    def test_stable_sort_and_fold(self) -> None:
        rows = stable_sort_rows("gsm8k", [{"question": "b"}, {"question": "a"}])
        self.assertEqual([row["_stable_ordinal"] for row in rows], [0, 1])
        self.assertEqual([row["_fold"] for row in rows], [0, 1])

    def test_duplicate_is_protocol_error(self) -> None:
        with self.assertRaises(RuntimeError):
            stable_sort_rows("gsm8k", [{"question": "same"}, {"question": "same"}])

    def test_seed_mapping(self) -> None:
        self.assertEqual(generation_seed(0, 0, 0), 20260828)
        self.assertNotEqual(generation_seed(0, 1, 0), generation_seed(1, 0, 0))

    def test_layer_mapping(self) -> None:
        self.assertEqual(resolve_layer_pairs(16), OLMOE_LAYER_PAIRS)


class AnswerAndTokenTests(unittest.TestCase):
    def test_gsm_extract_priority(self) -> None:
        extracted = extract_gsm8k_prediction("work 7. Final answer: 8. #### 9")
        self.assertIsNotNone(extracted)
        self.assertEqual(extracted.value, "9")
        self.assertEqual(extracted.method, "hash_marker")

    def test_gsm_exact_decimal(self) -> None:
        correct, extracted = verify_gsm8k("Final answer: 1,250.00", "steps #### 1250")
        self.assertTrue(correct)
        self.assertIsNotNone(extracted)
        wrong, _ = verify_gsm8k("Final answer: 1250.01", "steps #### 1250")
        self.assertFalse(wrong)

    def test_nested_box(self) -> None:
        extracted = extract_math_prediction(r"Therefore \\boxed{\\frac{2}{3}}.")
        self.assertIsNotNone(extracted)
        self.assertEqual(extracted.value, r"\\frac{2}{3}")

    @unittest.skipUnless(importlib.util.find_spec("math_verify"), "math_verify not installed")
    def test_math_equivalence(self) -> None:
        correct, _ = verify_math500(
            r"Final answer: \\boxed{0.5}", {"answer": r"\\frac{1}{2}"}
        )
        self.assertTrue(correct)
        wrong, _ = verify_math500(r"Final answer: \\boxed{3}", {"answer": "4"})
        self.assertFalse(wrong)

    def test_token_filter(self) -> None:
        self.assertFalse(token_surface_is_eligible("   "))
        self.assertFalse(token_surface_is_eligible("..."))
        self.assertTrue(token_surface_is_eligible(" x"))
        selected = select_fragile_token(
            probabilities=[0.2, 0.1, 0.05],
            surfaces=["alpha", "beta", "####"],
            token_ends=[5, 10, 15],
            final_answer_start=11,
        )
        self.assertEqual(selected, 1)


class RouteAndStatisticsTests(unittest.TestCase):
    def test_gumbel_routes_are_deterministic(self) -> None:
        logits = np.linspace(-1, 1, 64)
        first = build_alternatives(logits, tuple(range(56, 64)), 0, 7, 3)
        second = build_alternatives(logits, tuple(range(56, 64)), 0, 7, 3)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 6)
        self.assertTrue(all(len(route) == 8 for route in first))

    def test_matched_donors_exclude_observed_pair(self) -> None:
        records = synthetic_grid()
        result = matched_null_for_problem(records)
        self.assertEqual(len(result["rows"]), 36)
        for row in result["rows"]:
            for donor_index in row["donors"]:
                donor = records[donor_index]
                self.assertNotEqual(
                    (row["route_i_index"], row["route_j_index"]),
                    (donor["route_i_index"], donor["route_j_index"]),
                )

    def test_h3_equal_candidate_sets(self) -> None:
        records = synthetic_grid()
        result = h3_for_problem(records)
        self.assertEqual(len(result["independent_pair"]), 2)
        self.assertEqual(len(result["direct_pair"]), 2)
        self.assertGreaterEqual(result["margin_gap"], -1e-12)

    def test_interval_and_centered_p(self) -> None:
        samples = np.linspace(0.0, 1.0, 10_000)
        low, high = percentile_interval(samples)
        self.assertAlmostEqual(low, 0.025, places=3)
        self.assertAlmostEqual(high, 0.975, places=3)
        p_value = centered_bootstrap_p_value(0.6, samples, 0.5)
        self.assertGreater(p_value, 0)
        self.assertLessEqual(p_value, 1)

    def test_benjamini_hochberg(self) -> None:
        adjusted = benjamini_hochberg([0.01, 0.04, 0.20, 0.03])
        expected = [0.04, 0.05333333333333334, 0.20, 0.05333333333333334]
        np.testing.assert_allclose(adjusted, expected)


if __name__ == "__main__":
    unittest.main()
