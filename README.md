# ICLR Research Workspace

This repository records a falsification-first search for an ICLR-level research seed. It contains the original billiards-inspired mechanism discussion, adversarial novelty audits, and completed experiments whose preregistered gates stopped weak hypotheses before they grew into papers.

## Start here

1. **For a new research scout or Pro session:** read only [`docs/pro/README.md`](docs/pro/README.md) first.
2. For the binding project record, read [`docs/current/CURRENT_STATUS.md`](docs/current/CURRENT_STATUS.md).
3. For the latest completed scientific result, read [`experiments/endogenous_failure_conditioning/RESULTS_REPORT_ZH.md`](experiments/endogenous_failure_conditioning/RESULTS_REPORT_ZH.md).

There is currently **no authorized paper seed**. The latest Qwen2.5×Qwen3 crossed-repair pilot completed all 3,840 cells but ended at **`KILL_NO_SELECTION_REVERSAL`**. It found a strong within-provider lineage interaction, but MATH-500 had severe output truncation and the preregistered ability-ordering reversal did not occur, so no router or expansion is authorized. Earlier MoE route non-compositionality and transient-shortcut seeds also closed. The current state is **`NO_ACTIVE_SEED`**.

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
- Compute: one 8× RTX 4090 server. Outcome-blind jobs may share any card with sufficient measured free memory; wall-clock time is not treated as a scientific outcome.
- No physical robot dependency.
- Prefer public benchmarks, official evaluators, strong baselines, and open-weight models.
- Require a cheap falsification gate before authorizing a large experiment.
