# Current Research Status

Last updated: 2026-08-27

## Binding decision

The **conditionally irrelevant competing-operator interference** confirmatory seed is a **NO-GO**.

All 49 primary cells, three diagnostic suites, exact replay, and the two-way structured-state interventions completed for six independent model families plus one Qwen positive control. The machine-generated verdict is `NO_GO_STOP_CURRENT_SEED`; all required result cells are complete.

## What the experiment found

Gemma 2 9B was the only diagnostically admissible family. Under Pack A, adding the inactive competing operator reduced pair accuracy from 81.5% to 63.0% (D−C = −18.5 points; Holm-adjusted p = 0.0388). Wrong-operator execution increased, correcting the operator state rescued all four eligible wrong decisions, and reverse injection damaged four correct decisions.

The result did not survive the binding wording replication. Pack B retained only a −5.6-point effect, approximately 30% of the Pack-A magnitude, below both the 7-point and 70%-retention thresholds. Every other independent family failed the preregistered 65% baseline-capability requirement. There were therefore zero admissible negative families and zero admissible positive families.

## Interpretation

The run identifies a real but **single-model, wording-sensitive, causally manipulable local signal**. It does not establish a robust cross-family mechanism, sign heterogeneity, or a publishable ICLR contribution.

The frozen rule now applies: do not add models, prompts, subgroups, parsers, or benchmarks to rescue this seed. A GameBench expansion is not authorized. Further work must begin from a genuinely new hypothesis rather than a larger sweep around the same treatment.

## Canonical evidence

- Chinese confirmatory report: [`../../experiments/operator_interference/RESULTS_REPORT_ZH.md`](../../experiments/operator_interference/RESULTS_REPORT_ZH.md)
- Machine-generated final gate: [`../../experiments/operator_interference/results/FINAL_GATE.json`](../../experiments/operator_interference/results/FINAL_GATE.json)
- Primary metrics: [`../../experiments/operator_interference/results/primary/summary.csv`](../../experiments/operator_interference/results/primary/summary.csv)
- Paired contrasts: [`../../experiments/operator_interference/results/primary/contrasts.csv`](../../experiments/operator_interference/results/primary/contrasts.csv)
- Diagnostic summaries: [`../../experiments/operator_interference/results/diagnostics/`](../../experiments/operator_interference/results/diagnostics/)
- Intervention summary: [`../../experiments/operator_interference/results/interventions/intervention_summary.csv`](../../experiments/operator_interference/results/interventions/intervention_summary.csv)
- Frozen protocol: [`../../experiments/operator_interference/PREREGISTRATION.md`](../../experiments/operator_interference/PREREGISTRATION.md)
- Completed novelty audit: [`../audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md`](../audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md)

## Historical context

The earlier controller-insensitive-planning seed was also a NO-GO: compact chain-of-thought solved it too well. The subsequent broad algorithmic-prompting interpretation was narrowed by the novelty audit because correct-constraint harm, constrained-CoT harm, instruction interference, and prompt-dependent model reversals were already occupied. The now-completed factor-isolation experiment was the sole authorized test of the remaining competing-operator mechanism.
