# Stage D Analysis Engineering Amendment

Date: 2026-08-29

This amendment records two outcome-sealed engineering failures after the full 128-trajectory acquisition completed. It does not change `STAGE_D_FROZEN.yaml`, `THRESHOLDS.yaml`, H1--H4 definitions, seeds, folds, bootstrap resamples, multiplicity correction, or decision thresholds.

## Outer timeout

The initial pipeline completed all 64 GSM8K and 64 MATH-500 acquisitions in `10884.35 s` and wrote `route_effects.parquet`, but the six-hour outer process ended with code `124` during H4 cross-fitting. The analysis process was using excessive CPU threads for tiny neural models. A frozen synthetic cross-fitting benchmark completed in `16.2 s` with `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, and `OPENBLAS_NUM_THREADS=1`, versus the earlier severe oversubscription.

The existing route table was preserved as `route_effects.timeout_attempt.parquet`. The unchanged analysis code was rerun with only environment-level thread limits.

## JSON serialization failure

The first single-thread retry completed all numerical work and wrote route, H4-prediction, and problem-summary tables, but stopped while serializing `gates.json`: NumPy's scalar boolean is not accepted by the standard JSON encoder.

The failed outputs were preserved with `analysis_retry1` names. `stage_d_analyze.py` now supplies a JSON-only adapter that converts `numpy.generic` values via `.item()` and NumPy arrays via `.tolist()`. This adapter acts only during file serialization after every statistic and decision has been computed.

## Integrity checks

The successful retry completed in `384.20 s`. The original timeout route table, first retry route table, and final route table have the identical SHA-256:

`98d4ac49cdde50129e3c2cb404dbe377e3b2b1c2b1d7f1104ef7eb955ef13deb`

All hashes registered by `FINAL_GATE.json` match the downloaded files. All 128 compressed acquisition shards match their paired checksum records. The final automatic decision is `NO_GO_NO_INTERACTION_LAW`; Stage C remains unauthorized.

The automatic compute gate records successful acquisition plus successful analysis, as implemented by the frozen evaluator. Failed engineering-attempt CPU time is preserved in logs but excluded from that field and must be disclosed separately in any runtime claim.
