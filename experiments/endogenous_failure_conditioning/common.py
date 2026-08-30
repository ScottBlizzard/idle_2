#!/usr/bin/env python3
"""Deterministic mechanics shared by the crossed-repair pilot."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parent


def load_config(path: Path | None = None) -> dict[str, Any]:
    resolved = path or ROOT / "FROZEN_CONFIG.json"
    config = json.loads(resolved.read_text(encoding="utf-8"))
    if config.get("protocol_version") != "1.0-crossed-repair-pilot":
        raise RuntimeError("Unexpected crossed-repair protocol version")
    return config


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Invalid JSON at {path}:{line_number}") from exc


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(canonical_json(dict(row)) + "\n")
    temporary.replace(path)


def problem_key(domain: str, dataset_index: int) -> str:
    return f"{domain}:{int(dataset_index)}"


def case_id(error_id: str, corrector: str, wrapper: str) -> str:
    return sha256_text(canonical_json([error_id, corrector, wrapper]))


SYSTEM_PROMPT = (
    "You are a careful mathematical reasoner. Check the supplied solution rather than "
    "trusting it. Return a corrected derivation and end with exactly "
    "Final answer: \\boxed{ANSWER}."
)


def build_messages(record: Mapping[str, Any], wrapper: str) -> list[dict[str, str]]:
    question = str(record["question"])
    error = str(record["error_response"])
    if wrapper == "external_neutral":
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Problem:\n" + question + "\n\n"
                    "Proposed solution from an unspecified source:\n" + error + "\n\n"
                    "Check the proposed solution, repair every error you find, and give "
                    "the final answer in the required format."
                ),
            },
        ]
    if wrapper == "assistant_history":
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Problem:\n" + question + "\n\nSolve it carefully and give the final answer."
                ),
            },
            {"role": "assistant", "content": error},
            {
                "role": "user",
                "content": (
                    "Check the preceding solution, repair every error you find, and give "
                    "the final answer in the required format."
                ),
            },
        ]
    raise ValueError(f"Unknown wrapper: {wrapper}")


def prompt_payload_hash(record: Mapping[str, Any], wrapper: str) -> str:
    return sha256_text(canonical_json(build_messages(record, wrapper)))
