from __future__ import annotations

from typing import Iterable


PACK_A_CONDITIONS = ("A", "B", "C", "D", "E")
PACK_B_CONDITIONS = ("C", "D")
ALL_PACKS = {"A": PACK_A_CONDITIONS, "B": PACK_B_CONDITIONS}

SYSTEM_PROMPT = (
    "You are a precise decision analyst. Follow only the rule card in the user message, "
    "compute exact values, and return the required JSON object."
)


def _semantic_phrase(semantic: str, pack: str) -> str:
    if pack == "A":
        return "select the larger candidate value" if semantic == "larger" else "select the smaller candidate value"
    return "retain the greatest candidate value" if semantic == "larger" else "retain the least candidate value"


def _assignment(record: dict, role: str, pack: str) -> str:
    operator = record["role_to_operator"][role]
    semantic = record["operator_semantics"][operator]
    if pack == "A":
        return f"{role} is assigned {operator}; {operator} means {_semantic_phrase(semantic, pack)}."
    return f"For {role}, use {operator}. The meaning of {operator} is: {_semantic_phrase(semantic, pack)}."


def rule_card(record: dict, condition: str, pack: str) -> str:
    active = record["active_controller"]
    inactive = "ROLE_B" if active == "ROLE_A" else "ROLE_A"
    active_operator = record["role_to_operator"][active]
    inactive_operator = record["role_to_operator"][inactive]

    if pack == "A":
        if condition == "A":
            slots = {
                "ROLE_A": _assignment(record, "ROLE_A", pack)
                if active == "ROLE_A"
                else "ROLE_A's rule-card slot is neutral and contains no operation.",
                "ROLE_B": _assignment(record, "ROLE_B", pack)
                if active == "ROLE_B"
                else "ROLE_B's rule-card slot is neutral and contains no operation.",
            }
            return "\n".join(
                [
                    "Compact rule card:",
                    slots["ROLE_A"],
                    slots["ROLE_B"],
                    "Apply that active rule independently at every terminal-choice node.",
                ]
            )
        if condition == "B":
            return "\n".join(
                [
                    "Compact rule card:",
                    _assignment(record, "ROLE_A", pack),
                    _assignment(record, "ROLE_B", pack),
                    "Apply the assignment belonging to the active controller at every terminal-choice node.",
                ]
            )
        common = [
            "Procedural rule card:",
            "Step 1: copy the active controller exactly from the task.",
        ]
        if condition == "C":
            slots = {
                "ROLE_A": _assignment(record, "ROLE_A", pack)
                if active == "ROLE_A"
                else "ROLE_A's slot is intentionally neutral and adds no operation.",
                "ROLE_B": _assignment(record, "ROLE_B", pack)
                if active == "ROLE_B"
                else "ROLE_B's slot is intentionally neutral and adds no operation.",
            }
            rules = [f"Step 2: {slots['ROLE_A']}", f"Step 3: {slots['ROLE_B']}"]
        elif condition == "D":
            rules = [
                f"Step 2: {_assignment(record, 'ROLE_A', pack)}",
                f"Step 3: {_assignment(record, 'ROLE_B', pack)}",
            ]
        elif condition == "E":
            slots = {
                active: _assignment(record, active, pack),
                inactive: f"never apply {inactive_operator}, which belongs to inactive {inactive}.",
            }
            rules = [f"Step 2: {slots['ROLE_A']}", f"Step 3: {slots['ROLE_B']}"]
        else:
            raise ValueError(condition)
        return "\n".join(
            common
            + rules
            + [
                "Step 4: at each node, record the applied operator and selected candidate value.",
                "Step 5: probability-weight the selected node values for each root action.",
                "Step 6: choose the root action with the larger expected value.",
            ]
        )

    if pack != "B" or condition not in PACK_B_CONDITIONS:
        raise ValueError((pack, condition))
    if condition == "C":
        slots = {
            "ROLE_A": _assignment(record, "ROLE_A", pack)
            if active == "ROLE_A"
            else "Reserve ROLE_A's line as neutral text with no decision content.",
            "ROLE_B": _assignment(record, "ROLE_B", pack)
            if active == "ROLE_B"
            else "Reserve ROLE_B's line as neutral text with no decision content.",
        }
        rule_lines = [
            f"Instruction 2: {slots['ROLE_B']}",
            f"Instruction 3: {slots['ROLE_A']}",
        ]
    else:
        rule_lines = [
            f"Instruction 2: {_assignment(record, 'ROLE_B', pack)}",
            f"Instruction 3: {_assignment(record, 'ROLE_A', pack)}",
        ]
    return "\n".join(
        [
            "Independent procedural wording:",
            "Instruction 1: identify the controller marked active in the task.",
            *rule_lines,
            "Instruction 4: resolve every terminal-choice node with the active controller's operation.",
            "Instruction 5: calculate each chance-weighted root value exactly.",
            "Instruction 6: report the higher-valued root action.",
        ]
    )


