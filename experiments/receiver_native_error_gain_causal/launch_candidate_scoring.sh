#!/usr/bin/env bash
set -euo pipefail

ROOT=/mnt/sdb/ccj/idle_2/endogenous_failure_conditioning
REPO="$ROOT/repo"
OUT="$ROOT/runs/receiver_native_error_gain_causal_v1"
PY=/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/.venv-stage-d/bin/python
EXP="$REPO/experiments/receiver_native_error_gain_causal"
LIBRARY="$EXP/artifacts/candidate_library.jsonl"
PARENT="$REPO/experiments/endogenous_failure_conditioning/FROZEN_CONFIG_V2_QWEN_LINEAGES.json"
FROZEN="$EXP/FROZEN_CONFIG.json"
SCRIPT="$EXP/score_candidates.py"

mkdir -p "$OUT/outputs" "$OUT/logs"
if [[ -f "$OUT/STATUS.txt" ]]; then
  echo "Refusing to reuse an existing terminal run: $(cat "$OUT/STATUS.txt")" >&2
  exit 2
fi

declare -A GPU=( [qwen25_3b]=4 [qwen25_7b]=5 [qwen3_4b]=6 [qwen3_8b]=7 )
declare -a PIDS=()
for model in qwen25_3b qwen25_7b qwen3_4b qwen3_8b; do
  if [[ -f "$OUT/outputs/$model.manifest.json" ]]; then
    continue
  fi
  CUDA_VISIBLE_DEVICES="${GPU[$model]}" HF_HOME="$ROOT/hf_home" \
    HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    "$PY" "$SCRIPT" --library "$LIBRARY" --parent-config "$PARENT" \
      --frozen "$FROZEN" --model-key "$model" \
      --output "$OUT/outputs/$model.jsonl" >"$OUT/logs/$model.log" 2>&1 &
  pid=$!
  PIDS+=("$pid")
  echo "$pid $model ${GPU[$model]}" >> "$OUT/PIDS.txt"
done

failed=0
for pid in "${PIDS[@]}"; do
  if ! wait "$pid"; then
    failed=1
  fi
done
if [[ "$failed" -ne 0 ]]; then
  echo FAILED > "$OUT/STATUS.txt"
  exit 1
fi
echo COMPLETE > "$OUT/STATUS.txt"
