# Closed-Loop Bracket Steering: Independent Seed Audit

Date: 2026-08-28

Source proposal: [`../proposals/AI_RESEARCH_NEW_SEED_DIVERGENCE.md`](../proposals/AI_RESEARCH_NEW_SEED_DIVERGENCE.md)

Binding verdict: **`NO_GO_AS_CURRENTLY_FORMULATED`**

## Executive decision

The proposal's exact literal combination appears unoccupied: the audit found no prior paper that uses a zero-first-order group-commutator activation loop at inference time, predicts a third behavior, verifies reversal and quadratic scaling, and beats matched static and nonlinear controllers.

That literal vacancy is not sufficient novelty. At a fixed transformer layer and token position, the suffix receives only the final hidden state. It cannot observe how that state was produced. Exact replay of the loop's final displacement must therefore reproduce the same deterministic logits, and direct injection of the already-computed bracket vector should approximate the loop to second order. The proposed loop is consequently a way to compute a final activation perturbation, not a privileged path-causal control mechanism.

The central analogy with nonholonomic control breaks here. A physical robot may be unable to actuate directly along a Lie-bracket direction and must synthesize it by a loop. Transformer activation editing normally permits an arbitrary vector to be written directly. Once

\[
B(h)=[U,V](h)=J_V(h)U(h)-J_U(h)V(h)
\]

has been computed, one can inject \(\epsilon^2B(h)\), or its component outside \(\operatorname{span}\{U,V\}\), without executing the four-step loop.

Do not spend the proposed 34–60 GPU-hours on Stage 0. A radically narrower source-only bracket-feature question is retained as a **HOLD**, but it is a different seed and is not currently authorized for experimentation.

## Review setup

- **Material reviewed:** the full divergence report, including all 17 candidate seeds, the collision table, red-team section, Seed A protocol, thresholds, compute plan, and 72-hour execution plan.
- **External verification:** primary paper pages and official repositories were checked through 2026-08-28.
- **Review roles:** Reviewer 1 emphasizes mathematics and causal identification; Reviewer 2 emphasizes novelty and significance; Reviewer 3 emphasizes engineering feasibility, benchmarks, and reproducibility.
- **Scope boundary:** this is a seed audit, not a review of completed experimental evidence. No experiment was started and no server state was modified.

## Reviewer 1 — mathematics and causal identification

### Overall assessment

The local Baker–Campbell–Hausdorff expansion is valid for smooth vector fields and accurately integrated flows on the same hidden-state space:

\[
\Phi^V_{-\epsilon}\circ\Phi^U_{-\epsilon}\circ
\Phi^V_{\epsilon}\circ\Phi^U_{\epsilon}(h)
=h+\epsilon^2(DV\,U-DU\,V)+O(\epsilon^3).
\]

However, the proposal over-interprets this identity as new behavioral accessibility and path dependence.

### Who would be interested and why

Researchers in activation steering, mechanistic interpretability, and nonlinear control may value a careful empirical account of bracket-derived activation features. They would not accept a standard BCH residual by itself as a new control capability.

### Major strengths

- The hypothesis is falsifiable and includes reversal and scale-law checks.
- The report correctly recognizes that noncommutativity, nonlinear steering, and feedback are not themselves novel.
- The intended use of two source behaviors to predict a third is more interesting than merely measuring order sensitivity.

### Major concerns

1. **Fatal final-state equivalence.** If all four substeps occur at one fixed layer and token position, the downstream transformer computes only
   \[
   y=M_{\ell:}(h+\delta_{\mathrm{loop}}).
   \]
   Reinjecting the measured \(\delta_{\mathrm{loop}}\) must give the same deterministic logits up to numerical error. The suffix has no path memory.

2. **Direct bracket dominance.** The proposal computes \([U,V]\) to predict the effect but omits direct \(\epsilon^2[U,V]\) injection and projected-bracket injection from the mandatory baselines.

3. **Weak accessibility comparison.** A time-varying four-step controller over \(U,V\) already contains the proposed loop as a special case. Exiting the instantaneous two-dimensional span is classical Lie closure, not exiting the nonlinear controller's reachable set.

