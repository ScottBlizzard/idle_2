# Pre-inference Amendments

## Optional Markdown dependency

After the design and confirmatory-data commits, but before any confirmatory model output was generated or inspected, the engineering evaluator completed its numeric artifacts and then failed while rendering `REPORT.md` because `pandas.DataFrame.to_markdown()` requires the undeclared optional `tabulate` package.

The report writer now falls back to a fenced CSV table when that optional package is absent. A regression test exercises report generation in the frozen local environment. This changes only presentation-layer failure handling: benchmark data, prompts, output grammar, model inference, parsing, statistical calculations, contrasts, and scientific thresholds are unchanged.

## Orchestration wrappers

Before confirmatory inference, `run_all_diagnostics.sh` and `run_analysis_and_interventions.sh` were added to preflight completeness and invoke the already frozen replay, template, unconstrained-output, intervention, and final-gate programs without manual filename assembly. They introduce no new condition, sample, statistic, threshold, or fallback analysis.

## Model and runner provenance

Before confirmatory inference, the manifest freezer was strengthened to record the Hugging Face snapshot commit preserved in download metadata plus hashes of local tokenizer artifacts and the full Git commit of the inference runner. It rejects a model whose config and weights resolve to mixed Hub revisions. Existing local checkpoints without Hub metadata remain pinned by their local config, tokenizer, weight names, and byte sizes. This changes only provenance validation.

## Redundant Mistral artifact exclusion

The Mistral repository publishes both the three indexed `model-*.safetensors` shards used by Transformers and a redundant `consolidated.safetensors`. Before model freezing or confirmatory inference, the acquisition script was changed to exclude the redundant file. The three indexed shards, config, tokenizer, and Hub revision remain the frozen checkpoint.

## Native templates without a system role

The Gemma 2 native chat template rejects messages with a `system` role. Before confirmatory inference, chat rendering was changed to preserve the same system instruction by prepending it to the sole user message only when the native template explicitly reports that the system role is unsupported. Models whose templates accept a system role keep the original two-message rendering. The plain-template diagnostic is unchanged.

## Bounded numeric literals in constrained decoding

A pre-inference Mistral engineering probe produced valid completions on 10 of 12 items but used the unbounded numeric regex to repeat zero digits until the 192-token cap on two items. The output grammar and matching JSON schema now bound integer numerators to six digits and nonzero rational denominators to six digits; the intervention grammar uses the same bound. All benchmark candidates and exact oracle values are far inside this range. The 192-token cap, parser, correctness rule, prompts, benchmark, contrasts, and thresholds are unchanged.

## Server archive line endings

Before confirmatory inference, whole-commit deployment from the Windows workstation exposed that archived text files could acquire CRLF line endings. This both invalidated shell launchers and changed the byte-level hash of the otherwise identical confirmatory JSONL. The repository now declares LF endings for all auto-detected text, and server-side launch preflight requires both valid shell syntax and the preregistered confirmatory-data hash. This changes only cross-platform execution packaging; no benchmark, prompt, model, output, analysis, or threshold is changed.
