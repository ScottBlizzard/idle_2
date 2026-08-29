# Transient Shortcut Catalysis — Theory Feasibility Note

**Date:** 29 August 2026

**Status:** **`VALID_STYLIZED_RESULT — SUPERSEDED AS PAPER SEED`**

**Experiment authorization:** **0 GPU-hours**

> **Subsequent binding decision (30 August 2026):** the hostile audit repaired this theorem but showed that it does not establish an intrinsic help-to-harm boundary. The required general-law attempt reduced directly to existing level-set/null-space teleportation. See [`DURABLE_CLEAN_RATE_AMPLIFICATION_NOTE.md`](DURABLE_CLEAN_RATE_AMPLIFICATION_NOTE.md). The transient-shortcut Oral seed is closed.

## 1. Sharpened question

The retained C08 question can be made more precise than “a temporary shortcut sometimes helps.” The candidate mechanism is **transient shortcut catalysis**:

> An easy training-only shortcut can rapidly grow a parameter shared with a harder invariant feature, thereby moving the learner out of a slow small-initialization regime. If the shortcut is removed near its own saturation time, the shared state accelerates invariant learning; if it remains available, it solves the training objective and starves the invariant path of gradient.

This predicts a three-way separation:

1. clean-only learning is slow because the core path is higher order;
2. permanent-shortcut learning fits through the easy path but leaves the core path unlearned;
3. shortcut-then-clean learning succeeds quickly because the shortcut acts as a temporary catalyst.

The important object is not merely the final schedule. It is a time-scale separation and a predicted withdrawal window.

## 2. Minimal gradient-flow model

Let (a,u,v>0) be scalar parameters initialized at

\[
a(0)=u(0)=v(0)=\varepsilon,
\qquad 0<\varepsilon\ll1.
\]

Interpret (u^2) as a harder second-order core feature, (v) as an easy linear shortcut, and (a) as their shared readout.

The deployment/core prediction is

\[
f_c(a,u)=a u^2,
\]

with population loss

\[
L_c(a,u)=\frac12(1-a u^2)^2.
\]

During shortcut exposure, the training prediction is

\[
f_s(a,u,v)=a(u^2+v),
\]

with

\[
L_s(a,u,v)=\frac12(1-a(u^2+v))^2.
\]

At withdrawal time τ, the shortcut input is masked and gradient flow switches from (L_s) to (L_c). Parameter (v) remains present but receives no gradient and is absent from deployment prediction. All conditions have the same parameterization and total training time.

## 3. Exact dynamics

Write

\[
e_c=1-a u^2,
\qquad
e_s=1-a(u^2+v).
\]

Core-only gradient flow is

\[
\dot a=e_c u^2,
\qquad
\dot u=2e_c a u,
\qquad
\dot v=0.
\]

Shortcut-phase gradient flow is

\[
\dot a=e_s(u^2+v),
\qquad
\dot u=2e_s a u,
\qquad
\dot v=e_s a.
\]

The core-only system has the exact invariant

\[
a^2-\frac12u^2=\frac12\varepsilon^2.
\]

Near initialization this implies (a=\Theta(u)), so

\[
\dot u=\Theta(u^2)
\]

while the residual remains order one. Escaping from (u=\varepsilon) to constant scale therefore requires order (1/\varepsilon) time.

## 4. Shortcut catalysis time scale

Early in shortcut training, (u^2\ll v) and (e_s\approx1). The leading subsystem is

\[
\dot a\approx v,
\qquad
\dot v\approx a.
\]

With equal positive initialization,

\[
a(t)\approx v(t)\approx\varepsilon e^t.
\]

Thus the shared readout reaches constant scale at

\[
\tau_{\mathrm{sat}}\asymp\log(1/\varepsilon).
\]

During the same period,

\[
\frac{d}{dt}\log u=2e_s a,
\]

whose integral remains order one up to (t\asymp\log(1/\varepsilon)). Hence (u) can remain small even while (a) and (v) become order one.

