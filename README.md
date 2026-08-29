# ICLR Research Workspace

This repository records a falsification-first search for an ICLR-level research seed. It contains the original billiards-inspired mechanism discussion, adversarial novelty audits, and completed experiments whose preregistered gates stopped weak hypotheses before they grew into papers.

## Start here

1. **For a new research scout or Pro session:** read only [`docs/pro/README.md`](docs/pro/README.md) first.
2. For the binding project record, read [`docs/current/CURRENT_STATUS.md`](docs/current/CURRENT_STATUS.md).
3. For the latest completed scientific result, read [`experiments/moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md`](experiments/moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md).

There is currently **no authorized GPU-scale paper seed**. The latest frozen-MoE route-non-compositionality discovery ended at **`NO_GO_NO_INTERACTION_LAW`**, and a subsequent 15-candidate Pro search returned `NO_GO_NEED_NEW_SEED`. A re-audited theory-first candidate—**transient shortcut catalysis**—has now passed an internal feasibility gate: a stylized model proves a clean/permanent/transient time-scale separation, and one state-triggered rule transfers across four nonlinear XOR shortcut strengths. Novelty, natural-model generality, and Oral-level significance remain unresolved, so the next task is an adversarial theory/literature audit rather than a broad GPU experiment.

## Repository layout

```text
docs/
  pro/          Curated entry packet and current prompt for a new Pro session
  current/      Current decision and complete billiards-to-AI synthesis
  prompts/      Historical prompts retained for provenance
  audits/       Prior adversarial literature/research audits
  proposals/    Historical generated proposals and their audit trail
  archive/      Early provenance material
analysis/
  transient_shortcut_phase_transition/ Exploratory CPU existence checks for the theory-first HOLD
experiments/
  control_flip/ Reproducible benchmark, inference code, raw outputs, and analysis
  operator_interference/ Completed confirmatory experiment, diagnostics, interventions, and final gate
  moe_route_noncompositionality/ Completed engineering and Stage D discovery; final scientific NO-GO
```

See [`docs/README.md`](docs/README.md) for the full documentation map and [`experiments/README.md`](experiments/README.md) for the experiment index.

## Binding constraints

- Target venue: ICLR; oral-level insight is aspirational, never assumed.
- Compute: one 8× RTX 4090 server, with this project currently restricted to physical GPUs 4--7 (four 24 GB cards concurrently).
- No physical robot dependency.
- Prefer public benchmarks, official evaluators, strong baselines, and open-weight models.
- Require a cheap falsification gate before authorizing a large experiment.
