"""Deterministic scaling check for the transient-shortcut catalyst ODE.

This script is exploratory theory support, not a registered experiment.
"""

from __future__ import annotations

import math

import numpy as np


def integrate(
    epsilon: float,
    withdrawal_time: float,
    total_time: float,
    dt: float = 1e-3,
) -> tuple[float, float, float, float]:
    """Euler-integrate the shortcut then core-only gradient flow."""
    a = epsilon
    u = epsilon
    v = epsilon
    for step in range(int(total_time / dt)):
        if step * dt < withdrawal_time:
            residual = 1.0 - a * (u * u + v)
            da = residual * (u * u + v)
            du = 2.0 * residual * a * u
            dv = residual * a
        else:
            residual = 1.0 - a * u * u
            da = residual * u * u
            du = 2.0 * residual * a * u
            dv = 0.0
        a += dt * da
        u += dt * du
        v += dt * dv
    core_loss = 0.5 * (1.0 - a * u * u) ** 2
    return core_loss, a, u, v


def main() -> None:
    for epsilon in (0.1, 0.05, 0.02, 0.01, 0.005):
        predicted_time = math.log(1.0 / epsilon)
        total_time = 2.2 * predicted_time
        grid = np.linspace(0.0, total_time, 161)
        results = [
            (float(tau), *integrate(epsilon, float(tau), total_time))
            for tau in grid
        ]
        best = min(results, key=lambda row: row[1])
        clean = results[0]
        permanent = results[-1]
        predicted = integrate(epsilon, predicted_time, total_time)
        print(
            f"epsilon={epsilon:.3g} log_inv_epsilon={predicted_time:.6f} "
            f"total_time={total_time:.6f} clean_loss={clean[1]:.8f} "
            f"permanent_loss={permanent[1]:.8f} "
            f"predicted_withdrawal_loss={predicted[0]:.8f} "
            f"best_time={best[0]:.6f} "
            f"best_over_log={best[0] / predicted_time:.6f} "
            f"best_loss={best[1]:.8f}"
        )


if __name__ == "__main__":
    main()