Two consequences follow.

### Permanent shortcut

Once (a v\approx1), shortcut residual (e_s) becomes small. The shortcut has solved the training loss, so the core parameter (u) receives little additional gradient. Deployment loss can remain order one.

### Withdrawal near saturation

If (v) is masked when (a=\Theta(1)) but (a u^2\ll1), then core-only training starts with

\[
\frac{d}{dt}\log u\approx2a=\Theta(1).
\]

The core path can then reach constant scale in another (O(\log(1/\varepsilon))) interval. This suggests an exponential separation between clean-only escape time (\Omega(1/\varepsilon)) and transient-shortcut escape time (O(\log(1/\varepsilon))).

## 5. Stylized three-way separation proposition

Fix a shortcut withdrawal level (\bar v\in(0,1/4]) and a target loss δ in `(0, 1/2)`. Let τε be the first shortcut-flow time at which (v=\bar v). For sufficiently small ε, the exact dynamics above imply:

1. **Clean lower bound.** For every fixed (C>0) and (T=C\log(1/\varepsilon)),

   \[
   L_c(a_{\mathrm{clean}}(T),u_{\mathrm{clean}}(T))
   =\frac12-o(1).
   \]

2. **Permanent-shortcut failure.** Under (L_s), for any training horizon,

   \[
   L_c(a_{\mathrm{perm}}(T),u_{\mathrm{perm}}(T))
   =\frac12-O(\varepsilon^2).
   \]

3. **Predicted withdrawal time.** The threshold time satisfies

   \[
   \tau_\varepsilon=\Theta(\log(1/\varepsilon)).
   \]

4. **Transient success.** After withdrawal at τε, core-only flow reaches

   \[
   L_c(a_{\mathrm{trans}}(T),u_{\mathrm{trans}}(T))\le\delta
   \]

   after an additional `O(log(1 / epsilon) + log(1 / delta))` interval.

5. **Late-withdrawal boundary.** If withdrawal leaves `o(log(1 / epsilon))` core-only time, the core parameter remains vanishing and deployment loss stays bounded away from zero.

Thus both clean-only and permanent-shortcut training fail on a logarithmic horizon, while a state-triggered transient shortcut succeeds.

More explicitly, for every fixed target `delta`, the proof supplies constants `K_delta` and `epsilon_delta > 0` such that, at the **same** total horizon

\[
T_\varepsilon=K_\delta\log(1/\varepsilon),
\qquad 0<\varepsilon<\varepsilon_\delta,
\]

the transient trajectory has core loss at most `delta`, while clean-only has core loss `1/2 - o(1)` and permanent-shortcut training has core loss `1/2 - O(epsilon^2)`. The constants may depend on the fixed withdrawal level and target loss, but not on `epsilon`. This matched-horizon corollary is the intended three-way comparison; it does not compare methods at different compute budgets.

### Proof

Two identities make the shortcut phase exactly reducible. Direct differentiation gives

\[
\frac{d}{dt}
\left(a^2-v^2-\frac12u^2\right)=0,
\]

and, because `du / u = 2 e_s a dt` while `dv = e_s a dt`,

\[
u(v)=\varepsilon\exp(2(v-\varepsilon)).
\]

The shortcut output (z_s=a(u^2+v)) satisfies

\[
\dot z_s=(1-z_s)
\left[(u^2+v)^2+a^2(1+4u^2)\right].
\]

Since (z_s(0)<1), it increases toward one without crossing it. The invariant gives, for (v\ge\varepsilon),

\[
a^2=v^2+\frac12u^2-\frac12\varepsilon^2
\ge\frac12v^2.
\]

Because (z_s<1), this also bounds (v) and (a) by constants for the permanent-shortcut trajectory. The exact formula for (u(v)) then yields (u=O(\varepsilon)) for all shortcut time. Consequently (a u^2=O(\varepsilon^2)), proving permanent-shortcut core loss `1/2 - O(epsilon^2)`.

