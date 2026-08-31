#!/usr/bin/env bash
set -euo pipefail

physical_gpu="${1:-4}"
if [[ ! "$physical_gpu" =~ ^[4-7]$ ]]; then
  echo "physical GPU must be one of 4,5,6,7" >&2
  exit 2
fi
project_root="/mnt/sdb/ccj/idle_2/metamorphic_reentry_dynamics"
repo_dir="$project_root/repo/experiments/metamorphic_reentry_dynamics"
venv_python="/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/.venv-stage-d/bin/python"
mkdir -p "$project_root/results/preflight" "$project_root/hf_home" "$project_root/logs"
export CUDA_VISIBLE_DEVICES="$physical_gpu"
export HF_HOME="$project_root/hf_home"
export HF_ENDPOINT="https://hf-mirror.com"
export TOKENIZERS_PARALLELISM=false
"$venv_python" "$repo_dir/score_checkpoints.py" \
  --seed 1 --checkpoint step143000 \
  --config "$repo_dir/FROZEN_CONFIG.json" \
  --items "$repo_dir/items.jsonl" \
  --output "$project_root/results/preflight/seed1_step143000.jsonl" \
  --device cuda
"$venv_python" "$repo_dir/summarize_preflight.py" \
  --config "$repo_dir/FROZEN_CONFIG.json" \
  --input "$project_root/results/preflight/seed1_step143000.jsonl" \
  --output "$project_root/results/preflight/PREFLIGHT_GATE.json"
