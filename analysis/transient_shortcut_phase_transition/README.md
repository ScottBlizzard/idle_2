# Transient Shortcut Phase Transition — Exploratory Existence Checks

**Status:** outcome-exploratory CPU analysis; not preregistered; not evidence for a paper claim; no GPU authorization.

## Purpose

The literature-role re-audit retained one theory-first question: can temporary shortcut exposure have a help-to-harm transition rather than being uniformly harmful? These checks ask only whether a beneficial interval is possible in minimal learning dynamics.

## Check 1 — two-layer deep linear learner

A scalar-output, factorized linear learner was optimized by deterministic gradient flow on a core feature plus a correlated shortcut. The shortcut was removed after a swept time, with total training time fixed.

Across shortcut correlations `0.2`, `0.5`, `0.8`, `0.95`, and `0.999`, the best core-distribution loss always occurred at zero shortcut exposure. Longer exposure monotonically or near-monotonically worsened the endpoint.

**Interpretation:** a beneficial phase is not a generic consequence of factorization or a temporarily predictive extra feature. Any positive result requires additional nonlinear feature-learning structure.

This agrees with the detailed Phase-I analysis of [SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model](https://arxiv.org/abs/2606.30444): the spurious component grows rapidly while non-spurious signal components remain near initialization, before large shortcut-driven margins suppress later signal acquisition. That theory does not currently imply that early withdrawal can beat clean-only learning.

## Check 2 — nonlinear XOR learner

[`explore_xor.py`](explore_xor.py) trains ten independently initialized width-8 tanh MLPs using full-batch exact expectations over a finite XOR distribution. The input consists of two core XOR bits and one shortcut bit. During the first `tau` updates the shortcut agrees with the label at a fixed probability; it is independent thereafter. Clean-only training is `tau=0`.

All comparisons use:

- identical model family and initialization pairing;
- identical total updates;
- no data-sampling noise;
- the core-only distribution (`shortcut correlation = 0.5`) for endpoint evaluation;
- deterministic CPU operations.

### Long-horizon probe: 1,000 updates

The clean-only mean endpoint loss was `0.02653725`, with accuracy saturated at `1.0`.

| Shortcut correlation | Best observed early `tau` | Mean loss at that `tau` | Change from clean | Longer exposure example | Harm at longer exposure |
|---:|---:|---:|---:|---:|---:|
| 0.70 | 40 | 0.02590646 | -0.00063079 | 160 | +0.00120001 |
| 0.90 | 20 | 0.02582902 | -0.00070823 | 160 | +0.00444078 |
| 0.99 | 20 | 0.02581351 | -0.00072374 | 160 | +0.00651515 |
| 1.00 | 20 | 0.02582890 | -0.00070835 | 160 | +0.00678694 |

At correlation `1.00`, exposure through 640 updates raised loss by `0.16615310`, showing a large harmful regime. The best early settings improved paired-seed loss in 8--9 of 10 seeds, but the absolute benefit was small and accuracy was already saturated.

### Short-horizon probe: 200 updates

The clean-only mean loss was `0.59861882` and mean accuracy `0.7375`. Early-exposure loss improvements were small and inconsistent across correlations and seeds. Some settings raised accuracy while worsening loss; later exposure reliably harmed both.

**Interpretation:** the long-horizon sign reversal is a genuine optimization-dynamics clue, but it is not yet a robust task-level benefit. It may reflect convergence speed, parameterization, or loss-tail effects rather than better invariant representation.

## Binding conclusion

```text
DEEP_LINEAR: NO_BENEFICIAL_REGIME_OBSERVED
NONLINEAR_XOR: WEAK_EXISTENCE_SIGNAL_WITH_HELP_TO_HARM_REVERSAL
THEORY_GATE: NOT_PASSED
GPU_AUTHORIZATION: 0
```

The next valid step is analytical. We need to determine which nonlinear state variable makes the early exposure helpful, derive a prospective transition statistic, and show that the effect is not ordinary privileged information or curriculum tuning. No additional hyperparameter sweep should be interpreted as evidence before that mechanism is specified.
