# Durable Clean-Rate Amplification Beyond Relative Transfer

**Date:** 30 August 2026

**Status:** **`LOCAL_LAW_PROVED_BUT_DIRECTLY_OCCUPIED — NO_GO_AS_ORAL_SEED`**

**Experiment authorization:** **0 GPU-hours**

## 1. Why the previous theorem is insufficient

The repaired transient-shortcut theorem proves a real normal-form separation, but it does not prove an intrinsic help-to-harm transition. Its shortcut raises a favorable shared multiplier; continued shortcut exposure does not destroy that state, and a sufficiently long fresh clean phase can still learn the deployment path.

The stronger unresolved question is therefore:

> Can two training signals have the same immediate clean-task transfer, yet leave the learner in states with provably different future clean-learning rates after the signals disappear?

This note isolates one local answer. The resulting quantity is explicitly second order and cannot be reduced to current gradient cosine or first-order Relative Transfer. Whether this calculus-level result is already occupied by Hessian-aware auxiliary learning or meta-gradient work remains a binding novelty question.

## 2. Two matched training vector fields

Let `L : R^p -> R` be a `C^3` clean loss, with

\[
g(\theta)=\nabla L(\theta),
\qquad
F(\theta)=-g(\theta).
\]

Let `H` be a second gradient-flow vector field used only during temporary auxiliary or shortcut exposure. Define its excess update over clean training by

\[
A(\theta)=H(\theta)-F(\theta).
\]

If `H=-nabla L_s`, then the usual first-order Relative Transfer from the shortcut objective to the clean objective is

\[
\operatorname{RT}(c,s)
=\frac{g^\top\nabla L_s}{\|g\|^2}.
\]

Because `A=-nabla L_s+nabla L`,

\[
g^\top A
=\|g\|^2\bigl(1-\operatorname{RT}(c,s)\bigr).
\]

Thus

\[
g^\top A=0
\quad\Longleftrightarrow\quad
\operatorname{RT}(c,s)=1.
\]

This is an exact first-order match: replacing a clean update by the shortcut update has the same instantaneous clean-loss decrease.

## 3. Local rate-shaping theorem

Let `Phi_F^t` and `Phi_H^t` be the clean and shortcut flows. Starting from the same state `theta`, compare matched-total-time schedules

\[
\theta_{\mathrm{clean}}(\eta,s)
=\Phi_F^{s+\eta}(\theta),
\]

and

\[
\theta_{\mathrm{switch}}(\eta,s)
=\Phi_F^s\!\left(\Phi_H^\eta(\theta)\right).
\]

Define the endpoint gap

\[
\Delta(\eta,s)
=L(\theta_{\mathrm{switch}}(\eta,s))
-L(\theta_{\mathrm{clean}}(\eta,s)).
\]

### Theorem 1 — matched-RT clean-rate shaping

Suppose `L` and the two vector fields are sufficiently smooth near `theta`, and

\[
g(\theta)^\top A(\theta)=0.
\]

Then, as `eta,s -> 0`,

\[
\boxed{
\Delta(\eta,s)
=-\eta s\,D_A\|g\|^2
+O(\eta s^2+\eta^2).
}
\]

In particular, choosing `eta=s^2` gives

\[
\boxed{
\Delta(s^2,s)
=-s^3 D_A\|g\|^2+O(s^4).
}
\]

Therefore, for sufficiently small positive `s`:

- `D_A ||g||^2 > 0` implies temporary exposure strictly improves the future clean endpoint;
- `D_A ||g||^2 < 0` implies temporary exposure strictly harms it;
- `D_A ||g||^2 = 0` removes the cubic-order effect and requires higher-order analysis.

All cases have equal total gradient-flow time and identical first-order Relative Transfer.

### Proof

Let

\[
V_s(x)=L(\Phi_F^s(x)).
\]

The two exposure flows satisfy

\[
\Phi_H^\eta(\theta)-\Phi_F^\eta(\theta)
=\eta A(\theta)+O(\eta^2).
\]

Taylor expansion of `V_s` therefore gives

\[
\Delta(\eta,s)
=\eta\nabla V_s(\theta)^\top A(\theta)+O(\eta^2).
\]

Under clean gradient flow,

\[
V_s(\theta)
=L(\theta)-s\|g(\theta)\|^2+O(s^2),
\]

so

\[
\nabla V_s(\theta)
=g(\theta)-s\nabla\|g(\theta)\|^2+O(s^2).
\]

Substitution yields

\[
\Delta
=\eta g^\top A
-\eta s D_A\|g\|^2
+O(\eta s^2+\eta^2).
\]

The matched-RT assumption cancels the first term. Setting `eta=s^2` proves the cubic expansion. □

The rate-shaping coefficient also has the Hessian form

\[
\boxed{
D_A\|g\|^2
=2A^\top\nabla^2L\,g.
}
\]

This identity is an immediate warning: the local theorem may be a clean restatement of Hessian-aware transfer rather than a new learning principle.

## 4. Representation-only specialization

Let the clean task be a squared residual problem

\[
L(\theta)=\frac12\|r(\theta)\|^2,
\qquad
r(\theta)=f(\theta)-y.
\]

