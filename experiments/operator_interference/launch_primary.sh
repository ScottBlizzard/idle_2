#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="${ROOT}/model_manifest.json"
PYTHON="${PYTHON:-${ROOT}/.venv/bin/python}"

if [[ ! -f "${ROOT}/data/confirmatory.jsonl" ]]; then
  echo "Confirmatory data are absent. Commit the preregistration before generating them." >&2
  exit 2
fi
EXPECTED_DATA_SHA256="0270bf2c1f8dbe1a791a9935b08b9751a698902837452108cdc75fb1e804a688"
ACTUAL_DATA_SHA256="$(sha256sum "${ROOT}/data/confirmatory.jsonl" | awk '{print $1}')"
if [[ "${ACTUAL_DATA_SHA256}" != "${EXPECTED_DATA_SHA256}" ]]; then
  echo "Refusing launch: confirmatory data hash is ${ACTUAL_DATA_SHA256}, expected ${EXPECTED_DATA_SHA256}." >&2
  exit 2
fi
if [[ ! -x "${PYTHON}" ]]; then
  echo "Run setup_remote.sh first." >&2
  exit 2
fi

"${PYTHON}" - "${MANIFEST}" "${ROOT}" <<'PY'
import json
import pathlib
import sys

manifest = json.loads(pathlib.Path(sys.argv[1]).read_text())
root = pathlib.Path(sys.argv[2])
if not manifest.get("revisions_frozen"):
    raise SystemExit("model revisions are not frozen")
for model in manifest["models"]:
    path = pathlib.Path(model["local_dir"])
    if not path.is_absolute():
        path = root / path
    if not (path / "config.json").exists():
        raise SystemExit(f"missing model: {path}")
PY

for gpu in 0 1 2 3 4 5 6; do
  free="$(nvidia-smi --id="${gpu}" --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
  if [[ "${free}" -lt 22000 ]]; then
    echo "Refusing launch: physical GPU ${gpu} has only ${free} MiB free. No jobs started." >&2
    exit 2
  fi
done

mkdir -p "${ROOT}/logs" "${ROOT}/outputs/primary"
: > "${ROOT}/logs/primary_launches.tsv"

"${PYTHON}" - "${MANIFEST}" "${ROOT}" <<'PY' | while IFS=$'\t' read -r gpu family path revision; do
import json
import pathlib
import sys

manifest = json.loads(pathlib.Path(sys.argv[1]).read_text())
root = pathlib.Path(sys.argv[2])
for model in manifest["models"]:
    path = pathlib.Path(model["local_dir"])
    if not path.is_absolute():
        path = root / path
    print(model["gpu"], model["family"], path, model["revision"], sep="\t")
PY
  log="${ROOT}/logs/${family}.primary.log"
  nohup env \
    GPU="${gpu}" MODEL="${path}" MODEL_ID="${family}" MODEL_REVISION="${revision}" \
    PYTHON="${PYTHON}" \
    "${ROOT}/run_one_model.sh" > "${log}" 2>&1 &
  pid=$!
  printf '%s\t%s\t%s\t%s\n' "${pid}" "${family}" "${gpu}" "${log}" >> "${ROOT}/logs/primary_launches.tsv"
  echo "LAUNCHED ${family} pid=${pid} gpu=${gpu}"
done
