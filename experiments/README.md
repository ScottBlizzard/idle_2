# Experiments

Each experiment lives in a self-contained directory with its benchmark generator, inference code, tests, raw outputs, and analysis.

## Completed

- [`control_flip/`](control_flip/): paired controller-flip falsification experiment; 7,200 formal generations. The original robust-failure claim is **NO-GO**. See its [Chinese decision report](control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md).
- [`operator_interference/`](operator_interference/): completed preregistered factor-isolation experiment across six independent model families plus one positive control. The final gate is **`NO_GO_STOP_CURRENT_SEED`**. See its [Chinese results report](operator_interference/RESULTS_REPORT_ZH.md) and [machine-generated final gate](operator_interference/results/FINAL_GATE.json).
- [`moe_route_noncompositionality/`](moe_route_noncompositionality/): completed Stage E engineering validation and full Stage D discovery on GSM8K and MATH-500. The final automatic gate is **`NO_GO_NO_INTERACTION_LAW`**: 0/4 layer-pair regimes passed H1--H4 on both datasets. See the [Chinese Stage D report](moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md) and [machine-generated final gate](moe_route_noncompositionality/results/stage_d_discovery/FINAL_GATE.json).

## Active experiments

None. The repository is in a clean new-seed divergence phase. See the [curated Pro packet](../docs/pro/README.md).

New experiments should receive a separate directory rather than adding scripts or results to the repository root.
