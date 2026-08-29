# Contradiction-First Seed Reset — 2026-08-30

## 0. Binding status

This reset deliberately abandoned literal billiards-to-agent mappings and searched for
sign reversals that survive a direct-collision audit. It does **not** authorize a full GPU
campaign.

Superseding decision after the direct-collision audit:

- **Primary theory-first falsifier:** endogenous failure conditioning and relational error
  depth in self-correction.
- **Killed:** trajectory fault gain. AgentChaos, FACT-E, SEED, controlled
  deletion-versus-replacement studies, and adaptive fault injection occupy the estimand
  and its most obvious reranking consequence.
- **Killed before experiment:** redundancy-conditioned intervention dose. Redundancy and
  target-retain entanglement alone do not identify the dose-response signs; aggregation
  structure can reverse them, while editing/unlearning dose control is already crowded.
- **Research hold:** forced-move verification through safe diagnostic probes.
- **Killed:** capability-consequence inversion as inferred from the public AgentDojo
  trajectory bundle.

The new primary candidate has a proved selection-induced sign reversal and a cheap crossed
generator-by-corrector falsifier. It is not yet an active paper seed.

## 1. What changed in the search

The previous search repeatedly translated a snooker principle into a mature AI object:
value, viability, risk sensitivity, reachability, process reward, redundancy, or error
shaping. This round instead required all of the following:

1. a standard AI metric or monotone intuition must rank two systems one way;
2. a second, prospectively measurable quantity must predict a ranking reversal;
3. the reversal must imply a different algorithm, not merely a new evaluation column;
4. the cheapest experiment must be able to kill the idea in one day;
5. primary literature must be treated as a positive adversary or mechanism foundation,
   not only as a reason to abandon the topic.

The useful billiards content is therefore only a generator of contradictions:

- a banked route can carry the same error magnitude along a good-position corridor;
- a harder pot can have a safer miss distribution;
- a dense cluster can justify a stronger intervention than a sparse cluster;
- a snooker forces an informative constrained response instead of passively judging an
  unconstrained move.

## 2. Killed natural-data anomaly: capability-consequence inversion

### 2.1 Initial anomaly

The public `sungjuncho/agentdojo-trajectories` bundle contains full trajectories for
Gemma 4 E4B IT and Qwen 3.5 9B. Using a predeclared set of externally mutating tools,
the exploratory audit found:

| quantity | Gemma | Qwen |
|---|---:|---:|
| utility success | 3,445 / 7,874 = 43.75% | 6,265 / 7,126 = 87.92% |
| utility failures | 4,429 | 861 |
| external mutation given utility failure | 25.76% | 55.52% |

Among 779 exact task-and-attack pairs on which both models failed utility, Qwen alone
crossed the mutation boundary in 209 cases and Gemma alone did so in 22. The direction
held in all seven attack families and all four suites.

### 2.2 Decisive negative control

AgentDojo already reports that more capable models can be easier to attack, an inverse
scaling result. The key negative control therefore conditioned on both models avoiding
the security failure as well as both failing utility. Only 91 matched pairs remained:

| mutation pattern | count |
|---|---:|
| neither | 4 |
| Gemma only | 0 |
| Qwen only | 2 |
| both | 85 |

The apparent capability-consequence effect disappears outside the known
capability-security trade-off. External mutation is also not equivalent to harm or
irreversibility. The seed is therefore **killed**, not weakened.

Reproduction script:
[`../../analysis/capability_consequence_inversion/explore_agentdojo.py`](../../analysis/capability_consequence_inversion/explore_agentdojo.py)

