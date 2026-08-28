#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_D_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_D_REPO:-${stage_root}/repo}
output_root=${STAGE_D_PREFLIGHT_OUTPUT:-${stage_root}/results/stage_d_preflight_v2}
cache_root=${STAGE_D_CACHE:-/mnt/sdb/ccj/hf_cache_idle_2}
dataset_cache_root=${STAGE_D_DATASET_CACHE:-${cache_root}/datasets}
gpu_id=${STAGE_D_GPU_ID:-4}
python_bin=${STAGE_D_PYTHON:-${stage_root}/.venv-stage-d/bin/python}

[[ "${gpu_id}" =~ ^[4-7]$ ]] || { echo "Only physical GPUs 4-7 are authorized." >&2; exit 2; }
[[ ! -e "${output_root}" ]] || { echo "Refusing to overwrite ${output_root}." >&2; exit 21; }

for stable_check in $(seq 1 18); do
    used_mib=$(nvidia-smi --id="${gpu_id}" --query-gpu=memory.used --format=csv,noheader,nounits | tr -d ' ')
    process_count=$(nvidia-smi --id="${gpu_id}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^[[:space:]]*$/d' | wc -l)
    if [[ "${used_mib}" -gt 512 || "${process_count}" -ne 0 ]]; then
        echo "GPU ${gpu_id} lost exclusivity during the 180-second preflight check." >&2
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

cd "${repo_root}"
"${python_bin}" -m unittest discover -s experiments/moe_route_noncompositionality/tests -v
timeout --signal=TERM 3000 "${python_bin}" \
    experiments/moe_route_noncompositionality/stage_d_acquire.py \
    --preflight \
    --preflight-problems-per-dataset 2 \
    --max-problems-per-dataset 30 \
    --max-gpu-hours 0.75 \
    --analysis-reserve-seconds 0 \
    --output-dir "${output_root}" \
    --cache-dir "${cache_root}" \
    --dataset-cache-dir "${dataset_cache_root}" \
    --frozen-config experiments/moe_route_noncompositionality/STAGE_D_FROZEN.yaml \
    --thresholds experiments/moe_route_noncompositionality/THRESHOLDS.yaml \
    --device cuda:0

"${python_bin}" experiments/moe_route_noncompositionality/stage_d_preflight_validate.py \
    --preflight-dir "${output_root}" \
    --stage-root "${stage_root}" \
    --cache-dir "${cache_root}" \
    --output "${output_root}/PREFLIGHT_GATE.json"
