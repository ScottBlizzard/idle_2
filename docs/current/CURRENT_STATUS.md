# Current Research Status

Last updated: 2026-08-27

## Binding decision

The original **controller-insensitive planning failure** seed is a **NO-GO**.

Direct prompting produced strong same-action biases, but ordinary compact chain-of-thought reached 90.6% pair accuracy on Qwen3.5-4B and 97.2% on Qwen3.5-9B. The proposed failure therefore does not survive an obvious reasoning baseline.

## Surviving observation

A narrower and more counterintuitive observation remains:

> A correct algorithmic scaffold can help one model while systematically harming a stronger model on the same paired tasks.

On Qwen3.5-9B, pair accuracy fell from 97.2% with compact CoT to 78.9% with a generic Bellman scaffold. The paired difference was -18.3 percentage points with a 95% bootstrap interval of [-24.4, -12.2]. In contrast, Qwen3-8B improved from 63.9% to 76.7%.

Generated-reasoning evidence shows explicit unexpected MAX/MIN calls in 11.1% of Qwen3.5-9B Bellman items. Removing the competing operator recovered only part of the loss, so operator confusion is a partial rather than complete explanation.

## Current seed

Working label: **Non-monotonic algorithmic prompting / procedural overconstraint**.

This is not yet a paper claim. It currently rests on one synthetic benchmark and Qwen-family models. The next action is a targeted literature and diagnostic-design audit, followed only by a cheap cross-family smoke test if the audit finds a real novelty gap.

## Stop/go gate

Proceed to a full experiment only if both conditions hold:

1. the literature audit finds that the effect is not already subsumed by overthinking, prompt sensitivity, instruction interference, inverse scaling, or negative-instruction work; and
2. at least two independent non-Qwen model families show a meaningful negative algorithmic-prompting effect in a small smoke test.

Otherwise stop this seed.

## Canonical evidence

- Experiment report: [`../../experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`](../../experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md)
- Main metrics: [`../../experiments/control_flip/results/v2/analysis/summary.csv`](../../experiments/control_flip/results/v2/analysis/summary.csv)
- Paired comparisons: [`../../experiments/control_flip/results/v2/analysis/prompt_comparisons.csv`](../../experiments/control_flip/results/v2/analysis/prompt_comparisons.csv)
- Operator audit: [`../../experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md`](../../experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md)
- Next Pro prompt: [`../prompts/PRO_ALGORITHMIC_PROMPTING_AUDIT.md`](../prompts/PRO_ALGORITHMIC_PROMPTING_AUDIT.md)
