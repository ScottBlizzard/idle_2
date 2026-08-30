#!/usr/bin/env bash
set -euo pipefail

ROOT=/mnt/sdb/ccj/idle_2/endogenous_failure_conditioning
REPO="$ROOT/repo/experiments/endogenous_failure_conditioning"
RESULT="$ROOT/runs/no_trace_baseline_v1"
BANK="$ROOT/repo/experiments/endogenous_failure_conditioning/results/error_bank_v2_1_qwen_lineages/error_bank.jsonl"
PARENT="$REPO/FROZEN_CONFIG_V2_QWEN_LINEAGES.json"
FROZEN="$REPO/NO_TRACE_BASELINE_FROZEN.json"
PYTHON=/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/.venv-stage-d/bin/python
mkdir -p "$RESULT/outputs" "$RESULT/logs"

declare -A GPU=( [qwen25_3b]=4 [qwen25_7b]=5 [qwen3_4b]=6 [qwen3_8b]=7 )
declare -A BATCH=( [qwen25_3b]=8 [qwen25_7b]=4 [qwen3_4b]=8 [qwen3_8b]=4 )

for model in qwen25_3b qwen25_7b qwen3_4b qwen3_8b; do
  if [[ -f "$RESULT/outputs/$model.manifest.json" ]]; then
    continue
  fi
  CUDA_VISIBLE_DEVICES="${GPU[$model]}" HF_HOME="$ROOT/hf_home" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    "$PYTHON" "$REPO/run_no_trace_baseline.py" \
      --bank "$BANK" --model-key "$model" --output "$RESULT/outputs/$model.jsonl" \
      --batch-size "${BATCH[$model]}" --parent-config "$PARENT" --frozen "$FROZEN" \
      >"$RESULT/logs/$model.log" 2>&1 &
  echo "$! $model ${GPU[$model]}" >> "$RESULT/PIDS.txt"
done
wait
echo COMPLETE > "$RESULT/STATUS.txt"
