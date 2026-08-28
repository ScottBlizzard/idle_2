#!/usr/bin/env python3
"""Sealed Stage D trajectory and route-effect acquisition for OLMoE.

The console intentionally reports engineering progress only.  Scientific
effects are written to per-problem shards and are not aggregated here.
"""

from __future__ import annotations

import argparse
import gzip
import json
import math
import os
import platform
import random
import tempfile
import time
import types
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

from stage_d_common import (
    BASE_SEED,
    OLMOE_LAYER_PAIRS,
    build_alternatives,
    build_outside_pool_route,
    extract_gsm8k_prediction,
    extract_math_prediction,
    generation_seed,
    load_frozen_config,
    resolve_layer_pairs,
    select_fragile_token,
    sha256_bytes,
    sha256_file,
    shard_filename,
    stable_sort_rows,
    verify_gsm8k,
    verify_math500,
)


MODEL_ID = "allenai/OLMoE-1B-7B-0924-Instruct"
DATASETS = {
    "gsm8k": {
        "hf_name": "openai/gsm8k",
        "subset": "main",
        "split": "test",
        "question_field": "question",
        "dataset_code": 0,
    },
    "math500": {
        "hf_name": "HuggingFaceH4/MATH-500",
        "subset": None,
        "split": "test",
        "question_field": "problem",
        "dataset_code": 1,
    },
}


class HardStop(RuntimeError):
    pass


@dataclass
class AcquisitionClock:
    started: float
    maximum_seconds: float

    def elapsed(self) -> float:
        return time.perf_counter() - self.started

    def check(self, reserve_seconds: float = 0.0) -> None:
        if self.elapsed() + reserve_seconds >= self.maximum_seconds:
            raise HardStop("Stage D cumulative six-hour hard stop reached")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--dataset-cache-dir", type=Path, required=True)
    parser.add_argument("--frozen-config", type=Path, required=True)
    parser.add_argument("--thresholds", type=Path, required=True)
    parser.add_argument("--model", default=MODEL_ID)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--target-per-dataset", type=int, default=64)
    parser.add_argument("--minimum-per-dataset", type=int, default=48)
    parser.add_argument("--max-problems-per-dataset", type=int, default=0)
    parser.add_argument("--max-gpu-hours", type=float, default=6.0)
    parser.add_argument("--analysis-reserve-seconds", type=float, default=1800.0)
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--preflight-problems-per-dataset", type=int, default=2)
    parser.add_argument("--allow-existing-empty-output", action="store_true")
    return parser.parse_args()


def json_dump_atomic(path: Path, payload: Any, *, gzip_output: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb", dir=path.parent, prefix=path.name + ".", suffix=".tmp", delete=False
    ) as handle:
        temporary = Path(handle.name)
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        if gzip_output:
            handle.write(gzip.compress(raw, compresslevel=9, mtime=0))
        else:
            handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    if path.exists():
        temporary.unlink(missing_ok=True)
        raise FileExistsError(f"Refusing to overwrite sealed shard: {path}")
    temporary.replace(path)


def tensor_error(first: torch.Tensor, second: torch.Tensor) -> float:
    return float((first.float() - second.float()).abs().max().item())


def route_overlap(first: Sequence[int], second: Sequence[int]) -> float:
    return len(set(first).intersection(second)) / len(first)


def route_summary(router_logits: torch.Tensor, route: Sequence[int]) -> dict[str, float]:
    values = router_logits[list(route)].float().cpu().numpy()
    ranks = np.empty(router_logits.numel(), dtype=np.int64)
    order = np.argsort(-router_logits.float().cpu().numpy(), kind="stable")
    ranks[order] = np.arange(router_logits.numel())
    selected_ranks = ranks[list(route)]
    return {
        "sum": float(values.sum()),
        "mean": float(values.mean()),
        "minimum": float(values.min()),
        "maximum": float(values.max()),
        "rank_mean": float(selected_ranks.mean()),
        "rank_maximum": float(selected_ranks.max()),
    }


