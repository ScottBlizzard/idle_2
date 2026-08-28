#!/usr/bin/env python3
"""Frozen cross-fitted H4 predictors for Stage D."""

from __future__ import annotations

import copy
import math
import random
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

import numpy as np
import torch
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


CONTEXT = slice(0, 32)
LAYERS = slice(32, 35)
ROUTE_I = slice(35, 99)
ROUTE_J = slice(99, 163)
STANDARD_I = slice(163, 227)
STANDARD_J = slice(227, 291)
SUMMARY_I = slice(291, 297)
SUMMARY_J = slice(297, 303)
OVERLAPS = slice(303, 306)
PREDICTED_SINGLES = slice(306, 308)
FEATURE_DIMENSION = 308
SUMMARY_KEYS = ("sum", "mean", "minimum", "maximum", "rank_mean", "rank_maximum")
MODEL_SEEDS = (20260828, 20260829, 20260830)


def multihot(route: Sequence[int], size: int = 64) -> np.ndarray:
    result = np.zeros(size, dtype=np.float32)
    result[list(route)] = 1.0
    return result


def single_feature(record: Mapping[str, Any], side: str) -> np.ndarray:
    if side == "i":
        layer = float(record["layer_i"]) / 15.0
        route = record["route_i"]
        standard = record["standard_route_i"]
        summary = record["router_summary_i"]
        overlap = record["standard_overlap_i"]
    elif side == "j":
        layer = float(record["layer_j"]) / 15.0
        route = record["route_j"]
        standard = record["standard_route_j"]
        summary = record["router_summary_j"]
        overlap = record["standard_overlap_j"]
    else:
        raise ValueError(side)
    return np.concatenate(
        [
            np.asarray(record["hidden_projection"], dtype=np.float32),
            np.asarray([layer], dtype=np.float32),
            multihot(route),
            multihot(standard),
            np.asarray([summary[key] for key in SUMMARY_KEYS], dtype=np.float32),
            np.asarray([overlap], dtype=np.float32),
        ]
    )


def cross_fitted_single_predictions(records: Sequence[Mapping[str, Any]]) -> dict[tuple[str, str, int], float]:
    unique: dict[tuple[str, str, int], tuple[np.ndarray, float, int]] = {}
    for record in records:
        problem = str(record["problem_id"])
        fold = int(record["fold"])
        for side, index_key, effect_key in (
            ("i", "route_i_index", "single_effect_i"),
            ("j", "route_j_index", "single_effect_j"),
        ):
            key = (problem, side, int(record[index_key]))
            value = (single_feature(record, side), float(record[effect_key]), fold)
            if key in unique:
                old = unique[key]
                if not np.array_equal(old[0], value[0]) or old[1:] != value[1:]:
                    raise RuntimeError(f"Inconsistent duplicate single record: {key}")
            unique[key] = value
    predictions: dict[tuple[str, str, int], float] = {}
    for fold in range(5):
        train = [(key, value) for key, value in unique.items() if value[2] != fold]
        test = [(key, value) for key, value in unique.items() if value[2] == fold]
        if not train or not test:
            raise RuntimeError(f"Empty single-effect outer fold {fold}")
        model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
        model.fit(np.stack([value[0] for _, value in train]), [value[1] for _, value in train])
        output = model.predict(np.stack([value[0] for _, value in test]))
        predictions.update({key: float(prediction) for (key, _), prediction in zip(test, output)})
    if set(predictions) != set(unique):
        raise RuntimeError("Cross-fitted single predictions are incomplete")
    return predictions


def joint_feature(
    record: Mapping[str, Any], single_predictions: Mapping[tuple[str, str, int], float]
) -> np.ndarray:
    problem = str(record["problem_id"])
    predicted_i = single_predictions[(problem, "i", int(record["route_i_index"]))]
    predicted_j = single_predictions[(problem, "j", int(record["route_j_index"]))]
    return np.concatenate(
        [
            np.asarray(record["hidden_projection"], dtype=np.float32),
            np.asarray(
                [
                    float(record["layer_i"]) / 15.0,
                    float(record["layer_j"]) / 15.0,
                    float(record["normalized_layer_separation"]),
                ],
                dtype=np.float32,
            ),
            multihot(record["route_i"]),
            multihot(record["route_j"]),
            multihot(record["standard_route_i"]),
            multihot(record["standard_route_j"]),
            np.asarray(
                [record["router_summary_i"][key] for key in SUMMARY_KEYS], dtype=np.float32
            ),
            np.asarray(
                [record["router_summary_j"][key] for key in SUMMARY_KEYS], dtype=np.float32
            ),
            np.asarray(
                [
                    record["standard_overlap_i"],
                    record["standard_overlap_j"],
                    record["pair_overlap"],
                ],
                dtype=np.float32,
            ),
            np.asarray([predicted_i, predicted_j], dtype=np.float32),
        ]
    )


class CompatibilityModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.expert_i = nn.Parameter(torch.empty(64, 8))
        self.expert_j = nn.Parameter(torch.empty(64, 8))
        self.context = nn.Linear(32, 8)
        self.bilinear_weight = nn.Parameter(torch.ones(8))
        self.scalar = nn.Linear(18, 1)
        nn.init.normal_(self.expert_i, std=0.02)
        nn.init.normal_(self.expert_j, std=0.02)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        route_i = features[:, ROUTE_I]
        route_j = features[:, ROUTE_J]
        embedding_i = route_i @ self.expert_i / 8.0
        embedding_j = route_j @ self.expert_j / 8.0
        context = torch.tanh(self.context(features[:, CONTEXT]))
        interaction = torch.sum(
            embedding_i * embedding_j * context * self.bilinear_weight, dim=1
        )
        scalars = torch.cat(
            [features[:, LAYERS], features[:, SUMMARY_I], features[:, SUMMARY_J], features[:, OVERLAPS]],
            dim=1,
        )
        additive = features[:, PREDICTED_SINGLES].sum(dim=1)
        return additive + interaction + self.scalar(scalars).squeeze(1)


class ParameterPad(nn.Module):
    def __init__(self, count: int) -> None:
        super().__init__()
        self.unused = nn.Parameter(torch.zeros(max(0, count)))


class MatchedMLP(nn.Module):
    def __init__(self, target_parameters: int) -> None:
        super().__init__()
        width = 1
        while True:
            trial_parameters = (FEATURE_DIMENSION + 1) * width + (width + 1)
            if trial_parameters > target_parameters:
                break
            width += 1
        width = max(1, width - 1)
        self.network = nn.Sequential(
            nn.Linear(FEATURE_DIMENSION, width),
            nn.ReLU(),
            nn.Linear(width, 1),
        )
        current = trainable_parameter_count(self)
        self.padding = ParameterPad(target_parameters - current)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        return self.network(features).squeeze(1)


class MatchedGRU(nn.Module):
    def __init__(self, target_parameters: int) -> None:
        super().__init__()
        step_dimension = 169
        width = 1
        while True:
            trial = nn.GRU(step_dimension, width, batch_first=True)
            head_parameters = width + 4
            if sum(parameter.numel() for parameter in trial.parameters()) + head_parameters > target_parameters:
                break
            width += 1
        width = max(1, width - 1)
        self.gru = nn.GRU(step_dimension, width, batch_first=True)
        self.head = nn.Linear(width + 3, 1)
        current = trainable_parameter_count(self)
        self.padding = ParameterPad(target_parameters - current)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        context = features[:, CONTEXT]
        separation = features[:, LAYERS.start + 2 : LAYERS.stop]
        first = torch.cat(
            [
                context,
                features[:, LAYERS.start : LAYERS.start + 1],
                separation,
                features[:, ROUTE_I],
                features[:, STANDARD_I],
                features[:, SUMMARY_I],
                features[:, OVERLAPS.start : OVERLAPS.start + 1],
            ],
            dim=1,
        )
        second = torch.cat(
            [
                context,
                features[:, LAYERS.start + 1 : LAYERS.start + 2],
                separation,
                features[:, ROUTE_J],
                features[:, STANDARD_J],
                features[:, SUMMARY_J],
                features[:, OVERLAPS.start + 1 : OVERLAPS.start + 2],
            ],
            dim=1,
        )
        sequence = torch.stack([first, second], dim=1)
        _, hidden = self.gru(sequence)
        additive = features[:, PREDICTED_SINGLES].sum(dim=1)
        head_input = torch.cat(
            [hidden[-1], features[:, OVERLAPS.start + 2 : OVERLAPS.stop], features[:, PREDICTED_SINGLES]],
            dim=1,
        )
        return additive + self.head(head_input).squeeze(1)


def trainable_parameter_count(model: nn.Module) -> int:
    return sum(parameter.numel() for parameter in model.parameters() if parameter.requires_grad)


def model_factories() -> tuple[dict[str, Any], int]:
    compatibility = CompatibilityModel()
    parameter_count = trainable_parameter_count(compatibility)
    factories = {
        "compatibility": CompatibilityModel,
        "mlp": lambda: MatchedMLP(parameter_count),
        "gru": lambda: MatchedGRU(parameter_count),
    }
    for name, factory in factories.items():
        count = trainable_parameter_count(factory())
        if count != parameter_count:
            raise RuntimeError(f"Parameter matching failed for {name}: {count} != {parameter_count}")
    return factories, parameter_count


def deterministic_validation_ids(training_problem_ids: Sequence[str]) -> set[str]:
    ordered = sorted(set(training_problem_ids))
    selected = set(ordered[::10])
    if len(selected) == len(ordered) and len(ordered) > 1:
        selected = {ordered[0]}
    return selected


