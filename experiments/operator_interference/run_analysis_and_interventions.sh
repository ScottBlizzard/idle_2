#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-${ROOT}/.venv/bin/python}"
MANIFEST="${ROOT}/model_manifest.json"
DATA="${ROOT}/data/confirmatory.jsonl"
RESULTS="${ROOT}/results"

mkdir -p "${RESULTS}/primary" "${RESULTS}/diagnostics" "${RESULTS}/interventions"

"${PYTHON}" "${ROOT}/evaluate.py" \
  --data "${DATA}" \
  --predictions "${ROOT}/outputs/primary/*.jsonl" \
  --model-manifest "${MANIFEST}" \
  --output-dir "${RESULTS}/primary"

"${PYTHON}" "${ROOT}/compare_diagnostics.py" \
  --data "${DATA}" \
  --primary "${ROOT}/outputs/primary/*.jsonl" \
  --replay "${ROOT}/outputs/replay/*.jsonl" \
  --template "${ROOT}/outputs/template_plain/*.jsonl" \
  --unconstrained "${ROOT}/outputs/unconstrained/*.jsonl" \
  --output-dir "${RESULTS}/diagnostics"

"${PYTHON}" "${ROOT}/build_intervention_cases.py" \
  --data "${DATA}" \
  --predictions "${ROOT}/outputs/primary/*.jsonl" \
  --output "${RESULTS}/interventions/cases.jsonl"

free="$(nvidia-smi --id=7 --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
if [[ "${free}" -lt 22000 ]]; then
  echo "Refusing intervention GPU 7: ${free} MiB free." >&2
  exit 2
fi

"${PYTHON}" - "${MANIFEST}" "${ROOT}" <<'PY' | while IFS=$'\t' read -r family path revision; do
import json
import pathlib
import sys

manifest = json.loads(pathlib.Path(sys.argv[1]).read_text())
root = pathlib.Path(sys.argv[2])
for model in manifest["models"]:
    path = pathlib.Path(model["local_dir"])
    if not path.is_absolute():
        path = root / path
    print(model["family"], path, model["revision"], sep="\t")
PY
  CUDA_VISIBLE_DEVICES=7 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false \
    "${PYTHON}" "${ROOT}/run_intervention.py" \
      --cases "${RESULTS}/interventions/cases.jsonl" \
      --model "${path}" --model-id "${family}" --model-revision "${revision}" \
      --output "${ROOT}/outputs/interventions/${family}.jsonl"
done

"${PYTHON}" "${ROOT}/evaluate_intervention.py" \
  --predictions "${ROOT}/outputs/interventions/*.jsonl" \
  --output-dir "${RESULTS}/interventions"

"${PYTHON}" "${ROOT}/finalize_gate.py" \
  --summary "${RESULTS}/primary/summary.csv" \
  --contrasts "${RESULTS}/primary/contrasts.csv" \
  --process "${RESULTS}/primary/process_metrics.csv" \
  --pair-results "${RESULTS}/primary/pair_results.csv" \
  --replay-summary "${RESULTS}/diagnostics/replay_summary.csv" \
  --diagnostic-summary "${RESULTS}/diagnostics/format_template_summary.csv" \
  --intervention-summary "${RESULTS}/interventions/intervention_summary.csv" \
  --benchmark-audit "${ROOT}/data/confirmatory.audit.json" \
  --model-manifest "${MANIFEST}" \
  --output "${RESULTS}/FINAL_GATE.json"

echo "ANALYSIS AND BINDING GATE COMPLETE"
