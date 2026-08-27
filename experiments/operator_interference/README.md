# Competing-Operator Interference Smoke Test

This directory implements the single factor-isolation gate authorized by the completed novelty audit. It is a new experiment and does not overwrite `experiments/control_flip`.

## Frozen design

Read [`PREREGISTRATION.md`](PREREGISTRATION.md) before running anything. The broad algorithmic-prompting claim is not under test. The only hypothesis is a causal effect of an inactive competing operator, plus a preregistered sign reversal across independent model families.

## Current execution order

1. Validate the generator and both prompt packs on six engineering pairs.
2. Commit the protocol, generator, prompts, strict parser, analysis, and model manifest.
3. Generate the 54 confirmatory pairs from the frozen seed without inspecting model outputs.
4. Freeze exact model revisions and environment metadata.
5. Run Pack A A–E and Pack B C/D with strict grammar-constrained JSON.
6. Run replay, template, unconstrained-output, and structured-state intervention diagnostics.
7. Evaluate the binding GO/NO-GO gate and publish every cell.

Server workspace: `/mnt/sdb/ccj/idle_2/experiments/operator_interference`. Model weights and raw outputs remain outside Git while running; hashes, manifests, analysis, and appropriately compressed release artifacts are committed after completion.
