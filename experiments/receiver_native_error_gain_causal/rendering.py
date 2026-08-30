#!/usr/bin/env python3
"""Deterministic whitespace-only renderings for the causal error-gain test."""

from __future__ import annotations

import re
from typing import Any


VARIANT_SPECS: tuple[dict[str, Any], ...] = (
    {"id": "raw", "raw": True},
    {"id": "flat", "line": " ", "sentence": " ", "indent": 0},
    {"id": "line_single", "line": "\n", "sentence": " ", "indent": 0},
    {"id": "line_blank", "line": "\n\n", "sentence": " ", "indent": 0},
    {"id": "sentence_single", "line": " ", "sentence": "\n", "indent": 0},
    {"id": "sentence_blank", "line": " ", "sentence": "\n\n", "indent": 0},
    {"id": "steps_single", "line": "\n", "sentence": "\n", "indent": 0},
    {"id": "line_blank_steps_single", "line": "\n\n", "sentence": "\n", "indent": 0},
    {"id": "line_single_steps_blank", "line": "\n", "sentence": "\n\n", "indent": 0},
    {"id": "line_indent2", "line": "\n", "sentence": " ", "indent": 2},
    {"id": "steps_indent2", "line": "\n", "sentence": "\n", "indent": 2},
    {"id": "steps_indent4", "line": "\n", "sentence": "\n", "indent": 4}
)


def non_whitespace(text: str) -> str:
    return re.sub(r"\s+", "", text)


def _is_sentence_boundary(previous: str) -> bool:
    return bool(re.search(r"[.!?;:]$", previous)) and not bool(
        re.search(r"\d\.$", previous)
    )


def render(trace: str, spec: dict[str, Any]) -> str:
    if spec.get("raw"):
        return trace
    parts = re.split(r"(\s+)", trace.strip())
    output: list[str] = []
    previous_nonspace = ""
    for part in parts:
        if not part:
            continue
        if not part.isspace():
            output.append(part)
            previous_nonspace = part
            continue
        if "\n" in part or "\r" in part:
            replacement = str(spec["line"])
        elif _is_sentence_boundary(previous_nonspace):
            replacement = str(spec["sentence"])
        else:
            replacement = " "
        if "\n" in replacement and int(spec.get("indent", 0)):
            replacement += " " * int(spec["indent"])
        output.append(replacement)
    return "".join(output).strip()


def render_variants(trace: str) -> list[dict[str, str]]:
    source_key = non_whitespace(trace)
    seen: set[str] = set()
    rows: list[dict[str, str]] = []
    for spec in VARIANT_SPECS:
        text = render(trace, spec)
        if non_whitespace(text) != source_key:
            raise RuntimeError(f"Non-whitespace invariant failed for {spec['id']}")
        if text in seen:
            continue
        seen.add(text)
        rows.append({"variant_id": str(spec["id"]), "rendered_trace": text})
    return rows

