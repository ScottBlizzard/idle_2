#!/usr/bin/env bash
set -euo pipefail

# Requires all four authorized physical GPUs to be exclusively idle for three minutes.
# It never inspects, stops, or modifies a foreign process.

if [[ $# -ne 4 ]]; then
  echo "usage: $0 REPO_DIR BANK_DIR RUN_DIR CONFIG" >&2
  exit 2
fi

REPO_DIR="$(readlink -f "$1")"
BANK_DIR="$(readlink -f "$2")"
RUN_DIR="$(readlink -m "$3")"
CONFIG="$(readlink -f "$4")"
SCRIPT_DIR="$REPO_DIR/experiments/endogenous_failure_conditioning"
PYTHON_BIN="${PYTHON_BIN:-python}"
LOCK_FILE="$RUN_DIR.launch.lock"
mkdir -p "$(dirname "$RUN_DIR")"
exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  echo "another pilot watcher/launcher holds $LOCK_FILE" >&2
  exit 3
fi
if [[ -e "$RUN_DIR" ]]; then
  echo "refusing to reuse existing run directory: $RUN_DIR" >&2
  exit 4
fi
if [[ ! -f "$BANK_DIR/error_bank.jsonl" || ! -f "$BANK_DIR/MANIFEST.json" ]]; then
  echo "frozen error bank is missing" >&2
  exit 5
fi

gpu_idle() {
  local index="$1" uuid memory util
  uuid="$(nvidia-smi --query-gpu=index,uuid --format=csv,noheader,nounits | awk -F', ' -v i="$index" '$1==i {print $2}')"
  [[ -n "$uuid" ]] || return 1
  if nvidia-smi --query-compute-apps=gpu_uuid,pid --format=csv,noheader,nounits 2>/dev/null | awk -F', ' -v u="$uuid" '$1==u {found=1} END {exit !found}'; then
    return 1
  fi
  read -r memory util < <(nvidia-smi -i "$index" --query-gpu=memory.used,utilization.gpu --format=csv,noheader,nounits | tr ',' ' ')
  [[ "$memory" -le 256 && "$util" -le 5 ]]
}

consecutive=0
while [[ "$consecutive" -lt 18 ]]; do
  all_idle=1
  for gpu in 4 5 6 7; do
    if ! gpu_idle "$gpu"; then
      all_idle=0
    fi
  done
  if [[ "$all_idle" -eq 1 ]]; then
    consecutive=$((consecutive + 1))
    echo "idle observation $consecutive/18"
  else
    consecutive=0
    echo "authorized GPU set is busy; waiting"
  fi
  sleep 10
done

# Independent last-moment check. A conflict aborts safely before any model loads.
for gpu in 4 5 6 7; do
  if ! gpu_idle "$gpu"; then
    echo "GPU $gpu became busy during launch check; aborting without starting work" >&2
    exit 6
  fi
done

mkdir "$RUN_DIR"
cp "$BANK_DIR/MANIFEST.json" "$RUN_DIR/ERROR_BANK_MANIFEST.json"
"$PYTHON_BIN" "$SCRIPT_DIR/preflight.py" \
  --bank "$BANK_DIR/error_bank.jsonl" \
  --manifest "$BANK_DIR/MANIFEST.json" \
  --config "$CONFIG" \
  --output "$RUN_DIR/PREFLIGHT.json" \
  > "$RUN_DIR/preflight.log" 2>&1

mapfile -t MODELS < <("$PYTHON_BIN" -c 'import json,sys; print("\n".join(json.load(open(sys.argv[1]))["models"]))' "$CONFIG")
if [[ "${#MODELS[@]}" -ne 4 ]]; then
  echo "frozen config must contain exactly four models" >&2
  exit 9
fi
GPUS=(4 5 6 7)
mkdir "$RUN_DIR/outputs"
for index in 0 1 2 3; do
  model="${MODELS[$index]}"
  gpu="${GPUS[$index]}"
  if ! gpu_idle "$gpu"; then
    echo "GPU $gpu became busy after preflight; aborting before model launch" >&2
    exit 7
  fi
done

pids=()
for index in 0 1 2 3; do
  model="${MODELS[$index]}"
  gpu="${GPUS[$index]}"
  CUDA_VISIBLE_DEVICES="$gpu" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    "$PYTHON_BIN" "$SCRIPT_DIR/run_corrector.py" \
      --bank "$BANK_DIR/error_bank.jsonl" \
      --model-key "$model" \
      --config "$CONFIG" \
      --output "$RUN_DIR/outputs/$model.jsonl" \
      --backend auto \
      > "$RUN_DIR/$model.log" 2>&1 &
  pids+=("$!")
  echo "$model gpu=$gpu pid=$!" >> "$RUN_DIR/PIDS.txt"
done

failure=0
for pid in "${pids[@]}"; do
  if ! wait "$pid"; then
    failure=1
  fi
done
if [[ "$failure" -ne 0 ]]; then
  echo "one or more correctors failed; outputs preserved" >&2
  exit 8
fi

"$PYTHON_BIN" "$SCRIPT_DIR/analyze_pilot.py" \
  --bank "$BANK_DIR/error_bank.jsonl" \
  --outputs "$RUN_DIR/outputs" \
  --config "$CONFIG" \
  --result "$RUN_DIR/results" \
  > "$RUN_DIR/analyze.log" 2>&1
echo "pilot complete: $RUN_DIR/results/FINAL_GATE.json"
