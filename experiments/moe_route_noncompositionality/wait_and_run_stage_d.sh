#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_D_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_D_REPO:-${stage_root}/repo}
output_root=${STAGE_D_OUTPUT:-${stage_root}/results/stage_d_discovery}
gpu_candidates_text=${STAGE_D_GPU_IDS:-4 5 6 7}
queue_root=${stage_root}/queue
queue_log=${queue_root}/stage_d_discovery.log
queue_status=${queue_root}/stage_d_status.txt
authorization=${queue_root}/STAGE_D_RUN_AUTHORIZATION.json
launcher=${repo_root}/experiments/moe_route_noncompositionality/run_stage_d_4090.sh

mkdir -p "${queue_root}"
exec 9>"${queue_root}/stage_d.lock"
flock -n 9 || { echo "Another Stage D watcher is active." >&2; exit 30; }
[[ -f "${authorization}" ]] || { echo "Missing Stage D authorization." >&2; exit 22; }
[[ ! -e "${output_root}" ]] || { echo "Discovery output already exists." >&2; exit 21; }

read -r -a candidates <<< "${gpu_candidates_text}"
for candidate in "${candidates[@]}"; do
    [[ "${candidate}" =~ ^[4-7]$ ]] || { echo "Unauthorized GPU ${candidate}." >&2; exit 2; }
done

echo WAITING >"${queue_status}"
while true; do
    for candidate in "${candidates[@]}"; do
        used_mib=$(nvidia-smi --id="${candidate}" --query-gpu=memory.used --format=csv,noheader,nounits | tr -d ' ')
        process_count=$(nvidia-smi --id="${candidate}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^[[:space:]]*$/d' | wc -l)
        if [[ "${used_mib}" -le 512 && "${process_count}" -eq 0 ]]; then
            gpu_id=${candidate}
            break 2
        fi
    done
    sleep 10
done

echo "RUNNING physical_gpu=${gpu_id}" >"${queue_status}"
setsid env STAGE_D_GPU_ID="${gpu_id}" bash "${launcher}" >>"${queue_log}" 2>&1 &
run_pid=$!
run_pgid=$(ps -o pgid= -p "${run_pid}" | tr -d '[:space:]')
while kill -0 "${run_pid}" 2>/dev/null; do
    while IFS= read -r process_pid; do
        process_pid=$(echo "${process_pid}" | tr -d '[:space:]')
        [[ -z "${process_pid}" ]] && continue
        process_pgid=$(ps -o pgid= -p "${process_pid}" 2>/dev/null | tr -d '[:space:]' || true)
        if [[ -n "${process_pgid}" && "${process_pgid}" != "${run_pgid}" ]]; then
            printf '%s Foreign process %s appeared on GPU %s; stopping only Stage D.\n' \
                "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "${process_pid}" "${gpu_id}" >>"${queue_log}"
            kill -TERM -- "-${run_pgid}" 2>/dev/null || true
            echo "CONFLICT_ABORTED physical_gpu=${gpu_id}" >"${queue_status}"
            wait "${run_pid}" || true
            exit 31
        fi
    done < <(nvidia-smi --id="${gpu_id}" --query-compute-apps=pid --format=csv,noheader,nounits)
    sleep 5
done

set +e
wait "${run_pid}"
code=$?
set -e
if [[ "${code}" -eq 0 && -f "${output_root}/FINAL_GATE.json" ]]; then
    echo COMPLETE >"${queue_status}"
    exit 0
fi
echo "FAILED code=${code}" >"${queue_status}"
exit "${code}"
