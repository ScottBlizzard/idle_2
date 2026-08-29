# Oral-Seed Literature-Role Re-audit

**Audit date:** 29 August 2026  
**Input:** `AI_RESEARCH_ORAL_SEED_DIVERGENCE.md`  
**Decision:** **`NO_GPU_RUN — ONE_THEORY_FIRST_HOLD`**

## 1. Why this re-audit was necessary

The Pro divergence report correctly refused to manufacture an Oral-level seed, but its literature rule was too close to binary duplicate detection: nearby work frequently became a reason to reject a candidate even when that work could instead serve as a theoretical foundation, a mandatory baseline, or a positive adversary whose opposite result needs explanation.

This audit replaces that rule with a five-role classification.

| Literature role | Meaning | Default decision |
|---|---|---|
| **Direct collision** | Same central scientific claim, causal mechanism, decisive intervention, and consequence are already present | KILL |
| **Positive adversary** | A credible paper predicts the opposite sign or embodies the field's default belief | Potential opportunity; require a condition that explains both results |
| **Mechanism foundation** | The paper supplies a component, theorem, or vocabulary but not the proposed conditional law | Cite and build on it; not novelty by itself |
| **Mandatory baseline** | The paper supplies the strongest simpler explanation or remedy | Candidate survives only if it defeats this baseline |
| **Unexplained anomaly** | The paper reports a residual, reversal, subgroup, or ablation without a unifying explanation | High-value clue if the new claim predicts it prospectively |

A direction is bindingly killed by literature only when the closest work substantially matches the **claim, mechanism, intervention, and consequence**. Overlap on a carrier or one component is insufficient.

## 2. Executive result

The corrected rule does **not** turn the Pro report into an experiment authorization.

- Most of the 15 candidates remain closed.
- C11 is more directly occupied than the Pro report recognized.
- C07 remains mathematically clean but its consequence is already a mature model--solver co-design program.
- C04 is a legitimate representation-factorization question but currently lacks a surprising cross-domain law.
- C08 was rejected too quickly. Its cited papers contain a useful conflict rather than a single settled answer.

The sole retained research question is therefore:

> **Can a training-only shortcut have a predictable help-to-harm phase transition—accelerating invariant feature acquisition when withdrawn before shortcut-margin saturation, but suppressing it when retained beyond that point?**

This is a **theory-first HOLD**, not a seed and not an experiment authorization. The next gate is to establish that a non-empty beneficial regime exists in a controlled learning model and that its boundary is not merely an ordinary validation-tuned curriculum schedule.

## 3. Candidate reclassification

