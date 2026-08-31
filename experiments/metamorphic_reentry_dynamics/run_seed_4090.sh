#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 PHYSICAL_GPU SEED" >&2
  exit 2
fi

physical_gpu="$1"
seed="$2"
if [[ ! "$physical_gpu" =~ ^[4-7]$ ]]; then
  echo "physical GPU must be one of 4,5,6,7" >&2
  exit 2
fi
if [[ ! "$seed" =~ ^[1-9]$ ]]; then
  echo "seed must be 1..9" >&2
  exit 2
fi

project_root="/mnt/sdb/ccj/idle_2/metamorphic_reentry_dynamics"
repo_dir="$project_root/repo/experiments/metamorphic_reentry_dynamics"
venv_python="/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/.venv-stage-d/bin/python"
split="discovery"
if (( seed >= 6 )); then
  split="confirmation"
fi
output_dir="$project_root/results/$split"
mkdir -p "$output_dir" "$project_root/hf_home" "$project_root/logs"

export CUDA_VISIBLE_DEVICES="$physical_gpu"
export HF_HOME="$project_root/hf_home"
export HF_ENDPOINT="https://hf-mirror.com"
export TOKENIZERS_PARALLELISM=false

mapfile -t checkpoints < <("$venv_python" -c 'import json; print("\n".join(json.load(open("'"$repo_dir"'/FROZEN_CONFIG.json"))["checkpoints"]))')
for checkpoint in "${checkpoints[@]}"; do
  output="$output_dir/seed${seed}_${checkpoint}.jsonl"
  if [[ -s "$output" ]]; then
    echo "skip existing $output"
    continue
  fi
  echo "start seed=$seed checkpoint=$checkpoint physical_gpu=$physical_gpu"
  "$venv_python" "$repo_dir/score_checkpoints.py" \
    --config "$repo_dir/FROZEN_CONFIG.json" \
    --items "$repo_dir/items.jsonl" \
    --seed "$seed" \
    --checkpoint "$checkpoint" \
    --output "$output.tmp" \
    --device cuda
  mv "$output.tmp" "$output"
done
