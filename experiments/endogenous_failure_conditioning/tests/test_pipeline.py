from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

EXPERIMENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXPERIMENT))
sys.path.insert(0, str(EXPERIMENT.parents[1]))

from analyze_pilot import family_interaction, size_delta
from common import build_messages, case_id, prompt_payload_hash
from prepare_error_bank import rank_bins, stratified_problem_sample


def record(generator: str = "qwen_3b") -> dict:
    return {
        "error_id": "error-1",
        "question": "What is 1+1?",
        "error_response": "1+1=3. Final answer: \\boxed{3}",
        "generator_key": generator,
    }


def test_wrappers_preserve_raw_payload() -> None:
    row = record()
    for wrapper in ("external_neutral", "assistant_history"):
        messages = build_messages(row, wrapper)
        assert sum(message["content"].count(row["question"]) for message in messages) == 1
        assert sum(message["content"].count(row["error_response"]) for message in messages) == 1
        assert len(prompt_payload_hash(row, wrapper)) == 64
    assert case_id("e", "m", "w") == case_id("e", "m", "w")


def test_rank_bins_are_deterministic_and_bounded() -> None:
    values = {f"p{i}": float(i) for i in range(11)}
    bins = rank_bins(values)
    assert set(bins.values()) == {0, 1, 2, 3}
    assert bins == rank_bins(dict(reversed(list(values.items()))))


def synthetic_rows() -> list[dict]:
    rows = []
    models = {
        "qwen_3b": ("qwen", 0),
        "qwen_7b": ("qwen", 1),
        "gemma_2b": ("gemma", 0),
        "gemma_9b": ("gemma", 1),
    }
    for problem in range(10):
        for generator, (generator_family, _) in models.items():
            for corrector, (corrector_family, rank) in models.items():
                same = generator_family == corrector_family
                rows.append(
                    {
                        "domain": "gsm8k",
                        "wrapper": "external_neutral",
                        "problem_key": str(problem),
                        "generator_key": generator,
                        "generator_family": generator_family,
                        "corrector_key": corrector,
                        "corrector_family": corrector_family,
                        "corrector_size_rank": rank,
                        "correct": bool((not same) or rank == 1),
                    }
                )
    return rows


def test_family_interaction_and_size_delta() -> None:
    rows = synthetic_rows()
    assert family_interaction(rows, "gsm8k", "external_neutral") < 0
    assert size_delta(rows, "gsm8k", "qwen", False) > 0


def test_stratified_sample_uses_shared_problems() -> None:
    model_config = {
        "m1": {"hf_id": "a"},
        "m2": {"hf_id": "b"},
    }
    candidates = {
        f"gsm8k:{index}": {
            "m1": {"dataset_idx": index, "response": "x" * (index + 1)},
            "m2": {"dataset_idx": index, "response": "y" * (index + 2)},
        }
        for index in range(20)
    }
    difficulty = {
        "a": {("gsm8k_full", index): index / 20 for index in range(20)},
        "b": {("gsm8k_full", index): (20 - index) / 20 for index in range(20)},
    }
    selected = stratified_problem_sample(
        candidates, difficulty, model_config, "gsm8k_full", 12, 7
    )
    assert len(selected) == 12
    assert len(set(selected)) == 12
    assert set(selected) <= set(candidates)
