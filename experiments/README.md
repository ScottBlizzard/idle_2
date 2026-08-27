# Experiments

Each experiment lives in a self-contained directory with its benchmark generator, inference code, tests, raw outputs, and analysis.

## Completed

- [`control_flip/`](control_flip/): paired controller-flip falsification experiment; 7,200 formal generations. The original robust-failure claim is **NO-GO**. See its [Chinese decision report](control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md).

## Active gated experiment

- [`operator_interference/`](operator_interference/): preregistered one-day factor-isolation smoke test for conditionally inactive competing operators. Its thresholds are frozen before confirmatory generation; failure terminates the current seed.

New experiments should receive a separate directory rather than adding scripts or results to the repository root.
