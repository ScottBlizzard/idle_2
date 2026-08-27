from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def evenly_spaced(values: list[str], count: int) -> list[str]:
    if count > len(values):
        raise ValueError("requested subset is larger than the population")
    indices = [int(index * len(values) / count) for index in range(count)]
    return [values[index] for index in indices]


def write_ids(records: list[dict], pair_ids: list[str], output: Path) -> None:
    selected = [record["id"] for record in records if record["pair_id"] in set(pair_ids)]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(selected) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    records = read_jsonl(args.data)
    pair_ids = sorted({record["pair_id"] for record in records})
    template_pairs = evenly_spaced(pair_ids, 12)
    replay_pairs = evenly_spaced(pair_ids, 6)  # 12 items = 11.1% of 108 items per cell.
    write_ids(records, template_pairs, args.output_dir / "template_12_pairs.txt")
    write_ids(records, replay_pairs, args.output_dir / "replay_6_pairs.txt")
    print(
        json.dumps(
            {
                "pairs": len(pair_ids),
                "template_pairs": template_pairs,
                "replay_pairs": replay_pairs,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
