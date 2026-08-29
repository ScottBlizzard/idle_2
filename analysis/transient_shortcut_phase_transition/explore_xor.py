"""Outcome-exploratory CPU check for the theory-first transient-shortcut HOLD.

This is not a preregistered experiment and cannot authorize a paper seed.  It
tests only whether a beneficial temporary-shortcut regime exists in one minimal
nonlinear XOR learner under full-batch, distribution-exact gradient descent.
"""

from __future__ import annotations

import argparse
import itertools

import torch
from torch import nn


torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)


def distribution(shortcut_correlation: float) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    rows: list[list[float]] = []
    labels: list[float] = []
    weights: list[float] = []
    for x1, x2 in itertools.product((-1.0, 1.0), repeat=2):
        y = 1.0 if x1 * x2 > 0 else 0.0
        signed_y = 1.0 if y > 0 else -1.0
        for shortcut, probability in (
            (signed_y, shortcut_correlation),
            (-signed_y, 1.0 - shortcut_correlation),
        ):
            rows.append([x1, x2, shortcut])
            labels.append(y)
            weights.append(0.25 * probability)
    return (
        torch.tensor(rows, dtype=torch.float64),
        torch.tensor(labels, dtype=torch.float64),
        torch.tensor(weights, dtype=torch.float64),
    )


class BatchedTinyXOR(nn.Module):
    """Independent tiny MLPs evaluated in one vectorized computation."""

    def __init__(self, seeds: tuple[int, ...], width: int = 8) -> None:
        super().__init__()
        first_weights = []
        first_biases = []
        second_weights = []
        second_biases = []
        for seed in seeds:
            torch.manual_seed(seed)
            first = nn.Linear(3, width, bias=True, dtype=torch.float64)
            second = nn.Linear(width, 1, bias=True, dtype=torch.float64)
            first_weights.append(first.weight.detach())
            first_biases.append(first.bias.detach())
            second_weights.append(second.weight.detach().squeeze(0))
            second_biases.append(second.bias.detach().squeeze(0))
        self.first_weight = nn.Parameter(torch.stack(first_weights))
        self.first_bias = nn.Parameter(torch.stack(first_biases))
        self.second_weight = nn.Parameter(torch.stack(second_weights))
        self.second_bias = nn.Parameter(torch.stack(second_biases))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        hidden = torch.tanh(
            torch.einsum("ni,shi->snh", x, self.first_weight)
            + self.first_bias[:, None, :]
        )
        return (
            torch.einsum("snh,sh->sn", hidden, self.second_weight)
            + self.second_bias[:, None]
        )


def expected_losses(model: nn.Module, correlation: float) -> torch.Tensor:
    x, y, weight = distribution(correlation)
    logits = model(x)
    loss = nn.functional.binary_cross_entropy_with_logits(
        logits, y[None, :].expand_as(logits), reduction="none"
    )
    return (weight[None, :] * loss).sum(dim=1)


def run(
    seeds: tuple[int, ...],
    correlation: float,
    withdrawal_step: int,
    total_steps: int = 1_000,
) -> tuple[torch.Tensor, torch.Tensor]:
    model = BatchedTinyXOR(seeds)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.08)
    for step in range(total_steps):
        optimizer.zero_grad(set_to_none=True)
        phase_correlation = correlation if step < withdrawal_step else 0.5
        # Sum preserves each independent model's learning rate.
        expected_losses(model, phase_correlation).sum().backward()
        optimizer.step()

    x, y, weight = distribution(0.5)
    with torch.no_grad():
        logits = model(x)
        final_loss = (weight[None, :] * nn.functional.binary_cross_entropy_with_logits(
            logits, y[None, :].expand_as(logits), reduction="none"
        )).sum(dim=1)
        prediction = (logits >= 0).to(torch.float64)
        final_accuracy = (weight[None, :] * (prediction == y[None, :])).sum(dim=1)
    return final_loss, final_accuracy


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=1_000)
    args = parser.parse_args()
    seeds = tuple(range(10))
    correlations = (0.7, 0.9, 0.99, 1.0)
    withdrawals = (0, 5, 10, 20, 40, 80, 160, 320, 640)

    for correlation in correlations:
        baseline_loss_by_seed, baseline_accuracy_by_seed = run(
            seeds, correlation, 0, total_steps=args.steps
        )
        baseline_loss = float(baseline_loss_by_seed.mean())
        baseline_accuracy = float(baseline_accuracy_by_seed.mean())
        print(
            f"correlation={correlation:.2f} baseline_loss={baseline_loss:.8f} "
            f"baseline_accuracy={baseline_accuracy:.4f}"
        )
        for withdrawal in withdrawals[1:]:
            if withdrawal >= args.steps:
                continue
            loss_by_seed, accuracy_by_seed = run(
                seeds, correlation, withdrawal, total_steps=args.steps
            )
            mean_loss = float(loss_by_seed.mean())
            mean_accuracy = float(accuracy_by_seed.mean())
            paired_improvements = int((loss_by_seed < baseline_loss_by_seed).sum())
            print(
                f"  tau={withdrawal:>3d} loss={mean_loss:.8f} "
                f"delta_loss={mean_loss - baseline_loss:+.8f} "
                f"accuracy={mean_accuracy:.4f} "
                f"paired_loss_wins={paired_improvements}/{len(seeds)}"
            )


if __name__ == "__main__":
    main()
