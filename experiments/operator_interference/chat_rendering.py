from __future__ import annotations

from jinja2.exceptions import TemplateError

from prompts import SYSTEM_PROMPT


def _apply_native(tokenizer, messages: list[dict[str, str]]) -> str:
    kwargs = {"tokenize": False, "add_generation_prompt": True}
    try:
        return tokenizer.apply_chat_template(messages, enable_thinking=False, **kwargs)
    except TypeError:
        return tokenizer.apply_chat_template(messages, **kwargs)


def render_chat(tokenizer, user_prompt: str, template_mode: str) -> str:
    if template_mode == "plain":
        return f"System: {SYSTEM_PROMPT}\n\nUser: {user_prompt}\n\nAssistant:"
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
    try:
        return _apply_native(tokenizer, messages)
    except TemplateError as exc:
        message = str(exc).lower()
        if "system" not in message or "support" not in message:
            raise
        combined = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        return _apply_native(tokenizer, [{"role": "user", "content": combined}])