Let

\[
J=\nabla_\theta f,
\qquad
K=JJ^\top
\]

be the clean prediction Jacobian and empirical clean NTK. Then

\[
\|g\|^2=r^\top K r.
\]

Impose the stronger function-null condition

\[
\boxed{JA=0.}
\]

This means the excess shortcut update does not change the current clean prediction to first order. It automatically implies `g^T A=0` and hence `RT=1`. Moreover,

\[
D_A r=JA=0,
\]

so

\[
\boxed{
D_A\|g\|^2
=r^\top(D_AK)r.
}
\]

The leading endpoint difference becomes

\[
\boxed{
\Delta(s^2,s)
=-s^3 r^\top(D_AK)r+O(s^4).
}
\]

This is a precise local notion of **durable clean-rate amplification**: the shortcut changes neither current clean output nor first-order clean transfer, but changes the tangent geometry that controls subsequent clean contraction.

## 5. Exact positive, neutral, and harmful constructions

### 5.1 One clean model, two matched shortcut fields

Consider

\[
f(a,u)=au,
\qquad
L(a,u)=\frac12(au-y)^2.
\]

Its Jacobian and scalar NTK are

\[
J=(u,a),
\qquad
K=a^2+u^2.
\]

Define

\[
\psi(a,u)=\frac12(a^2-u^2),
\qquad
A_+=\nabla\psi=(a,-u),
\qquad
A_-=-A_+.
\]

Both directions are function-null:

\[
JA_+=ua-au=0,
\qquad
JA_-=0.
\]

They can be realized locally as shortcut gradient fields by

\[
L_s^+=L-\psi,
\qquad
L_s^-=L+\psi,
\]

because their flows satisfy

\[
H_+=F+A_+,
\qquad
H_-=F+A_-.
\]

At every state with `a>u>0`, both have `RT=1`, but

\[
D_{A_+}K=2(a^2-u^2)>0,
\]

and

\[
D_{A_-}K=-2(a^2-u^2)<0.
\]

Writing `r=au-y`, Theorem 1 gives

\[
\Delta_+(s^2,s)
=-2r^2(a^2-u^2)s^3+O(s^4)<0,
\]

while

\[
\Delta_-(s^2,s)
=+2r^2(a^2-u^2)s^3+O(s^4)>0.
\]

The two temporary signals have identical current clean transfer and identical first-order clean prediction, yet one helps future clean optimization and the other harms it.

### 5.2 Exact neutral independent shortcut

Add an independent parameter `z` that does not appear in `f` or `L`, and take

\[
A_0=c\,e_z.
\]

Then

\[
JA_0=0,
\qquad
D_{A_0}K=0.
\]

If the shortcut flow differs from clean flow only by this independent `z` update, the clean parameters `(a,u)` follow exactly the clean trajectory during exposure. After withdrawal the two clean trajectories are identical, so

\[
\boxed{\Delta_0(\eta,s)=0}
\]

for every exposure and continuation time, not just locally.

### 5.3 Fixed-kernel neutral class

For a linear clean predictor, `J` and `K` are parameter-independent. Every function-null excess direction satisfies

\[
D_AK=0.
\]

Thus the representation-rate term vanishes exactly. Fixed-kernel models may still display schedule effects through immediate output transfer or spectral state placement, but not through the function-null tangent-geometry catalyst isolated here.

## 6. Exact finite-continuation identity

Define the clean contraction rate

\[
\kappa(\theta)
=\frac{\|\nabla L(\theta)\|^2}{2L(\theta)},
\qquad L(\theta)>0.
\]

Along clean gradient flow,

\[
\frac{d}{dt}\log L=-2\kappa.
\]

For any two switch states `x_1,x_2` and clean continuation time `s`, integration gives the exact relation

\[
\boxed{
\log\frac{L(\Phi_F^s(x_1))}{L(\Phi_F^s(x_2))}
=\log\frac{L(x_1)}{L(x_2)}
-2\int_0^s
\left[
\kappa(\Phi_F^t(x_1))
-\kappa(\Phi_F^t(x_2))
\right]dt.
}
\]

This separates switch-state loss from durable future-rate advantage. It is exact but not yet prospective: the integral depends on the future clean trajectories. The local theorem replaces that future integral with a switch-time directional derivative plus smoothness-controlled remainder.

## 7. What has and has not been achieved

### Achieved

1. A formal positive/zero/negative law at matched total time.
2. Exact matching of current Relative Transfer in the positive and harmful constructions.
3. Under `JA=0`, exact matching of current clean prediction to first order.
4. A representation-only leading coefficient `r^T(D_AK)r`.
5. Exact neutral results for independent shortcuts and the function-null fixed-kernel class.
6. A concrete anti-core shared update with the opposite sign.

### Not achieved