| ID | Pro disposition | Correct literature roles | Re-audit disposition | Reason |
|---|---|---|---|---|
| C01 trainer-state hysteresis | KILL | Direct collision + foundation | **KILL** | Moment-only causal memory and optimizer-state transport are already the object; changing the remembered source to a shortcut is an application change. |
| C02 neuron-cloning arbitrariness | KILL | Direct collision + invariant baseline | **KILL** | Gauge/non-identifiability work already makes coordinate-level causal stories non-invariant; quotient/subspace attribution is the direct remedy. |
| C03 SAE reconstruction--causality inversion | KILL | Foundation + mandatory grouped/subspace baseline | **KILL AS SEED** | A sharper monotone inversion plot could be useful, but feature splitting and causal validation already predict it. |
| C04 full-state versus delta scratchpads | HOLD | Foundation + positive adversary | **HOLD, LOW PRIORITY** | Information-equivalent trace factorization is not directly closed, and causal-register work makes the question meaningful. The likely result still reads as representation-dependent inductive bias unless it yields a predictive computational-depth law. |
| C05 multimodal alignment erases synergy | KILL | Direct mechanism collision | **KILL** | PID/partial-alignment work already states the redundancy--synergy tradeoff and supplies the remedy. |
| C06 orthogonal adapters interfere | KILL | Near-direct collision + mandatory functional-geometry baseline | **KILL** | PermDoRA already reports that angular alignment and orthogonality are weak composition predictors and points to nonlinear shared-representation interactions. |
| C07 score error cancels solver error | REJECT | Foundation + positive adversary + mature baseline | **HOLD AS NUMERICAL NOTE, NOT SEED** | The exact cross-term could be new, but DPM-Solver-v3 and Bespoke Solvers already operationalize model-conditioned numerical design. The obvious consequence is occupied. |
| C08 temporary shortcut scaffold | REJECT | **Positive adversaries on both sides** + foundation + mandatory baselines | **PRIORITY THEORY-FIRST HOLD** | Spurious-feature dynamics predict inhibition, whereas training-time hints and bias-amplification methods show that temporary auxiliary bias can improve no-hint or robust endpoints. The unresolved object is the sign boundary, not whether either sign can occur. |
| C09 quotient-level distillation | KILL | Direct collision | **KILL** | Representation equivalence classes and normalized/invariant distillation directly cover the claim and remedy. |
| C10 duplicate topology | KILL | Foundation + direct covariance explanation | **KILL** | If per-example targets and mean gradients differ, ordinary statistics explain the result; if all relevant gradient distributions are matched, the remaining training process is identical. |
| C11 logical token clock | REJECT | **Near-direct collision** + positional baselines | **KILL AS ORAL SEED** | Position Coupling already assigns shared position IDs to structurally related tokens, obtains large length generalization gains, and proves a depth separation. The proposed quotient clock is a clean replication/generalization, not a new principle. |
| C12 teacher co-error topology | KILL | Foundation + structural identifiability check | **KILL** | With a fixed student, optimizer, batches, and per-example aggregate soft targets, teacher identity and higher-order topology cannot affect the gradient. Without matching aggregate targets, ordinary target differences explain the result. |
| C13 strategically wrong demonstration | KILL | Direct phenomenon collision + selection baseline | **KILL** | Negative demonstrations and learning from mistakes are established; version-space selection is a plausible selector, not a new causal law. |
| C14 gauge-equivalent checkpoints under Adam | KILL | Direct collision | **KILL** | The basis sensitivity of Adam and state transport are already the central result. |
| C15 sink-selective quantization improvement | KILL | Foundation + strong systems baselines | **KILL AS SEED** | The reversed sign may exist, but evaluator sensitivity, perturbation regularization, and established sink-preservation methods dominate the interpretation. |

## 4. Why C08 changes category

### 4.1 The cited literature does not all say the same thing

The following papers are not duplicates of C08; they occupy different sides of a conflict.

**Shortcut-inhibition side.**

