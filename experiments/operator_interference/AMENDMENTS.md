# Pre-inference Amendments

## Diagnostic pair-ID selection

After the design commit (`32c517f`) and confirmatory-data commit (`7cfea4b`), but before any confirmatory model output was generated or inspected, a dry-run audit found that `make_diagnostic_ids.py` deliberately writes pair IDs while `run_model.py` filtered only exact record IDs. This would have selected zero diagnostic records.

The implementation now accepts either an exact record ID or a pair ID; a pair ID selects its two frozen controller variants. A regression test verifies both behaviors. This is an orchestration correction only: benchmark instances and seed, prompts, output grammar, parser, statistical contrasts, thresholds, model list, and diagnostic sample IDs are unchanged.
