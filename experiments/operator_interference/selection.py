from __future__ import annotations


def select_records(records: list[dict], wanted: set[str]) -> list[dict]:
    """Select exact records or both controller variants of a frozen pair ID."""
    return [
        record
        for record in records
        if record["id"] in wanted or record["pair_id"] in wanted
    ]
