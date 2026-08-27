from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import torch

from run_model import load_model, render_chat, stable_hash, strict_prefix_function


def completed(path: Path) -> set[str]:
    if not path.exists():
        return set()
    result = set()
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                result.add(json.loads(line)["case_id"])
            except (json.JSONDecodeError, KeyError):
                continue
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    all_cases = [json.loads(line) for line in args.cases.read_text(encoding="utf-8").splitlines() if line.strip()]
    done = completed(args.output)
    cases = [case for case in all_cases if case["model_id"] == args.model_id and case["case_id"] not in done]
    if not cases:
        print(json.dumps({"status": "no_cases", "model_id": args.model_id}))
        return
    tokenizer, model = load_model(args.model)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8", buffering=1, newline="\n") as handle:
        for case in cases:
            rendered = render_chat(tokenizer, case["prompt"], "native")
            encoded = tokenizer(rendered, return_tensors="pt", add_special_tokens=False)
            input_tokens = int(encoded["input_ids"].shape[1])
            encoded = {key: value.to("cuda:0") for key, value in encoded.items()}
            started = time.time()
            with torch.inference_mode():
                output = model.generate(
                    **encoded,
                    max_new_tokens=96,
                    do_sample=False,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id,
                    use_cache=True,
                    prefix_allowed_tokens_fn=strict_prefix_function(tokenizer, case["regex"]),
                )
            token_ids = output[0, input_tokens:].detach().cpu().tolist()
            text = tokenizer.decode(token_ids, skip_special_tokens=True).strip()
            result = {
                **{key: case[key] for key in ("case_id", "intervention_pair_id", "source_id", "model_id", "kind", "variant", "optimal_action")},
                "model_revision": args.model_revision,
                "text": text,
                "output_token_ids": token_ids,
                "prompt_sha256": stable_hash(rendered),
                "elapsed_seconds": time.time() - started,
            }
            handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps({"status": "ok", "model_id": args.model_id, "cases": len(cases)}, sort_keys=True))


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
