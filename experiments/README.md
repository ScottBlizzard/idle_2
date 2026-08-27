# Experiments

Each experiment lives in a self-contained directory with its benchmark generator, inference code, tests, raw outputs, and analysis.

## Completed

- [`control_flip/`](control_flip/): paired controller-flip falsification experiment; 7,200 formal generations. The original robust-failure claim is **NO-GO**. See its [Chinese decision report](control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md).
- [`operator_interference/`](operator_interference/): completed preregistered factor-isolation experiment across six independent model families plus one positive control. The final gate is **`NO_GO_STOP_CURRENT_SEED`**. See its [Chinese results report](operator_interference/RESULTS_REPORT_ZH.md) and [machine-generated final gate](operator_interference/results/FINAL_GATE.json).

## Active experiments

None. The later decision-calibrated world-model uncertainty idea was stopped at the literature gate before an experiment directory was created. See the [binding collision audit](../docs/audits/DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md).

New experiments should receive a separate directory rather than adding scripts or results to the repository root.