For (v\in[2\varepsilon,\bar v]), the same identities give (a=\Theta(v)), (u=O(\varepsilon)), and (1-z_s=\Theta(1)). Therefore

\[
\dot v=(1-z_s)a=\Theta(v),
\]

and integrating `dv / v` proves

\[
\tau_\varepsilon=\Theta(\log(\bar v/\varepsilon))
=\Theta(\log(1/\varepsilon)).
\]

At withdrawal, (a=\Theta(1)) and (u=\Theta(\varepsilon)). Under subsequent core-only flow,

\[
a^2-\frac12u^2
\]

is constant and bounded below by a positive number, so (a\ge c>0). Until core output reaches the fixed level corresponding to loss δ,

\[
\frac{d}{dt}\log u
=2(1-au^2)a
\ge c_\delta>0.
\]

It therefore takes only `O(log(1 / epsilon) + log(1 / delta))` additional time to reach loss δ.

For clean-only training, the invariant is

\[
a^2-\frac12u^2=\frac12\varepsilon^2.
\]

While (u\ge\varepsilon), this gives (a\le u), hence

\[
\dot u\le2u^2.
\]

Comparison with the scalar equation `dw / dt = 2 w^2` shows that for every fixed (C), at (T=C\log(1/\varepsilon)), both (u) and (a) remain `O(epsilon)`. Thus (au^2=O(\varepsilon^3)) and clean loss is `1/2 - o(1)`.

Finally, after withdrawal (u) can grow by at most an exponential factor in the available core-only interval while parameters remain bounded. If that interval is `o(log(1 / epsilon))`, (u=o(1)) and core loss remains separated from zero. This establishes the late-withdrawal boundary. □

This proof is complete for the scalar gradient-flow construction. It does **not** establish novelty, stochastic-gradient robustness, or relevance to natural neural representations.

## 6. Deterministic scaling check

[`explore_catalytic_ode.py`](../../analysis/transient_shortcut_phase_transition/explore_catalytic_ode.py) integrates the exact ODE and uses

\[
T=2.2\log(1/\varepsilon).
\]

| ε | λ = log(1/ε) | clean loss | permanent-shortcut core loss | loss at τ=λ | best τ/λ |
|---:|---:|---:|---:|---:|---:|
| 0.100 | 2.303 | 0.380180 | 0.321228 | approximately 0 | 0.949 |
| 0.050 | 2.996 | 0.498772 | 0.417293 | approximately 0 | 1.045 |
| 0.020 | 3.912 | 0.499978 | 0.481122 | approximately 0 | 1.086 |
| 0.010 | 4.605 | 0.499998 | 0.494850 | approximately 0 | 1.100 |
| 0.005 | 5.298 | 0.500000 | 0.498669 | approximately 0 | 1.100 |

The optimal observed withdrawal time tracks λ within roughly 10% across a 20-fold initialization range. This is outcome-exploratory numerical support for the time-scale calculation, not a proof.

## 7. Nonlinear state-rule transfer check

The scalar theorem predicts that withdrawal should depend on training state rather than raw elapsed steps. The existing nonlinear XOR probe was therefore instrumented at each candidate withdrawal point. Two observations emerged:

1. the shortcut distribution's extra gradient becomes progressively anti-aligned with the clean/core gradient;
2. a common shortcut-aligned margin threshold can adapt the withdrawal time to shortcut strength.

Using `aligned_margin >= 0.40` on the width-8 tanh XOR learner selected steps `55`, `22`, `17`, and `17` for shortcut correlations `0.70`, `0.90`, `0.99`, and `1.00`, respectively. The resulting final clean losses improved over clean-only by `0.00063165`, `0.00073658`, `0.00075041`, and `0.00075820`. Eight or nine of ten paired initializations improved in every condition.

