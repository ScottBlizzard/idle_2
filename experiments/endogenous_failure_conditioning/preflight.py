#!/usr/bin/env python3
"""Outcome-blind structural and tokenizer preflight for the frozen pilot."""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

from common import build_messages, load_config, read_jsonl, sha256_file


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()

    from transformers import AutoConfig, AutoTokenizer, __version__ as transformers_version

    config = load_config(args.config)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    if sha256_file(args.bank) != manifest["error_bank_sha256"]:
        raise RuntimeError("Error-bank hash no longer matches its manifest")
    bank = list(read_jsonl(args.bank))
    expected_bank = (
        len(config["domains"])
        * int(config["problems_per_domain"])
        * len(config["models"])
    )
    if len(bank) != expected_bank:
        raise RuntimeError(f"Unexpected bank size: {len(bank)} != {expected_bank}")

    model_checks = {}
    passed = True
    for model_key, model in config["models"].items():
        try:
            tokenizer = AutoTokenizer.from_pretrained(model["hf_id"], revision=model["revision"])
            resolved = AutoConfig.from_pretrained(model["hf_id"], revision=model["revision"])
            lengths = []
            for record in bank:
                for wrapper in config["wrappers"]:
                    rendered = tokenizer.apply_chat_template(
                        build_messages(record, wrapper),
                        tokenize=False,
                        add_generation_prompt=True,
                        **model.get("chat_template_kwargs", {}),
                    )
                    lengths.append(len(tokenizer(rendered, add_special_tokens=False).input_ids))
            maximum = max(lengths)
            overflow = sum(
                length + int(config["max_new_tokens"]) > 8192 for length in lengths
            )
            revision_match = str(getattr(resolved, "_commit_hash", "")) == model["revision"]
            model_pass = overflow == 0 and revision_match
            model_checks[model_key] = {
                "hf_id": model["hf_id"],
                "expected_revision": model["revision"],
                "resolved_revision": str(getattr(resolved, "_commit_hash", "")),
                "revision_match": revision_match,
                "prompt_count": len(lengths),
                "maximum_prompt_tokens": maximum,
                "overflow_count": overflow,
                "chat_template_kwargs": model.get("chat_template_kwargs", {}),
                "pass": model_pass,
            }
        except Exception as exc:
            model_pass = False
            model_checks[model_key] = {
                "hf_id": model["hf_id"],
                "expected_revision": model["revision"],
                "pass": False,
                "error_type": type(exc).__name__,
                "error": str(exc)[:1000],
            }
        passed &= model_pass

    result = {
        "status": "PREFLIGHT_PASS" if passed else "PREFLIGHT_FAIL",
        "bank_rows": len(bank),
        "bank_sha256": sha256_file(args.bank),
        "manifest_sha256": sha256_file(args.manifest),
        "config_sha256": sha256_file(args.config or Path(__file__).with_name("FROZEN_CONFIG.json")),
        "python": platform.python_version(),
        "transformers": transformers_version,
        "models": model_checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
