#!/usr/bin/env bash
set -euo pipefail

stage_root=${STAGE_E_ROOT:-/mnt/sdb/ccj/idle_2/moe_route_noncompositionality}
repo_root=${STAGE_E_REPO:-${stage_root}/repo}
output_root=${STAGE_E_OUTPUT:-${stage_root}/results/stage_e}
cache_root=${STAGE_E_CACHE:-/mnt/sdb/ccj/hf_cache_idle_2}
gpu_candidates_text=${STAGE_E_GPU_IDS:-4 5 6 7}
idle_seconds_required=${STAGE_E_IDLE_SECONDS_REQUIRED:-180}
wait_seconds_max=${STAGE_E_WAIT_SECONDS_MAX:-0}
max_attempts=${STAGE_E_MAX_ATTEMPTS:-3}
launcher="${repo_root}/experiments/moe_route_noncompositionality/run_stage_e_4090.sh"
queue_root="${stage_root}/queue"
queue_log="${queue_root}/wait_and_run.log"
queue_status="${queue_root}/status.txt"
lock_file="${queue_root}/wait_and_run.lock"

mkdir -p "${queue_root}" "${output_root}"
exec 9>"${lock_file}"
flock -n 9 || { echo "Another Stage E queue watcher is already active." >&2; exit 30; }

log() {
    printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "${queue_log}"
}

read -r -a gpu_candidates <<< "${gpu_candidates_text}"
[[ "${#gpu_candidates[@]}" -gt 0 ]] || { echo "STAGE_E_GPU_IDS is empty." >&2; exit 2; }
declare -A seen_gpu=()
for candidate in "${gpu_candidates[@]}"; do
    [[ "${candidate}" =~ ^[4-7]$ ]] || {
        echo "Only physical GPUs 4-7 are authorized; got ${candidate}." >&2
        exit 2
    }
    [[ -z "${seen_gpu[${candidate}]:-}" ]] || {
        echo "Duplicate GPU candidate ${candidate}." >&2
        exit 2
    }
    seen_gpu[${candidate}]=1
done

wait_for_candidate_idle() {
    local waited=0
    local candidate used_mib process_count snapshot
    declare -A stable_by_gpu=()
    for candidate in "${gpu_candidates[@]}"; do stable_by_gpu[${candidate}]=0; done
    while [[ "${wait_seconds_max}" -eq 0 || "${waited}" -lt "${wait_seconds_max}" ]]; do
        snapshot=""
        for candidate in "${gpu_candidates[@]}"; do
            used_mib=$(nvidia-smi --id="${candidate}" --query-gpu=memory.used --format=csv,noheader,nounits | tr -d ' ')
            process_count=$(nvidia-smi --id="${candidate}" --query-compute-apps=pid --format=csv,noheader,nounits | sed '/^[[:space:]]*$/d' | wc -l)
            if [[ "${used_mib}" -le 512 && "${process_count}" -eq 0 ]]; then
                stable_by_gpu[${candidate}]=$((stable_by_gpu[${candidate}] + 10))
            else
                stable_by_gpu[${candidate}]=0
            fi
            snapshot+=" gpu${candidate}:memory=${used_mib},processes=${process_count},stable=${stable_by_gpu[${candidate}]}"
            if [[ "${stable_by_gpu[${candidate}]}" -ge "${idle_seconds_required}" ]]; then
                gpu_id=${candidate}
                log "Physical GPU ${gpu_id} has been exclusively idle for ${stable_by_gpu[${candidate}]}s."
                return 0
            fi
        done
        if (( waited % 60 == 0 )); then
            log "WAITING candidates=${gpu_candidates_text} waited_seconds=${waited}${snapshot}"
        fi
        sleep 10
        waited=$((waited + 10))
    done
    return 1
}

foreign_pid_on_target() {
    local allowed_pgid=$1
    local pid
    local pgid
    while IFS= read -r pid; do
        pid=$(echo "${pid}" | tr -d '[:space:]')
        [[ -z "${pid}" ]] && continue
        pgid=$(ps -o pgid= -p "${pid}" 2>/dev/null | tr -d '[:space:]' || true)
        if [[ -n "${pgid}" && "${pgid}" != "${allowed_pgid}" ]]; then
            echo "${pid}"
            return 0
        fi
    done < <(nvidia-smi --id="${gpu_id}" --query-compute-apps=pid --format=csv,noheader,nounits)
    return 1
}

if [[ -f "${output_root}/stage_e_summary.json" ]]; then
    log "Summary already exists; refusing to overwrite it."
    echo COMPLETE >"${queue_status}"
    exit 0
fi

echo WAITING >"${queue_status}"
attempt=0
while [[ "${attempt}" -lt "${max_attempts}" ]]; do
    if ! wait_for_candidate_idle; then
        log "Timed out waiting for an idle GPU among ${gpu_candidates_text}."
        echo WAIT_TIMEOUT >"${queue_status}"
        exit 31
    fi
    attempt=$((attempt + 1))
    log "Launching Stage E attempt ${attempt} on physical GPU ${gpu_id}."
    echo "RUNNING attempt=${attempt} physical_gpu=${gpu_id}" >"${queue_status}"
    setsid env \
        STAGE_E_ROOT="${stage_root}" \
        STAGE_E_REPO="${repo_root}" \
        STAGE_E_OUTPUT="${output_root}" \
        STAGE_E_CACHE="${cache_root}" \
        STAGE_E_GPU_ID="${gpu_id}" \
        bash "${launcher}" >>"${queue_log}" 2>&1 &
    stage_pid=$!
    stage_pgid=$(ps -o pgid= -p "${stage_pid}" | tr -d '[:space:]')
    conflict=0
    while kill -0 "${stage_pid}" 2>/dev/null; do
        if foreign=$(foreign_pid_on_target "${stage_pgid}"); then
            log "Foreign GPU process ${foreign} appeared; terminating Stage E attempt ${attempt}."
            kill -TERM -- "-${stage_pgid}" 2>/dev/null || true
            conflict=1
            break
        fi
        sleep 5
    done
    set +e
    wait "${stage_pid}"
    stage_code=$?
    set -e
    if [[ "${conflict}" -eq 1 ]]; then
        echo "CONFLICT_ABORTED attempt=${attempt}" >"${queue_status}"
        sleep 30
        continue
    fi
    if [[ "${stage_code}" -eq 20 ]]; then
        log "GPU ${gpu_id} lost exclusivity during launch; retrying candidate selection."
        echo "START_RACE_ABORTED attempt=${attempt}" >"${queue_status}"
        sleep 30
        continue
    fi
    if [[ "${stage_code}" -eq 0 && -f "${output_root}/stage_e_summary.json" ]]; then
        log "Stage E completed without a foreign GPU process."
        echo COMPLETE >"${queue_status}"
        exit 0
    fi
    log "Stage E exited with code ${stage_code}; not retrying an implementation or gate failure."
    echo "FAILED code=${stage_code}" >"${queue_status}"
    exit "${stage_code}"
done

log "Exhausted ${max_attempts} conflict retries."
echo CONFLICT_RETRIES_EXHAUSTED >"${queue_status}"
exit 32
