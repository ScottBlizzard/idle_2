#!/usr/bin/env python3
"""Minimal selection-induced inverse-scaling construction.

The corrector becomes strictly better with capability at every fixed task
difficulty.  Nevertheless, correction rate measured on each model's own
failure cohort decreases because stronger models fail on a harder selected
set.  No model inference or fitted parameter is used.
"""

from __future__ import annotations

import math


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def main() -> None:
    difficulties = [(-4.0 + 8.0 * index / 20_000) for index in range(20_001)]
    weights = [math.exp(-(difficulty**2) / 2.0) for difficulty in difficulties]
    normalizer = sum(weights)
    weights = [weight / normalizer for weight in weights]

    print("ability\tinitial_accuracy\town_failure_correction\tstandard_bank_correction")
    own_rates: list[float] = []
    standard_rates: list[float] = []

    for ability in (-1.0, 0.0, 1.0, 2.0):
        failure_probabilities = [
            sigmoid(2.0 * (difficulty - ability)) for difficulty in difficulties
        ]
        correction_probabilities = [
            sigmoid(-0.5 + 0.5 * ability - 2.5 * difficulty)
            for difficulty in difficulties
        ]

        failure_mass = sum(
            weight * failure
            for weight, failure in zip(weights, failure_probabilities, strict=True)
        )
        initial_accuracy = 1.0 - failure_mass
        own_rate = (
            sum(
                weight * failure * correction
                for weight, failure, correction in zip(
                    weights,
                    failure_probabilities,
                    correction_probabilities,
                    strict=True,
                )
            )
            / failure_mass
        )
        standard_rate = sum(
            weight * correction
            for weight, correction in zip(weights, correction_probabilities, strict=True)
        )

        own_rates.append(own_rate)
        standard_rates.append(standard_rate)
        print(
            f"{ability:.1f}\t{initial_accuracy:.6f}\t{own_rate:.6f}\t{standard_rate:.6f}"
        )

    assert all(left > right for left, right in zip(own_rates, own_rates[1:]))
    assert all(
        left < right for left, right in zip(standard_rates, standard_rates[1:])
    )


if __name__ == "__main__":
    main()
