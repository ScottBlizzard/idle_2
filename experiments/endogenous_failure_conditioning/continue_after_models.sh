#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 PROJECT_BASE" >&2
  exit 2
fi

BASE="$(readlink -f "$1")"
REPO="$BASE/repo"
EXPERIMENT="$REPO/experiments/endogenous_failure_conditioning"
CONFIG="$EXPERIMENT/FROZEN_CONFIG_V2_QWEN_LINEAGES.json"
BANK="$EXPERIMENT/results/error_bank_v2_1_qwen_lineages"
RUN="$BASE/runs/pilot_v2_1_qwen_lineages"
STATUS="$BASE/MODEL_DOWNLOAD_STATUS.json"
PYTHON_BIN="/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/.venv-stage-d/bin/python"

while [[ ! -f "$STATUS" ]]; do
  sleep 30
done
download_status="$("$PYTHON_BIN" -c 'import json,sys; print(json.load(open(sys.argv[1]))["status"])' "$STATUS")"
if [[ "$download_status" != "ALL_MODELS_READY" ]]; then
  echo "model preparation terminal status: $download_status" >&2
  exit 3
fi

export HF_HOME="$BASE/hf_home"
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export PYTHON_BIN
exec bash "$EXPERIMENT/wait_and_run_pilot.sh" "$REPO" "$BANK" "$RUN" "$CONFIG"
