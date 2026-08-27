#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-${ROOT}/.venv/bin/python}"
GPU="${GPU:-7}"
MODEL="${MODEL:?Set the model path.}"
MODEL_ID="${MODEL_ID:?Set the model identifier.}"
MODEL_REVISION="${MODEL_REVISION:?Set the frozen revision.}"
DATA="${ROOT}/data/confirmatory.jsonl"

free="$(nvidia-smi --id="${GPU}" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
if [[ "${free}" -lt 22000 ]]; then
  echo "Refusing diagnostic GPU ${GPU}: ${free} MiB free." >&2
  exit 2
fi

run_cell() {
  local pack="$1" condition="$2" output="$3" ids="$4" template="$5" unconstrained="$6"
  local extra=()
  if [[ "${unconstrained}" == "yes" ]]; then extra+=(--unconstrained); fi
  CUDA_VISIBLE_DEVICES="${GPU}" \
  HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false \
  PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  "${PYTHON}" "${ROOT}/run_model.py" \
    --data "${DATA}" --model "${MODEL}" --model-id "${MODEL_ID}" \
    --model-revision "${MODEL_REVISION}" --pack "${pack}" --condition "${condition}" \
    --ids-file "${ids}" --template-mode "${template}" --reverse-order \
    --output "${output}" "${extra[@]}"
}

mkdir -p "${ROOT}/outputs/replay" "${ROOT}/outputs/template_plain" "${ROOT}/outputs/unconstrained"
replay_ids="${ROOT}/data/diagnostics/replay_6_pairs.txt"
template_ids="${ROOT}/data/diagnostics/template_12_pairs.txt"

for condition in A B C D E; do
  run_cell A "${condition}" "${ROOT}/outputs/replay/${MODEL_ID}.packA.${condition}.jsonl" "${replay_ids}" native no
done
for condition in C D; do
  run_cell B "${condition}" "${ROOT}/outputs/replay/${MODEL_ID}.packB.${condition}.jsonl" "${replay_ids}" native no
done
for condition in C D; do
  run_cell A "${condition}" "${ROOT}/outputs/template_plain/${MODEL_ID}.packA.${condition}.jsonl" "${template_ids}" plain no
  run_cell A "${condition}" "${ROOT}/outputs/unconstrained/${MODEL_ID}.packA.${condition}.jsonl" "${template_ids}" native yes
done

echo "DIAGNOSTICS COMPLETE ${MODEL_ID}"
