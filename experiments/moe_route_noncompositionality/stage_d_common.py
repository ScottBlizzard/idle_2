#!/usr/bin/env python3
"""Frozen, outcome-agnostic utilities for Stage D.

This module contains only deterministic protocol mechanics.  It is imported by
preflight, acquisition, and analysis so that those entry points cannot silently
diverge in identifiers, seeds, answer verification, matching, or inference.
"""

from __future__ import annotations

import hashlib
import codecs
import math
import re
import signal
import unicodedata
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import numpy as np
import yaml


BASE_SEED = 20260828
DATASET_MULTIPLIER = 1_000_003
PROBLEM_MULTIPLIER = 10_007
LAYER_MULTIPLIER = 101
OUTSIDE_POOL_OFFSET = 50_000
OLMOE_LAYER_PAIRS = {
    "near_early": (3, 5),
    "medium": (3, 8),
    "far": (3, 13),
    "late": (8, 13),
}


def load_frozen_config(path: Path) -> dict[str, Any]:
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    if config.get("protocol_version") != "1.0-stage-d-amendment":
        raise RuntimeError("Unexpected Stage D protocol version")
    return config


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _byte_level_decoder() -> dict[str, int]:
    byte_values = list(range(ord("!"), ord("~") + 1))
    byte_values += list(range(ord("¡"), ord("¬") + 1))
    byte_values += list(range(ord("®"), ord("ÿ") + 1))
    unicode_values = list(byte_values)
    extra = 0
    for value in range(256):
        if value not in byte_values:
            byte_values.append(value)
            unicode_values.append(256 + extra)
            extra += 1
    return {chr(codepoint): byte for byte, codepoint in zip(byte_values, unicode_values)}


BYTE_LEVEL_DECODER = _byte_level_decoder()


def response_token_boundaries(
    tokenizer: Any, response_ids: Sequence[int]
) -> tuple[str, list[str], list[int]]:
    """Decode original byte-level BPE IDs into monotone character surfaces.

    Individual prefixes are not UTF-8 stable when one character spans multiple
    BPE tokens.  An incremental decoder assigns that character to the token
    completing it.  This uses the generated IDs directly, so decoded text need
    not re-tokenize to the same (potentially non-canonical) BPE segmentation.
    """
    ids = [int(value) for value in response_ids]
    expected = tokenizer.decode(
        ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )
    special_ids = {int(value) for value in tokenizer.all_special_ids}
    incremental = codecs.getincrementaldecoder("utf-8")(errors="replace")
    surfaces: list[str] = []
    for index, token_id in enumerate(ids):
        if token_id in special_ids:
            surfaces.append("")
            continue
        token = str(tokenizer.convert_ids_to_tokens(token_id))
        if all(character in BYTE_LEVEL_DECODER for character in token):
            payload = bytes(BYTE_LEVEL_DECODER[character] for character in token)
            surfaces.append(incremental.decode(payload, final=index == len(ids) - 1))
            continue
        # Added non-special tokens are literal strings rather than byte-alphabet
        # symbols. Flush any pending invalid suffix before inserting the literal.
        flushed = incremental.decode(b"", final=True)
        surfaces.append(flushed + token)
        incremental = codecs.getincrementaldecoder("utf-8")(errors="replace")
    if ids and ids[-1] in special_ids:
        surfaces[-1] += incremental.decode(b"", final=True)
    response = "".join(surfaces)
    if response != expected:
        raise RuntimeError("Direct byte-level token decoding disagreed with the tokenizer")
    ends: list[int] = []
    position = 0
    for surface in surfaces:
        position += len(surface)
        ends.append(position)
    return response, surfaces, ends


def shard_filename(stable_id: str) -> str:
    """Map an opaque stable ID to a single filesystem-safe shard name."""
    return hashlib.sha256(stable_id.encode("utf-8")).hexdigest() + ".json.gz"


def stable_problem_id(dataset: str, row: Mapping[str, Any]) -> str:
    if dataset == "gsm8k":
        source = str(row["question"])
        return hashlib.sha256(source.encode("utf-8")).hexdigest()
    if dataset == "math500":
        unique_id = str(row.get("unique_id") or "").strip()
        if unique_id:
            return unique_id
        source = str(row["problem"])
        return hashlib.sha256(source.encode("utf-8")).hexdigest()
    raise ValueError(f"Unknown dataset: {dataset}")


