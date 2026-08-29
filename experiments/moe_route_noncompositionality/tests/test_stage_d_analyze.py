from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import numpy as np


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from stage_d_analyze import json_default  # noqa: E402


class AnalysisSerializationTests(unittest.TestCase):
    def test_numpy_values_are_serialized_without_numeric_changes(self) -> None:
        payload = {
            "flag": np.bool_(True),
            "value": np.float64(1.25),
            "array": np.asarray([1, 2], dtype=np.int64),
        }
        decoded = json.loads(json.dumps(payload, default=json_default))
        self.assertEqual(decoded, {"flag": True, "value": 1.25, "array": [1, 2]})


if __name__ == "__main__":
    unittest.main()
