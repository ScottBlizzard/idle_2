# AI_RESEARCH_REACHABILITY_EXPANSION

> **Repository status:** Historical adversarial audit; retained as a binding negative result.
> **Literature cutoff:** 25 August 2026  
> **Executive verdict:** **PIVOT**  
> **Broad seed:** **NO-GO as a paper claim**  
> **Narrow residual:** **Authorize one tightly capped 3–7 day falsification sprint**

---

## 1. Executive verdict

### 1.1 Decision

**PIVOT.** The broad proposal—*recognize that current inference operators are insufficient, then selectively add a tool, subgoal, lemma, representation, planning mechanism, or control dimension*—is not a novel research contribution. Once operator choice is admitted as a meta-action, the proposal reduces to a familiar combination of rational metareasoning, algorithm selection, value of computation, hierarchical planning, adaptive tool use, decomposition, and test-time compute allocation. Options already treat temporally extended procedures as actions; rational metareasoning already asks which computation or algorithm to invoke; recent LLM work already learns when to reason, decompose, call tools, switch representations, restart, or spend more inference compute. citeturn581877search1turn422412search0turn422412search1turn422412search6turn422412search3turn665878search30

The idea becomes scientifically defensible only after a severe narrowing:

> **Do standard proof-progress or value models systematically mis-rank a structurally necessary lemma/cut introduction because it initially looks like negative progress, thereby pruning the only short proof available under a fixed compute budget?**

I will use **Cut-Induced Progress Inversion (CIPI)** as an internal label. The label is disposable; the phenomenon is the proposed contribution. A paper should not be marketed as “reachability expansion,” and the billiards analogy should disappear after one motivation sentence.

The residual is interesting because it is not merely “lemmas help.” A valid result would have to establish all of the following:

1. A useful lemma/cut initially increases open goals, proof-state size, predicted remaining steps, or another conventional difficulty signal.
2. A standard local progress/value estimator therefore scores it below a superficially simplifying alternative.
3. That ranking causes a **causal search failure** under a fixed token, node, verifier-call, and wall-clock budget.
4. More sampling, wider beam search, MCTS, and diversity from the original proof policy do not close the gap at matched cost.
5. A selector that predicts **counterfactual operator advantage**, rather than generic problem difficulty, activates lemma/cut search only when useful and beats both always-expand and never-expand.
6. The effect transfers from a controlled proof system with exact labels to natural Lean proofs.

This is a **conditional scientific bet**, not a positive finding. The literature already establishes that reusable lemmas, hierarchical proof decomposition, and proof DAGs can shorten or statistically simplify proof generation. Most importantly, a 2026 theory paper models theorem proving as finite-horizon reachability and proves an exponential sample-complexity separation between flat learners trained on inlined proof trees and hierarchical learners that predict reusable proof DAGs. citeturn224444search0 Therefore the residual cannot be “cuts expand reachability” or “hierarchy helps.” It must be a **previously undocumented estimator failure, a pre-failure diagnosis criterion, and a compute-fair causal intervention**.

### 1.2 Verdict hierarchy

| Scope | Verdict | Reason |
|---|---:|---|
| “AI should expand its operator set when stuck.” | **NO-GO** | Existing metareasoning and hierarchical-control formalisms already express it. |
| “Adaptive tool/decomposition/representation routing improves accuracy–cost.” | **NO-GO** | Crowded in 2024–2026; this is ordinary routing or value of computation. |
| “Auxiliary lemmas make difficult formal proofs easier.” | **NO-GO** | Directly occupied by lemma generation, theorem extraction, growing libraries, recursive decomposition, and cut-aware theory. |
| “Local proof-progress models exhibit a reproducible structural-detour blind spot around reusable cuts.” | **CONDITIONAL GO** | I did not find a primary-source paper that jointly certifies the bounded cut/no-cut gap, measures the score inversion, demonstrates causal pruning, controls compute/diversity, and learns a pre-failure advantage selector. |
| Full 30-day project | **DO NOT AUTHORIZE YET** | Unlock only after the staged 7-day gates in §15 pass. |

### 1.3 Confidence and stop-loss

These are research judgments, not measured probabilities:

- Broad formulation already occupied: **0.95**.
- A synthetic CIPI effect can be created: **0.85**.
- The effect survives non-tautological controlled experiments: **0.55–0.65**.
- It transfers to natural Lean proof search: **0.30–0.40**.
- Conditional on transfer, a strong ICLR main-track paper is plausible: **0.20–0.30**.
- Oral-level outcome before any evidence: **well below 0.10**.

**Cluster decision:** spend at most one staged week. Do not spend a month merely building another agentic theorem prover.

---

## 2. Strongest non-metaphorical formulation of the seed

Let an inference system have a current policy, an operationally enabled operator family, a verifier, and a finite resource budget. The scientific object is not logical solvability in the abstract; it is **success under a declared policy, operator set, representation, verifier, and cost cap**.

For instance $x$, state $s$, verifier $V$, operator family $\mathcal O$, policy $\pi$, and cost budget $B$, define

$$
p_{\pi,\mathcal O}(x,B)
=
\Pr\!\left[V(\tau)=1\;\middle|\;\tau\sim\pi(\cdot\mid x,\mathcal O),\;c(\tau)\le B\right].
$$

For an expansion $j$ with policy/operator pair $(\pi_j,\mathcal O_j)$, define its fixed-budget advantage

$$
\Delta_{\mathrm{op},j}(x;B)
=
p_{\pi_j,\mathcal O_j}(x,B)-p_{\pi_0,\mathcal O_0}(x,B),
$$

and the return from merely scaling the base search by factor $\kappa>1$:

$$
\Delta_{\mathrm{search}}(x;B,\kappa)
=
p_{\pi_0,\mathcal O_0}(x,\kappa B)-p_{\pi_0,\mathcal O_0}(x,B).
$$

A defensible empirical **operator-relative bounded deficit** requires preregistered thresholds $\delta>\epsilon$ such that

$$
\exists j:
\Delta_{\mathrm{op},j}(x;B)\ge\delta,
\qquad
\Delta_{\mathrm{search}}(x;B,\kappa)\le\epsilon,
$$

and the result must survive sham-operator, semantic-diversity, stronger-search, and compute-matched controls.

The model should not predict a vague binary “unreachable.” It should estimate a vector of **counterfactual marginal advantages**:

$$
A_j(x,B)
=
p_{\pi_j,\mathcal O_j}(x,B-c_j)
-p_{\pi_0,\mathcal O_0}(x,B),
$$

then select

$$
j^*(x,B)
=
\arg\max_{j\in\{0,\ldots,m\}}
\left[
\widehat p_j(x,B-c_j)
-\lambda c_j
-\mu C_{\mathrm{struct}}(j)
-\nu U_j(x)
\right],
$$

where $c_j$ is measured inference cost, $C_{\mathrm{struct}}$ is any application-specific expansion penalty, and $U_j$ is calibrated uncertainty.

This is the strongest general formulation—but it is also almost exactly a rational metareasoning or algorithm-selection objective. The formulation alone is therefore **not a contribution**. citeturn422412search0turn422412search1turn422412search5

### 2.1 The surviving specialization: proof-DAG construction under biased progress estimates

In formal proof search, let $\mathcal P_0$ be a flat proof policy that does not create separately solved, reusable intermediate lemmas, and let $\mathcal P_1$ permit one explicit reusable lemma/cut. Define shortest verified proof costs

$$
L_k(x)=\min_{\tau:V(\tau)=1,\;\tau\in\mathcal P_k} c(\tau),
$$

and a **cut-compression ratio**

$$
\rho(x)=\frac{L_0(x)}{L_1(x)}
\qquad\text{or}\qquad
\log\rho(x)=\log L_0(x)-\log L_1(x).
$$

For natural Lean, $L_0$ is generally unidentifiable because unobserved proofs may exist. In a finite proof DSL or bounded sequent calculus, it can be exhaustively computed or tightly bounded.

The proposed mechanism is a ranking inversion at the transition that introduces a useful lemma $\ell$:

$$
\widehat v(s\xrightarrow{\mathrm{introduce}\;\ell}s_{\ell})
<
\widehat v(s\xrightarrow{\mathrm{local\ simplify}}s_{\mathrm{local}}),
$$

while the true fixed-budget continuation success satisfies

$$
\Pr(\mathrm{success}\mid s_{\ell},B)
\gg
\Pr(\mathrm{success}\mid s_{\mathrm{local}},B).
$$

The strongest counterfactual hypothesis is:

> **Progress estimators trained primarily on successful flat traces undervalue reusable proof-DAG construction; as subproof reuse grows, this induces a predictable phase transition where locally “better” search is globally worse under fixed compute.**

### 2.2 Explicit non-claims

The project must not claim:

- that Lean theorems are mathematically unprovable without `have`, `suffices`, or auxiliary lemmas;
- that a tactic absent from a prompt is absent from Lean’s logic;
- that low pass@$k$ proves unreachability;
- that a longer prompt, more generated tokens, or more verifier calls changed reachability;
- that a generated subgoal is a new scientific operator merely because it has a new name;
- that a proof planner is novel because it “moves away from the goal”;
- that the billiards metaphor establishes a theorem, algorithm, or benchmark.

In natural Lean, the honest claim is **policy-relative, representation-relative, and budget-relative operational reachability**. Only the controlled finite calculus may support certified $B$-unreachability.

---

## 3. What changed relative to ordinary future-value reasoning

### 3.1 The useful distinction

Ordinary object-level value reasoning asks which currently available action best improves expected future return under a fixed state/action model:

$$
V(s)=\max_{a\in\mathcal A(s)}
\mathbb E\left[r(s,a,s')+\gamma V(s')\right].
$$

The seed appears to add a qualitatively different move: change $\mathcal A$, the representation, the transition generator, or the search graph itself. This distinction is useful for experimental bookkeeping because it separates:

- search depth or width within a fixed graph;
- policy diversity within a fixed graph;
- edge addition or state lifting that changes the operational graph;
- external information supplied by a tool;
- proof compression and reuse that change finite proof cost without changing logical provability.

### 3.2 Why the distinction does not create new theory

Augment the meta-state to

$$
z=(s,\mathcal O,b,h),
$$

where $b$ is remaining budget and $h$ is search history. Add meta-actions such as `continue`, `restart`, `invoke tool`, `introduce lemma`, `switch representation`, and `increase beam`. The operator-expansion problem is then an ordinary semi-Markov decision process over $z$, with expansion costs and delayed rewards. Options already formalize temporally extended actions; algorithm selection by rational metareasoning already chooses among specialized procedures; modern LLM methods already learn when to reason, decompose, or spend more test-time compute. citeturn581877search1turn422412search0turn422412search1turn422412search6turn422412search3

Therefore:

> **“The agent changes its reachable set” is an interpretation, not a novelty claim.**

A publishable residual must reveal something that the generic meta-MDP description does not provide for free. CIPI proposes one such possibility: a **systematic estimator misspecification** caused by local progress labels and proof-tree representations that fail to value future subproof reuse.

### 3.3 What would actually be new

At least one—and preferably three—of the following must be demonstrated:

1. **Failure mode:** standard progress/value models consistently mis-rank structurally necessary detours.
2. **Structural criterion:** a measurable reuse or bottleneck statistic predicts when the failure appears.
3. **Causal intervention:** adding the cut changes the fixed-budget solve frontier after compute and diversity are controlled.
4. **Lower bound:** a class of local progress estimators must fail on a constructed family.
5. **Cross-domain invariance:** the same diagnostic predicts gains in Lean and verified code or program synthesis.
6. **Adaptive frontier shift:** a cheap selector beats never-expand, always-expand, and strong search on the same cost axis.

Without such evidence, the work is ordinary future-value reasoning with new terminology.

---

## 4. Taxonomy of direct reachability, tolerance exploitation, dynamics modification, and lifted reachability

| Level | Operational definition | AI analogue | Closest established field | Novelty status |
|---|---|---|---|---:|
| **A. Direct reachability** | A verified trajectory is available under the current policy/operator family and budget; the problem is finding it. | Better tactic, branch, token sequence, action, or plan. | Bellman value, heuristic search, beam/MCTS, best-of-$N$, verifier-guided search. | **Occupied** |
| **B. Tolerance exploitation** | Multiple actions satisfy the current acceptance constraint but induce different future states. | Among currently correct partial answers or test-passing patches, choose one with better downstream proofability, robustness, editability, or option value. | Constrained MDPs, viability, empowerment, robust planning, future-value optimization. | **Coherent, not novel by itself** |
| **C. Dynamics modification** | An enabled control changes transition dynamics or uncertainty. | Invoke a tool, compiler, solver, execution mode, retrieval source, or calibrated environment model with context-dependent errors. | Model-based/robust RL, system identification, active inference, tool routing. | **Occupied** |
| **D. Lifted reachability** | A meta-action adds states/edges, changes representation, permits subgoals, or compresses repeated structure. | Lemma/cut, helper function, abstraction, latent mode, backward reasoning, library invention, option, temporary refactor. | Hierarchical RL, decomposition, program synthesis, theorem proving, representation switching, homotopy. | **Heavily occupied** |
| **D\*. Structural-detour blindness** | The expanded route is operationally superior, but local progress/value scores prune its first step because that step initially looks worse. | Useful cut opens a lemma goal; reusable abstraction initially increases burden; downstream proof DAG becomes much smaller. | Adjacent to proof progress, decomposition, and cut theory; the exact causal package appears open. | **Residual candidate** |

### 4.1 Tolerance as a constrained continuation problem

Let the current task admit an acceptance set

$$
\mathcal A_\tau(s)
=
\left\{a:
\Pr(\text{current acceptance}\mid s,a)\ge\tau
\right\}.
$$

“Cheating the pocket” becomes

$$
\max_{a\in\mathcal A_\tau(s)} K(T(s,a)),
$$

where $K$ measures downstream controllability, viability, expected value, or future solution volume. Empowerment already quantifies potential influence over future states, affordance work studies state-dependent available actions, and reachability-constrained control characterizes feasible sets. citeturn429357search5turn429357search3turn566917search5

