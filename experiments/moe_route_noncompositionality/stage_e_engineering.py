#!/usr/bin/env python3
"""Stage E engineering gate for frozen OLMoE route interventions.

This script is deliberately not a scientific experiment.  It verifies that
equal-cardinality expert-route interventions can be replayed deterministically,
that a layer-boundary suffix cache reproduces full forward passes, and that the
small intervention grid fits the preregistered engineering budget.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import platform
import random
import time
import types
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_ID = "allenai/OLMoE-1B-7B-0924-Instruct"
PROMPTS_AND_TARGETS = (
    ("Question: What is 2 + 2? Answer:", " 4"),
    ("Question: What is 7 - 3? Answer:", " 4"),
    ("Question: What is 3 times 5? Answer:", " 15"),
    ("Question: What is 12 divided by 4? Answer:", " 3"),
    ("Question: What is the next integer after 19? Answer:", " 20"),
    ("Question: How many sides does a triangle have? Answer:", " 3"),
    ("Question: If a dozen eggs are split equally into two groups, each group has", " 6"),
    ("Question: What is 10 percent of 50? Answer:", " 5"),
)


@dataclass
class ConditionResult:
    trajectory: int
    condition: str
    route_i: str
    route_j: str
    margin: float
    delta_from_standard: float
    full_suffix_max_abs_error: float
    deterministic_max_abs_error: float
    elapsed_seconds: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--model", default=MODEL_ID)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--seed", type=int, default=20260828)
    parser.add_argument("--max-trajectories", type=int, default=8)
    parser.add_argument("--alternatives", type=int, default=2)
    parser.add_argument("--pool-size", type=int, default=16)
    parser.add_argument("--max-gpu-hours", type=float, default=1.0)
    parser.add_argument(
        "--max-gpu-memory-gib",
        type=int,
        default=None,
        help="Engineering-only CPU placement cap; timings are invalid when set.",
    )
    parser.add_argument("--replay-tolerance", type=float, default=1e-4)
    parser.add_argument("--determinism-tolerance", type=float, default=1e-6)
    return parser.parse_args()


def upward_round(value: float) -> int:
    return int(math.floor(value + 0.5))


def resolve_layers(num_layers: int) -> tuple[int, int]:
    if num_layers < 2:
        raise ValueError(f"Need at least two MoE layers, found {num_layers}")
    first = upward_round(0.20 * (num_layers - 1))
    second = upward_round(0.30 * (num_layers - 1))
    if first == second:
        second = min(first + 1, num_layers - 1)
    return first, second


def tensor_max_abs(a: torch.Tensor, b: torch.Tensor) -> float:
    return float((a.float() - b.float()).abs().max().item())


def correct_token_margin(logits: torch.Tensor, target: int) -> float:
    vector = logits[0, -1].float()
    target_value = vector[target]
    masked = vector.clone()
    masked[target] = -torch.inf
    return float((target_value - masked.max()).item())


def build_alternatives(
    router_logits: torch.Tensor,
    standard_route: tuple[int, ...],
    pool_size: int,
    count: int,
    seed: int,
) -> list[tuple[int, ...]]:
    if router_logits.ndim != 1:
        raise ValueError("Expected one-dimensional target-token router logits")
    effective_pool = min(pool_size, router_logits.numel())
    pool = torch.topk(router_logits.float(), effective_pool).indices.cpu().numpy()
    pool_logits = router_logits.float().cpu().numpy()[pool]
    k = len(standard_route)
    if effective_pool < k:
        raise ValueError("Candidate pool is smaller than route cardinality")
    alternatives: list[tuple[int, ...]] = []
    standard_set = frozenset(standard_route)
    attempt = 0
    while len(alternatives) < count and attempt < 100:
        rng = np.random.default_rng(seed + attempt)
        scores = pool_logits + rng.gumbel(size=effective_pool)
        chosen = tuple(sorted(int(x) for x in pool[np.argpartition(scores, -k)[-k:]]))
        if frozenset(chosen) != standard_set and chosen not in alternatives:
            alternatives.append(chosen)
        attempt += 1
    if len(alternatives) != count:
        raise RuntimeError(f"Only produced {len(alternatives)} distinct alternatives")
    return alternatives


class RouteHarness:
    def __init__(self, model: torch.nn.Module, layer_i: int, layer_j: int):
        self.model = model
        self.layer_i = layer_i
        self.layer_j = layer_j
        self.layers = (layer_i, layer_j)
        self.forced_routes: dict[int, tuple[int, ...]] = {}
        self.captured_router_logits: dict[int, torch.Tensor] = {}
        self.captured_standard_routes: dict[int, tuple[int, ...]] = {}
        self._original_forwards: dict[int, Any] = {}

    def __enter__(self) -> "RouteHarness":
        for layer_idx in self.layers:
            block = self.model.model.layers[layer_idx].mlp
            self._original_forwards[layer_idx] = block.forward

            def routed_forward(this: torch.nn.Module, hidden_states: torch.Tensor, *, _idx=layer_idx):
                batch_size, sequence_length, hidden_dim = hidden_states.shape
                flat = hidden_states.reshape(-1, hidden_dim)
                router_logits, top_weights, top_indices = this.gate(flat)
                target_row = flat.shape[0] - 1
                self.captured_router_logits[_idx] = router_logits[target_row].detach().float().cpu()
                self.captured_standard_routes[_idx] = tuple(
                    int(x) for x in top_indices[target_row].detach().cpu().tolist()
                )
                forced = self.forced_routes.get(_idx)
                if forced is not None:
                    if len(forced) != top_indices.shape[-1]:
                        raise RuntimeError("Forced route changes active-expert cardinality")
                    forced_tensor = torch.tensor(forced, device=top_indices.device, dtype=top_indices.dtype)
                    top_indices = top_indices.clone()
                    top_weights = top_weights.clone()
                    top_indices[target_row] = forced_tensor
                    selected_logits = router_logits[target_row, forced_tensor].float()
                    selected_weights = torch.softmax(selected_logits, dim=-1).to(top_weights.dtype)
                    top_weights[target_row] = selected_weights
                result = this.experts(flat, top_indices, top_weights)
                return result.reshape(batch_size, sequence_length, hidden_dim)

            block.forward = types.MethodType(routed_forward, block)
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        for layer_idx, original in self._original_forwards.items():
            self.model.model.layers[layer_idx].mlp.forward = original


def capture_layer_input(model: torch.nn.Module, input_ids: torch.Tensor, layer_idx: int):
    captured: dict[str, Any] = {}

    def pre_hook(module: torch.nn.Module, args: tuple[Any, ...], kwargs: dict[str, Any]):
        captured["hidden_states"] = args[0].detach().clone()
        captured["kwargs"] = dict(kwargs)

    handle = model.model.layers[layer_idx].register_forward_pre_hook(pre_hook, with_kwargs=True)
    try:
        output = model(input_ids=input_ids, use_cache=False, logits_to_keep=1).logits.detach()
    finally:
        handle.remove()
    if not captured:
        raise RuntimeError("Failed to capture layer-boundary state")
    return output, captured["hidden_states"], captured["kwargs"]


def suffix_logits(
    model: torch.nn.Module,
    hidden_states: torch.Tensor,
    layer_kwargs: dict[str, Any],
    start_layer: int,
) -> torch.Tensor:
    state = hidden_states.clone()
    for layer in model.model.layers[start_layer:]:
        state = layer(state, **layer_kwargs)
    state = model.model.norm(state)
    return model.lm_head(state[:, -1:, :]).detach()


def encode_trajectory(tokenizer: Any, prompt: str, target_text: str, device: torch.device):
    prompt_ids = tokenizer(prompt, add_special_tokens=True, return_tensors="pt").input_ids[0]
    combined_ids = tokenizer(prompt + target_text, add_special_tokens=True, return_tensors="pt").input_ids[0]
    if combined_ids.numel() <= prompt_ids.numel():
        raise RuntimeError("Target text did not add a token")
    prefix = combined_ids[:-1].unsqueeze(0).to(device)
    target = int(combined_ids[-1].item())
    return prefix, target


def condition_name(route_i: str, route_j: str) -> str:
    if route_i == "standard" and route_j == "standard":
        return "standard"
    if route_j == "standard":
        return f"single_i_{route_i}"
    if route_i == "standard":
        return f"single_j_{route_j}"
    return f"joint_{route_i}_{route_j}"


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("Stage E requires one CUDA GPU")

    wall_start = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(args.model, cache_dir=args.cache_dir)
    load_kwargs: dict[str, Any] = {
        "cache_dir": args.cache_dir,
        "dtype": torch.bfloat16,
        "low_cpu_mem_usage": True,
        "attn_implementation": "eager",
    }
    if args.max_gpu_memory_gib is not None:
        load_kwargs["device_map"] = "auto"
        load_kwargs["max_memory"] = {
            device.index or 0: f"{args.max_gpu_memory_gib}GiB",
            "cpu": "256GiB",
        }
    model = AutoModelForCausalLM.from_pretrained(args.model, **load_kwargs)
    if args.max_gpu_memory_gib is None:
        model = model.to(device)
    model.eval()
    torch.set_grad_enabled(False)
    input_device = model.model.embed_tokens.weight.device

    num_layers = len(model.model.layers)
    layer_i, layer_j = resolve_layers(num_layers)
    config_checks = {
        "model_type": model.config.model_type,
        "num_hidden_layers": num_layers,
        "num_experts": int(model.config.num_experts),
        "num_experts_per_tok": int(model.config.num_experts_per_tok),
        "layer_i": layer_i,
        "layer_j": layer_j,
    }
    if model.config.model_type != "olmoe":
        raise RuntimeError(f"Expected model_type=olmoe, got {model.config.model_type}")
    if model.config.num_experts_per_tok <= 0 or model.config.num_experts < args.pool_size:
        raise RuntimeError(f"Unexpected expert configuration: {config_checks}")

    rows: list[ConditionResult] = []
    diagnostics: list[dict[str, Any]] = []
    maximum_replay_error = 0.0
    maximum_suffix_error = 0.0
    maximum_determinism_error = 0.0

    for trajectory_idx, (prompt, target_text) in enumerate(PROMPTS_AND_TARGETS[: args.max_trajectories]):
        input_ids, target = encode_trajectory(tokenizer, prompt, target_text, input_device)
        unmodified_logits, _, _ = capture_layer_input(model, input_ids, layer_i)

        with RouteHarness(model, layer_i, layer_j) as harness:
            replay_logits, cached_hidden, cached_kwargs = capture_layer_input(model, input_ids, layer_i)
            replay_error = tensor_max_abs(unmodified_logits, replay_logits)
            maximum_replay_error = max(maximum_replay_error, replay_error)

            standard_routes = dict(harness.captured_standard_routes)
            standard_router_logits = dict(harness.captured_router_logits)
            alternatives: dict[int, list[tuple[int, ...]]] = {}
            for layer_idx in (layer_i, layer_j):
                alternatives[layer_idx] = build_alternatives(
                    standard_router_logits[layer_idx],
                    standard_routes[layer_idx],
                    args.pool_size,
                    args.alternatives,
                    args.seed + trajectory_idx * 1000 + layer_idx * 100,
                )

            standard_margin = correct_token_margin(replay_logits, target)
            route_options_i: list[tuple[str, tuple[int, ...] | None]] = [("standard", None)] + [
                (f"a{k}", route) for k, route in enumerate(alternatives[layer_i])
            ]
            route_options_j: list[tuple[str, tuple[int, ...] | None]] = [("standard", None)] + [
                (f"a{k}", route) for k, route in enumerate(alternatives[layer_j])
            ]

            for name_i, route_i in route_options_i:
                for name_j, route_j in route_options_j:
                    harness.forced_routes.clear()
                    if route_i is not None:
                        harness.forced_routes[layer_i] = route_i
                    if route_j is not None:
                        harness.forced_routes[layer_j] = route_j
                    started = time.perf_counter()
                    full_logits = model(input_ids=input_ids, use_cache=False, logits_to_keep=1).logits.detach()
                    cached_logits = suffix_logits(model, cached_hidden, cached_kwargs, layer_i)
                    repeated_logits = model(input_ids=input_ids, use_cache=False, logits_to_keep=1).logits.detach()
                    elapsed = time.perf_counter() - started
                    suffix_error = tensor_max_abs(full_logits, cached_logits)
                    determinism_error = tensor_max_abs(full_logits, repeated_logits)
                    maximum_suffix_error = max(maximum_suffix_error, suffix_error)
                    maximum_determinism_error = max(maximum_determinism_error, determinism_error)
                    margin = correct_token_margin(full_logits, target)
                    rows.append(
                        ConditionResult(
                            trajectory=trajectory_idx,
                            condition=condition_name(name_i, name_j),
                            route_i=name_i,
                            route_j=name_j,
                            margin=margin,
                            delta_from_standard=margin - standard_margin,
                            full_suffix_max_abs_error=suffix_error,
                            deterministic_max_abs_error=determinism_error,
                            elapsed_seconds=elapsed,
                        )
                    )

            diagnostics.append(
                {
                    "trajectory": trajectory_idx,
                    "prompt": prompt,
                    "target_text": target_text,
                    "target_token_id": target,
                    "target_token": tokenizer.decode([target]),
                    "input_tokens": int(input_ids.shape[1]),
                    "standard_replay_max_abs_error": replay_error,
                    "standard_routes": {str(k): list(v) for k, v in standard_routes.items()},
                    "alternatives": {
                        str(k): [list(route) for route in routes] for k, routes in alternatives.items()
                    },
                }
            )

        if (time.perf_counter() - wall_start) / 3600.0 > args.max_gpu_hours:
            raise TimeoutError("Stage E exceeded the one-GPU-hour hard cap")

    elapsed_total = time.perf_counter() - wall_start
    mean_condition_seconds = float(np.mean([row.elapsed_seconds for row in rows]))
    # 128 trajectories/model total, four layer pairs, and 49 conditions.  The
    # multiplier of 2.4 is a conservative active-parameter proxy for DeepSeek.
    discovery_hours_projection = mean_condition_seconds * 128 * 4 * 49 / 3600.0
    confirmation_hours_projection = discovery_hours_projection * 2.4
    intervention_hours_projection = discovery_hours_projection + confirmation_hours_projection

    cardinality_ok = all(
        len(route) == model.config.num_experts_per_tok
        for item in diagnostics
        for routes in item["alternatives"].values()
        for route in routes
    )
    pass_replay = maximum_replay_error <= args.replay_tolerance
    pass_suffix = maximum_suffix_error <= args.replay_tolerance
    pass_determinism = maximum_determinism_error <= args.determinism_tolerance
    pass_budget = elapsed_total / 3600.0 <= args.max_gpu_hours
    # Generation is intentionally not estimated from hand-authored trajectories.
    # Therefore Stage E cannot pass its full-compute projection gate yet.
    summary = {
        "status": "ENGINEERING_INCOMPLETE_COMPUTE_PROJECTION",
        "scientific_interpretation_allowed": False,
        "model": args.model,
        "environment": {
            "hostname": platform.node(),
            "python": platform.python_version(),
            "torch": torch.__version__,
            "transformers": __import__("transformers").__version__,
            "gpu": torch.cuda.get_device_name(device),
            "max_gpu_memory_gib": args.max_gpu_memory_gib,
            "device_map": getattr(model, "hf_device_map", None),
        },
        "config_checks": config_checks,
        "counts": {"trajectories": len(diagnostics), "conditions": len(rows)},
        "errors": {
            "standard_replay_max_abs": maximum_replay_error,
            "full_suffix_max_abs": maximum_suffix_error,
            "deterministic_rerun_max_abs": maximum_determinism_error,
        },
        "timing": {
            "wall_seconds_including_model_load": elapsed_total,
            "gpu_hours_upper_bound": elapsed_total / 3600.0,
            "mean_three_pass_condition_seconds": mean_condition_seconds,
            "projected_intervention_hours_discovery": discovery_hours_projection,
            "projected_intervention_hours_confirmation_proxy": confirmation_hours_projection,
            "projected_intervention_hours_total": intervention_hours_projection,
            "trajectory_generation_hours": None,
        },
        "gates": {
            "route_cardinality": cardinality_ok,
            "standard_replay": pass_replay,
            "cached_uncached": pass_suffix,
            "deterministic_rerun": pass_determinism,
            "engineering_gpu_hour": pass_budget,
            "full_diagnostic_compute_projection": False,
            "exclusive_gpu_timing": args.max_gpu_memory_gib is None,
        },
        "note": "The route machinery may pass, but a generated-trajectory throughput pilot is still required before Stage E can be marked PASS.",
    }

    with (args.output_dir / "conditions.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    (args.output_dir / "diagnostics.json").write_text(
        json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (args.output_dir / "stage_e_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if all((cardinality_ok, pass_replay, pass_suffix, pass_determinism, pass_budget)) else 2


if __name__ == "__main__":
    raise SystemExit(main())
