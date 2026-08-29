"""Deterministic numerical check of the matched-RT cubic rate-shaping law.

This is a theorem sanity check, not a scientific experiment.  The clean model
is f(a, u)=a*u with target zero.  The two auxiliary vector fields have exactly
the same first-order Relative Transfer as clean flow, while changing the clean
NTK in opposite directions.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def clean_gradient(state: np.ndarray) -> np.ndarray:
    a, u = state
    residual = a * u
    return np.array([residual * u, residual * a])


def null_direction(state: np.ndarray) -> np.ndarray:
    a, u = state
    return np.array([a, -u])


def loss(state: np.ndarray) -> float:
    a, u = state
    return 0.5 * (a * u) ** 2


def flow(state: np.ndarray, vector_field, duration: float) -> np.ndarray:
    solution = solve_ivp(
        lambda _, value: vector_field(value),
        (0.0, duration),
        state,
        rtol=1e-12,
        atol=1e-14,
    )
    return solution.y[:, -1]


def main() -> None:
    initial = np.array([2.0, 0.5])
    coefficient = 2.0 * (initial[0] * initial[1]) ** 2 * (
        initial[0] ** 2 - initial[1] ** 2
    )
    print(f"predicted_cubic_coefficient={coefficient:.8f}")

    for continuation in (0.08, 0.04, 0.02, 0.01, 0.005):
        exposure = continuation**2
        clean_endpoint = flow(
            initial,
            lambda value: -clean_gradient(value),
            continuation + exposure,
        )
        rows = []
        for sign in (1.0, -1.0):
            switch_state = flow(
                initial,
                lambda value: -clean_gradient(value) + sign * null_direction(value),
                exposure,
            )
            endpoint = flow(
                switch_state,
                lambda value: -clean_gradient(value),
                continuation,
            )
            gap = loss(endpoint) - loss(clean_endpoint)
            rows.append((sign, gap, gap / continuation**3))
        print(
            f"s={continuation:.5f} eta={exposure:.8f} "
            f"positive_gap={rows[0][1]:+.10e} "
            f"positive_scaled={rows[0][2]:+.8f} "
            f"harmful_gap={rows[1][1]:+.10e} "
            f"harmful_scaled={rows[1][2]:+.8f}"
        )


if __name__ == "__main__":
    main()
