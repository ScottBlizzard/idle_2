# Stage 0 v1 preflight failure

Date: 31 August 2026  
Binding decision: **`NO_GO_PREFLIGHT_CAPABILITY_OR_COMPLETENESS`**  
Discovery launched: **no**

## Result

The final-checkpoint seed-1 preflight completed all 576 expected forced-choice records,
but no family cleared the frozen requirement that both representations exceed 60%
accuracy.

| family | original | transformed |
|---|---:|---:|
| Boolean De Morgan | 55.21% | 58.33% |
| graph bijection | 40.62% | 42.71% |
| linear reparameterization | 53.12% | 39.58% |

The full 5-seed discovery was therefore not started. No checkpoint-effect curve or
re-entry statistic was inspected. The gate is not weakened and v1 will not be rerun with
different thresholds.

## Independent implementation audit

A read-only adversarial review also found that v1 was not ready for scientific discovery:

- per-checkpoint majority support did not guarantee that the same seeds reproduced the
  entire three-lobe trajectory;
- confirmation seeds were not protected by an executable authorization seal;
- the scorer and analyzer did not enforce frozen input/code/model hashes or exact unique
  cell completeness;
- a single-checkpoint spike could count as a lobe, and the arbitrary triple search lacked
  multiplicity protection;
- the Boolean capability floor could be beaten by a template-majority shortcut;
- several preregistered alternative-explanation stops were not implemented.

These are independent reasons not to interpret any hypothetical v1 PASS. Since discovery
never ran, they can be repaired in a separately frozen v2 without contaminating a
scientific outcome. Any v2 must use a base-model-appropriate task, exact seed-trajectory
intersection, persistent lobes, held-out templates/items, immutable discovery sealing,
confirmation authorization, and complete hash/schema validation.

## Preserved artifacts

- `results/v1_preflight/PREFLIGHT_GATE.json`
- `results/v1_preflight/seed1_step143000.jsonl`
- `results/v1_preflight/preflight.log`

The raw preflight contains only the final checkpoint and is preserved for audit. It must
not be used to select v2 transformation-effect directions.