def token_metrics(logits: torch.Tensor, target: int, standard_logits: torch.Tensor | None = None) -> dict[str, float]:
    vector = logits[0, -1].float()
    log_probs = torch.log_softmax(vector, dim=-1)
    target_log_prob = log_probs[target]
    masked = vector.clone()
    masked[target] = -torch.inf
    metrics = {
        "margin": float((vector[target] - masked.max()).item()),
        "log_probability": float(target_log_prob.item()),
        "probability": float(target_log_prob.exp().item()),
    }
    if standard_logits is not None:
        standard_log_probs = torch.log_softmax(standard_logits[0, -1].float(), dim=-1)
        metrics["kl_from_standard"] = float(
            torch.sum(standard_log_probs.exp() * (standard_log_probs - log_probs)).item()
        )
    return metrics


class RouteHarness:
    def __init__(self, model: torch.nn.Module, layers: Sequence[int]):
        self.model = model
        self.layers = tuple(sorted(set(int(layer) for layer in layers)))
        self.forced_routes: dict[int, tuple[int, ...]] = {}
        self.forced_weights: dict[int, torch.Tensor] = {}
        self.captured_router_logits: dict[int, torch.Tensor] = {}
        self.captured_standard_routes: dict[int, tuple[int, ...]] = {}
        self.captured_standard_weights: dict[int, torch.Tensor] = {}
        self._original_forwards: dict[int, Any] = {}

    def __enter__(self) -> "RouteHarness":
        for layer_index in self.layers:
            block = self.model.model.layers[layer_index].mlp
            self._original_forwards[layer_index] = block.forward

            def routed_forward(this: torch.nn.Module, hidden_states: torch.Tensor, *, _idx=layer_index):
                batch_size, sequence_length, hidden_dim = hidden_states.shape
                flattened = hidden_states.reshape(-1, hidden_dim)
                router_logits, top_weights, top_indices = this.gate(flattened)
                target_row = flattened.shape[0] - 1
                self.captured_router_logits[_idx] = router_logits[target_row].detach().float().cpu()
                self.captured_standard_routes[_idx] = tuple(
                    int(value) for value in top_indices[target_row].detach().cpu().tolist()
                )
                self.captured_standard_weights[_idx] = top_weights[target_row].detach().float().cpu()
                forced = self.forced_routes.get(_idx)
                if forced is not None:
                    if len(forced) != top_indices.shape[-1]:
                        raise RuntimeError("Forced route changes active-expert cardinality")
                    forced_indices = torch.tensor(
                        forced, device=top_indices.device, dtype=top_indices.dtype
                    )
                    top_indices = top_indices.clone()
                    top_weights = top_weights.clone()
                    top_indices[target_row] = forced_indices
                    if _idx in self.forced_weights:
                        selected_weights = self.forced_weights[_idx].to(
                            device=top_weights.device, dtype=top_weights.dtype
                        )
                    else:
                        selected_weights = torch.softmax(
                            router_logits[target_row, forced_indices].float(), dim=-1
                        ).to(top_weights.dtype)
                    if selected_weights.numel() != forced_indices.numel():
                        raise RuntimeError("Forced weight cardinality mismatch")
                    top_weights[target_row] = selected_weights
                output = this.experts(flattened, top_indices, top_weights)
                return output.reshape(batch_size, sequence_length, hidden_dim)

            block.forward = types.MethodType(routed_forward, block)
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        for layer_index, original in self._original_forwards.items():
            self.model.model.layers[layer_index].mlp.forward = original


