from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from freeze_model_manifest import metadata_revision  # noqa: E402


class ManifestTests(unittest.TestCase):
    def test_hub_revision_is_read_from_download_metadata(self) -> None:
        revision = "a" * 40
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metadata = root / ".cache" / "huggingface" / "download" / "config.json.metadata"
            metadata.parent.mkdir(parents=True)
            metadata.write_text(f"{revision}\netag\ntimestamp\n", encoding="utf-8")
            self.assertEqual(metadata_revision(root, "config.json"), revision)

    def test_invalid_or_absent_metadata_is_not_a_hub_revision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertIsNone(metadata_revision(root, "config.json"))
            metadata = root / ".cache" / "huggingface" / "download" / "config.json.metadata"
            metadata.parent.mkdir(parents=True)
            metadata.write_text("not-a-commit\n", encoding="utf-8")
            self.assertIsNone(metadata_revision(root, "config.json"))


if __name__ == "__main__":
    unittest.main()