1. The result is infinitesimal and local.
2. The positive and harmful cases use different auxiliary fields; one signal does not yet change sign over time.
3. The auxiliary potentials `L +/- psi` are normal-form constructions, not natural shortcut datasets.
4. No basin, stochastic-gradient, finite-step, random-initialization, or generalization theorem is supplied.
5. `D_A ||g||^2 = 2 A^T Hess(L) g` may already be an occupied second-order transfer quantity.
6. The exact finite-time rate integral is future-dependent and cannot itself serve as a prospective stopping rule.
7. No intrinsic upper withdrawal boundary has been recovered.

## 8. Internal decision

The Pro-requested positive/neutral/harm separation can be obtained locally, and it is genuinely beyond first-order Relative Transfer in the narrow mathematical sense. However, the proof is elementary once the right Taylor expansion is written, and the proposed coefficient is Hessian-gradient alignment.

```text
LOCAL_GENERAL_LAW: PROVED
MATCHED_RELATIVE_TRANSFER: YES
FUNCTION_NULL_REPRESENTATION_SPECIALIZATION: YES
POSITIVE_ZERO_NEGATIVE_EXAMPLES: YES
GLOBAL_OR_INTRINSIC_PHASE_BOUNDARY: NO
NATURAL_SHORTCUT_REALIZATION: NO
NOVELTY_BEYOND_SECOND_ORDER_TRANSFER: UNRESOLVED
GPU_AUTHORIZATION: 0
```

The narrow primary-literature search required by this decision found a direct mathematical collision, documented below. No GPU experiment is justified by this local result.

## 9. Binding collision audit

### 9.1 Level-set teleportation is the same local object

[Level Set Teleportation: An Optimization Perspective](https://arxiv.org/abs/2403.03362) studies the optimization problem

\[
\max_w\frac12\|\nabla L(w)\|^2
\quad\text{subject to}\quad
L(w)=L(\theta),
\]

and proves convergence improvements under additional Hessian-stability conditions. Its feasible tangent directions satisfy

\[
g^\top A=0,
\]

which is exactly this note's matched-Relative-Transfer condition. The directional derivative of the teleportation objective is

\[
D_A\left(\frac12\|g\|^2\right)
=A^\top\nabla^2L\,g
=\frac12D_A\|g\|^2.
\]

Therefore Theorem 1's positive coefficient is precisely infinitesimal ascent of the already-defined level-set teleportation objective. The local positive/negative law is a Taylor expansion explaining why teleportation helps or hurts, not a distinct new principle.

### 9.2 The function-null specialization is also occupied

[Teleportation With Null Space Gradient Projection for Optimization Acceleration](https://arxiv.org/abs/2502.11362) explicitly projects the teleportation objective's gradient into an input null space so that the loss/function is preserved while parameters move toward more favorable optimization geometry. It applies this construction to MLPs, CNNs, and transformers.

This directly occupies the stronger specialization

\[
JA=0,
\qquad
r^\top(D_AK)r>0,
\]

as an algorithmic mechanism. The present clean-NTK expression is a function-space rewriting of null-space teleportation's local objective.

### 9.3 Additional occupied components

- [Adaptive Auxiliary Task Weighting for Reinforcement Learning](https://proceedings.neurips.cc/paper/2019/hash/0e900ad84f63618452210ab8baae0218-Abstract.html) already selects auxiliary gradients by their long-term, multi-step effect on the main-task loss.
- [Auxiliary Task Update Decomposition: The Good, The Bad and The Neutral](https://arxiv.org/abs/2108.11346) already decomposes auxiliary updates into helpful, harmful, and first-order-neutral primary-task directions.
- [Auxiliary Learning by Implicit Differentiation](https://arxiv.org/abs/2007.02693) already learns auxiliary objectives through higher-order/implicit effects on the primary objective.
- [Careful with that Scalpel](https://arxiv.org/abs/2402.02998) explicitly optimizes auxiliary objectives in directions orthogonal to the main gradient.
- [A Theory of Neural Tangent Kernel Alignment and Its Influence on Training](https://arxiv.org/abs/2105.14301) already interprets evolving NTK alignment as feature learning that accelerates training.

Together these works occupy both the exact local mathematical quantity and the surrounding auxiliary-learning interpretation.

## 10. Final decision

The original scalar separation remains a valid normal-form example. The attempted generalization also remains mathematically correct. Neither supports a new Oral-level seed:

1. the original scalar model does not prove an intrinsic help-to-harm phase transition;
2. the general local replacement is level-set teleportation;
3. the null-space/NTK specialization is already an explicit teleportation algorithm;
4. presenting a temporary shortcut as an automatic carrier of teleportation would be an application-level relabeling unless it produced an additional, non-teleportation law;
5. no such irreducible law has been identified.

```text
LOCAL_GENERAL_LAW: MATHEMATICALLY_VALID
DIRECT_THEOREM_COLLISION: LEVEL_SET_TELEPORTATION
DIRECT_ALGORITHMIC_COLLISION: NULL_SPACE_TELEPORTATION
AUXILIARY_LONG_HORIZON_COMPONENTS: HEAVILY_OCCUPIED
TRANSIENT_SHORTCUT_ORAL_SEED: NO_GO
GPU_AUTHORIZATION: 0
NEXT_ACTION: CLOSE_C08_AND_RETURN_TO_NEW_SEED_DISCOVERY
```
