#!/usr/bin/env bash
set -euo pipefail
ROOT=/mnt/sdb/ccj/idle_2/endogenous_failure_conditioning
REPO="$ROOT/repo"
OUT="$ROOT/runs/native_likelihood_error_gain_v1"
PY=/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/.venv-stage-d/bin/python
BANK="$REPO/experiments/endogenous_failure_conditioning/results/error_bank_v2_1_qwen_lineages/error_bank.jsonl"
CONFIG="$REPO/experiments/endogenous_failure_conditioning/FROZEN_CONFIG_V2_QWEN_LINEAGES.json"
SCRIPT="$REPO/analysis/native_likelihood_error_gain/score_trace_likelihood.py"
mkdir -p "$OUT/outputs" "$OUT/logs"
declare -A GPU=( [qwen25_3b]=4 [qwen25_7b]=5 [qwen3_4b]=6 [qwen3_8b]=7 )
for model in qwen25_3b qwen25_7b qwen3_4b qwen3_8b; do
  if [[ -f "$OUT/outputs/$model.manifest.json" ]]; then continue; fi
  CUDA_VISIBLE_DEVICES="${GPU[$model]}" HF_HOME="$ROOT/hf_home" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    "$PY" "$SCRIPT" --bank "$BANK" --config "$CONFIG" --model-key "$model" \
      --output "$OUT/outputs/$model.jsonl" >"$OUT/logs/$model.log" 2>&1 &
  echo "$! $model ${GPU[$model]}" >> "$OUT/PIDS.txt"
done
wait
echo COMPLETE > "$OUT/STATUS.txt"
