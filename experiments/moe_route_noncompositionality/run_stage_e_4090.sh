#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_E_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_E_REPO:-${stage_root}/repo}
output_root=${STAGE_E_OUTPUT:-${stage_root}/results/stage_e}
cache_root=${STAGE_E_CACHE:-/mnt/sdb/ccj/hf_cache_idle_2}
gpu_id=${STAGE_E_GPU_ID:-7}
python_bin=${STAGE_E_PYTHON:-/home/ccj/miniconda3/envs/iclr1/bin/python}

mkdir -p "${output_root}" "${cache_root}"

for stable_check in 1 2 3; do
    used_mib=$(nvidia-smi --id="${gpu_id}" --query-gpu=memory.used --format=csv,noheader,nounits | tr -d ' ')
    compute_pids=$(nvidia-smi --id="${gpu_id}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^$/d' | wc -l)
    if [[ "${used_mib}" -gt 512 || "${compute_pids}" -ne 0 ]]; then
        echo "Refusing to start: GPU ${gpu_id} is not exclusively idle (memory=${used_mib} MiB, processes=${compute_pids})." >&2
        exit 20
    fi
    if [[ "${stable_check}" -lt 3 ]]; then
        sleep 10
    fi
done

export CUDA_VISIBLE_DEVICES="${gpu_id}"
export HF_HOME="${cache_root}"
export HF_HUB_CACHE="${cache_root}/hub"
export TRANSFORMERS_CACHE="${cache_root}/transformers"
export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
export TOKENIZERS_PARALLELISM=false

exec timeout --signal=TERM 3600 "${python_bin}" "${repo_root}/experiments/moe_route_noncompositionality/stage_e_engineering.py" \
    --output-dir "${output_root}" \
    --cache-dir "${cache_root}" \
    --device cuda:0
