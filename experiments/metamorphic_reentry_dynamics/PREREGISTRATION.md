# Metamorphic Re-entry Dynamics — Stage 0 Preregistration

**Status:** anomaly-discovery scan, not an active paper seed  
**Frozen:** 31 August 2026  
**Maximum discovery compute:** 2 aggregate GPU-hours  
**Repository:** [ScottBlizzard/idle_2](https://github.com/ScottBlizzard/idle_2)

## Question

Static sensitivity to equivalent prompts is already well established. This scan asks a
narrower dynamic question:

> During pretraining, does the paired effect of one strictly semantics-preserving
> transformation undergo a reproducible re-entrant sign pattern across independent
> training seeds: beneficial, then harmful, then beneficial again (or the reverse)?

One monotone convergence, one competence-threshold crossing, or a final-checkpoint gap is
not a positive result. A surviving event would only be an anomaly requiring a second
scale and a separate mechanism study.

## Frozen objects

`FROZEN_CONFIG.json` fixes:

- PolyPythias 410M seeds 1–9 and sixteen aligned revisions;
- seeds 1–5 for discovery and seeds 6–9 for sealed confirmation;
- 96 items in each of three executable-equivalence families;
- the paired effect, capability floor, lobe magnitude, and cross-seed support gates;
- the requirement for a second model scale before promotion.

`items.jsonl` is built deterministically by `build_items.py`; its manifest hashes both
the config and all 288 pairs.

## Equivalence families

1. **Boolean De Morgan rewrites.** The assignment and truth value are fixed; only an
   exact De Morgan form changes.
2. **Directed-graph bijections.** A graph and reachability query are relabeled by a node
   bijection. The transformed graph is isomorphic and has the same answer.
3. **Linear reparameterizations.** `y=s*x` rewrites an integer expression while the
   executable result remains identical.

Every pair has the same correct and incorrect candidate continuations. The scorer uses
the correct-minus-incorrect continuation mean-log-probability margin, so no free-text
generation or parser enters the estimand.

## Estimand

For item `i`, checkpoint `t`, and training seed `s`:

```text
delta[s,t,i] = margin(transformed) - margin(original)
```

The cell effect is the within-family mean of `delta`. A checkpoint receives a positive
or negative active sign only if:

- the absolute mean effect is at least 0.15 logit;
- both representations exceed 60% forced-choice accuracy.

Zeros are not interpolated into a sign. Discovery requires three ordered checkpoints
with signs `+,-,+` or `-,+,-`, each supported by at least four of five discovery seeds.

## Outcome-sealing rule

Confirmation results must not be inspected unless discovery passes automatically.
If discovery passes, the exact family, three checkpoints, and sign order are frozen by
the discovery gate. Confirmation requires the same sign at every checkpoint for at least
three of four held-out seeds, yielding at least seven of nine total supporting seeds.

The only positive Stage 0 status is:

```text
ANOMALY_DISCOVERY_PASS_NEEDS_SECOND_SCALE
```

It is not a paper claim and does not authorize a method, regularizer, or full sweep.

## Automatic stops

Stop with `NO_GO_NO_REENTRANT_DISCOVERY` if discovery has no qualifying three-lobe
pattern. Stop with `NO_GO_CONFIRMATION_FAILED` if the sealed seeds fail. Also stop the
scientific direction if the apparent pattern is explained by:

- failure to clear the competence floor;
- temperature or global calibration drift;
- answer-token length/frequency;
- one ordinary transition from chance to competence;
- one outlier training seed;
- a template-specific effect that fails an independently frozen second scale.

## Literature boundary

Pythia and PolyPythias supply the checkpoint infrastructure and already establish
training phases and cross-seed stability. Formal and metamorphic-testing papers already
establish static failure of semantic invariance. Therefore none of the following is a
novel result: equivalent prompts differ, sensitivity changes with training, or one
checkpoint has an unusual gap. Only a replicated re-entrant sign law that predicts a new
held-out boundary could justify a later seed audit.

Primary starting points:

- [Pythia](https://arxiv.org/abs/2304.01373)
- [PolyPythias](https://arxiv.org/abs/2503.09543)
- [What Are the Right Symmetries for Formal Theorem Proving?](https://arxiv.org/abs/2605.22257)

## Engineering order

1. Build and hash items; run unit tests.
2. Run one final-checkpoint preflight to verify tokenizer compatibility, record count,
   runtime, and whether at least one family clears the capability floor.
3. Only then run discovery seeds 1–5 on physical GPUs 4–7.
4. Run `analyze_stage0.py` without a confirmation directory.
5. Acquire confirmation seeds only if the machine gate asks for them.

No process on physical GPUs 0–3 may be started, stopped, or modified. Existing foreign
processes are never stopped. Exclusive GPU ownership is not required; sufficient free
memory is sufficient.
