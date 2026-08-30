#!/usr/bin/env python3
"""Acquire frozen public traces and build the outcome-blind common error bank."""

from __future__ import annotations

import argparse
import http.client
import json
import shutil
import urllib.request
from collections import defaultdict
from pathlib import Path
from statistics import median
from typing import Any

import numpy as np

from common import (
    canonical_json,
    load_config,
    problem_key,
    sha256_file,
    sha256_text,
    write_jsonl,
)


def download(
    repo_id: str,
    revision: str,
    remote_path: str,
    target: Path,
    expected_size: int,
    expected_sha256: str,
) -> None:
    if target.exists() and target.stat().st_size == expected_size:
        if sha256_file(target) == expected_sha256:
            return
    target.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://huggingface.co/datasets/{repo_id}/resolve/{revision}/{remote_path}"
    temporary = target.with_suffix(target.suffix + ".partial")
    if target.exists():
        target.replace(temporary)

    # The official client handles Xet-backed CDN retries and content-addressed
    # caching more reliably than a raw HTTP stream. Keep the range implementation
    # below as a dependency-free fallback for minimal server environments.
    try:
        from huggingface_hub import hf_hub_download

        local_root = target
        for _ in Path(remote_path).parts:
            local_root = local_root.parent
        resolved = Path(
            hf_hub_download(
                repo_id=repo_id,
                filename=remote_path,
                repo_type="dataset",
                revision=revision,
                local_dir=local_root,
            )
        )
        if resolved.stat().st_size == expected_size and sha256_file(resolved) == expected_sha256:
            if resolved != target:
                shutil.copy2(resolved, target)
            return
    except (ImportError, OSError, RuntimeError, ValueError):
        pass

    for attempt in range(8):
        current = temporary.stat().st_size if temporary.exists() else 0
        if current > expected_size:
            raise RuntimeError(f"Partial download exceeds frozen size: {temporary}")
        if current == expected_size:
            actual = sha256_file(temporary)
            if actual != expected_sha256:
                raise RuntimeError(
                    f"Complete-size download has wrong hash for {remote_path}: {actual}"
                )
            temporary.replace(target)
            return
        request = urllib.request.Request(url, headers={"Range": f"bytes={current}-"})
        try:
            with urllib.request.urlopen(request, timeout=120) as source:
                append = current > 0 and source.status == 206
                mode = "ab" if append else "wb"
                if current > 0 and not append:
                    current = 0
                with temporary.open(mode) as sink:
                    shutil.copyfileobj(source, sink, length=1024 * 1024)
        except (http.client.IncompleteRead, TimeoutError, OSError):
            pass
    raise RuntimeError(
        f"Download remained incomplete after retries: {remote_path} "
        f"({temporary.stat().st_size if temporary.exists() else 0}/{expected_size})"
    )


def verify_source(path: Path, expected: str) -> None:
    actual = sha256_file(path)
    if actual != expected:
        raise RuntimeError(f"Source hash mismatch for {path}: {actual} != {expected}")


def load_difficulty(path: Path) -> dict[str, dict[tuple[str, int], float]]:
    raw = np.load(path, allow_pickle=True).item()
    return {
        str(model): {(str(source), int(index)): float(score) for source, index, score in rows}
        for model, rows in raw.items()
    }