def train_neural_model(
    factory: Any,
    x_train: np.ndarray,
    y_train: np.ndarray,
    train_problem_ids: Sequence[str],
    seed: int,
) -> nn.Module:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    model = factory()
    validation_ids = deterministic_validation_ids(train_problem_ids)
    validation_mask = np.asarray([problem in validation_ids for problem in train_problem_ids])
    training_mask = ~validation_mask
    if not training_mask.any() or not validation_mask.any():
        raise RuntimeError("Inner training/validation split is empty")
    train_dataset = TensorDataset(
        torch.from_numpy(x_train[training_mask]).float(),
        torch.from_numpy(y_train[training_mask]).float(),
    )
    generator = torch.Generator().manual_seed(seed)
    loader = DataLoader(train_dataset, batch_size=256, shuffle=True, generator=generator)
    validation_x = torch.from_numpy(x_train[validation_mask]).float()
    validation_y = torch.from_numpy(y_train[validation_mask]).float()
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.0)
    best_state = copy.deepcopy(model.state_dict())
    best_loss = float("inf")
    stale = 0
    for _ in range(200):
        model.train()
        for batch_x, batch_y in loader:
            optimizer.zero_grad(set_to_none=True)
            loss = torch.mean((model(batch_x) - batch_y) ** 2)
            loss.backward()
            optimizer.step()
        model.eval()
        with torch.no_grad():
            validation_loss = float(torch.mean((model(validation_x) - validation_y) ** 2).item())
        if validation_loss < best_loss - 1e-12:
            best_loss = validation_loss
            best_state = copy.deepcopy(model.state_dict())
            stale = 0
        else:
            stale += 1
            if stale >= 20:
                break
    model.load_state_dict(best_state)
    model.eval()
    return model


@dataclass
class H4Predictions:
    problem_ids: list[str]
    targets: np.ndarray
    predictions: dict[str, np.ndarray]
    parameter_count: int


def cross_fitted_joint_predictions(records: Sequence[Mapping[str, Any]]) -> H4Predictions:
    singles = cross_fitted_single_predictions(records)
    features = np.stack([joint_feature(record, singles) for record in records]).astype(np.float32)
    if features.shape[1] != FEATURE_DIMENSION:
        raise RuntimeError(f"Unexpected feature dimension: {features.shape}")
    targets = np.asarray([record["joint_effect"] for record in records], dtype=np.float32)
    problem_ids = [str(record["problem_id"]) for record in records]
    folds = np.asarray([int(record["fold"]) for record in records])
    factories, parameter_count = model_factories()
    predictions = {
        "compatibility": np.full(len(records), np.nan, dtype=np.float64),
        "mlp": np.full(len(records), np.nan, dtype=np.float64),
        "gru": np.full(len(records), np.nan, dtype=np.float64),
        "additive": features[:, PREDICTED_SINGLES].sum(axis=1).astype(np.float64),
        "router_ridge": np.full(len(records), np.nan, dtype=np.float64),
        "single_overlap_ridge": np.full(len(records), np.nan, dtype=np.float64),
    }
    router_columns = np.r_[np.arange(SUMMARY_I.start, SUMMARY_J.stop), np.arange(OVERLAPS.start, OVERLAPS.stop)]
    single_overlap_columns = np.r_[np.arange(PREDICTED_SINGLES.start, PREDICTED_SINGLES.stop), np.arange(OVERLAPS.start, OVERLAPS.stop)]
    for fold in range(5):
        train_mask = folds != fold
        test_mask = folds == fold
        if not train_mask.any() or not test_mask.any():
            raise RuntimeError(f"Empty joint outer fold {fold}")
        for name, columns in (
            ("router_ridge", router_columns),
            ("single_overlap_ridge", single_overlap_columns),
        ):
            ridge = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
            ridge.fit(features[train_mask][:, columns], targets[train_mask])
            predictions[name][test_mask] = ridge.predict(features[test_mask][:, columns])
        training_problem_ids = [problem_ids[index] for index in np.flatnonzero(train_mask)]
        for name, factory in factories.items():
            seeded = []
            for seed in MODEL_SEEDS:
                model = train_neural_model(
                    factory,
                    features[train_mask],
                    targets[train_mask],
                    training_problem_ids,
                    seed,
                )
                with torch.no_grad():
                    seeded.append(model(torch.from_numpy(features[test_mask]).float()).numpy())
            predictions[name][test_mask] = np.mean(np.stack(seeded), axis=0)
    if any(np.any(~np.isfinite(values)) for values in predictions.values()):
        raise RuntimeError("Non-finite cross-fitted prediction")
    return H4Predictions(problem_ids, targets.astype(np.float64), predictions, parameter_count)


def problem_spearman(
    problem_ids: Sequence[str], targets: np.ndarray, predictions: np.ndarray
) -> dict[str, float]:
    result: dict[str, float] = {}
    for problem in sorted(set(problem_ids)):
        indices = [index for index, value in enumerate(problem_ids) if value == problem]
        correlation = spearmanr(targets[indices], predictions[indices]).statistic
        result[problem] = 0.0 if not np.isfinite(correlation) else float(correlation)
    return result
