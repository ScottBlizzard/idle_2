from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    for model in manifest["models"]:
        directory = Path(model["local_dir"])
        if not directory.is_absolute():
            directory = args.root / directory
        config_path = directory / "config.json"
        if not config_path.exists():
            raise SystemExit(f"missing config: {config_path}")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if config.get("quantization_config"):
            raise SystemExit(f"quantized model is forbidden: {directory}")
        weight_files = sorted(
            path for pattern in ("*.safetensors", "pytorch_model*.bin") for path in directory.glob(pattern)
        )
        if not weight_files:
            raise SystemExit(f"no weight files: {directory}")
        tree_material = [
            {
                "name": path.name,
                "bytes": path.stat().st_size,
            }
            for path in weight_files
        ]
        tree_material.append({"config_sha256": sha256(config_path)})
        revision = hashlib.sha256(
            json.dumps(tree_material, sort_keys=True).encode("utf-8")
        ).hexdigest()
        model.update(
            {
                "revision": f"local-tree-{revision}",
                "resolved_local_dir": str(directory.resolve()),
                "config_sha256": sha256(config_path),
                "weight_files": len(weight_files),
                "weight_bytes": sum(path.stat().st_size for path in weight_files),
                "quantized": False,
            }
        )
    manifest["revisions_frozen"] = True
    args.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"models": len(manifest["models"]), "revisions_frozen": True}, sort_keys=True))


if __name__ == "__main__":
    main()
