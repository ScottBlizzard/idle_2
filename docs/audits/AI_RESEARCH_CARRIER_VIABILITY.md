# AI_RESEARCH_CARRIER_VIABILITY.md

**Research cutoff:** 25 August 2026  
**Target venue:** ICLR  
**Hardware constraint:** 8× NVIDIA RTX 4090; GPU-only; no physical robotics  
**Executive verdict:** **NO-GO**  
**Repository status:** Historical adversarial audit; retained as a binding negative result.

---

## 0. Executive verdict

### 0.1 Decision

**Do not launch “Post-Success Carrier Viability” as a new umbrella research direction or as the central claim of an ICLR submission.**

The motivating distinction is real: a system can finish the current task while leaving persistent state that makes later tasks harder. The problem is not importance; it is residual novelty. At the level of formal decision theory, the proposed objective is already expressible as one or more of:

- a terminal continuation value over future tasks;
- a constrained Markov decision process;
- a viability-kernel or reachability constraint;
- impact regularization or attainable-utility preservation;
- empowerment or retained-option preservation;
- risk-sensitive or multi-objective control;
- continual-learning retention when the persistent state is model parameters;
- stateful planning, transactional execution, or rollback when the persistent state is an external workspace.

The most damaging collision is not merely thematic. Krakovna et al. explicitly define side effects through an agent’s **ability to perform future tasks**, while attainable-utility preservation and empowerment preserve future achievable utility or controllability. citeturn135493search0turn135493search1turn135493search3 In 2026, the two empirically cleanest instantiations—persistent LLM memory and sequential code maintenance—became crowded with work on locally correct but harmful memories, longitudinal contamination, persistent carriers, matched persistence-on/off evaluations, transactional memory, rollback, future-edit correctness, chained software evolution, and code that passes current tests but becomes harder to extend. citeturn290956search0turn290956search1turn290956search2turn290956search3turn917474search0turn917474search2turn917474search3turn776223search5turn776223search8

The billiards motivation contributes intuition but **no independent scientific content**. It should not appear in a paper title, method name, formal claim, or novelty argument.

### 0.2 What, if anything, survives

The narrowest residual question I could not fully eliminate is:

> **With the user-visible current output held exactly fixed, can a post-output commit to an independently restorable persistent memory cause broad future-task degradation; can a cheap predictor identify that degradation better than a compute-matched continuation-value model and generic state-change measures; and does selective carrier rollback restore the lost capability?**

This is not a new theory of agency. It is a **causal evaluation protocol for persistent memory commits**. Even this residual is under heavy pressure from 2026 work: OEP studies locally correct but non-transferable experiences; *Remembering More, Risking More* uses fixed future probes and a no-memory counterfactual; PAST-Bench uses matched persistence-on/off episodes; ACL 2026 work measures error propagation and misaligned replay from seemingly correct experiences; MemTX and ChronoMem already provide commit discipline and rollback. citeturn290956search1turn290956search2turn290956search3turn917474search0turn917474search2turn917474search3

Accordingly, the residual deserves only a **strictly capped falsification audit**, not a 30-day project commitment:

| Decision item | Binding recommendation |
|---|---|
| Full 8×4090 allocation | **Reject** |
| New architecture before phenomenon test | **Reject** |
| Three-day pilot | **Allow**, using 2 GPUs and at most 150–200 GPU-hours |
| Full 3–7 day follow-up | Only if every pilot threshold in Section 17 is met |
| Working title if it survives | **Causal Externalities of Post-Output Memory Commits** |
| “Carrier viability” as claimed novelty | **Do not use** |
| Cross-domain paper now | **Reject as over-scoped** |

### 0.3 Why the verdict is not “PIVOT”

A pivot would imply that a positive project direction has already survived. It has not. The proposed pilot is an **audit whose default outcome is termination**. A positive pilot would justify reopening the decision, not retroactively make the current seed novel.

---

## 1. Non-metaphorical statement of the problem

An agent handles a current task and may modify persistent internal or external state while doing so. A current-task evaluator observes only a projection of the resulting system state—often a final answer, a test result, a solved issue, or a verified proof. Multiple trajectories can therefore receive the same current score while leaving different persistent states. Those states can change the probability, cost, or feasible action set for later tasks.

The scientifically meaningful problem is not “success can have side effects.” It is the following controlled identification problem:

> Given trajectories that are matched on current output, current verifier result, policy family, and compute, estimate the causal effect of the post-task persistent state on performance over a pre-registered distribution of future tasks.

A publishable study must separately establish:

1. **Present equivalence:** the current output and current-task quality are genuinely matched.
2. **Persistent-state difference:** a typed, snapshot-able state component differs after the current task.
3. **Future effect:** future-task performance differs under fixed policies and budgets.
4. **Mediation:** restoring or swapping the identified state component removes or transfers the effect.
5. **Non-trivial prediction:** the effect is not already captured by a fair continuation-value critic, generic state distance, task reward, memory size, or simple no-op policy.

Without all five, the result is ordinary long-horizon evaluation, confounded current quality, generic side-effect avoidance, or a repackaging of an established retention metric.

---

## 2. State ontology and precise definitions

### 2.1 Full state and dynamics

Let the complete Markov state be

\[
s_t = (x_t,c_t,e_t,z_t),
\]

where:

- \(x_t\) is the **current-task state**;
- \(c_t\) is the **capability-carrying state**;
- \(e_t\) is the **persistent external environment state**;
- \(z_t\) contains any additional latent variables required to make the process Markov.

Actions induce

\[
(x_{t+1},c_{t+1},e_{t+1},z_{t+1})
\sim P(\cdot\mid x_t,c_t,e_t,z_t,a_t).
\]

The user-visible output is

\[
y_T = O(x_T,c_T,e_T,z_T,\tau),
\]

where \(\tau\) is the recorded trajectory. In a well-specified Markov model, any history dependence that matters for the future must be represented in the endpoint state; the explicit \(\tau\) argument is needed only when the practical state representation is incomplete or when evaluation itself inspects process compliance.

### 2.2 Current-task state \(x\)

A variable belongs in \(x\) when it is primarily part of solving the presently active task and is normally discarded or reset afterward.

Examples:

- the open subgoals in a single Lean proof;
- an LLM’s active chain of thought or search tree for one problem;
- a temporary browser page used only for the current request;
- the current issue specification and local execution trace;
- a volatile context window or KV cache that will not be reused across tasks.

**Important exclusion:** a proof state or test-time reasoning prefix is usually not a capability carrier. It is the search state of the current problem. Ranking proof states by future solvability is precisely value estimation or proof search.

### 2.3 Capability-carrying state \(c\)

A component qualifies as \(c\) only if it satisfies all four criteria:

1. **Persistence:** it survives into independent future tasks or sessions.
2. **Policy relevance:** changing it can change the agent’s future action distribution, available operators, or effective competence.
3. **Independent intervention:** it can be snapshotted, restored, swapped, or selectively modified without necessarily changing the already-issued current output.
4. **Typed boundary:** the experiment can specify exactly what is inside and outside the component.

Clean examples:

- model parameters after an edit or continual-learning update;
- a persistent episodic, semantic, procedural, or skill memory;
- a persistent system prompt, runbook, or instruction file reused by later tasks;
- a learned skill library or tool-selection policy;
- a persistent credential, permission, or tool registry that changes available actions.

Ambiguous or invalid examples:

- “the agent’s capability” without a concrete state representation;
- an ephemeral reasoning trace that is deleted after the task;
- a repository modified by the agent, which is normally part of \(e\), not agent-side \(c\);
- the current proof state, which is normally \(x\);
- future performance itself, which is an outcome, not a state.

### 2.4 Persistent environment state \(e\)

The environment is external state that persists independently of the agent’s internal policy substrate:

- repository files, tests, dependency manifests, and build configuration;
- a filesystem, database, CRM, calendar, email account, or web application;
- external tool state, API-side resources, tickets, cloud resources, or permissions;
- shared artifacts used by multiple agents.

This distinction matters. If a coding agent leaves a bad patch, the immediate scientific object is **persistent environment modification and future maintainability**, not damage to an internal carrier. Calling the repository a “carrier” does not create novelty.

### 2.5 Current success and output quality

Let

\[
S_{\mathrm{cur}}(\tau)\in\{0,1\}
\]

be current-task success under an exact or highly reliable verifier, and let

\[
Q_{\mathrm{out}}(y_T)\in\mathbb{R}
\]

measure final output quality.

A matched-success comparison requires more than \(S_{\mathrm{cur}}=1\). The strongest design fixes the exact visible output string or exact patch behavior and additionally matches all available current-task tests, latency, token budget, tool calls, and stochastic decoding policy.

### 2.6 Future-task distribution and capability

Let \(q\sim\mathcal D_F\) be a future task sampled from a pre-registered distribution, and let \(B\) be a fixed execution budget. For a fixed future policy \(\pi\), define

\[
\Phi_{\mathcal D_F,B}^{\pi}(c,e)
=
\mathbb E_{q\sim\mathcal D_F,\,\omega}
\left[
\operatorname{Success}(q\mid c,e,\pi,B,\omega)
\right].
\]

This is the **future-task capability score**. It is measured independently from current reward.

A retained-option variant is

\[
\mathcal R_{B,\alpha}(c,e)
=
\left\{
q:\Pr[\operatorname{Success}(q\mid c,e,\pi,B)]\ge \alpha
\right\},
\]

with option mass

\[
\Omega_{B,\alpha}(c,e)
=
\Pr_{q\sim\mathcal D_F}[q\in\mathcal R_{B,\alpha}(c,e)].
\]

### 2.7 Degradation and viability

Relative to a pre-registered reference state \((c^{\mathrm{ref}},e^{\mathrm{ref}})\), define

\[
\Delta\Phi
=
\Phi(c^{\mathrm{ref}},e^{\mathrm{ref}})
-
\Phi(c_T,e_T).
\]

The state is viable at threshold \(\theta\) when

\[
\Phi(c_T,e_T)\ge \theta.
\]

A binary oracle label estimated from \(m\) fixed future probes is

\[
L_{\mathrm{oracle}}(c,e)
=
\mathbb 1\left[
\frac{1}{m}\sum_{i=1}^{m}S_i(c,e)\ge \theta
\right].
\]

The oracle label is expensive because it requires replaying future tasks. The proposed model target would be either \(\widehat\Phi(c,e)\) or \(\widehat L(c,e)\) from the post-task state and trace without running all probes.

### 2.8 Collision event