OUTPUT_INSTRUCTION = """Output contract:
Return exactly one JSON object and no surrounding prose.
Use these keys in order: controller, nodes, actions, final_action.
controller is the active role label.
nodes is a list in the task's displayed node order; each entry has node, operator, selected_value.
actions is a list in the task's displayed action order; each entry has action, expected_value.
All values and expected values must be strings containing exact integers or fractions such as \"7\" or \"-3/2\".
final_action is exactly one displayed action label."""


def unpadded_user_prompt(record: dict, condition: str, pack: str) -> str:
    if condition not in ALL_PACKS[pack]:
        raise ValueError((pack, condition))
    return f"{record['task']}\n\n{rule_card(record, condition, pack)}\n\n{OUTPUT_INSTRUCTION}"


def _token_count(tokenizer, text: str) -> int:
    return len(tokenizer.encode(text, add_special_tokens=False))


def _pad_to_target(tokenizer, text: str, target: int) -> tuple[str, int]:
    prefix = "\n\nNeutral length markers with no task meaning:"
    best_text = text + prefix
    best_count = _token_count(tokenizer, best_text)
    best_gap = abs(best_count - target)
    markers: list[str] = []
    for index in range(256):
        markers.append(f" N{index % 10}")
        candidate = text + prefix + "".join(markers)
        count = _token_count(tokenizer, candidate)
        gap = abs(count - target)
        if gap < best_gap:
            best_text, best_count, best_gap = candidate, count, gap
        if count >= target and best_gap <= 1:
            break
    if best_gap > 2:
        raise ValueError(f"failed token balancing: target={target}, got={best_count}")
    return best_text, best_count


def render_user_prompt(record: dict, condition: str, pack: str, tokenizer) -> tuple[str, dict]:
    if pack == "B":
        group: Iterable[str] = PACK_B_CONDITIONS
    elif condition in {"A", "B"}:
        group = ("A", "B")
    else:
        group = ("C", "D", "E")
    base = {cell: unpadded_user_prompt(record, cell, pack) for cell in group}
    target = max(_token_count(tokenizer, text) for text in base.values()) + 12
    balanced = {cell: _pad_to_target(tokenizer, text, target) for cell, text in base.items()}
    counts = {cell: item[1] for cell, item in balanced.items()}
    if max(counts.values()) - min(counts.values()) > 2:
        raise ValueError(f"prompt group is not token matched: {counts}")
    text, count = balanced[condition]
    return text, {"target": target, "token_count": count, "group_counts": counts}


def output_schema(record: dict) -> dict:
    node_names = []
    for action in record["action_order"]:
        for outcome_index, _ in enumerate(record["actions"][action]["outcomes"], start=1):
            node_names.append(f"NODE_{action[-1]}{outcome_index}")
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["controller", "nodes", "actions", "final_action"],
        "properties": {
            "controller": {"type": "string", "enum": ["ROLE_A", "ROLE_B"]},
            "nodes": {
                "type": "array",
                "minItems": len(node_names),
                "maxItems": len(node_names),
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["node", "operator", "selected_value"],
                    "properties": {
                        "node": {"type": "string", "enum": node_names},
                        "operator": {"type": "string", "enum": ["OP_X", "OP_Y"]},
                            "selected_value": {"type": "string", "pattern": "^-?[0-9]{1,6}(?:/[1-9][0-9]{0,5})?$"},
                    },
                },
            },
            "actions": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["action", "expected_value"],
                    "properties": {
                        "action": {"type": "string", "enum": ["ACTION_P", "ACTION_Q"]},
                        "expected_value": {"type": "string", "pattern": "^-?[0-9]{1,6}(?:/[1-9][0-9]{0,5})?$"},
                    },
                },
            },
            "final_action": {"type": "string", "enum": ["ACTION_P", "ACTION_Q"]},
        },
    }


def output_regex(record: dict) -> str:
    """A compact JSON grammar with fixed structural labels and free semantic values."""
    number = "(-?[0-9]{1,6}|-?[0-9]{1,6}/[1-9][0-9]{0,5})"
    operator = "(OP_X|OP_Y)"
    controller = "(ROLE_A|ROLE_B)"
    final_action = "(ACTION_P|ACTION_Q)"
    node_parts = []
    for action in record["action_order"]:
        for outcome_index, _ in enumerate(record["actions"][action]["outcomes"], start=1):
            node = f"NODE_{action[-1]}{outcome_index}"
            node_parts.append(
                r'\{"node":"' + node + r'","operator":"' + operator
                + r'","selected_value":"' + number + r'"\}'
            )
    action_parts = [
        r'\{"action":"' + action + r'","expected_value":"' + number + r'"\}'
        for action in record["action_order"]
    ]
    return (
        r'\{"controller":"'
        + controller
        + r'","nodes":\['
        + ",".join(node_parts)
        + r'\],"actions":\['
        + ",".join(action_parts)
        + r'\],"final_action":"'
        + final_action
        + r'"\}'
    )