def capture_boundaries(
    model: torch.nn.Module, input_ids: torch.Tensor, boundary_layers: Sequence[int]
) -> tuple[torch.Tensor, dict[int, tuple[torch.Tensor, dict[str, Any]]]]:
    captured: dict[int, tuple[torch.Tensor, dict[str, Any]]] = {}
    handles = []
    for layer_index in boundary_layers:
        def hook(module: torch.nn.Module, args: tuple[Any, ...], kwargs: dict[str, Any], *, _idx=layer_index):
            captured[_idx] = (args[0].detach().clone(), dict(kwargs))

        handles.append(
            model.model.layers[layer_index].register_forward_pre_hook(hook, with_kwargs=True)
        )
    try:
        logits = model(input_ids=input_ids, use_cache=False, logits_to_keep=1).logits.detach()
    finally:
        for handle in handles:
            handle.remove()
    if set(captured) != set(boundary_layers):
        raise RuntimeError("Failed to capture every requested layer boundary")
    return logits, captured


def suffix_forward(
    model: torch.nn.Module,
    hidden_states: torch.Tensor,
    layer_kwargs: Mapping[str, Any],
    start_layer: int,
    capture_layers: Sequence[int],
) -> tuple[torch.Tensor, torch.Tensor, dict[int, torch.Tensor]]:
    state = hidden_states.clone()
    outputs: dict[int, torch.Tensor] = {}
    capture = set(capture_layers)
    for layer_index in range(start_layer, len(model.model.layers)):
        state = model.model.layers[layer_index](state, **layer_kwargs)
        if layer_index in capture:
            outputs[layer_index] = state[0, -1].detach().float().cpu()
    final_residual = state[0, -1].detach().float().cpu()
    normalized = model.model.norm(state)
    logits = model.lm_head(normalized[:, -1:, :]).detach()
    return logits, final_residual, outputs


def response_token_boundaries(tokenizer: Any, response_ids: Sequence[int]) -> tuple[str, list[str], list[int]]:
    decoded_prefixes = [""]
    for end in range(1, len(response_ids) + 1):
        decoded_prefixes.append(
            tokenizer.decode(
                response_ids[:end],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            )
        )
    response = decoded_prefixes[-1]
    surfaces = [decoded_prefixes[index + 1][len(decoded_prefixes[index]) :] for index in range(len(response_ids))]
    ends = [len(value) for value in decoded_prefixes[1:]]
    if "".join(surfaces) != response:
        raise RuntimeError("Token-to-character offset mapping failed to round-trip")
    return response, surfaces, ends


def trim_generated_ids(tokenizer: Any, generated_ids: Sequence[int]) -> list[int]:
    special = {value for value in (tokenizer.eos_token_id, tokenizer.pad_token_id) if value is not None}
    result = list(int(value) for value in generated_ids)
    while result and result[-1] in special:
        result.pop()
    return result


def format_prompt(tokenizer: Any, dataset: str, question: str) -> tuple[str, torch.Tensor]:
    if dataset == "gsm8k":
        instruction = (
            "Solve the arithmetic word problem carefully. Show a concise derivation and end "
            "with exactly `#### NUMBER`."
        )
    else:
        instruction = (
            "Solve the mathematics problem carefully. Show a concise derivation and end with "
            "exactly `Final answer: \\boxed{ANSWER}`."
        )
    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": question},
    ]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    ids = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).input_ids
    return prompt, ids


def generate_candidates(
    model: torch.nn.Module,
    tokenizer: Any,
    input_ids: torch.Tensor,
    dataset_code: int,
    problem_ordinal: int,
    clock: AcquisitionClock,
) -> list[list[int]]:
    candidates = []
    for sample_index in range(4):
        clock.check()
        seed = generation_seed(dataset_code, problem_ordinal, sample_index)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        generated = model.generate(
            input_ids=input_ids,
            attention_mask=torch.ones_like(input_ids),
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            top_k=0,
            max_new_tokens=768,
            pad_token_id=tokenizer.eos_token_id,
        )[0]
        candidates.append(trim_generated_ids(tokenizer, generated[input_ids.shape[1] :].tolist()))
    return candidates


