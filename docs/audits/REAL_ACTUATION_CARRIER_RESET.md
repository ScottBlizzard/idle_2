# Real-Actuation Carrier Reset

Date: 2026-08-28

Binding outcome: **one candidate advances to preregistration only; no paper seed or GPU experiment is yet authorized.**

## 1. Why this reset was necessary

The rejected closed-loop bracket seed exposed a carrier error. Physical nonholonomic systems cannot directly actuate every desired direction, whereas activation editing usually permits an arbitrary vector to be written into the residual stream. The reset therefore searched for AI systems with all of the following properties:

1. a real, deployment-relevant actuator restriction rather than an experimenter-imposed ban;
2. a state change between operations, so later operations act on a genuinely different state;
3. no exact final-state replay or one-shot target controller that trivially dominates the sequence;
4. a scientific claim that is not merely planning, dynamic routing, information gain, risk sensitivity, more samples, or more compute;
5. public models, public data, local evaluation, and a decisive test compatible with 8×RTX 4090 GPUs.

Two independent searches covered frozen source-controller libraries and stateful inference/agent systems. A third search covered low-rank, sparse, routing, quantization, diffusion, and compression interfaces. Primary literature was checked through 2026-08-28.

## 2. General obstruction discovered by the search

Let the complete state contain every variable that can affect the future: model activations, token/KV history, external environment state, memory, parameters, and random state.

- If two control histories reach the same complete state, their future conditional behavior is identical. The path has no independent causal effect.
- If the complete states differ, the useful effect is state control, information acquisition, or constrained planning.

This does not say that sequential control is useless. It says that **“the path itself creates an otherwise unavailable capability” is usually not a distinct ML mechanism**. A paper must identify a more specific violated assumption, law, estimator, or credit-assignment failure.

## 3. Carrier kill matrix

