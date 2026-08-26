#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-/home/ccj/soccer/ICLR/memories-not-additive/.conda/bin/python}"
GPU="${GPU:?Set GPU to an explicitly reserved physical GPU index.}"
MODEL="${MODEL:?Set MODEL to a local model directory.}"
MODEL_ID="${MODEL_ID:?Set MODEL_ID.}"
MODE="${MODE:-direct}"
BATCH_SIZE="${BATCH_SIZE:-8}"
MIN_FREE_MIB="${MIN_FREE_MIB:-22000}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-}"
EXTRA_ARGS=()
if [[ -n "${MAX_NEW_TOKENS}" ]]; then
  EXTRA_ARGS+=(--max-new-tokens "${MAX_NEW_TOKENS}")
fi

FREE_MIB="$(nvidia-smi --id="${GPU}" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
if [[ "${FREE_MIB}" -lt "${MIN_FREE_MIB}" ]]; then
  echo "Refusing GPU ${GPU}: only ${FREE_MIB} MiB free; existing jobs are untouched." >&2
  exit 2
fi

mkdir -p "${ROOT}/outputs" "${ROOT}/logs"
echo "Using physical GPU ${GPU} (${FREE_MIB} MiB free) for ${MODEL_ID}/${MODE}."
cd "${ROOT}"
CUDA_VISIBLE_DEVICES="${GPU}" \
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false \
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
"${PYTHON}" run_model.py \
  --data data/control_flip.jsonl \
  --model "${MODEL}" \
  --model-id "${MODEL_ID}" \
  --prompt-mode "${MODE}" \
  --batch-size "${BATCH_SIZE}" \
  --output "outputs/${MODEL_ID}.${MODE}.jsonl" \
  "${EXTRA_ARGS[@]}"
