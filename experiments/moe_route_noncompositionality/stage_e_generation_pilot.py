#!/usr/bin/env python3
"""Outcome-blind Stage E generation-throughput pilot.

This pilot closes only the compute-projection item left open by
``stage_e_engineering.py``.  It does not score answers or inspect route
effects, and therefore has no scientific interpretation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import time
from pathlib import Path
from typing import Any

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_ID = "allenai/OLMoE-1B-7B-0924-Instruct"
DATASETS = (
    ("gsm8k", "openai/gsm8k", "main", "question"),
    ("math500", "HuggingFaceH4/MATH-500", None, "problem"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--engineering-summary", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--dataset-cache-dir", type=Path, required=True)
    parser.add_argument("--model", default=MODEL_ID)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--seed", type=int, default=20260828)
    parser.add_argument("--problems-per-dataset", type=int, default=2)
    parser.add_argument("--samples-per-problem", type=int, default=4)
    parser.add_argument("--max-new-tokens", type=int, default=768)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-p", type=float, default=0.95)
    parser.add_argument("--top-k", type=int, default=0)
    parser.add_argument("--target-trajectories-per-dataset", type=int, default=64)
    parser.add_argument("--confirmation-runtime-multiplier", type=float, default=2.4)
    parser.add_argument("--projection-guardband", type=float, default=1.25)
    parser.add_argument("--full-compute-hours-max", type=float, default=12.0)
    parser.add_argument("--cumulative-stage-e-hours-max", type=float, default=1.0)
    return parser.parse_args()


def stable_rows(
    dataset_name: str,
    subset: str | None,
    field: str,
    cache_dir: Path,
    count: int,
) -> list[dict[str, Any]]:
    kwargs: dict[str, Any] = {
        "path": dataset_name,
        "split": "test",
        "cache_dir": str(cache_dir),
    }
    if subset is not None:
        kwargs["name"] = subset
    dataset = load_dataset(**kwargs)
    rows = [dict(row) for row in dataset]
    if "unique_id" in dataset.column_names:
        rows.sort(key=lambda row: str(row["unique_id"]))
    else:
        rows.sort(key=lambda row: hashlib.sha256(str(row[field]).encode()).hexdigest())
    if len(rows) < count:
        raise RuntimeError(f"Dataset {dataset_name} has only {len(rows)} rows")
    return rows[:count]


def format_prompt(tokenizer: Any, question: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Solve the mathematics problem step by step. End with a concise "
                "final answer and do not use external tools."
            ),
        },
        {"role": "user", "content": question},
    ]
    if getattr(tokenizer, "chat_template", None):
        return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    return f"Question: {question}\nAnswer:"


def generated_token_count(sequence: torch.Tensor, prompt_tokens: int, eos_token_id: int) -> int:
    tail = sequence[prompt_tokens:]
    eos_positions = (tail == eos_token_id).nonzero(as_tuple=False)
    if eos_positions.numel() == 0:
        return int(tail.shape[0])
    return int(eos_positions[0, 0].item()) + 1


def main() -> int:
    args = parse_args()
    if args.problems_per_dataset <= 0 or args.samples_per_problem != 4:
        raise ValueError("The frozen pilot requires positive problems and exactly four samples")
    if (
        args.max_new_tokens != 768
        or args.temperature != 0.7
        or args.top_p != 0.95
        or args.top_k != 0
    ):
        raise ValueError("Generation settings differ from THRESHOLDS.yaml")
    args.output_dir.mkdir(parents=True, exist_ok=False)
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    args.dataset_cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("HF_DATASETS_CACHE", str(args.dataset_cache_dir))
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("Generation pilot requires one CUDA GPU")

    engineering = json.loads(args.engineering_summary.read_text(encoding="utf-8"))
    required_engineering_gates = (
        "route_cardinality",
        "standard_replay",
        "cached_uncached",
        "deterministic_rerun",
        "engineering_gpu_hour",
        "exclusive_gpu_timing",
    )
    if not all(engineering["gates"].get(gate) is True for gate in required_engineering_gates):
        raise RuntimeError("The intervention engineering prerequisites did not all pass")
    if engineering["gates"].get("full_diagnostic_compute_projection") is not False:
        raise RuntimeError("Expected the generation projection to be the sole open gate")

    wall_start = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(args.model, cache_dir=args.cache_dir)
    load_start = time.perf_counter()
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        cache_dir=args.cache_dir,
        dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).to(device)
    model.eval()
    torch.set_grad_enabled(False)
    torch.cuda.synchronize(device)
    model_load_seconds = time.perf_counter() - load_start
    if model.config.model_type != "olmoe" or int(model.config.num_experts_per_tok) != 8:
        raise RuntimeError("Unexpected OLMoE configuration")

    records: list[dict[str, Any]] = []
    seconds_per_generated_token: list[float] = []
    for dataset_key, dataset_name, subset, field in DATASETS:
        rows = stable_rows(
            dataset_name,
            subset,
            field,
            args.dataset_cache_dir,
            args.problems_per_dataset,
        )
        for problem_index, row in enumerate(rows):
            question = str(row[field])
            stable_id = str(row.get("unique_id") or hashlib.sha256(question.encode()).hexdigest())
            prompt = format_prompt(tokenizer, question)
            encoded = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(device)
            torch.manual_seed(args.seed + len(records) * 1000)
            torch.cuda.manual_seed_all(args.seed + len(records) * 1000)
            torch.cuda.synchronize(device)
            started = time.perf_counter()
            generated = model.generate(
                **encoded,
                do_sample=True,
                num_return_sequences=args.samples_per_problem,
                temperature=args.temperature,
                top_p=args.top_p,
                top_k=args.top_k,
                max_new_tokens=args.max_new_tokens,
                pad_token_id=tokenizer.eos_token_id,
            )
            torch.cuda.synchronize(device)
            elapsed = time.perf_counter() - started
            prompt_tokens = int(encoded.input_ids.shape[1])
            new_token_counts = [
                generated_token_count(sequence, prompt_tokens, int(tokenizer.eos_token_id))
                for sequence in generated
            ]
            total_new_tokens = int(sum(new_token_counts))
            if total_new_tokens <= 0:
                raise RuntimeError("Generation produced no new tokens")
            seconds_per_generated_token.append(elapsed / total_new_tokens)
            records.append(
                {
                    "dataset": dataset_key,
                    "stable_id": stable_id,
                    "problem_index": problem_index,
                    "prompt_tokens": prompt_tokens,
                    "new_token_counts": new_token_counts,
                    "elapsed_seconds": elapsed,
                    "seconds_per_generated_token": elapsed / total_new_tokens,
                    "generations": [
                        tokenizer.decode(sequence[prompt_tokens:], skip_special_tokens=True)
                        for sequence in generated
                    ],
                }
            )

    pilot_wall_seconds = time.perf_counter() - wall_start
    conservative_seconds_per_token = max(seconds_per_generated_token)
    problems_per_model = args.target_trajectories_per_dataset * len(DATASETS)
    generated_tokens_per_model = (
        problems_per_model * args.samples_per_problem * args.max_new_tokens
    )
    discovery_generation_hours = (
        conservative_seconds_per_token * generated_tokens_per_model / 3600.0
    )
    confirmation_generation_hours = (
        discovery_generation_hours * args.confirmation_runtime_multiplier
    )
    model_load_hours_total = (
        model_load_seconds * (1.0 + args.confirmation_runtime_multiplier) / 3600.0
    )
    intervention_hours = float(
        engineering["timing"]["projected_intervention_hours_total"]
    )
    raw_full_hours = (
        intervention_hours
        + discovery_generation_hours
        + confirmation_generation_hours
        + model_load_hours_total
    )
    guarded_full_hours = raw_full_hours * args.projection_guardband
    cumulative_stage_e_hours = (
        float(engineering["timing"]["gpu_hours_upper_bound"])
        + pilot_wall_seconds / 3600.0
    )
    compute_projection_ok = guarded_full_hours <= args.full_compute_hours_max
    stage_e_budget_ok = cumulative_stage_e_hours <= args.cumulative_stage_e_hours_max
    status = (
        "ENGINEERING_PASS"
        if compute_projection_ok and stage_e_budget_ok
        else "NO_GO_ENGINEERING"
    )
    summary = {
        "status": status,
        "scientific_interpretation_allowed": False,
        "model": args.model,
        "environment": {
            "hostname": platform.node(),
            "python": platform.python_version(),
            "torch": torch.__version__,
            "transformers": __import__("transformers").__version__,
            "gpu": torch.cuda.get_device_name(device),
        },
        "frozen_generation_settings": {
            "samples_per_problem": args.samples_per_problem,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "top_k": args.top_k,
            "max_new_tokens": args.max_new_tokens,
            "seed": args.seed,
        },
        "counts": {
            "datasets": len(DATASETS),
            "problems_per_dataset": args.problems_per_dataset,
            "pilot_problems": len(records),
            "pilot_generations": len(records) * args.samples_per_problem,
            "projected_target_problems_per_model": problems_per_model,
            "projected_generated_tokens_per_model": generated_tokens_per_model,
        },
        "timing": {
            "model_load_seconds": model_load_seconds,
            "pilot_wall_seconds": pilot_wall_seconds,
            "pilot_gpu_hours_upper_bound": pilot_wall_seconds / 3600.0,
            "maximum_seconds_per_generated_token": conservative_seconds_per_token,
            "projected_intervention_hours_total": intervention_hours,
            "projected_generation_hours_discovery": discovery_generation_hours,
            "projected_generation_hours_confirmation_proxy": confirmation_generation_hours,
            "projected_model_load_hours_total": model_load_hours_total,
            "projected_full_hours_raw": raw_full_hours,
            "projection_guardband": args.projection_guardband,
            "projected_full_hours_guarded": guarded_full_hours,
            "cumulative_stage_e_gpu_hours_upper_bound": cumulative_stage_e_hours,
        },
        "gates": {
            "generation_settings_frozen": True,
            "representative_dataset_prompts": True,
            "exclusive_gpu_timing": True,
            "engineering_gpu_hour": stage_e_budget_ok,
            "full_diagnostic_compute_projection": compute_projection_ok,
        },
        "projection_scope": (
            "Projects four 768-token candidates for each of the 64 target trajectories "
            "per dataset and model. It does not estimate extra problems required when none "
            "of four candidates is correct; Stage D must enforce its six-hour cumulative cap."
        ),
        "note": (
            "This is an outcome-blind engineering throughput result. It does not authorize "
            "scientific interpretation or any stage beyond the preregistered decision."
        ),
    }
    with (args.output_dir / "generation_records.jsonl").open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    (args.output_dir / "stage_e_generation_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if status == "ENGINEERING_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
