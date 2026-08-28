from __future__ import annotations

import sys
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from stage_d_common import response_token_boundaries  # noqa: E402


class PrefixChangingTokenizer:
    """Minimal fast-tokenizer stand-in for a split UTF-8 character."""

    all_special_ids = []

    def decode(self, ids, **_kwargs):
        values = list(ids)
        if values == [1]:
            return "\ufffd"
        if values == [1, 2]:
            return "\u00e9"
        raise AssertionError(values)

    def convert_ids_to_tokens(self, token_id):
        return {1: "Ã", 2: "©"}[token_id]


class ResponseBoundaryTests(unittest.TestCase):
    def test_uses_full_sequence_offsets_when_prefix_decoding_changes(self) -> None:
        response, surfaces, ends = response_token_boundaries(
            PrefixChangingTokenizer(), [1, 2]
        )
        self.assertEqual(response, "\u00e9")
        self.assertEqual(surfaces, ["", "\u00e9"])
        self.assertEqual(ends, [0, 1])


if __name__ == "__main__":
    unittest.main()