This can inspire useful engineering—for example, selecting among extensionally correct programs by future proofability—but it is not presently the best primary paper. P³ already shows that two seemingly acceptable implementation choices can induce radically different proof obligations and improves verified-code generation through joint program-and-proof planning. citeturn885201search1

### 4.2 Dynamics-changing controls and uncertainty

An auxiliary control may expand capability while introducing context-specific error. Formally, the transition kernel becomes $P_j(s'\mid s,a,\theta_j)$ with uncertain $\theta_j$. A robust objective could be

$$
\max_j\ \inf_{P\in\mathcal U_j}
\Pr_P(G\mid s,\mathcal O_j,B)-\lambda c_j.
$$

This is sensible but belongs to robust metareasoning/model-based control, not a new principle. Reachability-constrained RL and viability-style safety measures already cover the core geometry of feasible future sets. citeturn566917search5turn566917search2

### 4.3 Lifted reachability versus mere sampling

An expansion counts as scientifically meaningful only if it survives these tests:

- **Normalized-proof test:** after compiling outputs to a common proof representation, does the expanded route contain a reusable construct absent from the declared base search policy?
- **Equal-diversity test:** does matched semantic diversity from the base policy reproduce the gain?
- **Inlining test:** if the lemma is inlined or cross-branch memoization is disabled, does proof cost or success collapse?
- **Sham-expansion test:** does an equal-cost but nonfunctional expansion fail?
- **Search-scaling test:** does a much larger same-policy budget remain behind?
- **Oracle-minimality test:** is the smallest useful expansion identifiable, or does “enable everything” dominate?

These tests define the proposed project’s evidentiary bar.

---
## 5. Verified literature map with direct links

### 5.1 Search protocol and coverage audit

The search was repeated with both seed-friendly and seed-hostile queries. The hostile queries included combinations such as *operator insufficiency*, *search insufficiency*, *adaptive decomposition*, *strategy selection*, *value of computation*, *cut introduction*, *auxiliary lemma*, *proof progress*, *proof DAG*, *representation switching*, *tool routing*, *library learning*, *proof refactoring*, *lookahead constrained decoding*, and *policy-space expansion*. Primary conference pages, proceedings, arXiv abstracts/HTML, and official repositories were preferred. Papers found only through titles or snippets were not treated as verified contributions.

The search found no defensible novelty in the broad formulation. The following coverage table records the collision result across every mandatory area.

| Mandatory collision area | Representative verified sources | Adversarial conclusion |
|---|---|---|
| Bellman value and classical planning | Options framework; rational metareasoning; Tree of Thoughts. citeturn581877search1turn422412search0turn585552search0 | Operator choice can be made a meta-action; “future reachability” alone is not new. |
| Reachability and controllability | Reachability-constrained RL; learnable safety measures; affordances; empowerment. citeturn566917search5turn566917search2turn429357search3turn429357search5 | Levels A–C have mature control interpretations. |
| Constrained, robust, and risk-sensitive control | RCRL and robust peak-cost CRL. citeturn566917search5turn566917academia8 | Capability–uncertainty tradeoffs are established robust-control objectives. |
| Empowerment | Klyubin, Polani & Nehaniv. citeturn429357search5 | “Preserve or enlarge future control” is already a named information-theoretic objective. |
| Option discovery and hierarchical RL | Sutton, Precup & Singh. citeturn581877search1 | New macro-operators and temporally extended actions are standard. |
| Curriculum learning | Goedel-Prover-V2 scaffolded synthesis; LeanAgent curriculum. citeturn690539search0turn885201search34 | Easier-to-harder operator acquisition is crowded. |
| Adaptive computation | Rational metareasoning for LLMs; compute-optimal test-time scaling. citeturn422412search1turn422412search6 | “Use more reasoning only when needed” is directly occupied. |
| Tree search, MCTS, beam, best-of-$N$ | Tree of Thoughts; Snell et al.; Goedel-Prover-V2. citeturn585552search0turn422412search6turn690539search0 | Any gain must survive much stronger same-operator search. |
| Process reward and value models | Let’s Verify Step by Step; LeanProgress. citeturn585552search3turn758754search0 | These are the most important baselines and the suspected failure locus. |
| Verifier-guided reasoning | Goedel-Prover-V2 self-correction; Lean compiler feedback in LEAP and P³. citeturn690539search0turn224444search3turn885201search1 | Exact verification does not itself create novelty. |
| Tool use and tool routing | ReAct and Toolformer. citeturn585552search5turn585552search2 | “Call a tool when direct reasoning fails” is plainly occupied. |
| Representation learning/switching | Coconut, SwiReasoning, DyLaR, activation steering. citeturn665878search0turn665878search30turn665878search34turn665878search16 | Dynamic explicit/latent mode switching is already an active 2026 topic. |
| Latent planning | Coconut and Diffuser. citeturn665878search0turn876779search0 | Lifted or continuous trajectory generation is established. |
| Activation steering | Activation engineering and conditional steering. citeturn665878search2turn665878search23 | Extra inference controls are not new operators by themselves. |
| Auxiliary variables, abstraction, and library learning | DreamCoder, ReGAL, REFACTOR, LEGO-Prover, DreamProver. citeturn299529search0turn299529search1turn758754search2turn758754search1turn885201search0 | The core “invent reusable intermediate structure” idea is heavily occupied. |
| Decomposition and subgoal generation | ADaPT, DeepSeek-Prover-V2, Prover Agent, Quarry, LEAP. citeturn422412search3turn758754search3turn885201search3turn224444search1turn224444search3 | Generic adaptive decomposition is a NO-GO. |
| Self-refinement and reflection | Self-Refine and Reflexion. citeturn703381search0turn703381search1 | Iterative critique, retry, and memory-conditioned reattempts already provide indirect improvement trajectories. |
| Lemma invention | REFACTOR, hierarchical proof training, Prover Agent, Quarry. citeturn758754search2turn885201search6turn885201search3turn224444search1 | “Auxiliary lemmas help” is not residual novelty. |
| Backward reasoning | Forward–backward verification and explicit backward-reasoning studies. citeturn703381search10turn703381search22 | Reasoning from a candidate goal or conclusion toward missing premises is already an established transformation. |
| Program synthesis and search-space expansion | DreamCoder, ReGAL, PlanSearch. citeturn299529search0turn299529search1turn299529search14 | DSL/library expansion and plan-space search are established. |
| Diverse decoding and solution diversity | PlanSearch, model averaging in Goedel-Prover-V2, PSRO diversity work. citeturn299529search14turn690539search0turn876779search3 | Diversity is a mandatory alternative explanation. |
| Constrained decoding | NeuroLogic and NeuroLogic A*esque. citeturn665878search9turn876779search1 | Changing decoding connectivity under constraints is already well studied. |
| Diffusion guidance and trajectory control | Diffuser and conditional diffusion planning. citeturn876779search0turn876779search15 | “Move through a lifted trajectory space and project back” is not new. |
| Affordance learning | Khetarpal et al. citeturn429357search3 | Operator availability conditioned on state is established. |
| Model-based RL, system identification, and online calibration | Neural ODE/SDE dynamics models for adaptation and planning; continual model-based control under time-varying dynamics. citeturn155917search1turn155917search2 | Updating a transition model or calibrating dynamics before planning is established uncertainty-aware control. |
| Active inference | Active-inference formulations connect action selection, inference, preferences, and free-energy objectives. citeturn541706search25 | “Act or probe to reduce model uncertainty before pursuing the goal” is not a new operator-expansion principle. |
| Multi-agent strategy expansion | PSRO and response-diversity work. citeturn876779search2turn876779search3 | Iteratively adding strategies against an opponent is a canonical double-oracle pattern. |
| Continuation and homotopy | Continuation Path Learning. citeturn566917search3 | “Solve a transformed/easier problem and continue back” is established. |

**Bibliographic convention:** long author lists are abbreviated with “et al.” in the tables; the linked primary page gives the complete official list. 2026 arXiv papers are treated as preprints unless a primary venue page confirms acceptance.

### 5.2 Foundations and generic adaptive inference

| Paper | Authors; year; venue | Actual contribution | Seed portion already covered | Residual, if any |
|---|---|---|---|---|
| [**Dynamic Programming**](https://books.google.com/books/about/Dynamic_Programming.html?id=rZW4ugAACAAJ) | Richard Bellman; 1957; Princeton University Press | Establishes dynamic programming for multistage decisions and the recursive future-value viewpoint underlying Bellman optimality. citeturn569168search3 | Choosing an action for its downstream consequences under a fixed state/action model. | Operator expansion must add more than a restated value function. |
| [**Principles of Metareasoning**](https://www.sciencedirect.com/science/article/pii/000437029190015C) | Stuart Russell, Eric Wefald; 1991; *Artificial Intelligence* | Develops resource-bounded rational control of reasoning by evaluating computations at a metalevel. citeturn690268view14turn728371search3 | Decide whether and which computation to perform before acting. | Only a specific failure of metalevel value estimation. |
| [**Selecting Computations: Theory and Applications**](https://arxiv.org/abs/1207.5879) | Nicholas Hay, Stuart Russell, David Tolpin, Solomon Eyal Shimony; 2012; UAI | Gives a Bayesian theory and approximations for selecting simulations by expected improvement in decision quality. citeturn728371search2turn728371academia30 | Allocate finite search to the computation with highest expected benefit. | A new structural counterexample or estimator limitation, not the objective. |
| [**Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning**](https://www.sciencedirect.com/science/article/pii/S0004370299000521) | Richard S. Sutton, Doina Precup, Satinder Singh; 1999; *Artificial Intelligence* | Introduces options as temporally extended actions usable in planning and learning. citeturn581877search1 | Adding a macro-action, subpolicy, or extended operator. | None at the general level. |
| [**Empowerment: A Universal Agent-Centric Measure of Control**](https://researchprofiles.herts.ac.uk/en/publications/empowerment-a-universal-agent-centric-measure-of-control/) | Alexander S. Klyubin, Daniel Polani, Chrystopher L. Nehaniv; 2005; IEEE CEC | Measures an agent’s potential influence over future states using channel capacity. citeturn429357search5 | Exchanging current slack for downstream controllability. | A verifier-grounded analogue may be useful, not novel as a principle. |
| [**Algorithm Selection by Rational Metareasoning as a Model of Human Strategy Selection**](https://proceedings.neurips.cc/paper_files/paper/2014/hash/87b5e7e570f757a0b99f0a370ce2438c-Abstract.html) | Falk Lieder, Dillon Plunkett, Jessica Hamrick, Stuart Russell, Nicholas Hay, Thomas Griffiths; 2014; NeurIPS | Frames choosing among specialized algorithms as rational metareasoning. citeturn422412search0turn422412search12 | “Select the minimal appropriate operator expansion.” | Only a new failure of the selector or its value estimates. |
| [**What Can I Do Here? A Theory of Affordances in Reinforcement Learning**](https://arxiv.org/abs/2006.15085) | Khimya Khetarpal, Zafarali Ahmed, Gheorghe Comanici, David Abel, Doina Precup; 2020; ICML | Formalizes reliable state–intent transitions and uses them to reduce planning and model-learning burden. citeturn429357search3 | State-conditioned operator availability and reachable transitions. | Not a promising primary novelty route. |
| [**Reachability Constrained Reinforcement Learning**](https://proceedings.mlr.press/v162/yu22d.html) | Dongjie Yu, Haitong Ma, Shengbo Li, Jianyu Chen; 2022; ICML | Learns policies subject to persistent-safety reachability constraints and characterizes feasible sets with a safety value function. citeturn566917search5 | Reachable/viable sets under constraints. | Does not diagnose neural inference-operator deficits. |
| [**Continuation Path Learning for Homotopy Optimization**](https://proceedings.mlr.press/v202/lin23n.html) | Xi Lin, Zhiyuan Yang, Xiaoyuan Zhang, Qingfu Zhang; 2023; ICML | Learns a continuation path over easy-to-hard surrogate optimization problems. citeturn566917search3 | Temporarily transform/lift a problem and return to the target. | Only a discrete causal operator-deficit result remains. |
| [**Rational Metareasoning for Large Language Models**](https://arxiv.org/abs/2410.05563) | Nicolò De Sabbata, Theodore R. Sumers, Badr AlKhamissi, Antoine Bosselut, Thomas L. Griffiths; 2024/2025; arXiv | Trains LLMs to use intermediate reasoning selectively with a value-of-computation reward, reducing generated tokens at similar performance. citeturn422412search1turn422412search13 | Reason only when expected benefit exceeds cost. | Which operator is structurally useful, and why a value model misjudges it. |
| [**Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters for Reasoning**](https://openreview.net/forum?id=4FWAwZtd2n) | Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar; 2025; ICLR | Studies compute-optimal verifier-guided test-time search and adaptive allocation. citeturn422412search6turn422412search10 | Search scaling and compute allocation. | Operator gains must survive this family of baselines. |
| [**ADaPT: As-Needed Decomposition and Planning with Language Models**](https://aclanthology.org/2024.findings-naacl.264/) | Archiki Prasad, Alexander Koller, Mareike Hartmann, Peter Clark, Ashish Sabharwal, Mohit Bansal, Tushar Khot; 2024; Findings of NAACL | Recursively decomposes a task when the executor cannot complete a subtask. citeturn422412search3turn422412search7 | Failure-triggered operator expansion. | Pre-failure diagnosis and exact operator-relative labels. |
| [**Tree of Thoughts: Deliberate Problem Solving with Large Language Models**](https://papers.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html) | Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas Griffiths, Yuan Cao, Karthik Narasimhan; 2023; NeurIPS | Explores, evaluates, backtracks over, and searches among coherent reasoning units. citeturn585552search0turn585552search4 | Branching, lookahead, backtracking, and stronger search. | Cannot explain an edge absent from the declared base search process, but is a strong control. |

### 5.3 Tools, verifiers, representation changes, constrained generation, and latent planning

| Paper | Authors; year; venue | Actual contribution | Seed portion already covered | Residual, if any |
|---|---|---|---|---|
| [**ReAct: Synergizing Reasoning and Acting in Language Models**](https://openreview.net/forum?id=WE_vluYUL-X) | Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao; 2023; ICLR | Interleaves language reasoning with environment/tool actions and observations. citeturn585552search1turn585552search5 | External tool/environment calls that change information and trajectories. | None for generic tool invocation. |
| [**Toolformer: Language Models Can Teach Themselves to Use Tools**](https://arxiv.org/abs/2302.04761) | Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom; 2023; NeurIPS | Learns which APIs to call, when, with what arguments, and how to use the result. citeturn585552search2turn585552search14 | Adaptive tool routing. | No residual generic novelty. |
| [**Let’s Verify Step by Step**](https://openreview.net/forum?id=v8L0pN6EOi) | Hunter Lightman et al.; 2024; ICLR | Trains process reward models to judge intermediate mathematical reasoning steps. citeturn585552search3 | Local progress/value guidance during search. | Test whether such models undervalue useful structural detours. |
| [**Training Large Language Models to Reason in a Continuous Latent Space**](https://arxiv.org/abs/2412.06769) | Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, Yuandong Tian; 2024; arXiv | Introduces Coconut, feeding hidden states back as continuous thoughts and observing breadth-like latent exploration. citeturn665878search0turn665878search10 | Changing the representation in which reasoning proceeds. | No generic novelty in “switch representation.” |
| [**SwiReasoning: Switch-Thinking in Latent and Explicit for Pareto-Superior Reasoning LLMs**](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ddb7bad46132a323aa9d039000941881-Abstract-Conference.html) | Dachuan Shi, Abedelkadir Asi, Keying Li, Xiangchi Yuan, Leyan Pan, Wenke Lee, Wen Xiao; 2026; ICLR | Dynamically switches explicit and latent reasoning using entropy trends, improving accuracy/token efficiency. citeturn665878search30 | Adaptive representation switching. | Makes the broad representation-expansion claim especially crowded. |
| [**Improving Instruction-Following in Language Models through Activation Steering**](https://www.microsoft.com/en-us/research/?p=1137321) | Alessandro Stolfo, Vidhisha Balachandran, Safoora Yousefi, Eric Horvitz, Besmira Nushi; 2025; ICLR | Derives instruction-specific activation vectors and applies them at inference for constraint control. citeturn665878search16 | Adding inference-time control dimensions. | Not a reachability novelty. |
| [**NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints**](https://aclanthology.org/2021.naacl-main.339/) | Ximing Lu, Peter West, Rowan Zellers, Ronan Le Bras, Chandra Bhagavatula, Yejin Choi; 2021; NAACL | Enforces complex logical lexical constraints during decoding with beam-like asymptotic cost. citeturn665878search9 | Constraint-respecting reachable sequence sets. | Generic constrained reachability is occupied. |
| [**NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics**](https://aclanthology.org/2022.naacl-main.57/) | Ximing Lu et al.; 2022; NAACL | Adds efficient future-cost lookahead for constrained generation. citeturn876779search1turn876779search5 | Backward/lookahead reasoning to avoid future infeasibility. | No residual beyond a new estimator failure. |
| [**Planning with Diffusion for Flexible Behavior Synthesis**](https://arxiv.org/abs/2205.09991) | Michael Janner, Yilun Du, Joshua Tenenbaum, Sergey Levine; 2022; ICML | Treats denoising a trajectory as planning and supports flexible conditioning on goals/rewards. citeturn876779search0turn876779search4 | Lifted trajectory control and indirect paths. | Not suitable for the proposed GPU-only reasoning paper. |
| [**ReasonOps: Operator Segmentation for LLM Reasoning Traces**](https://arxiv.org/abs/2605.29192) | Daniel Lee, Owen Queen, James Zou; 2026; arXiv preprint | Infers a recurring vocabulary of reasoning operators from 44,662 traces across 12 models and eight benchmarks, and reports that operator-use features predict correctness; reflective operators can help hard cases while hurting easy ones. citeturn336186view0 | Operator taxonomies and the claim that always using a powerful reasoning mode can be harmful. | It neither adds verifier-defined operators nor identifies bounded reachability or cut-induced value inversion. |

### 5.4 Formal theorem proving: the decisive collision set

| Paper | Authors; year; status/venue | Actual contribution | Seed portion already covered | Residual, if any |
|---|---|---|---|---|
| [**LEGO-Prover: Neural Theorem Proving with Growing Libraries**](https://arxiv.org/abs/2310.00656) | Haiming Wang et al.; 2024; ICLR | Builds proofs modularly, creates verified lemmas, evolves a growing skill library, and reuses it. citeturn758754search1turn758754search29 | Lemma invention, reusable operators, library expansion. | Selective diagnosis of when expansion is harmful/useful. |
| [**REFACTOR: Learning to Extract Theorems from Proofs**](https://arxiv.org/abs/2402.17032) | Jin Peng Zhou, Yuhuai Wu, Qiyang Li, Roger Grosse; 2024; ICLR | Learns reusable theorem extraction from proof trees and refactors Metamath proofs. citeturn758754search2turn758754search14 | Proof-tree-to-DAG compression and abstraction invention. | Progress-model ranking during online cut introduction. |
| [**Formal Theorem Proving by Rewarding LLMs to Decompose Proofs Hierarchically**](https://arxiv.org/abs/2411.01829) | Kefan Dong, Arvind Mahankali, Tengyu Ma; 2024; arXiv | Trains LLMs with reward to generate and solve their own intermediate lemmas rather than relying on human lemmas. citeturn915994view18turn885201search6 | Learned hierarchical decomposition. | Causal estimator failure and pre-failure selective activation. |
| [**DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition**](https://arxiv.org/abs/2504.21801) | Z. Z. Ren, Zhihong Shao, Junxiao Song, et al.; 2025; arXiv technical report | Uses recursive subgoal decomposition for cold-start data and RL in Lean. citeturn758754search3 | Powerful decomposition operator at training and inference. | Not why progress estimators prune necessary cuts. |
| [**LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction**](https://openreview.net/forum?id=eTmOwvvRu9) | Robert Joseph George, Suozhi Huang, Peiyang Song, Anima Anandkumar; 2025; TMLR | Predicts remaining proof steps from Lean proof states and uses the estimate to guide search. citeturn483013search1turn483013search5 | The strongest direct progress-estimation baseline. | Its labels and search behavior are the hypothesized failure locus. |
| [**Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction**](https://arxiv.org/abs/2508.03613) | Yong Lin, Shange Tang, Bohan Lyu, et al.; 2025; technical report/OpenReview | Releases 8B and 32B Lean provers with scaffolded synthesis, compiler-guided self-correction, and model averaging. citeturn690539search0turn690268view10 | Strong open model and strong same-operator sampling/self-correction baseline. | Practical backbone for the proposed experiment. |
| [**Prover Agent: An Agent-Based Framework for Formal Mathematical Proofs**](https://arxiv.org/abs/2506.19923) | Kaito Baba, Chaoran Liu, Shuhei Kurita, Akiyoshi Sannai; 2025; arXiv | Coordinates informal reasoning, formal proving, Lean feedback, and auxiliary-lemma generation. citeturn885201search3turn885201search11 | Auxiliary lemmas for difficult proofs. | No exact operator-deficit diagnosis or progress-inversion test. |
| [**Exponential Sample Complexity Separation between Flat and Hierarchical Agentic Theorem Provers**](https://arxiv.org/abs/2602.10512) | Sho Sonoda, Shunta Akiyama, Yuya Uezato; 2026; arXiv | Models proof search as a deterministic finite-horizon MDP and shows an exponential sufficient-sample separation when flat traces duplicate reusable hard subproofs but a hierarchical learner predicts a proof DAG. citeturn224444search0 | The central proof-DAG/cut-compression motivation and bounded reachability framing. | Only empirical estimator inversion, causal pruning, adaptive diagnosis, and natural transfer. |
| [**DreamProver: Evolving Transferable Lemma Libraries via a Wake-Sleep Theorem-Proving Agent**](https://arxiv.org/abs/2604.26311) | Youyuan Zhang, Jialiang Sun, Hangrui Bi, Chuqin Geng, Wenjie Ma, Zhaoyu Li, Xujie Si; 2026; arXiv | Alternates proving with lemma proposal and sleep-stage abstraction/consolidation to evolve transferable libraries. citeturn885201search0turn885201search4 | Library invention and reuse. | Per-instance structural advantage prediction remains possible. |
| [**Optimizing the Cost-Quality Tradeoff of Agentic Theorem Provers in Lean**](https://arxiv.org/abs/2606.04883) | Kári Rögnvaldsson, Chenhao Sun, Jasper Dekoninck, Martin Vechev; 2026; arXiv | Uses failed Lean trajectories to decide whether to continue or restart from a new lemma decomposition, reducing cost at similar quality. citeturn224444search2 | Adaptive resource allocation over decomposition attempts. | Pre-failure cut advantage and value-model misspecification. |
| [**Planning to Hammer: Difficulty-Aware Decomposition for Automating Rocq Proofs**](https://arxiv.org/abs/2606.17981) | Ning Zhang, Nongyu Di, Zenan Li, Yuan Yao, Xiaoxing Ma; 2026; arXiv | Generates arbitrary sublemma decompositions, type-checks them under temporary admits, ranks by predicted hammer solvability, and recursively proves them. citeturn224444search1 | Difficulty-aware pre-proof decomposition. | A CIPI paper must show *why* difficulty/progress ranking fails, not just add a better ranker. |
| [**LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks**](https://arxiv.org/abs/2606.03303) | Po-Nien Kung et al.; 2026; arXiv | Uses informal blueprints, decomposition, Lean feedback, and iterative refinement; introduces Lean-IMO-Bench. citeturn224444search3 | Full agentic proof planning and decomposition. | Mechanistic failure analysis, not another agent stack. |
| [**FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models**](https://arxiv.org/abs/2605.10141) | Zeynel A. Uluşan, Burak S. Akbudak, Can S. Erer, Gözde Gül Şahin; 2026; arXiv | Evaluates proof reward models on preference pairs made from correct proofs and injected errors. citeturn690539academia30 | Reward-model evaluation in formal mathematics. | Does not test useful detours or counterfactual continuation value. |
| [**Mechanism-Level Routing Failure in LLMs over Lean-Verified Algebraic Structures**](https://arxiv.org/abs/2607.04534) | Manuel Israel Cázares, Wenlin Zhang, Haobo Ma; 2026; arXiv preprint | Studies whether models select the correct proof-mechanism template on a small Lean-anchored algebraic corpus and reports improvement from mechanism-bearing cues. citeturn790271search1 | Directly crowds a generic claim that an LLM should diagnose which reasoning mechanism to use. | It is fixed-label classification on a small corpus, not proof search, exact bounded reachability, reusable cuts, or causal value-model pruning. |
| [**P³: Joint Program-and-Proof Planning for Verified Code Generation**](https://arxiv.org/abs/2608.09277) | Zenan Li, Ziran Yang, Peiyang Song, Zhaoyu Li, Kaiyu Yang; 2026; arXiv | Jointly plans implementation and proof so the chosen program is structurally easier to verify; introduces Lean4Commit0. citeturn885201search1turn885201search5 | Level-B tolerance exploitation and structural proofability in code. | Directly blocks a generic “choose a proof-friendly implementation” paper. |

### 5.5 Program synthesis, code agents, multi-agent expansion, and search diversity

| Paper | Authors; year; venue | Actual contribution | Seed portion already covered | Residual, if any |
|---|---|---|---|---|
| [**DreamCoder: Growing Generalizable, Interpretable Knowledge with Wake-Sleep Bayesian Program Learning**](https://arxiv.org/abs/2006.08381) | Kevin Ellis et al.; 2021; PLDI | Alternates program synthesis with symbolic abstraction invention, extending the DSL with reusable concepts. citeturn299529search0 | Genuine language/operator-space expansion. | An exact selector benchmark is possible but likely dismissed as library learning. |
| [**ReGAL: Refactoring Programs to Discover Generalizable Abstractions**](https://arxiv.org/abs/2401.16467) | Elias Stengel-Eskin, Archiki Prasad, Mohit Bansal; 2024; ICML | Learns reusable helper functions by execution-verified refactoring. citeturn299529search1turn299529search29 | Auxiliary functions and abstraction reuse. | Per-instance routing is still incremental. |
| [**Planning in Natural Language Improves LLM Search for Code Generation**](https://openreview.net/forum?id=48WAZhwHHw) | Evan Wang et al.; 2025; ICLR | PlanSearch creates diverse observations and plans, then searches over plans rather than only code samples. citeturn299529search6turn299529search14 | Representation change and diversity during code search. | Strong evidence against interpreting gains as operator reachability without diversity controls. |
| [**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**](https://openreview.net/forum?id=VTF8yNQM66) | Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan; 2024; ICLR | Introduces repository-level issue resolution with executable tests. citeturn299529search7turn299529search27 | Public code-agent benchmark with local versus structural repairs. | Tests are incomplete proxies; engineering and compute confounds are severe. |
| [**Policy Space Response Oracles: A Survey**](https://arxiv.org/html/2403.02227v1) | A. Bighashdel et al.; 2024; IJCAI survey | Systematizes PSRO, which repeatedly expands a restricted strategy population with response oracles. citeturn876779search2 | Expand one’s strategy set against opponents. | Multi-agent version is already canonical double-oracle reasoning. |
| [**Towards Unifying Behavioral and Response Diversity for Open-Ended Learning in Zero-Sum Games**](https://proceedings.neurips.cc/paper/2021/hash/07bba581a2dd8d098a3be0f683560643-Abstract.html) | Xiangyu Liu et al.; 2021; NeurIPS | Develops diversity measures and population expansion for non-transitive games. citeturn876779search3 | Strategy-set expansion and diversity. | Makes multi-agent instantiation a high-collision choice. |

### 5.6 Literature conclusion

The literature leaves no broad conceptual territory. The closest residual is a **mechanism-level failure of learned progress/value estimates around proof-DAG construction**. Even that residual sits between several active lines:

- LeanProgress already predicts remaining proof steps. citeturn758754search0
- Quarry already ranks decompositions by predicted downstream solvability. citeturn224444search1
- Agentic Lean work already routes between continuing and restarting decompositions. citeturn224444search2
- Sonoda et al. already provide the proof-DAG sample-complexity mechanism. citeturn224444search0
- ReasonOps already maps recurring operator patterns and finds that reflective modes can have difficulty-dependent benefits, while mechanism-routing work already tests fixed proof-strategy classification. citeturn336186view0turn790271search1
- LEGO-Prover, REFACTOR, Prover Agent, DreamProver, and DeepSeek-Prover-V2 already establish that lemmas/decomposition can help. citeturn758754search1turn758754search2turn885201search3turn885201search0turn758754search3

The only credible claim is therefore not an architecture but a **falsifiable diagnostic statement**:

> Existing progress/value signals may be systematically anti-correlated with the value of a reusable detour exactly in the regime where proof-tree flattening becomes expensive.

---
## 6. Novelty-collision matrix

| Proposed claim | Strongest collision | Why the broad claim fails | What would have to survive |
|---|---|---|---|
| “The agent detects that ordinary reasoning is insufficient.” | Rational metareasoning; adaptive test-time compute; ADaPT. citeturn422412search0turn422412search1turn422412search3 | This is problem-dependent strategy selection or failure-triggered decomposition. | Predict **operator treatment effect**, not difficulty or generic need for more thinking. |
| “The agent adds a new operator or subgoal.” | Options, DreamCoder, LEGO-Prover, DeepSeek-Prover-V2. citeturn581877search1turn299529search0turn758754search1turn758754search3 | Temporally extended actions, DSL growth, and lemma generation already do this. | A precise operator restriction and causal evidence that the new edge—not extra tokens—matters. |
| “The agent changes representation.” | Coconut, SwiReasoning, activation steering. citeturn665878search0turn665878search30turn665878search16 | Dynamic latent/explicit switching and inference steering are active topics. | A representation-specific failure criterion with exact counterfactual labels. |
| “More search cannot compensate for a missing operator.” | Sonoda et al.; proof complexity; constrained decoding. citeturn224444search0turn665878search9turn876779search1 | In controlled calculi this is almost definitional; in natural LLM inference it is usually unidentifiable. | Exact finite-system certification plus natural transfer; no claim of logical unprovability. |
| “A temporary step away from the goal is necessary.” | Homotopy, hierarchical planning, backward reasoning, ToT. citeturn566917search3turn581877search1turn585552search0 | Detours and subgoals are standard planning phenomena. | Demonstrate a systematic **value-estimator sign error** on the detour. |
| “Task tolerance can be exchanged for future control.” | Empowerment, affordances, constrained control, P³. citeturn429357search5turn429357search3turn566917search5turn885201search1 | This is constrained future-value optimization; P³ directly covers proof-friendly implementation choice. | A new measurable conservation/tradeoff law, not just improved downstream accuracy. |
| “Always enabling powerful operators is worse.” | Cost-aware routers, tool routing, adaptive decomposition. citeturn224444search2turn585552search2turn422412search3 | Ordinary precision–cost routing predicts this. | Show that the selector exploits structural reuse features after conditioning on difficulty and cost. |
| “A value/PRM confuses low probability with operator insufficiency.” | LeanProgress, PRMs, FormalRewardBench. citeturn758754search0turn585552search3turn690539academia30 | Existing work evaluates progress and proof quality but not this exact counterfactual. | This is the strongest residual if demonstrated with exact labels and causal replay. |
| “Generated lemmas expand bounded proof reachability.” | Sonoda et al., REFACTOR, LEGO-Prover, DreamProver. citeturn224444search0turn758754search2turn758754search1turn885201search0 | The structural advantage of reusable lemmas is already established. | Shift claim to **when standard search scores reject them and how to diagnose that regime**. |

### 6.1 The smallest residual novelty statement

The narrowest defensible novelty claim is:

> **Under a fixed proof-search budget, local progress/value estimators trained on flat traces can display a predictable ranking inversion at reusable lemma introduction; a cut-aware advantage estimator corrects this failure and selectively improves the solve–compute frontier.**

This statement is narrower than the seed in four important ways:

1. It concerns one operator: a separately proved, reusable lemma/cut.
2. It concerns one failure mechanism: mis-ranking by progress/value estimates.
3. It uses one exact verifier: Lean or a finite proof calculus.
4. It makes no claim of mathematical unreachability in natural benchmarks.

---

## 7. Candidate AI instantiations

Scores use a 1–5 scale, where 5 is favorable. “Low-confound” means extra computation is relatively easy to rule out; “low-collision” means less occupied by prior work.

| Candidate domain | Novelty residual | Exact verifier | Causal isolation | 3–7 day signal | 8×4090 fit | Low compute confound | Low collision | Reviewer risk | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| **1. Formal theorem proving: CIPI** | 4 | 5 | 5 | 4 | 4 | 4 | 3 | “Just decomposition/cut theory.” | **SURVIVES** |
| **2. Finite proof system / SAT proof DSL** | 3 | 5 | 5 | 5 | 5 | 5 | 2 | “Toy benchmark; classical proof complexity.” | **Support substrate only** |
| **3. Program synthesis with adaptive DSL expansion** | 2 | 5 | 5 | 5 | 5 | 4 | 1 | “DreamCoder/library learning with a router.” | **ELIMINATE as main paper** |
| **4. Verifiable mathematical reasoning** | 2 | 4 | 2 | 4 | 4 | 2 | 1 | “Prompted transformations and tool use.” | **ELIMINATE** |
| **5. Code generation and code agents** | 2 | 3 | 2 | 2 | 3 | 1 | 1 | “Refactoring/planning; tests incomplete.” | **ELIMINATE** |
| **6. Verified code generation** | 2 | 5 | 4 | 2 | 3 | 3 | 1 | P³ directly occupies joint structural planning. | **ELIMINATE / later transfer** |
| **7. Generic test-time LLM reasoning** | 1 | 3 | 2 | 5 | 5 | 1 | 1 | “Adaptive TTC/metareasoning.” | **ELIMINATE** |
| **8. Constrained generation or safety** | 2 | 4 | 3 | 4 | 4 | 2 | 1 | “Constrained decoding/lookahead.” | **ELIMINATE** |
| **9. Multi-agent/adversarial reasoning** | 1 | 2 | 2 | 2 | 2 | 1 | 1 | “PSRO/double oracle/strategy diversity.” | **ELIMINATE** |
| **10. Latent/explicit representation switching** | 1 | 3 | 2 | 3 | 3 | 1 | 1 | SwiReasoning/DyLaR/Coconut already occupy it. | **ELIMINATE** |

### 7.1 Formal theorem proving

**Strengths**

- Lean provides exact final verification.
- One can log every proof state, candidate tactic, score, and compiler response.
- A small proof calculus permits exact shortest-path and no-proof-within-$B$ certificates.
- Auxiliary lemmas are semantically meaningful and directly instantiate a reusable detour.
- An open 8B prover is available and strong enough for a rapid experiment. Goedel-Prover-V2-8B reports high MiniF2F performance at modest pass@$k$, making it a practical backbone rather than a toy model. citeturn690539search0turn690539search3

**Weaknesses**

- Lemma generation and hierarchical proving are extremely crowded.
- Surface-level tactic restrictions in Lean can look artificial.
- Natural-benchmark “unreachability” is unidentifiable.
- MiniF2F is increasingly saturated and its original statements have known flaws; miniF2F-v2 corrects many of them. citeturn690539search1

**Conclusion:** highest potential only if the contribution is mechanistic and causal, not another prover stack.

### 7.2 Verifiable mathematical reasoning

Possible operators include backward reasoning, substitution, decomposition, symbolic solvers, and code execution. Final answers can often be checked. However, a direct chain-of-thought policy can in principle express most transformations, making “new operator” a prompt-level distinction rather than a clean graph change. Search diversity and latent probability are inseparable. This domain is excellent for downstream transfer but poor for the first causal paper.

**Decision:** eliminate.

### 7.3 Code generation and code agents

The seed maps naturally to local edit versus helper abstraction versus structural refactor. SWE-bench offers executable evaluation, but tests do not characterize all intended behavior, agents use heterogeneous tool traces, repository setup is expensive, and local versus structural solutions are not cleanly separated. PlanSearch already shows that plan-space diversity improves code search, ReGAL learns reusable helper abstractions, and P³ directly plans program structure for proofability. citeturn299529search14turn299529search1turn885201search1

**Decision:** eliminate from the initial project. Use verified code only as a later cross-domain transfer if CIPI is real.

### 7.4 Generic test-time LLM reasoning

This is the most tempting and the worst scientific choice. Sampling, branching, representation changes, subgoals, tools, reflection, and stopping can all be represented as meta-actions. Exact operational reachability is unavailable, answer verifiers are often noisy, and every gain can be attributed to more or more diverse compute. Snell et al., rational metareasoning, ADaPT, Tree of Thoughts, Coconut, and SwiReasoning collectively occupy the space. citeturn422412search6turn422412search1turn422412search3turn585552search0turn665878search0turn665878search30

**Decision:** hard NO-GO.

### 7.5 Constrained generation and safety

Finite-state or logical constraints can make valid-sequence reachability exact, and indirect paths may be necessary. But NeuroLogic and A*esque decoding already alter decoding to maintain future feasibility. A safety framing would add policy and benchmark ambiguity without strengthening the central science. citeturn665878search9turn876779search1

**Decision:** eliminate.

### 7.6 Multi-agent/adversarial reasoning

Expanding one’s strategy population while restricting an opponent is exactly the logic of double-oracle/PSRO methods. Outcomes are stochastic, training best responses is expensive, and causal attribution is weak. citeturn876779search2turn876779search3

**Decision:** hard NO-GO.

### 7.7 Program synthesis and finite DSL expansion

This domain offers the cleanest exact distinction: a base DSL may literally be unable to express a target, and a new primitive can make it expressible. Unfortunately, this collapses into grammar induction, abstraction invention, and library learning, exemplified by DreamCoder and ReGAL. citeturn299529search0turn299529search1 It is also easy to create trivial labels by exposing the missing primitive in the problem syntax.

**Decision:** use only as a controlled calibration substrate, not as the main contribution.

### 7.8 Verified code generation

This is the strongest conceptual match to Level B: several implementations satisfy the same specification, but their future proof obligations differ. Yet P³, posted in August 2026, explicitly observes this and jointly plans program and proof, improving solve rate and cost. citeturn885201search1

**Decision:** direct collision; reserve for cross-domain confirmation only.

---

## 8. Aggressive elimination funnel

### Gate 1: Is the operator distinction real?

Eliminate any candidate where the “new operator” is merely a prompt phrase that the base model could already emit. This removes most generic LLM reasoning and verifiable-math formulations.

### Gate 2: Can bounded reachability be identified?

Eliminate candidates where failure can only mean “the model did not sample it.” Natural language, code agents, and open-ended multi-agent tasks fail this gate. A finite proof calculus passes; natural Lean passes only as an empirical transfer domain.

### Gate 3: Can extra compute and diversity be matched?

Eliminate any design that gives the expanded method more generated tokens, verifier calls, candidate plans, or privileged feedback. Generic tool-use and multi-agent designs become difficult to interpret here.

### Gate 4: Is the idea already an established operator learner/router?

- Tool call: Toolformer/ReAct.
- Recursive decomposition: ADaPT, DeepSeek-Prover-V2, Prover Agent, Quarry, LEAP.
- Representation switch: Coconut, SwiReasoning, DyLaR.
- Library growth: DreamCoder, ReGAL, LEGO-Prover, DreamProver.
- Strategy population expansion: PSRO.
- Proof-friendly program planning: P³.

All are eliminated as primary novelty claims. citeturn585552search2turn585552search5turn422412search3turn758754search3turn885201search3turn224444search1turn224444search3turn665878search30turn299529search0turn299529search1turn758754search1turn885201search0turn876779search2turn885201search1

### Gate 5: Does a counterintuitive, mechanistic claim remain?

Only one candidate survives:

> A reusable lemma may make a bounded proof dramatically easier while making the immediate proof state look harder, causing local progress/value guidance to suppress exactly the operator it needs.

### Gate 6: Can this be tested in one week?

Yes, if the first experiment is a controlled proof-DAG benchmark plus a small Lean transfer test. No, if the project begins by building a general agent framework, training a new 8B prover, or running full PutnamBench.

---

## 9. Top surviving direction and fallback

### 9.1 Primary direction: Cut-Induced Progress Inversion in formal proof search

**Working title:**

> **When Proof Progress Goes Backward: Diagnosing Structural Detours in Verifier-Guided Theorem Proving**

**Core question:**

> When a proof requires constructing a reusable intermediate result, do state-value/progress models trained on flat proof traces systematically prefer locally simplifying but globally inferior actions?

**Why this is not simply “lemma generation”:**

- The object of study is the score and pruning behavior, not the lemma generator.
- The main intervention can reuse an existing lemma proposal mechanism.
- The experiment compares the same candidate graph under different priority functions.
- The claim is falsified if a strong value model already ranks useful cuts correctly.

**Why this could matter beyond Lean:**

The same structural error could occur whenever a system must temporarily create a reusable obligation: helper functions, invariants, intermediate representations, cached subplans, or verified API layers. P³ suggests the verified-code analogue, but that transfer should follow—not precede—the clean proof experiment. citeturn885201search1

### 9.2 Fallback/support direction: an exact counterfactual operator-advantage benchmark

Build a public finite proof benchmark in which:

- cut-free shortest cost is exactly known;
- one-cut shortest cost is exactly known;
- positive and no-reuse controls are syntax-matched;
- the optimal operator class is not directly stated in the input;
- local progress features are deliberately insufficient on some paired instances.

This benchmark is useful as an instrument for the main paper, but **not enough for ICLR main track on its own**. Without natural transfer it is likely a workshop, dataset, or proof-complexity result.

### 9.3 Explicitly rejected alternative: tolerance-to-proofability in verified code

A separate paper could ask whether, among extensionally correct programs, one should choose the implementation with maximum downstream proofability. That is attractive and exact—but P³ already jointly plans program and proof and reports gains from structurally compatible implementations. citeturn885201search1 The residual would be incremental unless tied to the same progress-inversion mechanism and validated after the theorem-proving result.

---

## 10. Formal problem statements

### 10.1 Formalization A: meta-MDP and value of computation

Define a meta-state

$$
z_t=(x,S_t,H_t,\mathcal O_t,b_t),
$$

where:

- $x$ is the theorem or task;
- $S_t$ is the current frontier of proof states;
- $H_t$ is the complete search history, including failed attempts;
- $\mathcal O_t$ is the currently enabled operator family;
- $b_t$ is remaining cost budget.

Meta-actions include

$$
a_t^{\mathrm{meta}}\in
\{\text{expand base node},\text{restart},\text{propose lemma},
\text{prove lemma},\text{retrieve},\text{stop}\}.
$$

The objective is

$$
\max_\mu
\mathbb E_\mu
\left[
\mathbf 1\{V(\tau)=1\}
-\lambda C_{\mathrm{total}}(\tau)
\right].
$$

**Assessment:** decision-theoretically correct but scientifically generic. It is indistinguishable from metareasoning unless the paper identifies a specific misspecified state representation or value estimator. Rational metareasoning and cost-aware theorem-prover routing already occupy the generic objective. citeturn422412search0turn422412search1turn224444search2

### 10.2 Formalization B: operator-augmented finite proof graph

Let

$$
\mathcal G_k(x)=(\mathcal S_k,\mathcal E_k)
$$

be the finite proof-search graph induced by operator policy $\mathcal O_k$ for theorem $x$. A node is a verified proof state plus any explicitly reusable local lemmas. An edge is a type-checked inference step or meta-step.

Define the budgeted reachable goal set

$$
R_B(x,\mathcal O_k)
=
\left\{
 g:\exists\tau\text{ from }s_0\text{ to }g,
\;V(\tau)=1,
\;c(\tau)\le B
\right\}.
$$

For a binary success task, define certified bounded reachability

$$
r_k(x,B)=\mathbf 1\{G\cap R_B(x,\mathcal O_k)\neq\varnothing\}.
$$

An instance has a certified one-cut deficit at budget $B$ when

$$
r_0(x,B)=0,
\qquad
r_1(x,B)=1.
$$

In a finite proof DSL, exhaustive search or dynamic programming can certify this. In natural Lean, it generally cannot; only empirical $p_k(x,B)$ may be reported.

**Assessment:** best scientific formalization because it makes “changed bounded reachability” exact in the controlled domain and exposes tree-versus-DAG reuse. It also aligns with the finite-horizon proof-search model in Sonoda et al. citeturn224444search0

### 10.3 Formalization C: operator expansion as a heterogeneous treatment effect

For each theorem $x$, define potential outcomes under matched budget:

$$
Y_0(x)=\mathbf 1\{\text{base search succeeds}\},
\qquad
Y_1(x)=\mathbf 1\{\text{one-lemma search succeeds}\}.
$$

The individual operator advantage is latent:

$$
\tau(x)=\mathbb E[Y_1(x)-Y_0(x)\mid x].
$$

A selector $g_\phi(x)$ should predict the sign and magnitude of $\tau(x)$, not $\mathbb E[Y_0(x)]$ alone. Its policy value is

$$
\mathcal V(g_\phi)
=
\mathbb E
\left[
Y_{g_\phi(x)}(x)
-\lambda C_{g_\phi(x)}(x)
\right].
$$

This formalization enables a direct “difficulty versus advantage” test:

- a difficulty model predicts $Y_0$;
- an advantage model predicts $Y_1-Y_0$;
- the latter must improve selective policy value after conditioning on base difficulty.

**Assessment:** useful for natural Lean, where exact reachability is latent. It forces cross-fitting, held-out seeds, and honest uncertainty, but it does not by itself establish structural reachability.

### 10.4 Observed and latent quantities

| Quantity | Controlled finite calculus | Natural Lean |
|---|---|---|
| Theorem/input | Observed | Observed |
| Enabled operators | Exactly enforced by verifier/grammar | Operationally enforced by search wrapper; not a logical restriction |
| Complete graph up to $B$ | Enumerated | Unobserved |
| Shortest cut-free and one-cut cost | Exact or bounded | Latent |
| Candidate lemma and proof | Verified | Verified |
| Progress/value scores | Observed | Observed |
| Final success | Exact | Exact for generated proof |
| Probability of success at budget | Estimated from exhaustive policy or repeated seeds | Estimated from repeated rollouts |
| “Mathematical unreachability” | Not claimed unless the finite calculus defines the entire task | Never claimed |
| Hindsight oracle | Exact | Empirical upper bound only |

### 10.5 What constitutes operator expansion

The main experiment permits **exactly one new meta-operator**:

$$
\operatorname{ProposeAndCacheLemma}(\ell):
(x,s_0)\mapsto
\bigl[(\ell,\text{proof obligation}),
(x\mid \ell,\text{main obligation})\bigr].
$$

The lemma must be:

1. well-typed in the original environment;
2. separately proved without `sorry`, admitted axioms, or untrusted code;
3. used at least twice in the controlled positive family, or pass a preregistered reuse test in Lean;
4. included in the final kernel-checked proof;
5. charged for proposal, proving, storage, and application.

Do **not** bundle retrieval, Python, SMT, backward prompting, multiple lemmas, or model switching into the primary treatment.

### 10.6 Oracle construction

**Controlled oracle:** exhaustive dynamic programming returns $L_0(x)$, $L_1(x)$, the optimal cut, and whether the cut changes $B$-reachability.

**Natural Lean oracle:** run both policies with a larger *offline labeling budget* on training/development problems and disjoint random seeds. Estimate

$$
\widehat\tau(x)=\widehat p_1(x,B)-\widehat p_0(x,B).
$$

Use cross-fitting so no evaluation theorem or evaluation seed labels itself. Call this a **hindsight empirical oracle**, never a ground-truth oracle.

### 10.7 Identifiability limits

The natural Lean experiment cannot distinguish these possibilities with certainty:

- no short flat proof exists;
- a short flat proof exists but the model assigns it tiny probability;
- a short flat proof exists but the search heuristic prunes it;
- the lemma changes only generation probability, not minimal proof length.

The controlled benchmark is therefore not optional. It supplies the exact structural fact; Lean supplies external validity.

---
## 11. Exact counterintuitive claims to test

The paper should preregister a small number of claims and be willing to kill them.

### H1. Progress inversion

For a root proof state $s$, let $s_\ell$ be the successor created by a useful reusable lemma and $s_a$ a matched local tactic successor. Define true fixed-budget continuation value

$$
q_B(s')=\Pr(\mathrm{verified\ success}\mid s',B-c(s\to s')).
$$

The claim is

$$
q_B(s_\ell)>q_B(s_a)
\quad\text{but}\quad
\widehat v(s_\ell)<\widehat v(s_a)
$$

on a nontrivial, predictable subset of problems.

**Counterintuitive form:** the action that appears to make the least immediate proof progress has the highest probability of eventual success.

**Falsifier:** a strong published progress/value model ranks useful lemma successors at least as well as local successors after calibration, or any inversion is restricted to trivial handcrafted examples.

### H2. Causal pruning, not merely bad correlation

Holding the candidate graph, generated tactics, node cap, and verifier outcomes fixed, changing only the frontier priority from a standard progress score to a cut-aware continuation score should recover useful lemma paths.

Let $\mathcal C$ be a frozen candidate graph and $\operatorname{Search}(\mathcal C,h,B)$ a deterministic replay with priority $h$. The causal effect is

$$
\Delta_{\mathrm{priority}}
=
\Pr[\operatorname{Search}(\mathcal C,h_{\mathrm{cut}},B)=1]
-
\Pr[\operatorname{Search}(\mathcal C,h_{\mathrm{base}},B)=1].
$$

**Falsifier:** gains disappear under frozen-graph replay, implying that generation diversity—not valuation/pruning—caused them.

### H3. A reuse-controlled phase transition

As repeated-subproof fan-out or depth grows, flat proof-tree cost should grow much faster than proof-DAG cost, and progress inversion should become more frequent or more damaging.

For family parameter $d$:

$$
\rho_d=\frac{L_0(d)}{L_1(d)}
$$

should increase predictably, and the search-success gap should appear near the budget crossing

$$
L_1(d)\le B<L_0(d).
$$

**Falsifier:** the apparent benefit is constant across reuse depth, equally strong in no-reuse controls, or explained by theorem length alone.

### H4. More base search is inferior to a small correct expansion

At matched or even moderately larger base-policy compute,

$$
p_1(x,B)>p_0(x,\kappa B)
$$

for preregistered $\kappa$ such as 2, 4, and 8 on the controlled positive family, and for a measurable natural-Lean subset.

**Falsifier:** 2–4× additional flat sampling, stronger search, or diversity matching closes most of the gap.

### H5. Always expanding is suboptimal

On no-reuse or easy-direct tasks, lemma generation adds branching, invalid obligations, and cost. Therefore a selective policy should beat both extremes:

$$
\mathcal V(g_\phi)
>
\max\{\mathcal V(\text{never}),\mathcal V(\text{always})\}.
$$

**Falsifier:** always-expand dominates or ties the selector across the full cost frontier. In that case there is no “minimal appropriate expansion” result.

### H6. Operator advantage is not generic difficulty

Let $d(x)$ be a strong difficulty prediction, such as base pass@$k$, predicted remaining steps, theorem length, and model uncertainty. The expansion selector must add information about

$$
\tau(x)=p_1(x,B)-p_0(x,B)
$$

after conditioning on $d(x)$.

**Falsifier:** a difficulty-only model matches the learned selector’s policy value, calibration, and ranking of expansion benefit.

### H7. The mechanism is reuse, not a longer scratchpad

The gain should collapse when the generated lemma is inlined, cannot be referenced more than once, or is replaced by an equal-length sham lemma.

**Falsifier:** sham and inlined controls retain the gain, indicating ordinary extra context, plan prompting, or sampling diversity.

---

## 12. Falsification-first 3–7 day killer experiment

### 12.1 Scientific question

> **Do published-style progress/value signals causally suppress reusable lemma detours in a regime where a one-cut proof is short but flat proof search is expensive, and can a cheap advantage selector activate the cut only on the affected instances?**

This experiment is deliberately not “does our new agent improve MiniF2F?” It has one mechanistic primary endpoint: **progress-score inversion with causal search consequences**.

### 12.2 Two-part design

#### Part A — `CutBench-S`: exact controlled proof-DAG benchmark

Create a small public benchmark encoded in a typed, kernel-checked proof DSL, preferably implemented inside Lean 4 or exported to Lean for final checking.

**Instance families**

1. **Reusable positive family.** A hard intermediate derivation $D_d$ is needed in multiple downstream branches. A one-cut proof proves $D_d$ once and references it; a flat proof must duplicate the derivation.
2. **No-reuse negative family.** Match theorem size, connective counts, branch count, and local proof-state statistics, but each branch requires a distinct $D_{d,i}$, so one cached lemma gives little benefit.
3. **Direct-easy family.** A short flat proof exists; introducing a lemma only increases cost.
4. **Sham-lift family.** An auxiliary obligation is added but is irrelevant or cannot be reused.
5. **Alias pairs.** Positive and negative instances share identical local/root features up to a chosen radius $h$, testing whether a local progress representation can distinguish them.

**Concrete pilot family**

Use a finite intuitionistic/sequent-style propositional calculus with normalized proof trees, conjunction introduction, implication elimination, and an optional single cut. For parameters depth $d$ and fan-out $k$, provide premises

$$
a_0,\quad a_0\to a_1,\ldots,a_{d-1}\to a_d,\quad a_d\to b_1,\ldots,a_d\to b_k,
$$

and target

$$
b_1\land b_2\land\cdots\land b_k.
$$

In the declared cut-free tree calculus, each conjunction branch must rederive $a_d$. With unit inference costs, a canonical flat proof has

$$
L_0(d,k)=k(d+1)+(k-1),
$$

whereas a one-cut proof derives and caches $a_d$ once, then reuses it:

$$
L_1(d,k)=d+2k
$$

under the stated normalization and one-unit cut charge. The dynamic-programming oracle—not these formulas alone—must certify shortest costs, because additional generated rules and distractors may create alternatives. Choose pilot points such as $(d,k)\in\{(16,16),(32,16),(32,32),(64,32),(64,64)\}$ so some instances satisfy $L_1\le B<L_0$ and others sit on both sides of the transition.

The no-reuse control replaces the shared chain with branch-specific chains $a_{i,0}\to\cdots\to a_{i,d}\to b_i$ while balancing symbol counts with disconnected distractor chains. Randomly permute atoms, implication order, conjunction bracketing, and irrelevant premises; generate graph-isomorphic alias pairs whose shared-versus-copied structure is hidden beyond radius $h$. This prevents a selector from solving the task through the token `a_d`, theorem length, or an exposed generator parameter.

This family is intentionally a diagnostic instrument, not evidence that natural Lean proofs share the same distribution. The natural-transfer arm is mandatory.

**Scale**

- 384 instances for the first run: 128 reusable positives, 128 no-reuse controls, 64 direct-easy, 64 alias/sham cases.
- Depth/fan-out levels chosen by pilot so shortest flat costs span roughly $0.25B$ to $32B$.
- Five generator/search seeds for controlled stochastic policies; exhaustive dynamic programming supplies exact $L_0$, $L_1$, and the optimal cut.

**Operational systems**

- $\mathcal O_0$: cut-free proof trees; no named reusable local result and no cross-branch memoization.
- $\mathcal O_1$: exactly one typed `cut`/`let-lemma` node, separately verified and reusable.
- Both systems use the same primitive inference rules.

**Why this is not circular**

The positive family is labeled by exact shortest-cost computation, not by whether the LLM happened to solve it. The no-reuse family prevents the selector from simply learning “large theorem means use a lemma.”

#### Part B — natural Lean transfer on `miniF2F-v2c`

Use the corrected Lean benchmark rather than silently relying on the flawed original statements. The miniF2F-v2 project reports correcting more than 300 statements and provides corrected variants. citeturn690539search1

**Initial subset**

- Select 120 test theorems before any model outcomes are observed.
- Use a deterministic hash of theorem name, stratified by source/topic if metadata is available.
- Pin the exact repository commit, Lean version, Mathlib version, and theorem list.
- If all 244 test theorems compile and wall-clock permits, run the full split after the primary 120-theorem analysis; do not redefine the primary endpoint.

**Natural operator policies**

- **Flat policy $\pi_0$.** Whole-proof generation/search using existing Mathlib lemmas and ordinary Lean tactics, but without a separately generated and independently searched auxiliary theorem.
- **One-lemma policy $\pi_1$.** First proposes one typed local lemma, proves it in a separate search process, caches it, then proves the main theorem with the lemma available.

This is an operational search-policy distinction, not a logical expressivity claim. The final Lean proof must contain no `sorry`, `admit`, untrusted axiom, or unchecked external result.

### 12.3 Candidate generation and frozen-graph replay

For each theorem/root state:

1. Generate a shared candidate set of local tactics and one-lemma proposals.
2. Type-check all candidates.
3. For valid lemma proposals, generate candidate lemma proofs and main-goal continuations.
4. Store a **candidate graph** containing states, edges, token costs, verifier costs, model log-probabilities, and all progress/value scores.
5. Replay the same graph under different priority functions:
   - model log-probability;
   - number of goals / syntactic size;
   - LeanProgress remaining-step prediction;
   - a strong learned base-value model;
   - the proposed cut-aware advantage score;
   - random priority as a sanity control.

Frozen-graph replay is the cleanest causal intervention. It separates “the lemma policy generated a better graph” from “the value model pruned the useful edge.”

### 12.4 Selector variants

1. **Zero-probe heuristic.** Uses theorem/root-state features only: repeated subexpression signatures, dependency graph motifs, predicted branching, root uncertainty, and a cheap lemma-reuse score.
2. **Cheap-probe heuristic.** Adds one fixed-cost plan probe or one direct attempt, capped at 256–512 generated tokens.
3. **Learned advantage selector.** Predicts $\widehat\tau(x)$ from root features and optional proposed-lemma features; trained with cross-fitting on controlled data plus the natural development split.
4. **Difficulty-only selector.** Same capacity, trained to predict base failure $1-Y_0$ rather than treatment advantage.
5. **Hindsight empirical oracle.** Chooses the empirically better arm from disjoint rollout seeds; analysis-only upper bound.

The selector should be tiny relative to the prover—linear/XGBoost for the first test and, only if needed, a LoRA-tuned 1–3B encoder. A new 8B router is unnecessary and would obscure the science.

### 12.5 Primary arms

| Arm | Operator family | Search/computation | Purpose |
|---|---|---|---|
| **A0 Never-expand** | Flat | Published-style best-first search | Base reference |
| **A1 Extra sampling** | Flat | Same generator, more independent samples, matched total cost | Rules out simple pass@$k$ scaling |
| **A2 Strong flat search** | Flat | Beam/RMaxTS-like or best-first with stronger value | Rules out weak search implementation |
| **A3 Diversity-matched flat** | Flat | Semantic clustering or DPP-style selection over ordinary trajectories | Rules out diversity explanation |
| **A4 Always-expand** | One lemma | Propose/prove/use one lemma on every theorem | Tests whether selectivity matters |
| **A5 Heuristic selector** | Adaptive | Cheap structural rule | Establishes whether the signal is simple/mechanistic |
| **A6 Learned advantage selector** | Adaptive | Predicts $Y_1-Y_0$ | Main adaptive arm |
| **A7 Difficulty selector** | Adaptive | Predicts base failure | Tests “merely predicts difficulty” attack |
| **A8 Hindsight oracle** | Adaptive | Best arm from held-out counterfactual rollouts | Headroom estimate |
| **A9 Sham expansion** | Nonfunctional auxiliary obligation | Same proposal/proof-length overhead where possible | Rules out longer prompt/scratchpad |
| **A10 Inlined/no-cache** | Lemma generated but not reusable | Same semantic content, sharing removed | Tests proof-DAG reuse mechanism |

### 12.6 Day-by-day execution

**Day 1 — infrastructure and preregistration**

- Pin Lean/Mathlib/model commits and compile the selected benchmark.
- Measure actual tokens/s, verifier throughput, and memory on the 4090 cluster.
- Freeze cost accounting and primary statistical tests.
- Implement controlled verifier and dynamic-programming oracle.

**Day 2 — exact structural test**

- Generate `CutBench-S` positive/negative families.
- Verify $L_0$, $L_1$, and budget crossings.
- Run sham and inlining controls.
- Apply Stage-A stop rule in §15.

**Days 3–4 — progress inversion and causal replay**

- Score paired cut/local successors with LeanProgress-style and stronger value models.
- Build frozen candidate graphs.
- Measure inversion rate and replay effect.
- Apply Stage-B stop rule.

**Days 5–7 — natural Lean transfer**

- Run miniF2F-v2c primary subset under A0–A10 with matched budgets.
- Train selectors only on controlled/development data.
- Compute paired confidence intervals and Stage-C decision.

No new large-model training is permitted during the killer experiment.

---

## 13. Datasets, models, baselines, metrics, and compute estimates

### 13.1 Datasets

| Dataset | Role | Size used initially | Why |
|---|---|---:|---|
| **CutBench-S** (new, released publicly) | Exact causal and reachability substrate | 384 instances | Exact $L_0/L_1$, matched controls, reusable-depth sweep |
| [**miniF2F-v2c**](https://github.com/roozbeh-mohit/miniF2F_v2) | Natural Lean transfer | 120 predeclared test theorems; expand to full test if positive | Corrected statements, exact Lean verification, manageable scale. citeturn690539search1 |
| [**PutnamBench**](https://github.com/trishullab/PutnamBench) | Optional 30-day hard transfer | 32–64 deterministic Lean theorems | Harder undergraduate mathematics and less saturation; not required in week one. citeturn690539search2turn690539search20 |
| [**TheoremBench**](https://arxiv.org/html/2606.09450v1) | Optional dependency-rich transfer | Small curated subset after infrastructure validation | Tests longer, dependency-rich developments beyond contest problems. citeturn690539search23 |

### 13.2 Model family

**Primary prover:** [Goedel-Prover-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Prover-V2-8B).

Reasons:

- open-source 8B scale is practical on the cluster: serve one worker per 4090 with memory-efficient inference/quantization where needed, or use two-GPU workers for long-context BF16 runs;
- specifically trained for Lean;
- compiler-guided self-correction and strong low-pass@$k$ performance make it a nontrivial baseline;
- eight GPUs permit several independent theorem workers, avoiding frontier-scale distributed training. citeturn690539search0turn690539search3

**Progress/value model:** [LeanProgress](https://github.com/lean-dojo/LeanProgress) or a faithful reimplementation of its remaining-step objective. Its public codebase predicts remaining proof steps and guides neural proof search. citeturn758754search8turn758754search12

**Second model after a positive initial result:** DeepSeek-Prover-V1.5-7B or another open 7B–14B Lean prover with a different training pipeline. The first week should not spend time on cross-model breadth before the mechanism exists.

### 13.3 Cost budget

A practical initial natural-task budget is:

- **8,192 generated tokens per theorem and arm**;
- **64 Lean verifier/elaboration calls**;
- **120 seconds wall-clock**, with a separately reported queue-adjusted GPU time;
- early stopping after a verified proof;
- lemma proposal, lemma proof, main proof, retries, and selector probe all debit the same budget.

The exact cap should be adjusted once Day-1 throughput is measured, but it must be frozen before seeing comparative outcomes. Report the full accuracy–cost curve at 25%, 50%, 75%, and 100% of $B$.

### 13.4 Baselines

Minimum credible baselines are:

- greedy/direct proof;
- flat best-of-$N$;
- flat beam or best-first search;
- a verifier/progress-guided search using LeanProgress;
- a stronger flat-search implementation, preferably the model’s published self-correction/search recipe;
- semantic-diversity or DPP-style flat candidate selection;
- always one-lemma;
- never one-lemma;
- failure-triggered decomposition/router inspired by ADaPT and the 2026 Lean cost-quality router;
- difficulty-only selector;
- sham expansion;
- inlined/no-cache lemma;
- hindsight oracle.

The comparison to ADaPT-style “decompose after failure” and failed-trajectory routing is essential because those systems already adapt decomposition to task/executor capability and prior failures. citeturn422412search3turn224444search2

### 13.5 Primary metrics

1. **Verified solve rate at fixed budget** $\operatorname{Solve@B}$.
2. **Area under the solve–cost curve** over preregistered budget fractions.
3. **Cut-compression ratio** $\rho=L_0/L_1$ on controlled tasks.
4. **Certified budget-crossing rate** $\Pr[L_1\le B<L_0]$.
5. **Progress inversion rate**
   $$
   \Pr[\widehat v(s_\ell)<\widehat v(s_a)\mid q_B(s_\ell)>q_B(s_a)].
   $$
6. **Causal prune effect** under frozen-graph replay.
7. **Oracle-recovery fraction**
   $$
   \operatorname{ORF}
   =
   \frac{\mathcal V(g_\phi)-\mathcal V(\text{never})}
   {\mathcal V(\text{oracle})-\mathcal V(\text{never})}.
   $$
8. **Selector regret** relative to the hindsight oracle.
9. **Brier score, ECE, and AUROC/AUPRC** for expansion advantage.
10. **Reuse validity:** fraction of generated lemmas proved, used, and actually referenced more than once.
11. **Normalized proof cost:** final proof-term/tree/DAG size after a fixed canonicalization.
12. **Verifier efficiency:** successful proofs per 1,000 verifier calls and per million generated tokens.

### 13.6 Statistical design

- **Seeds:** five search/generation seeds on controlled tasks; at least three on natural Lean.
- **Primary uncertainty:** paired, theorem-level stratified bootstrap with 10,000 resamples.
- **Binary paired comparison:** report Newcombe or paired-bootstrap confidence intervals; McNemar test only as a secondary check.
- **Multiple comparisons:** Holm correction across preregistered primary arm contrasts.
- **Selector evaluation:** nested cross-fitting by theorem family; never split individual rollouts from one theorem across train and test.
- **Difficulty control:** conditional logistic regression or doubly robust treatment-effect estimation with theorem length, root uncertainty, base pass@$k$, predicted remaining steps, and topic as covariates.
- **Effect heterogeneity:** report by reuse depth/fan-out, not only a pooled average.

### 13.7 Compute estimate

The experiment should be budgeted in **generated tokens and verifier calls**, not optimistic throughput claims. A reasonable upper envelope is:

| Work item | Generated-token envelope | GPU estimate | Other compute |
|---|---:|---:|---:|
| Controlled benchmark generation/search | 3–8M | 15–50 GPU-hours | modest verifier CPU |
| Candidate-graph construction and scoring | 2–5M | 10–35 GPU-hours | 20–80 CPU-hours |
| 120-theorem natural experiment, all primary arms/seeds | 12–25M | 60–160 GPU-hours | 100–300 CPU-hours for Lean |
| Small selector training/calibration | negligible–2M | 2–20 GPU-hours | negligible |
| Contingency and reruns | 20% | 20–50 GPU-hours | proportional |
| **Total** | **17–40M** | **approximately 100–250 GPU-hours** | **ordinary host CPU required for Lean verification** |

With eight GPUs, 100–250 GPU-hours corresponds to roughly 12.5–31.25 hours of fully utilized eight-GPU wall time, but real wall time will be longer because theorem verification, failed compilations, batching inefficiency, and orchestration create idle periods. The Day-1 microbenchmark must replace these planning estimates with measured throughput.

“GPU-only” here means no robot or special physical system. Lean’s trusted kernel and elaborator run on ordinary host CPUs; this is unavoidable but does not require specialized hardware.

---

## 14. Compute-fair comparison rules

A reviewer should be able to reconstruct every unit of test-time cost.

### 14.1 Primary cost ledger

For every theorem and arm, log:

- input and output tokens;
- model forward-pass FLOPs or a documented proxy;
- number of model calls;
- number of generated candidates;
- Lean elaboration/verifier calls;
- Lean CPU seconds;
- GPU active seconds;
- wall-clock time;
- peak GPU memory;
- selector/probe cost;
- lemma proposal, lemma proof, and failed lemma costs;
- retrieval/indexing cost if any is later added.

### 14.2 Budget matching

1. **Same model weights.** No stronger model only in the expanded arm.
2. **Same context access.** Both arms see the same theorem, imports, and retrieval corpus.
3. **All expansion overhead counts.** Proposal, type-checking, proving, storage, and use debit $B$.
4. **Early stopping applies to all.** Saved compute is part of the result.
5. **Matched verifier calls.** Extra-sampling receives any calls not used by lemma generation.
6. **Matched generated tokens.** A longer lemma prompt is not free.
7. **Matched candidate count where testing priorities.** Frozen-graph replay uses identical candidates.
8. **Matched semantic diversity.** Compare against clustered/DPP-selected flat trajectories, not only IID samples.
9. **No hidden oracle at test time.** Hindsight oracle is analysis-only.
10. **Pinned infrastructure.** Same Lean/Mathlib version, compiler flags, timeout policy, and hardware queue.
11. **Report a frontier, not one operating point.** Accuracy versus tokens, verifier calls, FLOPs, and wall time.
12. **Do not pool labeling compute with test compute.** Report offline oracle-labeling/training cost separately.

### 14.3 Three distinct fairness experiments

**Compute-matched:** all arms receive exactly budget $B$.

**Outcome-matched:** compare cost required to reach a common solve rate.

**Overpowered-base:** give flat search $2B$, $4B$, and $8B$ to test whether a small expansion remains superior even when the base is favored.

### 14.4 Diversity control

Estimate semantic diversity using normalized proof sketches or tactic-sequence embeddings. Construct an A3 flat set whose diversity distribution matches the expanded arm. If the expansion gain disappears, the correct conclusion is “diverse planning helped,” not changed bounded reachability.

### 14.5 Inlining and caching control

Compile a successful hierarchical proof into:

- a shared proof DAG;
- a fully inlined proof tree;
- a version where the lemma may be referenced only once.

The mechanism predicts that reuse-sensitive gains correlate with DAG/tree expansion and weaken when sharing is removed.

---

## 15. Expected positive, negative, and ambiguous outcomes with explicit GO/NO-GO thresholds

### 15.1 Stage A — exact controlled separation, deadline end of Day 2

**GO only if all hold:**

1. On reusable positives at moderate depth, median $L_0/L_1\ge8$.
2. At least 70% of positives cross the chosen budget: $L_1\le B<L_0$.
3. Matched no-reuse controls have median ratio $<1.5$.
4. Inlining or disabling reuse removes at least 70% of the success/cost advantage.
5. An 8× flat budget closes at most 25% of the controlled success gap at the target depth.

**NO-GO if:**

- the one-cut system wins mainly because the benchmark directly reveals the cut;
- no-reuse controls show similar gains;
- the gap is only prompt length or compression accounting;
- exhaustive search finds short cut-free proofs within $B$ for most positives.

### 15.2 Stage B — progress inversion and causal pruning, deadline end of Day 4

**GO only if all hold:**

1. Useful cut successors are ranked below matched local successors on at least **65%** of positive pairs, with 95% CI lower bound above **55%**.
2. Their estimated fixed-budget continuation success is at least **15 percentage points** higher on average.
3. Frozen-graph replay with cut-aware ranking improves controlled solve rate by at least **10 points** at identical node/token/verifier caps.
4. The inversion rate increases with exact reuse ratio $\rho$ after controlling for state size.
5. Sham cuts do not show the same continuation advantage.

**NO-GO if:**

- a calibrated LeanProgress/value baseline already ranks the useful cut correctly;
- the effect disappears under frozen candidates;
- only crude metrics such as number of goals fail, while strong learned values do not;
- inversion occurs only on constructions whose label is lexically obvious.

### 15.3 Stage C — natural Lean transfer, deadline end of Day 7

**Full 30-day GO only if:**

1. Hindsight one-lemma selection beats never-expand by at least **8 absolute solve-rate points** at matched cost on the preregistered miniF2F-v2c subset, or reduces cost by at least **20%** at parity solve rate.
2. The learned selector recovers at least **40%** of the oracle improvement.
3. It beats always-expand by at least **3 solve-rate points** or **15% cost** at parity performance.
4. Stronger flat search and diversity matching recover less than **50%** of the oracle expansion gain.
5. The advantage selector improves treatment-effect AUROC by at least **0.05** over a capacity-matched difficulty-only model, or yields a statistically better policy value after conditional adjustment.
6. The primary paired 95% CI excludes zero and the result is not driven by fewer than ten theorems.

**Immediate NO-GO if any occurs:**

- extra flat sampling/search recovers **80% or more** of the gain;
- always-expand dominates the selector at all costs;
- natural effect is below **5 points** and its CI crosses zero;
- useful lemmas are rarely independently proved or rarely reused;
- the selector only learns theorem length/base failure;
- the effect vanishes with a second random seed or after fixing leakage/benchmark bugs.

### 15.4 Interpreting intermediate outcomes

| Outcome | Interpretation | Decision |
|---|---|---|
| Exact controlled gap, no value inversion | Cuts compress proofs, but standard values already understand them. | **NO-GO for CIPI** |
| Value inversion, no search consequence | Interesting diagnostic, but not operationally important. | Workshop/analysis only; **do not spend 30 days** |
| Synthetic causal effect, no Lean transfer | Controlled proof-complexity result; likely too toy for ICLR main. | **Stop or redirect to logic/ATP venue** |
| Lean oracle gain, learned selector fails | Operator headroom exists but diagnosis is unsolved. | One additional week maximum; no method claim yet |
| Always-expand wins | Lemmas are broadly useful, but no minimal expansion result. | **Pivot to prover engineering or stop** |
| Selector beats both extremes but flat search closes gap | Adaptive compute allocation, not operator deficiency. | **NO-GO under current framing** |
| Full controlled + natural + selector + fairness package succeeds | Genuine residual survives. | **Authorize 30-day plan** |

---

## 16. Strongest reviewer attacks and the evidence required to survive them

The rejection case below is intentionally harsher than a normal internal review. Passing it is the point of the project.

| Reviewer attack | Why the attack is credible | Evidence required for survival |
|---|---|---|
| **“This is just hierarchical planning.”** | A lemma or subproof is a temporally extended action; the selector is a meta-controller. Options and hierarchical proof decomposition already provide this language. | Concede the hierarchy. Make the contribution the **specific estimator failure**: show that a standard progress/value model systematically reverses the ranking of reusable-cut versus local-progress states; intervene only on that score; recover success without changing candidate generation; predict when the inversion occurs from a structural reuse statistic. |
| **“This is just adaptive tool use.”** | `introduce lemma` can be described as calling a proof-construction tool. | Use no external information source and no privileged solver in the primary treatment. The treatment is a typed proof-theoretic operation inside the same verifier, model family, theorem environment, and information set. Charge lemma proposal and proof fully. A tool-use interpretation remains possible, but it no longer explains away the measured progress inversion. |
| **“This is just test-time compute allocation.”** | The expanded route consumes extra tokens and verifier calls. Rational metareasoning already optimizes this tradeoff. | Publish complete token, node, verifier-call, FLOP-proxy, memory, and wall-clock ledgers. Compare at identical caps and across Pareto curves. Give the flat system 2×, 4×, and 8× budget. Show that the operator intervention wins at the same cost and that the empirical gap tracks proof reuse rather than raw expenditure. |
| **“The theorem was never unreachable; your model just assigned it low probability.”** | In Lean, most surface restrictions do not establish logical impossibility; a sufficiently clever flat proof may exist. | Never claim mathematical unreachability on natural Lean. Use **exact $B$-reachability** only in the finite controlled calculus where shortest costs are exhaustively certified. In Lean, use “operator-policy-relative fixed-budget deficit,” report empirical confidence intervals, and explicitly leave open the existence of longer flat proofs. |
| **“The auxiliary operator only increases trajectory diversity.”** | A lemma prompt may simply elicit different ordinary completions. | Use four controls together: frozen candidate-graph replay; semantic-diversity matching; an equal-cost sham operator; and proof-DAG inlining/no-cache ablations. Normalize verified proofs before measuring. The core effect must disappear when sharing is removed, not merely when wording changes. |
| **“Your oracle analysis is circular.”** | Labeling an instance as lemma-needing after observing which method solved it can manufacture headroom. | In CutBench-S, construct the oracle from exhaustive shortest-path computation before model evaluation. In Lean, call it a **hindsight empirical oracle**, keep it analysis-only, derive it from disjoint generation seeds, and never train/test a selector on the same outcome rollouts. Report selector performance against both the oracle ceiling and prospective held-out policy value. |
| **“The selector merely predicts problem difficulty.”** | Hard theorems are more likely to fail flat search and to benefit from any extra procedure. | Train a capacity-matched difficulty-only baseline on base pass rate, statement length, state size, and predicted proof length. Use randomized/cross-fitted treatment data and predict $Y_1-Y_0$, not $Y_0$. Compare within narrow base-difficulty strata and matched pairs. Require incremental treatment-effect accuracy and policy value after conditioning on difficulty. |
| **“The comparison is compute-unfair.”** | Always-expand may secretly receive two proofs, more context, or additional verifier feedback. | Count every generated token, rejected syntax, lemma attempt, theorem retrieval, verifier invocation, search node, and retry. Include the selector’s own inference cost. Enforce per-instance hard caps rather than only matching average cost. Provide accuracy–cost curves and a reproducible accounting script. |
| **“New terminology hides an old metareasoning problem.”** | At the meta level, the objective is indisputably value of computation or algorithm selection. | Say so in the abstract and related work. Do not claim a new general decision framework. Claim only a previously undocumented **structural misspecification of proof-progress estimators**, its causal consequence, and a targeted correction. If the experiment does not reveal that misspecification, drop the paper. |
| **“The billiards metaphor contributes no science.”** | Correct. It neither defines an operator nor yields a theorem. | Remove it after at most one motivation sentence. The title, abstract, formalization, benchmark, and method should be intelligible without billiards. |
| **“Your base operator restriction is artificial.”** | Banning `have` or similar syntax can trivially create an advantage for a lemma operator. | Separate two claims. The controlled calculus uses an explicit proof system to establish exact finite-budget facts; it is not presented as natural Lean. Natural transfer uses ordinary Lean verification and compares search procedures, not logical languages. Include alias, no-reuse, direct-easy, and inlining controls so the controlled effect is not a parser trick. |
| **“LeanProgress is a straw man.”** | A single progress predictor may be outdated or trained without hierarchical traces. | Evaluate at least: a hand-designed heuristic, LeanProgress, a verifier-trained outcome model, and a model retrained on hierarchical/cut traces. The effect should survive at least one strong learned baseline, or the paper should become a narrower data-distribution finding rather than a general claim. citeturn758754search0turn585552search3 |
| **“Your synthetic family is hand-crafted to prove the answer.”** | A benchmark can encode its label lexically or structurally. | Generate blinded isomorphic/alias variants, balance superficial statistics, include no-reuse and sham families, hide generator parameters from the selector, and test out-of-distribution depths and symbol permutations. Then require natural Lean transfer. |
| **“The final Lean proof contains a lemma, but flat Lean could also write that lemma.”** | Surface proof syntax is not a clean operator boundary. | Define the treatment as a search protocol: independently propose, verify, cache, and reuse an intermediate theorem with a separately budgeted subsearch. Compare against a flat generator that is allowed ordinary Lean syntax but does not receive the cached verified subproblem interface. Normalize final proof terms and avoid claims about logical expressivity. |
| **“Lemma proposal quality, not valuation, explains everything.”** | A stronger proposal prompt may produce better proof content. | Run the primary causal experiment on a **frozen common candidate set** containing the same local and lemma edges. Change only ranking/pruning. Separately report candidate-generation recall. A generation improvement can be a secondary result, never the evidence for CIPI. |
| **“The gain comes from theorem retrieval or library leakage.”** | Generated lemmas may reproduce existing library facts. | Record all imported declarations and exact dependency graphs; deduplicate generated lemmas against available theorems up to definitional equality or normalized statement similarity; report results both with and without retrieval. A useful retrieved theorem is tool use, not invented structural expansion. |
| **“miniF2F is saturated or contaminated.”** | Modern open provers report high miniF2F performance, and the original benchmark has known statement-quality issues. | Pin the corrected miniF2F-v2c version, disclose model-training overlap uncertainty, use low-budget per-instance evaluation rather than pass@large, and confirm on a harder independent set such as a preregistered PutnamBench or TheoremBench subset. citeturn690539search0turn690539search1turn690539search2turn690539search23 |
| **“The oracle gain is concentrated in a handful of examples.”** | Small formal benchmarks are vulnerable to outliers. | Report theorem-level paired bootstrap intervals, the number needed to benefit, distribution of per-instance effects, leave-one-family-out results, and a minimum count of independently benefiting theorems. Do not headline an aggregate gain driven by fewer than ten natural tasks. |
| **“A stronger value model or MCTS would solve this.”** | Existing systems combine proof-state values, recursive decomposition, MCTS, or cost-aware routing. citeturn758754search3turn224444search1turn224444search2turn224444search3 | Include an outcome/value model trained on full continuation success, MCTS or best-first search with matched nodes, and a cut-aware retrained value. The residual claim survives only if local-progress bias remains measurable or the structural feature improves the strongest matched baseline. |
| **“The theory paper already proves your result.”** | Sonoda et al. already prove exponential flat-versus-hierarchical sample-complexity separation under reusable proof-DAG structure. citeturn224444search0 | Position that result as motivation and a boundary condition. The new paper must empirically identify *which learned estimators fail*, causally connect the failure to pruning in realistic verified search, and learn a prospective minimal-expansion policy. A restatement or empirical illustration of the separation is insufficient. |

### 16.1 Rejection draft a skeptical reviewer could reasonably write

> The paper repackages hierarchical proof search as “reachability expansion.” Its lemma operator adds computation and diversity, while the claimed oracle is defined from the same trials used to evaluate it. The base prover is artificially prevented from expressing reusable structure, and the learned router appears to predict theorem difficulty. Existing work already decomposes formal proofs, learns auxiliary lemmas, routes compute, predicts proof progress, and proves theoretical separations between flat and hierarchical provers. The experiments do not establish unreachability, and the billiards metaphor has no technical role.

The submission should be considered defensible only when every factual premise of that paragraph is either explicitly conceded and scoped away or experimentally falsified.

---

## 17. Thirty-day project plan, conditional on a positive first week

This plan is **not** authorization to run for thirty days automatically. Each gate can terminate the project.

### Days 1–7: complete the falsification sprint

Deliverables:

- CutBench-S generator, exact verifier, dynamic-programming shortest-cost oracle, and all four control families;
- frozen candidate graph construction;
- never/always/flat-search/diversity/sham/inlining baselines;
- LeanProgress and at least one outcome-value baseline;
- preregistered miniF2F-v2c subset and complete compute ledger;
- a one-page decision report applying §15 thresholds without reinterpretation.

**Gate G1:** stop unless Stages A and B pass and Stage C shows either the stated natural effect or unusually clear oracle headroom that is not recovered by flat search.

### Days 8–10: replication, hygiene, and benchmark freeze

1. Re-run the controlled and natural experiments from clean environments and fresh random seeds.
2. Audit proof normalization, verifier caching, token accounting, timeouts, and accidental library access.
3. Freeze benchmark generation, all split hashes, model checkpoints, prompts, search hyperparameters, and outcome definitions.
4. Expand from the 120-theorem subset to the complete feasible miniF2F-v2c test split.
5. Produce per-theorem traces for every claimed useful cut and manually inspect a blinded sample.

**Gate G2:** stop if the primary effect changes sign, falls below half its initial magnitude, or depends on a small implementation artifact.

### Days 11–14: second model and second natural benchmark

1. Replicate with a second open prover from a meaningfully different lineage, for example DeepSeek-Prover-V1.5-7B or another reproducible 7B–14B Lean model.
2. Run a preregistered, difficulty-balanced subset of PutnamBench or TheoremBench; do not select examples based on observed lemma benefit.
3. Re-estimate the oracle ceiling, selector value, inversion rate, and flat-search recovery.
4. Test cross-model transfer: train the selector on model A and evaluate on model B with only calibration, not full retraining.

**Gate G3:** continue only if the direction of the effect replicates on the second model and either the second benchmark or a clearly harder miniF2F stratum. A single-model artifact is not an ICLR project.

### Days 15–18: isolate selector learning from value learning

1. Train three matched predictors:
   - base difficulty $\widehat p_0$;
   - expanded success $\widehat p_1$;
   - direct treatment advantage $\widehat A=\widehat p_1-\widehat p_0$ or a doubly robust treatment-effect estimator.
2. Add structural features only after statement/state encoders are fixed: predicted subgoal reuse, repeated normalized subexpressions, dependency fan-out, separator/bottleneck statistics, and DAG/tree expansion proxies.
3. Evaluate cross-fitting, calibration, selective-risk curves, policy regret, and capacity-matched difficulty controls.
4. Retrain the value model on hierarchical traces. This is a crucial adversarial test: perhaps the “failure” is merely missing training support.
5. Test abstention: when selector uncertainty is high, allocate a small diagnostic probe rather than always expanding.

**Required result:** structural or treatment-aware prediction must improve actual policy value, not merely AUROC.

### Days 19–21: theory and structural criterion

Aim for one modest but real theorem, not decorative notation. Two plausible targets are:

#### A. Local-observation indistinguishability

Construct paired proof states whose radius-$h$ local features and immediate progress signals are identical, but whose optimal action differs because one candidate subgoal will be reused $k$ times. Prove that any $h$-local scorer must incur nonzero ranking error, while a reuse-aware scorer separates the pair.

#### B. Reuse-driven budget phase transition

For a recursive family with subproof cost $m$ reused $k$ times, characterize when

$$
L_{\mathrm{cut}}=m+c_{\ell}+O(k)
\quad\text{and}\quad
L_{\mathrm{flat}}=\Omega(km),
$$

or an exponential analogue. Derive a threshold $B$ for which $L_{\mathrm{cut}}\le B<L_{\mathrm{flat}}$, and connect the threshold to measured search success.

The theorem must not duplicate the existing exponential separation result; it should target the **information available to a progress estimator or selector**. citeturn224444search0

**Gate G4:** if neither a robust selector nor a meaningful estimator theorem emerges, downgrade the project to a diagnostic/benchmark paper.

### Days 22–24: optional cross-domain transfer

Run this only after the theorem-proving result is stable. The cleanest transfer is verified code, not open-ended software agents:

- choose small proof-carrying program tasks where introducing a helper specification/function creates a reusable verification boundary;
- compare local monolithic proof repair against independently verified helper abstraction;
- use exact compiler/proof verification and the same frozen-candidate/ranking protocol;
- test whether local value models undervalue a temporary increase in obligations that later shortens both program and proof.

P³ already jointly plans programs and proofs, so the transfer contribution cannot be “structural planning helps verified code.” It must be the same progress-inversion mechanism and diagnostic across domains. citeturn885201search1

**Gate G5:** abandon cross-domain claims if the operator cannot be normalized or if extra code diversity explains the result.

### Days 25–27: phase diagram and scaling analysis

Map the phenomenon over:

- reuse fan-out $k$;
- sublemma proof cost;
- direct proof depth;
- model size/checkpoint;
- search budget;
- value-model training distribution;
- lemma proposal recall and false-positive rate;
- always-expand overhead.

The desired product is a **predictable phase diagram**, not a single benchmark bar chart. At minimum, fit held-out curves showing where the cut crosses from harmful overhead to necessary compression and whether the selector anticipates that transition.

### Days 28–30: paper, release, and hostile reproducibility audit

Release:

- exact CutBench-S generator and verifier;
- pinned Lean environment and benchmark hashes;
- all prompts, candidate graphs, proof traces, and normalized proof DAGs;
- cost-accounting code and raw per-instance ledger;
- pretrained selectors/value models where licensing permits;
- a script reproducing every primary table and confidence interval;
- negative results and failed baselines.

Paper structure:

1. one-paragraph motivation, with no dependence on billiards;
2. operational definition and explicit non-claims;
3. controlled exact separation;
4. progress inversion and causal replay;
5. natural Lean transfer and adaptive selector;
6. theory/structural criterion;
7. compute fairness and adversarial ablations;
8. limitations, including policy-relative rather than logical unreachability.

---

## 18. Contribution thresholds

### 18.1 Minimum publishable result

A minimum defensible paper would contain:

- a public controlled benchmark with exact cut/no-cut shortest-cost labels;
- balanced no-reuse, alias, sham, and inlining controls;
- evidence that at least one widely used proof-progress estimator ranks useful reusable cuts incorrectly;
- frozen-graph causal replay showing that the ranking error changes verified success at fixed nodes and verifier calls;
- one natural Lean study establishing that the phenomenon occurs outside the synthetic generator, even if a learned selector is not yet strong;
- transparent negative results and compute accounting.

This could be valuable to a theorem-proving, neuro-symbolic, or evaluation venue. By itself, it is **not a strong ICLR main-track contribution**. A controlled separation that merely illustrates known cut compression is closer to a workshop or automated-reasoning paper.

### 18.2 Strong ICLR main-track result

A credible main-track package requires all of the following:

1. **Previously undocumented failure mode:** multiple strong progress/value models exhibit the inversion, including at least one trained on hierarchical traces.
2. **Causal evidence:** changing ranking while freezing candidates materially changes verified success.
3. **Natural breadth:** two open 7B–14B prover families and two benchmark distributions.
4. **Compute fairness:** the adaptive method lies above never-expand, always-expand, strong flat search, and diversity-matched search on the accuracy–cost frontier.
5. **Non-difficulty diagnosis:** the selector predicts counterfactual operator advantage and yields lower policy regret than a matched difficulty router.
6. **Structural explanation:** reuse/fan-out or a related graph property predicts the effect out of distribution.
7. **Theory:** at least one nontrivial result explaining why a class of local progress estimators cannot capture the relevant future reuse.
8. **Reproducibility:** exact benchmark generation, verifier pinning, cost ledgers, and all decision thresholds released.

A gain of several benchmark points without these components is another prover engineering paper, not the proposed scientific result.

### 18.3 Plausible Oral-level result

Oral potential would require an unexpectedly broad and clean discovery, for example:

- the same progress-inversion phenomenon recurs across formal theorem proving, verified code, and perhaps program synthesis;
- a simple structural statistic predicts a sharp reuse–budget phase transition across models and search algorithms;
- a theorem establishes an information-theoretic or locality-based limitation of standard progress/value estimators;
- an adaptive selector substantially shifts the accuracy–compute frontier and the shift cannot be reproduced by 8× flat compute, stronger MCTS, a stronger outcome model, or matched semantic diversity;
- retraining on more proof traces does not remove the failure unless the model is given explicit DAG/reuse information;
- the benchmark becomes a useful stress test for process reward models and agentic reasoning systems beyond the proposed method.

Even that is only **plausible** Oral territory. Benchmark gains, a clever router, or a new acronym are not enough. The paper would need a result that changes how researchers think about process supervision: local “progress” can be anti-correlated with finite-budget solvability when reasoning constructs reusable structure.

### 18.4 What does not meet any serious threshold

The following outcomes should not be dressed up as novelty:

- lemma prompting improves pass@k;
- always decomposing beats direct proof generation;
- a router saves tokens by sending hard problems to a stronger strategy;
- more branches improve diversity;
- generated lemmas resemble library retrieval;
- a synthetic DSL is unsolvable after deliberately deleting a required primitive;
- a value model trained without cut examples improves after training on cut examples, with no broader mechanism;
- the method wins only under average-cost matching while violating per-instance caps.

---

## 19. Final recommendation on investing the 8×4090 cluster

### 19.1 Authorized investment

**Authorize one bounded falsification sprint:**

- **Duration:** no more than seven calendar days;
- **GPU budget:** approximately **100–250 aggregate RTX-4090 GPU-hours**, adjusted after the Day-1 throughput measurement;
- **Model scale:** one 8B prover for the primary run, with a second 7B–14B checkpoint only if the first two gates pass early;
- **No training from scratch:** inference, small value/selector fine-tuning, and controlled benchmark generation only;
- **No open-ended agent engineering:** every component must answer one of the A/B/C/D causal distinctions in the prompt;
- **Hard stop:** apply §15 thresholds without moving them after results are seen.

This is a sensible use of the cluster because the core hypothesis can be killed cheaply. Exact controlled search should reveal within two days whether the supposed reachability distinction is real or merely an artificial prompt effect. Frozen-graph replay should reveal by Day 4 whether progress/value ranking is causally implicated. The natural Lean subset should reveal by Day 7 whether the phenomenon matters outside a constructed proof system.

### 19.2 Not authorized yet

Do **not** authorize:

- a month of general theorem-prover development;
- large-scale supervised fine-tuning on newly generated proofs;
- a custom foundation-model pretraining run;
- a multi-agent framework;
- a code-agent/SWE-bench implementation before the theorem experiment works;
- a broad “operator expansion benchmark” spanning unrelated prompts and tools;
- a paper organized around the billiards taxonomy.

Those paths are expensive and collision-prone, and they weaken causal identification.

### 19.3 Decision after the first week

| Week-one outcome | Cluster decision |
|---|---|
| Stage A fails | **Stop immediately.** The operational separation is not clean. |
| Stage A passes, Stage B fails | **Stop CIPI.** Known proof compression exists, but the claimed estimator failure does not. |
| A/B pass, natural oracle headroom is negligible | **Stop or redirect to ATP theory.** Not an ICLR AI project. |
| Natural oracle headroom exists, selector fails | Permit **one additional week** focused only on treatment-effect diagnosis; no full project yet. |
| Selector beats both extremes but flat search recovers the gain | **Stop reachability framing.** This is adaptive compute allocation. |
| All Stage C criteria pass | **Authorize the 30-day plan.** |

### 19.4 Final investment judgment

The expected value is positive only because the proposed first experiment is sharply bounded and falsification-first. The broad research program is not worth the cluster. The narrow CIPI hypothesis is worth a small, disciplined bet.

---

## 20. Unresolved questions that genuinely require experiments

1. **Do strong learned proof-progress estimators actually undervalue useful lemma/cut introduction, or only crude hand-designed metrics such as open-goal count?**
2. **Does the inversion persist after the value model is trained on hierarchical proof traces with explicit reusable lemmas?**
3. **Is there a predictable phase transition in reuse fan-out, lemma cost, and budget where the locally worse transition becomes globally necessary?**
4. **Can a selector predict counterfactual expansion advantage before any failed trajectory is observed, rather than simply detecting hard theorems?**
5. **How much of the gain remains after matching semantic trajectory diversity and proposal entropy?**
6. **Does frozen-candidate reranking recover the same gains as a full lemma-generating agent, establishing valuation rather than generation as the bottleneck?**
7. **How should Lean proof terms be canonically normalized into tree and DAG cost measures without accidentally charging syntax rather than proof work?**
8. **Are independently provable and multiply reused intermediate lemmas common enough in natural benchmarks to support a practical adaptive policy?**
9. **Does always enabling lemma generation hurt because of proposal noise and budget dilution, or does it dominate once the prover is strong enough?**
10. **Can a locality or observability lower bound be proved for progress estimators on paired proof states with identical local features but different future reuse?**
11. **Does the phenomenon transfer to verified program construction, where a helper abstraction temporarily creates more obligations but shrinks the joint program–proof search?**
12. **Is the effect robust to theorem retrieval, richer imported libraries, and stronger automation, or does library maturity erase the need for invented cuts?**
13. **Does model scale reduce the deficit by internally planning reusable structure, or increase it by making local progress scores more confidently wrong?**
14. **Can calibrated uncertainty identify when none of the available expansion operators is useful, preventing an always-more-complex policy?**
15. **What fraction of apparent operator deficits are actually proposal-support failures, value-ranking failures, verifier bottlenecks, or simple insufficient search?**

---

## Final verdict

The seed contains a useful scientific instinct—distinguish spending more effort inside a fixed reasoning regime from changing the operational structure of the search—but that instinct is not a new general AI principle. In its broad form, the proposal is already rational metareasoning, hierarchical planning, adaptive tool use, decomposition, representation routing, or proof search under another name.

The only residual direction I recommend testing is narrower and harsher:

> **A reusable lemma/cut may be the only short route within a fixed proof-search budget, yet standard local progress/value models may score its introduction as regression and causally prune it.**

That claim is novel enough to test only because it demands an exact controlled oracle, a measured ranking inversion, frozen-graph causal intervention, full compute and diversity controls, prospective treatment-effect selection, and natural Lean transfer. It is also close enough to existing cut-aware theorem-proving work that failure on any one of those dimensions should terminate the project.

**Decision:** **PIVOT. Invest the 8×4090 cluster for one 3–7 day falsification sprint, capped at roughly 100–250 aggregate GPU-hours. Do not authorize the full project unless every Stage C gate passes.**