def verify_candidate(
    dataset: str, response: str, row: Mapping[str, Any]
) -> tuple[bool, Any]:
    if dataset == "gsm8k":
        return verify_gsm8k(response, str(row["answer"]))
    return verify_math500(response, row)


def fragile_token(
    model: torch.nn.Module,
    tokenizer: Any,
    prompt_ids: torch.Tensor,
    response_ids: Sequence[int],
    answer_start: int,
) -> dict[str, Any] | None:
    response, surfaces, ends = response_token_boundaries(tokenizer, response_ids)
    device = prompt_ids.device
    combined = torch.cat(
        [prompt_ids, torch.tensor([response_ids], dtype=prompt_ids.dtype, device=device)], dim=1
    )
    with torch.inference_mode():
        logits = model(input_ids=combined[:, :-1], use_cache=False).logits.detach().float()
    prompt_length = int(prompt_ids.shape[1])
    probabilities = []
    for response_index, target in enumerate(response_ids):
        absolute_target = prompt_length + response_index
        predictor_position = absolute_target - 1
        probabilities.append(
            float(torch.softmax(logits[0, predictor_position], dim=-1)[int(target)].item())
        )
    selected = select_fragile_token(probabilities, surfaces, ends, answer_start)
    if selected is None:
        return None
    absolute_target = prompt_length + selected
    prefix = combined[:, :absolute_target]
    return {
        "response": response,
        "response_ids": list(response_ids),
        "selected_response_index": selected,
        "selected_token_id": int(response_ids[selected]),
        "selected_token_surface": surfaces[selected],
        "selected_probability": probabilities[selected],
        "prefix_ids": prefix,
    }


def random_projection(hidden: torch.Tensor, dimensions: int = 32) -> list[float]:
    vector = hidden.detach().float().cpu().numpy()
    norm = float(np.linalg.norm(vector))
    if norm == 0:
        raise RuntimeError("Cannot project a zero hidden state")
    rng = np.random.default_rng(BASE_SEED)
    matrix = rng.normal(size=(vector.size, dimensions)) / math.sqrt(dimensions)
    return ((vector / norm) @ matrix).astype(np.float32).tolist()


