# Viability-Aligned Planning Internal Novelty Audit

> **Superseded on 2026-08-28:** the conditional decision-calibrated uncertainty pivot below was rejected by a follow-up literature collision audit before experimentation. See [`DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md`](DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md). The broad-principle `NO-GO` remains valid; the `CONDITIONAL PIVOT` does not.

Audit date: 2026-08-27  
Method: three parallel adversarial reviews covering control theory, ML/RL and ICLR-style significance, followed by primary-source cross-checking and synthesis.  
Candidate origin: the billiards observation that a longer route can tolerate more total variation when that variation is aligned with a region of good follow-up positions.

## Executive verdict

### Original claim: NO-GO

The broad idea cannot be claimed as a new planning principle:

> A plan can have larger total uncertainty yet higher task success when its errors lie along task-irrelevant or goal-equivalent directions rather than crossing the future viable-state boundary.

This is almost exactly covered by the minimum-intervention principle, uncontrolled/goal-equivalent manifold analysis, Gaussian chance constraints, LQG motion planning and covariance steering. The option-preservation extension is separately covered by reachability, stochastic viability, empowerment, relative reachability, attainable utility preservation and future-task objectives.

Merely moving this principle into an LLM or AI-agent setting would be a weak application paper, not an ICLR oral contribution.

### Narrow residual: CONDITIONAL PIVOT

One computational question may remain:

> A learned world model can be well calibrated in NLL, mean error or scalar uncertainty while systematically misranking downstream plan risk because its predictive uncertainty is not calibrated relative to the recursively learned future-value boundary.

The possible contribution is therefore **decision-calibrated uncertainty for learned planners**, not error shaping as a newly discovered principle. It deserves only a short, preregistered kill test. A full paper cycle is not yet authorized.

## 1. What the billiards intuition actually rediscovered

The useful intuition remains correct:

- success states form a region or equivalence class rather than one ideal point;
- total variance is not the relevant risk statistic;
- uncertainty can be harmless along a goal-equivalent direction and dangerous across a success boundary;
- a longer route can be more reliable than a shorter route;
- preserving recovery options can dominate maximizing immediate geometric accuracy.

But each component has substantial prior art.

### 1.1 Minimum intervention and task-irrelevant variability