| Carrier | Real constraint and history | Strongest collision or shortcut | Verdict |
|---|---|---|---|
| Token/layer/turn LoRA choreography | Execute-only adapters can be realistic; token and KV history persist | [X-LoRA](https://arxiv.org/abs/2402.07148), [MoLoRA](https://arxiv.org/abs/2603.15965), [LORAUTER](https://arxiv.org/abs/2601.21795), [Compositional Steering](https://arxiv.org/abs/2601.05062), and a general token/layer-conditioned router | **KILL** |
| Diffusion-time LoRA/ControlNet sequencing | Denoising state makes order genuine | [Multi-LoRA Composition](https://arxiv.org/abs/2402.16843), [CMLoRA](https://arxiv.org/abs/2502.04923), and [FREE-Switch](https://arxiv.org/abs/2604.10023) already cover alternating, ordered, and dynamic timestep schedules | **KILL** |
| Prompt/operator/tool sequencing | Black-box APIs and external tool state are real constraints | Decomposed prompting, program search, DSPy-style optimization, active information gathering, and ordinary agent planning subsume the mechanism | **KILL** |
| Source-only logit/reward modules | Generated prefixes preserve history | Additive/dynamic guidance such as [UniR](https://arxiv.org/abs/2505.19075), verifier-guided search, and general state-dependent decoding controllers | **KILL** |
| External skill policies/options | Physical or simulated state makes the billiards analogy valid | Hierarchical RL, option planning, MPC, and skill-library search; it also reintroduces simulator cost outside the desired project scope | **KILL** |
| Net-zero tool loop with retained observations | External state can be restored while information remains | Observation replay reduces it to memory/prompting; otherwise it is active experimentation and information gain | **KILL** |
| Longer but wider-success action path | Real execution uncertainty | Robust planning, risk-sensitive planning, viability, and continuation-set optimization | **KILL** |
| Individually safe but jointly unsafe tool calls | Temporal state and authorization are real | Temporal safety, information-flow control, [Verifiably Safe Tool Use](https://arxiv.org/abs/2601.08012), [Agent-SafetyBench](https://arxiv.org/abs/2412.14470), and [Vera](https://arxiv.org/abs/2607.01793) | **KILL** |
| Delayed irreversible action / reversibility | External state and opportunity loss are real | Option value, abstention, [Revisable by Design](https://arxiv.org/abs/2604.23283), and [AgentAbstain](https://arxiv.org/abs/2607.10059) | **KILL** |
| Query-agnostic context/KV compression before future queries | Future query is genuinely unrevealed and eviction is irreversible | [KVzip](https://arxiv.org/abs/2505.23416), future-query-distribution attention, OracleKV, and query-agnostic reconstruction already occupy the problem | **KILL** |
| Low-rank/sparse adapter composition | Storage/rank constraints are real | LoRA expressivity, adapter merging, retrieval composition, MoE-LoRA routing, rank concatenation, and direct compression/merge methods | **KILL** |
| Frozen MoE expert routing across layers | Top-k expert budget is a hard systems constraint; early route changes later hidden states and router inputs | Single-layer counterfactual routing, recurrent routers, path-constrained MoEs, and expert-path search are close, but none found tests the compositional validity of single-layer causal preferences in a pretrained frozen MoE | **ADVANCE TO PREREGISTRATION ONLY** |

## 4. Sole retained candidate

### Counterfactual Route Non-Compositionality in Frozen MoEs

#### Central claim

Recent counterfactual routing analysis evaluates one layer at a time: replace the standard route at layer \(\ell\), keep the rest of the model's policy intact, and measure the resulting next-token utility. This produces a local route preference.

The retained hypothesis is:

> On fragile reasoning tokens, independently beneficial equal-compute expert substitutions at two layers are frequently harmful when combined, while individually neutral or harmful substitutions can become beneficial together. Consequently, single-layer counterfactual preferences are not transportable credit signals for multi-layer router improvement.

This is not a claim that paths have independent causal power. It is a claim that a currently used **single-intervention causal diagnostic may be non-compositional** because the first intervention changes the state on which the later router and experts act.

#### Why this is counterintuitive

A common engineering instinct is to improve multiple layers by applying each layer's independently measured better route. The hypothesis predicts a “best parts make a worse whole” regime: every replacement passes its own local counterfactual test, yet the combined router is worse than the original.

#### Mathematical object

For a locked correct next token \(y_t\), define a score \(S\) using its pre-softmax logit margin, not only probability. Let \(a\) be a route substitution at layer \(i\) and \(b\) at layer \(j\):

\[
\Delta_i(a)=S(a)-S_0,\qquad
\Delta_j(b)=S(b)-S_0,
\]

\[
\Delta_{ij}(a,b)=S(a,b)-S_0,
\]

\[
I_{ij}(a,b)=\Delta_{ij}(a,b)-\Delta_i(a)-\Delta_j(b).
\]

The decisive events are sign reversals, not merely nonzero interaction:

- individually beneficial but jointly harmful: \(\Delta_i>0,\Delta_j>0,\Delta_{ij}<0\);
- individually non-beneficial but jointly beneficial: \(\Delta_i\le0,\Delta_j\le0,\Delta_{ij}>0\).

#### Closest work

- [When Are Experts Misrouted?](https://arxiv.org/abs/2605.07260) evaluates sampled equal-compute alternatives one layer at a time and shows large route gaps on fragile tokens.
- [Layerwise Recurrent Router for Mixture-of-Experts](https://openreview.net/pdf?id=eWNEqdH0vk) uses past routing information across layers.
- [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297) argues that independent per-layer routing creates an excessive expert-path space and improves training by constraining it.
- Q-MoE's ExpertPath method already treats independent layer selection as greedy and searches paths in a task-specific multimodal architecture.
- [Geometric Routing Enables Causal Expert Control](https://arxiv.org/abs/2604.14434) reports additive cross-layer effects in a specially constructed interpretable MoE, which provides a useful contrasting regime rather than an exact collision.

The literal residual is narrow: **whether local counterfactual route preferences in existing pretrained language MoEs compose interventionally, and whether their failure invalidates independent multi-layer router updates.**

## 5. Proposed preregistered kill test

This is a design target, not authorization to run.

### Models and data

- Discovery: [OLMoE-1B-7B-0924-Instruct](https://huggingface.co/allenai/OLMoE-1B-7B-0924-Instruct), fully open and single-4090 compatible.
- Locked confirmation: DeepSeek-V2-Lite-Chat, sharded across two 4090s.
- Teacher-forced verified trajectories from GSM8K and a locked MATH subset.
- Primary units: fragile assistant-response tokens, defined before route intervention by a frozen confidence threshold.

### Frozen intervention matrix

- Four preregistered layer pairs spanning near, medium, and far separation.
- Six sampled equal-compute route alternatives per layer, plus the standard route.
- Singles and the full 6×6 pair grid on the same tokens.
- Target 64 independent correct problem trajectories per model and dataset (128 per model total), with a preregistered minimum of 48 per dataset.
- No target-token-based route sampling; the correct token is used only to score locked counterfactual outcomes.

### Mandatory baselines and controls

1. standard router;
2. independently best single-layer substitutions;
3. independently best routes applied jointly;
4. random route pairs matched by router score, expert overlap, layer distance, and intervention norm;
5. direct joint route search upper bound at the same candidate-evaluation budget;
6. an additive first-order predictor;
7. a generic nonlinear pair predictor with identical training information;
8. final-layer-only counterfactual router update following the closest paper;
9. independent multi-layer updates versus a path-aware update;
10. probability, target-logit, and logit-margin analyses to rule out softmax saturation artifacts.

### Numerical and scientific gates

The candidate survives the diagnostic stage only if all are true:

1. both sign-reversal types exceed matched-null rates by at least 10 percentage points on discovery and confirmation models;
2. the effect is present in pre-softmax logit margins, not only probabilities;
3. clustered 95% bootstrap confidence intervals by problem exclude zero;
4. the effect appears in at least three of four frozen layer-pair regimes and both datasets;
5. a cross-fitted path-compatibility model predicts joint utility beyond single effects and router scores with held-out Spearman \(\rho\ge0.4\);
6. no diagnostic selection or prediction benefit relies on observing the answer token at route-selection time;
7. total diagnostic compute, including trajectory generation, stays below 12 GPU-hours.

Only after all diagnostic gates pass may a separate amendment authorize path-aware router training and free-generation evaluation. Those are algorithmic-consequence tests, not movable requirements inside the current diagnostic.

Immediate stop conditions:

- interaction is explained by softmax saturation, activation norm, or route-overlap mismatch;
- sign reversals are rare or model-specific;
- a generic nonlinear pair predictor or direct joint search removes any method-specific advantage;
- the result is only “deep networks are nonlinear” without a stable predictive law.

If a later algorithmic amendment is authorized, failure to survive free generation or to beat a matched recurrent/router-only baseline is a mandatory algorithmic-stage stop.

## 6. Review setup

- **Input scope:** a concept-level hypothesis and preregistration sketch, not experimental results.
- **Assessment boundary:** novelty and test validity can be assessed; empirical magnitude and broad significance cannot.
- **Shared claim:** single-layer counterfactual MoE route preferences may fail under joint intervention, invalidating independent multi-layer route credit.
- **Visible evidence:** closest papers establish single-layer misrouting, cross-layer route dependence, and path-space structure, but do not establish the proposed sign-reversal law.
- **Missing evidence:** all empirical results, a working route-intervention harness, and an algorithm that improves end-to-end generation.

## Reviewer 1

### Overall assessment

The hypothesis is technically coherent and avoids the final-state fallacy of the previous bracket seed. Its largest risk is triviality: nonlinear networks generically exhibit pairwise interactions, so nonzero \(I_{ij}\) is not evidence. Only preregistered sign reversals, a matched null, cross-model prediction, and downstream router consequences could establish a meaningful result.

### Who would be interested in the results, and why

Researchers analyzing or training sparse MoE routers would care if single-layer counterfactual preferences are shown to be invalid credit signals for multi-layer updates.

### Major strengths

- The top-k actuator restriction is real and tied to active-compute budgets.
- The causal intervention and interaction term are precisely defined.
- The proposal directly tests an assumption implicit in recent counterfactual routing work.

### Major concerns

- Correct-token scoring is privileged teacher-forced information and cannot be used by the deployed router.
- Route-pair effects may be ordinary curvature, normalization, or softmax artifacts.
- Selecting only fragile tokens may inflate effects and weaken end-to-end relevance.

### Technical failings that need to be addressed before the case is established

- Freeze the fragile-token definition, layer pairs, candidate sampler, and scoring metric.
- Use pre-softmax margins and hidden-state controls.
- Cluster statistics by problem, not token.
- Demonstrate free-generation consequences and an answer-free selection rule.

### Assessment against Nature-style criteria

- Originality: **potentially original but narrowly separated from recent work**.
- Scientific importance: **not established without router-training consequences**.
- Interdisciplinary readership: **low; primarily MoE specialists**.
- Technical soundness: **testable, with substantial leakage and null-model risks**.
- Readability: **the “best parts make a worse whole” statement is accessible**.

### Recommendation posture

**Support preregistration of a cheap kill test; do not yet support a full paper program.**

## Reviewer 2

### Overall assessment

The literal empirical law appears unoccupied in the searched literature, but the surrounding space is crowded by recurrent routers, expert-path methods, path-constrained MoEs, and counterfactual misrouting analysis. Novelty depends on showing that the new law invalidates or changes an existing method, not merely that pairwise interactions exist.

### Who would be interested in the results, and why

The immediate audience is sparse-model routing and efficient LLM inference. Broader interest would require demonstrating a general causal-credit principle shared across multiple conditional-computation architectures.

### Major strengths

- It makes a risky, directional prediction rather than renaming dynamic routing.
- It uses existing pretrained models and same-compute route interventions.
- Negative results are decisive and inexpensive.

### Major concerns

- Q-MoE already describes independent routing as greedy and searches expert paths.
- PathMoE and recurrent routers already motivate cross-layer coordination.
- A generic path-aware router or RL objective may fully subsume the proposed method.

### Technical failings that need to be addressed before the case is established

- Show an explicit failure of independently trained counterfactual preferences.
- Beat a recurrent or generic nonlinear router at equal information and expert compute.
- Establish model-family replication and free-generation benefit.

### Assessment against Nature-style criteria

- Originality: **literal residual present; conceptual neighborhood heavily occupied**.
- Scientific importance: **conditional on changing how counterfactual router training is performed**.
- Interdisciplinary readership: **not yet demonstrated**.
- Technical soundness: **the proposed kill test is appropriately adversarial**.
- Readability: **clear if framed as causal-credit non-compositionality, not path magic**.

### Recommendation posture

**Conditional advance to preregistration only.**

## Reviewer 3

### Overall assessment

The experiment is substantially more reproducible than the rejected activation-loop study. OLMoE fits one 4090, evaluation is local and deterministic, and the first-stage claim can be tested without training a large model. DeepSeek-V2-Lite integration and exhaustive route-pair hooks remain the main engineering risks.

### Who would be interested in the results, and why

MoE systems researchers would care because a path-aware router could improve quality without increasing the number of active experts. Practitioners would care only if wall-clock overhead and end-to-end accuracy improve.

### Major strengths

- Public open models and benchmarks.
- No proprietary judge or robot simulator.
- A 12 GPU-hour stopping rule is credible for a carefully cached teacher-forced diagnostic.

### Major concerns

- Route hooks differ across OLMoE and DeepSeek custom implementations.
- Pair grids multiply suffix forwards quickly.
- Candidate-search compute must not be hidden when comparing deployed methods.

### Technical failings that need to be addressed before the case is established

- Benchmark suffix-caching correctness and route-hook determinism first.
- Report both active-expert FLOPs and total search/training wall time.
- Separate an offline diagnostic upper bound from a deployable router.

### Assessment against Nature-style criteria

- Originality: **plausible narrow gap**.
- Scientific importance: **not assessable before end-to-end results**.
- Interdisciplinary readership: **limited in current form**.
- Technical soundness: **engineering-feasible with strict accounting**.
- Readability: **good conceptual summary; implementation details remain specialist-heavy**.

### Recommendation posture

**Proceed only to a frozen preregistration and engineering feasibility check.**

## Cross-review synthesis

### Consensus strengths

- This candidate uses a real active-compute constraint and genuine cross-layer state transitions.
- It no longer claims that a path has independent causal power.
- The central sign-reversal hypothesis is falsifiable, counterintuitive, and cheap to kill.

### Consensus technical risks

- Generic nonlinearity may explain the entire observation.
- Teacher-forced correct-token scoring may not translate into an answer-free deployed policy.
- Recent path-aware MoE work leaves only a narrow novelty residual.
- A generic recurrent or nonlinear router may subsume any proposed algorithm.

### Where emphasis differs across reviewers

- Reviewer 1 weights causal identification and leakage most heavily.
- Reviewer 2 weights the narrow prior-art gap and algorithmic consequence most heavily.
- Reviewer 3 weights implementation, compute accounting, and deployment relevance most heavily.

### Broad-interest / significance readout

The present concept is not an oral-level contribution. It could become a competitive paper only if the sign-reversal law is cross-model, predictable, invalidates independent counterfactual router training, and yields an answer-free path-aware router that improves real generation at unchanged active-expert compute.

### Most important issues to resolve before a strong case is established

1. demonstrate sign reversals beyond generic curvature and softmax effects;
2. show that independent counterfactual preferences actually damage a jointly updated router;
3. produce an answer-free predictor or training objective;
4. beat recurrent and generic nonlinear routing baselines at equal compute;
5. confirm on a second MoE family and free generation.

## Risk / unsupported claims

- No empirical evidence currently supports the sign-reversal frequency or thresholds.
- No retrieved paper was found to run the exact paired intervention, but literature vacancy is not proof of importance.
- The 12 GPU-hour estimate assumes hidden-state caching and narrow teacher-forced evaluation; a full generation and training package would be larger.
- Any claim of general path dependence, new reachability, or broad control theory would be unsupported.
- Any target-token-informed deployment result would be invalid due to answer leakage.

## 7. Binding decision

The broad **path-dependent control carrier search is closed**. It produced no surviving source-controller, diffusion, agent, memory, planning, compression, or generic structural carrier.

Exactly one narrow candidate remains:

> **Counterfactual Route Non-Compositionality in Frozen MoEs**

Status: **`ADVANCE_TO_PREREGISTRATION_ONLY`**.

This does not authorize a GPU run. The next legitimate artifact is a frozen, implementation-level preregistration that resolves route hooks, candidate sampling, leakage prevention, equal-compute accounting, and the second-model confirmation protocol. If that document cannot be made precise, the candidate is killed before experimentation.
