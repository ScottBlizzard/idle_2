# Pilot Protocol Amendment V2 — Qwen Lineages

## Status and timing

This amendment was frozen before any correction outcome was generated or inspected.
The v1 public error bank was constructed successfully, but its model-access preflight
failed: both `google/gemma-2-*` correctors require a gated license unavailable to the
local account, the 4090 server has no cached Gemma weights, and `hf-mirror` returns HTTP
403 for the frozen Gemma revision. V1 remains preserved and must not be called a run.

## Outcome-blind replacement grid

V2 changes only the four model identities and the interpretation of the interaction:

| lineage | smaller | larger |
|---|---|---|
| Qwen 2.5 | Qwen2.5-3B-Instruct | Qwen2.5-7B-Instruct |
| Qwen 3 | Qwen3-4B | Qwen3-8B |

The source dataset revision, two domains, 60 shared problems per domain, 480-error bank
size, wrappers, decoding, 5-point reversal threshold, 5-point interaction threshold,
cluster bootstrap, parser/truncation gate, and 3-point router threshold are unchanged.
The executable increment is `v2.1-qwen-lineages-no-thinking`. Qwen 3 correction calls
freeze `enable_thinking=false`; otherwise Qwen 3 alone would
consume part of the equal 768-token output budget in a hidden-reasoning mode unavailable
to Qwen 2.5. This setting was frozen before any correction outcome.
V2 receives a new config, error-bank directory, preflight record, and result directory;
it never overwrites v1.

## Claim restriction

The V2 interaction is a **lineage interaction**, not a cross-provider family effect. A
positive result can justify the complementarity-router test and acquisition of an
ungated cross-provider replication grid. It cannot by itself establish universal
relational error depth or satisfy the Oral promotion bar. A negative V2 result kills the
cheap same-provider rescue and does not authorize model substitution after outcomes are
visible.

Frozen configuration:
[`FROZEN_CONFIG_V2_QWEN_LINEAGES.json`](FROZEN_CONFIG_V2_QWEN_LINEAGES.json).
