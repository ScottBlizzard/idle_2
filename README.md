# ICLR Research Workspace

This repository records a falsification-first research process: the original billiards-inspired discussion, prior novelty audits, the completed control-flip experiment, and the resulting operator-interference pivot.

## Start here

1. Read [`docs/current/CURRENT_STATUS.md`](docs/current/CURRENT_STATUS.md) for the binding decision.
2. Read [`docs/audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md`](docs/audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md) for the completed Pro novelty audit and the exact one-day gate.
3. Read [`experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`](experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md) for the completed 7,200-generation exploratory experiment.

The original controller-insensitive-planning seed is a **NO-GO**, and the broad “algorithmic prompting inversion” interpretation is a **PIVOT** rather than a paper claim. The remaining testable hypothesis is whether a conditionally irrelevant competing operator causally induces wrong-operator execution, with genuinely different signs across independent model families.

## Repository layout

```text
docs/
  current/      Current decision and complete billiards-to-AI synthesis
  prompts/      Current and historical Pro prompts
  audits/       Prior adversarial literature/research audits
  archive/      Early provenance material
experiments/
  control_flip/ Reproducible benchmark, inference code, raw outputs, and analysis
```

See [`docs/README.md`](docs/README.md) for the full documentation map and [`experiments/control_flip/README.md`](experiments/control_flip/README.md) for reproduction instructions.

## Binding constraints

- Target venue: ICLR; oral-level insight is aspirational, never assumed.
- Compute: 8 independent RTX 4090 GPUs with 24 GB VRAM each.
- No physical robot dependency.
- Prefer public benchmarks, official evaluators, strong baselines, and open-weight models.
- Require a cheap falsification gate before authorizing a large experiment.
