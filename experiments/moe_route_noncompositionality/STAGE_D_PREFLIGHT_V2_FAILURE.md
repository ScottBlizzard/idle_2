# Stage D Preflight v2 Failure Report

Date: 2026-08-28  
Binding decision: **`NO_GO_STAGE_D_PREFLIGHT`**  
Scientific interpretation: **not allowed**  
Stage D discovery: **not authorized**

## Outcome

The corrected outcome-blind v2 acquisition completed with two retained trajectories for GSM8K and two for MATH-500. All five Stage E artifact hashes matched; the two validator-visible GSM8K shards passed token filtering, 36-pair route-grid completeness, matched-null determinism, standard replay, cached/uncached equivalence, and deterministic rerun checks. The 1,315-parameter compatibility, MLP, and GRU models were parameter matched, and the 360-row synthetic cross-fitting test produced finite predictions.

The automatic gate nevertheless returned `NO_GO_STAGE_D_PREFLIGHT`. This decision is binding for v2.

## Root cause

MATH-500 exposes stable identifiers such as `test/algebra/1098.json`. Acquisition used the opaque stable identifier directly as a shard filename, so its slash characters created nested directories:

`shards/math500/test/algebra/1098.json.json.gz`

The validator used the frozen one-level glob `shards/*/*.json.gz`. It therefore saw both GSM8K shards but zero MATH-500 shards, even though `config_resolved.json` recorded two retained MATH-500 trajectories. The gate correctly failed the required `{gsm8k: 2, math500: 2}` count check.

No H1--H4 route-effect value was inspected or reported while diagnosing this serialization mismatch.

## Preserved evidence

- Server result directory: `/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/results/stage_d_preflight_v2`
- Server log: `/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/queue/stage_d_preflight_v2.log`
- Automatic gate: `results/stage_d_preflight_v2/PREFLIGHT_GATE.json`
- v1 remains separately preserved and invalid because it lacked an explicit generation attention mask.

Neither preflight directory may be overwritten or reused as a passing gate.

## Engineering correction prepared but not executed

The repository now hashes every opaque stable ID into a flat SHA-256 shard filename while retaining the original stable ID inside the immutable shard. Both validator and analyzer also use recursive shard discovery as a defense-in-depth check. A unit test asserts that identifiers containing `/` or `\\` cannot become path separators.

This changes no dataset, example ordering, answer verifier, token rule, route, model, hypothesis, scientific threshold, multiplicity family, or compute cap. It does not retroactively convert v2 into a pass. A new v3 preflight requires an explicit resumed authorization.

