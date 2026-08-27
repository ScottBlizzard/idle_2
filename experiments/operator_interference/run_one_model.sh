#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-${ROOT}/.venv/bin/python}"
GPU="${GPU:?Set the physical GPU index.}"
MODEL="${MODEL:?Set the local model directory.}"
MODEL_ID="${MODEL_ID:?Set the frozen model family identifier.}"
MODEL_REVISION="${MODEL_REVISION:?Set the frozen model revision.}"
DATA="${DATA:-${ROOT}/data/confirmatory.jsonl}"
OUTPUT_ROOT="${OUTPUT_ROOT:-${ROOT}/outputs/primary}"
MIN_FREE_MIB="${MIN_FREE_MIB:-22000}"

FREE_MIB="$(nvidia-smi --id="${GPU}" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
if [[ "${FREE_MIB}" -lt "${MIN_FREE_MIB}" ]]; then
  echo "Refusing GPU ${GPU}: only ${FREE_MIB} MiB free. Existing processes are untouched." >&2
  exit 2
fi

mkdir -p "${OUTPUT_ROOT}" "${ROOT}/logs"
echo "START ${MODEL_ID} on physical GPU ${GPU}; free=${FREE_MIB} MiB"

run_cell() {
  local pack="$1"
  local condition="$2"
  local output="${OUTPUT_ROOT}/${MODEL_ID}.pack${pack}.${condition}.jsonl"
  echo "CELL ${MODEL_ID} Pack ${pack} ${condition}"
  CUDA_VISIBLE_DEVICES="${GPU}" \
  HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false \
  PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  "${PYTHON}" "${ROOT}/run_model.py" \
    --data "${DATA}" \
    --model "${MODEL}" \
    --model-id "${MODEL_ID}" \
    --model-revision "${MODEL_REVISION}" \
    --pack "${pack}" \
    --condition "${condition}" \
    --output "${output}"
}

for condition in A B C D E; do
  run_cell A "${condition}"
done
for condition in C D; do
  run_cell B "${condition}"
done

echo "COMPLETE ${MODEL_ID}"
