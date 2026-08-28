#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_D_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_D_REPO:-${stage_root}/repo}
output_root=${STAGE_D_OUTPUT:-${stage_root}/results/stage_d_discovery}
cache_root=${STAGE_D_CACHE:-/mnt/sdb/ccj/hf_cache_idle_2}
dataset_cache_root=${STAGE_D_DATASET_CACHE:-${cache_root}/datasets}
python_bin=${STAGE_D_PYTHON:-${stage_root}/.venv-stage-d/bin/python}

cd "${repo_root}"
"${python_bin}" experiments/moe_route_noncompositionality/stage_d_acquire.py \
    --output-dir "${output_root}" \
    --cache-dir "${cache_root}" \
    --dataset-cache-dir "${dataset_cache_root}" \
    --frozen-config experiments/moe_route_noncompositionality/STAGE_D_FROZEN.yaml \
    --thresholds experiments/moe_route_noncompositionality/THRESHOLDS.yaml \
    --device cuda:0 \
    --target-per-dataset 64 \
    --minimum-per-dataset 48 \
    --max-gpu-hours 6 \
    --analysis-reserve-seconds 1800

"${python_bin}" experiments/moe_route_noncompositionality/stage_d_analyze.py \
    --input-dir "${output_root}" \
    --maximum-cumulative-hours 6 \
    --minimum-per-dataset 48
