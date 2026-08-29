# Stage D Execution Status

Updated: 2026-08-29 Asia/Hong_Kong

Status: **COMPLETE — `NO_GO_NO_INTERACTION_LAW`**

## Binding decision

Stage D discovery is complete. The automatic gate found zero layer-pair regimes that passed H1--H4 on both GSM8K and MATH-500; the frozen requirement was at least three of four. `FINAL_GATE.json` therefore sets:

- `status = NO_GO_NO_INTERACTION_LAW`;
- `scientific_interpretation_allowed = true`;
- `stage_c_authorized = false`;
- `compute_pass = true`.

Stage C and Stage A must not run. The current seed is closed and may not be rescued by adding models, changing thresholds, selecting subgroups, or redefining layer regimes.

## Completion and integrity

- GSM8K: 64 retained trajectories from 109 examined.
- MATH-500: 64 retained trajectories from 315 examined.
- Acquisition: `10884.35 s`.
- Successful analysis: `384.20 s`.
- Automatic cumulative compute: `11268.55 s / 21600 s`.
- Downloaded compressed shards: 128; every paired checksum passes.
- Four final artifact hashes: all match `FINAL_GATE.json`.
- Three independently written route-effect Parquet files are byte-identical.

## Result synopsis

H1/H2 reversal excesses were generally near zero and did not reach their frozen `0.10` effect requirements. A few H3 cells had positive point estimates above `0.10`, but none survived the full 32-test Benjamini--Hochberg family. H4 compatibility correlations ranged from `-0.063` to `0.040`, far below the required `0.40`. No cell passed all four hypotheses.

## Engineering disclosure

The first full pipeline timed out during CPU analysis after completing acquisition because tiny neural predictors were oversubscribed across CPU threads. A single-thread retry completed the frozen computation in minutes. That retry then encountered a JSON-only NumPy scalar serialization error; the serialization adapter changed no statistic or decision. All failed outputs and logs remain preserved.

The automatic compute field includes the successful acquisition and successful analysis, as implemented by the evaluator; failed engineering-attempt CPU time is disclosed separately and excluded from that field.

## Canonical documents

- [`STAGE_D_RESULTS_REPORT_ZH.md`](STAGE_D_RESULTS_REPORT_ZH.md)
- [`STAGE_D_ANALYSIS_ENGINEERING_AMENDMENT.md`](STAGE_D_ANALYSIS_ENGINEERING_AMENDMENT.md)
- [`STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md`](STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md)
- [`STAGE_D_PROTOCOL_AMENDMENT_V1.md`](STAGE_D_PROTOCOL_AMENDMENT_V1.md)
- [`results/stage_d_discovery/FINAL_GATE.json`](results/stage_d_discovery/FINAL_GATE.json)