A **collision-like event** is not ordinary gradual degradation. For two interventions \(u,u'\), define it by four simultaneous conditions:

\[
d(u,u')\le \varepsilon,
\]

\[
y_T(u)=y_T(u'),\qquad S_{\mathrm{cur}}(u)=S_{\mathrm{cur}}(u')=1,
\]

\[
d_s(s_T(u),s_T(u'))\le \eta,
\]

but

\[
\left|\Phi(s_T(u))-\Phi(s_T(u'))\right|\ge \kappa.
\]

Here \(d\) and \(d_s\) must be declared before seeing results. A useful empirical standard is \(\kappa\ge 0.20\) absolute future-success difference for a perturbation in the lowest decile of the chosen semantic/state-distance distribution.

A top-\(k\) retrieval boundary can produce discontinuity in observed behavior, but that fact alone is not surprising. The scientific burden is to show a broad reachable-task collapse, current-output equivalence, causal recovery, and failure of matched baselines.

### 2.9 Reversibility and recoverability

Let \(I\) be an intervention that changes selected state components after current output has been committed. Define restoration cost

\[
\rho(s\rightarrow s^{\mathrm{ref}};y_T)
=
\min_{I}
\operatorname{Cost}(I)
\quad\text{s.t.}\quad
I(s)\equiv s^{\mathrm{ref}}
\text{ on selected components, and }y_T\text{ remains valid}.
\]

- **Reversible:** exact restoration is possible.
- **Recoverable:** an acceptable viable state can be reached, even if exact restoration is impossible.
- **Irreversible:** no allowed intervention restores viability within budget.

Rollback is primarily a **causal instrument** in this investigation. It is not itself novel; reset-free RL, reversibility-aware RL, memory versioning, and transactional agent systems already study it. citeturn653492search2turn653492search3turn917474search2turn917474search3

### 2.10 Essential distinctions

| Quantity | What it asks | Independent measurement required? | Typical confound |
|---|---|---:|---|
| Current task success | Did the present task pass? | Yes | Weak or incomplete verifier |
| Final output quality | How good is the delivered answer/patch? | Yes | Treating binary pass as equivalence |
| Final carrier quality | Is persistent agent-side state healthy? | Yes | Vague carrier boundary |
| Final environment quality | Is the workspace/world healthy? | Yes | Calling all state “memory” |
| Full-trajectory side effects | Did intermediate actions violate process constraints or alter hidden state? | Yes | Missing endpoint variables |
| Reversibility | Can the relevant change be undone? | Yes | Confusing undo cost with capability |
| Future capability | How well can later tasks be solved? | Yes | Reusing current reward |
| Generic long-horizon value | Expected future return under a task process | Baseline, not new metric | Different task distribution or compute |
| Catastrophic forgetting | Did a parameter update erase prior skills? | Yes | External-memory effects |
| Memory contamination | Did stored/retrieved state induce later errors? | Yes | Context length or retrieval recall |
| Maintainability | Can later changes be implemented correctly and efficiently? | Yes | Subjective static metrics |
| Generic state change | How much did the state move? | Baseline only | Large benign changes; small catastrophic changes |

---

## 3. Why present success and post-success viability can diverge

### 3.1 Many-to-one evaluation

A current evaluator usually observes a projection

\[
E_{\mathrm{cur}}:s_T\mapsto (y_T,S_{\mathrm{cur}},Q_{\mathrm{out}}).
\]

If \(E_{\mathrm{cur}}\) is many-to-one, then two distinct complete states can receive identical current scores:

\[
E_{\mathrm{cur}}(s_T)=E_{\mathrm{cur}}(s'_T)
\quad\text{while}\quad
\Phi(s_T)\ne\Phi(s'_T).
\]

This is the entire non-metaphorical core. The phenomenon is plausible whenever the current verifier ignores persistent memory, dependencies, permissions, latent tool state, code structure, or model parameters.

### 3.2 Full-endpoint equivalence proposition

**Proposition.** If two trajectories end in the same complete Markov state, face the same future-task distribution, use the same future policy and compute budget, and share the same exogenous randomness distribution, then they have identical future capability.

**Consequence.** “Endpoint-equivalent trajectories with different future viability” is impossible when endpoint equivalence means equality of the **complete** state. Any claimed trajectory-only effect implies at least one of:

1. the logged endpoint omits a persistent latent state;
2. the environment contains unobserved side effects;
3. the future policy conditions on history;
4. stochastic seeds or budgets are not matched;
5. evaluation includes process constraints rather than only future task success.

This proposition prevents an attractive but invalid narrative. Full-trajectory evaluation can be practically necessary because traces reveal hidden writes, unsafe intermediate effects, or state transitions that endpoint instrumentation misses. It is not a new exception to Markov decision theory.

### 3.3 Causal graph

The intended causal structure is

\[
A_{0:T}
\longrightarrow
(C_T,E_T)
\longrightarrow
Y_{F},
\]

with current output \(Y_C\) held fixed. A valid mediation result should show:

\[
Y_C(a)=Y_C(a')
\]

but

\[
Y_F(a)\ne Y_F(a'),
\]

and after restoring the alleged mediator,

\[
Y_F\bigl(a,\operatorname{do}(C_T=C_T(a'))\bigr)
\approx
Y_F(a').
\]

The same logic applies to environment restoration. Without intervention, correlation between a memory write and later failure is not enough: both can be caused by a harder current episode or a generally weaker trajectory.

### 3.4 When divergence is scientifically uninteresting

The following observations do not establish a new failure mode:

- a worse current patch later causes more failures;
- a model edit with lower current-edit quality has worse locality;
- a longer context causes lower accuracy;
- an agent that spends less compute now has less information later;
- an unsafe policy has lower cumulative reward;
- a proof tactic creates harder subgoals;
- a memory record containing an explicit attack is retrieved later;
- no-write beats indiscriminate write because irrelevant context is distracting.

A credible result needs exact or unusually strong current matching, independent future probes, and state mediation.

---

## 4. Search protocol and evidentiary standard

### 4.1 Search cutoff and source policy

The search was conducted independently through **25 August 2026**. It used repeated query families rather than a single keyword pass, including combinations of:

- future tasks, side effects, reachability, attainable utility, empowerment, reversibility, viability, recoverability;
- persistent state, memory contamination, self-evolving agents, memory admission, rollback, transaction boundaries, persistent carriers;
- sequential code repair, software evolution, maintainability, future edits, chained issues, technical debt;
- proof-state value, theorem-search progress, process reward, trajectory value;
- model editing locality, sequential editing, catastrophic forgetting, interference;
- stateful tools, workspace side effects, transactional agents, rollback and checkpointing.

Primary sources were preferred: official proceedings, ACL Anthology, OpenReview, arXiv abstract pages, and official repositories. Search snippets were used only to locate papers; claims below are based on opened primary pages or their official abstracts. Papers first posted in 2026 and not yet peer reviewed are labeled **arXiv preprint** and should be treated as provisional evidence of novelty collision, not as validated scientific conclusions.

### 4.2 Novelty standard

A prior paper counts as a collision when it contains the same **measured variable or intervention**, not merely similar language. The strongest collisions satisfy one or more of:

- future-task success is the actual side-effect metric;
- current/local correctness coexists with harmful later behavior;
- persistent state is explicitly toggled, snapshotted, restored, or transacted;
- sequential code changes are evaluated by later modifications;
- proof states are ranked by later solvability;
- model updates are judged by retained capabilities or locality;
- a benchmark already separates task completion from safety or persistent state.

The report does not grant novelty for renaming these constructs as “carrier viability.”


---

## 5. Verified literature map

### 5.1 Foundational collision: future capability is already an impact and safety objective

| Paper | Authors, year, venue | Actual contribution | What it already covers | Residual left for this seed |
|---|---|---|---|---|
| [Avoiding Side Effects By Considering Future Tasks](https://proceedings.neurips.cc/paper/2020/hash/dc1913d422398c25c5f0b81cab94cc87-Abstract.html) | Victoria Krakovna, Laurent Orseau, Richard Ngo, Miljan Martic, Shane Legg; 2020; NeurIPS | Defines side-effect penalties through changes in the agent's ability to complete a set or distribution of future tasks rather than through raw state distance. | The central sentence of the seed—present success can preserve or destroy future-task capability—is already the paper's operational object. | Only domain-specific causal identification, measurement efficiency, or a new structural phenomenon can remain; the abstract objective is not novel. citeturn135493search0 |
| [Conservative Agency via Attainable Utility Preservation](https://arxiv.org/abs/1902.09725) | Alexander Matt Turner, Dylan Hadfield-Menell, Prasad Tadepalli; 2020; AIES | Penalizes decreases and increases in attainable auxiliary utilities to limit impact while retaining useful action. | Preserving a broad set of future achievable utilities is a direct formal antecedent of “retained future capability.” | AUP does not supply the proposed frozen-output, component-rollback causal protocol for LLM memory; that protocol is implementation-level residual, not a new objective. citeturn135493search1 |
| [Penalizing Side Effects Using Stepwise Relative Reachability](https://arxiv.org/abs/1806.01186) | Victoria Krakovna, Laurent Orseau, Ramana Kumar, Miljan Martic, Shane Legg; 2018/2019; arXiv preprint | Measures how actions reduce reachability of states relative to an inaction baseline, with stepwise penalties intended to avoid offsetting incentives. | Covers irreversible loss of reachable states and action consequences invisible to current reward. | It is state-reachability rather than task-distribution evaluation; a residual can test when task probes outperform reachability proxies in a concrete stateful agent. citeturn135493search2 |
| [AvE: Assistance via Empowerment](https://proceedings.neurips.cc/paper/2020/hash/30de9ece7cf3790c8c39ccff1a044209-Abstract.html) | Yuqing Du, Stas Tiomkin, Emre Kiciman, Daniel Polani, Pieter Abbeel, Anca Dragan; 2020; NeurIPS | Uses empowerment—the influence an agent can exert over future states—as a task-agnostic assistance objective. | Covers preservation of future controllability or option capacity without enumerating every later task. | Future benchmark success may diverge from generic empowerment, but that is an empirical comparison, not a new formal category. citeturn135493search3 |
| [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) | Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, Dan Mané; 2016; arXiv preprint | Systematizes negative side effects, reward hacking, scalable oversight, safe exploration, and distributional shift. | Already frames successful optimization as potentially damaging unpenalized state and future operation. | No residual at the problem-statement level. citeturn757684search0 |
| [Constrained Policy Optimization](https://proceedings.mlr.press/v70/achiam17a.html) | Joshua Achiam, David Held, Aviv Tamar, Pieter Abbeel; 2017; ICML | Optimizes expected return subject to expected cost constraints with policy updates designed to satisfy constraints. | The proposed “maximize current success subject to viability” objective is a constrained MDP once viability is a state/action cost or terminal constraint. | Residual must be in how the constraint is identified or predicted, not in writing it down. citeturn653492search0 |
| [Reachability Constrained Reinforcement Learning](https://proceedings.mlr.press/v162/yu22d.html) | Dongjie Yu, Haitong Ma, Shengbo Li, Jianyu Chen; 2022; ICML | Uses reachability analysis to enforce persistent safety rather than only cumulative expected costs. | Directly covers state constraints that must hold throughout a trajectory and distinguishes persistent safety from expected-cost safety. | No residual for the viability-kernel formulation itself. citeturn653492search5turn791547search15 |
| [Viability Theory](https://link.springer.com/book/10.1007/978-0-8176-4910-4) | Jean-Pierre Aubin; 2009 edition; Birkhäuser/Springer | Develops viability kernels: states from which admissible dynamics can remain within constraints. | The condition \(c_t\in K(e_t)\) and “best current action lies outside the viability kernel” are textbook viability statements. | Only a new learned estimator, empirical domain, or observation model can be novel. citeturn791547search6turn791547search14 |
| [There Is No Turning Back: A Self-Supervised Approach for Reversibility-Aware Reinforcement Learning](https://proceedings.neurips.cc/paper/2021/hash/0e98aeeb54acf612b9eb4e48a269814c-Abstract.html) | Nathan Grinsztajn, Johan Ferret, Olivier Pietquin, Matthieu Geist; 2021; NeurIPS | Learns to identify irreversible transitions and uses that signal in control. | Covers discrete “point of no return” events and recoverability-aware behavior. | LLM memory commits permit cleaner exact restoration and matched-output interventions, but irreversibility itself is not new. citeturn653492search2turn653492search6 |
| [Leave No Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning](https://openreview.net/forum?id=S1vuO-bCW) | Benjamin Eysenbach, Shixiang Gu, Julian Ibarz, Sergey Levine; 2018; ICLR | Jointly learns forward and reset policies so autonomous learning avoids unrecoverable states. | Covers reset, recoverability, and the danger of reaching states from which future operation is impaired. | Rollback cannot be sold as a new answer; it can only be used as a causal instrument. citeturn653492search3 |
| [Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach](https://proceedings.neurips.cc/paper/2015/hash/64223ccf70bbb65a3a4aceac37e21016-Abstract.html) | Yinlam Chow, Aviv Tamar, Shie Mannor, Marco Pavone; 2015; NeurIPS | Optimizes tail risk through CVaR in MDPs. | Covers rare high-cost future collapses when they are represented in a return/cost distribution. | A collision boundary may be statistically hard for a critic, but tail-risk optimization is not new. citeturn822243search0 |
| [Homeostatic Reinforcement Learning for Integrating Reward Collection and Physiological Stability](https://doi.org/10.7554/eLife.04811) | Mehdi Keramati, Boris Gutkin; 2014; eLife | Models reward through regulation of internal variables around viable ranges. | Covers agents trading task reward against maintenance of a capability-supporting internal state. | The LLM instantiation is different; the homeostatic abstraction is already occupied. citeturn791547search1 |
| [The Off-Switch Game](https://arxiv.org/abs/1611.08219) | Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel, Stuart Russell; 2017; IJCAI | Formalizes incentives around human intervention and shutdown under objective uncertainty. | Relevant when “future capability” means preserving human control or the shutdown channel. | Not a central match unless carrier changes disable oversight; including corrigibility would otherwise be scope inflation. citeturn822243search2 |
| [Reward Tampering Problems and Solutions in Reinforcement Learning](https://arxiv.org/abs/1908.04734) | Tom Everitt, Marcus Hutter, Ramana Kumar, Victoria Krakovna; 2021; Synthese | Analyzes agents altering reward functions or reward channels and formal countermeasures. | Covers current apparent success generated while corrupting the evaluative machinery for future behavior. | Distinct from benign memory contamination only when the carrier is not the reward channel. citeturn822243search3 |

**Binding conclusion from this table:** the generic objective has no residual novelty. A reviewer can translate it into an existing formalism without loss.

### 5.2 Persistent LLM memory: the cleanest carrier and the most damaging 2026 collision

The papers below are especially important because they use an independently persistent, inspectable state that genuinely changes later agent behavior. Most 2026 entries are arXiv preprints rather than peer-reviewed publications; that weakens their evidentiary status but not their ability to defeat a novelty claim.

| Paper | Authors, year, venue | Actual contribution | Seed coverage | Narrow residual, if any |
|---|---|---|---|---|
| [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://openreview.net/forum?id=pZiyCaVuti) | Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu; 2025; ICLR | Provides 500 questions testing information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention over long interaction histories. | Supplies public standardized future-memory probes with automatic or reliable evaluation. | Does not itself require exact current-output matching or component-level causal rollback. citeturn778306search0turn778306search2 |
| [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions / MemoryAgentBench](https://openreview.net/forum?id=DT7JyQC3MR) | Yuanzhe Hu, Yu Wang, Julian McAuley; 2026; ICLR | Evaluates accurate retrieval, test-time learning, long-range understanding, and selective forgetting under incremental information arrival. | Makes memory competence and selective forgetting established benchmark objects. | Can serve as a future-probe suite, but does not create the carrier-viability concept. citeturn820957search0turn820957search3 |
| [LongMemEval-V2: Benchmarking Memory-Augmented LLM Agents in Long-Term Multi-Session Conversations](https://arxiv.org/abs/2605.12493) | Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang; 2026; arXiv preprint | Extends evaluation to 451 questions and 1,870 trajectories with richer multi-session agent behavior and released data. | Provides realistic long-horizon trajectories and exact future probes. | Still leaves room for a frozen-output post-commit intervention, but not for another generic memory benchmark. citeturn778306search8turn778306search10turn778306search15 |
| [How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://aclanthology.org/2026.acl-long.27/) | Zidi Xiong, Yuping Lin, Wenya Xie, Pengfei He, Zirui Liu, Jiliang Tang, Himabindu Lakkaraju, Zhen Xiang; 2026; ACL | Studies how stored experiences are followed later and finds that apparently correct records can still be misleading; labels are grounded in downstream task outcomes. | Directly covers “locally/currently correct persistent state harms future tasks.” | Exact identical-output forks and restoration-mediated effects are not the paper's central design. citeturn917474search0 |
| [What Deserves Memory: Adaptive Memory Distillation for LLM Agents](https://aclanthology.org/2026.acl-long.1607/) | Wenquan Ma, Jiayan Nan, Wenlong Wu; 2026; ACL | Learns what to retain using future utility/predictability rather than only salience or recency. | Covers estimating whether a write will be useful for future behavior. | A new “viability critic” would collide directly unless it predicts harmful externalities under stronger causal controls. citeturn917474search1 |
| [Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences](https://arxiv.org/abs/2605.18930) | Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li; 2026; arXiv preprint | Introduces experiences that appear correct locally but transfer badly and poison subsequent self-evolution. | Almost exactly instantiates current/local success with later capability damage in a persistent experience carrier. | Its adversarial threat model leaves a benign self-generated, exact-output-matched setting as a residual. citeturn290956search2 |
| [Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents](https://arxiv.org/abs/2605.17830) | Ahmad Al-Tawaha, Shangding Gu, Peizhi Niu, Ruoxi Jia, Ming Jin; 2026; arXiv preprint | Uses longitudinal memory snapshots, fixed probes, and a no-memory counterfactual to track delayed safety risk. | Covers fixed post-success probes, persistence, counterfactual memory removal, and delayed harm. | The surviving gap is task capability rather than safety behavior, plus exact output-frozen write forks. citeturn290956search3 |
| [State Contamination in Memory-Augmented LLM Agents](https://arxiv.org/abs/2605.16746) | Yian Wang, Agam Goyal, Yuen Chen, Hari Sundaram; 2026; arXiv preprint | Uses paired counterfactual rollouts to show persistent memory can contaminate later reasoning and action. | Covers causal comparison of different persistent memory states and downstream propagation. | Selective restoration and a broad, pre-registered future-task capability distribution may still sharpen the protocol. citeturn513258search2turn513258search10 |
| [HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses](https://arxiv.org/abs/2608.06984) | Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He; 2026; arXiv preprint | Evaluates 328 lifecycle cases across seven persistent carrier families, including memory, skills, tools, and shared artifacts. | Defeats the claim that “persistent carrier” is an unstudied umbrella and already moves beyond memory alone. | A non-adversarial, capability-centered causal estimator could differ, but a cross-carrier benchmark is no longer novel by itself. citeturn290956search0 |
| [PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](https://arxiv.org/abs/2608.04003) | Shuhan Xue, Zixin Ding, Yichen Shen, Yinjie Wang, Zhenfei Yin, Yingcheng Wu, Yuxin Chen, Mengdi Wang, Ling Yang; 2026; arXiv preprint | Provides 26 scenarios and 204 episodes with persistence-on versus persistence-off comparisons and mechanism-oriented analysis. | Directly operationalizes matched persistent-state effects on later agent behavior. | Exact same current output and component swaps remain stricter than a coarse persistence toggle. citeturn290956search1 |
| [Memory Reward Inflation in Self-Improving LLM Agents](https://arxiv.org/abs/2608.00017) | Mohammad Asadolahi, Amir Amini, Samira Talebi, Amirfarhad Farhadi, Azadeh Zamanifar; 2026; arXiv preprint | Shows self-generated memory can inflate internal reward signals and impair self-improvement. | Covers self-induced carrier corruption rather than only adversarial poisoning. | A frozen visible output and exact causal capability recovery are not yet the central claim. citeturn513258search3turn513258search7 |
| [ChronoMem: Version Control and Semantic Rollback for LLM Agent Memory](https://arxiv.org/abs/2607.27773) | Yongye Su, Wujiang Xu, Chaoji Zuo, Elisa Bertino; 2026; arXiv preprint | Adds versioned memory and semantic rollback, enabling post-exposure restoration and counterfactual evaluation. | Covers rollback of persistent memory and restoration as a mitigation. | Rollback can still be used as a mediation test, but it is not method novelty. citeturn917474search2 |
| [MemTX: Transactional Belief Commit for Stateful Agent Memory](https://arxiv.org/abs/2607.23929) | Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Taotao Cai; 2026; arXiv preprint | Introduces transactional belief commits and cascade repair for stateful memory. | Covers commit control, corrupted-state propagation, and repair. | A predictor specifically optimized for future-task capability could be compared, but “transactional memory prevents damage” is occupied. citeturn917474search3 |
| [MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory](https://arxiv.org/abs/2607.27834) | Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia; 2026; arXiv preprint | Verifies source support, resolves conflicting versions, and restores complete declared active state after faults. | Covers write admission, visibility, full-state recovery, and memory transaction boundaries. | The residual must involve harmful but source-supported writes or future capability not reducible to factual consistency. citeturn820957search1turn820957search4 |
| [ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control](https://arxiv.org/abs/2607.22962) | Yan Zhang, Shibo Li; 2026; arXiv preprint | Uses write-time support checks to reject contaminated facts and evaluates downstream effects on conversation benchmarks. | Covers pre-commit prediction and prevention of persistent contamination. | A source-supported yet non-transferable or over-generalized write is the narrower unresolved regime. citeturn820957search2turn820957search5 |

**Memory verdict:** this is the best domain for causal identifiability, but the worst domain for claiming an untouched problem. A publishable result must target the thin seam between **truth/support of a write** and **its broad future externality under exact current-output equivalence**.

### 5.3 Sequential code and software evolution

| Paper | Authors, year, venue | Actual contribution | Seed coverage | Residual, if any |
|---|---|---|---|---|
| [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) | Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan; 2024; ICLR | Establishes repository-level issue resolution with executable tests. | Supplies exact current-task verifiers and realistic repositories. | It is mostly isolated-task; future repository viability is not its central metric. citeturn105489search27 |
| [SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios](https://arxiv.org/abs/2512.18470) | Minh V. T. Thai, Tue Le, Dung Nguyen Manh, Huy Phan Nhat, Nghi D. Q. Bui; 2025; arXiv preprint | Builds long-horizon software-evolution trajectories rather than isolated issue repair. | Directly moves evaluation to persistent repositories and later changes. | Exact matched-success patch pairs and component mediation may remain, but the domain-level pitch is occupied. citeturn999593search0 |
| [SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration](https://arxiv.org/abs/2603.03823) | Jialong Chen, Xander Xu, Hu Wei, Chuan Chen, Bing Zhao; 2026; arXiv preprint | Operationalizes maintainability by whether future modifications continue to work, rather than relying only on current tests or static quality proxies. | This is almost the exact code instantiation requested: current correctness versus later edit correctness. | A stricter causal paired-patch protocol is residual, not a new research object. citeturn776223search8turn105489search0 |
| [SlopCodeBench: Benchmarking How Coding Agents Degrade over Long-Horizon Iterative Tasks](https://arxiv.org/abs/2603.24755) | Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Frederic Sala, Aws Albarghouthi; 2026; arXiv preprint | Uses 20 problems and 93 checkpoints to show code can continue passing tests while becoming structurally harder to extend. | Covers present-task success with hidden future-maintenance damage and structural erosion. | Causal localization of the damaging edit and exact rollback could remain, but the headline phenomenon is occupied. citeturn999593search1 |
| [Beyond Isolated Tasks: A Benchmark for Long-Horizon Software Engineering / SWE-STEPS](https://arxiv.org/abs/2604.03035) | K. N. Ajay Shastry, Ganesh Senrayan, Shrey Satapara, Pranoy Panda, Chaitanya Devaguptapu; 2026; arXiv preprint | Evaluates agents across sequential pull-request-style changes in a persistent codebase. | Covers accumulated repository state and later-task degradation. | The residual is an ex ante damage predictor under current-patch matching. citeturn999593search2 |
| [SWE-Chain: A Longitudinal Benchmark for Continual Software Evolution](https://arxiv.org/abs/2605.14415) | Man Ho Lam, Chaozheng Wang, Hange Liu, Jingyu Xiao, Haau-sing Li, Jen-tse Huang, Terry Yue Zhuo, Michael R. Lyu; 2026; arXiv preprint | Constructs chained release-level software changes to evaluate continual evolution. | Covers long-term codebase state, cumulative edits, and later solvability. | No broad residual; only a stronger causal pair construction. citeturn999593search3 |
| [ChainSWE: Benchmarking Coding Agents on Multi-Bug Software Maintenance](https://arxiv.org/abs/2607.02606) | Qirui Jin, Lingching Tung, Kenan Li, Qiyang Shi, Yushi She, Huanzhong Jia, Harrison Zhao, Kejing Xia, Zhenbang Du, Yikai Zhang, Jiaxin Pei, Zhenyu Zhang, Zhen Qi, Yuyan Duan, Wenke Lee, Zijian Jin; 2026; arXiv preprint | Sequences 304 issues from 54 Python projects, comparing shared accumulated state with cleaner/oracle variants. | Directly measures how earlier patches affect later issue resolution and provides reset-style counterfactuals. | Exact behavior-equivalent patch forks and selective file/dependency restoration remain narrower. citeturn489343search0 |
| [Is Agent Code Less Maintainable Than Human Code? / CodeThread](https://arxiv.org/abs/2606.21804) | Shaswat Patel, Betty Li Hou, Arun Purohit, Kai Xu, Jane Pan, He He, Valerie Chen; 2026; arXiv preprint | Uses controlled two-step pull-request chains and test-based downstream evaluation; reports that common static metrics often fail to capture later maintainability. | Covers causal downstream edit difficulty, human-versus-agent patches, and failure of generic code-quality proxies. | A more exact same-output/current-semantics match might tighten identification, but the main empirical question is already explicit. citeturn489343search1 |
| [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) | D. Sculley, Gary Holt, Daniel Golovin, Eugene Davydov, Todd Phillips, Dietmar Ebner, Vinay Chaudhary, Michael Young, Jean-François Crespo, Dan Dennison; 2015; NeurIPS | Catalogues entanglement, hidden feedback loops, undeclared consumers, data dependencies, and other future costs invisible to immediate metrics. | Establishes the general current-performance versus future-maintainability problem. | LLM-agent causal experiments can be new; “technical debt exists” cannot. citeturn776223search0 |

**Code verdict:** benchmark maturity and executable verifiers are excellent, but 2026 work already occupies future-edit viability. Producing multiple genuinely equivalent correct patches and running downstream agents is also materially slower and more confounded than the memory audit.

### 5.4 Tool agents, persistent workspaces, and transactions

| Paper | Authors, year, venue | Actual contribution | Seed coverage | Residual, if any |
|---|---|---|---|---|
| [ToolEmu: Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://openreview.net/forum?id=GEcwtMk1uA) | Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, Tatsunori Hashimoto; 2024; ICLR | Uses an emulated tool sandbox to evaluate risky agent actions and side effects. | Covers successful task pursuit that causes unpenalized tool/environment harm. | Does not specifically measure retained future-task capability, but generic tool side effects are occupied. citeturn313749search24 |
| [ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](https://aclanthology.org/2025.findings-naacl.65/) | Jiarui Lu, Thomas Holleis, Yizhe Zhang, Bernhard Aumayer, Feng Nan, Felix Bai, Shuang Ma, Shen Ma, Mengyu Li, Guoli Yin, Zirui Wang, Ruoming Pang; 2025; Findings of NAACL | Provides stateful tool interactions with milestones, dependencies, and exact environment checks. | Supplies persistent state, trajectory-level evaluation, and reliable verifiers. | A future-task replay protocol could be added, but it would be a benchmark extension. citeturn313749search1turn313749search5 |
| [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) | Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan; 2024; arXiv/benchmark | Evaluates policy compliance and database-state correctness in realistic multi-turn tool domains. | Covers task completion plus persistent database consequences. | Later-task controllability is not central, but stateful planning is established. citeturn390810view0 |
| [τ²-bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) | Victor Barres, Honghua Dong, Soham Ray, Xujie Si, Karthik Narasimhan; 2025; arXiv preprint | Extends interactive evaluation to jointly evolving user and tool environments. | Covers environment coupling and multi-turn state consequences. | No distinct carrier concept emerges. citeturn313749search2 |
| [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/abs/2606.17573) | Zheng Chen, Hanqing Liu, Duling Xu, Dong Dong, Jialin Li, Bangzheng Pu, Jidong Zhai; 2026; arXiv preprint | Introduces semantic transaction boundaries to manage and recover external effects of tool trajectories. | Directly covers commit, rollback, partial failure, and persistent external state. | “Use transactions to preserve viability” is not novel. A predictive commit-risk estimator could be compared. citeturn489343search2 |
| [Agentic Transaction: Towards ACID-Compliant Agent Systems](https://arxiv.org/abs/2608.13900) | Zhaoyan Sun, Xiaoxiao Wang, Guoliang Li; 2026; arXiv preprint | Applies transaction semantics to agent actions and persistent effects. | Occupies rollback/checkpoint/atomicity as an agent-design contribution. | Only task-specific semantic risk prediction remains. citeturn390810view1 |
| [AgentS4D](https://arxiv.org/abs/2607.27294) | Jiajun Zhou, Zhaoxuan Ke, Jihang Ye, Xuanze Chen, Shanqing Yu, Qi Xuan; 2026; arXiv preprint | Uses independent completion and safety checkers over traces, artifacts, and workspace state. | Separates completion from safety and endpoint from trace/workspace checks. | Future capability probes could be another checker target, not a new framework. citeturn489343search3 |

**Tool/workspace verdict:** clean state intervention is possible, but the framing collapses to safe stateful planning and semantic transactions. The residual is weaker than in memory because the “carrier” is usually just the external environment.

### 5.5 Model parameters, continual learning, theorem proving, and test-time reasoning

| Paper | Authors, year, venue | Actual contribution | Seed coverage | Verdict |
|---|---|---|---|---|
| [Overcoming Catastrophic Forgetting in Neural Networks](https://www.pnas.org/doi/10.1073/pnas.1611835114) | James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, Raia Hadsell; 2017; PNAS | EWC protects parameters important to previous tasks while learning new tasks. | The model weights are a true carrier, and future capability loss after a successful update is catastrophic forgetting. | No residual umbrella novelty. citeturn634527search2turn634527search5 |
| [Gradient Episodic Memory for Continual Learning](https://proceedings.neurips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html) | David Lopez-Paz, Marc'Aurelio Ranzato; 2017; NeurIPS | Constrains updates using episodic memories and introduces retention/transfer metrics. | Covers matched present learning against retained prior-task performance. | No residual except a new task or mechanism. citeturn634527search1turn634527search18 |
| [Locating and Editing Factual Associations in GPT / ROME](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html) | Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov; 2022; NeurIPS | Causally localizes and edits factual associations in transformer parameters and evaluates edit success, generalization, and specificity. | Model weights are the carrier; locality is collateral capability preservation. | The seed collapses to model-editing locality. citeturn634491search0 |
| [Memory-Based Model Editing at Scale / SERAC](https://proceedings.mlr.press/v162/mitchell22a.html) | Eric Mitchell, Charles Lin, Antoine Bosselut, Christopher D. Manning, Chelsea Finn; 2022; ICML | Uses an external edit memory and scope classifier to change selected behavior while preserving out-of-scope predictions. | Explicitly separates current edit success from locality and broad side effects. | No residual umbrella novelty. citeturn634527search3 |
| [Model Editing at Scale Leads to Gradual and Catastrophic Forgetting](https://aclanthology.org/2024.findings-acl.902/) | Akshat Gupta, Anurag Rao, Gopala Anumanchipalli; 2024; Findings of ACL | Shows sequential ROME/MEMIT edits cause gradual then abrupt forgetting of prior edits and downstream abilities. | Directly covers discontinuous capability collapse after individually successful updates. | This candidate domain is eliminated. citeturn120042search0turn120042search2 |
| [Model Editing Harms General Abilities of Large Language Models: Regularization to the Rescue](https://aclanthology.org/2024.emnlp-main.934/) | Jia-Chen Gu, Hao-Xiang Xu, Jun-Yu Ma, Pan Lu, Zhen-Hua Ling, Kai-Wei Chang, Nanyun Peng; 2024; EMNLP | Measures general reasoning, NLI, and QA degradation after successful edits and proposes update regularization. | Directly measures independent future/general capability damage. | Eliminated. citeturn120042search1turn120042search3 |
| [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html) | Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J. Prenger, Animashree Anandkumar; 2023; NeurIPS Datasets and Benchmarks | Provides a Lean environment, data extraction, retrieval, and exact proof verification. | Supplies exact states and action trajectories, but subgoal quality is current-problem search state. | Domain eliminated unless the agent edits a persistent shared library. citeturn634491search3 |
| [HyperTree Proof Search for Neural Theorem Proving](https://arxiv.org/abs/2205.11491) | Guillaume Lample, Timothee Lacroix, Marie-Anne Lachaux, Aurelien Rodriguez, Amaury Hayat, Thibaut Lavril, Gabriel Ebner, Xavier Martinet; 2022; NeurIPS | Uses learned tactic and value guidance over proof-search states. | Ranking two tactics by later solvability is already proof-state value/search. | Eliminated. citeturn634491search2 |
| [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://arxiv.org/abs/2408.08152) | Huajian Xin, Z. Z. Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, Wenjun Gao, Qihao Zhu, Dejian Yang, Zhibin Gou, Z. F. Wu, Fuli Luo, Chong Ruan; 2024/2025; arXiv, ICLR 2025 | Uses proof-assistant feedback, RL, and MCTS to improve Lean proof search. | Current subgoal choices and continuation viability are explicit search/value objects. | Eliminated. citeturn864141view1 |
| [Let's Verify Step by Step](https://openreview.net/forum?id=v8L0pN6EOi) | Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe; 2024; ICLR | Trains process reward models to evaluate intermediate reasoning steps and guide selection. | A “reasoning-state viability critic” is a process/value model unless state persists beyond the problem. | Test-time reasoning candidate eliminated. citeturn182784search0turn182784search1 |

### 5.6 Literature-map conclusion

The literature produces a clean partition:

- **Abstract decision problem:** already covered by future-task impact measures, AUP, viability, constrained control, empowerment, and risk-sensitive value.
- **Model parameters:** already covered by continual learning, edit locality, and sequential-edit forgetting.
- **Proof/reasoning state:** already covered by value-guided search and process reward models.
- **Repository/workspace:** already covered by software maintenance, stateful-agent safety, and transactions.
- **Persistent memory:** causally clean but heavily occupied; only a stricter post-output commit intervention remains plausibly distinct.

This is sufficient for a **NO-GO** on the broad seed.

---

## 6. Novelty-collision matrix and mandatory collision ledger

The table below addresses every required adjacent field. “Collapse severity” asks whether replacing that field's terminology with “carrier viability” would leave the mathematical or empirical problem essentially unchanged.

| Adjacent field | Exact collision with the seed | Collapse severity | What would have to be new |
|---|---|---:|---|
| Negative side effects in AI safety | Successful action damages unpriced state or later opportunities. | **Fatal at umbrella level** | A concrete causal estimator that beats existing impact measures under exact matching. |
| Impact measures | State change is penalized by reachability, attainable utilities, or deviations from a baseline. | **Fatal** | Show generic impact scores reverse the correct ranking while targeted future probes succeed. |
| Attainable utility preservation | Preserves future achievable auxiliary utilities. | **Fatal** | A practical/statistical failure of utility sampling, not a renamed objective. |
| Relative reachability | Measures lost reachable states after an action. | **Fatal for option-set framing** | Demonstrate small semantic state changes with large task-specific capability loss that reachability proxies miss. |
| Empowerment / assistance via empowerment | Preserves future control over states or the human's options. | **High** | Show task success distribution contains information not captured by empowerment at matched estimator capacity. |
| Viability theory / viability kernels | Maintains state inside a set from which constraints remain satisfiable. | **Fatal for \(K(e)\)** | Learn/identify the kernel in a new partially observed domain with causal ground truth. |
| Safe RL | Trades task return against safety or failure avoidance. | **High** | Current output must be fixed and the target must be an independently measured persistent-state externality. |
| Constrained MDPs | Maximizes current or cumulative reward subject to a cost/viability constraint. | **Fatal formal collapse** | Only the construction and estimation of the constraint can be novel. |
| Risk-sensitive RL | Penalizes rare or tail future capability collapse. | **High** | Evidence that rare discontinuities defeat fair CVaR/distributional critics and are recoverable by a specialized observable. |
| Reversible MDPs / recoverability | Avoids or detects irreversible transitions and points of no return. | **High** | Typed LLM-state interventions with exact output freezing; reversibility itself is old. |
| Reset-free RL | Maintains states from which autonomous operation can continue and learns reset behavior. | **High** | External-memory causal protocol; reset/rollback is not the contribution. |
| Safe exploration | Avoids entering unknown unsafe or unrecoverable regions. | **High** | The damage must occur after verified success and be separable from exploration risk. |
| Homeostatic RL | Regulates internal variables needed for continued operation. | **High** | A concrete digital carrier and independent task probes; not another homeostatic objective. |
| Long-horizon planning | Values current actions by later outcomes. | **Fatal in principle** | Partial observability, unknown future distribution, sample-efficient probing, or critic misspecification must be the scientific issue. |
| Model-based RL / world models | Predicts state transitions and downstream consequences before acting. | **High** | Demonstrate a systematic blind spot not repaired by a compute-matched learned transition/value model. |
| Multi-objective control | Optimizes current task, future capability, compute, and state change jointly. | **Fatal objective collapse** | A non-obvious causal metric and Pareto improvement, not a new weighted sum. |
| Catastrophic forgetting | Successful learning of a new task damages prior-task ability. | **Fatal for parameter carrier** | None at the umbrella level. |
| Continual learning | Evaluates retention, backward transfer, interference, and future learning. | **Fatal for parameter updates** | A new domain or identifiable mechanism beyond established retention metrics. |
| Neural interference | Small updates alter unrelated functions or future learnability. | **High** | A structural, reproducible discontinuity with causal parameter-subspace evidence. |
| Model editing / edit locality | Current edit success is separated from locality and general abilities. | **Fatal for model-edit instantiation** | None without a fundamentally new causal question. |
| Sequential model editing | Repeated successful edits cause gradual or abrupt collapse. | **Fatal** | None for “collision-like” parameter damage. |
| Memory-augmented agents | Persistent writes are retrieved and affect later behavior. | **High** | Exact output-frozen write forks, broad future probes, fair value baselines, and component restoration. |
| Memory poisoning | Benign-looking or locally correct records induce downstream failures. | **Near-fatal** | Non-adversarial self-generated writes and source-supported but non-transferable content. |
| Memory management | Admission, deletion, consolidation, relevance, and future utility are optimized. | **Near-fatal** | Predict a different target—causal broad degradation—not relevance, truth, or expected utility already optimized. |
| Context pollution | Irrelevant/conflicting context reduces future accuracy. | **High** | Separate persistence from context length and retrieval load; restore only the persistent record. |
| Tool-use side effects | Correct task completion produces unsafe or unintended external actions. | **High** | Show future action-set loss after matched successful trajectories, beyond existing safety checkers. |
| Persistent-state agents | Later behavior depends on retained database/workspace/memory state. | **Near-fatal** | A narrow mechanism or prediction result, not the statefulness observation. |
| Transactional agents | Validate, commit, abort, checkpoint, and roll back agent effects. | **Near-fatal for mitigation** | Transactions are a baseline; perhaps selective risk-aware commits beat always-transactional conservatism. |
| Rollback / checkpointing | Restores a safe or correct prior state. | **Fatal as method novelty** | Use rollback only for causal identification or show selective rollback dominates full rollback. |
| Software maintainability | A current change affects cost/correctness of later changes. | **Fatal for code framing** | Objective, executable, causal matched-patch evidence and a predictor beyond current 2026 benchmarks. |
| Technical debt | Immediate functionality hides future coupling and maintenance cost. | **Fatal conceptually** | An LLM-agent-specific mechanism and benchmark result. |
| Sequential code repair | Earlier patches change later issue solvability. | **Near-fatal empirically** | Exact behavior-equivalent patch pairs and selective state swaps. |
| Repository-level code agents | Act in a persistent codebase with executable verification. | **High** | Future-edit externalities at matched current semantics, not just another SWE-bench score. |
| Proof-state evaluation | A tactic leaves subgoals with different future solvability. | **Fatal** | Only persistent proof-library edits could escape current-task value. |
| Process reward models | Score intermediate steps by correctness/continuation quality. | **Fatal for test-time reasoning** | State must persist across independent tasks; otherwise this is process reward. |
| Value models / trajectory evaluation | Predict later success from current state or trace. | **Fatal in principle** | A measurable statistical failure and a target cheaper/more identifiable than generic value. |
| Reward hacking / specification gaming | Apparent task success damages evaluator, environment, or intended objective. | **High** | Focus on benign output-equivalent state externalities with an uncompromised verifier. |
| Conservative agency | Preserves options or minimizes impact, risking excessive inaction. | **High** | Show a targeted predictor improves the success–future-capability Pareto frontier over no-write/no-change. |
| Corrigibility / shutdown reachability | Preserves human intervention and shutdown options. | **Peripheral** | Relevant only if the carrier modification changes oversight/control channels. |

### 6.1 The decisive mathematical collapse

Let the future task request \(q\), persistent state \((c,e)\), policy \(\pi\), and budget \(B\) be included in an augmented state. Then

\[
V_F(c,e)
=
\mathbb E_{q\sim\mathcal D_F}
\left[
\operatorname{Success}(q\mid c,e,\pi,B)
\right]
\]

is a terminal continuation value. A policy that maximizes

\[
\Pr(S_{\mathrm{cur}}=1)+\lambda V_F(c_T,e_T)
\]

is ordinary long-horizon or multi-objective control. A policy subject to

\[
V_F(c_T,e_T)\ge \tau
\]

is a constrained control problem. Requiring state to remain in

\[
\mathcal K_\tau=\{(c,e):V_F(c,e)\ge\tau\}
\]

is a viability formulation. Replacing \(V_F\) with a vector of auxiliary attainable utilities gives AUP; replacing it with reachable-state mass gives relative reachability; replacing it with channel capacity gives empowerment.

Therefore an extra “carrier critic” is **not necessary in principle**. It is scientifically justified only if at least one practical failure is demonstrated:

1. the relevant persistent state is partially observed or omitted from standard value inputs;
2. the future-task distribution is unknown, shifting, or too broad to enumerate;
3. broad future evaluation is prohibitively expensive and a small probe set is predictively sufficient;
4. damage is rare and discontinuous, causing ordinary regression/value training to average it away;
5. generic state distance, reachability, or empowerment is badly misaligned with task competence;
6. the causal carrier component can be isolated more cleanly than total return.

The proposed pilot must test these failures rather than assume them.

---

## 7. Candidate AI instantiations and comparative evaluation

### 7.1 Scoring convention

Scores below range from 1 to 5. For **readiness variables**, 5 is favorable. For **collision risk**, 5 means the candidate is very likely to collapse into known work and is therefore unfavorable. “First signal” scores how plausible a decisive result is within 3–7 days, not how easy it is to produce any number.

### 7.2 Eight candidate instantiations

| ID | Instantiation | Concrete \(x\) | Concrete \(c\) | Concrete \(e\) | Current-success match | Future probe |
|---|---|---|---|---|---|---|
| A | Sequential code agents | Current issue specification and local test state | Agent memory/skills, if persisted | Repository, tests, dependencies, CI state | Two patches pass the same full current suite and behavioral probes | Later chronological issues or controlled follow-up PRs |
| B | Memory-augmented LLM agents | Current dialogue/request and answer | Writable episodic/semantic/procedural memory plus retrieval metadata | External facts/tools, held fixed | Freeze the exact answer, then fork only the memory commit | Fixed later QA, update, conflict, tool-action, and shifted-task probes |
| C | Continual learning / model editing | Current task batch or requested factual edit | Model parameters and optimizer state | Dataset/evaluation environment | Same current loss/edit success and paraphrase generalization | Prior tasks, general abilities, locality, future learning |
| D | Formal theorem proving | Current theorem's proof state | Normally none; optionally a persistent lemma/tactic library | Lean environment and imported libraries | Both tactics close the same immediate subgoal or prove the theorem | Remaining proof solvability or later theorems |
| E | Multi-turn tool agents | Current user request and active plan | Persistent agent memory/tool policy | Database, filesystem, calendar, CRM, permissions | Same delivered answer and exact task-state checker | Later tasks replayed from post-action workspace snapshots |
| F | Test-time LLM reasoning | Current reasoning prefix/search node | Usually none persistent | Static problem | Same intermediate or final answer correctness | Continuation success on the same problem |
| G | Self-evolving skill-library agents | Current task and selected skill execution | Persisted skills, reflections, demonstrations, routing metadata | Task environment | Same current task output; different skill admission | Later task families requiring transfer or conflicting skills |
| H | Persistent prompts, runbooks, and dependency registries | Current task | Reused `CLAUDE.md`-like instructions, policy files, tool registry, credentials | Repository/workspace | Same current answer/patch; different persistent instruction update | Later code/tool tasks under the updated runbook |

### 7.3 Empirical readiness

| Domain | Public benchmark availability | Verifier quality | Causal identifiability | Exact current matching | Future-probe quality | Engineering tractability | 8×4090 fit | Decisive 3–7 day signal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A. Sequential code | 5 | 5 | 3 | 2 | 4 | 2 | 3 | 2 |
| B. Persistent memory | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 |
| C. Continual/model editing | 5 | 5 | 5 | 4 | 5 | 4 | 3 | 4 |
| D. Theorem proving | 5 | 5 | 4 | 3 | 2 | 3 | 4 | 4 |
| E. Tool/workspace agents | 4 | 4 | 4 | 3 | 3 | 2 | 4 | 3 |
| F. Test-time reasoning | 5 | 5 | 2 | 4 | 1 | 5 | 5 | 5 |
| G. Skill-library agents | 2 | 3 | 4 | 4 | 3 | 2 | 4 | 2 |
| H. Persistent prompts/runbooks | 3 | 4 | 5 | 5 | 4 | 4 | 5 | 5 |

### 7.4 Novelty and reviewer risk

| Domain | Baseline maturity | Metric objectivity | Risk of subjective claims | Collapse risk | 2026 prior-work pressure | ICLR residual assessment |
|---|---:|---:|---:|---:|---:|---|
| A. Sequential code | 5 | 5 for tests, 2 for style | High unless future tests are used | 5 | **Extreme**: SWE-CI, ChainSWE, SWE-STEPS, SWE-Chain, SlopCodeBench, CodeThread | **Eliminate as primary** |
| B. Persistent memory | 5 | 4 | Moderate | 5 | **Extreme**: OEP, PAST-Bench, HarnessSafe, State Contamination, ACL 2026 memory work, transactions | **Keep only a narrow causal audit** |
| C. Continual/model editing | 5 | 5 | Low | 5 | Mature for years; direct sequential-collapse results | **Eliminate** |
| D. Theorem proving | 5 | 5 | Low | 5 | Value-guided proof search is standard | **Eliminate** |
| E. Tool/workspace agents | 4 | 4 | Moderate | 5 | ToolEmu, ToolSandbox, τ-bench, Cordon, transactional agents | **Eliminate as carrier paper** |
| F. Test-time reasoning | 5 | 5 | Low | 5 | Process rewards and value search directly cover it | **Eliminate immediately** |
| G. Skill-library agents | 2 | 3 | High | 4 | Rapidly growing self-evolving-agent and skill-poisoning work | **Too immature and crowded** |
| H. Persistent prompts/runbooks | 3 | 4 | Moderate | 4 | HarnessSafe and 2026 agentic-coding memory/instruction work | **Possible replication, not primary** |

### 7.5 Domain-specific feasibility and failure modes

#### A. Sequential code agents

**Strengths.** Repositories are snapshot-able; tests can be exact; future changes are meaningful; causal rollback is possible at file or hunk granularity.

**Fatal weaknesses.** “Same tests pass” does not imply semantically equivalent current patches. A patch that causes later failure may simply be under-specified now. Producing several independently correct solutions per issue is expensive. Future-agent performance also compounds stochastic planning errors and large inference cost. Most importantly, 2026 benchmarks already define maintainability through future changes. citeturn776223search5turn776223search8turn105489search1turn105489search2

**Decision:** secondary replication only, after a strong memory result.

#### B. Persistent memory

**Strengths.** The visible answer can be generated once and frozen; the memory commit happens afterward; stores can be copied exactly; later probes can be replayed from identical snapshots; a single record can be deleted or swapped; computation is modest with 7B–14B models.

**Fatal weaknesses.** Nearly every intuitive claim has appeared in 2026: locally correct harmful experiences, contamination, future-utility admission, matched persistence controls, longitudinal probes, rollback, and transactions. citeturn290956search1turn290956search2turn290956search3turn917474search0turn917474search1turn917474search2turn820957search1

**Decision:** only domain worth a capped falsification audit because causal cleanliness is unusually high.

#### C. Continual learning and model editing

The carrier is unambiguous and exact restoration is trivial by loading the old checkpoint. Unfortunately, retention, backward transfer, locality, sequential interference, gradual forgetting, and abrupt collapse are established. citeturn634527search2turn634527search3turn120042search1turn120042search2

**Decision:** eliminate.

#### D. Formal theorem proving

Within one theorem, a tactic's “future viability” is the value of its resulting proof state. Exact verification does not rescue novelty. A persistent lemma library would move the problem to code/library evolution or continual memory, with greater engineering burden.

**Decision:** eliminate.

#### E. Multi-turn tool agents

Persistent database and workspace effects are clear, and transaction boundaries permit interventions. But the natural formulation is safe stateful planning, policy compliance, or transactional execution. ToolEmu, ToolSandbox, τ-bench, Cordon, and AgentS4D already separate completion from unsafe trace or workspace effects. citeturn221013search0turn221013search1turn221013search2turn513258search12

**Decision:** eliminate as a standalone carrier-viability paper.

#### F. Test-time reasoning

The reasoning prefix is normally discarded. It therefore does not carry capability into independent future tasks. Its continuation quality is a process reward or value model.

**Decision:** eliminate without experiment.

#### G. Self-evolving skills

This is a true carrier, and the locally-successful/non-transferable skill story is plausible. OEP and 2026 skill-poisoning work already target it, while benchmarks and exact verifiers remain less mature than memory QA. citeturn290956search2turn633221search13turn633221search25

**Decision:** eliminate for a rapid project; possible long-term security topic.

#### H. Persistent prompts and runbooks

The intervention is exceptionally clean: issue the same current answer, then write different persistent instructions. Later tasks can reveal useful or harmful over-generalization. However, HarnessSafe already treats persistent instructions/skills/artifacts as carriers, and agentic coding work studies growing instruction files. citeturn290956search0turn390810view2

**Decision:** reserve as a low-cost replication condition inside the memory audit, not a second paper.

---

## 8. Aggressive elimination funnel

### Gate 1: Is the proposed “carrier” actually persistent across independent tasks?

- **Test-time reasoning:** no → eliminate.
- **Ordinary proof state:** no → eliminate.
- **Current issue state:** no; the repository is external state → reclassify as environment.
- **Weights, writable memory, skill libraries, persistent prompts:** yes → continue.

### Gate 2: Does the formal objective survive translation into established theory?

- Weights plus future-task retention → continual learning/model editing.
- Reachable future tasks → relative reachability/AUP/empowerment.
- Remain inside safe state set → viability/reachability-constrained RL.
- Expected future probe success → continuation value.
- Current success under a future-capability constraint → CMDP.

**Result:** no formalization survives as a new decision problem.

### Gate 3: Does a concrete empirical domain remain undermeasured?

- Model editing: no; current edit success versus general ability/locality is established.
- Code: no at domain level; 2026 long-horizon and future-maintenance benchmarks exist.
- Tools: no at domain level; stateful safety and transactions exist.
- Memory: mostly no; 2026 work directly studies contamination, future utility, persistence, rollback, and locally correct harmful experiences.

**Result:** only an unusually strict causal protocol remains.

### Gate 4: Can that residual be tested without subjective labels or a new large benchmark?

- Code: difficult, because current semantic equivalence and future issue sequencing are expensive.
- Tool agents: possible, but environment configuration and user-policy evaluation are substantial.
- Memory: yes, because the output can be frozen and stores can be snapshotted and replayed with public future QA.

**Result:** memory is the only practical audit domain.

### Gate 5: Could a positive result exceed “memory pollution exists”?

Only if all of the following hold:

1. exact current output and current quality are fixed;
2. the harmful write is source-supported and not an obvious poison;
3. broad future capability—not only one targeted question—drops materially;
4. selective memory restoration recovers most of the loss;
5. generic state-change, truth, relevance, confidence, and compute-matched value baselines fail;
6. no-write is not the Pareto winner;
7. a small predictor or probe set generalizes across models and future-task resampling;
8. preferably, a small intervention crosses a reproducible collision boundary.

**Result:** a pilot can try to falsify this conjunction. It should not presume success.

---

## 9. The top surviving audit domains

### 9.1 Primary audit: post-output writes in persistent LLM memory

**Exact residual question**

> After producing exactly the same correct current answer, do different source-supported memory commits cause large and causally recoverable changes in broad later-task performance, and can that effect be predicted more accurately than by generic continuation value, write confidence, relevance, or state distance?

Why this is the least-bad option:

- the carrier boundary is exact;
- current output can be byte-identical;
- write timing can be moved after output generation;
- memory state can be snapshotted, swapped, and selectively rolled back;
- LongMemEval, LongMemEval-V2, MemoryAgentBench, LoCoMo, and PAST-Bench provide public scenarios and probes; citeturn778306search0turn778306search8turn820957search0turn190493search1turn290956search1
- 7B–14B open models fit the available hardware;
- the experiment can fail decisively in days.

Why it is not yet a GO:

- the core phenomenon is anticipated by OEP, ACL 2026 memory-management work, State Contamination, PAST-Bench, and *Remembering More, Risking More*; citeturn290956search1turn290956search2turn290956search3turn513258search2turn917474search0
- a top-\(k\) retrieval discontinuity is mathematically unsurprising;
- a better heuristic gate would look incremental next to Nemori, ConsistencyGate, MemTX, and MemTxn. citeturn917474search1turn917474search3turn820957search1turn820957search2

### 9.2 Secondary replication: paired future edits in code

This should be attempted only after the memory pilot produces a large, baseline-resistant causal effect. The replication would use pairs of current patches that pass the same full suite, then replay one or two controlled follow-up changes from each repository snapshot. The purpose would not be another code benchmark; it would be to test whether the same **small-state-change / large-future-effect / selective-restoration** signature appears in a different substrate.

The code replication is expensive and carries a severe semantic-equivalence confound. It is therefore inappropriate as the first 3–7 day test.

### 9.3 Survivor status

| Domain | Status | Permitted investment now |
|---|---|---:|
| Persistent memory | **Residual audit only** | 2 GPUs, ≤200 GPU-hours |
| Sequential code | **Conditional replication only** | 0 until memory gate passes |
| All others | **Eliminated** | 0 |

---

## 10. Competing formalizations

### 10.1 Formalization A: expected future-task success

For a matched-success trajectory set

\[
\mathcal T^+(q_0)
=
\{\tau:S_{\mathrm{cur}}(q_0,\tau)=1,
\;Q_{\mathrm{out}}(\tau)\ge q_{\min}\},
\]

define terminal future capability

\[
\Phi_{\mathcal D_F,B}^{\pi}(\tau)
=
\mathbb E_{q\sim\mathcal D_F}
\left[
S(q\mid c_T(\tau),e_T(\tau),\pi,B)
\right].
\]

Post-success damage relative to a reference trajectory \(\tau^{\mathrm{ref}}\) is

\[
D_F(\tau)
=
\Phi(\tau^{\mathrm{ref}})-\Phi(\tau).
\]

An oracle label is obtained by replaying a fixed sample of future tasks from the post-success snapshot. The prediction target is either \(D_F\) or a thresholded label \(\mathbb 1[D_F\ge d_0]\).

**Advantage:** directly interpretable and benchmarkable.

**Fatal collapse:** this is a terminal value function over a task distribution. If the state, task distribution, policy, and budget are known, a generic value model is sufficient in principle.

**Residual scientific question:** can \(D_F\) be estimated much more sample-efficiently from typed persistent-state interventions than by a generic critic, especially under distribution shift and rare discontinuities?

### 10.2 Formalization B: retained option set and viability kernel

For a success threshold \(\alpha\), define the retained option set

\[
\mathcal R_{\alpha,B}(c,e)
=
\{q:\Pr[S(q\mid c,e,\pi,B)=1]\ge\alpha\}.
\]

Given a minimum acceptable option mass \(\tau\), define

\[
\mathcal K_{\alpha,\tau}
=
\left\{(c,e):
\Pr_{q\sim\mathcal D_F}
[q\in\mathcal R_{\alpha,B}(c,e)]
\ge\tau
\right\}.
\]

A trajectory is viable when its endpoint lies in \(\mathcal K_{\alpha,\tau}\); a stronger pathwise condition requires every persistent post-commit state to remain in the set.

A tail-sensitive variant is

\[
\Phi_{\mathrm{tail}}(c,e)
=
\operatorname{CVaR}_{\beta}
\left(S(q\mid c,e,\pi,B)\right),
\]

or, for grouped task families,

\[
\Phi_{\mathrm{robust}}(c,e)
=
\min_{g\in\mathcal G}
\mathbb E_{q\sim\mathcal D_g}[S(q\mid c,e)].
\]

**Advantage:** distinguishes average competence from losing an entire class of future options and captures rare collapses.

**Fatal collapse:** this is viability theory plus distributionally robust or risk-sensitive control. Relative reachability, AUP, and empowerment are alternative option-preservation proxies. citeturn135493search0turn135493search1turn135493search2turn135493search3turn822243search0

**Residual scientific question:** do task-grounded option sets reveal damage that generic state reachability, empowerment, and average value systematically miss in persistent LLM memory?

### 10.3 Formalization C: causal post-output commit externality

This is the narrowest formulation that remains worth testing.

Let \(s^-=(x_T,c^-,e_T)\) be the state immediately after the visible answer is generated but before a persistent commit. The answer \(y\) is cached and immutable. A commit policy applies intervention \(u\) to produce

\[
c^+(u)=U(c^-,u),
\qquad y(u)=y\quad\forall u.
\]

Let \(Y_i(u)\) be success on future probe \(q_i\) from \((c^+(u),e_T)\). Relative to a reference commit \(u_0\), define the causal post-output externality

\[
\operatorname{CPE}(u;u_0)
=
\frac{1}{m}
\sum_{i=1}^{m}
\left(Y_i(u_0)-Y_i(u)\right).
\]

For a component \(j\) of memory, a restoration intervention gives

\[
\operatorname{Med}_j(u)
=
\Phi\!\left(
\operatorname{do}(c_j=c_j^-),
 c_{-j}=c_{-j}^+(u),e_T
\right)
-
\Phi(c^+(u),e_T).
\]

The restoration fraction is

\[
R_j(u)
=
\frac{\operatorname{Med}_j(u)}
{\Phi(c^- ,e_T)-\Phi(c^+(u),e_T)+\epsilon}.
\]

**Advantage:** exact output freezing and typed rollback remove the strongest current-quality and mediation confounds. It distinguishes the delivered answer from the post-answer write.

**Relationship to value:** \(\operatorname{CPE}\) is still a difference of continuation values. The novelty claim can only be that this intervention yields a cleaner estimand and a cheaper, more reliable prediction target in a partially observed agent harness.

### 10.4 Formalization D: local collision boundary

Let \(u\) parameterize a memory commit's content and retrieval metadata. Define local sensitivity

\[
J(u,u')
=
\frac{|\Phi(c^+(u),e)-\Phi(c^+(u'),e)|}
{d(u,u')+\epsilon}.
\]

A collision boundary exists empirically when there is a non-negligible set of pairs satisfying:

- the current output is identical;
- the committed text is identical or semantically near-identical;
- \(d(u,u')\) is in the lowest decile of natural commit variation;
- the pair straddles an operational boundary such as top-\(k\) retrieval, conflict resolution, permission activation, or dependency selection;
- \(|\Delta\Phi|\ge\kappa\);
- selective rollback or a state swap transfers the effect.

A robust boundary is not one hand-crafted tie. It must recur across episodes, seeds, models, and future-task resamplings.

**Advantage:** could support a counterintuitive mechanistic paper rather than another average benchmark gain.

**Risk:** discrete top-\(k\) systems are discontinuous by construction. The result is trivial unless the downstream option loss is broad, naturally prevalent, difficult for fair value baselines to predict, and not repaired by simple retrieval smoothing.

### 10.5 Why an additional formulation might still be scientifically useful

A generic value function is enough in an ideal fully observed MDP. The practical claim worth testing is narrower:

> The complete future-task value is too expensive to label, generic critics underfit rare persistent-state externalities, and a small set of typed counterfactual probes or commit-level influence features can estimate those externalities with substantially less compute and better out-of-distribution calibration.

This claim is falsifiable. If a compute-matched generic critic performs as well, the extra carrier formulation has no scientific purpose.

---

## 11. Exact counterintuitive hypotheses

The project must pre-register hypotheses and their negations. “Memory can be polluted” is not among them.

### H1 — Output-equivalent commits create a large future-capability gap

Among episodes with a byte-identical correct current answer,

\[
\max_{u,u'\in\mathcal U_{\text{benign}}}
|\Phi(u)-\Phi(u')|
\ge 0.15
\]

on both benchmark families and both model scales.

Here \(\mathcal U_{\text{benign}}\) excludes explicit attacks and knowingly false records. It may include literal records, truthful context-scoped reflections, duplicated records, and metadata changes.

**Falsifier:** the paired absolute gap is below 0.05 after strict matching, or appears only for explicit misinformation.

### H2 — Damage is mediated by the persistent carrier

For harmful commit \(u_h\), selective restoration of the implicated memory component recovers at least 75% of the future-success loss:

\[
R_j(u_h)\ge 0.75.
\]

Restoring an irrelevant state component or re-running from the same environment without memory restoration recovers at most 20%.

**Falsifier:** rollback does not recover performance, indicating current-task difficulty, model stochasticity, or another hidden state caused the gap.

### H3 — Naturally occurring small perturbations cross collision boundaries

For at least 10% of pre-registered near-boundary commit pairs, an identical-text or semantically negligible metadata perturbation causes at least a 20 percentage-point change in future success:

\[
\Pr\left[|\Delta\Phi|\ge0.20\mid d(u,u')\le\varepsilon\right]\ge0.10.
\]

**Falsifier:** large jumps occur only in manually manufactured exact ties, disappear under retrieval smoothing, or affect only the directly memorized fact.

### H4 — Present-task and generic impact metrics reverse the correct ranking

At least one high-current-efficiency commit policy is ranked above a safer policy by current reward, latency, or memory-size/state-distance metrics, but below it by oracle future capability. Across episodes, the best generic metric has pairwise ranking accuracy below 0.65.

**Falsifier:** answer confidence, memory size, semantic distance, retrieval KL, or a basic continuation critic already ranks states reliably.

### H5 — A cheap predictor beats a fair generic value baseline

A predictor that uses no test-time future-task rollouts achieves:

- AUROC \(\ge0.80\) for oracle damage labels;
- AUPRC materially above class prevalence;
- at least 0.10 absolute AUROC over the best compute- and data-matched generic value baseline;
- expected calibration error \(\le0.08\);
- retained performance under leave-one-task-family-out and cross-model transfer.

**Falsifier:** the advantage is below 0.05 AUROC, disappears after equalizing labels/parameters/forward passes, or fails cross-family evaluation.

### H6 — Targeted preservation is better than blanket conservatism

A selective commit policy must strictly improve the Pareto frontier over both “write everything” and “write nothing.” At a current-task or memory-utility loss of at most 2 percentage points, it should reduce future capability loss by at least 30% relative to the best non-selective baseline.

**Falsifier:** no-write is Pareto-optimal, or avoiding state change entirely gives equal future performance at lower cost.

### H7 — The effect is not merely future-distribution shift

The direction of damage must replicate in:

1. in-distribution future probes;
2. held-out task templates within the benchmark;
3. a second benchmark or task family;
4. multiple plausible reweightings of \(\mathcal D_F\).

**Falsifier:** the result exists only under one hand-picked future distribution or reverses under modest reweighting.

### H8 — Immediate efficiency can be anti-correlated with future capability

The strongest potentially surprising finding is:

> More compressed or more aggressively reusable memory commits improve immediate retrieval efficiency but reduce later capability by over-generalizing a locally correct experience.

This must be measured at matched current output and total inference budget. A statistically significant negative within-episode association between immediate efficiency and \(\Phi\), after controlling for record length and retrieval frequency, would be interesting.

**Falsifier:** efficiency and future capability are independent, or the association is wholly explained by prompt/token differences.

---

## 12. Causal interventions

| Intervention | What is held fixed | What changes | Causal question | Feasibility in memory | Feasibility in code |
|---|---|---|---|---:|---:|
| Post-output fork | Exact visible answer, pre-commit state, model seed | Only memory commit | Can state damage occur after a completed correct output? | **Exact** | Difficult; patch itself is usually the output |
| Carrier restore | Current answer and external environment | Restore selected memory record/index/metadata | Does restoring \(c\) restore future capability? | **Exact** | Only if agent-side memory is involved |
| Environment restore | Current answer and carrier | Reset external database/repository/workspace | Is the effect mediated by \(e\) rather than \(c\)? | Easy negative control | **Exact and central** |
| State swap | Same future tasks, policy, and budget | Swap post-task carrier states between matched episodes | Does damage transfer with the carrier? | **Exact** | Repository swap is possible but semantic matching is hard |
| Selective deletion | All other memory records and metadata | Remove one implicated record | Which component mediates the effect? | **Exact** | Hunk/file deletion may break current correctness |
| Metadata-only perturbation | Record text and answer | Salience, timestamp, namespace, embedding, top-\(k\) rank | Is there a collision boundary? | **Exact** | Dependency-resolution metadata is possible but expensive |
| Duplicate insertion | Record semantics | Multiplicity/retrieval competition | Can truthful redundancy degrade later behavior? | Easy | Duplicate code is confounded with maintainability |
| Reset versus persistent | Task sequence and model | Preserve or reset state between episodes | Is persistence necessary for the gap? | Established, easy | Established in chained benchmarks |
| Common-random-number replay | Future tasks and sampling seeds | Post-state only | Remove stochastic policy variance | Easy | Possible but agent trajectories remain long |
| Future-distribution resampling | Post-state | Task-family weights and held-out templates | Is the effect robust or arbitrary? | Easy | Moderate |
| Full rollback | Everything after current output | Restore full pre-commit snapshot | Upper bound on recoverable loss | Easy | May erase the delivered patch and thus invalidate current success |
| Selective rollback | Only predicted damaging state components | Preserve useful commits | Can preservation avoid excessive conservatism? | Easy | Hard; requires dependency-aware patch decomposition |

### 12.1 Required mediation pattern

The strongest admissible result has this structure:

1. \(y_T\) and current verifier results are identical.
2. Memory snapshots differ only in a declared record or metadata field.
3. The same future probes and random seeds produce different performance.
4. Swapping the record transfers the effect.
5. Deleting/restoring the record removes most of the effect.
6. Restoring unrelated state does not.
7. The result survives token/compute matching.

Anything weaker should be described as association, not causal carrier damage.

---

## 13. Three-to-seven-day falsification-first experiment

### 13.1 Objective

Test whether the narrow residual phenomenon exists **before** designing a new architecture:

> Can different post-output persistent-memory commits, made after the same correct answer, cause a large, broad, causally recoverable future-task gap that is missed by fair long-horizon value and generic state-change baselines?

The experiment is deliberately designed so that a clean negative result terminates the project.

### 13.2 Public benchmarks

Use exactly two primary benchmarks:

1. **[MemoryAgentBench](https://openreview.net/forum?id=DT7JyQC3MR)** — ICLR 2026, public code and data; provides incremental interactions and four memory competencies: retrieval, test-time learning, long-range understanding, and selective forgetting. citeturn820957search0turn820957search3
2. **[PAST-Bench](https://arxiv.org/abs/2608.04003)** — public 2026 preprint with 26 scenarios, 204 episodes, and persistence-on/off structure. citeturn290956search1

Use **LongMemEval-V2** only as a contingency if one primary benchmark lacks enough valid post-output fork points or has an evaluator failure rate above 5%. Do not silently add it after seeing results. Its public trajectories make it a defensible pre-registered replacement. citeturn778306search8turn778306search10

### 13.3 Models

Use two public open-weight dense models:

- **[Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)**;
- **[Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)**.

The Qwen3 family includes public 8B and 14B dense checkpoints and is documented in the official technical report. citeturn142990search0turn142990search1turn142990search2

Recommended serving:

- Qwen3-8B in BF16 on one RTX 4090 per replica;
- Qwen3-14B in BF16 with tensor parallelism over two RTX 4090s;
- vLLM or SGLang with fixed versions, deterministic kernels where available, and logged model hashes;
- maximum context 16k unless a benchmark instance requires more, in which case use one fixed 32k setting for all conditions.

Do not fine-tune the answer model in the killer experiment. A small critic or logistic model may be trained only after oracle labels are produced.

### 13.4 Experimental unit and exact current-task matching

For each benchmark episode:

1. Start from a canonical pre-task memory snapshot \(c^-_0\) and immutable environment snapshot \(e_0\).
2. Run the current task once with a fixed prompt, model, tool policy, and decoding seed.
3. Keep only episodes whose current answer passes the official evaluator.
4. Cache the answer bytes, current trace, token counts, log probabilities where available, and all tool/environment hashes.
5. Move the memory-write operation **after** the visible answer.
6. Fork the state into commit conditions while returning the same cached answer in every condition.

Thus:

\[
y_T^{(0)}=y_T^{(1)}=\cdots=y_T^{(K)}
\]

by construction, not merely by approximate score matching.

Any benchmark whose agent API cannot separate answer emission from persistence is unsuitable for the primary analysis; wrap it or replace it rather than weakening the intervention.

### 13.5 Memory substrate

Implement one transparent external store with versioned snapshots:

```text
record_id
content
provenance_episode
source_span
namespace
created_at
valid_from / valid_to
confidence
salience
embedding
supersedes
active
```

Use SQLite or immutable JSON for records and a deterministic FAISS or equivalent dense index. Every fork must have:

- a cryptographic hash of logical records;
- a hash of index inputs and configuration;
- a version identifier;
- a complete diff from the pre-commit state;
- exact restore and single-record delete operations.

Do not use an opaque production memory framework in the causal core. Framework-specific replications can follow later.

### 13.6 Commit conditions

Use six pre-registered post-output forks:

| ID | Commit | Purpose |
|---|---|---|
| U0 | **No write** | Blanket-conservatism and null-memory baseline |
| U1 | **Minimal literal record** extracted from canonical source spans | Low-impact, high-support reference |
| U2 | **Raw successful trace/transcript** within a fixed token cap | Common write-everything baseline |
| U3 | **Scoped reflection** generated from the successful trace and required to include provenance and explicit scope | Tests useful procedural compression |
| U4 | **Same U3 text, low retrieval leverage** through pre-registered salience/namespace metadata | Metadata-only matched pair |
| U5 | **Same U3 text, high retrieval leverage or one exact duplicate** | Tests retrieval amplification and collision behavior |

Primary claims must use only source-supported records. A write is admitted to the primary set when:

- every factual clause is entailed by a cited source span under the benchmark's canonical record;
- it contains no hidden instruction or adversarial string;
- two independent automated entailment checks agree, with a blinded manual audit of at least 20% of the test records;
- the scope field is preserved rather than deleted.

Stale, contradictory, malicious, or deliberately poisoned writes may be included as **secondary stress tests**, but cannot support the paper's core novelty claim.

### 13.7 Retrieval and collision intervention

Use a fixed hybrid retriever with:

- top-\(k=4\);
- fixed dense/BM25 mixing coefficient;
- fixed 512-token total memory budget;
- deterministic tie breaking;
- logged rank and score for every candidate record.

Two collision analyses must be separated:

1. **Natural prevalence analysis:** apply the same small metadata perturbation distribution to all eligible records without looking at future outcomes; estimate how often future capability changes sharply.
2. **Boundary stress test:** identify records near rank \(k\)/\(k+1\) using only the query and retrieval scores—not answer correctness—and move them across the boundary with the smallest logged perturbation. Report this as a stress test, not natural prevalence.

A smoothing baseline that retrieves a soft mixture or top-\(k+2\) set is mandatory. If smoothing removes the entire effect at negligible cost, the “collision” result is an implementation artifact rather than a general principle.

### 13.8 Future-task probes

After each commit, replay the same future tasks from the resulting memory snapshot. Pre-register four probe strata:

| Stratum | Question | Required role |
|---|---|---|
| In-distribution retention | Can the agent correctly use relevant persistent information? | Measures intended memory utility |
| Update/conflict | Can it replace stale information and respect temporal scope? | Detects contamination and over-persistence |
| Transfer/related tasks | Does a locally correct experience help or harm a related but non-identical task? | Tests non-transferability |
| Unrelated negative control | Does the write affect tasks that should not depend on it? | Tests broad collateral damage |

A fifth **held-out-family shift** stratum is used only in Stage 2. Future tasks must be assigned before running any commit condition. The same task order and stochastic seeds are used across paired states.

### 13.9 Oracle viability label

For episode \(i\), commit \(u\), probe stratum \(g\), and three paired decoding seeds,

\[
\widehat\Phi_{iug}
=
\frac{1}{3m_g}
\sum_{r=1}^{3}
\sum_{j=1}^{m_g}
S_{ijgr}(u).
\]

Define overall and robust scores:

\[
\widehat\Phi_{iu}
=
\sum_g w_g\widehat\Phi_{iug},
\qquad
\widehat\Phi^{\min}_{iu}
=
\min_g\widehat\Phi_{iug}.
\]

The primary damage label relative to U1 is

\[
L_{iu}=\mathbb 1
\left[
\widehat\Phi_{i,U1}-\widehat\Phi_{iu}\ge0.10
\right].
\]

The 0.10 threshold is for classifier labels; the project-level GO threshold is stricter.

Use the official exact match, F1, action-state, or benchmark-specific deterministic evaluator. LLM-as-judge scores are secondary and must be blinded to commit condition.

### 13.10 Required baselines

#### Current-output baselines

- current verifier success;
- exact output identity;
- current answer log probability;
- current task latency and token count;
- writer confidence and source-support score.

These should have little discriminative power after matching; if not, matching failed.

#### Memory-management baselines

- write everything/raw trace;
- write nothing;
- minimal literal facts;
- recency, salience, and relevance heuristics;
- a source-consistency gate inspired by ConsistencyGate;
- a future-utility/admission baseline inspired by ACL 2026 memory-distillation work;
- transaction/rollback baselines inspired by MemTX, MemTxn, and ChronoMem. citeturn917474search1turn917474search2turn917474search3turn820957search1turn820957search2

#### Generic state-change and impact baselines

- token edit distance and record count;
- embedding cosine/L2 distance from pre-commit memory;
- total retrieved-token change;
- retrieval-distribution Jensen–Shannon divergence over a calibration query set;
- output-logit KL on neutral calibration prompts;
- rollback cost;
- an AUP-like auxiliary-task score computed on a fixed random probe bank;
- retained retrieval/action-option count.

#### Long-horizon value baselines

At least two are mandatory:

1. **Generic learned critic:** a Qwen3-8B value head or small encoder trained on the same oracle labels, splits, state representation, and parameter/label budget as the proposed predictor. It receives the pre-state, candidate commit, and task-distribution descriptor and predicts \(\widehat\Phi\).
2. **Limited-rollout value:** estimate future value from \(r\) sampled calibration tasks, where \(r\) is chosen so its total GPU-seconds equal the proposed probe-based predictor.

A zero-shot LLM self-assessment may be reported but cannot be the strongest value baseline.

### 13.11 Prediction target without a complex architecture

The killer experiment should not introduce a new neural module. Evaluate a simple, auditable **commit-risk regressor** using:

- source-support and scope-specificity features;
- contradiction/update indicators against active memory;
- record length, duplication, and namespace features;
- retrieval leverage: frequency and rank margin over a fixed calibration query bank;
- change in action/output distributions on a small, disjoint calibration probe set;
- provenance diversity and temporal-validity features.

Use logistic regression, gradient-boosted trees, and a small MLP. The claim, if any, is about the estimand and mechanism, not architectural sophistication.

No test-set future probe or label may be queried at commit time.

### 13.12 Causal restoration and swapping

For every test episode classified as damaged:

1. **Delete implicated record only.** Re-run future probes.
2. **Restore metadata only.** Keep record text fixed.
3. **Restore full pre-commit memory.** Obtain recovery upper bound.
4. **Swap harmful record into the U1 state.** Test transfer of damage.
5. **Swap U1 record into the harmful state.** Test rescue.
6. **Restore environment only.** Confirm the environment was not the mediator.
7. **Re-run with memory retrieval disabled but the store intact.** Distinguish stored-state damage from retrieval activation.

### 13.13 Staging and stopping rules

#### Stage 0 — implementation smoke test

- 10 episodes;
- one model;
- all six forks;
- exact snapshot/restore tests;
- no scientific claims.

Stop immediately if state diffs show undeclared changes or official evaluators cannot be reproduced.

#### Stage 1 — two-GPU pilot, target completion by Day 3

- 80 current episodes total, balanced across the two benchmarks;
- Qwen3-8B;
- six commit states;
- eight future probes per episode;
- three paired decoding seeds.

Total future runs:

\[
80\times6\times8\times3=11{,}520.
\]

Proceed only if the Stage 1 thresholds in Section 17.2 are all met.

#### Stage 2 — confirmation, Days 4–7

- 160 held-out current episodes total;
- both Qwen3-8B and Qwen3-14B;
- six commit states;
- twelve future probes per episode;
- three paired decoding seeds;
- held-out task-family shift;
- full restoration and swap interventions on all damaged pairs.

Nominal future runs:

\[
160\times6\times12\times3\times2=69{,}120.
\]

Do not expand the architecture during this stage. The only permitted changes are bug fixes documented before unblinding confirmation results.

### 13.14 Statistical analysis

- Treat the **current episode**, not each future probe, as the primary independent unit.
- Use paired common-random-number comparisons across commit states.
- Report paired mean differences with 95% cluster-bootstrap confidence intervals over episodes.
- Use at least 10,000 bootstrap resamples.
- Fit a mixed-effects logistic model as a secondary analysis with random intercepts for episode and task family.
- Correct the pre-registered family of primary commit contrasts with Holm's method.
- Report both average success and worst-group/minimum-stratum success.
- Report all seeds, excluded episodes, evaluator failures, and missing outputs.
- Do not convert an ambiguous confidence interval into a positive result through post-hoc pooling.

### 13.15 Why this is a killer experiment

A negative result is decisive because it would establish one of the following:

- exact current matching removes the apparent phenomenon;
- damage is limited to explicit false/poisoned writes;
- generic value or simple memory heuristics already solve prediction;
- restoration does not mediate the effect;
- no-write is the correct conservative policy;
- discontinuities are rare implementation artifacts;
- results do not transfer across models or task families.

Any of these outcomes removes the remaining ICLR-level rationale.

---

## 14. Datasets, models, baselines, metrics, and compute estimates

### 14.1 Resource table

| Component | Primary choice | Why | License/public status consideration |
|---|---|---|---|
| Benchmark 1 | MemoryAgentBench | ICLR 2026; incremental memory competencies; public implementation | Verify current repository license and pin commit before running. citeturn820957search3 |
| Benchmark 2 | PAST-Bench | Explicit persistent-state episodes and matched persistence structure | 2026 preprint; archive exact data/version. citeturn290956search1 |
| Contingency | LongMemEval-V2 | Public longitudinal trajectories and questions | Use only under pre-registered replacement rule. citeturn778306search8turn778306search10 |
| Answer model A | Qwen3-8B | Strong open 8B model; one-GPU BF16 deployment | Pin official checkpoint revision. citeturn142990search0turn142990search1 |
| Answer model B | Qwen3-14B | Scale replication within 8×4090 | Use two-GPU BF16 TP or one documented quantization consistently. citeturn142990search2 |
| Dense retriever | One fixed open embedding model | Deterministic retrieval and score logging | Do not tune on test future queries. |
| Sparse retriever | BM25 | Transparent hybrid baseline | Fixed tokenizer and index. |
| Store | SQLite/JSON + FAISS | Exact versioning and selective restore | Release schema and diffs. |
| Predictor | Logistic regression, gradient boosting, small MLP | Minimizes architecture novelty claims | Same splits and labels as critics. |

### 14.2 Primary metrics

| Metric | Definition | Purpose |
|---|---|---|
| Exact current match | SHA-256 equality of delivered answer plus official pass | Removes present-output confounding |
| Future success \(\Phi\) | Mean official success across fixed future probes | Main capability outcome |
| Worst-group capability | Minimum success across probe strata | Detects option-family collapse |
| Tail capability | CVaR or lower quantile of episode-level future success | Detects rare large damage |
| Paired damage \(\Delta\Phi\) | U1 future success minus candidate future success | Main treatment effect |
| Restoration fraction \(R\) | Fraction of lost capability recovered after selective restore | Causal mediation |
| Collision prevalence | Share of small-perturbation pairs with \(|\Delta\Phi|\ge0.20\) | Tests discontinuity hypothesis |
| Ranking accuracy | Pairwise agreement/Kendall correlation with oracle state ranking | Tests current/value/state metrics |
| Predictor AUROC/AUPRC | Damage-label discrimination | Ex ante prediction |
| Calibration | Brier score and ECE | Decision reliability |
| Pareto frontier | Current utility, future capability, and compute | Detects over-conservatism |
| Compute | GPU-seconds, input/output tokens, calls, peak memory | Fairness and practicality |

### 14.3 Compute estimate

These are planning estimates, not guaranteed throughput claims; measure actual throughput during Stage 0 and publish it.

| Stage | Nominal workload | Estimated 4090 GPU-hours | Expected wall time |
|---|---:|---:|---:|
| Stage 0 | 10 episodes, six states, smoke probes | 5–15 | <1 day |
| Stage 1 | 11,520 future runs, Qwen3-8B | 80–200 | 1–3 days on 2 GPUs |
| Stage 2 | 69,120 future runs, 8B + 14B | 500–1,200 | roughly 3–6 days on 8 GPUs with batching |
| Small critics/predictors | Label reuse; no new oracle rollouts | 10–40 | <1 day |
| Full causal replays | Included for damaged test pairs; depends on prevalence | 50–200 additional | 0.5–2 days |

The upper range is more credible if contexts approach 16k–32k or tool simulations are slow. If Stage 0 projects more than 1,400 GPU-hours for Stage 2, reduce episode count according to a pre-registered power calculation; do not silently shorten future probes after seeing effects.

### 14.4 Minimal power logic

The primary analysis is paired at the episode level. Before confirmation, estimate the Stage 1 standard deviation \(s_d\) of paired damage differences and choose Stage 2 sample size for 90% power to detect a 0.10 absolute mean gap at two-sided \(\alpha=0.05\), capped by the compute budget. The pre-registered ICLR GO effect remains 0.15; powering at 0.10 prevents a noisy false negative while keeping the scientific threshold strict.

If the required sample exceeds the available 8×4090 budget, that is evidence against the desired “rapidly decisive” project profile.

---

## 15. Compute-fair comparison rules

These rules are binding. Violating any one invalidates the main comparison.

1. **Generate the current answer once.** Every commit condition returns the same cached bytes; no condition may re-reason about the current task.
2. **Post-output intervention only.** Memory writes occur after the answer and cannot feed back into current generation.
3. **Hash all state.** Pre-state, post-state, environment, retriever configuration, model checkpoint, and prompt templates receive immutable hashes.
4. **One declared state difference.** The primary U4–U5 pair changes only specified metadata or duplicate count; hidden caches and indexes must be rebuilt deterministically.
5. **Common future tasks.** Each paired state receives identical future task text, order, tool state, and random seeds.
6. **Equal future policy.** Same answer model, system prompt, retriever, top-\(k\), tool policy, max context, and output cap.
7. **Equal semantic memory budget.** Retrieved memory is capped at the same number of records and tokens. Batch padding may equalize GPU shape but must be attention-masked.
8. **Report realized compute.** Input tokens, output tokens, wall time, GPU-seconds, and model calls are reported per condition; a claimed gain may not hide extra rollouts.
9. **Match predictor compute.** A probe-based predictor and generic value baseline receive equal test-time GPU-seconds or equal model-forward-call budgets; report both normalizations if they disagree.
10. **Match supervision.** Critics and proposed predictors use the same oracle labels, train/validation/test split, task-family exclusions, and hyperparameter-search budget.
11. **No oracle leakage.** Test future probes, labels, answers, retrieval scores conditioned on their correct answer, and benchmark-specific hidden metadata cannot enter the commit predictor.
12. **Blind evaluators.** Any human or LLM judge sees only future output and rubric, not commit identity or hypothesis.
13. **Exact current quality audit.** Exclude any episode whose cached current answer is not accepted by the official evaluator; report exclusion rate by model and benchmark.
14. **No cherry-picked future distribution.** Fix probe strata and weights before outcomes. Report sensitivity over a declared simplex of alternative weights.
15. **No pseudo-replication.** Confidence intervals cluster by current episode; multiple probes and seeds are repeated measures.
16. **Same conservatism budget.** Compare selective commit policies at matched current-memory utility or write coverage, not against an unconstrained no-write policy only.
17. **Version-pin everything.** Model, tokenizer, serving engine, CUDA, benchmark, retriever, and evaluator revisions are archived.
18. **Release failed conditions.** Negative, timed-out, evaluator-error, and restoration-failure cases remain in the artifact with reason codes.

---

## 16. Positive, negative, and ambiguous outcomes

### 16.1 Positive outcome that reopens the project

All of the following occur:

- exact current outputs are identical;
- benign/source-supported commits yield a large future-task gap on both benchmarks and models;
- the gap affects transfer, update/conflict, or unrelated-control behavior—not only recall of the written fact;
- selective memory restoration recovers most of the loss and state swaps transfer it;
- generic value and state-change baselines mis-rank a substantial share of pairs;
- a low-cost predictor generalizes across task families and models;
- no-write is not Pareto-optimal;
- naturally occurring or minimally stressed collision boundaries are prevalent enough to matter.

**Interpretation:** reopen as a narrow causal memory-commit project. Do not claim a new theory of carrier viability.

### 16.2 Clean negative outcome

Any of the following is a useful project-ending result:

- paired gaps fall below 5 percentage points after exact matching;
- harmful effects require explicit falsehoods or adversarial triggers;
- damage is confined to the directly memorized fact;
- a generic continuation critic matches the specialized predictor;
- state distance or retrieval leverage explains the result;
- selective restore fails to recover capability;
- results disappear in the second model or benchmark;
- no-write dominates all selective policies;
- collision behavior vanishes under a simple smooth retriever.

**Interpretation:** archive the protocol and stop. The seed has collapsed into known memory management or ordinary value prediction.

### 16.3 Ambiguous outcomes and required resolution

| Ambiguous result | Most likely explanation | One allowed diagnostic | Decision if unresolved |
|---|---|---|---|
| Gap on one benchmark only | Benchmark-specific future distribution | Pre-registered contingency benchmark or leave-family-out test | NO-GO |
| Gap on 8B but not 14B | Model-specific fragility | Equalize current accuracy and retrieval behavior | NO-GO for general claim |
| Gap only for raw transcripts | Context-length/retrieval load | Token-matched minimal/raw comparison | Reclassify as context pollution |
| Gap only under high temperature | Sampling variance | Deterministic or lower-temperature paired replay | NO-GO if effect vanishes |
| Rollback partly recovers | Multiple hidden mediators | Full snapshot restore and component ablation | NO-GO if carrier mediation <75% |
| Predictor wins only with more calls | Added inference compute | GPU-second-matched value baseline | No method claim |
| Collision only at selected top-\(k\) ties | Constructed implementation artifact | Natural perturbation prevalence and soft retrieval | No general collision claim |
| Future shift causes the gap | Distribution mismatch | Separate in-distribution and shift strata | Reframe as memory robustness, not viability |
| Static metrics fail but value succeeds | State distance is weak, value is adequate | None needed | Broad carrier critic unnecessary |
| Positive mean, severe subgroup harm | Aggregation hides viability failure | Worst-group/CVaR analysis | Continue only if subgroup result is stable and pre-registered |

---

## 17. Binding GO/NO-GO thresholds

### 17.1 Non-negotiable validity checks

A result is invalid rather than merely negative if:

- current answer hashes differ across commit conditions;
- any undeclared environment or carrier component differs;
- official current evaluator outcomes differ;
- future tasks or seeds are not paired;
- restoration does not recreate the declared snapshot hash;
- test future probes leak into commit generation or predictor training;
- more than 5% of official future evaluations fail without a pre-registered missing-data rule.

### 17.2 Stage 1 continuation gate

Proceed from the two-GPU pilot to full confirmation only if all conditions hold:

1. At least 90% of selected episodes support exact post-output forks and reproducible restore.
2. The largest benign paired commit contrast has mean \(|\Delta\Phi|\ge0.10\).
3. Its 95% paired bootstrap interval excludes zero.
4. Full memory restore recovers at least 60% of the observed loss in the pilot.
5. The gap is not explained by input-token count: the token-matched estimate remains at least 0.08.
6. At least one generic current/state metric has a ranking reversal, but this alone is not enough.
7. No-write is not strictly better on both future success and compute for every episode family.

Failure of any condition ends the project without Stage 2.

### 17.3 Full project GO threshold

After Stage 2, the seed survives only if **all core conditions** and at least one **structural condition** hold.

#### Core conditions

1. **Replicated effect:** mean benign paired gap \(\ge0.15\) on each of two benchmarks and in both model scales, or a hierarchical pooled gap \(\ge0.15\) with no benchmark/model estimate below 0.10.
2. **Statistical certainty:** 95% paired cluster-bootstrap intervals exclude zero for both benchmarks; corrected \(p<0.05\) for primary contrasts.
3. **Causal recovery:** selective carrier restoration recovers \(\ge75\%\) of lost capability; irrelevant/environment-only restoration recovers \(\le20\%\).
4. **Broadness:** at least one non-direct stratum—transfer, update/conflict, or unrelated control—shows a gap \(\ge0.10\); direct recall alone is insufficient.
5. **Value-baseline failure:** best specialized predictor AUROC \(\ge0.80\), at least 0.10 above the strongest compute/data-matched generic value baseline, with ECE \(\le0.08\).
6. **Distribution robustness:** direction and at least two-thirds of magnitude survive leave-one-family-out, held-out templates, and reasonable future-task reweightings.
7. **Non-conservatism:** selective commit improves future loss by \(\ge30\%\) relative to the best non-selective baseline at \(\le2\) percentage-point current-memory-utility loss and \(<15\%\) inference overhead.
8. **State-change control:** effect remains after matching or conditioning on record length, memory size, semantic distance, retrieval count, and prompt tokens.

#### At least one structural condition

- **Collision:** at least 10% of natural near-boundary pairs show \(|\Delta\Phi|\ge0.20\), replicated across both models; or
- **Ranking reversal:** immediate efficiency/current utility is significantly negatively associated with future capability within matched episodes and reverses policy ranking; or
- **Probe compression:** eight or fewer disjoint calibration probes predict a 20-plus-probe oracle with AUROC \(\ge0.85\) across task families and models; or
- **Cross-substrate replication:** the same small-change/large-effect/restoration signature appears in a tightly controlled code or persistent-runbook setting.

### 17.4 Automatic NO-GO conditions

Stop and do not write an ICLR carrier-viability paper if any of these occurs:

- the best effect is below 0.10 after matching;
- the best fair generic value critic is within 0.05 AUROC of the proposed predictor;
- carrier restoration recovers below 50%;
- only adversarial or false memories produce damage;
- only one model or benchmark is positive;
- no-write is Pareto-optimal;
- the collision disappears with a trivial smooth-retrieval baseline;
- the future distribution must be tuned after seeing outcomes;
- current-task equivalence cannot be defended beyond a weak verifier.

These thresholds are intentionally severe. The literature collision is severe enough that merely obtaining a statistically significant effect is not a sufficient reason to continue.

---

## 18. Strongest reviewer attacks and the evidence required to survive

| Reviewer attack | Why the attack is valid | Evidence required for survival |
|---|---|---|
| **“This is just long-horizon planning.”** | Future-task success is a continuation value once the full state and task process are included. | Explicitly concede the in-principle equivalence. Show that a compute/data-matched critic systematically misses rare persistent-state effects, while a typed causal estimator generalizes across task families and models. Without that result, accept rejection. |
| **“This is standard safe RL or a CMDP.”** | Maximizing current success subject to \(\Phi\ge\tau\) is a constrained control problem. | Do not claim a new objective. Claim only a new identifiable estimand and measurement protocol in writable agent memory, with exact post-output interventions and public oracle probes. |
| **“This is attainable utility preservation or relative reachability.”** | Both explicitly preserve future options or attainable utilities. | Implement AUP-like auxiliary-task and reachability/option proxies. Show ranking failures after equal estimator capacity and compute, especially for small semantic changes with broad task loss. |
| **“This is catastrophic forgetting.”** | If \(c\) is model weights, it is exactly forgetting/interference. | Keep the primary carrier external and writable, restore it without changing weights, and show the effect transfers with the memory snapshot. Do not use parameter editing as a novelty domain. |
| **“This is just software maintainability or technical debt.”** | In code, current patches affecting later edits are standard maintainability, and 2026 benchmarks already measure it. | Treat code only as cross-substrate replication. Use executable paired downstream changes and avoid claiming code maintainability as the new concept. |
| **“Your future-task distribution is arbitrary.”** | Any state ranking can change when the future task weights change. | Use two public benchmarks, pre-register probe strata, report a full sensitivity analysis over plausible weights, include worst-group/CVaR scores, and perform leave-one-family-out and held-out-template evaluation. |
| **“The carrier state is vaguely defined.”** | The seed lists weights, memory, proof state, code, context, and tools as though interchangeable. | Provide a typed schema, persistence test, independent-intervention test, state hashes, and explicit exclusions. One paper should study one carrier, not a bag of metaphors. |
| **“Any sufficiently good value model already solves this.”** | Correct in principle. | Use the strongest fair critic possible, equalize labels, parameters, forward calls, and GPU-seconds, and report when it succeeds. The paper survives only with a large, robust predictive gap. |
| **“The result disappears if current-task quality is matched correctly.”** | Passing one verifier does not imply equal semantic correctness. | Freeze and replay the exact current answer. For memory, commit only after output. Audit answer hash and official score. In code replication, require full current tests plus behavioral equivalence probes and state this remains imperfect. |
| **“Your harmful policy simply makes larger state changes.”** | Memory size, tokens, or patch size may explain later difficulty. | Use identical-text metadata-only pairs, distance-matched samples, regressions controlling for token/record/retrieval counts, and generic state-distance baselines. |
| **“Future degradation is just distribution shift.”** | A locally useful write can fail on a changed task distribution without being intrinsically damaging. | Separate in-distribution, update/conflict, transfer, unrelated, and held-out strata. Show mediation and robust direction under reweighting. Describe shift-specific effects as robustness, not universal damage. |
| **“The benchmark is synthetic.”** | Hand-crafted forks and top-\(k\) ties can manufacture a phase transition. | Base episodes and future tasks on public natural interaction benchmarks, distinguish natural prevalence from boundary stress tests, release all construction code, and replicate at least one result in an unmodified benchmark workflow. |
| **“Your metric rewards excessive conservatism.”** | No-write or no-action can preserve options by refusing useful updates. | Plot the current-memory-utility–future-capability–compute frontier. Require a selective policy to beat both write-all and write-none at matched utility/coverage. |
| **“Rollback trivially solves the problem.”** | If all state can be restored cheaply, a predictor may be unnecessary. | Treat rollback as a causal instrument. Show that full rollback removes useful information or is incompatible with later tasks, and that selective commit/rollback improves the Pareto frontier. If full rollback is free and sufficient, there is no method paper. |
| **“Trajectory evaluation is unnecessary; endpoints suffice.”** | In a complete Markov state, future performance depends on the endpoint, not the path. | Agree. Use traces only to discover omitted persistent state or process violations. Do not claim history dependence after complete-state matching. |
| **“Your collision is just a top-\(k\) artifact.”** | Discrete retrieval creates obvious rank discontinuities. | Show natural prevalence, broad downstream option loss, cross-model replication, persistence under alternative retrievers, and non-trivial prediction failure. If soft retrieval fixes it, narrow the claim to brittle memory infrastructure. |
| **“The predictor gains come from extra inference compute.”** | Probe banks and counterfactual calls can approximate rollouts. | Match GPU-seconds and forward calls to limited-rollout value baselines; include zero-extra-call and equal-call results; charge all commit-time overhead to the method. |
| **“The effect is memory poisoning, not benign operation.”** | Explicitly false or adversarial records make later failure unsurprising. | Core analyses must use source-supported, non-adversarial commits with provenance and scope. Report attack/stale records only as stress tests. |
| **“Recent 2026 preprints already do this.”** | HarnessSafe, PAST-Bench, OEP, State Contamination, memory-management work, rollback, and transactions occupy most of the space. | A related-work matrix showing the exact missing intervention: byte-identical output, post-output source-supported commit, broad public future probes, component swap/restore, and fair value baselines. A missing combination alone is insufficient; the result must also be surprising. |
| **“The billiards metaphor adds no scientific content.”** | Correct. | Remove it from the paper. At most one sentence in motivation; preferably none. |

### 18.1 The strongest overall rejection paragraph

A skeptical ICLR reviewer could reasonably write:

> The paper observes that persistent state created during a successful task can affect later tasks. This is a direct instance of long-horizon value and negative side effects, with established formulations through future-task ability, attainable utility, reachability, viability, and constrained control. In LLM memory, recent work already studies locally correct harmful experiences, contamination, persistence-on/off counterfactuals, future-utility admission, rollback, and transactions. The proposed metric depends on an arbitrary future-task distribution, while the method is a specialized value estimator. Any effect from top-\(k\) retrieval is an implementation discontinuity, and no-write/rollback are obvious baselines. The paper therefore combines known ideas without a new principle.

The study survives only by experimentally defeating every substantive clause in that paragraph. At present, it has not done so.

---

## 19. Conditional 30-day plan if—and only if—the seed survives the pilot

This is not authorization to start a 30-day project now. It is the execution plan after all Stage 1 thresholds are met.

| Days | Work | Compute allocation | Required deliverable | Stop gate |
|---|---|---:|---|---|
| 1–3 | Implement typed store, post-output fork, exact hashes, two benchmarks; run Stage 0 and Stage 1 | 2 GPUs; ≤200 GPU-hours | Frozen protocol, pilot report, state-diff audit, paired CIs | Stop if any Section 17.2 condition fails |
| 4–7 | Run Stage 2 on 8B/14B, both benchmarks, all six commits, fixed probes/seeds | Up to 8 GPUs; 500–1,200 GPU-hours | Blinded confirmation table and raw artifacts | Stop if pooled gap <0.15, any model/benchmark <0.10, or restore <75% |
| 8–10 | Implement strongest generic value, AUP-like, state-distance, truth/relevance, and transaction baselines | 2–4 GPUs | Compute- and data-matched baseline audit | Stop if best value baseline is within 0.05 AUROC |
| 11–13 | Train simple commit-risk regressors; calibration and leave-family-out tests | 1–2 GPUs | AUROC/AUPRC/ECE, equal-compute curves | Stop if AUROC <0.80 or advantage <0.10 |
| 14–17 | Full causal interventions: delete, metadata restore, state swap, retrieval disable, environment negative control | 4–8 GPUs depending damaged-pair count | Mediation table and restoration fractions | Stop if selective carrier mediation <75% |
| 18–20 | Natural collision prevalence, boundary stress test, soft-retrieval baseline, future-distribution sensitivity | 4 GPUs | Collision and robustness report | Drop collision claim if smoothing or resampling removes effect |
| 21–23 | Conservatism/Pareto experiments: write-all, no-write, selective commit, full/selective rollback | 2–4 GPUs | Success–future-capability–compute frontier | Stop method claim if no-write remains Pareto-optimal |
| 24–26 | One secondary replication: either persistent runbook or a very small paired-code chain | 4–8 GPUs | Cross-substrate result or documented failure | Do not expand if semantic matching fails |
| 27–28 | Re-run all primary tables from clean environment; artifact release; external reproduction by a second operator | As needed | Reproducibility checksum and immutable result bundle | Stop submission if clean rerun changes main conclusion |
| 29–30 | Write paper with the narrow claim; adversarial internal review | Minimal | Submission draft, limitations, negative cases | Reject broad “carrier viability” framing |

### 19.1 Scope discipline during the 30 days

Forbidden expansions:

- inventing a billiards simulator;
- training a large new world model;
- adding theorem proving, model editing, and code merely to claim breadth;
- naming a new general framework before causal confirmation;
- replacing failed thresholds with post-hoc metrics;
- turning a negative result into a benchmark paper through cosmetic task generation;
- using closed frontier models as the only positive result.

Allowed expansion after a positive core result:

- one simple predictor;
- one soft-retrieval or transaction baseline;
- one secondary substrate replication;
- one formal sample-complexity or identifiability analysis directly tied to the estimator.

---

## 20. Publication and Oral-level bars

### 20.1 Minimum publishable result

A defensible workshop, Findings-style, or specialized-agent paper would require:

- exact post-output intervention and reproducible state snapshots;
- one public benchmark and at least two open models;
- a benign matched-output future gap of at least 0.10;
- selective rollback recovering at least 60%;
- a clear metric or audit protocol;
- a simple selective commit baseline improving future performance without catastrophic current utility loss;
- complete release of trajectories, states, and evaluators.

This level does **not** justify claiming a new general concept. It is a careful memory-management or agent-safety result.

### 20.2 Strong ICLR main-track result

A credible ICLR main-track paper would require all Section 17.3 core thresholds plus:

- two public benchmark families and two model scales;
- byte-identical current outputs and typed state mediation;
- broad damage beyond direct recall;
- failure of strong compute-matched value, AUP-like, and state-distance baselines;
- cross-family predictor generalization and calibrated risk estimates;
- a selective policy that improves the current-utility–future-capability–compute frontier;
- extensive negative cases showing when the effect does not occur;
- a claim limited to **post-output persistent-memory commit externalities**.

This would be a strong empirical-mechanistic paper, not a new theory of agency.

### 20.3 Plausible ICLR Oral-level result

Benchmark gains alone are nowhere near the bar. Oral plausibility would require a sharp general principle such as all of the following:

1. **Output equivalence:** byte-identical correct outputs hide a 20–30 percentage-point future-capability gap.
2. **Causal transfer:** swapping one small persistent-state component transfers the failure; selective restoration recovers at least 85–90%.
3. **Natural phase transition:** a reproducible collision boundary occurs in at least 15% of naturally near-boundary cases, not only hand-crafted ties.
4. **Baseline reversal:** current reward, state distance, relevance/truth gates, AUP-like auxiliary probes, and strong compute-matched value critics systematically rank important pairs incorrectly.
5. **Probe compression:** a tiny fixed probe set predicts broad 20-plus-task degradation with AUROC at least 0.88 and transfers across model families.
6. **Cross-domain replication:** the same causal signature appears in at least two genuinely different carriers/substrates—for example memory and repository/runbook state—with the same intervention logic.
7. **Pareto shift:** the method materially changes the success–compute–future-capability frontier rather than merely reducing writes.
8. **Structural explanation:** a mechanistic account predicts where the boundary occurs and is validated prospectively, not fitted after seeing failures.

Even with these results, Oral selection would remain uncertain because the foundational objective is old. Without cross-domain causal evidence and a genuine structural law, Oral potential is not credible.

### 20.4 Current probability assessment

These are subjective research-program estimates, not empirical frequencies:

| Outcome from the current seed | Estimated prior plausibility |
|---|---:|
| Clean Stage 1 phenomenon under exact matching | 20–35% |
| Survives all full GO thresholds | 5–15% |
| Strong ICLR main-track paper | <10% |
| Plausible Oral-level paper | <2% |

The main reason is not that the phenomenon is unlikely. It is that the **novel, baseline-resistant remainder** is small.

---

## 21. Relationship to operator-space expansion

### 21.1 Is the larger framework coherent?

The proposed sequence is logically coherent:

1. test whether the goal is reachable under base operators \(\mathcal A_0\);
2. expand to \(\mathcal A_1\supset\mathcal A_0\) if necessary;
3. evaluate the post-action persistent state;
4. choose an operator sequence that reaches the goal while satisfying a future-capability constraint.

A formal version is

\[
\max_{\tau\in\operatorname{Reach}(s_0,\mathcal A)}
\Pr[S_{\mathrm{cur}}(\tau)=1]
\quad\text{s.t.}\quad
\Phi(c_T(\tau),e_T(\tau))\ge\tau_F,
\]

with a cost for operator expansion.

That is scientifically coherent but not automatically novel. It is a planning problem with action-set expansion and a terminal constraint/value.

### 21.2 Recommended relationship

**Carrier viability should not be an independent paper in its present form.** Its best possible role is:

1. **first choice:** a downstream causal evaluation protocol for operator-expanded agents;
2. **second choice:** a constraint or risk estimate inside an operator-expansion method, if empirical evidence shows expanded operators create damage missed by ordinary value;
3. **not recommended:** a unified grand framework introduced before either component has an independent result.

### 21.3 Evidence required before combining directions

Combine only if all of the following are demonstrated:

1. A meaningful subset of tasks is genuinely unreachable under \(\mathcal A_0\) at a fixed compute budget.
2. Operator expansion materially raises current-task success.
3. Among expanded-operator trajectories with matched current success, future capability differs substantially.
4. The difference is mediated by a typed persistent carrier/environment component.
5. A standard long-horizon value model, safe planner, AUP-like penalty, and generic state-distance baseline fail to rank those trajectories.
6. A carrier-specific estimator improves the joint current-success–compute–future-capability frontier.
7. The joint method outperforms a two-stage baseline that first expands operators and then applies an existing safety/transaction mechanism.

If conditions 3–6 fail, carrier evaluation adds no scientific value. If conditions 1–2 fail, operator expansion adds no value. If both components work independently but their interaction is additive, write separate papers rather than force unification.

### 21.4 Final classification

| Possible role | Decision |
|---|---|
| Independent “Post-Success Carrier Viability” paper | **Reject** |
| Constraint within operator-space expansion | **Conditional, after evidence** |
| Downstream evaluation protocol | **Most defensible role** |
| Grand unified framework now | **Reject** |

---

## 22. Final recommendation on the 8×4090 cluster

### 22.1 Binding recommendation

**Do not invest the full 8×RTX 4090 cluster in this seed as currently framed.**

The broad concept fails the novelty test. The formal objective is established, and the clean concrete domains are unusually crowded as of August 2026. A full project would have a high probability of producing a technically competent but conceptually redundant paper.

Authorize only the following:

- **2 GPUs**;
- **maximum 3 days**;
- **maximum 150–200 GPU-hours**;
- the exact Stage 1 post-output memory audit;
- no new architecture;
- automatic termination unless every Section 17.2 threshold is met.

If the pilot passes, a separate decision may authorize Stage 2 on all eight GPUs. Passing Stage 1 is not evidence that “carrier viability” is novel; it merely establishes that the narrow residual deserves confirmation.

### 22.2 Paper framing if the unlikely positive case occurs

Use a title and claim centered on the actual estimand, for example:

> **Causal Externalities of Post-Output Memory Commits in Stateful LLM Agents**

The paper should say:

- future capability is a continuation-value concept;
- existing side-effect and memory work motivates the problem;
- the contribution is an exact intervention and an unexpected empirical mechanism;
- rollback is a causal tool and baseline;
- the result applies to the tested persistent-memory systems, not all AI capability carriers.

Do not say:

- “we introduce carrier viability”;
- “existing agents evaluate only immediate success”;
- “no prior work studies future capability after successful actions”;
- “proof states, codebases, weights, memory, and context are one unified phenomenon”;
- “the billiards insight creates a new theory.”

### 22.3 Final decision table

| Question | Answer |
|---|---|
| Is the motivating phenomenon real? | **Yes** |
| Is the broad formulation novel? | **No** |
| Is it distinct from long-horizon value in principle? | **No** |
| Is it distinct from safe RL/CMDPs/viability at the objective level? | **No** |
| Are model editing and continual learning viable primary domains? | **No** |
| Are theorem proving and test-time reasoning viable primary domains? | **No** |
| Is sequential code clean enough and novel enough for the first experiment? | **No** |
| Is persistent memory causally clean? | **Yes** |
| Is persistent memory uncrowded? | **No** |
| Does a narrow post-output causal residual remain? | **Possibly** |
| Should the full cluster be invested now? | **No** |
| Should a tightly capped falsification audit be run? | **Yes** |
| Current executive verdict | **NO-GO** |

### 22.4 Bottom line

The seed identifies an important engineering and evaluation concern, but not a new general AI research problem. The literature already contains its formal core and most natural instantiations. The only rational investment is a small attempt to falsify the narrowest remaining causal claim. Unless that audit reveals a large, recoverable, baseline-resistant, and preferably discontinuous effect under exact current-output matching, the project should end.
