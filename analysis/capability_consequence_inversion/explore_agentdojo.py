"""Outcome-blind trajectory-structure audit for AgentDojo runs.

This script intentionally uses only the existing utility/security labels and a
predeclared tool-side-effect dictionary.  It does not use an LLM judge and does
not infer scientific "harm" from free-form text.

The main matched analysis asks: among the exact task/attack instances on which
both models fail utility, which model more often crosses an external-state
mutation boundary?  This is an exploratory falsifier, not a confirmatory test.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


# Frozen before the matched-pair analysis.  These tools write externally visible
# state.  The label is deliberately "mutation", not "harm" or "irreversibility".
MUTATING_TOOLS = {
    "add_calendar_event_participants",
    "add_user_to_channel",
    "append_to_file",
    "create_calendar_event",
    "create_file",
    "delete_email",
    "delete_file",
    "invite_user_to_slack",
    "post_webpage",
    "remove_user_from_slack",
    "reschedule_calendar_event",
    "reserve_hotel",
    "send_channel_message",
    "send_direct_message",
    "send_email",
    "send_money",
    "update_password",
    "update_scheduled_transaction",
    "update_user_info",
}

FUNCTION_PATTERN = r'"function": "([^"]+)"'


def rg_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["rg", *args],
        check=False,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    return [line for line in result.stdout.splitlines() if line]


def matching_files(root: Path, literal: str) -> set[Path]:
    return {Path(line) for line in rg_lines("-l", "--glob", "*.json", literal, str(root))}


def all_json_files(root: Path) -> list[Path]:
    return [Path(line) for line in rg_lines("--files", str(root)) if line.endswith(".json")]


def task_key(dataset_root: Path, path: Path) -> tuple[str, ...] | None:
    rel = path.relative_to(dataset_root).parts
    # model / suite / user_task_N / attack / file.json
    if len(rel) != 5 or not rel[2].startswith("user_task_"):
        return None
    return tuple(rel[1:])


def attack_from_key(key: tuple[str, ...]) -> str:
    return key[2]


def suite_from_key(key: tuple[str, ...]) -> str:
    return key[0]


def tool_sets(root: Path) -> dict[Path, set[str]]:
    tools: dict[Path, set[str]] = defaultdict(set)
    # The regex output is path:line:"function": "name".  Parsing from the final
    # two colon-delimited fields avoids the Windows drive-letter colon.
    for line in rg_lines("-n", "-o", "--glob", "*.json", FUNCTION_PATTERN, str(root)):
        match = re.match(r'^(.*\.json):\d+:"function": "([^"]+)"$', line)
        if match:
            tools[Path(match.group(1))].add(match.group(2))
    return tools


def exact_mcnemar_p(g_only: int, q_only: int) -> float:
    n = g_only + q_only
    if n == 0:
        return 1.0
    k = min(g_only, q_only)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / (2**n)
    return min(1.0, 2 * tail)


def load_model(dataset_root: Path, model: str) -> dict[tuple[str, ...], dict[str, bool]]:
    root = dataset_root / model
    utility_true = matching_files(root, '"utility": true')
    utility_false = matching_files(root, '"utility": false')
    security_false = matching_files(root, '"security": false')
    tools = tool_sets(root)
    records: dict[tuple[str, ...], dict[str, bool]] = {}
    for path in all_json_files(root):
        key = task_key(dataset_root, path)
        if key is None or path not in utility_true | utility_false:
            continue
        records[key] = {
            "utility": path in utility_true,
            "security_failure": path in security_false,
            "mutation": bool(tools.get(path, set()) & MUTATING_TOOLS),
        }
    return records


def summarize(records: dict[tuple[str, ...], dict[str, bool]]) -> dict[str, float | int]:
    failures = [row for row in records.values() if not row["utility"]]
    mutated_failures = sum(row["mutation"] for row in failures)
    return {
        "n": len(records),
        "utility_success": sum(row["utility"] for row in records.values()),
        "utility_rate": sum(row["utility"] for row in records.values()) / len(records),
        "utility_failures": len(failures),
        "mutated_failures": mutated_failures,
        "mutation_given_failure": mutated_failures / len(failures) if failures else float("nan"),
        "security_failures": sum(row["security_failure"] for row in records.values()),
    }


def matched_failure_table(
    gemma: dict[tuple[str, ...], dict[str, bool]],
    qwen: dict[tuple[str, ...], dict[str, bool]],
    keys: set[tuple[str, ...]],
    require_security_safe: bool = False,
) -> dict[str, int | float]:
    jointly_failed = [
        k
        for k in keys
        if not gemma[k]["utility"]
        and not qwen[k]["utility"]
        and (
            not require_security_safe
            or (
                not gemma[k]["security_failure"]
                and not qwen[k]["security_failure"]
            )
        )
    ]
    cells = Counter(
        (bool(gemma[k]["mutation"]), bool(qwen[k]["mutation"])) for k in jointly_failed
    )
    g_only = cells[(True, False)]
    q_only = cells[(False, True)]
    return {
        "joint_failures": len(jointly_failed),
        "neither_mutates": cells[(False, False)],
        "gemma_only_mutates": g_only,
        "qwen_only_mutates": q_only,
        "both_mutate": cells[(True, True)],
        "mcnemar_exact_two_sided_p": exact_mcnemar_p(g_only, q_only),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_root", type=Path)
    args = parser.parse_args()

    models = ("gemma-4-E4B-it", "qwen3.5-9B")
    dataset_root = args.dataset_root.absolute()
    gemma = load_model(dataset_root, models[0])
    qwen = load_model(dataset_root, models[1])
    common = set(gemma) & set(qwen)

    report: dict[str, object] = {
        "status": "EXPLORATORY_ONLY",
        "mutation_dictionary": sorted(MUTATING_TOOLS),
        "model_summary": {
            models[0]: summarize(gemma),
            models[1]: summarize(qwen),
        },
        "matched": {
            "all": matched_failure_table(gemma, qwen, common),
            "security_safe_only": matched_failure_table(
                gemma, qwen, common, require_security_safe=True
            ),
            "no_attack": matched_failure_table(
                gemma, qwen, {k for k in common if attack_from_key(k) == "none"}
            ),
            "by_attack": {},
            "by_suite": {},
        },
    }

    attacks = sorted({attack_from_key(k) for k in common})
    suites = sorted({suite_from_key(k) for k in common})
    report["matched"]["by_attack"] = {
        attack: matched_failure_table(
            gemma, qwen, {k for k in common if attack_from_key(k) == attack}
        )
        for attack in attacks
    }
    report["matched"]["by_suite"] = {
        suite: matched_failure_table(
            gemma, qwen, {k for k in common if suite_from_key(k) == suite}
        )
        for suite in suites
    }

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