def run_interventions(
    model: torch.nn.Module,
    tokenizer: Any,
    prefix_ids: torch.Tensor,
    target: int,
    dataset: str,
    dataset_code: int,
    problem_ordinal: int,
    stable_id: str,
    selected_probability: float,
    clock: AcquisitionClock,
) -> dict[str, Any]:
    layer_indices = sorted({layer for pair in OLMOE_LAYER_PAIRS.values() for layer in pair})
    boundary_layers = sorted({pair[0] for pair in OLMOE_LAYER_PAIRS.values()})
    unwrapped_logits = model(input_ids=prefix_ids, use_cache=False, logits_to_keep=1).logits.detach()
    with RouteHarness(model, layer_indices) as harness:
        standard_logits, boundaries = capture_boundaries(model, prefix_ids, boundary_layers)
        standard_replay_error = tensor_error(unwrapped_logits, standard_logits)
        if standard_replay_error > 1e-4:
            raise RuntimeError(f"Standard replay mismatch: {standard_replay_error}")
        standard_routes = dict(harness.captured_standard_routes)
        standard_router_logits = dict(harness.captured_router_logits)
        alternatives = {
            layer: build_alternatives(
                standard_router_logits[layer].numpy(),
                standard_routes[layer],
                dataset_code,
                problem_ordinal,
                layer,
            )
            for layer in layer_indices
        }
        outside_routes = {
            layer: build_outside_pool_route(
                standard_router_logits[layer].numpy(),
                len(standard_routes[layer]),
                dataset_code,
                problem_ordinal,
                layer,
            )
            for layer in layer_indices
        }
        standard_metrics = token_metrics(standard_logits, target)
        regimes: dict[str, Any] = {}
        maximum_suffix_error = 0.0

        for regime, (layer_i, layer_j) in OLMOE_LAYER_PAIRS.items():
            clock.check()
            hidden, kwargs = boundaries[layer_i]
            harness.forced_routes.clear()
            harness.forced_weights.clear()
            replay_logits, standard_residual, standard_layer_outputs = suffix_forward(
                model, hidden, kwargs, layer_i, (layer_i, layer_j)
            )
            suffix_error = tensor_error(standard_logits, replay_logits)
            maximum_suffix_error = max(maximum_suffix_error, suffix_error)
            if suffix_error > 1e-4:
                raise RuntimeError(f"Cached/uncached mismatch {suffix_error} in {regime}")

            singles_i: dict[int, Any] = {}
            singles_j: dict[int, Any] = {}
            hidden_projection = random_projection(hidden[0, -1])
            for which, layer, destination in (
                ("i", layer_i, singles_i),
                ("j", layer_j, singles_j),
            ):
                for route_index, route in enumerate(alternatives[layer]):
                    clock.check()
                    harness.forced_routes.clear()
                    harness.forced_weights.clear()
                    harness.forced_routes[layer] = route
                    logits, residual, layer_outputs = suffix_forward(
                        model, hidden, kwargs, layer_i, (layer_i, layer_j)
                    )
                    metrics = token_metrics(logits, target, standard_logits)
                    destination[route_index] = {
                        "route": list(route),
                        "metrics": metrics,
                        "effect": metrics["margin"] - standard_metrics["margin"],
                        "final_residual_norm": float(
                            torch.linalg.vector_norm(residual - standard_residual).item()
                        ),
                        "layer_output_norm": float(
                            torch.linalg.vector_norm(
                                layer_outputs[layer] - standard_layer_outputs[layer]
                            ).item()
                        ),
                        "router": route_summary(standard_router_logits[layer], route),
                        "standard_overlap": route_overlap(route, standard_routes[layer]),
                    }

            pairs = []
            for route_i_index, route_i in enumerate(alternatives[layer_i]):
                for route_j_index, route_j in enumerate(alternatives[layer_j]):
                    clock.check()
                    harness.forced_routes.clear()
                    harness.forced_weights.clear()
                    harness.forced_routes[layer_i] = route_i
                    harness.forced_routes[layer_j] = route_j
                    logits, residual, layer_outputs = suffix_forward(
                        model, hidden, kwargs, layer_i, (layer_i, layer_j)
                    )
                    metrics = token_metrics(logits, target, standard_logits)
                    pairs.append(
                        {
                            "dataset": dataset,
                            "problem_id": stable_id,
                            "problem_ordinal": problem_ordinal,
                            "fold": problem_ordinal % 5,
                            "regime": regime,
                            "layer_i": layer_i,
                            "layer_j": layer_j,
                            "route_i_index": route_i_index,
                            "route_j_index": route_j_index,
                            "route_i": list(route_i),
                            "route_j": list(route_j),
                            "standard_route_i": list(standard_routes[layer_i]),
                            "standard_route_j": list(standard_routes[layer_j]),
                            "single_effect_i": singles_i[route_i_index]["effect"],
                            "single_effect_j": singles_j[route_j_index]["effect"],
                            "joint_effect": metrics["margin"] - standard_metrics["margin"],
                            "interaction_residual": (
                                metrics["margin"]
                                - standard_metrics["margin"]
                                - singles_i[route_i_index]["effect"]
                                - singles_j[route_j_index]["effect"]
                            ),
                            "joint_metrics": metrics,
                            "joint_final_residual_norm": float(
                                torch.linalg.vector_norm(residual - standard_residual).item()
                            ),
                            "joint_layer_output_norm_i": float(
                                torch.linalg.vector_norm(
                                    layer_outputs[layer_i] - standard_layer_outputs[layer_i]
                                ).item()
                            ),
                            "joint_layer_output_norm_j": float(
                                torch.linalg.vector_norm(
                                    layer_outputs[layer_j] - standard_layer_outputs[layer_j]
                                ).item()
                            ),
                            "router_score_sum_i": singles_i[route_i_index]["router"]["sum"],
                            "router_score_sum_j": singles_j[route_j_index]["router"]["sum"],
                            "router_summary_i": singles_i[route_i_index]["router"],
                            "router_summary_j": singles_j[route_j_index]["router"],
                            "standard_overlap_i": singles_i[route_i_index]["standard_overlap"],
                            "standard_overlap_j": singles_j[route_j_index]["standard_overlap"],
                            "pair_overlap": route_overlap(route_i, route_j),
                            "single_residual_norm_i": singles_i[route_i_index]["final_residual_norm"],
                            "single_residual_norm_j": singles_j[route_j_index]["final_residual_norm"],
                            "normalized_layer_separation": (layer_j - layer_i) / 15.0,
                            "hidden_projection": hidden_projection,
                            "selected_standard_probability": selected_probability,
                        }
                    )

            controls = []
            for route_index in range(6):
                route_i = alternatives[layer_i][route_index]
                route_j = alternatives[layer_j][route_index]
                harness.forced_routes = {layer_i: route_i, layer_j: route_j}
                harness.forced_weights = {
                    layer_i: torch.softmax(standard_router_logits[layer_i][list(route_i)], dim=-1),
                    layer_j: torch.softmax(standard_router_logits[layer_j][list(route_j)], dim=-1),
                }
                logits, _, _ = suffix_forward(model, hidden, kwargs, layer_i, (layer_i, layer_j))
                controls.append(
                    {
                        "type": "fixed_standard_state_weights_diagonal",
                        "route_index": route_index,
                        "joint_effect": token_metrics(logits, target)["margin"] - standard_metrics["margin"],
                    }
                )

                harness.forced_routes = {layer_i: route_i, layer_j: route_i}
                harness.forced_weights.clear()
                logits, _, _ = suffix_forward(model, hidden, kwargs, layer_i, (layer_i, layer_j))
                controls.append(
                    {
                        "type": "same_expert_identities",
                        "route_index": route_index,
                        "joint_effect": token_metrics(logits, target)["margin"] - standard_metrics["margin"],
                    }
                )

            outside_single_effects = {}
            for label, layer in (("i", layer_i), ("j", layer_j)):
                harness.forced_routes = {layer: outside_routes[layer]}
                harness.forced_weights.clear()
                logits, _, _ = suffix_forward(model, hidden, kwargs, layer_i, (layer_i, layer_j))
                outside_single_effects[label] = token_metrics(logits, target)["margin"] - standard_metrics["margin"]
            harness.forced_routes = {
                layer_i: outside_routes[layer_i],
                layer_j: outside_routes[layer_j],
            }
            harness.forced_weights.clear()
            logits, _, _ = suffix_forward(model, hidden, kwargs, layer_i, (layer_i, layer_j))
            controls.append(
                {
                    "type": "outside_top16",
                    "route_i": list(outside_routes[layer_i]),
                    "route_j": list(outside_routes[layer_j]),
                    "single_effect_i": outside_single_effects["i"],
                    "single_effect_j": outside_single_effects["j"],
                    "joint_effect": token_metrics(logits, target)["margin"] - standard_metrics["margin"],
                }
            )
            regimes[regime] = {
                "layer_i": layer_i,
                "layer_j": layer_j,
                "cached_uncached_max_abs_error": suffix_error,
                "standard_metrics": standard_metrics,
                "singles_i": singles_i,
                "singles_j": singles_j,
                "pairs": pairs,
                "controls": controls,
            }

        harness.forced_routes.clear()
        harness.forced_weights.clear()
        repeated_logits, _ = capture_boundaries(model, prefix_ids, boundary_layers)
        deterministic_error = tensor_error(standard_logits, repeated_logits)
        if deterministic_error > 1e-6:
            raise RuntimeError(f"Deterministic rerun mismatch: {deterministic_error}")
    return {
        "standard_metrics": standard_metrics,
        "standard_replay_error": standard_replay_error,
        "maximum_cached_uncached_error": maximum_suffix_error,
        "deterministic_rerun_error": deterministic_error,
        "standard_routes": {str(key): list(value) for key, value in standard_routes.items()},
        "alternatives": {
            str(key): [list(route) for route in value] for key, value in alternatives.items()
        },
        "regimes": regimes,
    }


