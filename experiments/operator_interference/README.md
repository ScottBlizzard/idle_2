# Competing-Operator Interference Smoke Test

This directory implements the single factor-isolation gate authorized by the completed novelty audit. It is a new experiment and does not overwrite `experiments/control_flip`.

## Final result

The complete confirmatory run finished on 2026-08-27. The binding verdict is **`NO_GO_STOP_CURRENT_SEED`**.

Only Gemma 2 9B met diagnostic admissibility. It showed a significant Pack-A effect and passed the preregistered process interventions, but the effect did not retain the required magnitude under the independent Pack-B wording. No second admissible negative family or distinct admissible positive family was observed. The current seed is therefore closed and does not authorize GameBench expansion.

Read [`RESULTS_REPORT_ZH.md`](RESULTS_REPORT_ZH.md) for the interpretation and [`results/FINAL_GATE.json`](results/FINAL_GATE.json) for the machine-generated binding decision.

## Frozen design

Read [`PREREGISTRATION.md`](PREREGISTRATION.md) before running anything. The broad algorithmic-prompting claim is not under test. The only hypothesis is a causal effect of an inactive competing operator, plus a preregistered sign reversal across independent model families.

## Executed protocol

1. Validate the generator and both prompt packs on six engineering pairs.
2. Commit the protocol, generator, prompts, strict parser, analysis, and model manifest.
3. Generate the 54 confirmatory pairs from the frozen seed without inspecting model outputs.
4. Freeze exact model revisions and environment metadata.
5. Run Pack A A–E and Pack B C/D with strict grammar-constrained JSON.
6. Run replay, template, unconstrained-output, and structured-state intervention diagnostics.
7. Evaluate the binding GO/NO-GO gate and publish every cell.

Server workspace: `/mnt/sdb/ccj/idle_2_runtime/experiments/operator_interference`. Model weights, raw outputs, and logs remain outside Git. The complete evaluated result artifacts, hashes, frozen manifests, and analysis are stored here.
