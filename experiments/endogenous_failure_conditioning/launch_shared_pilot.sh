#!/usr/bin/env bash
set -euo pipefail

# Outcome-blind engineering launcher. It shares GPUs with unrelated workloads
# when measured free memory is sufficient; it never stops or modifies them.

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
GPU_POOL="${GPU_POOL:-0 1 2 3 4 5 6 7}"
LOCK_FILE="$RUN_DIR.launch.lock"

mkdir -p "$(dirname "$RUN_DIR")"
exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  echo "another pilot watcher/launcher holds $LOCK_FILE" >&2
  exit 3
fi
if [[ -f "$RUN_DIR/results/FINAL_GATE.json" ]]; then
  echo "pilot already complete: $RUN_DIR/results/FINAL_GATE.json"
  exit 0
fi
if [[ ! -f "$BANK_DIR/error_bank.jsonl" || ! -f "$BANK_DIR/MANIFEST.json" ]]; then
  echo "frozen error bank is missing" >&2
  exit 5
fi

mkdir -p "$RUN_DIR/outputs"
if [[ -f "$RUN_DIR/ERROR_BANK_MANIFEST.json" ]]; then
  cmp -s "$BANK_DIR/MANIFEST.json" "$RUN_DIR/ERROR_BANK_MANIFEST.json" || {
    echo "existing run has a different error-bank manifest" >&2
    exit 6
  }
else
  cp "$BANK_DIR/MANIFEST.json" "$RUN_DIR/ERROR_BANK_MANIFEST.json"
fi
if [[ ! -f "$RUN_DIR/PREFLIGHT.json" ]]; then
  "$PYTHON_BIN" "$SCRIPT_DIR/preflight.py" \
    --bank "$BANK_DIR/error_bank.jsonl" \
    --manifest "$BANK_DIR/MANIFEST.json" \
    --config "$CONFIG" \
    --output "$RUN_DIR/PREFLIGHT.json" \
    > "$RUN_DIR/preflight.log" 2>&1
fi

# Conservative measured-free-memory requirements include model weights, KV
# cache, the batch of two, and several GiB of headroom. Largest models select
# first from the currently freest distinct GPU.
MODELS=(qwen3_8b qwen25_7b qwen3_4b qwen25_3b)
NEEDS=(20000 18000 11500 9500)
declare -A USED
declare -A ASSIGNED
declare -A FREE_AT_SELECTION

for index in "${!MODELS[@]}"; do
  model="${MODELS[$index]}"
  need="${NEEDS[$index]}"
  if [[ -f "$RUN_DIR/outputs/$model.manifest.json" ]]; then
    continue
  fi
  best_gpu=""
  best_free=-1
  for gpu in $GPU_POOL; do
    [[ -z "${USED[$gpu]:-}" ]] || continue
    free="$(nvidia-smi -i "$gpu" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
    if [[ "$free" -ge "$need" && "$free" -gt "$best_free" ]]; then
      best_gpu="$gpu"
      best_free="$free"
    fi
  done
  if [[ -z "$best_gpu" ]]; then
    echo "no distinct GPU currently has ${need} MiB free for $model" >&2
    exit 20
  fi
  USED[$best_gpu]=1
  ASSIGNED[$model]="$best_gpu"
  FREE_AT_SELECTION[$model]="$best_free"
done

allocation="$RUN_DIR/RESOURCE_ALLOCATION.tsv"
printf 'model\tgpu\tminimum_free_mib\tobserved_free_mib\n' > "$allocation"
for index in "${!MODELS[@]}"; do
  model="${MODELS[$index]}"
  [[ -n "${ASSIGNED[$model]:-}" ]] || continue
  printf '%s\t%s\t%s\t%s\n' "$model" "${ASSIGNED[$model]}" "${NEEDS[$index]}" "${FREE_AT_SELECTION[$model]}" >> "$allocation"
done

pids=()
launched=()
for index in "${!MODELS[@]}"; do
  model="${MODELS[$index]}"
  gpu="${ASSIGNED[$model]:-}"
  [[ -n "$gpu" ]] || continue
  need="${NEEDS[$index]}"
  free="$(nvidia-smi -i "$gpu" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
  if [[ "$free" -lt "$need" ]]; then
    echo "GPU $gpu free memory fell below the $model launch floor: $free < $need MiB" >&2
    exit 21
  fi
  CUDA_VISIBLE_DEVICES="$gpu" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    "$PYTHON_BIN" "$SCRIPT_DIR/run_corrector.py" \
      --bank "$BANK_DIR/error_bank.jsonl" \
      --model-key "$model" \
      --config "$CONFIG" \
      --output "$RUN_DIR/outputs/$model.jsonl" \
      --backend transformers \
      > "$RUN_DIR/$model.log" 2>&1 &
  pids+=("$!")
  launched+=("$model")
  printf '%s gpu=%s pid=%s free_before_launch_mib=%s\n' "$model" "$gpu" "$!" "$free" | tee -a "$RUN_DIR/PIDS.txt"
done

failure=0
for index in "${!pids[@]}"; do
  if ! wait "${pids[$index]}"; then
    echo "corrector failed: ${launched[$index]} pid=${pids[$index]}" >&2
    failure=1
  fi
done
if [[ "$failure" -ne 0 ]]; then
  echo "one or more correctors failed; batch-level outputs were preserved for resume" >&2
  exit 8
fi

"$PYTHON_BIN" "$SCRIPT_DIR/analyze_pilot.py" \
  --bank "$BANK_DIR/error_bank.jsonl" \
  --outputs "$RUN_DIR/outputs" \
  --config "$CONFIG" \
  --result "$RUN_DIR/results" \
  > "$RUN_DIR/analyze.log" 2>&1
echo "pilot complete: $RUN_DIR/results/FINAL_GATE.json"