Mandatory collision: [AgentDojo](https://arxiv.org/abs/2406.13352).

## 3. Archived Candidate A — Trajectory Fault Gain (`KILL`)

### 3.1 Counterintuitive claim

> A locally correct or causally necessary reasoning step need not be a robust step. Two
> clean-correct trajectories with the same answer can have sharply different amplification
> of plausible intermediate faults; selecting or training for lower fault gain can improve
> end-to-end robustness even when it chooses a longer trajectory or one with a lower
> conventional process score.

This is not the claim that errors propagate, that long chains are fragile, or that some
tokens matter more. The separating object is the response to a *plausible local fault*.

For a clean trajectory

\[
\tau=(s_1,\ldots,s_T), \qquad Y(\tau)=y,
\]

let \(Q_i(\cdot\mid s_i)\) be a frozen, task-valid local fault channel at step \(i\), and
let \(\tau_{i\leftarrow\delta}\) denote continuation from the perturbed prefix. Define

\[
G_i(\tau;Q)=
\mathbb E_{\delta\sim Q_i}
\left[\ell\!\left(Y(\tau_{i\leftarrow\delta}),y^*\right)
-\ell\!\left(Y(\tau),y^*\right)\right],
\]

and a trajectory fault gain

\[
\kappa_Q(\tau)=\sum_i w_i G_i(\tau;Q)
\quad\text{or}\quad
\kappa_Q^{\max}(\tau)=\max_i G_i(\tau;Q).
\]

Three quantities must remain separate:

| quantity | intervention | question |
|---|---|---|
| local correctness | judge/oracle labels the existing step | is the step right? |
| causal necessity | delete or mask the step | is the step used? |
| fault gain | insert a plausible wrong local state and continue | how much does a small fault get amplified? |

A necessary step can have low fault gain because its downstream representation contains
checks or invariances. An apparently optional step can have high fault gain when a wrong
version controls a later bottleneck. This separation is the proposed novelty hinge.

### 3.2 Why the nearest papers do not automatically kill it

- [Beyond Uniform Credit](https://arxiv.org/abs/2602.09331) masks spans and weights
  policy gradients by their causal contribution to the final answer. It estimates
  necessity, not response to a distribution of plausible wrong states.
- [Efficient Forecasting of Task Failures through Adaptive Fault Injection](https://openreview.net/pdf/f81b4d72b4ac58cbc7ec781bdc3f8e3c705d4650.pdf)
  predicts whether a partial agent trace is safe to continue. It is the strongest method
  collision: a fault-gain paper must beat generic prefix failure forecasting and show that
  *trajectory choice* changes under matched clean success.
- [Fragile Reasoning](https://arxiv.org/abs/2604.01639) introduces a layer-wise Cascading
  Amplification Index for meaning-preserving input perturbations. It is a positive
  adversary: the proposed work must intervene on intermediate computational states and
  compare alternative clean-correct paths, not rename input robustness.
- [Stepwise Reasoning Error Disruption](https://arxiv.org/abs/2412.11934) demonstrates
  that injected reasoning errors can break models. A new result requires path-level
  ranking, prospective prediction, and an intervention that improves robustness.
- [Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341) and
  [Verifiable Process Supervision](https://arxiv.org/abs/2605.12519) establish that process
  scores and outcomes can be misaligned. They do not establish that optimizing local
  correctness selects higher-gain trajectories.

The theory is adjacent to numerical conditioning and fault-tolerant computation. A paper
cannot claim the abstract idea of error amplification as new. The contribution must be a
measurable separation from correctness and causal importance in generated reasoning.

### 3.3 One-day kill test

Use open 7B and 14B reasoning models and no training in the first pass.

1. Generate 4--8 clean-correct, answer-equivalent trajectories per problem on GSM8K and a
   frozen MATH-500 subset.
2. Parse only mechanically verifiable numerical, symbolic, or tool-result states.
3. Freeze fault channels before model comparison: sign flip, off-by-one, unit swap,
   operand substitution, stale tool result, and one domain-specific fault.
4. For each path, estimate fault gain from one subset of fault types.
5. Test whether it ranks held-out fault types and independent continuations.
6. Compare reranking against clean log-probability, length, PRM score, per-step
   correctness, masking-based causal importance, and a prefix failure forecaster.
7. Replicate the central ranking result on an executed tool/code carrier to address
   chain-of-thought unfaithfulness.

Automatic **KILL** if any condition holds:

- within-problem variation in fault gain is negligible after matching clean correctness;
- incremental AUROC over length, PRM, causal importance, and prefix forecasting is below
  `0.05`;
- reranking improves held-out-fault success by less than `5 pp`, or costs more than
  `2 pp` clean success;
- rankings do not transfer across at least two fault families;
- the effect disappears on executed states and exists only in free-form chain of thought;
- the useful signal requires observing final failures used to fit the same examples.

### 3.4 Oral ceiling

The result becomes broadly interesting only if it shows a reversal such as:

> process-supervised or higher-PRM trajectories are cleaner locally but have greater
> held-out fault gain, while fault-gain-aware selection or training reverses the robustness
> ranking under matched clean accuracy and compute.

A new metric plus a small reranking gain is a poster-level contribution at best.

## 4. Archived Candidate B — Redundancy-Conditioned Intervention Dose (`KILL`)

### 4.1 Counterintuitive claim

> A target represented more redundantly may require a stronger edit to remove, yet can
> initially tolerate a stronger edit with less non-target damage. The usual monotone
> erase-utility trade-off is therefore conditional on two distinct pre-intervention
> quantities: target redundancy and target-retain entanglement.

This candidate is inspired by the reversal between aggressively opening a dense red-ball
cluster and gently separating a sparse two- or three-ball cluster. It is not a claim that
distributed knowledge is simply hard to erase.

Let component-wise causal target scores be \(a_j\ge0\). A first prospective redundancy
measure is the participation ratio

\[
R=\frac{(\sum_j a_j)^2}{\sum_j a_j^2}.
\]

Let \(E\) measure overlap between target-support and retain-support interventions. For
intervention dose \(d\), define forgetting \(F(d)\) and collateral utility loss \(C(d)\).
The pre-registered directional hypothesis is:

\[
\frac{\partial d^*}{\partial R}>0,
\qquad
\left.\frac{\partial^2 C}{\partial d\,\partial R}\right|_E<0
\quad\text{for low-to-moderate }E,
\]

where \(d^*\) is the minimum dose reaching a fixed forgetting target. At high
entanglement, the second sign may reverse. Thus `distributed` and `entangled` must not be
used as synonyms.

### 4.2 Collision boundary

- [Does Localization Inform Editing?](https://arxiv.org/pdf/2301.04213) finds that common
  localization signals do not predict the best edit location. This is a positive
  adversary: a redundancy statistic must predict a dose-response curve out of sample, not
  merely correlate with localization.
- [Capability Localization](https://arxiv.org/abs/2502.20992) argues that capabilities can
  be more stably localized than individual facts.
- [CRU](https://openreview.net/pdf?id=mySXIkXEdi) and
  [MUTE](https://arxiv.org/abs/2602.22562) already adapt *where* to intervene based on
  representation structure.
- [Model Editing Harms General Abilities](https://arxiv.org/abs/2401.04700) and
  [Unlearning with Control](https://arxiv.org/abs/2406.09179) establish excessive-editing
  damage and strength control.
- [LLM Unlearning Coresets](https://arxiv.org/abs/2504.10185) shows that current
  benchmarks can be dominated by compact keyword effects, so a standard WMDP-only result
  is inadmissible.

No located primary paper directly establishes the two-sign law above. However, the
neighborhood is crowded and evaluation is fragile.

### 4.3 Cheapest credible falsifier

1. Use one 1.5B--3B model for a synthetic controlled phase and one 7B model for a natural
   replication.
2. Manipulate target redundancy at matched target-token count using independently
   paraphrased/contextualized encodings, not raw repetition count alone.
3. Measure pre-edit participation ratio and target-retain support overlap with frozen
   causal ablations.
4. Sweep the same dose grid for GA/NPO or RMU plus one localization-based method.
5. Estimate the forgetting threshold and collateral-loss slope before inspecting the
   natural benchmark.
6. Replicate on TOFU/LKF-like facts or a capability target; do not use WMDP as the sole
   evidence.

Automatic **KILL** if:

- redundancy adds less than `0.05` held-out \(R^2\) beyond exposure count, base
  confidence, gradient norm, and target frequency;
- the predicted dose sign fails in either architecture;
- collateral slope is fully explained by target-retain semantic similarity;
- natural and controlled regimes disagree in sign;
- robust forgetting under paraphrase/relearning does not track the claimed threshold.

### 4.4 Oral ceiling

The ceiling is higher than Candidate A because a prospective `(redundancy, entanglement)`
phase diagram could change how unlearning/editing strength is selected. The cost is a
much higher risk of confounding and benchmark failure. A single adaptive hyperparameter
heuristic is not enough.

## 5. Candidate C — Forced-Move Verification

### 5.1 Claim

Instead of passively scoring a complete agent plan, a supervisor selects a reversible,
low-consequence environment action whose possible outcomes maximally separate valid and
invalid latent plans. The agent is forced to react before any irreversible action.

This differs from asking for an explanation. The probe must change or query the real
task state: a discriminating test, dry run, readback, quote, permission check, or
postcondition query.

The strongest possible reversal is:

> a weaker supervisor that controls one diagnostic probe outperforms a stronger passive
> verifier under the same token and tool budget.

### 5.2 Why it remains a hold

Cross-examination, active diagnosis, AI-control resampling/deferral, failure forecasting,
and tool postcondition checks are all strong neighbors:

- [Scalable AI Safety via Doubly-Efficient Debate](https://openreview.net/pdf?id=6jmdOTRMIO)
- [Evaluating Control Protocols for Untrusted AI Agents](https://arxiv.org/abs/2511.02997)
- [REFLECT](https://arxiv.org/abs/2606.09071)
- [Failing Tools](https://openreview.net/pdf?id=j7YsSnA64D)

The candidate reopens only if a formal probe-selection objective and a benchmark with
multiple admissible state-changing probes can be specified without constructing an entire
new environment. Until then it is not the fast path.

## 6. Comparative decision

| candidate | novelty headroom | one-day falsifiability | engineering burden | main fatal risk | decision |
|---|---:|---:|---:|---|---|
| trajectory fault gain | low after collision audit | high | medium | directly occupied by fault injection and deletion/replacement work | **KILL** |
| redundancy-conditioned dose | low after identification audit | medium | high | redundancy/entanglement do not determine dose-response signs | **KILL** |
| forced-move verification | medium-high | low-medium | high | cross-examination/postcondition-checking equivalence | **HOLD** |
| capability-consequence inversion | low after control | completed | low | known AgentDojo inverse scaling | **KILL** |

The superseding sequence is:

1. preserve the killed candidates as provenance and do not run their proposed pilots;
2. test the diagonal non-identification and relational-error-depth candidate described in
   [`../theory/ENDOGENOUS_FAILURE_CONDITIONING_NOTE.md`](../theory/ENDOGENOUS_FAILURE_CONDITIONING_NOTE.md);
3. promote it only if the complete crossed matrix reveals a replicated relational
   interaction and an equal-budget routing consequence.

Minimal theory separation:
[`../theory/TRAJECTORY_FAULT_GAIN_NOTE.md`](../theory/TRAJECTORY_FAULT_GAIN_NOTE.md).
