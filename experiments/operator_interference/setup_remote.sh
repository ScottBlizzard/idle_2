#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_PYTHON="${BASE_PYTHON:-/home/ccj/soccer/ICLR/memories-not-additive/.conda/bin/python}"
VENV="${VENV:-${ROOT}/.venv}"

if [[ ! -x "${VENV}/bin/python" ]]; then
  "${BASE_PYTHON}" -m venv --system-site-packages "${VENV}"
fi

"${VENV}/bin/python" -m pip install --disable-pip-version-check \
  "lm-format-enforcer==0.11.2"

"${VENV}/bin/python" - <<'PY'
import lmformatenforcer
import scipy
import torch
import transformers

print("lm-format-enforcer", getattr(lmformatenforcer, "__version__", "0.11.2"))
print("scipy", scipy.__version__)
print("torch", torch.__version__)
print("transformers", transformers.__version__)
PY