Todorov and Jordan explicitly argued that optimal feedback control corrects deviations only when they interfere with task performance. Their analysis permits greater variability in task-irrelevant directions and presents the elongated covariance structure that motivates the present idea. [NeurIPS 2002 paper](https://papers.neurips.cc/paper_files/paper/2002/hash/8c5f6ecd29a0eb234459190ca51c16dd-Abstract.html)

The uncontrolled-manifold and goal-equivalent-manifold traditions already decompose variability into components parallel and orthogonal to a task-equivalent solution set. [Scholz and Schöner, 1999](https://pubmed.ncbi.nlm.nih.gov/10382616/), [Cusumano and Cesari, 2006](https://doi.org/10.1007/s00422-006-0052-1)

Consequently, the following claims are not available:

- first to distinguish task-relevant from task-irrelevant error;
- first to use tangent/normal variability;
- first to show that higher total variance can accompany lower task error;
- first to treat successful outcomes as a manifold rather than a point.

### 1.2 Path geometry and directional uncertainty

LQG-MP predicts the state distribution induced by candidate paths and evaluates collision probability from the geometry of the uncertainty ellipse relative to obstacles. Its examples already show that paths with comparable nominal geometry can have sharply different success probabilities because of uncertainty direction. [van den Berg, Abbeel and Goldberg, RSS 2010](https://people.eecs.berkeley.edu/~pabbeel/papers/vandenBergAbbeelGoldberg_RSS2010.pdf)

For a local Gaussian constraint, the chance constraint depends on projected variance,

\[
a^\top\mu + \Phi^{-1}(1-\alpha)\sqrt{a^\top\Sigma a}\le b,
\]

not on `trace(Σ)`. This is standard in chance-constrained path planning. [Blackmore, Ono and Williams, 2011](https://dspace.mit.edu/server/api/core/bitstreams/1bcd431a-3fdd-4735-a689-2ea5d1f2b5d0/content)

Covariance steering goes further and actively shapes the state distribution while satisfying state constraints. [Okamoto and Tsiotras, 2019](https://arxiv.org/abs/1809.03380), [data-driven covariance steering, L4DC 2024](https://proceedings.mlr.press/v242/pilipovsky24a.html)

Therefore, “rotate or stretch uncertainty to match the good corridor” is an existing control technique, not merely an unclaimed observation.

### 1.3 Viability, reachability and recovery

Maximizing the probability of reaching a viable terminal set is already an expected-return MDP with an indicator terminal reward. Requiring the trajectory to remain inside a safe set gives stochastic reach-avoid or stochastic viability. Learned feasible-set variants include [RCRL, ICML 2022](https://proceedings.mlr.press/v162/yu22d.html) and [RESPO, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/dca63f2650fe9e88956c1b68440b8ee9-Abstract-Conference.html).

Tube MPC, LQR-Trees and funnel libraries similarly reason about sets of perturbed trajectories that remain controllable or lead back to the goal. Hence “leave the next state recoverable” is not a new objective.

### 1.4 Task-relevant uncertainty and compatible continuations

STRUG is a particularly close collision. It distinguishes task-relevant from task-irrelevant uncertainty by checking whether different belief particles require incompatible successful plans; state differences that share a successful plan need not be resolved. [Curtis, Kaelbling and Jain, ICRA 2023](https://www.merl.com/publications/TR2023-046)

Value-equivalent models and goal-conditioned bisimulation also collapse states that are different in observation space but equivalent for downstream decision value. [Value Equivalence, NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html), [Goal-conditioned bisimulation, ICML 2022](https://proceedings.mlr.press/v162/hansen-estruch22a.html)

### 1.5 Preserving future options

Empowerment measures future controllability. Relative reachability, attainable utility preservation and future-task objectives explicitly reward preservation of reachable states or future capabilities. [Relative reachability](https://arxiv.org/abs/1806.01186), [AUP](https://doi.org/10.1145/3375627.3375851), [Future Tasks, NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/dc1913d422398c25c5f0b81cab94cc87-Abstract.html)

Thus “insurance balls”, “keep options open” and future option volume are good explanatory analogies but not contribution claims.

## 2. Why the original mathematical story would be rejected

### 2.1 It can collapse to ordinary Bellman planning

If the future task, dynamics and value are correctly known, maximizing

\[
\mathbb E[V^*(s')]
\]

already integrates where the outcome distribution lands. A new viability score that is numerically equivalent to expected success or expected value is only a reinterpretation of Bellman backup.

If future tasks are unknown, maximizing generic retained capability instead collides with empowerment, relative reachability and AUP.

### 2.2 A success set need not be a smooth manifold

Future viable regions can be disconnected, non-convex, non-smooth and topology-changing. A unique tangent and normal may not exist. Even when the boundary is smooth, tangential variance is harmless only to first order; curvature turns finite tangential variation into boundary-crossing risk.

### 2.3 Covariance is insufficient

Multi-step learned dynamics can yield skewed or multimodal outcome distributions. Two distributions with identical mean and covariance may have completely different failure probabilities. This is especially relevant to the original K-ball intuition, where small perturbations create discrete collision-mode changes.

### 2.4 Option count is not value

The number or geometric volume of available actions is coordinate dependent and need not reflect their usefulness. A state with many bad continuations can be inferior to one with a single reliable high-value continuation.

## 3. The only promising reformulation

The candidate should be renamed and redefined as **decision-calibrated uncertainty for learned planning**.

Define the future-value boundary risk of an action as

\[
R_\tau(s,a)
=
\Pr_{s'\sim p_\theta(\cdot\mid s,a)}
\left[V_{t+1}(s')<\tau\right],
\]

where both the transition model and downstream value or recoverability boundary are learned. The research question is not whether this is the correct ideal objective; standard decision theory already answers that. The research questions are:

1. Do learned world models that look calibrated under task-agnostic metrics systematically misestimate this boundary-crossing risk?
2. Can boundary-aware calibration predict rare planning failures more sample-efficiently than direct Monte Carlo under a fixed rollout budget?
3. Does the estimator remain useful under curved boundaries, multimodal pushforward distributions and dynamics shift?
4. Does it improve closed-loop planning after controlling for world model, rollout count and compute?

Potential algorithmic ingredients include a world-model ensemble, a learned future-value boundary, non-Gaussian outcome propagation, calibrated boundary-crossing estimates and conditional recovery probability. None is a contribution unless the combination yields an estimator or regret guarantee that is not equivalent to adding a value bonus or running more rollouts.

### Secondary, weaker route: continuation-equivalent uncertainty for tool agents

For a state `s`, define the reliable continuation set

\[
\mathcal C_\tau(s)
=
\{\pi:\Pr(\text{success}\mid s,\pi)\ge\tau\}.
\]

An action can have high surface-level outcome entropy but low task-relevant execution uncertainty when its possible outcomes share substantially overlapping continuation sets. A learned estimator could rerank tool-agent plans before execution.

This differs from recent rollback systems by planning prospectively rather than recovering only after failure. However, it remains close to STRUG compatibility, bisimulation and ordinary rollout search. Its likely ceiling is a solid benchmark/estimator paper unless it reveals a strong cross-model law and a substantial sample-efficiency advantage.

## 4. Minimum contribution needed for a competitive ICLR paper

At minimum:

1. an impossibility or separation result showing that task-agnostic scalar uncertainty rankings can be reversed by downstream decision boundaries;
2. a boundary-risk approximation with a curvature or non-Gaussian error characterization;
3. a finite-sample or planning-regret advantage over direct failure Monte Carlo;
4. a method that cannot be reduced to expected-value MPC with extra samples;
5. one controlled causal environment and two natural decision domains;
6. compute-matched comparison with expected-value MPC, Monte Carlo, CVaR, chance constraints, covariance steering, reachability and scalar ensemble uncertainty;
7. evaluation under multiple noise directions and OOD dynamics, including calibration, success, first failure, recovery and compute.

The first two theoretical observations alone are not novel; the paper lives or dies on the third, fourth and the natural-domain evidence.

## 5. Recommended staged kill test

### Stage 0: controlled counterfactual

Hold mean, path length, action cost, `trace(Σ)` and `logdet(Σ)` fixed. Rotate only the predictive distribution relative to a success boundary. Verify that scalar metrics remain unchanged while true failure probability reverses.

Then add:

- a higher-trace but lower-risk plan;
- a curved boundary, showing where first-order normal risk fails;
- equal-mean/equal-covariance multimodal distributions with different risk;
- equal-compute estimators of direct failure probability and proposed boundary risk.

This stage demonstrates implementation correctness, not novelty.

### Stage 1: two-to-three-day mechanism gate

Use a GPU-native or vectorized environment such as Brax/Safety-Gymnasium. Train or reuse one compact world model and freeze it. The binding questions are whether task-agnostic calibration misses boundary risk and whether the proposed estimator improves held-out failure prediction at equal sample count.

Automatic stop if either condition fails.

### Stage 2: natural-domain gate

Only after Stage 1 passes, use GPUDrive, optionally cross-checked with Waymax. GPUDrive is an ICLR 2025 GPU-native multi-agent driving simulator with public code and pretrained agents, compatible with the available 8×4090 server. [GPUDrive paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/3107ddd4209e5f93c0371425763041a3-Paper-Conference.pdf), [official repository](https://github.com/Emerge-Lab/gpudrive)

Safety-Gymnasium provides public safety environments and baselines; TD-MPC2 provides a strong public world-model baseline. [Safety-Gymnasium, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3c557a3d6a48cc99444f85e924c66753-Abstract-Datasets_and_Benchmarks.html), [TD-MPC2](https://arxiv.org/abs/2310.16828)

LLM-agent benchmarks such as AgentBoard or τ-bench should be treated only as a later discrete extrapolation because their symbolic action spaces do not naturally support the geometric theory. [AgentBoard, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Datasets_and_Benchmarks_Track.html), [τ-bench, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf)

### Binding stop conditions

Stop the candidate if any occurs:

1. direct expected-success Monte Carlo or an existing chance-constrained planner matches the proposed estimator at equal compute;
2. the new score has no incremental predictive value after expected return and scalar ensemble uncertainty;
3. gains disappear on held-out boundary geometry or noise direction;
4. the method fails on multimodal outcomes or reduces to Gaussian covariance rotation;
5. planning gains come from extra rollouts, greater conservatism or a stronger world model;
6. the result does not replicate across two natural environments.

## 6. Resource and publication assessment

| Candidate | Novelty | Fit to 8×4090 | Fast falsification | Likely ceiling |
|---|---:|---:|---:|---|
| Original viability/error-shaping principle | 1/5 | 5/5 | already falsified by literature | none |
| Continuous learned-planner boundary calibration | 2.5–3/5 | 4/5 | 7–10 days | competitive regular paper if all gates pass |
| Tool-agent continuation equivalence | 2–2.5/5 | 5/5 | hours to 1 day | benchmark/regular paper |
| Direct control/RL transplantation | 1–2/5 | 4/5 | short | weak novelty |

An oral-level story would additionally require a broad, reproducible failure mechanism showing why learned world models are directionally miscalibrated, not merely another demonstration that scalar uncertainty is incomplete.

## Final recommendation

Do not send the broad idea to Pro for another unconstrained brainstorm and do not start a large experiment. The internal review is already sufficient to reject the principle-level claim.

If continuing, first write a one-page preregistration for the decision-calibrated learned-planner kill test. Run Stage 0 and Stage 1 only. Ask Pro for a final targeted audit only if the new score beats direct Monte Carlo and strong existing risk baselines at equal compute. That ordering prevents another literature-first NO-GO after a large model sweep.