- [Complexity Matters](https://arxiv.org/abs/2403.03375) finds that simpler or more strongly correlated spurious features slow core-feature learning and are not forgotten.
- [SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model](https://arxiv.org/abs/2606.30444) derives phases in which rapid shortcut growth and majority-margin saturation suppress the XOR signal.
- [Beyond Distribution Shift](https://arxiv.org/abs/2302.09344) distinguishes benign from harmful spurious features by their learnability relative to the core feature, but does not establish a regime where a deliberately temporary easy shortcut improves the final invariant representation.

These are **positive adversaries**: the retained hypothesis must explain their harmful regime rather than evade it.

**Training-only-scaffold side.**

- [Learning to Hint for Reinforcement Learning](https://arxiv.org/abs/2604.00698) shows that adaptive training-time hints can create transferable updates for the no-hint policy and introduces hint reliance as a transfer diagnostic.
- [Learning from Failure](https://arxiv.org/abs/2007.02561) deliberately amplifies a biased model and uses its failures to train a debiased model.
- [Bias Amplification Enhances Minority Group Performance](https://arxiv.org/abs/2309.06717) uses an explicit bias-amplification stage before robust reweighting.
- [Removing Spurious Features Can Hurt Accuracy](https://arxiv.org/abs/2012.04104) shows that deleting spurious inputs can reduce accuracy under model inductive bias, although it does not study transient exposure or invariant-feature acquisition.

These papers prove that “bias or extra training-only signal can help” is not itself novel. They are foundations and mandatory baselines. What remains potentially new is a **single-model conditional law** predicting when the same transient shortcut changes from scaffold to poison.

### 4.2 Sharpened candidate: Transient Shortcut Phase Transition

Let a model receive a core feature (x_c) and a training-only shortcut (x_s). During the first phase, (x_s) is correlated with the label; after a fixed withdrawal time τ it becomes uninformative or is removed. Let (G_c(t)) denote progress on a core-only probe or a core-feature population objective.

The candidate is not the weak statement

> “a temporary shortcut sometimes helps.”

The candidate is the stronger signed prediction

\[
\Delta G_c(\tau)
:=
G_c^{\text{shortcut}\to\text{clean}}(T;\tau)
-
G_c^{\text{clean}}(T)
\]

with a prospectively identifiable transition:

\[
\Delta G_c(\tau)>0
\quad\text{for}\quad
0<\tau<\tau^*,
\qquad
\Delta G_c(\tau)<0
\quad\text{for}\quad
\tau>\tau^*.
\]

The hypothesized mechanism contains two competing terms:

1. **alignment/scaffolding:** early shortcut gradients align shared representation or output signs with the core task, reducing the optimization barrier for the harder invariant feature;
2. **margin suppression/reliance:** once shortcut-driven margins become large, loss gradients on majority examples vanish and the core feature is starved of updates.

The transition τ* must be predicted from a pre-outcome statistic combining shortcut--core representation-gradient alignment and shortcut-margin saturation. Selecting τ by validation would reduce the contribution to ordinary curriculum tuning.

### 4.3 Why this might matter

If valid, the result would connect literatures currently framed separately:

- shortcut learning and spurious-correlation suppression;
- learning using privileged information;
- training-time hints and scaffolded reasoning;
- curricula and continuation methods;
- bias amplification used for robust learning.

The broad claim would be that **training-only information is neither generically helpful nor harmful; its sign is controlled by a measurable dynamical phase boundary**. Existing papers supply both sides of the phenomenon, while the proposed law would explain when each side applies.

## 5. Why this is not yet an Oral seed

Several serious collapse modes remain.

1. The beneficial regime may be empty in the simplest honest model; shortcut margins may only suppress core learning.
2. Any apparent gain may reduce to ordinary privileged information or an easy-to-hard curriculum.
3. The transition may require measuring the final outcome or tuning τ, making it retrospective rather than predictive.
4. Gradient alignment may merely become another hyperparameter selector rather than a new law.
5. A synthetic phase diagram may not transfer to natural representations or language-model hinting.
6. Bias-amplification and hint-reliance work may already supply all useful algorithmic consequences even if the same-model theorem is new.

The full Phase-I analysis in the 2026 XOR shortcut paper makes the first risk concrete: during early shortcut growth, the non-spurious signal weights remain close to initialization while the shortcut component grows rapidly; later, majority-margin saturation suppresses signal acquisition. Merely withdrawing an **independent** shortcut before the harmful phase may therefore remove damage without ever outperforming clean-only learning. A genuinely positive theorem may require the temporary cue to share an upstream representation with the core feature. That requirement must be formalized carefully, because an arbitrarily chosen shared cue can collapse into ordinary privileged information.

Therefore no GPU run is authorized.

## 6. Binding theory-first gate

Before any implementation or benchmark work, a follow-up must answer four questions.

### Gate T1 — Existence

Construct a minimal analytically tractable learner in which a temporary shortcut strictly improves a core-only population objective over clean-only training at matched steps and information available at deployment. If the beneficial regime requires changing capacity, adding a second model, reweighting data after observing failures, or retaining the shortcut at deployment, **KILL**.

### Gate T2 — Sign transition

Prove or derive a prospectively testable sufficient condition for both signs and a finite τ*. A post-hoc non-monotonic curve without a location prediction is insufficient.

### Gate T3 — Nontriviality against foundations

Show why the result is not already implied by:

- generic learning using privileged information;
- easy-to-hard curricula or continuation/homotopy;
- two-model bias amplification and failure reweighting;
- hint reliance or extra label information;
- ordinary gradient alignment in multi-task learning.

The contribution must isolate a fact specific to the **same feature being initially useful, deployment-spurious, and dynamically sign-changing**.

### Gate T4 — Consequence

State one prospective intervention other than validation-tuning the withdrawal time. A credible option is a stopping rule using only training-time margins and gradient geometry that transfers across two learning systems. If no non-obvious consequence exists, retain the result as theory/diagnostic work rather than an Oral seed.

Only if all four theory gates pass may a separately preregistered CPU/small-GPU Stage 0 be designed.

## 7. Initial theory-existence probes

Two deterministic CPU checks were performed after fixing the theory-first question. They are exploratory and cannot satisfy the gates above.

1. **Deep linear factorization:** no beneficial shortcut-exposure interval was observed across five correlation strengths. Zero exposure always minimized the final core-distribution loss. This rules out the idea that a positive phase follows generically from faster norm growth or factorized optimization.
2. **Nonlinear XOR feature learning:** a width-8 tanh MLP trained on exact full-batch distributions showed a small long-horizon loss improvement for short exposure and a clear loss penalty for longer exposure. For shortcut correlations `0.90--1.00`, the best observed exposure was approximately 20 of 1,000 updates; exposure through 160 or more updates was harmful. The early benefit appeared in 8--9 of 10 paired seeds, but accuracy was already saturated. At a 200-update horizon, benefits were inconsistent across loss and accuracy.

The nonlinear result was initially a **weak existence signal**, not a discovered law. At this checkpoint it suggested that a sign transition might exist in nonlinear representation dynamics, but did not establish invariant-feature improvement, a prospective location predictor, or external validity. The subsequent theory result below supersedes only the statement that the analytical gate was unpassed; GPU authorization remains zero.

- Exploratory code and exact summary: [`../../analysis/transient_shortcut_phase_transition/README.md`](../../analysis/transient_shortcut_phase_transition/README.md)

### Subsequent analytical resolution — 29 August 2026

A three-parameter gradient-flow construction now proves a matched-horizon asymptotic separation: clean-only and permanent-shortcut learning retain order-one core loss on a logarithmic horizon, whereas state-triggered shortcut withdrawal reaches an arbitrarily small fixed core loss in logarithmic time. The construction has exact invariants and an exact shortcut-phase relation `u = epsilon * exp(2(v - epsilon))`.

The nonlinear XOR probe was also instrumented with training-state diagnostics. One common shortcut-aligned margin threshold (`0.40`) adapted the withdrawal step across four shortcut correlations and improved final clean loss in every condition, with 8--9 of 10 paired seeds improving. This makes T1/T2/T4 plausible in a stylized sense; T3 and external generality remain unresolved.

- Formal note: [`../theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md`](../theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md)
- Current Pro audit prompt: [`../pro/PRO_TRANSIENT_SHORTCUT_CATALYSIS_THEORY_AUDIT.md`](../pro/PRO_TRANSIENT_SHORTCUT_CATALYSIS_THEORY_AUDIT.md)

## 8. Decisions for the other near-misses

### C07 — solver cross-cancellation

Keep as a technical note only. [DPM-Solver-v3](https://arxiv.org/abs/2310.13268) minimizes model-dependent discretization error using empirical model statistics, while [Bespoke Solvers](https://arxiv.org/abs/2310.19075) explicitly fits a solver to a pretrained flow. The proposed error cross-term could explain a local reversal, but the practical consequence—condition the solver on the model—is already central to the field.

### C11 — logical token clock

Close as the main seed. [Position Coupling](https://arxiv.org/abs/2405.20671) already replaces unique token positions with shared structure-aware position IDs, demonstrates substantial arithmetic length generalization, and provides a depth-separation theorem. The exact microtoken-refinement experiment could still be pedagogically clean, but it no longer clears the novelty or consequence bar.

### C04 — information-equivalent scratchpads

Retain only as a low-priority question. [Do Models Read What They Write?](https://arxiv.org/abs/2606.29522) demonstrates that written scratchpad states can become causally used registers. A strong future C04 would need to predict when two bijective traces induce different computational depth or causal register structure—not merely report that format affects length generalization.

## 9. Operational decision

```text
NO_GPU_RUN
ONE_THEORY_FIRST_HOLD: TRANSIENT_SHORTCUT_PHASE_TRANSITION
```

The project still has no authorized GPU-scale experimental seed. Mathematical feasibility is now established for a stylized construction, so the immediate next action is a fresh hostile audit of proof correctness, direct literature collisions, general-law potential, and Oral-level significance. Only a positive audit may authorize a separately preregistered Stage 0.
