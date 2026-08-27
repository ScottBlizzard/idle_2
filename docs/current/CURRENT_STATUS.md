# Current Research Status

Last updated: 2026-08-27

## Binding decision

The original **controller-insensitive planning failure** seed is a **NO-GO**.

Direct prompting produced strong same-action biases, but ordinary compact chain-of-thought reached 90.6% pair accuracy on Qwen3.5-4B and 97.2% on Qwen3.5-9B. The proposed failure therefore does not survive an obvious reasoning baseline.

The broader **non-monotonic algorithmic prompting / procedural overconstraint** interpretation receives a **PIVOT** verdict. Recent work already covers correct-constraint harm, constrained-CoT harm, instruction interference, and model-relative prompt reversals. The current experiment also bundles multiple prompt factors, uses only Qwen-lineage models, admits a controller-to-action shortcut, and has parser-dependent ablations.

## Surviving observation

A narrower and more counterintuitive observation remains:

> A correct algorithmic scaffold can help one model while systematically harming a stronger model on the same paired tasks.

On Qwen3.5-9B, pair accuracy fell from 97.2% with compact CoT to 78.9% with a generic Bellman scaffold. The paired difference was -18.3 percentage points with a 95% bootstrap interval of [-24.4, -12.2]. In contrast, Qwen3-8B improved from 63.9% to 76.7%.

Generated-reasoning evidence shows explicit unexpected MAX/MIN calls in 11.1% of Qwen3.5-9B Bellman items. Removing the competing operator recovered only part of the loss, so operator confusion is a partial rather than complete explanation.

## Current hypothesis

Working label: **conditionally irrelevant competing-operator interference**.

> Adding an inactive competing control rule may causally induce oracle-verifiable wrong-operator execution, and the sign of that interference may differ across independently trained model families.

This is a testable hypothesis, not a paper claim. The next and only authorized experiment is the sealed, one-day factor-isolation smoke test specified in the completed Pro audit. It replaces the shortcut-bearing generator, crosses procedural detail with single-versus-dual operator inventory, uses strict structured output, repeats the key contrast under independent wording, and tests six non-Qwen model families plus a Qwen positive control.

## Stop/go gate

Proceed to the public GameBench stage only if all core conditions hold:

1. at least two diagnostically admissible non-Qwen families show a robust negative dual-operator effect under both frozen prompt wordings;
2. a different admissible non-Qwen family shows the preregistered positive effect, establishing genuine sign heterogeneity;
3. dual-operator prompting specifically increases oracle-verified inactive-operator execution; and
4. correcting or injecting the structured operator state causally changes the final decision in the predicted direction.

The full numerical thresholds and automatic termination rules in the Pro audit are binding. Otherwise stop this seed rather than expanding the sweep or searching for a favorable prompt.

## Canonical evidence

- Experiment report: [`../../experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`](../../experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md)
- Main metrics: [`../../experiments/control_flip/results/v2/analysis/summary.csv`](../../experiments/control_flip/results/v2/analysis/summary.csv)
- Paired comparisons: [`../../experiments/control_flip/results/v2/analysis/prompt_comparisons.csv`](../../experiments/control_flip/results/v2/analysis/prompt_comparisons.csv)
- Operator audit: [`../../experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md`](../../experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md)
- Completed novelty audit: [`../audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md`](../audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md)
- Prior reset audit: [`../audits/AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md`](../audits/AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md)
- Completed Pro prompt: [`../prompts/PRO_ALGORITHMIC_PROMPTING_AUDIT.md`](../prompts/PRO_ALGORITHMIC_PROMPTING_AUDIT.md)
