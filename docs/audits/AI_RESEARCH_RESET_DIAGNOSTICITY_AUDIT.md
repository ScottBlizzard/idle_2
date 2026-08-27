# AI Research Reset–Diagnosticity Audit

**Audit date:** 26 August 2026
**Target venue:** ICLR main track; Oral-level insight is aspirational, not assumed
**Compute boundary:** exactly 8 independent NVIDIA RTX 4090 GPUs with 24 GB VRAM each; no NVLink and no pooled memory
**Repository audited:** [`ScottBlizzard/idle_2`](https://github.com/ScottBlizzard/idle_2), default branch `main`
**Binding scope:** Seeds A, B, and C in `BILLIARDS_TO_AI_RESEARCH_SYNTHESIS.md`

---

## Epistemic labels

- **[VERIFIED FACT]** Directly supported by the audited repository, a primary paper, an official benchmark, or an official implementation.
- **[LITERATURE-SUPPORTED JUDGMENT]** An evaluative conclusion supported by multiple verified sources.
- **[INFERENCE]** A reasoned extrapolation whose premises are stated.
- **[HYPOTHESIS]** A falsifiable proposition that has not been established.
- **[PROJECT DECISION]** A binding allocation, continuation, or termination choice.

---

# 1. Executive verdict

## 1.1 Binding result

> **[PROJECT DECISION] FINAL CLUSTER DECISION: DO NOT RUN.**

No primary direction and no fallback direction survive the novelty audit. The three seeds should not be merged into one paper. None currently warrants a two-GPU pilot, a one-week eight-GPU sprint, or a conditional 30-day program.

| Seed | Strongest charitable scientific reading | Decisive collision | Binding status |
|---|---|---|---|
| **A. Resettable Failure with Epistemic Progress** | A lower-immediate-success route can be globally preferable when its failures are externally recoverable, diagnostically informative, and remembered across attempts under a fixed total budget. | **AgentRewind** already restores aligned agent-context and environment checkpoints, preserves failure-derived rewind memory, evaluates natural software tasks, and ablates environment rewind, context rewind, and memory. Classical iterative learning control, counterexample-guided synthesis, execution-feedback repair, and safe-reset RL occupy the broader mechanism. | **NO-GO as an independent contribution.** A cost-matched open-model replication would be useful engineering evidence, not an ICLR-level distinction. |
| **B. Diagnosable Control under a Collapsing Robust Action Set** | Learnability is governed more by feedback topology—local observability, identifiability, and monotone diagnostic response—than by nominal action-space dimension or geometric tolerance. | Finite partial-monitoring theory already classifies learnability by the joint loss/feedback structure and local observability; dual control and active system identification choose actions for identification; noisy bisection exploits monotone directional feedback; residual control occupies the operational recipe. | **At most a mechanism inside A; NO-GO independently.** “Primitive → residual → saturation → route switch” is domain engineering absent a new law. |
| **C. Macro-Control beyond Point Predictability** | Exact-state forecasts can fail before task-relevant event/value/set predictions; remaining risk budget can change the optimal risk profile. | Value-equivalent models, MuZero, adaptive/short model rollouts, distributional model equivalence, risk-sensitive Bayes-adaptive planning, budgeted MDPs, conformal set prediction, and resource-dependent risk-seeking results occupy both halves. | **Independent NO-GO.** Its components are known, and their combination does not itself yield a new causal law. |

## 1.2 Why this is not a cautious “maybe”

**[VERIFIED FACT]** The August 2026 preprint [AgentRewind: Rewinding Agentic Systems](https://arxiv.org/abs/2608.14380) formalizes checkpoints containing both agent context and environment state, restores them after failure, and injects retained rewind memory so that a new attempt begins from an earlier external state with information learned from the failed continuation. It introduces [MettleBench](https://github.com/Kelvin-Coffee/MettleBench), evaluates several execution strategies, and includes ablations removing environment rewind, context rewind, or rewind memory. This is not a loose thematic neighbor; it instantiates Seed A’s defining asymmetry.

**[VERIFIED FACT]** In finite partial monitoring, learnability depends on the relationship between losses and observable feedback, with local observability governing attainable regret regimes. That is the non-metaphorical core of Seed B: a narrow but diagnostic channel can be easier than a wider but uninformative one. Primary sources include [Bartók et al. (2011)](https://proceedings.mlr.press/v19/bartok11a.html), [Kirschner et al. (2020)](https://proceedings.mlr.press/v125/kirschner20a.html), and [Lattimore and Szepesvári (2020)](https://proceedings.mlr.press/v125/lattimore20a.html).

**[VERIFIED FACT]** Seed C’s “coarse predictions remain decision-useful” component is covered by value-equivalent and value-predictive modeling. Its “risk preference changes with remaining resources” component is covered by budgeted and risk-sensitive planning. A particularly close 2025 preprint, [Emergent Risk Awareness in Rational Agents under Resource Constraints](https://arxiv.org/abs/2505.23436), studies resource-dependent transitions between risk-seeking and survival-oriented behavior.

**[LITERATURE-SUPPORTED JUDGMENT]** The only apparent residual—a cost-matched, information-controlled, superadditive interaction among reset fidelity, retained memory, and feedback observability—is not presently a viable research direction. It has no preliminary evidence, no natural benchmark that cleanly holds decision-relevant information fixed while varying observability, and a direct neighboring paper that already performs the obvious component ablations. A week of computation cannot repair a missing scientific distinction.

## 1.3 What would have been required to survive

A surviving paper would have needed all of the following simultaneously:

1. A **natural public task family**, not a reward-engineered toy, in which an accepted standard policy or metric systematically ranks two routes incorrectly.
2. A **counterintuitive ranking inversion** under strict matching of tokens, verifier calls, environment calls, and wall-clock time.
3. A **single causal variable** not reducible to more information, more retries, safer rollback, larger continuation value, active identification, or a different risk objective.
4. A targeted intervention that removes the inversion while preserving ordinary information amount, compute, and endpoint reachability.
5. Replication across at least two benchmark families and two open-weight models.
6. A contribution that remains after direct comparison with AgentRewind, partial-monitoring/dual-control baselines, active information acquisition, safe exploration, and risk-aware planning.

No seed currently supplies this package.

---

# 2. Repository audit and binding provenance

## 2.1 Files read in full

**[VERIFIED FACT]** The repository contained eight Markdown files on the audited default branch. Each was read completely rather than sampled by title, heading, or executive summary.

| File | Role in this audit | Binding implication |
|---|---|---|
| [`README.md`](https://raw.githubusercontent.com/ScottBlizzard/idle_2/main/README.md) | Repository map and reading order. | Establishes that the later synthesis is the current task specification and earlier reports are provenance, not conclusions to inherit uncritically. |
| [`BILLIARDS_TO_AI_RESEARCH_SYNTHESIS.md`](../current/BILLIARDS_TO_AI_RESEARCH_SYNTHESIS.md) | Current three-seed synthesis; Section 6 contains the binding English task specification. | Defines Seeds A–C, hard constraints, reviewer attacks, and stop conditions. |
| [`AI_RESEARCH_REABSTRACTION.md`](AI_RESEARCH_REABSTRACTION.md) | Adversarial attempt to find a nontrivial abstraction after action-set restriction failed. | Generic re-abstraction, semantic relays, operator addition, and route expansion were not established as novel. |
| [`AI_RESEARCH_REACHABILITY_EXPANSION.md`](AI_RESEARCH_REACHABILITY_EXPANSION.md) | Investigation of tools, operators, subgoals, lemmas, and representations that enlarge reachable solution sets. | Broad “add a capability when stuck” claims were terminated; generic meta-MDP/value-of-computation framing is not novel. |
| [`AI_RESEARCH_CARRIER_VIABILITY.md`](AI_RESEARCH_CARRIER_VIABILITY.md) | Carrier audit for current success damaging future capability and option preservation. | Continuation value, recoverability, optionality, side-effect avoidance, and transaction analogies were judged crowded or reducible to known objectives. |
| [`AI_RESEARCH_IDEA_LANDSCAPE.md`](../archive/AI_RESEARCH_IDEA_LANDSCAPE.md) | Earlier landscape and candidate formalizations. | Useful provenance only; later audits rejected its broadest routes. |
| [`AI_research_idea_scout_prompt.md`](../prompts/AI_research_idea_scout_prompt.md) | Original adversarial scouting specification. | Preserves the initial constraints and anti-renaming requirements. |
| [`AI_research_reabstraction_prompt.md`](../prompts/AI_research_reabstraction_prompt.md) | Specification for the second independent abstraction attempt. | Requires abandoning failed anchors rather than polishing them. |

## 2.2 Binding negative knowledge carried forward

The following are treated as terminated claims, not as available novelty components:

- Reducing or lowering the dimension of an action space improves finite-budget search.
- Adding tools, operators, subgoals, lemmas, or representations when the agent is stuck.
- Current success can damage future capability.
- Preserving reachability, optionality, empowerment, recoverability, or future value.
- Generic adaptive routing, hierarchical control, and value-of-computation formulations.
- Renaming a constrained Bayes-adaptive decision problem as a new object.

**[PROJECT DECISION]** None of those claims is reopened here. When they appear below, they are collision evidence rather than ingredients proposed for reuse.

## 2.3 Constraints that materially shape the verdict

- Exactly eight independent 24 GB RTX 4090 GPUs; every inference worker must fit on one card.
- No physical-robot dependency.
- Public tasks, open weights, official or deterministic evaluators, and reproducible repositories are strongly preferred.
- The first experiment must produce a decisive signal in 3–7 days.
- A 30-day program is permitted only after numerical first-week gates.
- A missing combination of known components is insufficient; the combination must yield a new causal empirical law, a failure of a standard method, and a useful intervention.

**[LITERATURE-SUPPORTED JUDGMENT]** These constraints make software-agent environments the most executable carrier for A, simulation the most executable carrier for B, and Atari or stochastic-control simulation the most executable carrier for C. Those are also the carriers with the closest prior art.

---

# 3. Non-metaphorical reconstruction of the three seeds

## 3.1 Seed A — Resettable Failure with Epistemic Progress

### Non-metaphorical statement

Consider a partially observed task with latent instance parameter \(\theta\), external state \(x_t\), agent memory or belief \(m_t\), and a finite resource budget. Some failed trajectories enter a recoverable set from which a reset operator can approximately restore an earlier external checkpoint, while the agent retains feedback from the failed suffix. The next attempt therefore starts from nearly the same external condition but a different internal information state.

The policy chooses not only task actions but also whether to continue, reset, or terminate. A route with lower immediate success probability can be globally superior if its failures are recoverable and diagnostic, while a route with higher immediate success probability can be inferior if its failures consume an irreversible resource or move the system outside the reset boundary.

### Strongest defensible claim

**[HYPOTHESIS A-strong]** Under exact budget matching, verified reset fidelity, equalized immediate-success probability, and feedback channels matched for scalar information content, the *topology* of failure feedback interacts superadditively with external reset and cross-attempt memory. This interaction reverses the ranking induced by pass@1 or first-attempt expected progress on natural tasks.

This is the strongest form because it excludes the trivial explanations “more attempts,” “more information,” “less damage,” and “more compute.” It is also far stronger than anything currently demonstrated.

### Weakest trivialized version

> Failed attempts are useful when the environment can be restored and the agent remembers the error.

That version is already occupied by iterative learning control, counterexample-guided synthesis, self-debugging, execution-feedback agents, rollback systems, and AgentRewind.

### Required falsifier

If the reset × memory × diagnosticity interaction disappears after matching tokens, verifier calls, environment calls, and decision-relevant information—or if ordinary continuation value explains it—Seed A is dead. Current evidence makes that the default expectation.

## 3.2 Seed B — Diagnosable Control under a Collapsing Robust Action Set

### Non-metaphorical statement

Let the nominal action space be \(\mathcal A\), but define a state- and belief-dependent reliable subset \(\mathcal A_{\mathrm{rel}}(x,b)\) containing actions that satisfy task and safety constraints with high probability. Its useful geometry need not be captured by ambient dimension or volume. A thin or one-dimensional channel may be learnable if action perturbations produce locally monotone, identifiable observations. A geometrically wider channel may be harder if observations are aliased, coupled, or noisy.

The proposed operational strategy is to use a stable natural controller, expose one residual degree of freedom, probe until the response saturates or ceases to be locally identifiable, and then switch routes.

### Strongest defensible claim

**[HYPOTHESIS B-strong]** For natural control tasks with the same robust-success measure and the same observation entropy, local observability of the action-to-feedback map predicts sample efficiency better than reliable-set volume, ambient dimension, or local Lipschitz tolerance. Moreover, a saturation-triggered route switch is causally optimal only when local monotonicity holds.

### Weakest trivialized version

> Low-dimensional, well-shaped, or informative action channels are easier to search and calibrate than high-dimensional noisy ones.

That is not new. It is covered by partial monitoring, system identification, Fisher-information design, coordinate or residual control, and action-representation learning.

### Required falsifier

If an ordinary active-identification or information-directed policy explains performance, if the effect vanishes after controlling for information, or if the residual-control recipe only works on constructed tasks, Seed B is dead as an independent paper.

## 3.3 Seed C — Macro-Control beyond Point Predictability

### Non-metaphorical statement

A learned transition model may become poorly calibrated for exact future states as rollout depth and model mismatch grow, while remaining calibrated for task-relevant events, sets, values, or outcome classes. A planner could therefore vary its prediction abstraction and rollout depth. Separately, the optimal risk profile can depend on remaining recoverable attempts or safety budget: conservative retries may dominate early, while a high-variance action may dominate near terminal failure.

### Strongest defensible claim

**[HYPOTHESIS C-strong]** There exists a natural benchmark on which an abstraction-adaptive planner chooses the finest prediction target whose calibration remains valid and exhibits a nontrivial, model-mismatch-dependent switch in risk preference that cannot be reproduced by a distributional value model, a constrained or budgeted MDP, CVaR planning, or adaptive rollout depth.

### Weakest trivialized version

> Coarse events are easier to predict than exact states, and high variance can be useful when the agent is losing.

Both clauses are known and explicitly barred as sufficient contributions.

### Required falsifier

If value-equivalent or distributional planning plus a standard budget state reproduces the policy, or if the switch follows directly from the reward design, Seed C is dead. Existing literature already strongly supports that outcome.

---

# 4. Formal reduction: why new notation would not create novelty

## 4.1 Reset-feedback constrained Bayes-adaptive semi-MDP

Let:

- \(\theta \sim p_0\) be an unknown task or environment parameter;
- \(x_t \in \mathcal X\) be the externally realized state;
- \(h_t\) be the complete interaction history;
- \(b_t = p(\theta\mid h_t)\) be the posterior belief;
- \(m_t\) be retained agent memory, which may be an imperfect statistic of \(h_t\);
- \(B_t\) be remaining compute, token, verifier, or environment budget;
- \(R_t\) be remaining irreversible-risk or recovery budget;
- \(a_t \in \mathcal A(x_t)\) be a task action;
- \(u_t \in \{\text{continue},\text{reset-to-}k,\text{terminate}\}\) be a meta-action;
- \(y_t \sim Q_\theta(\cdot\mid x_t,a_t,x_{t+1})\) be feedback;
- \(G\) and \(C\) be goal and catastrophe sets.

The augmented decision state is

\[
    s_t^+ = (x_t,b_t,m_t,B_t,R_t,\mathcal K_t),
\]

where \(\mathcal K_t\) is the set of available checkpoints and their restoration metadata. A reset to checkpoint \(k\) induces

\[
   x_{t+1} \sim \mathcal R_k(\cdot\mid x_t), \qquad
   m_{t+1}=U_{\mathrm{reset}}(m_t,h_{k:t}),
\]

with resource decrement \(B_{t+1}=B_t-c_{\mathrm{reset}}\) and any residual external-risk update included in \(R_{t+1}\).

### Reduction lemma

**[INFERENCE]** If the posterior or a sufficient memory statistic is included in the state, checkpoint availability is represented, reset stochasticity is modeled, and all budgets are explicit, the problem is an ordinary constrained Bayes-adaptive semi-MDP or POMDP on \(s_t^+\).

**Proof sketch.** Conditioned on \(s_t^+\) and the chosen task/meta-action, the distribution of the next augmented state is independent of earlier history. Retained feedback changes \(b_t\) or \(m_t\); reset changes the external-state component; safety and compute are state variables. Standard dynamic programming or belief-space planning therefore applies in principle.

### Consequence

A paper cannot claim novelty merely by introducing “epistemically productive reset,” “safe informative failure,” “diagnostic route,” or “macro-control” as new nouns. Scientific novelty must instead be a theorem or empirical law that existing Bayes-adaptive, information-directed, constrained, or risk-sensitive formulations do not already predict.

## 4.2 Reset fidelity

For checkpoint state \(x_k\), metric \(d_x\), tolerance \(\epsilon_R\), and failure probability \(\delta_R\), define

\[
  \Pr\left[d_x(X^{\mathrm{reset}},x_k)\le \epsilon_R\right] \ge 1-\delta_R.
\]

This definition must include every state component that can influence future evaluation. In software agents, filesystem restoration without process, cache, network, credential, clock, or external-service restoration is not exact reset.

A **safe recoverable failure** is a failed trajectory whose side effects stay inside a declared reset boundary and whose restoration satisfies the condition above. An **irreversible failure** violates the boundary or consumes a nonrenewable resource.

## 4.3 Diagnosticity

A first proxy is conditional information gain:

\[
  D_{\mathrm{MI}}(a\mid s)=I(\theta;Y\mid s,a,F),
\]

where \(F\) denotes the failure branch. This proxy is insufficient: equal mutual information can support different decisions. A decision-relevant alternative is expected reduction in Bayes regret:

\[
  D_{\mathrm{BR}}(a\mid s)
   = \mathbb E\left[\min_{a'}\mathbb E[L(a',\theta)\mid s]
   -\min_{a'}\mathbb E[L(a',\theta)\mid s,Y]\right].
\]

Partial-monitoring theory further shows that *which loss differences are observable from feedback* matters, not only scalar entropy or mutual information. This is why “diagnosability” does not currently constitute a new abstraction.

## 4.4 Reliable action set

For safety tolerance \(\alpha\), define

\[
\mathcal A_{\mathrm{rel}}(x,b;\alpha)=
\left\{a\in\mathcal A(x):
\Pr(G\cup \mathcal X_{\mathrm{recoverable}}\mid x,b,a)\ge 1-\alpha,
\ \Pr(C\mid x,b,a)\le \alpha
\right\}.
\]

Ambient dimension, intrinsic dimension, volume, curvature, connectedness, and feedback observability are distinct properties. Seed B is correct to reject volume as a universal difficulty measure, but that rejection is already standard in partial monitoring and active identification.

## 4.5 Objective and safety conditions

A representative lexicographic objective is:

1. Minimize \(\Pr(\tau_C\le \tau_G,\ C_{0:\tau}\le B_0)\).
2. Subject to the best achievable level of objective 1, maximize

\[
\Pr(\tau_G < \tau_C,\ C_{0:\tau}\le B_0).
\]

An equivalent constrained form maximizes success probability subject to

\[
\mathbb E[C_{0:\tau}]\le B_0,
\qquad
\Pr(\tau_C<\tau_G)\le \delta.
\]

These are standard constrained and risk-aware objectives. A novel contribution must arise from a result about their behavior, not their restatement.

## 4.6 The only plausible residual interaction

Define a factorial value \(V(r,m,d)\) for reset availability \(r\in\{0,1\}\), cross-attempt memory \(m\in\{0,1\}\), and diagnostic feedback \(d\in\{0,1\}\), under matched budgets and action interfaces. The three-way interaction is

\[
\begin{aligned}
\Delta_{RMD} ={}& V(1,1,1)-V(1,1,0)-V(1,0,1)-V(0,1,1)\\
&+V(1,0,0)+V(0,1,0)+V(0,0,1)-V(0,0,0).
\end{aligned}
\]

**[HYPOTHESIS]** A positive, transferable \(\Delta_{RMD}\) after information and compute matching would be a potentially interesting empirical law.

**[LITERATURE-SUPPORTED JUDGMENT]** This is not currently a viable paper thesis. AgentRewind already tests the obvious components; partial-monitoring theory predicts feedback-structure interactions; and no natural benchmark offers a credible way to hold decision-relevant information fixed while changing only observability topology. A positive effect from corrupted or removed feedback would be expected, not novel.

---

# 5. Verified primary-source literature map

The map prioritizes papers that occupy a mechanism rather than merely sharing vocabulary. For every close source it records what is established, the experiment or theorem, which seed territory it occupies, and whether the residual gap is scientific or merely implementation/evaluation.

## 5.1 Reset, rewind, rollback, and retained failure information

| Primary source | What it already establishes | Experiment or theorem | Seed territory occupied | Residual gap |
|---|---|---|---|---|
| [AgentRewind: Rewinding Agentic Systems (arXiv, 2026)](https://arxiv.org/abs/2608.14380); [official implementation](https://github.com/Futuresis/replay-agent-recorder) | Checkpoints jointly represent agent context and environment state; failure can trigger restoration of both while rewind memory records what failed. The paper separates environment rewind, context rewind, and retained memory. | MettleBench, Terminal-Bench 2.0, several agent harnesses, execution-strategy comparisons, and component ablations. | **A—direct defining mechanism.** | Strict cost matching, open-model replication, and broader domains are evaluation/implementation gaps. A scientific gap exists only if a new interaction remains after those controls. |
| [MettleBench (official repository, 2026)](https://github.com/Kelvin-Coffee/MettleBench) | Provides 82 long-horizon engineering tasks with 640 ordered criteria and deterministic evaluation exposing the first unsatisfied criterion. | Rewritten tasks derived from public software-engineering benchmarks; criterion-by-criterion hidden evaluation. | **A/B carrier:** recoverable workspace failures plus unusually diagnostic ordered feedback. | The ordered checklist may itself create diagnosability; that is a benchmark property, not a discovered law. |
| [GA-Rollback (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.892/) | Uses global and local signals to decide how far to roll back instead of always continuing or restarting. | Mathematical and reasoning benchmarks with adaptive rollback versus non-rollback baselines. | **A:** failure localization and retained reasoning context. | Environment-state restoration is weaker than AgentRewind; this is a carrier distinction, not broad novelty. |
| [WebRollback (EACL 2026)](https://aclanthology.org/2026.eacl-short.12/) | Lets web agents decide whether and where to roll back after an erroneous action. | Mind2WebLive and WebVoyager, with zero-shot and fine-tuned variants. | **A:** adaptive recovery in GUI/web trajectories. | Live sites drift and external effects are not fully reversible. Better state capture is systems engineering. |
| [DeltaBox (arXiv, 2026)](https://arxiv.org/abs/2605.22781) | OS-level incremental snapshots make speculative branches and rollback cheap enough to increase exploration under fixed time. | Software-agent and RL microbenchmarks measuring checkpoint/rollback overhead and explored branches. | **A:** bounded-cost reversible failure and speculative execution. | Infrastructure, not a new epistemic law. |
| [Crab (arXiv, 2026)](https://arxiv.org/abs/2604.28138) | Semantic checkpoints improve recovery relative to naive periodic checkpointing while reducing unnecessary checkpoint traffic. | Shell/code-repair workloads with injected failures and recovery evaluation. | **A:** reset fidelity and checkpoint placement. | Systems-policy gap only. |
| [DART (arXiv, 2026)](https://arxiv.org/abs/2605.23311) | Uses dependency and commitment information to determine when rollback is safe and semantically valid. | Structured tool-agent settings and framework integration. | **A:** recoverability boundary and irreversible side effects. | A stronger runtime would not establish the seed’s proposed AI law. |
| [Atomix (arXiv, 2026)](https://arxiv.org/abs/2602.14849) | Stages external effects and commits them transactionally, preventing partial workflows from corrupting external state. | Tool-agent workflows with faults and transactional recovery. | **A:** transactions, safe failure, and commit boundaries. | Directly occupies the transaction analogy; retained learning is separable. |
| [Cordon (arXiv, 2026)](https://arxiv.org/abs/2606.17573) | Defines semantic transaction boundaries for workflows containing irreversible operations. | Benign and adversarial workflow evaluations. | **A:** recoverability versus commitment. | Combining it with memory is a component combination unless a new causal effect follows. |
| [ACRFence (arXiv, 2026)](https://arxiv.org/abs/2603.20625) | Shows that replaying or regenerating external calls during rollback can create semantic inconsistency and security failures. | Proof-of-concept rollback attacks and mitigation experiments. | **A:** attacks naive exact-reset assumptions. | Security hardening weakens rather than rescues the broad seed. |
| [Leave No Trace (2018)](https://arxiv.org/abs/1711.06782) | Jointly learns a forward policy and reset policy; reset value estimates when exploration risks entering an unrecoverable state. | Simulated and physical continuous-control tasks. | **A:** safe exploration with learned recoverability. | Retained epistemic progress is not isolated, but the broad safe-reset idea is occupied. |
| [Recovery RL (2020)](https://arxiv.org/abs/2010.15920) | Uses an offline safety critic and recovery policy to keep exploration inside recoverable regions. | Six simulated domains and a physical-robot navigation task. | **A/B:** recoverable-state geometry and safety intervention. | Reset-memory interaction is absent; adding it needs a new law, not a module. |
| [Reachability Constrained Reinforcement Learning (ICML 2022)](https://proceedings.mlr.press/v162/yu22d.html) | Enforces persistent safety by reasoning over feasible/reachable safe sets. | Continuous-control safety benchmarks. | **A/B:** recoverability and reliable control sets. | Already covers viability geometry. |
| [A Learnable Safety Measure (CoRL 2019)](https://proceedings.mlr.press/v100/heim20a.html) | Learns whether future constraint satisfaction remains possible from a state. | Robotic/control simulations. | **A/B:** future recoverability and safe action choice. | No opening for generic “preserve recoverability.” |
| [Failure-Aware Iterative Learning of State-Control Invariant Sets (arXiv, 2026)](https://arxiv.org/abs/2604.06776) | Learns admissible state-control regions from one-step failing state-input pairs without known dynamics and gives convergence properties. | Numerical control experiments including a double-integrator setting. | **A/B—close:** failures progressively identify the reliable region. | Natural high-dimensional transfer is empirical; the core mechanism is explicit. |

## 5.2 Failure feedback, iterative repair, and counterexamples

| Primary source | What it already establishes | Experiment or theorem | Seed territory occupied | Residual gap |
|---|---|---|---|---|
| [Reflexion (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) | Converts task feedback into verbal reflections stored in episodic memory and reused on later trials. | Sequential decision, reasoning, and programming tasks. | **A:** failure feedback plus cross-attempt memory. | External-state rewind was absent; AgentRewind closes that gap. |
| [Teaching Large Language Models to Self-Debug (ICLR 2024)](https://openreview.net/forum?id=KuPixIqPiq) | Uses execution outcomes and model-generated explanations to iteratively repair code. | Text-to-SQL, code translation, and program-generation tasks. | **A:** execution feedback and retry improvement. | Reset is implicit through rerunning code in a sandbox. |
| [LEVER (ICML 2023)](https://proceedings.mlr.press/v202/ni23b.html) | Learns a verifier over the problem, generated program, and execution result to rerank candidates. | Four language-to-code datasets. | **A/B:** diagnostic verifier feedback and selection. | Sequential rewind is not central, but “verifier feedback helps” is occupied. |
| [NExT (ICML 2024)](https://proceedings.mlr.press/v235/ni24a.html) | Self-trains execution-aware reasoning from execution traces. | Code-reasoning and trace-prediction tasks. | **A/B:** structured failure observations improve internal reasoning. | Cross-attempt control is an implementation choice. |
| [RLEF (ICML 2025)](https://proceedings.mlr.press/v267/gehring25a.html) | Trains code models using executable feedback rather than only text supervision. | Program-generation benchmarks with unit tests. | **A/B:** failure signal as learning supervision. | Online checkpointing is separate; broad productive failure is known. |
| [μCODE (ICML 2025)](https://proceedings.mlr.press/v267/jain25a.html) | Formulates iterative code repair as a recoverable multi-turn process driven by execution feedback. | Code-generation benchmarks with repeated execution and repair. | **A—close at task level.** | External workspace restoration is narrower than AgentRewind; broad novelty is gone. |
| [Combinatorial Sketching / CEGIS lineage (ASPLOS 2006)](https://people.csail.mit.edu/asolar/papers/asplos06.pdf) | Alternates candidate generation with counterexamples that eliminate inconsistent candidates; failure information accumulates while the specification persists. | Program-synthesis benchmarks and algorithmic analysis. | **A/B:** externally repeatable attempts with epistemically progressive counterexamples. | Scaling to natural agents is implementation, not a new principle. |
| [COPRA (COLM 2024)](https://arxiv.org/abs/2310.04353) | Uses proof-state feedback, backtracking, and retained search history in Lean and Coq. | miniF2F and CompCert theorem-proving tasks. | **A:** reset to proof states plus informative failures. | Blocks theorem proving as a clean carrier. |
| [Proving Theorems Recursively (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/9de7a49945898da86e062e7029baa284-Paper-Conference.pdf) | Decomposes proof goals into recursively verified sketches and subclaims. | Formal theorem-proving benchmarks. | Earlier binding negative route: tools/subgoals/lemmas and reachability expansion. | No reopening is justified. |
| [Prover Agent (arXiv, 2025)](https://arxiv.org/abs/2506.19923) | Uses Lean feedback and generated auxiliary lemmas in an iterative agent. | miniF2F and related formal-proof tasks. | **A/B** plus the rejected “add lemmas” route. | Crowded carrier; implementation refinements only. |

## 5.3 Observability, active identification, and reliable control geometry

| Primary source | What it already establishes | Experiment or theorem | Seed territory occupied | Residual gap |
|---|---|---|---|---|
| [Minimax Regret of Finite Partial-Monitoring Games (COLT 2011)](https://proceedings.mlr.press/v19/bartok11a.html) | Classifies games by the relation between losses and observable feedback rather than action-space volume. | Minimax-regret theory and canonical game classes. | **B—core abstraction.** | Natural deep-agent validation is empirical, but the principle is not novel. |
| [Information Directed Sampling for Linear Partial Monitoring (COLT 2020)](https://proceedings.mlr.press/v125/kirschner20a.html) | Derives adaptive regret guarantees controlled by observability and information ratio. | Theory and structured online-learning examples. | **B:** diagnostic feedback as a determinant of learnability. | Scaling is application work unless a new law emerges. |
| [Exploration by Optimisation in Partial Monitoring (COLT 2020)](https://proceedings.mlr.press/v125/lattimore20a.html) | Chooses exploration using the loss/feedback geometry of partial-monitoring problems. | Regret analysis across finite games. | **B:** observation-aware action choice. | Direct theoretical collision. |
| [Dual Control for Approximate Bayesian Reinforcement Learning (JMLR 2016)](https://www.jmlr.org/papers/v17/15-162.html) | Treats actions as simultaneously controlling the system and identifying uncertain dynamics. | Bayesian control simulations. | **A/B:** actions selected for future information and control value. | “Diagnostic action” is not new. |
| [Amortized Bayesian Experimental Design for Decision-Making (ICML 2020)](https://proceedings.mlr.press/v119/kleinegesse20a.html) | Optimizes experiments by estimated mutual information with amortized neural estimators. | Bayesian experimental-design tasks. | **B:** information-maximizing probes. | Scalar information differs from local observability, but both are established. |
| [ASID: Active Exploration for System Identification in Robotic Manipulation (ICLR 2024)](https://arxiv.org/abs/2404.12308) | Uses a simulator prior to design interactions that identify unknown physical parameters before manipulation. | Articulation, mass, and manipulation experiments in simulation and on robots. | **B:** diagnostic control and active system identification. | Robot dependence violates the preferred carrier; simulation-only replication is less compelling. |
| [Probabilistic Bisection Converges Almost as Quickly as Stochastic Approximation (ICML 2013)](https://proceedings.mlr.press/v28/sznitman13.pdf) | Exploits noisy directional feedback to localize a target efficiently. | Stochastic root-finding theory and simulations. | **B:** narrow, monotone, highly diagnosable channel. | Direct conceptual collision. |
| [Residual Reinforcement Learning for Robot Control (ICRA 2019)](https://arxiv.org/abs/1812.03201) | Adds a learned residual action to a stable hand-designed controller. | Real-robot block assembly and control tasks. | **B:** natural primitive plus residual variable. | Saturation-triggered switching is engineering absent a new law. |
| [Learning Action Representations for Reinforcement Learning (ICML 2019)](https://proceedings.mlr.press/v97/chandak19a.html) | Learns a lower-dimensional action representation and decoder for large action spaces. | Large-action-space benchmarks and theory. | **B** and a binding negative claim about action dimension. | No reopening. |
| [SALAS (CoRL 2022)](https://proceedings.mlr.press/v199/corrado22a.html) | Learns structured latent action spaces to make control more tractable. | Continuous-control and robotic tasks. | **B:** structured/reduced control manifold. | Crowded and partly robot-dependent. |
| [Robot Reinforcement Learning on the Constraint Manifold (CoRL 2021)](https://proceedings.mlr.press/v164/liu22c.html) | Keeps learned actions on task-constraint manifolds instead of the full ambient space. | Robotic manipulation/control tasks. | **B:** collapsing reliable action set and manifold control. | Missing nonrobot carrier is not a new mechanism. |

## 5.4 Macro prediction, model mismatch, and resource-dependent risk

| Primary source | What it already establishes | Experiment or theorem | Seed territory occupied | Residual gap |
|---|---|---|---|---|
| [The Value Equivalence Principle (NeurIPS 2020)](https://proceedings.neurips.cc/paper_files/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html) | A model need not reproduce observations exactly if it preserves values needed by the planner. | Theory and model-learning experiments comparing task-relevant objectives with likelihood learning. | **C—core macro/task-relevant prediction claim.** | Event-calibration diagnostics may be useful, but the principle is known. |
| [MuZero (Nature 2020)](https://www.nature.com/articles/s41586-020-03051-4) | Learns reward, value, and policy-relevant latent dynamics without reconstructing observations. | Go, chess, shogi, and 57 Atari games. | **C:** decision-useful prediction beyond exact state prediction. | Direct collision at scale. |
| [MBPO: When to Trust Your Model (NeurIPS 2019)](https://proceedings.neurips.cc/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) | Controls model bias by using short model rollouts rather than trusting long uncertain predictions. | MuJoCo continuous-control benchmarks. | **C:** uncertainty-aware rollout depth. | Horizon mismatch is occupied. |
| [STEVE (NeurIPS 2018)](https://proceedings.neurips.cc/paper/2018/hash/f02208a057804ee16ac72ff4d3cec53b-Abstract.html) | Uses model uncertainty to weight value targets from different rollout horizons. | Continuous-control benchmarks. | **C:** uncertainty-aware depth selection. | Direct collision. |
| [A Distributional Perspective on Reinforcement Learning (ICML 2017)](https://arxiv.org/abs/1707.06887) | Models return distributions rather than only expectations, enabling tail- and risk-sensitive decisions. | Atari 2600. | **C:** outcome distributions and high-variance decisions. | “High variance can help” is not novel. |
| [Distributional Model Equivalence (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/file/b0cd0e8027309ea050951e758b70d60e-Paper-Conference.pdf) | Shows that ordinary value equivalence may be insufficient for risk-sensitive planning and defines equivalence notions preserving selected risk measures. | Tabular and larger-scale model-based RL experiments. | **C—direct:** task-relevant prediction plus distributional risk. | Leaves implementation and benchmark choice, not the broad claim. |
| [Budgeted Reinforcement Learning in Continuous State Space (NeurIPS 2019)](https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html) | Makes remaining cost budget part of the state and learns policies trading reward and cost. | Continuous-state budgeted-MDP experiments. | **C:** policy changes as remaining budget changes. | Direct reduction of the desperation switch to a standard budget state. |
| [Risk-Averse Bayes-Adaptive Reinforcement Learning (NeurIPS 2021)](https://proceedings.neurips.cc/paper/2021/hash/08f90c1a417155361a5c4b8d297e0d78-Abstract.html) | Optimizes CVaR in a Bayes-adaptive MDP, accounting jointly for epistemic and aleatoric uncertainty. | Bayesian planning experiments with Monte Carlo tree search and optimization. | **C:** risk-aware belief-state planning. | Direct collision. |
| [Emergent Risk Awareness in Rational Agents under Resource Constraints (arXiv, 2025)](https://arxiv.org/abs/2505.23436) | Analyzes how resource level and horizon induce transitions between risk-seeking and survival-oriented behavior without a special desperation module. | Survival-bandit analysis, numerical examples, and an open-source-LLM decision experiment. | **C—closest to budget-exhaustion risk switching.** | Natural transfer is empirical; the qualitative law is occupied. |
| [Conformal Predictive Programming for Chance-Constrained Shrinking-Horizon MPC (L4DC 2024)](https://proceedings.mlr.press/v242/stamouli24a.html) | Uses conformal uncertainty sets to enforce chance constraints while planning horizon shrinks. | Control benchmarks with finite-sample safety analysis. | **C:** set prediction and chance-constrained planning. | Event-level model choice is an application detail. |
| [Adaptive Conformal Prediction for Motion Planning among Dynamic Agents (L4DC 2023)](https://proceedings.mlr.press/v211/dixit23a.html) | Adapts conformal uncertainty sets online under changing prediction errors. | Simulated dynamic-agent motion planning. | **C:** calibrated set-level prediction under mismatch. | Broad claim occupied. |

## 5.5 Coverage of the required collision families

| Required family | Representative primary sources | Audit conclusion |
|---|---|---|
| Reversible/resettable MDPs; recoverability; safe exploration | Leave No Trace; Recovery RL; Reachability-Constrained RL; Learnable Safety Measure | Broad reset/recoverability claims are mature. |
| Rollback, transactions, checkpointing, sandboxing, speculative execution | AgentRewind; DeltaBox; Crab; DART; Atomix; Cordon; ACRFence | Seed A now has a direct 2026 systems-and-agent cluster. |
| Learning from failure; verifier/execution feedback; iterative repair | Reflexion; Self-Debugging; LEVER; NExT; RLEF; μCODE; CEGIS | “Failure feedback improves the next attempt” is decisively non-novel. |
| Active learning; Bayesian design; value of information; dual control | Dual Control; Bayesian experimental design; information-directed sampling | Seed B’s diagnostic-action component is known. |
| Bayes-adaptive and belief-state planning | Dual Control; Risk-Averse Bayes-Adaptive RL | Seeds A and C reduce to known augmented-state planning unless a new law is shown. |
| Lexicographic/constrained objectives; irreversible side effects; option preservation | Budgeted RL; reachability-constrained RL; transaction systems; repository carrier audit | Explicitly barred as a novelty route. |
| Observability, identifiability, Fisher information, diagnostic actions | Partial monitoring; ASID; Bayesian design; probabilistic bisection | Seed B’s strongest abstraction collides directly. |
| Action manifolds, robust controllability, viability kernels, low-rank control | Residual RL; action representations; constraint-manifold RL; invariant-set learning | Geometry and control-structure claims are crowded. |
| Continuation, coordinate/residual control, gain scheduling, saturation | Residual RL; probabilistic bisection; classic adaptive/hybrid control | The operational recipe is engineering unless a new invariant appears. |
| Options, skill chaining, action representation, temporal abstraction | Action-representation learning; repository reachability audit | Binding negative result; not reopened. |
| Distributional/risk-sensitive/robust RL, stochastic MPC, chance constraints | Distributional RL; distributional model equivalence; risk-averse BAMDP; conformal MPC | Seed C is occupied. |
| Set prediction, event prediction, value-equivalent world models | Value Equivalence; MuZero; conformal prediction | “Macro events survive point-prediction failure” is known. |
| Uncertainty-aware rollout depth | MBPO; STEVE | Direct collision. |
| Risk-seeking under losses, remaining budgets, desperation strategies | Budgeted RL; Emergent Risk Awareness; risk-sensitive planning | Direct collision; reward-designed inversions are especially weak. |
| Formal theorem proving | COPRA; Proving Theorems Recursively; Prover Agent | Reset/backtrack/feedback and generated-lemma carriers are active and crowded. |
| Code, tool, web/GUI agents | AgentRewind/MettleBench; GA-Rollback; WebRollback; transactional systems | Most executable carrier, but also most directly preempted. |
| Generative modeling and GPU simulation | Distributional/model-based RL; conformal planning; rejection/repair pipelines | Executable but likely to yield synthetic or already-predicted effects. |

---

# 6. Novelty-collision matrix

Scores use **0 = no meaningful collision**, **3 = substantial overlap**, and **5 = direct occupation**.

| Proposed claim | Closest prior mechanisms | Collision | What remains after subtraction | Verdict |
|---|---|---:|---|---|
| A1. External task state resets while internal knowledge progresses | AgentRewind; CEGIS; iterative learning control; code repair | **5.0** | Cost-matched open-model replication and reset-boundary verification | Implementation/evaluation, not sufficient science |
| A2. Repeated failures are not independent retries | Reflexion; self-debugging; μCODE; COPRA | **5.0** | Nothing broad | Eliminated |
| A3. A lower-immediate-success route wins because failure is safe and informative | Bayes-adaptive planning; dual control; safe-reset RL; AgentRewind | **4.5** | A natural, information-matched inversion unexplained by continuation value or information value | No evidence; very high burden |
| A4. Exact context–environment alignment is necessary | AgentRewind ablations; transactional/checkpoint systems | **5.0** | Broader open-model replication | Implementation |
| A5. Apparent success can be worse than recoverable failure | Constrained/Bayes-adaptive value functions; prior carrier audit | **5.0** | Only a standard-metric failure with a causal intervention | No carrier identified |
| A6. Reset fidelity and diagnostic feedback interact nonlinearly | AgentRewind ablations; partial monitoring; invariant-set learning | **4.0** | A transferable three-way reset × memory × observability law under information matching | Sole residual hypothesis, not a direction |
| B1. Nominal dimension differs from the reliable action set | Constraint manifolds; viability kernels; action representations | **5.0** | Nothing broad | Eliminated |
| B2. Geometric tolerance does not determine learnability | Partial monitoring; dual control; active identification | **5.0** | A natural-task predictor outperforming observability/information measures | No evidence |
| B3. A narrow diagnostic channel beats a wider noisy channel | Partial monitoring; probabilistic bisection | **5.0** | Deep-agent natural-task demonstration | Application, likely constructed |
| B4. Natural primitive plus one residual variable | Residual RL; latent action learning | **5.0** | Saturation-triggered switch | Engineering absent a new law |
| B5. Saturation should trigger a route switch | Gain scheduling; hybrid control; active identification | **4.0** | Cross-domain invariant threshold | Unsupported and hard to benchmark naturally |
| C1. Point prediction fails before task-relevant prediction | Value Equivalence; MuZero | **5.0** | Calibration diagnostics or implementation | Eliminated as contribution |
| C2. Rollout abstraction/depth should adapt to uncertainty | STEVE; MBPO; robust MPC | **5.0** | Different implementation | Eliminated |
| C3. Near budget exhaustion, optimal behavior becomes risk-seeking | Budgeted MDPs; resource-constrained risk analysis | **5.0** | A qualitatively new, non-reward-induced transition | Directly threatened by 2025 work |
| C4. Macro prediction and desperation switching belong in one policy | Distributional model equivalence; risk-sensitive BAMDP | **4.5** | Causal coupling between calibration scale and risk switch | No evidence; combination insufficient |

## 6.1 Scientific versus implementation gaps

| Candidate gap | Classification | Reason |
|---|---|---|
| Run AgentRewind with an open Qwen model instead of a proprietary frontier model | Implementation/reproducibility | Changes model and cost profile, not mechanism. |
| Match token, verifier, environment-call, and wall-clock budgets | Evaluation hygiene | Necessary, but not a causal discovery. |
| Add exact filesystem hashing and external-side-effect auditing | Systems correctness | Important after ACRFence, but not the requested AI insight. |
| Compare ordered feedback with binary error feedback | Expected ablation | Removing useful information should hurt. |
| Match feedback entropy while varying semantic structure | Potentially scientific but insufficient | Entropy is not decision-relevant information; partial monitoring predicts structure matters. |
| Match posterior decision value while varying only local observability | Potentially scientific | Difficult to define on natural-language feedback; no feasible public benchmark was found. |
| Show a transferable three-way reset × memory × observability interaction | Potentially scientific | Could reopen the question, but direct prior art and theory make the prior low. |
| Build a benchmark engineered to exhibit that interaction | Synthetic effect | It would likely bake the conclusion into the feedback matrix. |

---

# 7. Carrier generation and elimination funnel

Eighteen mechanism-diverse carriers were considered. A carrier was eliminated if it was directly occupied, robot-dependent, evaluator-unstable, frontier-compute-heavy, likely to manufacture the effect, or incapable of a decisive first-week test.

| # | Carrier | Public task/evaluator candidate | Seed | 8×4090 feasibility | Adversarial assessment | Decision |
|---:|---|---|---|---|---|---|
| 1 | Repository/code agents with filesystem checkpoints | MettleBench; mini-SWE-agent; SWE-bench-derived workspaces | A/B | High | Best natural carrier, but directly occupied by AgentRewind. Ordered criteria may create diagnosticity. | **Eliminate for novelty** |
| 2 | Terminal/shell agents in containers | Terminal-Bench 2.0; InterCode-style environments | A | Medium–high | Rollback/checkpoint systems are already a 2026 cluster; tasks can be slow and nondeterministic. | Eliminate |
| 3 | Web/GUI agents | Mind2WebLive; WebVoyager | A/C | Medium | WebRollback exists; websites drift, external effects can be irreversible, and evaluation is noisy. | Eliminate |
| 4 | Structured tool workflows | Public LangGraph-style workflows; ToolBench-like tasks | A | High | DART, Atomix, and Cordon occupy semantic recovery and transactions. Mock tools make reversibility artificial. | Eliminate |
| 5 | SQL/database agents using transactions | Spider/BIRD-derived sandboxes | A/B | High | Rollback is native and obvious; execution feedback is mature. Positive results look like database engineering. | Eliminate |
| 6 | Formal theorem proving with proof-state rollback | miniF2F; LeanDojo; Coq/Lean proof states | A/B | Medium | COPRA already backtracks with proof-state feedback; generated lemmas/subgoals are binding negative routes. | Eliminate |
| 7 | CEGIS/program synthesis | SyGuS and finite-program suites | A/B | High | Counterexamples already instantiate resettable epistemic progress exactly. | Eliminate |
| 8 | Multi-turn code generation from tests | HumanEval+, MBPP+, APPS subsets | A/B | High | Reflexion, Self-Debugging, LEVER, NExT, RLEF, and μCODE make this crowded. | Eliminate |
| 9 | Safe exploration in continuous-control simulators | Safety Gymnasium; MuJoCo; reachability tasks | A/B | High | Leave No Trace, Recovery RL, viability measures, and reachability constraints occupy the space. Designed resets risk a toy effect. | Eliminate |
| 10 | Iterative learning control on repeated trajectories | Public trajectory-tracking simulators | A/B | High | The external task repeats while trial-to-trial error is retained: the classical mechanism itself. | Eliminate |
| 11 | Active system identification before manipulation | Isaac Gym/MuJoCo parameter identification | B | High in simulation | ASID and dual control occupy diagnostic probing. Simulator-only evidence invites “constructed identifiability.” | Eliminate |
| 12 | Cyber-range/network-configuration rollback | Containerized network labs | A/B | Medium | Checkpointing is natural, but rollback/transaction safety is mature and evaluators are heterogeneous. | Eliminate |
| 13 | Atari/world-model planning with macro events | ALE official scores | C | Medium–high | MuZero, value equivalence, distributional models, and adaptive rollout trust occupy the thesis. | Eliminate |
| 14 | Stochastic MPC or driving simulation | CARLA; conformal MPC tasks | B/C | Medium | Conformal set prediction and chance-constrained control already cover calibrated macro sets; first-week causality would be weak. | Eliminate |
| 15 | Board-game/MCTS “last-chance” play | OpenSpiel; chess/Go variants | C | High | Risk changes with score, horizon, and remaining moves are standard dynamic-programming/game-theoretic effects. | Eliminate |
| 16 | Generative-model sampling with reversible rejection/repair | Diffusion/autoregressive constraint tasks | A/C | High | Rejection, resampling, verifier guidance, and iterative refinement are standard. | Eliminate |
| 17 | Multi-agent negotiation or adversarial mixing | OpenSpiel bargaining/security games | C | High | High variance or mixing when behind is predicted by equilibrium and risk-sensitive objectives. | Eliminate |
| 18 | Scientific experimental design with safe failed trials | Public Bayesian-optimization simulators | A/B | High | Bayesian experimental design and dual control already value informative failures. Physical validation is unavailable. | Eliminate |

## 7.1 Funnel summary

| Funnel stage | Carriers remaining | Reason for removal |
|---|---:|---|
| Initial mechanism-diverse candidates | 18 | — |
| Remove direct literature occupation | 7 | Code/tool/web rollback, CEGIS, proof search, safe-reset RL, and model-based risk planning are occupied. |
| Remove artificial-effect carriers | 4 | Constructed finite games, simulator-only diagnostic channels, and reward-designed desperation switches miss the natural-task bar. |
| Remove evaluator instability or robot dependence | 1 | Web/GUI and real-system-ID carriers are unsuitable for a decisive GPU-only test. |
| Final candidate | 1 | MettleBench/AgentRewind factorial replication. |
| Remove insufficient novelty | **0** | Even a positive result is predominantly a replication/ablation of a paper released before the audit date. |

**[PROJECT DECISION]** The funnel terminates at zero. The last candidate is retained only as a falsification protocol, not as an authorized direction.


---

# 8. Separate decisions on Seeds B and C

## 8.1 Is Seed B an independent paper, a mechanism inside Seed A, or NO-GO?

> **[PROJECT DECISION] Seed B is a plausible explanatory moderator inside Seed A, but a NO-GO as an independent paper.**

The nontrivial part of B is not “small action spaces are easier.” It is that two channels with comparable geometric tolerance can differ sharply because one makes payoff-relevant distinctions observable. That is a real mechanism, but it is already occupied:

1. **Partial monitoring formalizes it.** Local observability and feedback geometry determine learnability and regret.
2. **Dual control and active system identification operationalize it.** Actions are selected because they expose uncertain dynamics.
3. **Probabilistic bisection is the canonical one-dimensional case.** A thin monotone response supports efficient localization despite noise.
4. **Residual control supplies the proposed interface.** A stable primitive plus learned residual is established.
5. **Saturation-triggered switching is not a standalone contribution.** Without a cross-domain law or theorem, it is gain scheduling or hybrid control.

The only legitimate role for B would be as a moderator of A: rewind is useful only when retained failure observations distinguish future actions. MettleBench’s ordered-criterion evaluator already makes that intuition likely, so even this role is not new enough by itself.

## 8.2 Does Seed C survive independently?

> **[PROJECT DECISION] Seed C is an independent NO-GO.**

C contains two separable claims:

- **Prediction abstraction:** exact state reconstruction can be unnecessary or unreliable while value-, event-, or set-level predictions remain useful.
- **Risk-budget switching:** as resources or attempts disappear, the optimal action can move toward higher variance.

The first is occupied by value equivalence, MuZero, short/adaptive model rollouts, distributional model equivalence, and conformal sets. The second is occupied by budgeted MDPs, risk-sensitive Bayes-adaptive planning, survival-bandit/resource analyses, and ordinary dynamic programming. Joining the two does not force a new causal relationship. A planner whose budget state selects both abstraction and risk is a routine augmented-state policy.

A viable C paper would need evidence that *calibration scale causally controls the risk switch* after holding the return distribution and budget fixed. No natural benchmark or mechanism supporting such an intervention was found.

## 8.3 Merge decision

> **[PROJECT DECISION] Do not merge A, B, and C.**

- A and B share a possible reset × observability interaction, but AgentRewind plus partial-monitoring theory already anticipates it.
- C adds a different mechanism—model abstraction and budget-dependent risk—that broadens the paper while weakening causal focus.
- A three-seed paper would read as a framework unifying known ideas, explicitly disallowed by the novelty rules.

---

# 9. Direction selection

## 9.1 Primary direction

**None selected.**

## 9.2 Fallback direction

**None selected.**

## 9.3 Strongest surviving formulation (residual only; not selected)

For clarity, the sole residual hypothesis is:

> Under strict compute and information matching, external reset, cross-attempt memory, and feedback local observability exhibit a positive three-way interaction on natural tasks, causing a route-ranking inversion that cannot be reproduced by an ordinary Bayes-adaptive or information-directed policy.

This is not selected because:

- direct prior art already studies the three obvious components;
- the information-matching intervention is not well-defined for natural-language feedback;
- a positive true-feedback-versus-shuffled-feedback result would be expected;
- a negative result would merely confirm the collision analysis;
- one week cannot provide the second natural domain and theoretical separation required for transfer.

---

# 10. Exact failure target and causal signature a surviving result would require

Although no direction survives, the rejection criterion should be explicit.

## 10.1 Standard metric or policy predicted to fail

A credible paper would have to show systematic failure of at least one accepted target:

1. **First-attempt success / pass@1** as a route-ranking metric.
2. **Current evaluator progress** or number of completed criteria as a myopic route-selection metric.
3. **Continue-from-current-state** as the default recovery policy after a failed suffix.
4. A **Bayes-adaptive value-of-information policy** with the same reset, memory, and budget state.
5. An **information-directed or active-identification policy** using the same feedback channel.

Beating “restart from scratch without feedback” is not sufficient.

## 10.2 Required counterintuitive ranking inversion

Let route \(a\) have higher first-attempt success than route \(b\):

\[
    p_1(a) > p_1(b).
\]

The claimed inversion would be

\[
    V_{B,R}(b) > V_{B,R}(a)
\]

under identical total budgets \(B\) and risk limits \(R\), because failures under \(b\) are recoverable and decision-relevant while failures under \(a\) are not. The inversion must occur on naturally occurring tasks and not be guaranteed by a hand-written reward or transition table.

## 10.3 Causal variable

The acceptable causal variable is not “feedback exists.” It is the interaction among:

- **reset fidelity** \((\epsilon_R,\delta_R)\),
- **cross-attempt retention** of failure-specific information,
- **local observability** of action-relevant differences from that information.

The target estimand is \(\Delta_{RMD}\) from Section 4.6, with tokens, verifier calls, environment calls, and elapsed time matched.

## 10.4 Intervention predicted to remove the effect

A genuine causal result would need all four interventions:

1. **Reset ablation:** restore neither environment nor context while preserving the total budget.
2. **Memory ablation:** restore state but erase all information from the failed suffix.
3. **Observability ablation:** retain a token- and format-matched signal that does not reveal payoff-relevant action differences.
4. **Alignment ablation:** rewind environment and context to mismatched checkpoints while preserving their individual content.

If only binary-feedback or shuffled-text controls hurt, the result is ordinary information removal, not a new law.

## 10.5 Why this would still need to differ from known frameworks

A surviving result must rule out the following explanations:

- **Ordinary long-horizon value:** the route wins because continuation value is larger.
- **Active learning/value of information:** the route wins because it yields more posterior information.
- **Safe exploration/recoverability:** the route wins because it avoids irreversible states.
- **Dual control:** the route wins because probing improves future control.
- **Rollback/checkpointing:** the route wins because retry cost is lower.
- **Distributional or budgeted RL:** the route wins because the objective includes remaining risk or attempts.
- **Partial monitoring:** the route wins because the feedback matrix is locally observable.

**[LITERATURE-SUPPORTED JUDGMENT]** Ruling out all seven is exactly why the residual is impractical. The seed’s intuitive force is largely the conjunction of these known explanations.

---

# 11. Falsifiable hypotheses for the last residual

These hypotheses make the termination falsifiable. They do **not** constitute authorization to run the project.

## H1 — Counterintuitive myopic-ranking inversion

**[HYPOTHESIS]** From the same first-failure branch point, a Continue policy has a higher probability of satisfying the next unmet evaluator criterion within the next 20 environment actions, yet an aligned-rewind-plus-memory policy has a higher final task-success probability under the same remaining budget.

This does not follow directly from a constructed reward: it is measured on unmodified public software tasks using the official evaluator. It is the minimum counterintuitive result needed.

## H2 — Three-way superadditivity

**[HYPOTHESIS]** The reset × cross-attempt-memory × diagnostic-feedback interaction \(\Delta_{RMD}\) is positive and at least 0.06 in absolute task-success probability, with a 95% task-cluster bootstrap lower bound above 0.03.

Pairwise additivity or a simple “memory helps” result falsifies the proposed law.

## H3 — Feedback topology beyond token count

**[HYPOTHESIS]** True ordered-criterion feedback outperforms length-, format-, and marginal-frequency-matched permuted feedback after controlling for total tokens and verifier calls, and the advantage is mediated by the ability to distinguish which repair branch will satisfy the next criterion.

This would still not prove information equivalence, but failure to obtain it kills B as a moderator.

## H4 — Alignment is causally necessary

**[HYPOTHESIS]** Rewinding the environment and agent context to different checkpoint indices removes at least 75% of the full aligned-rewind gain, despite preserving the same amount of environment state and text history.

AgentRewind already motivates this hypothesis; confirming it alone is replication.

## H5 — Reset fidelity has a sharp rather than linear effect

**[HYPOTHESIS]** There is a reproducible fidelity threshold: below a checkpoint mismatch rate of 0.5%, further fidelity improvements have little effect, whereas controlled mismatch above 2% collapses the memory benefit disproportionately.

A smooth proportional degradation is ordinary robustness behavior and not a new law.

## H6 — Failure-specific memory, not generic advice, drives recovery

**[HYPOTHESIS]** A deterministic failure-specific memory containing the failed criterion, relevant diff, and invalidated assumption outperforms a token-matched generic debugging memory by at least 6 absolute success points, while raw-transcript retention performs no better once context length is matched.

## H7 — Diagnostic saturation predicts when rewind stops helping

**[HYPOTHESIS]** A preregistered saturation statistic—the same first-unmet criterion after two matched rewinds with no reduction in the failing-test set—predicts negative marginal value of another rewind and supports a route switch better than a fixed retry count.

If the best threshold differs arbitrarily by task family or is selected post hoc, the claim reduces to tuning.

## H8 — Seed C negative control

**[HYPOTHESIS]** Any apparent shift toward “continue with a high-variance repair” as the rewind budget approaches zero is fully reproduced by a standard budget-augmented expected-utility or distributional baseline. A special desperation mechanism adds no predictive value.

Failure of this negative-control hypothesis would be surprising, but would still require replication outside software agents before reopening C.

---

# 12. Three-to-seven-day killer experiment

## 12.1 Status

> **[PROJECT DECISION] This is a last-chance falsification design, not a recommended run.**

Its purpose is to determine whether the sole residual interaction is empirically present. A positive first week would still not automatically constitute an ICLR contribution because the closest system and benchmark already exist.

## 12.2 Exact public stack

| Component | Selection | Reason |
|---|---|---|
| Primary benchmark | [MettleBench](https://github.com/Kelvin-Coffee/MettleBench), all 82 tasks, pinned to the repository commit used at launch | Natural long-horizon software tasks, public deterministic evaluators, ordered failure criteria, and direct comparability with AgentRewind. |
| Confirmatory benchmark, only after Day-4 GO | [Terminal-Bench 2.0](https://github.com/laude-institute/terminal-bench), 12 outcome-blind tasks that run without external credentials or uncontrolled network access | Tests whether the interaction is specific to MettleBench’s ordered criteria. |
| Agent harness | [mini-SWE-agent](https://github.com/mini-swe-agent/mini-swe-agent) plus the [AgentRewind recorder/replayer](https://github.com/Futuresis/replay-agent-recorder) | Public, lightweight relative to larger frameworks, and directly comparable to the closest prior work. |
| Primary model | [Qwen2.5-Coder-14B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-AWQ) | Official open-weight 4-bit model; one server fits on one 24 GB 4090 without model parallelism. |
| Scaling check | Official Qwen2.5-Coder 7B Instruct model or official quantization, on a preregistered 24-task subset | Tests whether the sign depends on one model scale. |
| Serving | vLLM or SGLang, one independent server per GPU | No pooled memory; task-level parallelism only. |
| Evaluator | MettleBench’s official criterion evaluator; Terminal-Bench’s official verifier | No learned reward model and no proprietary judge. |
| Training | None | Inference-only first week; no fine-tuning. |

All network access inside task containers must be disabled unless an official task requires a deterministic local service. Tasks requiring credentials or live external services are excluded by a rule frozen before outcomes are inspected.

## 12.3 Outcome-blind task protocol

1. Freeze benchmark, agent, model, evaluator, and container-image commits before the first scored run.
2. Run an evaluator-determinism audit three times per task from the untouched initial state.
3. Exclude a task only if the official evaluator disagrees across identical states or frozen dependencies cannot be installed. Log exclusions before viewing condition outcomes.
4. Use all remaining MettleBench tasks; do not select a “promising” subset after seeing results.
5. Randomize condition order within task and rotate conditions across GPUs to avoid hardware or thermal confounding.
6. Use two fixed decoding seeds by Day 4 and Day 7. Temperature, top-p, prompt, tool schema, token limits, and context truncation are identical across conditions.
7. Branch conditions from the same serialized first-failure checkpoint wherever technically possible, enabling paired within-task comparisons.

## 12.4 Nine preregistered recovery conditions

| ID | Environment after failure | Agent context after failure | Failure-specific memory | Feedback | Purpose |
|---|---|---|---|---|---|
| **C0 Continue** | Current failed state | Current context retained | None beyond raw context | True evaluator feedback | Strong no-rewind baseline. |
| **C1 Clean restart** | Initial task state | Initial prompt/context | None | Binary failure only | Independent-retry baseline. |
| **C2 Restart + experience** | Initial task state | Initial context | Deterministic failure memory | True feedback | Memory without local checkpoint preservation. |
| **C3 Environment-only rewind** | Last valid environment checkpoint | Current post-failure context | None | True feedback | Environment/context misalignment. |
| **C4 Context-only rewind** | Current failed environment | Last valid context checkpoint | None | True feedback | Complementary misalignment. |
| **C5 Aligned rewind, no memory** | Last valid environment checkpoint | Matching context checkpoint | None | Feedback erased after rewind | Pure reset effect. |
| **C6 Full aligned rewind** | Last valid environment checkpoint | Matching context checkpoint | Deterministic failure memory | True ordered-criterion feedback | Open-model AgentRewind-style treatment. |
| **C7 Full rewind + binary feedback** | As C6 | As C6 | Binary-failure memory of matched format | Pass/fail only | Diagnosability ablation. |
| **C8 Full rewind + permuted feedback** | As C6 | As C6 | Token-/format-matched criterion-permuted memory | Fixed within-task permutation | Destroys action relevance while preserving superficial statistics. |

The deterministic memory is generated without an extra LLM call from a fixed template containing the first unmet criterion, failing verifier output, files changed since checkpoint, and last action. C6 therefore receives no hidden inference-compute advantage.

## 12.5 Paired route-ranking test

At the first evaluator-detected failure after a valid checkpoint, fork two branches with identical remaining budgets:

- **Myopic branch:** C0 Continue.
- **Recoverable branch:** C6 Full aligned rewind.

Define immediate post-failure progress

\[
q_{20}(\pi)=\Pr(\text{first unmet criterion is satisfied within 20 further environment actions}\mid \pi).
\]

Define fixed-budget final success

\[
S_B(\pi)=\Pr(\text{all official criteria pass before the common token/action/verifier budget is exhausted}\mid \pi).
\]

A qualifying inversion is

\[
q_{20}(\text{Continue}) > q_{20}(\text{Rewind})
\quad\text{and}\quad
S_B(\text{Continue}) < S_B(\text{Rewind}).
\]

The first inequality makes the result counterintuitive: rewind sacrifices near-term criterion progress rather than dominating at every horizon.

## 12.6 Fixed per-episode budget

### Qwen2.5-Coder-14B-AWQ

- Maximum generated tokens: **24,000**.
- Maximum cumulative prompt/prefill tokens: **96,000**.
- Maximum environment/tool actions: **120**.
- Maximum official verifier calls: **8**.
- Maximum rewind operations: **4**.
- Maximum wall-clock time: **75 minutes**.
- Fixed decoding parameters; no best-of-\(n\) sampling.

### 7B scaling check

- Maximum generated tokens: **16,000**.
- Maximum cumulative prompt/prefill tokens: **64,000**.
- Maximum environment/tool actions: **90**.
- Maximum verifier calls: **6**.
- Maximum rewind operations: **3**.
- Maximum wall-clock time: **50 minutes**.

A condition exceeding a cap is scored as a budget failure. Unused budget is not transferred between tasks.

## 12.7 Strong baselines

1. Continue (C0).
2. Clean restart (C1).
3. Restart with retained experience (C2).
4. Environment-only rewind (C3).
5. Context-only rewind (C4).
6. Aligned rewind without memory (C5).
7. Full aligned rewind with memory (C6).
8. Full rewind with outcome-only feedback (C7).
9. Full rewind with superficially matched but action-irrelevant feedback (C8).
10. A **budget-aware oracle selector**, evaluated offline: at each logged branch point, choose Continue or Rewind using cross-validated estimates from other tasks only.
11. A **myopic selector** choosing the branch with higher predicted \(q_{20}\).
12. A **budget-augmented logistic policy** using remaining tokens, actions, rewinds, criterion index, and prior failures; this is the Seed C negative-control baseline.

No baseline may receive a different model, longer context, more verifier calls, or more generated tokens.

## 12.8 Metrics

### Primary metrics

1. **Official full-task success rate** under the fixed budget.
2. **Three-way interaction \(\Delta_{RMD}\)** estimated from preregistered contrasts, with task-cluster bootstrap intervals.
3. **Paired route-ranking inversion rate** among eligible branch points.
4. **Success per million generated tokens** and **success per 100 GPU-hours**.

### Secondary metrics

- Ordered-criterion completion fraction.
- Area under criterion-progress versus token curve.
- Recovery probability after first failure.
- Reset-state mismatch rate.
- Verifier calls, environment calls, prompt tokens, generated tokens, GPU-seconds, and wall-clock seconds.
- Marginal value of rewind number 1, 2, 3, and 4.
- Repeated failure on the same criterion.
- Calibration of Continue-versus-Rewind selectors.

### Statistical analysis

- Paired task-level differences whenever branches share a checkpoint.
- Hierarchical logistic regression with task random intercepts and fixed reset, memory, diagnosticity, and interaction effects.
- Nonparametric task-cluster bootstrap for headline confidence intervals.
- Exact paired permutation tests for Day-2 samples.
- Holm correction across the eight preregistered hypotheses.
- No task-level cherry-picking and no post-hoc seed removal.

---

# 13. Compute ledger on exactly 8×RTX 4090

## 13.1 Hardware topology

- Eight independent GPU workers.
- One model server and one agent worker per GPU.
- No tensor parallelism, no pipeline parallelism, no NVLink assumption, and no cross-GPU KV cache.
- A CPU-side queue dispatches independent task-condition episodes.
- Container snapshots and evaluators run on local CPU/storage; their time is included in wall-clock accounting.

## 13.2 Stage ledger

The ledger uses conservative throughput assumptions for a 14B 4-bit coder model: **18–25 generated tokens/s per GPU** after accounting for variable context lengths. The “total GPU-hours” column includes a 1.6–1.8× allowance for prefills, tool pauses, evaluator synchronization, and under-filled batches.

| Stage | Workload | Episodes | Output-token cap | Verifier-call cap | Environment-call cap | Conservative total GPU-hours | Eight-GPU wall-clock |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Day 2 screen** | 18 tasks × 9 conditions × 1 seed | 162 | 2.916 M | 972 | 14,580 | 70–85 h | 9–12 h plus setup |
| **Day 4 test** | 36 tasks × 9 conditions × 2 seeds | 648 | 12.960 M | 4,536 | 68,040 | 280–340 h | 35–43 h cumulative |
| **Day 7 main** | 82 tasks × 9 conditions × 2 seeds | 1,476 | 35.424 M | 11,808 | 177,120 | 820–900 h | 103–113 h cumulative |
| **7B scaling check** | 24 tasks × 9 conditions × 2 seeds | 432 | 6.912 M | 2,592 | 38,880 | 70–90 h | 9–12 h, interleaved late in week |
| **Optional 12-task Terminal-Bench confirmation** | 12 tasks × 9 conditions × 1 seed | 108 | 1.944–2.592 M | ≤864 | ≤12,960 | 45–65 h | 6–9 h, only after Day-4 GO |

### Full-week upper bound

- **Generated tokens:** approximately 42.34 M without Terminal-Bench; at most 44.93 M with it.
- **Cumulative prompt/prefill tokens:** capped at approximately 169 M for the 14B and 7B runs combined.
- **Token-level decoding forward steps:** approximately equal to generated-token count, 42–45 M; exact fused-kernel invocation count is implementation-dependent and must be logged rather than inferred.
- **Verifier calls:** at most 14,400 without Terminal-Bench; 15,264 with it.
- **Environment/tool calls:** at most 216,000 without Terminal-Bench; 228,960 with it.
- **Training examples:** **0** for the agent model; only logged evaluation episodes are used for offline statistical models.
- **GPU-seconds:** approximately 3.2–3.8 million without Terminal-Bench; up to 4.0 million with it.
- **Total wall-clock:** approximately 5.0–6.5 days including environment build, evaluator audit, failed-container retries, and final analysis, provided all eight GPUs remain continuously available.

## 13.3 Honest feasibility caveats

- Long prompts and repository I/O can reduce throughput below the nominal AWQ rate.
- Some tasks may hit the 75-minute wall cap before token caps.
- Docker snapshot performance depends strongly on storage; NVMe is assumed, not network storage.
- A cold environment-build failure can consume half a day. Images should be built once and frozen.
- No training is budgeted. Any proposal to fine-tune a route selector during the first week violates the protocol.
- Running the original AgentRewind proprietary-model configuration is outside the stated resource assumptions; this audit therefore proposes an open-model replication, which further weakens novelty.

---

# 14. Causal ablations

## 14.1 Reset

1. **None:** C0 Continue.
2. **Initial restart:** C1/C2.
3. **Environment-only:** C3.
4. **Context-only:** C4.
5. **Aligned checkpoint reset:** C5/C6.
6. **Controlled fidelity degradation:** leave a preregistered class of nonessential cache/process metadata unrestored, producing measured mismatch bands of 0–0.5%, 0.5–2%, and >2%.

Every reset must record:

- recursive workspace content hash;
- Git status and file metadata;
- process table and open local ports;
- environment variables and working directory;
- container/image identifier;
- checkpoint index for environment and context;
- evaluator result immediately before and after restoration.

No claim of exact reset is permitted if an evaluator-relevant state component is outside the boundary.

## 14.2 Feedback retention

- **Raw retained trace:** post-failure context remains visible, as in Continue.
- **Erased trace:** context rewinds and no failure information survives.
- **Compressed deterministic trace:** only the fixed memory template survives.
- **Token-matched generic trace:** same length and formatting but generic debugging advice.

This separates “the model saw more text” from failure-specific retention.

## 14.3 Cross-attempt memory

- No memory.
- Deterministic failure memory.
- Memory from the wrong task, length-matched and drawn from the same benchmark stratum.
- Memory with correct criterion but permuted file/diff references.
- Raw transcript truncated to the same token count as deterministic memory.

The wrong-task and permuted-reference controls test whether gains come from generic self-critique tone rather than task-specific epistemic progress.

## 14.4 Diagnosability

- True first-unsatisfied criterion and verifier output.
- Binary pass/fail only.
- Fixed within-task permutation of criterion labels/text.
- Already-satisfied criterion substituted for the failed one.
- Same feedback delayed until after one additional action, testing whether timing matters.

A post-hoc classifier may be trained on logged branches to predict which candidate repair action satisfies the next criterion. Its cross-validated accuracy is a *diagnostic measure*, not a learned policy. The proposed B mechanism is supported only if this action-discriminability mediates the rewind gain better than token length, lexical entropy, or raw verifier-output size.

## 14.5 Saturation

Preregister saturation as:

\[
\sigma_t = \mathbf 1\{c_t=c_{t-1}=c_{t-2}\}
\cdot \mathbf 1\{F_t=F_{t-1}=F_{t-2}\},
\]

where \(c_t\) is the first unsatisfied criterion and \(F_t\) is the set of failing verifier checks after rewind \(t\). Compare:

- fixed maximum of four rewinds;
- stop after one rewind;
- stop at \(\sigma_t=1\);
- a cross-validated budget-aware selector.

A tuned threshold selected after seeing all tasks is not evidence.

## 14.6 Risk budget

Use remaining rewind allowance \(K_t\in\{0,1,2,3,4\}\) as an observed budget state. Compare Continue versus Rewind choices using:

- expected final success;
- a distributional outcome model over fail/partial/full success;
- the budget-augmented logistic baseline;
- a deliberately “desperation-seeking” heuristic that chooses the higher empirical variance branch at \(K_t=0\).

Seed C is reopened only if the desperation heuristic predicts behavior or outcomes beyond the ordinary budget-aware distributional baseline on held-out tasks. The expected result is that it does not.

## 14.7 Cost matching

For every paired comparison, report absolute and relative differences in:

- generated tokens;
- prompt tokens;
- model calls;
- verifier calls;
- environment actions;
- snapshot/restore time;
- GPU-seconds;
- end-to-end wall-clock time.

A headline comparison is invalid if any resource differs by more than **3%** after censoring at common caps. Results may still be reported descriptively, but they cannot support a causal claim.

---

# 15. Numerical GO, NO-GO, and ambiguous-result gates

These thresholds are intentionally severe because the closest prior art is direct. Passing a gate authorizes only the next stage, not a paper claim.

## 15.1 Day 2 gate — engineering and sign screen

**Dataset:** 18 outcome-blind MettleBench tasks, all nine conditions, one fixed decoding seed.

### GO to Day 4 only if all hold

1. C6 Full aligned rewind is the best preregistered condition on official fixed-budget success.
2. C6 exceeds both C0 Continue and C5 Aligned-no-memory by at least **11.1 absolute percentage points**—at least two additional successes among 18 tasks.
3. The point estimate of the reset × memory × diagnosticity interaction is at least **0.10**.
4. At least **3 tasks** exhibit the H1 near-term/final ranking inversion.
5. Reset mismatch is below **1%** of audited checkpoint components.
6. Median generated-token and wall-clock differences between C6 and its paired baselines are within **3%**.

### NO-GO immediately if any hold

- C6 is not the best condition.
- C6 improves by at most one task over C0 or C5.
- The interaction point estimate is ≤0.03 or negative.
- No qualifying ranking inversion appears.
- More than 10% of tasks fail evaluator determinism or checkpoint restoration.
- Cost matching fails by >5%.

### Ambiguous

Any result between these thresholds. The only permitted response is to diagnose implementation failures on the same 18 tasks; do not add tasks, tune prompts, or alter hypotheses.

## 15.2 Day 4 gate — causal interaction screen

**Dataset:** 36 tasks × 9 conditions × 2 fixed seeds, paired wherever possible.

### GO to full Day 7 only if all hold

1. C6 exceeds the strongest non-full baseline by **≥8 absolute points** in fixed-budget success.
2. The task-cluster bootstrap lower bound for that difference is **>0** at 95% confidence.
3. \(\widehat\Delta_{RMD}\ge0.06\), with a one-sided 90% lower bound above 0.
4. At least **15%** of eligible branch points exhibit H1 ranking inversion, on at least **8 distinct tasks**.
5. Environment-only and context-only rewinds each lose at least **50%** of the C6-over-C0 gain.
6. Failure-specific memory beats token-matched generic memory by **≥5 points**.
7. The full effect remains after common-budget censoring and per-task pairing.
8. No single benchmark source family contributes more than 60% of the aggregate gain.

### NO-GO if any hold

- C6’s advantage is <4 points.
- The interaction is <0.03 or its bootstrap distribution is centered at zero.
- Gains are fully explained by more tokens, more verifier calls, or longer wall-clock.
- True feedback only beats binary/permuted feedback, with no reset-memory interaction.
- All inversions occur in one task source or one decoding seed.
- The reset boundary cannot be audited to <1% mismatch.

### Ambiguous

A 4–8 point gain, a positive point interaction with interval crossing zero, or inversion concentrated in one task family. Ambiguous results do **not** justify a 30-day program; they justify a terminal report.

## 15.3 Day 7 gate — scientific survival gate

**Dataset:** all valid MettleBench tasks × 9 conditions × 2 seeds, plus the 7B scaling subset. Terminal-Bench confirmation is allowed only if Day-4 GO was reached with time remaining.

### Scientific GO only if every criterion holds

1. **Effect size:** C6 beats the strongest cost-matched baseline by **≥8 absolute success points**, with a 95% task-cluster lower bound of **≥3 points**.
2. **Interaction:** \(\widehat\Delta_{RMD}\ge0.06\), with a 95% lower bound of **≥0.03**.
3. **Ranking inversion:** at least **20%** of eligible first-failure branch points and at least **20 distinct tasks** show H1; the inversion has the same sign in both model scales.
4. **Scale replication:** the 7B estimate has the same sign and at least **50%** of the 14B interaction magnitude.
5. **Alignment:** mismatched environment/context checkpoints remove at least **75%** of the full benefit.
6. **Specificity:** failure-specific memory beats both generic and wrong-task memory by **≥6 points**.
7. **Budget integrity:** every headline contrast is within **3%** for generated tokens, verifier calls, environment calls, and GPU-seconds.
8. **Reset integrity:** audited checkpoint mismatch is **≤0.5%**, with no evaluator-relevant mismatch.
9. **Beyond trivial information removal:** action-discriminability mediates the effect after controlling for feedback length and lexical entropy, and the interaction remains after excluding tasks whose official feedback explicitly names the required edit.
10. **Not Seed C in disguise:** a budget-aware distributional selector reproduces any risk-budget switch; no special desperation component is needed.
11. **External confirmation:** on the optional Terminal-Bench subset, the C6-over-best-baseline effect has the same sign and is at least **4 points**, or the project remains domain-specific and fails the gate.

### Day 7 NO-GO

Failure of **any** scientific-GO criterion. Because the direct collision is so strong, there is no “mostly passed” path to a 30-day program.

### Day 7 ambiguous

There is no binding ambiguous extension at Day 7. A suggestive but incomplete result is archived as a negative/replication report; it does not receive more compute.

---

# 16. Conditional 30-day plan

This plan is **inactive**. It may be activated only if every Day-7 scientific-GO criterion is met and a fresh literature search confirms that no post-audit paper has closed the residual.

## Days 8–11 — independent-domain replication

- Run the full core comparison on at least 40 tasks from a second public domain with a deterministic evaluator.
- Preferred order: Terminal-Bench 2.0, then formal theorem proving only if a clean state-checkpoint interface can be frozen.
- Use the same model and budget caps before changing architecture.
- Gate: same-sign interaction, ≥4-point full-system advantage, and at least 10 natural ranking inversions.

## Days 12–15 — information-control audit

- Construct feedback controls preserving length, syntax, marginal criterion frequency, and verifier-output size.
- Estimate action-discriminability, conditional mutual information proxies, and expected Bayes-regret reduction from logged branches.
- Compare the proposed diagnosticity predictor against information ratio, entropy, feedback length, criterion index, and task difficulty.
- Gate: local observability proxy must explain held-out recovery benefit materially better than all simpler proxies.

## Days 16–19 — theory or impossibility result

Pursue one, not both:

1. **Positive theorem route:** identify a restricted partial-monitoring-with-reset model in which the three-way interaction changes the regret or sample-complexity class, rather than only constants.
2. **Impossibility route:** prove that under sufficient belief state and exact reset, the mechanism reduces to a standard Bayes-adaptive process; then position the empirical result as a representation failure of practical agents.

A theorem that merely writes the augmented state is insufficient.

## Days 20–23 — useful intervention

Develop the smallest intervention supported by the mechanism:

- checkpoint selection based on predicted action-discriminability, not generic uncertainty;
- memory compression retaining counterfactual action distinctions;
- saturation-triggered switch using the preregistered statistic.

Compare with AgentRewind, Continue, restart-with-experience, an information-gain selector, and a budget-aware route selector. The intervention must improve success at fixed cost on both domains.

## Days 24–26 — robustness and negative controls

- Two model families or, minimally, two scales and two decoding regimes.
- Three seeds on the main subset.
- Strict reset-boundary audit.
- Cost curves rather than a single budget.
- Remove tasks whose evaluator directly states the patch.
- Test whether a learned selector trained on one source family transfers to another.

## Days 27–30 — paper assembly and hostile internal review

- Release code, frozen task manifests, container digests, raw traces, and per-task costs.
- Write the paper around one causal law, not the billiards metaphor.
- Include AgentRewind as the closest baseline in the abstract/introduction, not buried in related work.
- Run an internal rejection review using Section 17.
- Stop if the contribution is still “rewind plus informative memory works better.”

### Thirty-day resource ceiling

- No more than **2,500 additional GPU-hours** on the same eight 4090s.
- No frontier-model API dependence for headline results.
- No new benchmark whose reward or feedback matrix is engineered after observing first-week outcomes.
- No physical-robot claims.

---

# 17. Strongest skeptical ICLR rejection

## 17.1 Rejection paragraph

> This paper repackages known ingredients—checkpoint rollback, retained failure summaries, execution feedback, and feedback observability—without establishing a new learning principle. AgentRewind already rewinds aligned environment and agent context and ablates retained rewind memory on the same style of software tasks; partial-monitoring and dual-control theory already explain why action-relevant feedback makes retries useful. The reported factorial gains therefore show only that removing state restoration or useful information hurts. MettleBench’s ordered first-unsatisfied criterion is unusually diagnostic and may manufacture the effect, while the proposed “ranking inversion” is an ordinary horizon/continuation-value phenomenon. The paper neither matches decision-relevant information across feedback conditions nor demonstrates a regret-class change, a failure of a strong Bayes-adaptive/information-directed baseline, or transfer beyond checkpointable software environments. The intervention is consequently an AgentRewind variant and benchmark-specific routing heuristic, not an ICLR-level scientific contribution.

## 17.2 Evidence required to defeat that rejection

Every item below is necessary:

1. **Direct-head-to-head comparison with AgentRewind** under the same open model, prompt, task, budget, and evaluator.
2. **A natural ranking inversion** between immediate progress and final success on at least two independent public domains.
3. **A genuine three-way interaction**, not pairwise benefits from reset and information.
4. **Information-structure controls** that preserve superficial statistics and establish that action-relevant observability—not feedback quantity—mediates the effect.
5. **Strong explanatory baselines:** Bayes-adaptive/value-of-information, information-directed, budget-aware, and distributional route selectors.
6. **A practically useful intervention** that improves fixed-cost success beyond AgentRewind on both domains.
7. **Reset-boundary correctness** with state hashes and semantic side-effect auditing.
8. **A theorem or empirical invariant** that is more than an augmented-state restatement and survives task/model changes.
9. **Full cost curves** over tokens, verifier calls, environment actions, GPU-seconds, and wall-clock.
10. **Open reproducibility:** model weights, code, frozen images, task manifests, traces, and evaluator versions.

Without all ten, the strongest reviewer attack stands.

---

# 18. Calibrated probability assessment

The probabilities below are conditional on running the one-week falsification protocol competently. They concern the current framing, not the general value of rollback systems.

| Outcome | Probability | 80% subjective interval | Rationale |
|---|---:|---:|---|
| Produce a positive **synthetic or benchmark-conditioned effect** | **0.86** | 0.73–0.94 | True diagnostic feedback, aligned reset, and task-specific memory should outperform ablations on a benchmark designed around ordered criteria. |
| Transfer the full interaction to **natural public tasks outside MettleBench** | **0.23** | 0.11–0.39 | Reset semantics and feedback structure vary sharply; software benchmarks are unusually checkpointable. |
| Produce a result that is **scientifically distinct from AgentRewind and partial monitoring** | **0.09** | 0.03–0.18 | The residual requires information-controlled superadditivity, not ordinary component gains. |
| Reach **ICLR main-track quality** in the current project cluster | **0.035** | 0.010–0.080 | Direct 2026 collision, no preliminary signal, and difficult natural-domain transfer. |
| Reach **ICLR Oral-level quality** | **0.003** | 0.0005–0.010 | Oral-level work would require a surprising law, theory, broad transfer, and a useful intervention—all currently unsupported. |

## 18.1 Interpretation

- The high probability of “an effect” is not encouraging. It is exactly why the project is dangerous: an expected benchmark gain can consume a month while leaving novelty unchanged.
- The key bottleneck is not compute or implementation. It is scientific subtraction after AgentRewind, partial monitoring, dual control, and budget-aware planning.
- A negative first-week result would be decisive. A positive result would still face a much harder novelty gate.

---

# 19. Binding cluster decision

## 19.1 Final classification

- **Seed A:** NO-GO as an independent paper.
- **Seed B:** useful explanatory language inside A, but independently NO-GO.
- **Seed C:** independently NO-GO.
- **Merged A+B+C paper:** NO-GO.
- **Primary direction:** none.
- **Fallback direction:** none.

## 19.2 Final instruction

> # **DO NOT RUN**

Do not allocate the eight-GPU cluster to this research family. Do not begin the proposed one-week experiment merely because it is executable. Do not relabel an AgentRewind replication as a new principle, and do not manufacture an information-matched toy benchmark to preserve the idea.

The cluster should be redirected to a different seed whose novelty survives primary-source subtraction *before* implementation. The falsification protocol in this document should be retained only as a future audit template if genuinely new evidence or a new natural carrier appears.
