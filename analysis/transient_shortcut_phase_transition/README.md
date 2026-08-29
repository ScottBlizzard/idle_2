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

### Training-state withdrawal probe

The fixed-step sweep was then instrumented at the withdrawal boundary. As exposure increased, the gradient contributed by the shortcut distribution became progressively more anti-aligned with the clean/core gradient. The best fixed withdrawals occurred before that conflict became nearly complete. A simpler statistic—the mean signed margin on shortcut-aligned examples—was therefore used as a state trigger.

One common threshold, `aligned_margin >= 0.40`, selected a different withdrawal step for each shortcut strength without observing final clean loss:

| Shortcut correlation | Triggered step | Final clean loss | Change from clean | Paired-seed wins |
|---:|---:|---:|---:|---:|
| 0.70 | 55 | 0.02590560 | -0.00063165 | 8/10 |
| 0.90 | 22 | 0.02580067 | -0.00073658 | 9/10 |
| 0.99 | 17 | 0.02578684 | -0.00075041 | 9/10 |
| 1.00 | 17 | 0.02577905 | -0.00075820 | 9/10 |

At the trigger, the mean extra-gradient/core-gradient cosine ranged from approximately `-0.64` to `-0.77`. A later margin threshold of `0.60` weakened the gain and was already slightly harmful at correlation `0.70`; fixed schedules whose margin had reached roughly `0.75--1.1` were harmful. This is a cross-correlation transfer check for a training-state rule rather than a claim that `0.40` is universal.

The threshold was selected after inspecting this toy system, so it remains outcome-exploratory. A valid next-stage test must freeze either the margin threshold or a theoretically normalized analogue before changing width, initialization, optimizer, shortcut construction, and task.

## Binding conclusion

```text
DEEP_LINEAR: NO_BENEFICIAL_REGIME_OBSERVED
NONLINEAR_XOR: WEAK_EXISTENCE_SIGNAL_WITH_HELP_TO_HARM_REVERSAL
THEORY_GATE: STYLIZED_PASS_WITH_STATE_RULE
GPU_AUTHORIZATION: 0
```

The next valid step is analytical. We need to determine which nonlinear state variable makes the early exposure helpful, derive a prospective transition statistic, and show that the effect is not ordinary privileged information or curriculum tuning. No additional hyperparameter sweep should be interpreted as evidence before that mechanism is specified.

## Sharpened catalytic model

A subsequent three-parameter gradient-flow construction identifies one sufficient mechanism: the shortcut can exponentially amplify a shared readout needed by a higher-order core path, while permanent shortcut saturation starves that core path of gradient. Withdrawal near `log(1 / initialization_scale)` converts the amplified shared state into rapid core learning. Across initialization scales from `0.1` to `0.005`, the best numerical withdrawal time stayed within roughly 10% of this prediction.

- Theory derivation and theorem target: [`../../docs/theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md`](../../docs/theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md)
- Deterministic ODE check: [`explore_catalytic_ode.py`](explore_catalytic_ode.py)