def ensure_new_output(path: Path, allow_existing_empty: bool) -> None:
    if path.exists():
        if allow_existing_empty and path.is_dir() and not any(path.iterdir()):
            return
        raise FileExistsError(f"Refusing to overwrite existing output: {path}")
    path.mkdir(parents=True)


def main() -> int:
    args = parse_args()
    ensure_new_output(args.output_dir, args.allow_existing_empty_output)
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    args.dataset_cache_dir.mkdir(parents=True, exist_ok=True)
    frozen = load_frozen_config(args.frozen_config)
    clock = AcquisitionClock(time.perf_counter(), args.max_gpu_hours * 3600.0)
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("HF_DATASETS_CACHE", str(args.dataset_cache_dir))
    random.seed(BASE_SEED)
    np.random.seed(BASE_SEED)
    torch.manual_seed(BASE_SEED)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("Stage D acquisition requires one CUDA GPU")

    resolved = {
        "status": "ACQUISITION_RUNNING",
        "scientific_output_sealed": True,
        "protocol_sha256": sha256_file(args.frozen_config),
        "thresholds_sha256": sha256_file(args.thresholds),
        "model": args.model,
        "environment": {
            "hostname": platform.node(),
            "python": platform.python_version(),
            "torch": torch.__version__,
            "transformers": __import__("transformers").__version__,
            "datasets": __import__("datasets").__version__,
            "gpu": torch.cuda.get_device_name(device),
        },
        "datasets": {},
    }
    json_dump_atomic(args.output_dir / "config_resolved.initial.json", resolved)

    tokenizer = AutoTokenizer.from_pretrained(args.model, cache_dir=args.cache_dir)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        cache_dir=args.cache_dir,
        dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).to(device)
    model.eval()
    torch.set_grad_enabled(False)
    if model.config.model_type != "olmoe":
        raise RuntimeError(f"Expected OLMoE, got {model.config.model_type}")
    if int(model.config.num_experts) != 64 or int(model.config.num_experts_per_tok) != 8:
        raise RuntimeError("Unexpected OLMoE expert configuration")
    if resolve_layer_pairs(len(model.model.layers)) != OLMOE_LAYER_PAIRS:
        raise RuntimeError("Resolved layer pairs differ from frozen pairs")

    retained_counts: dict[str, int] = {}
    examined_counts: dict[str, int] = {}
    try:
        for dataset, specification in DATASETS.items():
            raw = load_dataset(
                specification["hf_name"],
                specification["subset"],
                split=specification["split"],
                cache_dir=args.dataset_cache_dir,
            )
            rows = stable_sort_rows(dataset, raw)
            resolved["datasets"][dataset] = {
                "fingerprint": raw._fingerprint,
                "row_count": len(raw),
                "stable_id_sha256": sha256_bytes(
                    "\n".join(row["_stable_id"] for row in rows).encode("utf-8")
                ),
            }
            target = args.preflight_problems_per_dataset if args.preflight else args.target_per_dataset
            if args.max_problems_per_dataset > 0:
                rows = rows[: args.max_problems_per_dataset]
            retained = 0
            examined = 0
            for row in rows:
                if retained >= target:
                    break
                clock.check(args.analysis_reserve_seconds if not args.preflight else 0)
                examined += 1
                question = str(row[specification["question_field"]])
                _, prompt_ids_cpu = format_prompt(tokenizer, dataset, question)
                prompt_ids = prompt_ids_cpu.to(device)
                candidate_ids = generate_candidates(
                    model,
                    tokenizer,
                    prompt_ids,
                    specification["dataset_code"],
                    row["_stable_ordinal"],
                    clock,
                )
                chosen = None
                for sample_index, response_ids in enumerate(candidate_ids):
                    response, _, _ = response_token_boundaries(tokenizer, response_ids)
                    correct, extracted = verify_candidate(dataset, response, row)
                    if correct and extracted is not None:
                        chosen = (sample_index, response_ids, response, extracted)
                        break
                if chosen is None:
                    print(f"PROGRESS dataset={dataset} examined={examined} retained={retained}", flush=True)
                    continue
                sample_index, response_ids, response, extracted = chosen
                selected = fragile_token(
                    model,
                    tokenizer,
                    prompt_ids,
                    response_ids,
                    extracted.start,
                )
                if selected is None:
                    print(f"PROGRESS dataset={dataset} examined={examined} retained={retained}", flush=True)
                    continue
                interventions = run_interventions(
                    model,
                    tokenizer,
                    selected.pop("prefix_ids"),
                    selected["selected_token_id"],
                    dataset,
                    specification["dataset_code"],
                    row["_stable_ordinal"],
                    row["_stable_id"],
                    selected["selected_probability"],
                    clock,
                )
                shard = {
                    "dataset": dataset,
                    "problem_id": row["_stable_id"],
                    "problem_ordinal": row["_stable_ordinal"],
                    "fold": row["_fold"],
                    "sample_index": sample_index,
                    "prompt_token_count": int(prompt_ids.shape[1]),
                    "response_token_count": len(response_ids),
                    "answer_extraction_method": extracted.method,
                    "answer_span_start": extracted.start,
                    "selected_token": selected,
                    "interventions": interventions,
                }
                shard_path = (
                    args.output_dir
                    / "shards"
                    / dataset
                    / shard_filename(row["_stable_id"])
                )
                json_dump_atomic(shard_path, shard, gzip_output=True)
                checksum_path = shard_path.with_suffix(shard_path.suffix + ".sha256")
                json_dump_atomic(checksum_path, {"sha256": sha256_file(shard_path)})
                retained += 1
                print(
                    f"PROGRESS dataset={dataset} examined={examined} retained={retained} "
                    f"elapsed_seconds={clock.elapsed():.1f}",
                    flush=True,
                )
            retained_counts[dataset] = retained
            examined_counts[dataset] = examined
            minimum = args.preflight_problems_per_dataset if args.preflight else args.minimum_per_dataset
            if retained < minimum:
                raise HardStop(
                    f"Dataset {dataset} retained {retained}, below required minimum {minimum}"
                )
    except HardStop as error:
        terminal = {
            "status": "NO_GO_NO_INTERACTION_LAW" if not args.preflight else "NO_GO_STAGE_D_PREFLIGHT",
            "reason": str(error),
            "retained": retained_counts,
            "examined": examined_counts,
            "elapsed_seconds": clock.elapsed(),
            "scientific_output_sealed": True,
        }
        json_dump_atomic(args.output_dir / "ACQUISITION_TERMINAL.json", terminal)
        print(json.dumps({"status": terminal["status"], "reason": terminal["reason"]}), flush=True)
        return 2

    resolved["status"] = "PREFLIGHT_ACQUISITION_COMPLETE" if args.preflight else "DISCOVERY_ACQUISITION_COMPLETE"
    resolved["retained"] = retained_counts
    resolved["examined"] = examined_counts
    resolved["elapsed_seconds"] = clock.elapsed()
    json_dump_atomic(args.output_dir / "config_resolved.json", resolved)
    print(
        json.dumps(
            {
                "status": resolved["status"],
                "retained": retained_counts,
                "examined": examined_counts,
                "elapsed_seconds": clock.elapsed(),
            }
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