4. **Vacuous geometry threshold.** In a residual dimension of thousands, a generic vector will lie mostly outside a two-dimensional span. The proposed \(\rho\ge0.35\) gate lacks a dimension-aware random-field null and depends on the residual-space metric.

5. **Probe-manufactured curvature.** For gradient fields,
   \[
   [\nabla f,\nabla g]=H_g\nabla f-H_f\nabla g.
   \]
   Nonlinear probes therefore manufacture the Hessians that create the bracket; this does not identify intrinsic transformer geometry.

6. **Normalization is not neutral.** For state-dependent scalars \(a,b\),
   \[
   [aU,bV]=ab[U,V]+aU(b)V-bV(a)U.
   \]
   Normalization changes the finite trajectory, bracket norm, and target projection.

### Technical failings

- Three positive epsilon values are insufficient to distinguish quadratic scaling from leakage, saturation, and integration error.
- RK2/RK4 agreement within 10% is too loose for a second-order signal.
- Constant-field controls do not cover commuting state-dependent fields, \(U=V\), or colinear fields.
- The hidden-state object and intervention location are underspecified: last prompt position versus all positions, prefill-only versus every generated token, layer input versus output, and pre- versus post-normalization.
- Distributing interventions across layers or decode positions could introduce genuine path dependence, but then the four flows no longer act on a single fixed state space and the stated bracket derivation no longer applies without a new formulation.

### Assessment axes

- Technical soundness: **2/5**
- Causal identification: **1/5**
- Falsifiability: **4/5**
- Reproducibility as written: **2/5**

### Recommendation posture

**Reject the current mechanism claim.** A loop experiment may verify the BCH identity, but that is a numerical sanity check rather than an ML discovery.

## Reviewer 2 — novelty and significance

### Overall assessment

The exact four-step behavior-synthesis formulation appears literally vacant, but the useful claim is squeezed between classical control theory and strong nonlinear activation-steering work. The proposal currently confuses an unoccupied implementation detail with paper-level algorithmic novelty.

### Who would be interested and why

The work could interest the representation-control community if it established a surprising zero-target compositional generalization law or a theorem separating loop and direct-bracket interventions. Without that separation, the likely ceiling is a workshop diagnostic.

### Major strengths

- The report conducted broad collision search and did not claim that Lie brackets themselves were new.
- It correctly identified direct nonlinear control as the strongest threat.
- No retrieved paper implements the proposal's full conjunction of active group commutator, third-behavior prediction, reversal, quadratic scaling, and matched-controller advantage.

### Major concerns

