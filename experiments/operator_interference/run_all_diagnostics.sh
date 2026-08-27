#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-${ROOT}/.venv/bin/python}"
MANIFEST="${ROOT}/model_manifest.json"

"${PYTHON}" - "${ROOT}" "${MANIFEST}" <<'PY'
import json
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
manifest = json.loads(pathlib.Path(sys.argv[2]).read_text())
if not manifest.get("revisions_frozen"):
    raise SystemExit("model revisions are not frozen")
expected = {(model["family"], pack, condition) for model in manifest["models"] for pack, conditions in {"A": "ABCDE", "B": "CD"}.items() for condition in conditions}
missing = []
for model, pack, condition in sorted(expected):
    path = root / "outputs" / "primary" / f"{model}.pack{pack}.{condition}.jsonl"
    rows = sum(1 for line in path.open(encoding="utf-8") if line.strip()) if path.exists() else 0
    if rows != 108:
        missing.append(f"{path.name}:{rows}/108")
if missing:
    raise SystemExit("primary matrix incomplete: " + ", ".join(missing))
print(f"primary preflight passed: {len(expected)} cells")
PY

free="$(nvidia-smi --id=7 --query-gpu=memory.free --format=csv,noheader,nounits | tr -d ' ')"
if [[ "${free}" -lt 22000 ]]; then
  echo "Refusing diagnostic GPU 7: ${free} MiB free." >&2
  exit 2
fi

mkdir -p "${ROOT}/logs/diagnostics"
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
  echo "DIAGNOSTIC START ${family}"
  GPU=7 MODEL="${path}" MODEL_ID="${family}" MODEL_REVISION="${revision}" PYTHON="${PYTHON}" \
    "${ROOT}/run_diagnostics_one_model.sh" > "${ROOT}/logs/diagnostics/${family}.log" 2>&1
  echo "DIAGNOSTIC COMPLETE ${family}"
done

echo "ALL DIAGNOSTICS COMPLETE"
