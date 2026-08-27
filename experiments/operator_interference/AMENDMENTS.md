# Pre-inference Amendments

## Optional Markdown dependency

After the design and confirmatory-data commits, but before any confirmatory model output was generated or inspected, the engineering evaluator completed its numeric artifacts and then failed while rendering `REPORT.md` because `pandas.DataFrame.to_markdown()` requires the undeclared optional `tabulate` package.

The report writer now falls back to a fenced CSV table when that optional package is absent. A regression test exercises report generation in the frozen local environment. This changes only presentation-layer failure handling: benchmark data, prompts, output grammar, model inference, parsing, statistical calculations, contrasts, and scientific thresholds are unchanged.

## Orchestration wrappers

Before confirmatory inference, `run_all_diagnostics.sh` and `run_analysis_and_interventions.sh` were added to preflight completeness and invoke the already frozen replay, template, unconstrained-output, intervention, and final-gate programs without manual filename assembly. They introduce no new condition, sample, statistic, threshold, or fallback analysis.