def rank_bins(values: dict[str, float], bin_count: int = 4) -> dict[str, int]:
    ordered = sorted(values, key=lambda key: (values[key], key))
    size = max(1, len(ordered))
    return {key: min(bin_count - 1, index * bin_count // size) for index, key in enumerate(ordered)}


def stratified_problem_sample(
    candidates: dict[str, dict[str, dict[str, Any]]],
    difficulties: dict[str, dict[tuple[str, int], float]],
    model_config: dict[str, Any],
    domain_source: str,
    count: int,
    seed: int,
) -> list[str]:
    aggregate_difficulty: dict[str, float] = {}
    aggregate_length: dict[str, float] = {}
    for key, by_model in candidates.items():
        dataset_index = int(next(iter(by_model.values()))["dataset_idx"])
        aggregate_difficulty[key] = float(
            np.mean(
                [
                    difficulties[model_config[model_key]["hf_id"]][
                        (domain_source, dataset_index)
                    ]
                    for model_key in model_config
                ]
            )
        )
        aggregate_length[key] = float(
            median(len(by_model[model_key]["response"]) for model_key in model_config)
        )
    difficulty_bin = rank_bins(aggregate_difficulty)
    length_bin = rank_bins(aggregate_length)
    strata: dict[tuple[int, int], list[str]] = defaultdict(list)
    for key in candidates:
        strata[(difficulty_bin[key], length_bin[key])].append(key)
    for stratum, keys in strata.items():
        keys.sort(key=lambda key: sha256_text(f"{seed}|{stratum}|{key}"))

    selected: list[str] = []
    while len(selected) < count:
        progressed = False
        for stratum in sorted(strata):
            keys = strata[stratum]
            if keys and len(selected) < count:
                selected.append(keys.pop(0))
                progressed = True
        if not progressed:
            break
    if len(selected) < count:
        raise RuntimeError(f"Only {len(selected)} common problems survive; need {count}")
    return sorted(selected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()

    config = load_config(args.config)
    dataset = config["dataset"]
    source_root = args.cache / dataset["revision"]
    difficulty_path = source_root / dataset["difficulty_path"]
    download(
        dataset["repo_id"], dataset["revision"], dataset["difficulty_path"],
        difficulty_path, int(dataset["difficulty_size"]), dataset["difficulty_sha256"]
    )
    verify_source(difficulty_path, dataset["difficulty_sha256"])

    source_paths: dict[str, Path] = {}
    for model_key, model in config["models"].items():
        path = source_root / model["source_path"]
        download(
            dataset["repo_id"], dataset["revision"], model["source_path"], path,
            int(model["source_size"]), model["source_sha256"]
        )
        verify_source(path, model["source_sha256"])
        source_paths[model_key] = path

    difficulty = load_difficulty(difficulty_path)
    by_domain_model: dict[str, dict[str, dict[str, list[dict[str, Any]]]]] = {
        domain: {model_key: defaultdict(list) for model_key in config["models"]}
        for domain in config["domains"]
    }
    source_to_domain = {source: domain for domain, source in config["domains"].items()}
    for model_key, path in source_paths.items():
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                row = json.loads(line)
                domain = source_to_domain.get(str(row.get("dataset_source")))
                if domain is None or row.get("label") is not False:
                    continue
                response = str(row.get("response") or "")
                if not response or len(response) > int(config["max_error_characters"]):
                    continue
                key = problem_key(domain, int(row["dataset_idx"]))
                by_domain_model[domain][model_key][key].append(row)

    bank: list[dict[str, Any]] = []
    selection_summary: dict[str, Any] = {}
    for domain, domain_source in config["domains"].items():
        common = set.intersection(
            *(set(by_domain_model[domain][model_key]) for model_key in config["models"])
        )
        candidates: dict[str, dict[str, dict[str, Any]]] = {}
        missing_public_difficulty = 0
        for key in sorted(common):
            chosen: dict[str, dict[str, Any]] = {}
            for model_key in config["models"]:
                rows = by_domain_model[domain][model_key][key]
                rows.sort(
                    key=lambda row: sha256_text(
                        f"{config['seed']}|{model_key}|{row['id']}|{row['response']}"
                    )
                )
                chosen[model_key] = rows[0]
            questions = {str(row["question"]) for row in chosen.values()}
            golds = {str(row["gold_answer"]) for row in chosen.values()}
            dataset_index = int(next(iter(chosen.values()))["dataset_idx"])
            has_public_difficulty = all(
                (domain_source, dataset_index)
                in difficulty[config["models"][model_key]["hf_id"]]
                for model_key in config["models"]
            )
            if not has_public_difficulty:
                missing_public_difficulty += 1
            elif len(questions) == 1 and len(golds) == 1:
                candidates[key] = chosen

        required = int(config["problems_per_domain"])
        if len(candidates) < int(config["minimum_problems_per_domain"]):
            raise RuntimeError(
                f"UNDERPOWERED {domain}: {len(candidates)} common problems below minimum"
            )
        selected = stratified_problem_sample(
            candidates,
            difficulty,
            config["models"],
            domain_source,
            min(required, len(candidates)),
            int(config["seed"]),
        )
        selection_summary[domain] = {
            "raw_common_problems": len(common),
            "excluded_missing_public_difficulty": missing_public_difficulty,
            "common_candidate_problems": len(candidates),
            "selected_problems": len(selected),
        }
        for key in selected:
            for model_key, row in candidates[key].items():
                error_text = str(row["response"])
                error_id = sha256_text(canonical_json([domain, key, model_key, row["id"]]))
                bank.append(
                    {
                        "error_id": error_id,
                        "domain": domain,
                        "problem_key": key,
                        "dataset_source": domain_source,
                        "dataset_idx": int(row["dataset_idx"]),
                        "source_id": str(row["id"]),
                        "generator_key": model_key,
                        "generator_family": config["models"][model_key]["family"],
                        "generator_hf_id": config["models"][model_key]["hf_id"],
                        "question": str(row["question"]),
                        "error_response": error_text,
                        "error_sha256": sha256_text(error_text),
                        "gold_answer": str(row["gold_answer"]),
                        "source_extracted_answer": row.get("extract_gen_answer"),
                        "generator_difficulty": difficulty[
                            config["models"][model_key]["hf_id"]
                        ][(domain_source, int(row["dataset_idx"]))],
                        "response_characters": len(error_text),
                    }
                )

    bank.sort(key=lambda row: (row["domain"], row["problem_key"], row["generator_key"]))
    output = args.output
    output.mkdir(parents=True, exist_ok=False)
    bank_path = output / "error_bank.jsonl"
    write_jsonl(bank_path, bank)
    manifest = {
        "status": "ERROR_BANK_FROZEN",
        "config_sha256": sha256_file(args.config or Path(__file__).with_name("FROZEN_CONFIG.json")),
        "dataset_revision": dataset["revision"],
        "source_sha256": {
            model_key: sha256_file(path) for model_key, path in source_paths.items()
        },
        "difficulty_sha256": sha256_file(difficulty_path),
        "selection": selection_summary,
        "error_count": len(bank),
        "error_bank_sha256": sha256_file(bank_path),
    }
    (output / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
