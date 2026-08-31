#!/usr/bin/env python3
"""Score frozen metamorphic pairs at one PolyPythias seed/checkpoint."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def continuation_mean_logprob(model, tokenizer, prompts: list[str], continuations: list[str], device: str) -> list[float]:
    texts = [p + c for p, c in zip(prompts, continuations)]
    enc = tokenizer(texts, return_tensors="pt", padding=True)
    prompt_enc = tokenizer(prompts, return_tensors="pt", padding=True)
    input_ids = enc.input_ids.to(device)
    attention_mask = enc.attention_mask.to(device)
    prompt_lengths = prompt_enc.attention_mask.sum(dim=1).tolist()
    with torch.inference_mode():
        logits = model(input_ids=input_ids, attention_mask=attention_mask).logits[:, :-1]
        targets = input_ids[:, 1:]
        token_lp = torch.log_softmax(logits.float(), dim=-1).gather(-1, targets.unsqueeze(-1)).squeeze(-1)
    scores = []
    total_lengths = attention_mask.sum(dim=1).tolist()
    for row, (prompt_len, total_len) in enumerate(zip(prompt_lengths, total_lengths)):
        start = max(int(prompt_len) - 1, 0)
        stop = int(total_len) - 1
        piece = token_lp[row, start:stop]
        scores.append(float(piece.mean().item()))
    return scores


def batched(rows: list[dict], size: int):
    for start in range(0, len(rows), size):
        yield rows[start : start + size]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("FROZEN_CONFIG.json"))
    parser.add_argument("--items", type=Path, default=Path(__file__).with_name("items.jsonl"))
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if str(args.seed) not in config["model_repositories"]:
        raise SystemExit(f"seed {args.seed} is not frozen")
    if args.checkpoint not in config["checkpoints"]:
        raise SystemExit(f"checkpoint {args.checkpoint} is not frozen")
    rows = [json.loads(line) for line in args.items.read_text(encoding="utf-8").splitlines() if line]
    repo = config["model_repositories"][str(args.seed)]
    tokenizer = AutoTokenizer.from_pretrained(repo, revision=args.checkpoint)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    dtype = torch.float16 if config["dtype"] == "float16" else torch.float32
    model = AutoModelForCausalLM.from_pretrained(repo, revision=args.checkpoint, torch_dtype=dtype).to(args.device)
    model.eval()
    outputs = []
    for batch in batched(rows, config["batch_size"]):
        for representation, key in (("original", "prompt_original"), ("transformed", "prompt_transformed")):
            prompts = [x[key] for x in batch]
            if max(len(tokenizer(p).input_ids) for p in prompts) > config["max_prompt_tokens"]:
                raise RuntimeError("frozen max_prompt_tokens exceeded")
            correct = continuation_mean_logprob(model, tokenizer, prompts, [x["correct_continuation"] for x in batch], args.device)
            incorrect = continuation_mean_logprob(model, tokenizer, prompts, [x["incorrect_continuation"] for x in batch], args.device)
            for item, corr, incorr in zip(batch, correct, incorrect):
                if not math.isfinite(corr) or not math.isfinite(incorr):
                    raise RuntimeError("non-finite log probability")
                outputs.append({
                    "study_id": config["study_id"],
                    "seed": args.seed,
                    "checkpoint": args.checkpoint,
                    "item_id": item["item_id"],
                    "family": item["family"],
                    "representation": representation,
                    "correct_mean_logprob": corr,
                    "incorrect_mean_logprob": incorr,
                    "margin": corr - incorr,
                    "correct_choice": corr > incorr,
                })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(x, sort_keys=True) + "\n" for x in outputs), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "records": len(outputs), "repo": repo, "checkpoint": args.checkpoint}))


if __name__ == "__main__":
    main()
