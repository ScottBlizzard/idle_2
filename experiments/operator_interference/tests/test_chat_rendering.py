from __future__ import annotations

import sys
import unittest
from pathlib import Path

from jinja2.exceptions import TemplateError


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from chat_rendering import render_chat  # noqa: E402
from prompts import SYSTEM_PROMPT  # noqa: E402


class FakeTokenizer:
    def __init__(self, support_system: bool) -> None:
        self.support_system = support_system
        self.calls: list[list[dict[str, str]]] = []

    def apply_chat_template(self, messages, **_kwargs):
        self.calls.append(messages)
        if messages[0]["role"] == "system" and not self.support_system:
            raise TemplateError("System role not supported")
        return "|".join(f"{message['role']}:{message['content']}" for message in messages)


class ChatRenderingTests(unittest.TestCase):
    def test_native_system_role_is_used_when_supported(self) -> None:
        tokenizer = FakeTokenizer(support_system=True)
        rendered = render_chat(tokenizer, "TASK", "native")
        self.assertEqual(len(tokenizer.calls), 1)
        self.assertIn("system:" + SYSTEM_PROMPT, rendered)
        self.assertIn("user:TASK", rendered)

    def test_system_text_is_preserved_for_user_only_template(self) -> None:
        tokenizer = FakeTokenizer(support_system=False)
        rendered = render_chat(tokenizer, "TASK", "native")
        self.assertEqual(len(tokenizer.calls), 2)
        self.assertEqual(tokenizer.calls[-1][0]["role"], "user")
        self.assertIn(SYSTEM_PROMPT, rendered)
        self.assertIn("TASK", rendered)

    def test_plain_template_is_unchanged(self) -> None:
        rendered = render_chat(FakeTokenizer(False), "TASK", "plain")
        self.assertEqual(rendered, f"System: {SYSTEM_PROMPT}\n\nUser: TASK\n\nAssistant:")


if __name__ == "__main__":
    unittest.main()