- [Feed-Forward Steering in Transformer Residual Dynamics](https://arxiv.org/abs/2608.02071) already formulates transformer residual dynamics using local steering fields and commutator defects.
- [Inverse-Free Wilson Loops for Transformers](https://arxiv.org/abs/2510.08648) already uses activation-level commutators and JVP-based curvature/order diagnostics.
- [Steering Vector Fields](https://arxiv.org/abs/2602.01654) already provides state-dependent differentiable activation fields.
- [FLAS](https://arxiv.org/abs/2605.05892) learns curved, multi-step, token-varying activation trajectories and reports stronger AxBench results than prompting; it is a mandatory core baseline, not an optional add-on.
- ODESteer, PID feedback steering, INNSteer, model-based LQR steering, dynamic multi-property composition, and nonlinear interventions further occupy the surrounding algorithmic space.
- Classical bracket-generating controllability already predicts directions outside the instantaneous source span. Therefore “outside \(\operatorname{span}\{U,V\}\)” is not a sufficient novelty target.

### Technical failings

- The report omits the most obvious same-information controls: direct bracket injection, projected bracket residual, a bracket-augmented one-step optimizer, and an arbitrary time-varying source-field controller.
- A global static-span oracle is intentionally weaker than an example-adaptive nonlinear controller.
- The target scorer is used for triple selection and effect prediction while the proposal also gestures at “zero-target-training.” Target-guided selection is target information.
- Discovery on Gemma plus Benjamini–Hochberg correction is not confirmation; the untouched model must carry the confirmatory inference.

### Assessment axes

- Literal vacancy: **4/5**
- Algorithmic novelty: **2/5**
- Potential significance if all strong controls are beaten: **4/5**
- Probability of surviving those controls: **1/5**

### Recommendation posture

**`NO_GO_AS_CURRENTLY_FORMULATED`.** Literal vacancy is real; paper-worthy distinctiveness is not. The method is likely dominated by direct bracket injection or subsumed by nonlinear control.

## Reviewer 3 — engineering feasibility and benchmark validity

### Overall assessment

The small-probe geometry is implementable on one RTX 4090. The full Stage 0 protocol is not implementation-ready, and its 34–60 GPU-hour / 72-hour estimate is not credible under the stated search matrix, model-native derivatives, behavioral generation, and baseline suite.

### Who would be interested and why

Practitioners could reproduce a narrowly specified hidden-state bracket smoke test. They cannot currently reproduce the claimed end-to-end behavior study without making many consequential choices that the protocol leaves open.

### Major strengths

- Gemma-2-2B-it and Qwen2.5-3B-Instruct fit individually on 24 GB cards for ordinary inference and small-probe interventions.
- AxBench and SteeringSafety provide useful public data or infrastructure.
- The available 8×RTX 4090 resource is sufficient for a corrected, tightly bounded experiment; hardware is not the scientific blocker.

### Major concerns

1. **Combinatorial undercount.** With 8 concepts, ordered source-pair/third-target triples, 3 layers, 3 scales, and both orientations create 6,048 conditions; with 12 concepts, 23,760. At 50 prompts each this is roughly 302,000–1,188,000 generations.
2. **Second-order transformer cost.** A model-native field requires a backward pass through the suffix; its bracket requires a Hessian-vector product or double backward. A four-segment loop costs 8 field evaluations with RK2 or 16 with RK4. Earlier-layer Qwen runs may exceed 24 GB.
3. **Benchmark-policy mismatch.** AxBench's standard semantic steering evaluation invokes GPT-4o-mini, conflicting with the report's no-proprietary-API rule. SteeringSafety contains local exact-match subsets, but several evaluations use Groq or OpenAI. TruthfulQA open-ended evaluation also needs judges; MC1/MC2 is the clean local option.
4. **Baseline portability.** Official ODESteer and FLAS support does not match both proposed checkpoints out of the box; SVF and INNSteer lack readily verified official implementations. Porting and validating all of them cannot be treated as a ten-hour tail task.
5. **Environment mismatch.** Current AxBench requires Python 3.12 while the report specifies Python 3.11.

### Technical failings

- No exact hook location, token policy, probe architecture, target objective, field normalization convention, epsilon unit, or local evaluator is frozen.
- “Field evaluations” are not an equal-compute unit when a tiny MLP probe and a transformer-suffix double backward have radically different costs.
- Gemma requires accepted license/authentication; this dependency is absent from the plan.
- Repeated steering at every generated token and a one-time prefill intervention are scientifically different protocols with very different cost and persistence.
- A realistic reduced experiment is approximately 36–98 GPU-hours over 3–6 wall-clock days; the full model-native and multi-baseline version is plausibly 100–300+ GPU-hours.

### Assessment axes

- Basic implementability: **4/5**
- Protocol completeness: **1/5**
- Credibility of compute estimate: **1/5**
- Benchmark reproducibility under stated policy: **2/5**

### Recommendation posture

**Do not launch Stage 0 as written.** A sub-two-GPU-hour engineering check could validate autograd and memory, but it would not repair the scientific no-go and is therefore not authorized as the next paper experiment.

## Cross-review synthesis

All three reviewers agree on the binding outcome:

1. The exact wording is not directly occupied by one paper.
2. The BCH identity and span-exit phenomenon are expected from classical nonlinear control.
3. At one transformer layer, the loop has no downstream path memory; its only causal product is the final displacement.
4. Direct bracket injection and exact final-displacement replay are missing, decisive controls.
5. Strong nonlinear activation controllers occupy the useful comparison space and likely subsume the loop.
6. The proposed scale and benchmark stack do not fit the advertised compute or no-API constraints.

The most damaging result is available before running a GPU: **the current path-causal story is structurally false at a fixed layer.** A successful experiment could still show that a bracket-derived vector is behaviorally useful, but it could not show that executing the loop has privileged causal power.

### Binding verdict

**`NO_GO_AS_CURRENTLY_FORMULATED`**

- Do not run the proposed 72-hour Stage 0.
- Do not rescue the seed by weakening baselines, reducing confirmation requirements, or calling a bracket vector a new reachable direction.
- Do not claim behavioral path dependence when the transformer suffix sees only the final state.
- The repository remains without an authorized active paper seed.

### Narrow alternative retained as HOLD

A materially different question remains logically testable:

> Can a bracket feature computed solely from two model-native source objectives provide reproducible zero-shot steering of a preregistered third behavior better than every source-only control?

This alternative would require:

- no target examples, scores, or effects for pair, layer, scale, or sign selection;
- one fixed last-prompt token and one frozen hook location;
- model-native unnormalized fields with globally frozen scaling;
- three human-preregistered triples, two model families, and at least 256 locked prompts per triple;
- five symmetric epsilon magnitudes and accurate FP32 integration;
- exact final-displacement replay, direct bracket injection, projected bracket injection, static source-span and arbitrary time-varying source-field controls;
- random, colinear, identical, and analytically commuting field nulls;
- an evaluator independent of field construction and selection;
- local API-free evaluation only;
- compute matching by measured wall time, FLOPs/backward calls, and peak memory, not nominal field-call count.

Even this version is a **HOLD**, not an active experiment. If direct bracket injection or a source-only nonlinear controller matches it, the seed is immediately killed. If it survives, the contribution must be described as a bracket-derived compositional feature basis, not a special closed-loop mechanism.

## Risk and unsupported-claim register

| Claim in the proposal | Audit status | Required correction |
|---|---|---|
| The loop creates a new direction inaccessible to the source controls | Unsupported | Compare with the full time-varying source-field controller and Lie closure, not the instantaneous span. |
| The path itself causally changes behavior at a fixed layer | False under deterministic suffix evaluation | Exact final-state replay must match; only final displacement is visible. |
| Span-exterior fraction \(\rho\ge0.35\) is surprising | Unsupported | Use dimension-aware random nulls and a declared metric/whitening convention. |
| The effect reveals transformer curvature | Unsupported for probe-gradient fields | Separate probe Hessian artifacts from model-native fields. |
| The method can be described as zero-target | Contradicted by target-guided triple selection | Freeze all choices without target information or drop the claim. |
| The full protocol fits 34–60 GPU-hours | Not credible | Collapse the matrix, freeze local evaluation, and measure double-backward cost first. |
| AxBench supplies an API-free standard evaluation | Generally false | Use a preregistered local subset or another locked local metric. |
| Three epsilon values and 10% RK agreement establish the bracket law | Too weak | Use at least five symmetric scales and integration error below 5% of the residual. |

## Primary-source basis

- [Feed-Forward Steering in Transformer Residual Dynamics](https://arxiv.org/abs/2608.02071)
- [Inverse-Free Wilson Loops for Transformers](https://arxiv.org/abs/2510.08648)
- [First-Order Predictable but Pairwise Fragile](https://arxiv.org/abs/2607.16821)
- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)
- [ODESteer](https://arxiv.org/abs/2602.17560)
- [Activation Steering with a Feedback Controller](https://openreview.net/pdf?id=wwc3NEmWo8)
- [INNSteer](https://arxiv.org/abs/2606.08454)
- [FLAS](https://arxiv.org/abs/2605.05892)
- [Local Linearity of LLMs Enables Activation Steering via Model-Based Linear Optimal Control](https://arxiv.org/abs/2604.19018)
- [Non-linear Interventions on Large Language Models](https://arxiv.org/abs/2605.14749)
- [AxBench official repository](https://github.com/stanfordnlp/axbench)
- [SteeringSafety official repository](https://github.com/wang-research-lab/SteeringSafety)
