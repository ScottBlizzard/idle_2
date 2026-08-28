#!/usr/bin/env bash
set -euo pipefail

cache_root=${1:-/mnt/sdb/ccj/hf_cache_idle_2}
repo_id=allenai/OLMoE-1B-7B-0924-Instruct
repo_cache="${cache_root}/models--allenai--OLMoE-1B-7B-0924-Instruct"
snapshot_id=7f1c97f440f06ce36705e4f2b843edb5925f4498
blob_root="${repo_cache}/blobs"
snapshot_root="${repo_cache}/snapshots/${snapshot_id}"
endpoint=${HF_ENDPOINT:-https://hf-mirror.com}

mkdir -p "${blob_root}" "${snapshot_root}"

download_one() {
    local filename=$1
    local digest=$2
    local expected_size=$3
    local final_path="${blob_root}/${digest}"
    local partial_path
    local actual_size
    local actual_digest

    if [[ -f "${final_path}" ]]; then
        actual_size=$(stat -c %s "${final_path}")
        actual_digest=$(sha256sum "${final_path}" | awk '{print $1}')
        [[ "${actual_size}" == "${expected_size}" && "${actual_digest}" == "${digest}" ]] || {
            echo "Existing final blob failed verification: ${filename}" >&2
            return 2
        }
    else
        partial_path=$(find "${blob_root}" -maxdepth 1 -type f -name "${digest}.*.incomplete" \
            -printf '%s %p\n' | sort -nr | head -1 | cut -d' ' -f2-)
        if [[ -z "${partial_path}" ]]; then
            partial_path="${blob_root}/${digest}.manual.incomplete"
            : >"${partial_path}"
        fi
        curl --fail --location --silent --show-error --retry 8 --continue-at - \
            --output "${partial_path}" \
            "${endpoint}/${repo_id}/resolve/main/${filename}"
        actual_size=$(stat -c %s "${partial_path}")
        [[ "${actual_size}" == "${expected_size}" ]] || {
            echo "Size mismatch for ${filename}: ${actual_size} != ${expected_size}" >&2
            return 3
        }
        actual_digest=$(sha256sum "${partial_path}" | awk '{print $1}')
        [[ "${actual_digest}" == "${digest}" ]] || {
            echo "SHA-256 mismatch for ${filename}: ${actual_digest} != ${digest}" >&2
            return 4
        }
        mv "${partial_path}" "${final_path}"
    fi
    ln -sfn "../../blobs/${digest}" "${snapshot_root}/${filename}"
    echo "VERIFIED ${filename} ${expected_size} ${digest}"
}

download_one model-00001-of-00003.safetensors \
    6c79ac0487c3f23e8ee3d38752197d1e4a1a39d6c1438ec5fd7862874bb19321 4997744872 &
pid1=$!
download_one model-00002-of-00003.safetensors \
    b58ca7a9f28f35d76b56b0ec40fc46c356fd84ccf078083b251a3ad6a2da9a35 4997235176 &
pid2=$!
download_one model-00003-of-00003.safetensors \
    e93653ed509223e63eabae6f72ac8ea5a41115c5c7785574b9b2068ca0961c45 3843741912 &
pid3=$!

failed=0
wait "${pid1}" || failed=1
wait "${pid2}" || failed=1
wait "${pid3}" || failed=1
[[ "${failed}" -eq 0 ]] || exit 5
echo "OLMOE_CACHE_READY ${snapshot_root}"
