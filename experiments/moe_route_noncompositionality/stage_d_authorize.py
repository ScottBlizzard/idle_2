#!/usr/bin/env python3
"""Create the machine-verifiable transition from preflight to one Stage D run."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from stage_d_common import sha256_file


SOURCE_FILES = (
    "STAGE_D_FROZEN.yaml",
    "THRESHOLDS.yaml",
    "stage_d_common.py",
    "stage_d_predictors.py",
    "stage_d_acquire.py",
    "stage_d_analyze.py",
    "run_stage_d_4090.sh",
    "stage_d_pipeline.sh",
    "wait_and_run_stage_d.sh",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-experiment-dir", type=Path, required=True)
    parser.add_argument("--preflight-gate", type=Path, required=True)
    parser.add_argument("--discovery-output", type=Path, required=True)
    parser.add_argument("--authorization-output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    gate = json.loads(args.preflight_gate.read_text(encoding="utf-8"))
    if gate.get("status") != "STAGE_D_PREFLIGHT_PASS":
        raise RuntimeError("Stage D preflight did not pass")
    if gate.get("scientific_interpretation_allowed") is not False:
        raise RuntimeError("Preflight gate has an invalid interpretation flag")
    if args.discovery_output.exists():
        raise FileExistsError("Discovery output already exists")
    hashes = {}
    for relative in SOURCE_FILES:
        path = args.repo_experiment_dir / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        hashes[relative] = sha256_file(path)
    result = {
        "status": "STAGE_D_RUN_AUTHORIZED",
        "authorized_runs": 1,
        "authorized_model": "allenai/OLMoE-1B-7B-0924-Instruct",
        "authorized_physical_gpus": [4, 5, 6, 7],
        "stage_c_authorized": False,
        "preflight_gate_sha256": sha256_file(args.preflight_gate),
        "source_sha256": hashes,
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    args.authorization_output.parent.mkdir(parents=True, exist_ok=True)
    with args.authorization_output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
    print(json.dumps({"status": result["status"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
