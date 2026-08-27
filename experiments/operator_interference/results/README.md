# Result artifacts

The authoritative decision is [`FINAL_GATE.json`](FINAL_GATE.json): `NO_GO_STOP_CURRENT_SEED`.

The files under `primary/` were generated before diagnostics and interventions completed. Consequently, `primary/gate.json` and the heading in `primary/REPORT.md` intentionally retain the intermediate status `PRIMARY_RESULTS_ONLY_DIAGNOSTICS_PENDING`; they are audit artifacts, not the final verdict.

Contents:

- `primary/`: evaluated item, pair, contrast, and process results for 5,292 primary outputs;
- `diagnostics/`: exact-replay and format/template comparisons;
- `interventions/`: 892 correction/injection cases and their evaluated outcomes;
- `FINAL_GATE.json`: binding evaluation over all required evidence.

Raw generation files and runtime logs are retained on the experiment server rather than committed to Git. See [`../RESULTS_REPORT_ZH.md`](../RESULTS_REPORT_ZH.md) for execution details and interpretation.
