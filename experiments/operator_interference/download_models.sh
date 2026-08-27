#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HF_BIN="${HF_BIN:-/home/ccj/soccer/ICLR/memories-not-additive/.conda/bin/hf}"
export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
export HF_HOME="${HF_HOME:-/mnt/sdb/ccj/hf_cache_idle2}"

mkdir -p "${ROOT}/models" "${ROOT}/logs"

download() {
  local repo="$1"
  local directory="$2"
  shift 2
  echo "DOWNLOAD ${repo} -> ${directory}"
  "${HF_BIN}" download "${repo}" --local-dir "${ROOT}/models/${directory}" "$@"
}

download unsloth/Meta-Llama-3.1-8B-Instruct llama31_8b
download unsloth/gemma-2-9b-it gemma2_9b
download mistralai/Mistral-7B-Instruct-v0.3 mistral7b_v03 --exclude consolidated.safetensors
download microsoft/Phi-4-mini-instruct phi4_mini
download allenai/OLMo-2-1124-7B-Instruct olmo2_7b
download ibm-granite/granite-3.1-8b-instruct granite31_8b

echo "All model downloads completed."
