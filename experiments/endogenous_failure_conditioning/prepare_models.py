#!/usr/bin/env python3
"""Download every frozen corrector revision before GPU allocation."""

from __future__ import annotations

import argparse
import json
import os
import platform
import time
from pathlib import Path

from common import load_config


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if not os.environ.get("HF_HOME"):
        raise RuntimeError("HF_HOME must point to the project directory on /mnt/sdb")
    from huggingface_hub import snapshot_download

    args.output.parent.mkdir(parents=True, exist_ok=True)
    records = []
    for model_key, model in load_config(args.config)["models"].items():
        started = time.time()
        try:
            resolved = snapshot_download(
                repo_id=model["hf_id"],
                revision=model["revision"],
                repo_type="model",
            )
            records.append(
                {
                    "model_key": model_key,
                    "hf_id": model["hf_id"],
                    "revision": model["revision"],
                    "resolved_path": resolved,
                    "elapsed_seconds": time.time() - started,
                    "status": "READY",
                }
            )
        except Exception as exc:
            records.append(
                {
                    "model_key": model_key,
                    "hf_id": model["hf_id"],
                    "revision": model["revision"],
                    "elapsed_seconds": time.time() - started,
                    "status": "FAILED",
                    "error_type": type(exc).__name__,
                    "error": str(exc)[:2000],
                }
            )
            result = {
                "status": "MODEL_DOWNLOAD_FAILED",
                "hostname": platform.node(),
                "hf_home": os.environ["HF_HOME"],
                "models": records,
            }
            args.output.write_text(
                json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )
            print(json.dumps(result, indent=2, sort_keys=True))
            raise SystemExit(2)

    result = {
        "status": "ALL_MODELS_READY",
        "hostname": platform.node(),
        "hf_home": os.environ["HF_HOME"],
        "models": records,
    }
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
