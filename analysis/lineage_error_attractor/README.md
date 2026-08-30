# Lineage-conditioned error-attractor diagnostic

Status: **post-hoc anomaly diagnosis; not an authorized scientific gate**.

The completed crossed-repair pilot found a strong Qwen2.5×Qwen3 interaction but did not
pass its frozen selection-reversal gate. This diagnostic asks a narrower descriptive
question on GSM8K, where only 2.40% of cases hit the parser-or-truncation quality
definition: does a corrector disproportionately retain the source error's final answer
when the error was produced by its own lineage?

Run:

```bash
python analysis/lineage_error_attractor/diagnose_gsm8k.py
```

The script uses 10,000 problem-clustered bootstrap draws and writes
[`DIAGNOSTIC_SUMMARY.json`](DIAGNOSTIC_SUMMARY.json). It does not change the completed
pilot's `KILL_NO_SELECTION_REVERSAL` decision.

## Descriptive result

Under `external_neutral`, same-lineage correctors retained the original wrong answer in
62.29% of cases versus 45.00% for cross-lineage correctors. Their correction accuracy was
17.92% versus 32.50%. Under `assistant_history`, retention was 73.12% versus 51.88%, and
accuracy was 13.54% versus 26.25%.

This pattern is compatible with a lineage-specific error attractor, but it is not yet
causal evidence. The same result can arise if a lineage's failure cohort simply selects
problems or reasoning states that the lineage cannot solve even from scratch.

## Required separating intervention

For every frozen problem and corrector, measure a no-error solve-from-scratch baseline.
Then compare the effect of exposing the corrector to an incorrect trace from the same or
a different lineage. A lineage-specific attractor requires a negative exposure effect
beyond the no-error baseline that is more severe for same-lineage traces. If the crossed
interaction is already present without error exposure, the current anomaly reduces to
ordinary complementary capability and does not support an error-contagion mechanism.

Only after literature collision review and a new outcome-blind preregistration may this
intervention become a GPU experiment.
