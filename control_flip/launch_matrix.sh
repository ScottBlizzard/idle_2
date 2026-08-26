#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:-direct}"

case "${MODE}" in
  direct|cot|bellman|local_operator|positive_operator) ;;
  *) echo "Usage: $0 {direct|cot|bellman|local_operator|positive_operator}" >&2; exit 2 ;;
esac

mkdir -p "${ROOT}/logs" "${ROOT}/outputs"

launch() {
  local gpu="$1"
  local model="$2"
  local model_id="$3"
  local batch_size="$4"
  local free_mib

  free_mib="$(nvidia-smi --id="${gpu}" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
  if [[ "${free_mib}" -lt 22000 ]]; then
    echo "SKIP ${model_id}/${MODE}: GPU ${gpu} has only ${free_mib} MiB free; no process was touched." >&2
    return 1
  fi

  echo "LAUNCH ${model_id}/${MODE} on physical GPU ${gpu} (${free_mib} MiB free)"
  nohup env \
    GPU="${gpu}" MODEL="${model}" MODEL_ID="${model_id}" MODE="${MODE}" \
    BATCH_SIZE="${batch_size}" MIN_FREE_MIB=22000 \
    "${ROOT}/run_server.sh" \
    >"${ROOT}/logs/${model_id}.${MODE}.log" 2>&1 &
  echo "$! ${model_id} ${MODE} GPU=${gpu}" >>"${ROOT}/logs/launches.tsv"
}

# Physical GPUs 0-3 stay unallocated for the user's other experiment.
launch 4 /home/ccj/soccer/ICLR/memories-not-additive/models/Qwen3.5-4B qwen35_4b 16
launch 5 /home/ccj/soccer/ICLR/memories-not-additive/models/Qwen3.5-9B qwen35_9b 8
launch 6 /home/ccj/bridgecover-aaai27/models/Qwen3-8B qwen3_8b 8
launch 7 /mnt/sdb/ccj/rr_orthkd/models/teacher_weak/Qwen2.5-Math-7B-Instruct qwen25_math7b 8

echo "All ${MODE} jobs submitted."
