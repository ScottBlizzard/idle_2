# ICLR Research Workspace

This repository records a falsification-first research process: the original billiards-inspired discussion, prior novelty audits, the completed control-flip experiment, and the current Pro handoff.

## Start here

1. Read [`docs/current/CURRENT_STATUS.md`](docs/current/CURRENT_STATUS.md) for the binding decision.
2. Read [`experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`](experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md) for the completed 7,200-generation experiment.
3. Give [`docs/prompts/PRO_ALGORITHMIC_PROMPTING_AUDIT.md`](docs/prompts/PRO_ALGORITHMIC_PROMPTING_AUDIT.md) to Pro for the next targeted literature and design audit.

The original controller-insensitive-planning seed is a **NO-GO**. The only surviving observation is a narrower one: correct algorithmic scaffolding can have non-monotonic, model-dependent effects and substantially harm Qwen3.5-9B on the paired diagnostic. This is a research seed, not yet a paper claim.

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