This is stronger than a fixed-step optimum because the same observed-state boundary adapts across four learning speeds. It is still exploratory: the threshold was chosen on this system, the gain is small and loss-only, and accuracy is saturated. The valid conclusion is that the theorem's **state-triggered form transfers qualitatively** to one nonlinear learner—not that the numerical threshold is universal.

## 8. Relation to existing literature

This model must be positioned against, not hidden from, four literatures.

1. [SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model](https://arxiv.org/abs/2606.30444) proves rapid shortcut growth followed by margin-driven signal suppression for a permanent shortcut. It does not analyze withdrawal or prove that shortcut growth can catalyze later core learning.
2. [Learning to Hint for Reinforcement Learning](https://arxiv.org/abs/2604.00698) proves that training-time hints can transfer to an unhinted policy and introduces hint reliance. It is evidence that auxiliary training signals can help, but not a help/permanent-harm time-scale separation in one shared learner.
3. [Principled Curriculum Learning using Parameter Continuation Methods](https://arxiv.org/abs/2507.22089) treats curriculum as parameter continuation. It is a strong foundation and reviewer reduction: the present result must establish more than “homotopy helps optimization.”
4. [Critical Learning Periods for Multisensory Integration in Deep Networks](https://arxiv.org/abs/2210.04643) shows that early correlated multi-source exposure can permanently shape integration. It makes early path dependence expected, but does not supply the specific catalytic/gradient-starvation separation above.
5. [Understanding and Improving Feature Learning for Out-of-Distribution Generalization](https://arxiv.org/abs/2304.11327) proves that ERM can learn invariant and spurious features before an OOD objective is applied. It is a particularly strong positive adversary because ERM pretraining followed by IRM is already a two-stage spurious-to-invariant pipeline. Its result does not establish that the spurious path itself creates an asymptotic speedup over clean-only learning while permanent exposure fails, but any paper must distinguish those claims explicitly.
6. [Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics](https://arxiv.org/abs/2608.17268) proposes a state-dependent relative-transfer view of curriculum schedules. This is a very recent mechanism-level foundation and a possible reduction risk for any broad “dynamic stopping by transfer” claim. The retained contribution must be the shortcut-specific three-way separation and removable shared-bottleneck mechanism, not dynamic curricula in general.
7. [Shortcut Features as Top Eigenfunctions of NTK](https://arxiv.org/abs/2602.03066) explains rapid shortcut preference through kernel eigenstructure. It supplies a competing explanation and a negative control: in a lazy or effectively linear regime, our own deep-linear probe found no catalytic benefit.

Bias-amplification and privileged-information methods are additional mandatory baselines. The theorem can still be new, but “use an easy signal and remove it” is not a new algorithmic template.

## 9. Main scientific risk

The stylized model was deliberately constructed so that the shortcut grows the exact shared readout needed by the core path. If arbitrary shared structure is allowed, beneficial scaffolding is unsurprising and can be described as privileged information or continuation.

The next theory step must therefore characterize a structural condition that is neither hand-designed nor outcome-defined. One candidate is:

\[
\text{shortcut catalysis}
\iff
\text{the shortcut update amplifies a shared multiplicative bottleneck while its own path remains removable}.
\]

This condition must predict both positive and negative cases. An independent shortcut should not help; a shortcut that shares only the final label should not automatically qualify; and permanent shortcut saturation must suppress the core gradient.

## 10. Current decision

```text
STYLIZED_THEOREM_VALID
STYLIZED_THREE_WAY_SEPARATION_PROVED
ONE_STATE_RULE_TRANSFERS_ACROSS_FOUR_XOR_CORRELATIONS
NATURAL_MODEL_PREDICTION_NOT_ESTABLISHED
GENERAL_LAW_DIRECTLY_COLLIDES_WITH_LEVEL_SET_TELEPORTATION
ORAL_SEED_NO_GO
GPU_RUN_NOT_AUTHORIZED
```

The scalar construction remains a valid technical example. It is not an active paper seed. The subsequent audit and general-law collision close GPU-scale continuation of this direction.