def stable_sort_rows(dataset: str, rows: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    resolved: list[dict[str, Any]] = []
    seen: set[str] = set()
    for original_index, row in enumerate(rows):
        item = dict(row)
        stable_id = stable_problem_id(dataset, item)
        if stable_id in seen:
            raise RuntimeError(f"Duplicate stable ID in {dataset}: {stable_id}")
        seen.add(stable_id)
        item["_stable_id"] = stable_id
        item["_original_row_index"] = original_index
        resolved.append(item)
    resolved.sort(key=lambda item: (item["_stable_id"], item["_original_row_index"]))
    for ordinal, item in enumerate(resolved):
        item["_stable_ordinal"] = ordinal
        item["_fold"] = ordinal % 5
    return resolved


def generation_seed(dataset_code: int, problem_ordinal: int, sample_index: int) -> int:
    return (
        BASE_SEED
        + DATASET_MULTIPLIER * dataset_code
        + PROBLEM_MULTIPLIER * problem_ordinal
        + sample_index
    )


def gumbel_seed(dataset_code: int, problem_ordinal: int, layer: int, draw: int) -> int:
    return (
        BASE_SEED
        + DATASET_MULTIPLIER * dataset_code
        + PROBLEM_MULTIPLIER * problem_ordinal
        + LAYER_MULTIPLIER * layer
        + draw
    )


def upward_round(value: float) -> int:
    return int(math.floor(value + 0.5))


def resolve_layer_pairs(num_layers: int) -> dict[str, tuple[int, int]]:
    relative = {
        "near_early": (0.20, 0.30),
        "medium": (0.20, 0.55),
        "far": (0.20, 0.85),
        "late": (0.55, 0.85),
    }
    pairs = {
        name: (
            upward_round(first * (num_layers - 1)),
            upward_round(second * (num_layers - 1)),
        )
        for name, (first, second) in relative.items()
    }
    if num_layers == 16 and pairs != OLMOE_LAYER_PAIRS:
        raise RuntimeError(f"Frozen OLMoE layer mapping changed: {pairs}")
    if any(first >= second for first, second in pairs.values()):
        raise RuntimeError(f"Invalid layer mapping: {pairs}")
    return pairs


def build_alternatives(
    router_logits: np.ndarray,
    standard_route: Sequence[int],
    dataset_code: int,
    problem_ordinal: int,
    layer: int,
    pool_size: int = 16,
    count: int = 6,
    maximum_draw_attempts: int = 100,
) -> list[tuple[int, ...]]:
    values = np.asarray(router_logits, dtype=np.float64)
    if values.ndim != 1:
        raise ValueError("router_logits must be one-dimensional")
    if pool_size < len(standard_route) or pool_size > values.size:
        raise ValueError("Invalid candidate pool size")
    pool = np.argsort(-values, kind="stable")[:pool_size]
    pool_logits = values[pool]
    standard = tuple(sorted(int(x) for x in standard_route))
    alternatives: list[tuple[int, ...]] = []
    for draw in range(maximum_draw_attempts):
        rng = np.random.default_rng(gumbel_seed(dataset_code, problem_ordinal, layer, draw))
        perturbed = pool_logits + rng.gumbel(size=pool_size)
        selected_positions = np.argpartition(perturbed, -len(standard))[-len(standard) :]
        route = tuple(sorted(int(pool[position]) for position in selected_positions))
        if route != standard and route not in alternatives:
            alternatives.append(route)
            if len(alternatives) == count:
                return alternatives
    raise RuntimeError(f"Only produced {len(alternatives)} distinct alternatives")


def build_outside_pool_route(
    router_logits: np.ndarray,
    cardinality: int,
    dataset_code: int,
    problem_ordinal: int,
    layer: int,
) -> tuple[int, ...]:
    values = np.asarray(router_logits, dtype=np.float64)
    ranked = np.argsort(-values, kind="stable")
    outside = ranked[16:]
    if outside.size < cardinality:
        raise RuntimeError("Outside-top-16 pool is smaller than route cardinality")
    rng = np.random.default_rng(
        gumbel_seed(dataset_code, problem_ordinal, layer, OUTSIDE_POOL_OFFSET)
    )
    return tuple(sorted(int(x) for x in rng.choice(outside, cardinality, replace=False)))


@dataclass(frozen=True)
class ExtractedAnswer:
    value: str
    start: int
    end: int
    method: str


def _last_balanced_box(text: str) -> ExtractedAnswer | None:
    start = text.rfind("\\boxed")
    if start < 0:
        return None
    brace = text.find("{", start + len("\\boxed"))
    if brace < 0:
        tail = text[start + len("\\boxed") :].strip()
        if not tail:
            return None
        value_start = text.find(tail, start + len("\\boxed"))
        return ExtractedAnswer(tail, start, value_start + len(tail), "boxed_space")
    depth = 0
    for index in range(brace, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return ExtractedAnswer(text[brace + 1 : index], start, index + 1, "boxed")
    return None


_FINAL_ANSWER_RE = re.compile(r"(?is)final\s+answer\s*(?:is|:|=)\s*(.+)")
_NUMBER_RE = re.compile(r"[-+]?(?:\d[\d,]*\.?\d*|\.\d+)(?:[eE][-+]?\d+)?%?")


def extract_gsm8k_prediction(text: str) -> ExtractedAnswer | None:
    marker = text.rfind("####")
    if marker >= 0:
        tail = text[marker + 4 :]
        matches = list(_NUMBER_RE.finditer(tail))
        if matches:
            match = matches[-1]
            return ExtractedAnswer(
                match.group(0), marker, marker + 4 + match.end(), "hash_marker"
            )
    final_matches = list(_FINAL_ANSWER_RE.finditer(text))
    if final_matches:
        match = final_matches[-1]
        numbers = list(_NUMBER_RE.finditer(match.group(1)))
        if numbers:
            number = numbers[-1]
            absolute_end = match.start(1) + number.end()
            return ExtractedAnswer(number.group(0), match.start(), absolute_end, "final_answer")
    numbers = list(_NUMBER_RE.finditer(text))
    if numbers:
        match = numbers[-1]
        return ExtractedAnswer(match.group(0), match.start(), match.end(), "last_number")
    return None


def extract_math_prediction(text: str) -> ExtractedAnswer | None:
    boxed = _last_balanced_box(text)
    if boxed is not None:
        return boxed
    matches = list(_FINAL_ANSWER_RE.finditer(text))
    if not matches:
        return None
    match = matches[-1]
    value = match.group(1).strip().splitlines()[0].strip().rstrip(".")
    if not value:
        return None
    value_start = text.find(value, match.start(1))
    return ExtractedAnswer(value, match.start(), value_start + len(value), "final_answer")


def extract_math_gold(row: Mapping[str, Any]) -> str | None:
    answer = str(row.get("answer") or "").strip()
    if answer:
        return answer
    solution = str(row.get("solution") or "")
    boxed = _last_balanced_box(solution)
    return None if boxed is None else boxed.value


def _normalized_decimal(value: str) -> Decimal | None:
    cleaned = value.strip().replace(",", "")
    cleaned = cleaned.strip("$£€¥% ").rstrip(".")
    try:
        number = Decimal(cleaned)
    except (InvalidOperation, ValueError):
        return None
    return number if number.is_finite() else None


def verify_gsm8k(response: str, reference_answer: str) -> tuple[bool, ExtractedAnswer | None]:
    prediction = extract_gsm8k_prediction(response)
    marker = reference_answer.rfind("####")
    gold_text = reference_answer[marker + 4 :] if marker >= 0 else reference_answer
    gold_matches = list(_NUMBER_RE.finditer(gold_text))
    if prediction is None or not gold_matches:
        return False, prediction
    predicted_number = _normalized_decimal(prediction.value)
    gold_number = _normalized_decimal(gold_matches[-1].group(0))
    return predicted_number is not None and predicted_number == gold_number, prediction


@contextmanager
def _verification_timeout(seconds: int):
    if not hasattr(signal, "SIGALRM"):
        yield
        return
    previous = signal.getsignal(signal.SIGALRM)

    def handler(signum: int, frame: Any) -> None:
        raise TimeoutError("answer verification timed out")

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def verify_math500(
    response: str, row: Mapping[str, Any], timeout_seconds: int = 2
) -> tuple[bool, ExtractedAnswer | None]:
    prediction = extract_math_prediction(response)
    gold = extract_math_gold(row)
    if prediction is None or gold is None:
        return False, prediction
    try:
        from math_verify import LatexExtractionConfig, parse, verify

        with _verification_timeout(timeout_seconds):
            parsed_gold = parse(
                "\\boxed{" + gold + "}",
                extraction_config=[LatexExtractionConfig()],
            )
            parsed_prediction = parse(
                "\\boxed{" + prediction.value + "}",
                extraction_config=[LatexExtractionConfig()],
            )
            outcome = verify(parsed_gold, parsed_prediction)
        return bool(outcome) if isinstance(outcome, (bool, np.bool_)) else False, prediction
    except Exception:
        return False, prediction


def token_surface_is_eligible(surface: str) -> bool:
    normalized = unicodedata.normalize("NFKC", surface).strip()
    if not normalized:
        return False
    return any(unicodedata.category(character)[0] in {"L", "N"} for character in normalized)


def select_fragile_token(
    probabilities: Sequence[float],
    surfaces: Sequence[str],
    token_ends: Sequence[int],
    final_answer_start: int,
    probability_max: float = 0.50,
) -> int | None:
    if not (len(probabilities) == len(surfaces) == len(token_ends)):
        raise ValueError("Token arrays have different lengths")
    eligible = [
        index
        for index, (probability, surface, end) in enumerate(
            zip(probabilities, surfaces, token_ends)
        )
        if float(probability) <= probability_max
        and end <= final_answer_start
        and token_surface_is_eligible(surface)
    ]
    if not eligible:
        return None
    return min(eligible, key=lambda index: (float(probabilities[index]), index))


def _route_covariates(record: Mapping[str, Any]) -> np.ndarray:
    return np.asarray(
        [
            record["router_score_sum_i"],
            record["router_score_sum_j"],
            record["standard_overlap_i"],
            record["standard_overlap_j"],
            record["pair_overlap"],
            record["single_residual_norm_i"],
            record["single_residual_norm_j"],
            record["normalized_layer_separation"],
        ],
        dtype=np.float64,
    )


def matched_null_for_problem(records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    if len(records) != 36:
        raise ValueError(f"Expected 36 route pairs, found {len(records)}")
    matrix = np.stack([_route_covariates(record) for record in records])
    means = matrix.mean(axis=0)
    stds = matrix.std(axis=0, ddof=1)
    standardized = np.divide(
        matrix - means,
        stds,
        out=np.zeros_like(matrix),
        where=stds > 0,
    )
    donor_indices: list[list[int]] = []
    balance: list[np.ndarray] = []
    for index, record in enumerate(records):
        candidates: list[tuple[float, int, int, int]] = []
        for donor_index, donor in enumerate(records):
            if donor_index == index:
                continue
            distance = float(np.linalg.norm(standardized[index] - standardized[donor_index]))
            candidates.append(
                (
                    distance,
                    int(donor["route_i_index"]),
                    int(donor["route_j_index"]),
                    donor_index,
                )
            )
        candidates.sort()
        selected = [candidate[3] for candidate in candidates[:3]]
        if len(selected) != 3:
            raise RuntimeError("Fewer than three matched-null donors")
        donor_indices.append(selected)
        balance.extend(np.abs(standardized[index] - standardized[selected]))

    result_rows: list[dict[str, Any]] = []
    for index, record in enumerate(records):
        single_i = float(record["single_effect_i"])
        single_j = float(record["single_effect_j"])
        joint = float(record["joint_effect"])
        donor_nulls = []
        for donor_index in donor_indices[index]:
            donor = records[donor_index]
            interaction = float(donor["joint_effect"]) - float(
                donor["single_effect_i"]
            ) - float(donor["single_effect_j"])
            donor_nulls.append(single_i + single_j + interaction)
        h1_eligible = single_i > 0 and single_j > 0
        h2_eligible = single_i <= 0 and single_j <= 0
        result_rows.append(
            {
                "route_i_index": int(record["route_i_index"]),
                "route_j_index": int(record["route_j_index"]),
                "h1_eligible": h1_eligible,
                "h1_observed": float(joint < 0) if h1_eligible else None,
                "h1_null": float(np.mean(np.asarray(donor_nulls) < 0)) if h1_eligible else None,
                "h2_eligible": h2_eligible,
                "h2_observed": float(joint > 0) if h2_eligible else None,
                "h2_null": float(np.mean(np.asarray(donor_nulls) > 0)) if h2_eligible else None,
                "donors": donor_indices[index],
            }
        )
    balance_array = np.stack(balance)
    return {
        "rows": result_rows,
        "balance_mean_abs_by_coordinate": balance_array.mean(axis=0).tolist(),
        "h1_eligible_pairs": sum(row["h1_eligible"] for row in result_rows),
        "h2_eligible_pairs": sum(row["h2_eligible"] for row in result_rows),
    }


def problem_weighted_reversal_effect(
    matched_by_problem: Mapping[str, Mapping[str, Any]], hypothesis: str
) -> tuple[float, dict[str, float], int]:
    if hypothesis not in {"h1", "h2"}:
        raise ValueError(hypothesis)
    per_problem: dict[str, float] = {}
    pair_count = 0
    for problem_id, result in matched_by_problem.items():
        rows = [row for row in result["rows"] if row[f"{hypothesis}_eligible"]]
        if not rows:
            continue
        pair_count += len(rows)
        per_problem[problem_id] = float(
            np.mean(
                [row[f"{hypothesis}_observed"] - row[f"{hypothesis}_null"] for row in rows]
            )
        )
    if not per_problem:
        return float("nan"), per_problem, pair_count
    return float(np.mean(list(per_problem.values()))), per_problem, pair_count


def h3_for_problem(records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    lookup = {
        (int(record["route_i_index"]), int(record["route_j_index"])): record
        for record in records
    }
    if set(lookup) != {(i, j) for i in range(6) for j in range(6)}:
        raise ValueError("H3 requires the complete 6x6 joint grid")
    first_by_index = {i: float(lookup[(i, 0)]["single_effect_i"]) for i in range(6)}
    second_by_index = {j: float(lookup[(0, j)]["single_effect_j"]) for j in range(6)}
    best_i = max(range(6), key=lambda i: (first_by_index[i], -i))
    best_j = max(range(6), key=lambda j: (second_by_index[j], -j))
    independent_effect = float(lookup[(best_i, best_j)]["joint_effect"])
    direct_candidates = [(k, k) for k in range(6)] + [(k, (k + 1) % 6) for k in range(6)]
    direct_pair = max(
        direct_candidates,
        key=lambda pair: (float(lookup[pair]["joint_effect"]), -pair[0], -pair[1]),
    )
    direct_effect = float(lookup[direct_pair]["joint_effect"])
    return {
        "independent_pair": [best_i, best_j],
        "direct_pair": list(direct_pair),
        "independent_effect": independent_effect,
        "direct_effect": direct_effect,
        "success_difference": float(direct_effect > 0) - float(independent_effect > 0),
        "margin_gap": direct_effect - independent_effect,
    }


def bootstrap_mean(
    values_by_problem: Mapping[str, float],
    resamples: int,
    seed: int,
) -> np.ndarray:
    problem_ids = sorted(values_by_problem)
    if not problem_ids:
        raise ValueError("No problem clusters to bootstrap")
    values = np.asarray([values_by_problem[problem_id] for problem_id in problem_ids], dtype=np.float64)
    rng = np.random.default_rng(seed)
    draws = rng.integers(0, len(values), size=(resamples, len(values)))
    return values[draws].mean(axis=1)


def percentile_interval(samples: Sequence[float], confidence: float = 0.95) -> tuple[float, float]:
    alpha = 1.0 - confidence
    low, high = np.quantile(np.asarray(samples, dtype=np.float64), [alpha / 2, 1 - alpha / 2])
    return float(low), float(high)


def centered_bootstrap_p_value(
    estimate: float, samples: Sequence[float], null_boundary: float
) -> float:
    values = np.asarray(samples, dtype=np.float64)
    count = int(np.count_nonzero(values - estimate >= estimate - null_boundary))
    return (1.0 + count) / (len(values) + 1.0)


def benjamini_hochberg(p_values: Sequence[float]) -> list[float]:
    values = np.asarray(p_values, dtype=np.float64)
    if values.ndim != 1 or np.any(~np.isfinite(values)) or np.any((values < 0) | (values > 1)):
        raise ValueError("p-values must be finite numbers in [0,1]")
    order = np.argsort(values, kind="stable")
    adjusted_sorted = np.empty(len(values), dtype=np.float64)
    running = 1.0
    for reverse_rank in range(len(values) - 1, -1, -1):
        index = order[reverse_rank]
        rank = reverse_rank + 1
        running = min(running, float(values[index]) * len(values) / rank)
        adjusted_sorted[reverse_rank] = running
    adjusted = np.empty(len(values), dtype=np.float64)
    adjusted[order] = np.minimum(adjusted_sorted, 1.0)
    return adjusted.tolist()


def group_records(records: Iterable[Mapping[str, Any]], *keys: str) -> dict[tuple[Any, ...], list[Mapping[str, Any]]]:
    grouped: dict[tuple[Any, ...], list[Mapping[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[tuple(record[key] for key in keys)].append(record)
    return dict(grouped)
