#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_E_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_E_REPO:-${stage_root}/repo}
engineering_root=${STAGE_E_ENGINEERING_OUTPUT:-${stage_root}/results/stage_e}
output_root=${STAGE_E_GENERATION_OUTPUT:-${stage_root}/results/stage_e_generation}
cache_root=${STAGE_E_CACHE:-/mnt/sdb/ccj/hf_cache_idle_2}
dataset_cache_root=${STAGE_E_DATASET_CACHE:-${cache_root}/datasets}
gpu_id=${STAGE_E_GPU_ID:-7}
python_bin=${STAGE_E_PYTHON:-/home/ccj/miniconda3/envs/iclr1/bin/python}

[[ ! -e "${output_root}" ]] || {
    echo "Refusing to overwrite existing generation-pilot output: ${output_root}" >&2
    exit 21
}
[[ -f "${engineering_root}/stage_e_summary.json" ]] || {
    echo "Missing Stage E engineering summary." >&2
    exit 22
}

for stable_check in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18; do
    used_mib=$(nvidia-smi --id="${gpu_id}" --query-gpu=memory.used --format=csv,noheader,nounits | tr -d ' ')
    compute_pids=$(nvidia-smi --id="${gpu_id}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^$/d' | wc -l)
    if [[ "${used_mib}" -gt 512 || "${compute_pids}" -ne 0 ]]; then
        echo "Refusing to start: GPU ${gpu_id} is not exclusively idle (memory=${used_mib} MiB, processes=${compute_pids})." >&2
        exit 20
    fi
    if [[ "${stable_check}" -lt 18 ]]; then sleep 10; fi
done

export CUDA_VISIBLE_DEVICES="${gpu_id}"
export HF_HOME="${cache_root}"
export HF_HUB_CACHE="${cache_root}/hub"
export HF_DATASETS_CACHE="${dataset_cache_root}"
export TRANSFORMERS_CACHE="${cache_root}/transformers"
export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
export TOKENIZERS_PARALLELISM=false

exec timeout --signal=TERM 3300 "${python_bin}" \
    "${repo_root}/experiments/moe_route_noncompositionality/stage_e_generation_pilot.py" \
    --output-dir "${output_root}" \
    --engineering-summary "${engineering_root}/stage_e_summary.json" \
    --cache-dir "${cache_root}" \
    --dataset-cache-dir "${dataset_cache_root}" \
    --device cuda:0
