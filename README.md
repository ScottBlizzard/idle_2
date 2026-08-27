# ICLR Research Workspace

This repository records a falsification-first research process: the original billiards-inspired discussion, adversarial novelty audits, and two completed experimental seeds that were stopped by their preregistered gates.

## Start here

1. Read [`docs/current/CURRENT_STATUS.md`](docs/current/CURRENT_STATUS.md) for the binding decision.
2. Read [`docs/audits/DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md`](docs/audits/DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md) for the latest three-agent literature collision audit.
3. Read [`experiments/operator_interference/RESULTS_REPORT_ZH.md`](experiments/operator_interference/RESULTS_REPORT_ZH.md) for the most recent completed confirmatory experiment.

The controller-insensitive-planning and operator-interference seeds are both **NO-GO**. The later viability-aligned-planning idea was already covered as a general principle, and its narrow decision-calibrated world-model uncertainty pivot is now **`NO_GO_BEFORE_EXPERIMENT`** after a direct July 2026 literature collision. There is currently no authorized active paper seed.

## Repository layout

```text
docs/
  current/      Current decision and complete billiards-to-AI synthesis
  prompts/      Current and historical Pro prompts
  audits/       Prior adversarial literature/research audits
  archive/      Early provenance material
experiments/
  control_flip/ Reproducible benchmark, inference code, raw outputs, and analysis
  operator_interference/ Completed confirmatory experiment, diagnostics, interventions, and final gate
```

See [`docs/README.md`](docs/README.md) for the full documentation map and [`experiments/README.md`](experiments/README.md) for the experiment index.

## Binding constraints

- Target venue: ICLR; oral-level insight is aspirational, never assumed.
- Compute: 8 independent RTX 4090 GPUs with 24 GB VRAM each.
- No physical robot dependency.
- Prefer public benchmarks, official evaluators, strong baselines, and open-weight models.
- Require a cheap falsification gate before authorizing a large experiment.
