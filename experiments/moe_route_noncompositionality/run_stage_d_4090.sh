#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_D_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_D_REPO:-${stage_root}/repo}
output_root=${STAGE_D_OUTPUT:-${stage_root}/results/stage_d_discovery}
authorization=${STAGE_D_AUTHORIZATION:-${stage_root}/queue/STAGE_D_RUN_AUTHORIZATION.json}
gpu_id=${STAGE_D_GPU_ID:-4}

[[ "${gpu_id}" =~ ^[4-7]$ ]] || { echo "Only physical GPUs 4-7 are authorized." >&2; exit 2; }
[[ ! -e "${output_root}" ]] || { echo "Refusing to overwrite ${output_root}." >&2; exit 21; }
[[ -f "${authorization}" ]] || { echo "Missing Stage D run authorization." >&2; exit 22; }
status=$(${stage_root}/.venv-stage-d/bin/python -c "import json; print(json.load(open('${authorization}'))['status'])")
[[ "${status}" == "STAGE_D_RUN_AUTHORIZED" ]] || { echo "Invalid authorization status." >&2; exit 22; }

for stable_check in $(seq 1 18); do
    used_mib=$(nvidia-smi --id="${gpu_id}" --query-gpu=memory.used --format=csv,noheader,nounits | tr -d ' ')
    process_count=$(nvidia-smi --id="${gpu_id}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^[[:space:]]*$/d' | wc -l)
    if [[ "${used_mib}" -gt 512 || "${process_count}" -ne 0 ]]; then
        echo "GPU ${gpu_id} lost exclusivity during the 180-second discovery check." >&2
        exit 20
    fi
    if [[ "${stable_check}" -lt 18 ]]; then sleep 10; fi
done

export CUDA_VISIBLE_DEVICES="${gpu_id}"
exec timeout --signal=TERM 21600 bash "${repo_root}/experiments/moe_route_noncompositionality/stage_d_pipeline.sh"
