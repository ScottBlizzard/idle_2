# Executive Verdict

**Document date:** 2026-08-25 (Asia/Tokyo)  
**Compute constraint:** exactly eight independent NVIDIA RTX 4090 GPUs, each with 24 GB VRAM; no NVLink, no memory pooling, and no assumed cloud compute.  
**Decision:** **CONDITIONAL GO — authorize only the 1–3 day falsification pilot. Do not authorize the full experiment program until every pilot gate below is passed.**

## Recommendation hierarchy

| Rank | Direction | Verdict | Why it survives | Main danger |
|---|---|---|---|---|
| 1 | **Basin-First Adaptive Planning (BFAP): utility-constrained multiresolution action parameterization for finite-budget model-predictive planning** | **Primary; pilot authorized** | It converts the billiard intuition into a measurable distinction between nominal action-sequence expressivity and the robust probability mass of near-successful plans. It makes a sharp, cheap, non-monotonic prediction and can be tested with exact state dynamics and standard sampling-based planners. | Reviewers may conclude that it is merely spline smoothing or action repeat unless the paper measures success-set geometry, enforces a strict utility floor, and demonstrates an adaptive selector rather than a hand-tuned fixed basis. |
| 2 | **Bridge-Preserving Reduced Datasets for Offline RL (BriCoRe)** | **Backup A** | It predicts that low-return transitions can be more valuable than high-return trajectories when they preserve graph connectivity needed for stitching. Public offline-RL suites and strong baselines make the claim rapidly testable. | ICLR 2025 ReDOR, ICML 2025 GAS, and trajectory-stitching work make the novelty margin narrow. The contribution must be a connectivity-preserving subset objective, not generic data pruning. |
| 3 | **Capture-Region Relay Planning (CRRP): set-valued predecessor subgoals under an unchanged final goal** | **Backup B** | It directly operationalizes backward propagation of reachability: an intermediate region may enlarge the upstream capture basin even when the final goal, horizon, and utility threshold remain fixed. | Skill chaining, initiation sets, graph search, and 2026 work on learned goal subsets, quasimetrics, spectral bottlenecks, and subset-valued goal languages already cover much of the surrounding space [R13–R16]. A merely “larger subgoal” method is not novel. |

## Binding interpretation

The seed should **not** be framed as ordinary error attenuation. The useful object is the **measure and robustness of a successful preimage under a fixed resource and utility budget**. In planning language, the question is whether a representation or sequence of intermediate constraints reshapes the set from which a finite-budget optimizer can discover a successful plan.

The primary paper is viable only if it establishes all three facts simultaneously:

1. **Finite-budget inversion:** a nominally more expressive, full per-time-step action space performs *worse* than an intermediate-dimensional action basis under the same simulator-call budget.
2. **Nontrivial capability preservation:** the winning basis retains at least 95%—preferably 98%—of the high-budget attainable utility of the full action space, so the gain is not purchased by making the task weaker or exhausting action magnitude.
3. **Mechanistic prediction:** a measured robust near-optimal preimage-mass statistic predicts planner success across action bases, tasks, and budgets better than smoothness, dimensionality, or best sampled return alone.

A result satisfying only item 1 is an engineering observation. Items 1–3 together could support a strong scientific contribution.

## Gate audit

| Gate | Current assessment | Pilot pass condition |
|---|---|---|
| Novelty | **Conditional pass.** Fixed spline, low-pass, latent-action, learned-proposal, and covariance-design methods are established, but the search found no work that jointly defines normalized robust success preimage mass, imposes an explicit high-budget capability-retention constraint, and selects the action basis online under the same rollout budget. Absence from the searched record is not proof of nonexistence. | Final adversarial search still finds no functional duplicate; method beats both fixed structured controls and strong sampler-design baselines. |
| Meaning | **Pass by design, not yet by evidence.** | Gains survive matched action norm, total variation, path length, horizon, terminal tolerance, simulator calls, and executed steps; restricted bases meet the utility floor. |
| Pilot | **Pass.** | One exact-model experiment can produce or kill the predicted inverted-U relation within 1–3 days. |
| Benchmark | **Pass.** | Use DM Control/MuJoCo or MJX tasks, PushT, and public planner implementations; no custom dataset is needed. |
| Compute | **Pass.** | Pilot remains within 2–8 GB VRAM per process and 60–120 aggregate GPU-hours; full plan remains within approximately 2,000–3,200 GPU-hours. |
| Story | **Conditional pass.** | The evidence chain is: expressivity–mass trade-off → measured basin geometry → adaptive basis choice → fixed-budget success. |
| Robustness | **Conditional pass.** | Effect appears on at least two of three pilot tasks and later across two environment families and two planners. |

## Immediate decision rule

Proceed to the full package **only** when the pilot shows, on at least two of three tasks:

- an intermediate basis improves strict task success by at least **10 percentage points** over full per-step control at a fixed tight rollout budget;
- the improvement survives matched utility, action-energy, smoothness, horizon, and execution-length controls;
- the high-budget capability-retention ratio is at least **0.95**;
- robust preimage mass correlates with seed-level planning success with **Spearman $\rho \ge 0.4$** and a confidence interval not crossing zero.

Otherwise, stop the primary direction. Switch to Backup A only if its own pilot gate is independently passed. Do not turn a failed primary result into a vague “structured actions are smoother” paper.

## Evidence labels used throughout

- **[V] Verified fact:** directly supported by an official proceedings page, paper, project page, or repository listed in the bibliography.
- **[J] Literature-supported judgment:** an interpretation based on several verified sources.
- **[I] Inference:** a reasoned conclusion from the literature and constraints, not itself established by a cited experiment.
- **[H] Untested hypothesis:** a prediction this project must test.

# Idea Seed and Correct Abstraction

## 1. From billiards to a formal AI question

The seed intuition is that a narrow downstream success region may have a larger upstream preimage after introducing intermediate contacts, states, or degrees of freedom. The billiard picture is useful only insofar as it points to four precise objects:

1. a **terminal success set**;
2. a **map from upstream choices to terminal outcomes**;
3. the **preimage** of success under that map;
4. a **resource or utility constraint** that prevents a fake gain caused by damping, slowing, shortening, or simplifying the task.

For a finite-horizon controlled system,

$$
x_{t+1}=f(x_t,u_t), \qquad u_t\in\mathcal U\subseteq\mathbb R^m,
$$

let $U=u_{0:H-1}\in\mathcal U^H$ be a full action sequence and let $J_x(U)$ be task utility from initial state $x$. For a required utility $\tau$ and hard constraints $C_x(U)\le 0$, define the successful action-sequence set

$$
\mathcal S_\tau(x)
=
\{U\in\mathcal U^H: J_x(U)\ge \tau,\; C_x(U)\le 0\}.
$$

A lower-dimensional action representation uses a decoder

$$
D_k:\mathbb R^{mk}\rightarrow \mathcal U^H,
$$

where $k$ may be the number of temporal knots or basis coefficients. Examples include zero-order hold, piecewise-linear interpolation, cubic B-splines, discrete-cosine coefficients, and the full representation $k=H$. The success preimage in representation $k$ is

$$
\mathcal Z_{k,\tau}(x)=D_k^{-1}\big(\mathcal S_\tau(x)\big).
$$

The project does not claim that the raw Euclidean volume of $\mathcal Z_{k,\tau}$ is directly comparable across dimensions. The operational quantity is the **normalized robust hit mass under the actual proposal distribution**:

$$
\rho_k(x;\tau,\sigma)
=
\Pr_{z\sim q_k,\;\epsilon\sim\nu_\sigma}
\left[
D_k(z+\epsilon)\in\mathcal S_\tau(x)
\right].
$$

Here $q_k$ is the planner's normalized proposal over coefficients and $\nu_\sigma$ is a controlled perturbation distribution. The perturbation term tests whether a sampled success lies in a robust basin rather than at an isolated knife-edge point.

For $N$ independent proposals, the diagnostic first-hit probability is

$$
P_{\mathrm{hit}}(k,N)=1-(1-\rho_k)^N.
$$

CEM, iCEM, MPPI, and related planners adapt proposals, so this expression is not a complete model of their behavior. It is nevertheless a useful diagnostic: the early optimization iterations are dominated by the probability of landing in informative or near-successful regions, and the representation changes that probability.

## 2. Expressivity and discoverability are different

A full action sequence has a superset of the trajectories available to a restricted decoder when the restricted decoder is embedded in the full space. Therefore, its **best possible** return cannot be lower:

$$
J_H^*(x)=\max_{U\in\mathcal U^H}J_x(U)
\ge
\max_{z\in\mathbb R^{mk}}J_x(D_k(z))=J_k^*(x).
$$

The default inference from this fact is that more action degrees of freedom should help. That inference ignores finite search. Extra dimensions may create broad regions of irrelevant, oscillatory, dynamically cancelling, or constraint-violating action variation. The optimum remains present, but the normalized probability mass of useful plans may shrink.

A simple box model makes the mechanism explicit. Suppose $r$ directions materially control task outcome and $n$ additional directions must accidentally remain within narrow tolerances. If the proposal range in direction $i$ is $R_i$, useful widths are $\delta_i$ in relevant directions and $\eta_j$ in nuisance directions, then

$$
\rho_{\mathrm{full}}
\approx
\prod_{i=1}^{r}\frac{\delta_i}{R_i}
\prod_{j=1}^{n}\frac{\eta_j}{R_j}.
$$

A decoder that removes nuisance directions while approximating the required trajectory can multiply hit mass by

$$
\prod_{j=1}^{n}\frac{R_j}{\eta_j},
$$

which can be exponentially large in $n$. But an overly restrictive decoder also incurs approximation error. If $J_x$ is locally $L$-Lipschitz in action-sequence norm and the closest decoded sequence to an optimal full sequence has error $\epsilon_k$, then

$$
J_H^*(x)-J_k^*(x)\le L\epsilon_k.
$$

This yields the predicted non-monotonic trade-off:

- very small $k$: high hit mass but excessive approximation bias;
- intermediate $k$: enough expressivity and much larger robust near-optimal mass;
- $k=H$: maximal nominal expressivity but poor finite-budget discoverability.

That is the paper's correct abstraction of “intermediate balls enlarge tolerance.” It is not that each stage numerically shrinks error. It is that a structured map may remove nuisance directions and reshape a small downstream success set into a larger normalized upstream hit region while preserving useful capability.

## 3. Guard against trivial attenuation

The following outcomes are **not** evidence for the thesis:

- the restricted controller succeeds because it uses less action energy and simply stops before failure;
- the task horizon or terminal tolerance is relaxed;
- the restricted method executes more low-level steps or receives more replanning opportunities;
- a smooth basis is compared against deliberately rough white-noise controls without low-pass or colored-noise controls;
- the basis removes dynamic maneuvers that would be needed at high utility;
- success improves only because the reward function favors low movement;
- the adaptive selector uses extra model rollouts not charged to its budget.

Define a high-budget capability-retention ratio

$$
\kappa_k(x)=
\frac{J_{k,\mathrm{oracle}}^*(x)-J_{\mathrm{random}}(x)}
{J_{H,\mathrm{oracle}}^*(x)-J_{\mathrm{random}}(x)}.
$$

The primary claim is considered meaningful only when $\kappa_k\ge0.95$ on the affected tasks, with $0.98$ as the preferred strict threshold. “Oracle” here means a prespecified large but feasible planning budget used only for capability assessment, not access to the true solution.

## 4. Relation to reachability and funnels

Backward reachable sets, regions of attraction, and funnels formalize sets of states from which a controller can reach a target despite uncertainty. LQR-trees and funnel libraries compose verified or empirically estimated regions of attraction for feedback motion planning [P23–P25]. Skill chaining similarly learns initiation regions so that one option terminates inside the next option's initiation set [R01–R04]. These are genuine relatives of the seed.

The primary direction differs in where the set lives and what is varied:

- funnels and skill chains mainly reshape or compose **state-space** reachability using controllers or options;
- BFAP studies the **proposal-space preimage of near-successful action sequences** under a fixed task and planner budget;
- the object of selection is a temporal action decoder, not an environmental scaffold, learned option library, or relaxed terminal goal.

This distinction is functionally important. It makes the first experiment cheap: exact state dynamics and standard MPC suffice; no robot, learned skill library, or custom data collection is required.

# Search Strategy and Coverage

## 1. Retrieval protocol

The literature search was conducted iteratively while candidates were generated and eliminated, rather than selecting a preferred idea and searching only for support. Retrieval date was **2026-08-25**. The search covered 2009–2026, with emphasis on 2023–2026 and backward tracing to foundational work.

Primary and official sources were prioritized:

- OpenReview and ICLR proceedings;
- PMLR for ICML, AISTATS, CoRL, L4DC, CoLLAs, and related venues;
- NeurIPS proceedings;
- AAAI OJS and IJCAI proceedings;
- ACL Anthology;
- RSS proceedings;
- IEEE Xplore and journal pages;
- arXiv for preprints not yet in proceedings;
- official author project pages and code repositories for implementation status.

No bibliometric database was treated as authoritative when an official proceedings page was available. Preprints are explicitly labeled as preprints; workshop records are not upgraded to main-conference publications.

## 2. Mechanism-level synonym map

| Seed concept | Search terms used | Neighboring communities |
|---|---|---|
| Narrow success tolerance | success set, feasible-action set, robust success region, near-optimal set, level-set volume, capture basin, viability kernel | optimal control, rare-event optimization, robust planning |
| Backward expansion | preimage expansion, backward reachable set, predecessor set, controllable set, region of attraction, funnel | reachability, formal methods, feedback motion planning |
| Intermediate contacts or states | relay states, intermediate goals, subgoal regions, skill chaining, initiation set, terminal-set regularization | hierarchical RL, options, long-horizon manipulation |
| Composition of local reachability | funnel composition, option composition, skill graph, graph search, trajectory stitching | robotics, offline RL, planning |
| Search geometry | action-space shaping, trajectory parameterization, temporal basis, control knots, spline controls, low-pass sampling, latent actions | sampling-based MPC, black-box optimization |
| Finite-budget exploration | hit probability, proposal coverage, sample efficiency, low-discrepancy sampling, covariance design, learned proposal | CEM, MPPI, evolutionary strategies |
| Utility-preserving restriction | compressed control, action abstraction, action persistence, control frequency, action chunking, approximation regret | RL, behavior cloning, control |
| Bridge value in data | graph connectivity, articulation state, betweenness, bottleneck state, data subset, coreset, stitching transition | offline RL, active learning, dataset pruning |
| Intermediate distributions | gradual domain adaptation, intermediate domains, continuation path, homotopy | domain adaptation, optimization |
| Added constraints as benefit | bottleneck, compression, rank growth, noise schedule, restart, rewiring | representation learning, generative modeling, GNNs |

## 3. Adversarial prior-art procedure

For every candidate that reached the provisional top five, the search attempted to disprove novelty by varying:

- terminology: “action basis,” “control knots,” “spline sampling,” “latent action,” “low-frequency MPPI,” “trajectory parameterization,” and “action chunking” for BFAP;
- functional unit: fixed decoder, learned decoder, proposal covariance, temporal prior, low-discrepancy samples, global/local mixture, and adaptive control rate;
- application area: robot manipulation, locomotion, motion planning, model-based RL, offline GCRL, imitation learning, and control theory;
- venue: ICLR, ICML, NeurIPS, AAAI, IJCAI, ACL, EMNLP, CVPR, ICCV, ECCV, CoRL, RSS, L4DC, TMLR, TRO, RA-L, and IJRR;
- time: recent submissions and preprints through August 2026, plus backward citation tracing to foundational work.

A paper was treated as a duplicate based on function, not title. The audit compared problem definition, inputs and outputs, optimized objective, representation, training or planning procedure, theoretical statement, evaluation protocol, and empirical conclusion.

## 4. Venue-coverage summary for the primary idea

| Venue family | Search focus | Outcome |
|---|---|---|
| ICLR / OpenReview | latent actions, action tokenization, adaptive temporal abstraction, compact planning spaces | Several nearby representation and control-frequency papers; no exact utility-constrained robust-preimage selector found. |
| ICML / PMLR | CEM/MPPI proposal design, GCRL, offline-data selection | Strongest functional neighbors: CoVO-MPC, learned sampling distributions, MTP/TMLR, GAS, and data-quality work. |
| NeurIPS | action tokenization, offline RL, model-based planning, dataset quality | Nearby latent/action-compression and offline-RL baselines; no exact primary duplicate found. |
| AAAI / IJCAI | offline stitching, composable options, active RL | Important for backups; weaker direct overlap with BFAP. |
| CoRL / RSS | sampling MPC, manipulation, motion planning, funnels | Dense prior art on structured controls and trajectory proposals; these venues create the highest “this is just smoothing” reviewer risk. |
| L4DC / TMLR / journals | predictive sampling, covariance design, smooth priors, legged MPC | Strong mechanism and implementation neighbors; no robust near-optimal preimage-selection objective found. |
| ACL / EMNLP | bridge retrieval, value-guided multi-hop reasoning | Used to eliminate the retrieval reformulation; no direct control-space duplicate. |
| CVPR / ICCV / ECCV | action tokenization, diffusion policies, visual planning | Relevant only to learned action representations and imitation; pilot should avoid this complexity. |

## 5. Search limitations

The search found no paper that exactly combines all of the following: normalized robust near-optimal preimage mass across nested action decoders; an explicit high-budget utility-retention constraint; same-budget online decoder selection; and a cross-task prediction that intermediate action dimension is optimal under finite sampling. This is a **negative search result, not proof of novelty**. New submissions, papers with different terminology, or inaccessible manuscripts may still overlap. A fresh citation and venue search is mandatory immediately before submission.

# Literature Landscape

## 1. Sampling-based planning already recognizes proposal geometry

Sampling-based MPC methods are sensitive to their proposal distributions. iCEM adds temporally correlated noise, memory, and population decay to improve sample efficiency [P07]. Watson and Peters use Gaussian-process action priors to obtain smooth Monte Carlo control [P06]. CoVO-MPC derives covariance schedules that improve convergence [P05]. Learned sampling distributions move optimization into a learned latent proposal space [P10], and MTP mixes globally diverse structured samples with local CEM-style exploitation [P02]. C-Uniform targets configuration-space trajectory coverage [P03].

**[J] Consequence:** it is not novel to say that “sampling distribution matters,” “smooth actions are easier,” or “reduced-dimensional controls can improve MPC.” A publishable BFAP paper must isolate a new object—the robust near-optimal preimage mass under a utility constraint—and show that this object predicts when nominal expressivity hurts.

## 2. Structured and reduced action trajectories are established

Spline, interpolation, and spectral structure already appear in planning and control:

- STORM combines low-discrepancy sampling and smooth interpolation for high-dimensional manipulation [P09].
- Low-frequency and low-pass MPPI variants shape temporal spectra [P04, P29].
- Whole-body legged MPC uses spline-reduced controls [P12].
- Reference-Free Sampling-Based MPC uses a dual-space spline parameterization [P19].
- A 2026 quadruped study directly compares unstructured, linear, cubic-spline, and Bézier sampling strategies [P01].
- MTP samples and interpolates global trajectories using B-splines and Akima splines [P02].
- Predictive Sampling and the MuJoCo MPC implementation expose control knots as practical MPC interfaces [P13, S07].

**[V/J] Consequence:** “use B-splines in CEM/MPPI” is already done and should be eliminated as a paper direction. The primary contribution must be an adaptive, utility-constrained basis-selection theory and mechanism diagnostic.

## 3. Compact and learned action spaces are also crowded

TAP plans in a compact learned latent action space [P14]. Learning Sampling Distributions for MPC uses a normalizing-flow latent distribution [P10]. VQ-ACE, BEAST, and B-spline Policy compress or structure action sequences for manipulation and imitation learning [P15–P17]. Parameterized-action MBRL studies hybrid action types and continuous parameters [P26]. Action chunking and adaptive execution-frequency methods further reduce decision frequency.

**[J] Consequence:** a learned decoder alone is a weak novelty claim and adds training confounds. The pilot should use transparent fixed bases. A learned basis is a later ablation, not the central mechanism.

## 4. Reachability, funnels, and skills capture the state-space cousin

LQR-trees and funnel libraries cover state space with regions from which feedback controllers can reach target neighborhoods [P23–P25]. Skill Chaining, Deep Skill Chaining, Deep Skill Graphs, and robust composable options learn or compose initiation and termination regions [R01–R04]. Abstract Value Iteration accepts user-specified subgoal regions and plans through an abstract decision process [R10]. SoRB and imagined-subgoal methods use graph or model-based search over replay data [R05–R06].

**[J] Consequence:** the broad statement “intermediate regions enlarge reachability” is foundational, not new. CRRP survives only as a backup because it would need a new optimization criterion for *set-valued relay regions under a fixed exact final goal and fixed horizon*, with an inverted-U prediction and strict controls.

## 5. Offline-RL data quality is not monotone in return or size

D4RL made dataset quality and coverage central to offline RL [D09]. A Dataset Perspective on Offline RL separates trajectory quality from state-action coverage [D06]. ReDOR explicitly shows that reduced datasets can improve offline RL and selects data through gradient approximation and submodular optimization [D01]. DiffStitch and SSD synthesize stitching transitions [D03–D04], while GAS constructs a temporal-distance graph and filters transitions using temporal efficiency [D02].

**[J] Consequence:** “less data can be better” is already published. BriCoRe is defensible only if it predicts and tests a specific topological role: low-return bridge transitions preserve reachability between otherwise disconnected high-value components, under a fixed subset budget and without synthetic data.

## 6. Cross-disciplinary candidates mostly fail novelty or tractability

Gradual domain adaptation already studies paths through intermediate distributions and optimal adaptation routes [E01–E04]. Graph virtual nodes and rewiring already address information bottlenecks and over-squashing [E08–E09]. Dynamic rank growth and low-rank continuation are established optimization ideas [E10–E11]. Multi-hop retrieval increasingly models bridge passages and passage utility [E05–E06]. Predecessor/successor representations have been used for intrinsic exploration [E12–E13].

These neighboring areas validate the seed's generality, but they are weaker vehicles for a rapid paper because novelty margins are smaller, causal controls are harder, or compute and data confounds are greater.

# Eliminated Directions and Why

| Candidate | Attractive counterintuitive idea | Adversarial finding | Decision |
|---|---|---|---|
| Fixed spline or low-pass MPC | Fewer temporal degrees of freedom can outperform full actions. | Already instantiated by STORM, low-frequency/low-pass MPPI, legged whole-body MPC, Reference-Free MPC, MTP, and the 2026 interpolation comparison [P01–P04, P09, P12, P19, P29]. | **Eliminate as standalone idea.** Retain only as components and baselines inside BFAP. |
| Learned latent-action planning | A compressed latent space is easier to search than raw controls. | TAP and learned MPC sampling distributions directly cover compact/learned control spaces [P10, P14]; later action-tokenization work is crowded. | **Eliminate.** Too close to established work and adds training cost. |
| Predecessor/successor intrinsic exploration | Backward reachability representations create larger useful exploration regions. | Successor–predecessor intrinsic-exploration work already operationalizes this family [E12–E13]. | **Eliminate.** Functional overlap is too high. |
| Relay domains for gradual domain adaptation | Several imperfect intermediate domains can outperform one close source-target jump. | Gradual domain adaptation already analyzes self-training paths, optimal routes, and gradient-flow views [E01–E04]. | **Eliminate.** Mature problem definition. |
| Multi-hop retrieval bridge utility | A low-relevance passage can be essential because it connects evidence. | Bridge-passage and contextual-passage-utility work now directly targets this mechanism [E05–E06]. | **Eliminate.** Fast-moving and duplicate-prone. |
| Prefix-completion-volume program search | A prefix with lower immediate score can have more correct completions. | Outcome/value models and verifier-guided search already estimate prefix promise; clean evaluation would likely require large code models and expensive inference. | **Eliminate.** High confounding and cost. |
| Diffusion restart or reheat schedule | Adding noise mid-sampling can improve fixed-NFE generation. | Schedule, restart, and sampler design are heavily populated; a decisive mechanism study would require broad generative-model evaluation. | **Eliminate.** Novelty and compute risk. |
| Temporary low-rank bottleneck then rank growth | Restricting optimization early can enlarge the learnable basin. | Incremental-rank training and dynamic rank adjustment already exist [E10–E11]. | **Eliminate.** Likely rebranding without a new theorem or task. |
| GNN relay-node subdivision | Extra intermediate nodes reduce long-range difficulty. | Virtual-node, rewiring, and over-squashing work already treats this mechanism [E08–E09]. | **Eliminate.** Crowded and easy to dismiss as another rewiring heuristic. |
| Temporary environment scaffolds | Constraints or stepping stones make a harder final policy easier to discover. | Curriculum, reverse curriculum, environment design, and scaffolding are broad mature areas; proving nontrivial utility preservation is difficult without custom environments. | **Eliminate for rapid paper.** Good long-term program, poor 1–3 day falsification. |
| Topology-aware active learning | Label low-uncertainty bridge nodes instead of high-uncertainty points. | Graph-centrality and topology-aware active learning are already substantial; dataset and representation sensitivity would dominate a short paper. | **Eliminate despite feasibility.** Novelty gate fails. |
| Adaptive chunk or control frequency | Fewer decisions can improve long-horizon success. | Action persistence, adaptive control frequency, chunking, and recent commitment methods cover much of the idea. | **Eliminate as primary.** Retain as a BFAP ablation. |
| Safe Bayesian-optimization continuation | Intermediate feasible points enlarge access to a narrow optimum. | Mechanism is plausible and cheap, but the AI story is weaker, benchmark authority is lower, and it drifts toward optimization methodology. | **Park.** Possible fallback outside the current top three. |
| Multi-agent relay communication | Additional agents or messages create reachability through distributed relays. | Hard to separate from extra bandwidth, model capacity, and total compute; authoritative rapid benchmarks are less clean. | **Eliminate.** Meaning gate is difficult to satisfy. |
| LLM/VLA reasoning scaffolds | Intermediate states expand the set of prompts that succeed. | Test-time search, chain-of-thought, verifier guidance, and action tokenization are exceptionally crowded; experiments would introduce model-size and inference-budget confounds. | **Explicitly reject.** Not the best vehicle under the stated budget. |

# Candidate Scorecard

All criteria use 1–10, where 10 is favorable. For **top-tier reviewer risk**, 10 means *low* risk. The overall column is the unweighted mean; it is a triage aid, not a substitute for the gate analysis.

| # | Candidate | Functional novelty | Counterintuitive strength | Mechanism clarity | Falsifiability | Separation from prior | Benchmarks/baselines | 8×4090 feasibility | Pilot speed | Full cost | Low reviewer risk | Negative-result value | Mean |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | BFAP: utility-constrained basin-first action parameterization | 8 | 9 | 9 | 10 | 7 | 9 | 10 | 10 | 9 | 6 | 9 | **8.73** |
| 2 | BriCoRe: bridge-preserving offline-RL coresets | 7 | 8 | 8 | 9 | 6 | 10 | 9 | 8 | 7 | 5 | 9 | **7.82** |
| 3 | CRRP: set-valued capture-region relays | 6 | 8 | 8 | 9 | 4 | 9 | 9 | 8 | 7 | 3 | 8 | **7.18** |
| 4 | Topological bridge-node active learning | 4 | 7 | 7 | 9 | 3 | 10 | 10 | 9 | 9 | 4 | 8 | 7.27 |
| 5 | Safe-BO continuation through feasible relay points | 5 | 7 | 8 | 8 | 5 | 8 | 9 | 8 | 8 | 5 | 8 | 7.18 |
| 6 | Diffusion reheat/restart under fixed NFE | 5 | 7 | 6 | 9 | 4 | 9 | 8 | 9 | 7 | 4 | 8 | 6.91 |
| 7 | Adaptive action chunk/control frequency | 4 | 8 | 8 | 9 | 3 | 9 | 9 | 8 | 7 | 3 | 8 | 6.91 |
| 8 | Temporary low-rank continuation | 4 | 7 | 7 | 8 | 3 | 9 | 9 | 8 | 8 | 3 | 7 | 6.64 |
| 9 | GNN relay-node or edge-subdivision mechanism | 3 | 6 | 7 | 8 | 2 | 10 | 10 | 9 | 9 | 3 | 6 | 6.64 |
| 10 | Gradual-domain relay path | 3 | 6 | 7 | 8 | 2 | 9 | 9 | 8 | 8 | 3 | 7 | 6.36 |
| 11 | Prefix-completion-volume search | 4 | 8 | 7 | 8 | 3 | 8 | 8 | 7 | 6 | 3 | 8 | 6.36 |
| 12 | Temporary environment scaffolds | 5 | 8 | 8 | 8 | 4 | 6 | 9 | 6 | 5 | 4 | 7 | 6.36 |
| 13 | Multi-agent relay communication | 5 | 7 | 6 | 8 | 4 | 8 | 8 | 7 | 6 | 4 | 7 | 6.36 |
| 14 | Multi-hop bridge retrieval | 3 | 7 | 7 | 8 | 2 | 9 | 9 | 8 | 7 | 3 | 6 | 6.27 |
| 15 | Predecessor–successor intrinsic exploration | 3 | 6 | 8 | 8 | 2 | 8 | 9 | 8 | 7 | 3 | 7 | 6.27 |
| 16 | Learned latent-action planning as the central contribution | 3 | 6 | 7 | 8 | 2 | 9 | 7 | 6 | 5 | 3 | 6 | 5.64 |

The scorecard alone would keep active learning and safe BO near the shortlist. They were removed because their novelty/story gates are weaker after adversarial search. The final shortlist therefore contains exactly the three candidates whose mechanisms most directly preserve the seed while retaining a credible AI-conference story.

# Shortlist Deep Dives

## Direction 1 — BFAP: Basin-First Adaptive Planning

### One-sentence research question

Can a planner improve strict task success under a fixed rollout budget by selecting, at each state, the least restrictive temporal action basis whose high-budget attainable utility remains essentially unchanged, because that basis has a larger robust near-optimal proposal-space preimage?

### One-sentence counterintuitive headline

**Although the full per-step action sequence contains every restricted plan, an intermediate-dimensional basis can be substantially more successful—and the full space can become worse as nominal capability increases—because finite-budget sampling sees the normalized mass of robust near-optimal plans rather than set inclusion.**

### B/P/M/E formulation

- **Default belief B:** Full per-step control weakly dominates any spline, block, or low-frequency restriction because it contains the restricted trajectories and can use additional degrees of freedom when needed.
- **Counterintuitive prediction P:** At tight but practical rollout budgets, success as a function of action-basis dimension is inverted-U shaped. The best intermediate basis retains at least 95% of high-budget full-space utility yet beats full control by at least 10 percentage points on narrow-tolerance tasks. As the rollout budget grows, the optimum shifts toward higher dimension and the gap shrinks.
- **Mechanism M:** The representation changes the normalized robust near-optimal hit mass $\rho_k$. Added dimensions can create many high-variance nuisance directions that sharply reduce the probability of sampling a plan inside the useful level set. Too much compression eventually produces approximation bias. Finite-budget success is governed by this bias–mass trade-off, not by expressivity alone.
- **Discriminating experiment E:** Run the same iCEM or MPPI implementation on three exact-state benchmark tasks using nested temporal bases $k\in\{2,4,8,16,H\}$, exactly matched rollout counts, and identical action bounds/horizon. Estimate robust near-optimal mass by perturbing candidate coefficients. The hypothesis is supported only if the inverted-U, utility retention, and mass–success correlation co-occur.

### Minimal formalization

Let $\mathcal D=\{D_{b,k}\}$ be a family of decoders indexed by basis family $b$ and dimensionality $k$. For task state $x$, task threshold $\tau$, proposal $q_{b,k}$, and perturbation scale $\sigma$:

$$
\rho_{b,k}(x)=
\Pr_{z\sim q_{b,k},\epsilon\sim\nu_\sigma}
\left[J_x(D_{b,k}(z+\epsilon))\ge\tau\right].
$$

Let $\widehat U_{b,k}$ be an upper-confidence estimate of the best attainable utility from the probe samples and $\widehat\rho^{\mathrm{LCB}}_{b,k}$ a lower credible bound on robust hit mass. BFAP chooses

$$
(b^*,k^*)=
\arg\max_{(b,k)\in\mathcal D}
\widehat\rho^{\mathrm{LCB}}_{b,k}
$$

subject to

$$
\widehat U_{b,k}
\ge
\max_{b',k'}\widehat U_{b',k'}-\Delta_U,
$$

and any task-level constraints on action energy, total variation, collisions, and terminal tolerance. All probe and robustness rollouts are charged to the same planning budget.

### Real relationship to the seed

The decoder is the chain of intermediate “contacts” in the abstraction. It maps a lower-dimensional upstream coefficient vector to a full downstream action sequence. A useful decoder increases the proposal-normalized preimage of the same terminal success set. Unlike physical damping, no action magnitude, horizon, terminal tolerance, or task requirement is relaxed. The research question is therefore exactly whether intermediate structure **transports or expands discoverable reachability in proposal space** without consuming the capability needed for success.

### Closest-work table and functional differences

| Closest work | What it does | Functional overlap | Decisive difference from BFAP |
|---|---|---|---|
| iCEM [P07] | Uses colored noise, elite reuse, and population decay for sample-efficient CEM. | Finite-budget trajectory-search geometry. | Uses a fixed full trajectory representation; does not compare nested decoder preimages, impose a capability-retention gate, or select a representation using robust near-optimal mass. |
| Watson & Peters [P06] | Places a Gaussian-process prior over action trajectories for smooth Monte Carlo control. | Temporal correlation and smooth proposal geometry. | Prior is fixed; paper does not formulate the expressivity–hit-mass inversion or adaptive decoder selection. |
| CoVO-MPC [P05] | Optimizes sampling covariance and derives convergence properties. | Proposal-shape optimization under finite samples. | Optimizes covariance in a given space, not the dimensional image of the action decoder; no utility-preserving basis trade-off. |
| STORM [P09] | Uses low-discrepancy samples, smooth interpolation, and GPU MPC for manipulation. | Interpolated action controls and sample efficiency. | Structured trajectory generation is engineering infrastructure; no normalized success-preimage theory or online basis selection. |
| Learning Sampling Distributions for MPC [P10] | Learns a normalizing-flow proposal from prior experience. | Low-dimensional or structured search distribution. | Requires training data and learns proposals; BFAP first asks a training-free geometric question and compares transparent nested images. |
| MTP [P02] | Mixes global B-spline/Akima trajectory proposals with local CEM exploitation. | Structured global trajectories and exploration/exploitation. | Chooses a fixed model-tensor sampling strategy; no per-state utility-constrained basis selection or preimage-mass mechanism test. |
| C-Uniform [P03] | Samples control trajectories to improve configuration-space coverage. | Recognizes that control-space sampling is not equivalent to useful trajectory coverage. | Optimizes uniformity in configuration space, not probability mass of a task-defined near-optimal success set; no expressivity phase diagram. |
| Tao et al. [P01] | Compares unstructured, linear, cubic-spline, and Bézier sampling for legged MPPI. | Directly compares temporal parameterizations. | It is the sharpest empirical threat. BFAP must go beyond performance comparison by predicting representation choice from robust success mass, enforcing high-budget capability retention, and adapting under equal rollout cost. |
| Low-pass Sampling in MPPI [P04] | Filters perturbations to suppress high-frequency controls. | Removes temporal nuisance directions. | A fixed filter can explain smoothness gains but not cross-basis utility-constrained selection or the proposed mass diagnostic. |
| Whole-body spline MPC [P12] | Reduces control variables using splines for real-time legged control. | Lower-dimensional temporal controls. | Application-specific fixed representation, with no claim about non-monotonic nominal capability or robust success-set volume. |
| Reference-Free Sampling-Based MPC [P19] | Uses dual-space spline parameterization and sample reuse. | Spline representation plus sampling efficiency. | No online representation-selection criterion and no finite-budget expressivity inversion under a capability floor. |
| TAP [P14] | Learns a compact latent action space and plans in it. | Compact planning representation. | Learned action space, offline training, and different input/output problem; does not establish that an intermediate transparent basis wins because of measurable success preimage mass. |
| B-spline Policy [P17] | Represents high-frequency manipulation actions with B-spline control points. | Action compression with B-splines. | Policy-learning and real-robot/behavior setting; no finite-budget black-box planning selector or utility-preserving basin geometry. |
| Predictive Sampling [P13] | Provides a simple sampling-based MPC baseline with practical knot controls. | Directly usable implementation and fixed-knot baseline. | Does not study why or when knot count should vary; BFAP uses it as a controlled implementation substrate. |

### Three most likely rejection reasons

1. **“This is just B-splines or action repeat.”** The paper will fail if it reports only that smooth lower-dimensional plans work better. The robust mass diagnostic, capability-retention constraint, adaptive selector, and strong fixed-structure baselines are mandatory.
2. **“The estimator is circular and noisy.”** If BFAP defines success relative to its own sampled best, a weak basis can look artificially robust. Thresholds must be task-native or anchored to a shared cross-basis utility reference; estimates need calibration and held-out prediction.
3. **“The benchmarks were selected to favor smooth motion.”** The suite must include smooth underactuated control, contact-rich or obstacle tasks, and at least one task requiring a sharp action change. The adaptive method must select higher dimension when compression genuinely harms capability.

### 1–3 day falsification pilot

**Tasks:** DM Control `cartpole/swingup_sparse`, `reacher/hard`, and `ball_in_cup/catch`, or the nearest exact-state equivalents supported by the selected JAX/MuJoCo planner stack [S01–S04]. These are state-based, small, recognized, and have narrow terminal or sparse-success structure.

**Planner:** iCEM first, because its colored-noise baseline is a strong control against the claim that full actions fail only because they are white-noise rough [P07]. A second planner is not required until the pilot passes.

**Bases:** zero-order hold and piecewise-linear interpolation with $k\in\{2,4,8,16,H\}$; one DCT low-pass basis at matched $k$; full per-step colored-noise iCEM.

**Budgets:** 128, 256, and 512 trajectories per MPC update; identical CEM iterations and total simulated transitions after accounting for horizon.

**Seeds:** five planner seeds × 50 fixed initial states per task. Use common random numbers and identical initial-state files across methods.

**Primary outputs:** strict task success, return, capability retention, empirical robust mass, action energy, total variation, collision/constraint count, and wall-clock.

**Pilot kill condition:** stop immediately if no intermediate basis improves success by at least 10 percentage points on two tasks at either 128 or 256 samples while retaining $\kappa_k\ge0.95$, or if the gain disappears after comparison to full-space colored-noise/low-pass iCEM.

### Recommended benchmarks, metrics, and baselines

- **Mechanism-isolation tasks:** DM Control sparse or hard tasks; exact dynamics; state observations [S01].
- **Contact and obstacle extension:** PushT from the Diffusion Policy benchmark [S05]; Hydrax/MuJoCo or MTP tasks such as crane, cube, and planar navigation if official implementations reproduce [S06–S08].
- **Optional learned-model extension:** a PETS-style ensemble or another public state-space dynamics model trained from a fixed transition dataset; do not escalate to pixels unless the exact-model mechanism passes.
- **Metrics:** task-native success, episode return, regret to high-budget reference, normalized capability retention $\kappa$, robust mass $\rho$, samples-to-first-success, area under success-versus-budget curve, action $L_2$ energy, total variation, spectral energy, planning latency, and model-rollout count.
- **Baselines:** random shooting; CEM; iCEM; full-space iCEM with colored noise; fixed zero-order hold; fixed linear and cubic-spline controls; DCT/low-pass controls; MTP; CoVO-MPC; C-Uniform when code/task integration is practical; per-task validation-selected best fixed basis; and an offline oracle basis selector that sees high-budget results but receives no extra online rollouts.

### Compute estimate

| Item | Estimate |
|---|---|
| Per-process VRAM | 2–6 GB for the three pilot tasks; 6–12 GB for large batched contact tasks. |
| Pilot GPU-hours | 60–120 aggregate GPU-hours, including five seeds and robustness perturbations. |
| Pilot wall-clock on eight GPUs | Approximately 8–20 compute hours after compilation; allow 1–3 calendar days including integration and debugging. |
| Pilot storage | 5–15 GB for trajectories, episode summaries, and small diagnostic samples. |
| System RAM | 64 GB workable; 128 GB recommended for eight concurrent simulation/logging workers. |
| Full package | Approximately 2,000–3,200 GPU-hours, 100–250 GB storage, and 11–18 days of wall-clock compute if all eight GPUs remain saturated. |

### Fairness controls and essential ablations

- Count every simulated trajectory, including basis probes and perturbation evaluations.
- Match horizon, replanning frequency, executed low-level steps, action bounds, terminal tolerance, reward, and initial states.
- Include full-space colored-noise and low-pass controls, not only white-noise full control.
- Match or report action energy, total variation, and path length; include constrained comparisons where these are equalized.
- Compare fixed bases selected by validation with BFAP to show that adaptation, not merely a good global hyperparameter, matters.
- Vary $\Delta_U$, perturbation scale $\sigma$, probe-budget fraction, basis family, and basis-grid density.
- Replace robust mass with simple elite fraction, dimensionality, smoothness, and best-return heuristics.
- Run a task requiring high-frequency action changes. BFAP should choose a finer basis there; otherwise it is a universal smoother, not an adaptive mechanism.
- Use held-out initial-state regions and at least one held-out task to test whether the mass statistic predicts representation choice.

### Statistical analysis and failure criteria

- Treat success as Bernoulli and report Wilson intervals plus stratified bootstrap intervals over seeds and initial states.
- Fit a mixed-effects logistic model with basis dimension, log rollout budget, their quadratic/interaction terms, task, and planner; seed and initial-state batch are random effects.
- Test the preregistered inverted-U coefficient and the predicted dimension × budget interaction.
- Use paired bootstrap differences for return and success, Holm correction across the primary task/budget comparisons, and Cliff's delta or rank-biserial effect size where distributional assumptions fail.
- Evaluate whether $\log\widehat\rho$ predicts seed-level success after controlling for dimension, total variation, and best probe return. Report cross-validated $R^2$ or deviance reduction.
- Failure is declared if the apparent gain is explained by smoothness, lower action norm, longer execution, relaxed utility, or a single task/planner.

### Evidence thresholds by paper tier

| Target | Minimum evidence |
|---|---|
| Workshop or short paper | Clean toy proposition; pilot on three state-based tasks; inverted-U with strict utility control; open code. |
| Solid main-conference paper | Six to eight tasks across at least two families; two planners; adaptive method beats tuned fixed bases at equal rollouts; robust-mass diagnostic predicts success; strong statistics and runtime accounting. |
| Potential standout paper | A predictive finite-budget phase diagram across task tolerance, action dimension, horizon, and budget; held-out-task basis selection; exact-model and learned-model confirmation; a theorem or bound linking approximation regret and hit mass; failure cases that the selector correctly detects. |

## Direction 2 — BriCoRe: Bridge-Preserving Reduced Datasets for Offline RL

### One-sentence research question

Under a fixed offline-data budget, can retaining low-return transitions with high marginal graph-connectivity value improve policy learning more than retaining only high-return or high-advantage data, because those transitions enable value propagation and trajectory stitching between otherwise disconnected behavioral components?

### One-sentence counterintuitive headline

**Removing some high-return transitions and keeping apparently mediocre “bridge” transitions can improve offline RL, because a disconnected collection of excellent local behaviors may be less usable than a connected collection containing lower-reward relays.**

### B/P/M/E formulation

- **Default belief B:** When reducing an offline dataset, keep the highest-return, highest-advantage, most recent, or most representative transitions; low-return detours are noise.
- **Counterintuitive prediction P:** At the same subset size and training-update count, a connectivity-preserving subset that retains low-return high-bridge-score transitions can outperform return-based, diversity-based, random, and gradient-based subsets on stitching-heavy tasks. Performance versus the fraction of bridge data should be non-monotonic: too few bridges disconnect support, while too many replace useful local control data.
- **Mechanism M:** Offline value propagation and policy improvement are limited by the support graph. High-quality trajectory fragments on separate components cannot be composed if transition support does not connect their neighborhoods. A transition's usefulness is therefore partly its marginal increase in source-goal reachability or reduction of graph disconnection, not its immediate reward.
- **Discriminating experiment E:** Construct state-transition graphs from fixed D4RL/OGBench datasets, keep exactly 10%, 20%, or 30% of transitions using different selectors, and train the same IQL or TD3+BC implementation for exactly matched gradient updates. The hypothesis is supported only if high-bridge, low-return transitions receive disproportionate retention and their removal causes a causal drop beyond reward/coverage-matched controls.

### Minimal formalization

Given offline transitions $\mathcal D=\{(s_i,a_i,r_i,s'_i)\}$, form a graph $G_\mathcal D=(V,E)$ after clustering or discretizing a fixed state representation. Every transition induces an edge. Let $\mathcal Q$ be a distribution over source-goal pairs or start-terminal regions. Define graph reachability coverage

$$
\mathrm{Reach}(G_S)=
\mathbb E_{(v_s,v_g)\sim\mathcal Q}
\left[
\mathbf 1\{v_s\rightsquigarrow v_g \text{ in } G_S\}
\right]
$$

for subset $S\subseteq\mathcal D$. A practical marginal bridge score for transition $e$ is

$$
b(e\mid S)=
\mathrm{Reach}(G_{S\cup\{e\}})-\mathrm{Reach}(G_S),
$$

approximated through landmark pairs, replacement paths, or sampled betweenness. The coreset objective is

$$
\max_{S\subseteq\mathcal D,\;|S|=B}
\lambda_R\mathrm{Reach}(G_S)
+\lambda_C\mathrm{Coverage}(S)
+\lambda_Q\mathrm{Quality}(S)
-\lambda_D\mathrm{Redundancy}(S),
$$

subject to minimum local state-action support within retained graph regions. “Quality” prevents a graph made of useless transitions; “reachability” prevents isolated high-return islands.

### Real relationship to the seed

A bridge transition is an intermediate contact in the support graph. It can enlarge the set of start states whose learned value or behavior can reach a downstream high-return component. The gain is not obtained by adding data: the subset cardinality is fixed, and the bridge must displace some other transition. Nor is terminal utility relaxed. The claim is that data topology changes the upstream set from which successful behavior can be learned.

### Closest-work table and functional differences

| Closest work | What it does | Functional overlap | Decisive difference from BriCoRe |
|---|---|---|---|
| ReDOR [D01] | Selects a reduced offline dataset through gradient approximation and submodular optimization; shows fewer data can be better. | Exact dataset-reduction problem and counterintuitive size claim. | BriCoRe's hypothesized sufficient statistic is support-graph connectivity and marginal bridge value. It must outperform or complement ReDOR while explaining low-return transition retention. |
| GAS [D02] | Builds a temporal-distance graph and filters transitions using temporal efficiency; generates graph-assisted subgoals for offline HRL. | Graph structure, transition filtering, and stitching. | GAS favors temporally efficient edges for hierarchical planning. BriCoRe preserves graph-critical edges in a fixed-cardinality dataset for generic offline algorithms, including low-return edges that may be temporally inefficient locally. |
| DiffStitch [D03] | Uses conditional diffusion to generate connecting transitions between sub-trajectories. | Explicitly addresses disconnected offline trajectories. | Adds synthetic data and a learned generator; BriCoRe asks which *existing* transitions must not be removed and makes a fixed-data causal claim. |
| SSD [D04] | Generates high-quality stitching transitions with conditional diffusion. | Same trajectory-stitching gap. | Synthetic augmentation and generative modeling, not coreset topology or low-return bridge value. |
| A Dataset Perspective on Offline RL [D06] | Separates trajectory quality and state-action coverage and analyzes dataset properties. | Establishes that return alone is insufficient. | Does not optimize a connectivity-preserving subset or test marginal articulation/bridge transitions. |
| Offline RL: Role of State Aggregation and Trajectory Data [D07] | Theoretically analyzes aggregation and trajectory data. | Connects offline performance to state representation and trajectory structure. | BriCoRe is an actionable subset algorithm and causal graph-removal experiment on public suites. |
| Data-Efficient Pipeline for Offline RL with Limited Data [D08] | Improves offline learning from limited data through representation and synthetic augmentation. | Limited-data regime. | Changes representation and augments data rather than selecting bridge-preserving subsets at fixed raw data. |
| D4RL [D09] | Standardizes offline datasets with varying quality and coverage. | Benchmark foundation. | Benchmark, not a data-selection method. |
| IQL [D10] | Strong offline RL algorithm avoiding explicit out-of-distribution action evaluation. | Main learner baseline. | Learner, not data topology. BriCoRe must work without modifying IQL's objective. |
| TD3+BC [D11] | Minimalist actor-critic plus behavior-cloning baseline. | Strong, simple offline baseline. | Learner, not dataset selection; useful for testing algorithm independence. |
| Active RL Strategies for Offline Policy Improvement [D05] | Selects online queries or interactions to improve an offline policy. | Values data by downstream policy improvement rather than reward alone. | Adds active data; BriCoRe is strictly offline and fixed-cardinality. |
| Offline Imitation Learning through Graph Search and Retrieval [D12] | Retrieves and graph-searches offline trajectories for imitation. | Graph connectivity and stitching through stored experience. | Uses retrieval at inference; BriCoRe changes which data are retained for standard offline training. |

### Three most likely rejection reasons

1. **“Graph construction is arbitrary.”** Results may depend on state scaling, embedding, cluster count, or $k$-NN radius. The effect must survive multiple representations and graph constructions, including raw normalized state, learned encoder, and dynamics-aware distance.
2. **“This is ReDOR plus betweenness.”** A naive centrality score is not enough. The paper needs a formal marginal source-goal reachability objective, a causal removal test, and evidence that topology explains performance beyond gradient similarity, reward, and coverage.
3. **“Offline RL does not actually stitch these behaviors.”** If standard algorithms cannot exploit bridges, preserving them will not help. The pilot must test at least one goal-conditioned or hierarchical setting where stitching is plausible and one standard offline learner.

### 1–3 day falsification pilot

**Datasets:** D4RL Maze2D and AntMaze or the equivalent maintained datasets; OGBench pointmaze/antmaze if installation is smoother [D09, S09]. Use only state observations in the pilot.

**Subset fractions:** 10%, 20%, and 30% of transitions.

**Selectors:** random; top trajectory return; transition advantage or return-to-go; k-center diversity; ReDOR if its official implementation is reproducible; BriCoRe; and BriCoRe with bridge term removed.

**Learner:** IQL first. Add TD3+BC only after a positive signal.

**Graph:** normalized raw state, mini-batch k-means or farthest-point landmarks, directed edges from observed transitions; sampled source-goal pairs from benchmark start/goal distributions. Do not use reward labels in the bridge score.

**Causal diagnostic:** identify transitions in the top decile of bridge score but bottom half of return-to-go. Remove exactly those transitions, then remove a reward-, state-density-, and trajectory-length-matched control set. Retrain with identical updates. A larger drop after bridge removal is the critical mechanism test.

**Pilot kill condition:** stop if BriCoRe fails to beat random and return-based subsets by at least 5 normalized-return points or 10 success percentage points on two stitching-heavy tasks; if the causal removal gap is absent; or if results reverse under a second graph construction.

### Recommended benchmarks, metrics, and baselines

- **Benchmarks:** D4RL Maze2D/AntMaze [D09]; OGBench pointmaze/antmaze and selected manipulation datasets [S09]; optionally ExORL or another public exploratory dataset only after the primary suites.
- **Learners:** IQL [D10], TD3+BC [D11], and one goal-conditioned/hierarchical baseline compatible with OGBench.
- **Selectors:** random, return-to-go, advantage, density, k-center/core-set, ReDOR [D01], GAS-style temporal efficiency [D02], and an oracle subset optimized on evaluation return solely as a headroom estimate.
- **Metrics:** normalized return, task success, number of reachable source-goal landmark pairs, largest strongly connected component, graph diameter on reachable pairs, action-support coverage, Bellman-error propagation across components, and training wall-clock.

### Compute estimate

| Item | Estimate |
|---|---|
| Per-run VRAM | 3–8 GB for state-based IQL/TD3+BC; 8–12 GB for larger encoders or OGBench manipulation states. |
| Pilot run count | Roughly 45–90 learner runs depending on subset fractions and selectors. |
| Pilot GPU-hours | 80–240 aggregate GPU-hours. |
| Pilot wall-clock on eight GPUs | Approximately 12–36 compute hours; 1–3 calendar days including graph implementation. |
| Full package | Approximately 1,800–3,500 GPU-hours, 150–400 GB including datasets/checkpoints, and 10–22 wall-clock days. |
| System RAM | 128 GB recommended because graph construction, replay storage, and eight concurrent learners compete for host memory. |

### Fairness controls, ablations, statistics, and failure criteria

- Fix transition count, gradient-update count, optimizer steps, batch size, evaluation protocol, and hyperparameter-tuning budget.
- Report both fixed updates and fixed epochs; a smaller dataset should not secretly receive more optimizer exposure without a matched comparison.
- Match removed bridge transitions to controls by reward, return-to-go, state density, action norm, trajectory index, and temporal position.
- Vary graph representation, cluster count, edge threshold, directed versus undirected connectivity, and source-goal sampling.
- Compare reachability, ordinary edge betweenness, articulation count, coverage, diversity, reward, and gradient-based importance.
- Use at least ten seeds for final Bernoulli success metrics and five for continuous-return tasks; paired bootstrap over shared dataset subsets.
- Test whether bridge score predicts causal removal impact after controlling for reward, density, temporal position, and state novelty.
- Failure is declared if topology gains vanish after stronger coverage baselines, depend on one discretization, or require a custom goal distribution unavailable to the learner.

### Evidence thresholds by paper tier

| Target | Minimum evidence |
|---|---|
| Workshop or short paper | Two maze tasks, one learner, causal bridge-removal result, and a graph-topology analysis. |
| Solid main-conference paper | Multiple D4RL/OGBench families, two or three learners, strong ReDOR/GAS comparisons, graph robustness, and fixed-update/epoch fairness. |
| Potential standout paper | A theorem or lower-bound example showing when disconnected high-quality support is unusable; bridge score predicts subset value across algorithms and datasets; an embedding-robust coreset algorithm with favorable scaling. |

## Direction 3 — CRRP: Capture-Region Relay Planning

### One-sentence research question

Can planning through learned set-valued intermediate goal regions—rather than precise point subgoals—expand the backward reachable start set and improve exact final-goal success under an unchanged terminal tolerance, total horizon, and low-level policy?

### One-sentence counterintuitive headline

**Less precise intermediate goals can produce more precise final outcomes: widening a relay region can improve exact terminal success up to a task-dependent optimum, after which further widening becomes harmful.**

### B/P/M/E formulation

- **Default belief B:** Precise point subgoals are safer because they specify exactly where the low-level controller should go; a larger subgoal region injects ambiguity.
- **Counterintuitive prediction P:** With the final goal and total horizon fixed, exact final success is non-monotonic in intermediate-region width. A moderate region is easier to enter and still lies inside the downstream predecessor set; an overly broad region contains states with poor downstream reachability.
- **Mechanism M:** For local horizon $h$ and success threshold $\alpha$, the backward predecessor of a region $G$ is $\mathrm{Pre}_{h,\alpha}(G)=\{s:\Pr_\pi(s_{\le h}\text{ reaches }G\mid s_0=s)\ge\alpha\}$. A valid relay $G_i\subseteq\mathrm{Pre}_{h_{i+1},\alpha}(G_{i+1})$ can enlarge $\mathrm{Pre}_{h_i,\alpha}(G_i)$ without relaxing $G_L$, the final goal.
- **Discriminating experiment E:** Hold the low-level goal-conditioned policy, high-level decision count, total primitive horizon, and exact final tolerance fixed. Compare point landmarks with ellipsoidal or clustered relay regions of increasing width. Measure exact final success and empirical predecessor-set size. The predicted inverted-U must appear on at least two tasks.

### Minimal formalization

For goal-conditioned policy $\pi(a\mid s,g)$ and region $G$,

$$
\mathrm{Pre}_{h,\alpha}(G)
=
\left\{s:
\Pr_\pi\left[\exists t\le h:\;s_t\in G\mid s_0=s\right]\ge\alpha
\right\}.
$$

A chain $G_0,G_1,\ldots,G_L$ has exact terminal target $G_L$ and fixed segment horizons $h_1+\cdots+h_L=H$. A utility-constrained relay objective is

$$
\max_{G_1,\ldots,G_{L-1}}
\sum_{i=1}^{L}
\log \mu_i\left(\mathrm{Pre}_{h_i,\alpha_i}(G_i)\right)
-\beta\sum_{i=1}^{L-1}\mathrm{Risk}(G_i,G_{i+1}),
$$

subject to

$$
G_i\subseteq \mathrm{Pre}_{h_{i+1},\alpha_{i+1}}(G_{i+1})
\quad\text{approximately under the learned reachability model,}
$$

and $G_L$ unchanged. In practice, $G_i$ can be a set of replay-buffer states, a learned ellipsoid, or a connected cluster filtered by downstream reachability.

### Real relationship to the seed

Each intermediate region is a relay that maps the narrow final goal backward into a larger admissible state set. The effect is not metaphorical: it is composition of predecessor operators. The required control is that the terminal set stays exactly the same and the sum of primitive horizons stays fixed, so success is not purchased by allowing a looser final target or a longer episode.

### Closest-work table and functional differences

| Closest work | What it does | Functional overlap | Decisive difference from CRRP |
|---|---|---|---|
| Skill Chaining [R01] | Learns options whose initiation sets chain into a target skill. | Direct predecessor/initiation-set composition. | Foundationally very close. CRRP would need offline goal-conditioned set optimization, fixed exact terminal tolerance, and a quantitative inverted-U region-width claim. |
| Deep Skill Chaining [R02] | Extends skill chaining with deep policies and initiation classifiers. | Learned initiation regions and long-horizon chaining. | Learns separate skills online; CRRP plans with a fixed low-level goal-conditioned policy and explicitly optimizes relay-set geometry. |
| Deep Skill Graphs [R03] | Builds a graph of discovered skills for planning and exploration. | Skill graph and compositional reachability. | Skill discovery and graph planning, not set-valued relay optimization under fixed total horizon. |
| Robustly Learning Composable Options [R04] | Improves option composability with termination-aware regularization. | Ensures one option reaches states usable by the next. | Optimizes option policies/termination; CRRP changes high-level goal regions while keeping the low-level policy fixed in the pilot. |
| SoRB [R05] | Searches a graph over replay-buffer states using a learned goal-conditioned value function. | Replay landmarks and test-time subgoal routing. | Uses point states/edges and shortest-path-style costs; CRRP's contribution would be set-valued relays selected for predecessor-volume expansion. |
| Imagined Subgoals [R06] | Generates subgoals to improve goal-conditioned RL. | Subgoal generation and reachability. | Does not center a certified region-width trade-off or exact final-goal predecessor composition. |
| Test-Time Graph Search for GCRL [R07] | Adds graph search at test time to improve goal-conditioned policies. | Test-time subgoal planning with a fixed policy. | Strong direct neighbor; CRRP must show that region-valued nodes and predecessor volume add information beyond better point-graph routing. |
| Autonomous RL via Subgoal Curricula [R08] | Uses generated subgoals and curricula to learn autonomously. | Subgoal selection based on learnability/reachability. | Training curriculum rather than fixed-policy set-valued relay planning. |
| T-STAR [R09] | Uses temporal-logic specification-guided abstraction refinement for offline RL. | Abstract regions and long-horizon constraints. | Logic-guided abstraction and policy learning, not maximizing predecessor region measure under an unchanged goal. |
| Abstract Value Iteration [R10] | Plans among user-provided subgoal regions using abstract value functions. | Explicit region-valued subgoals. | The strongest conceptual threat. CRRP must contribute automatic region construction, the capture-volume objective, and the non-monotonic precision result. |
| Sub-Goal Trees [R11] | Uses learned subgoal tree planning for long-horizon goal reaching. | Hierarchical decomposition into intermediates. | Tree of point or generated subgoals, not utility-constrained predecessor regions. |
| Adaptive Coarse-to-Fine Subgoal Refinement [R12] | Refines subgoals at adaptive granularity for offline GCRL. | Adaptive subgoal precision and current 2026 overlap. | Potentially severe threat; CRRP survives only if its formal object is a reachable **set**, not a coarse point representation, and if its decisive experiment measures predecessor-set expansion. |
| Hierarchical Goal Abstractions via Learned Subset Relations [R13] | Learns hierarchical goal abstractions through subset relations. | Direct 2026 overlap on set-valued or subset-structured goals. | A severe novelty constraint: CRRP cannot claim that region-valued goals are new. It must optimize empirical predecessor-volume transport under an unchanged exact terminal set and fixed primitive horizon. |
| Adaptive Quasimetric Mapping [R14] | Learns time-to-reach geometry and a sparse topological abstraction for robust offline goal-conditioned navigation. | Reachability-aware abstraction, landmark selection, and graph planning. | CRRP changes the geometry of relay **sets** and predicts a region-width phase transition; AQM changes the sparse map and quasimetric. AQM is a mandatory navigation baseline or comparison point. |
| Bottleneck-Guided Spectral Subgoals [R15] | Selects spectral bottleneck subgoals for offline goal-conditioned RL. | Mechanism-level overlap on high-leverage intermediate states. | CRRP does not select bottleneck points; it predicts that moderate relay-region width enlarges composed predecessor measure while preserving the exact goal. The distinction must be measured, not asserted. |
| First-Order Representation Languages for Goal-Conditioned RL [R16] | Represents goals as subsets or lifted subgoals to create easier curricula in relational planning tasks. | Directly shows that subset-valued goals can improve sparse-reward learning. | Different symbolic/generalized-planning setting, but it eliminates any generic novelty claim that “sets rather than points help.” CRRP must remain a fixed-policy, fixed-horizon predecessor-composition result. |

### Three most likely rejection reasons

1. **“Skill chaining and 2026 goal-abstraction work already did this.”** This objection is valid unless CRRP provides a distinct fixed-policy predecessor-volume objective and a mechanistic region-width phase diagram under an unchanged final goal and primitive horizon [R01–R04, R10, R13–R16].
2. **“The reachability model is inaccurate.”** Estimated predecessor sets may simply reflect model bias or dataset density. Calibration and ground-truth navigation tests are essential.
3. **“Wider regions just make subgoals easier.”** The terminal goal and total primitive horizon must remain fixed, and every accepted relay state must retain downstream reachability. Otherwise the result is a trivial task relaxation.

### 1–3 day falsification pilot

**Environment:** OGBench pointmaze or antmaze state tasks, plus a small deterministic maze where predecessor sets can be enumerated for mechanism validation [S09].

**Policy:** one frozen public goal-conditioned policy or one uniformly trained low-level policy shared by all methods.

**Regions:** point landmark; $k$ nearest replay states; ellipsoid around landmark; connected cluster filtered by a downstream reachability threshold. Sweep region widths over at least five values.

**Controls:** same number of high-level decisions, same segment horizons summing to the same $H$, same final tolerance, same low-level calls, point-graph search, random regions of matched volume, and regions matched for dataset density.

**Mechanism measurement:** sample start states on a fixed grid or replay distribution and estimate empirical predecessor membership. Compare measured predecessor volume with exact final success.

**Pilot kill condition:** stop if there is no inverted-U relation on two tasks; if region methods fail to beat the strongest point-graph baseline by at least 10 success percentage points; or if the gain disappears when final tolerance and primitive-step budget are exactly matched.

### Recommended benchmarks, metrics, and baselines

- **Benchmarks:** OGBench pointmaze and antmaze [S09]; D4RL Maze2D/AntMaze [D09]; one manipulation state task only after navigation evidence.
- **Baselines:** direct goal policy; fixed point subgoals; SoRB [R05]; test-time graph search [R07]; abstract-value or region baseline when code permits [R10]; skill-chain-inspired initiation regions; adaptive coarse-to-fine points [R12]; learned subset abstractions [R13]; AQM-style quasimetric graphs [R14]; and spectral bottleneck point subgoals [R15].
- **Metrics:** exact terminal success, predecessor-set measure under a fixed start distribution, conditional downstream success from relay states, primitive steps, high-level decisions, path length, goal-region diameter, calibration error of reachability estimates, and wall-clock.

### Compute estimate

| Item | Estimate |
|---|---|
| Per-run VRAM | 3–8 GB for state GCRL; up to 12 GB for larger manipulation encoders. |
| Pilot GPU-hours | 70–180 aggregate GPU-hours, assuming a frozen policy is available; 150–400 if low-level policies must be retrained. |
| Pilot wall-clock | 1–3 calendar days with eight GPUs. |
| Storage/RAM | 20–80 GB storage; 64 GB RAM workable, 128 GB recommended. |
| Full package | Approximately 1,500–3,000 GPU-hours and 10–18 wall-clock days. |

### Fairness controls, ablations, statistics, and failure criteria

- Match final goal set, total primitive horizon, low-level policy, number of replans, and state-observation information.
- Use density-matched random regions to separate reachability from “more replay points.”
- Calibrate the reachability model and report false inclusion: states admitted to a relay region that cannot reach the next region.
- Sweep region family, width, downstream threshold, segment horizon allocation, and number of relays.
- Compare set-valued planning with point ensembles containing the same number of replay states.
- Use paired initial states and bootstrap success differences; fit a quadratic region-width model with task random effects.
- Failure is declared if region width only tracks goal tolerance, if predecessor volume does not predict exact final success, or if gains require more primitive steps.

### Evidence thresholds by paper tier

| Target | Minimum evidence |
|---|---|
| Workshop or short paper | Exact predecessor visualization in small mazes plus two OGBench navigation tasks and strict final-goal controls. |
| Solid main-conference paper | Automatic region construction; multiple environment families; strong point-graph and skill-chain comparisons; calibrated reachability; fixed-horizon success gains. |
| Potential standout paper | A theorem on predecessor-operator composition and optimal relay width; generalization to held-out layouts; empirical prediction of failure from region false-inclusion and overlap statistics. |

# Novelty Audit Against Closest Work

## 1. Functional novelty boundary for BFAP

The novelty claim must be stated narrowly. BFAP is **not** the first work to use splines, action knots, low-pass noise, compact actions, learned proposals, temporal correlation, or adaptive MPC. It is intended to be the first work—subject to final verification—to make and test the following coupled contribution:

> Under a fixed model-rollout budget, select among nested temporal action images by maximizing a lower-confidence estimate of robust near-optimal proposal mass, subject to a shared high-utility feasibility constraint; then show that this statistic predicts a non-monotonic expressivity–success relation across tasks and budgets.

The table below separates that functional claim from the nearest mechanisms.

| Functional dimension | Existing coverage | Remaining proposed contribution | Required evidence to defend it |
|---|---|---|---|
| Smooth or temporally correlated controls | GP action priors, iCEM colored noise, STORM interpolation, low-pass MPPI [P04, P06, P07, P09, P29] | Smoothness is only one baseline feature; BFAP may choose a non-smooth or finer basis when utility requires it. | Gains over colored-noise and spectral controls; selector chooses finer controls on a rapid-switch task. |
| Lower-dimensional control points | Whole-body spline MPC, Reference-Free MPC, MTP, Tao et al., Predictive Sampling [P01–P03, P12, P13, P19] | Compare multiple nested dimensions and select online under an explicit capability floor. | Fixed best-k and per-task tuned-k baselines; same-budget probe accounting. |
| Learned compact actions | TAP, learned sampling distributions, action tokenization [P10, P14–P17] | Training-free geometric mechanism first; learned bases are optional. | Transparent basis results that survive without demonstrations or representation pretraining. |
| Proposal covariance or distribution | CoVO-MPC, learned proposals, CEM variants [P05, P07, P08, P10] | Change the decoder image itself and estimate task-level robust near-optimal mass. | Ablation holding decoder fixed while optimizing covariance; show both factors are complementary. |
| Global trajectory coverage | C-Uniform, MTP [P02–P03] | Task-conditioned near-optimal mass, not generic configuration coverage. | Compare configuration-space coverage and $\rho$ as predictors; $\rho$ should explain more held-out success. |
| Adaptive controller complexity | Adaptive parameterized MPC and classical move-blocking literature [P20–P22] | Basis selection driven by finite-budget hit geometry rather than model mismatch, active-set changes, or predetermined block schedules. | Equal-rollout online selection and cross-task mechanism prediction. |
| State-space funnels | LQR-trees and funnel libraries [P23–P25] | Proposal-space success preimages under a fixed task, not verified state-space regions of attraction. | Explicit state-space versus coefficient-space diagnostics; no claim of formal safety verification. |
| Action-frequency or chunk adaptation | Action persistence/chunking literature | Preserve the low-level control horizon and allow interpolation; distinguish search dimension from execution frequency. | Same execution frequency and number of environment steps across bases. |

## 2. Backward citation tracing

The backward trace reveals three established roots:

1. **Regions of attraction and funnel composition.** LQR-trees and funnel libraries show that controllers can cover and compose state-space regions [P23–P25]. This supports the seed's reachability vocabulary but also prevents claiming that basin composition itself is new.
2. **Sampling-based trajectory optimization.** CEM motion planning, MPPI, CEM-MPC, and Predictive Sampling establish fixed-budget action-sequence search [P08, P13, P27–P28]. This is the algorithmic substrate, not the contribution.
3. **Control parameterization and temporal priors.** Smooth priors, interpolation, control knots, and low-frequency perturbations reduce effective search complexity [P01, P04, P06, P09, P12, P19, P29]. This is the closest engineering lineage.

The proposed novelty lies at their intersection: a task-conditioned, utility-constrained criterion for choosing the representation and a falsifiable prediction about normalized near-optimal mass.

## 3. Forward and recent-work tracing

Recent papers make the novelty test stricter:

- **Tao et al. 2026 [P01]** empirically compare several interpolation schemes for legged MPPI. Any BFAP submission must cite it prominently and show that BFAP is not a post-hoc recommendation of cubic splines.
- **MTP [P02]** combines structured global proposals with local exploitation. BFAP must compare against it or an equivalent global/local mixture on compatible tasks.
- **C-Uniform [P03]** changes sampling to improve trajectory-space coverage. BFAP must show why task-defined success mass is different from generic configuration coverage.
- **B-spline Policy and action-tokenization papers [P15–P17]** show that compressed action representations are an active trend. BFAP must avoid an imitation-learning or tokenization claim.
- **CoVO-MPC [P05]** provides a principled covariance-design baseline. A reviewer can reasonably ask whether covariance adaptation makes basis adaptation unnecessary.
- **Reference-Free MPC and deterministic-sample CEM [P18–P19]** reduce sampling variance through structured proposals. They are necessary efficiency controls if code is stable.

## 4. Venue-by-venue adversarial audit for the primary

| Venue | What was inspected | Closest evidence | Audit conclusion |
|---|---|---|---|
| ICLR 2023–2026 | compact latent actions, action tokenization, adaptive temporal abstractions, planning representations | TAP and recent action representation work [P14–P16] | Strong overlap on compact actions, but not on task-conditioned robust preimage selection. |
| ICML 2023–2026 | sampling distributions, covariance design, graph/data methods, learned goal subsets, quasimetrics, and spectral subgoals | learned MPC proposals, CoVO-MPC, GAS, learned subset relations, AQM, and spectral bottleneck subgoals [P05, P10, D02, R13–R15] | Proposal design is mature; the 2026 goal-abstraction papers sharply narrow CRRP, while BFAP still requires the coupled geometry/utility claim. |
| NeurIPS 2023–2026 | action compression, model-based planning, offline RL | BEAST/action tokenization and strong offline baselines [P16, D10–D11] | No exact duplicate found; learned-action crowding raises reviewer bar. |
| AAAI / IJCAI 2023–2026 | trajectory stitching, composable options, active offline RL, and subset-valued goal languages | SSD, robust composable options, and first-order subset goals [D04, R04, R16] | Mainly relevant to backups; R16 removes any broad novelty claim around subset-valued goals. No primary BFAP duplicate was located. |
| CoRL / RSS 2017–2026 | CEM, MPPI, manipulation MPC, action priors, motion planning | iCEM, STORM, learned proposals, CEM motion planning [P07–P10] | Highest prior-art density; BFAP needs stronger mechanism evidence than a typical control-parameterization paper. |
| L4DC / TMLR / TRO / RA-L / IJRR | predictive sampling, MTP, legged spline MPC, funnels | [P01–P03, P12–P13, P23–P25] | No exact combination found, but individual components are well established. |
| ACL / EMNLP | multi-hop bridge passages and passage utility | [E05–E06] | Eliminates retrieval reformulation; no direct action-planning duplicate. |
| CVPR / ICCV / ECCV | diffusion-policy action chunks and tokenization | [P15–P17] | Visual-policy direction is crowded and unnecessarily expensive for mechanism discovery. |

## 5. Novelty audit for BriCoRe

BriCoRe's novelty margin is narrower than BFAP's. ReDOR already optimizes reduced datasets [D01]; GAS already uses graph temporal structure and transition filtering [D02]; DiffStitch/SSD explicitly connect sub-trajectories [D03–D04]. The defensible boundary is:

- no synthetic transitions;
- fixed-cardinality selection for standard offline learners;
- a source-goal reachability or replacement-path objective, not generic centrality;
- a preregistered causal test on low-return high-bridge transitions;
- graph-construction robustness and reward/coverage-matched controls.

If the method reduces to “retain high-betweenness transitions,” novelty is insufficient.

## 6. Novelty audit for CRRP

CRRP is directly adjacent to Skill Chaining, Abstract Value Iteration, SoRB, and adaptive subgoal refinement [R01, R05, R10, R12]. The August 2026 audit materially tightened this boundary: ICML 2026 work on learned subset relations [R13], adaptive quasimetric maps [R14], and spectral bottleneck subgoals [R15], together with AAAI 2026 work on subset-valued goal languages [R16], means that **“use regions rather than point subgoals” is no longer a defensible contribution**. CRRP survives only if the paper's central object is an automatically constructed set-valued relay satisfying an estimated downstream predecessor constraint, and if the decisive result is an exact-final-goal, fixed-primitive-horizon inverted-U as region width changes. A point-subgoal method, initiation-set classifier, symbolic subset-goal curriculum, ordinary graph search, or generic bottleneck detector would fail the novelty gate.

# Primary Recommendation

## Provisional title

**Less Control, More Success: Utility-Constrained Basin Expansion for Finite-Budget Model-Predictive Planning**

Alternative title if the adaptive method is the strongest part:

**Basin-First Adaptive Planning: Choosing Action Representations by Robust Near-Optimal Preimage Mass**

## Central claim

For sampling-based planning with a fixed rollout budget, action-sequence expressivity and task success need not be monotone. A temporal basis that preserves high-budget utility can enlarge the proposal-normalized robust near-optimal preimage enough to outperform the full action space. Estimating this mass online enables a planner to choose action resolution adaptively and recover performance across tasks requiring different temporal complexity.

## Genuine scientific contributions

1. **A finite-budget expressivity inversion.** Establish theoretically in a controlled model and empirically across benchmarks that adding action-sequence degrees of freedom can lower strict success despite nondecreasing optimal utility.
2. **A measurable mechanism.** Define robust near-optimal preimage mass under the planner's proposal and show that it predicts success better than action dimension, smoothness, generic trajectory coverage, or best sampled return alone.
3. **A utility-preserving selection principle.** Formulate action-basis choice as maximizing a confidence bound on robust mass subject to a shared utility floor and fixed task resources.
4. **A same-budget adaptive planner.** Implement BFAP using probe-and-allocate or successive halving across nested bases, counting all rollouts, and demonstrate that it approaches the best basis per state without oracle task-specific tuning.

Routine GPU batching, implementation of existing bases, and benchmark integration are not scientific contributions.

## Textual method diagram

A paper figure should be read left to right:

1. **Current state and fixed task:** the same state $x_t$, horizon $H$, action bounds, terminal success set, and rollout budget $N$ feed every branch.
2. **Nested action decoders:** parallel branches show $k=2,4,8,16,H$ coefficients decoded into full-length action sequences by zero-order hold, linear/spline, or spectral bases.
3. **Shared probe rollouts:** a small equal-budget batch is simulated for each branch. Successful and near-successful trajectories are highlighted; coefficient perturbations reveal whether successes occupy broad or knife-edge regions.
4. **Capability gate:** branches whose upper utility estimate falls more than $\Delta_U$ below the shared best are removed.
5. **Basin score:** remaining branches receive a lower-confidence robust-mass score, with uncertainty bars.
6. **Budget allocation and refinement:** the remaining rollout budget is assigned to the best-scoring branch, optionally with one nested refinement into a finer basis.
7. **MPC execution:** only the first action is executed; previous plans are shifted and projected into every basis for the next step.
8. **Diagnostic panel:** a separate plot shows full-space set inclusion but intermediate-basis larger normalized near-optimal mass, visually separating capability from discoverability.

## Decoder family

Use a small transparent family in the main method:

- **ZOH-$k$:** $k$ control knots held constant over equal temporal blocks;
- **LIN-$k$:** linearly interpolated control knots;
- **DCT-$k$:** first $k$ temporal cosine coefficients per action dimension;
- **FULL:** $k=H$, one action per time step.

Cubic B-splines should be a baseline and optional branch, not the only representation, because otherwise the contribution will look like a spline paper. The default main selector can use LIN and DCT plus FULL; the generality claim is tested by adding ZOH and B-splines.

## Robust mass estimator

A practical estimator must avoid circularity. Use a task-native threshold when available—for example binary success, terminal distance, or sparse reward. For dense tasks, define a shared threshold from all probes:

$$
\tau_t=
\max\left(
J_{\mathrm{warm}},
Q_{1-\alpha}\left(\bigcup_{b,k}\{J_i^{b,k}\}\right)-\Delta_\tau
\right).
$$

For basis $(b,k)$, draw $n_{b,k}$ probe coefficients. For each coefficient $z_i$, draw one small normalized perturbation $\epsilon_i$ after initial screening. Define

$$
y_i^{b,k}=
\mathbf 1\left[
J_x(D_{b,k}(z_i))\ge\tau_t
\;\wedge\;
J_x(D_{b,k}(z_i+\epsilon_i))\ge\tau_t
\right].
$$

With a Beta$(1,1)$ prior,

$$
p_{b,k}\mid y
\sim
\mathrm{Beta}\left(1+\sum_i y_i,\;1+n_{b,k}-\sum_i y_i\right).
$$

Use a lower posterior quantile $\mathrm{LCB}_\delta(p_{b,k})$ as the basin score. A cheaper ablation uses the unperturbed elite fraction; a stronger diagnostic uses multiple perturbations around a small subset of candidates.

## Capability estimate

The online gate should not require an expensive oracle. Use the maximum of warm-start, cross-basis probe best, and an optimistic extreme-value estimate:

$$
\widehat U_{b,k}=
\max_i J_i^{b,k}
+ c_U\widehat s_{b,k}\sqrt{\frac{\log T}{n_{b,k}}},
$$

where $\widehat s$ is a robust scale estimate and $T$ is the total probe count. A basis is active when

$$
\widehat U_{b,k}
\ge
\max_{b',k'} \widehat U_{b',k'}-\Delta_U.
$$

The paper should not claim this is a calibrated bound without proof. It is an optimistic selection heuristic. Calibration is measured empirically against high-budget utility.

## Same-budget probe-and-allocate algorithm

```text
Input: state x, horizon H, rollout budget N, decoder set D,
       previous plan U_prev, utility slack ΔU, perturbation scale σ.

1. Shift U_prev and project it into every decoder as the common warm start.
2. Reserve N_probe = floor(αN) rollouts; split equally across decoders.
3. Sample and evaluate probe coefficients for each decoder.
4. Build a shared task-utility threshold τ from task-native success or all probes.
5. Use a charged subset of probe budget to perturb candidates and estimate
   a lower confidence bound on robust near-optimal mass.
6. Remove decoders whose optimistic utility is more than ΔU below the shared best.
7. Allocate N - N_probe remaining rollouts to the active decoder with largest
   robust-mass LCB, or use successive halving if confidence intervals overlap.
8. Run the base optimizer in that decoder; decode the best plan.
9. Execute only the first action. Log all basis scores and repeat.
```

## Optional nested refinement

A stronger variant starts in a coarse basis and lifts the elite mean into the next finer basis only when either:

- the coarse basis fails the utility gate;
- elite residuals show systematic unrepresented temporal structure;
- the confidence intervals of two bases overlap and the finer basis has a higher utility estimate.

This variant should be secondary until the simple selector passes. Otherwise the paper risks becoming an opaque bundle of heuristics.

## Minimal theoretical results

The theory should be modest and exact rather than grandiose.

### Proposition 1 — expressivity does not imply finite-budget dominance

Construct nested spaces where $\mathrm{Im}(D_k)\subseteq\mathrm{Im}(D_{k+1})$, $J_{k+1}^*\ge J_k^*$, but the proposal mass of a fixed near-optimal set satisfies $\rho_{k+1}<\rho_k$. The box example above gives an immediate proof. This establishes possibility, not universality.

### Proposition 2 — finite-budget hit advantage

For independent proposals, if $\rho_k>\rho_H$, then

$$
1-(1-\rho_k)^N > 1-(1-\rho_H)^N
$$

for all $N>0$. The absolute difference is largest in an intermediate rare-event regime and vanishes as both hit probabilities approach one. This predicts why the gap should shrink with a very large budget.

### Proposition 3 — utility-preserving restriction

Under local $L$-Lipschitz utility and decoder approximation error $\epsilon_k$, capability regret is bounded by $L\epsilon_k$. This motivates a measurable approximation or high-budget utility gate.

### Optional theorem — selector regret

Under stationary Bernoulli robust-success observations and a valid utility-feasibility test, a successive-halving or bandit allocation rule can bound the probability of selecting a suboptimal basis. This is useful only if assumptions and constants remain readable; it is not required for the pilot.

## What the paper must not claim

- It does not show that lower-dimensional action spaces are universally better.
- It does not prove safety, formal reachability, or exact basin volume in nonlinear systems.
- It does not claim novelty for spline controls, low-pass sampling, or action knots.
- It does not claim that robust mass is invariant to parameterization; the proposal and normalization are part of the operational object.
- It does not claim superiority at unlimited compute; the thesis is explicitly finite-budget.

# Minimal Falsification Pilot

## 1. Objective

The pilot is not intended to prove a paper. It asks one binary question:

> Does a strict, utility-preserving, non-monotonic action-dimension effect exist under a strong full-space sampling baseline, and does robust near-optimal mass predict it?

A negative answer kills BFAP before any learned models, pixels, large sweeps, or new environments are introduced.

## 2. Pilot stack

**Recommended implementation path:** JAX + MuJoCo/MJX, using Hydrax or Predictive Sampling as the trajectory-optimization substrate and iCEM as the primary algorithmic reference [P07, P13, S02–S08]. Use whichever stack reproduces one official example first; do not spend the pilot building a new simulator wrapper.

**State only:** exact simulator state, no images, no learned encoder, no model-learning error.

**Single process per GPU:** each GPU runs one task/seed/configuration worker. Independent workers exploit the eight-GPU machine without assuming shared memory.

## 3. Tasks

| Task | Why it is useful | Native success definition | Risk addressed |
|---|---|---|---|
| DM Control `cartpole/swingup_sparse` | Underactuated, sparse, and sensitive to timing. | Native sparse success or a preregistered upright-angle and angular-velocity threshold. | Tests whether too-coarse controls lose dynamic capability. |
| DM Control `reacher/hard` | Narrow terminal target and low action dimension. | Native target-distance success. | Clean narrow tolerance with simple dynamics. |
| DM Control `ball_in_cup/catch` | Requires temporal coordination; success is not merely low-energy stabilization. | Native catch success. | Rejects the “damping explains everything” alternative. |

If one task is not supported in the chosen stack within the first implementation day, replace it with an official equivalent such as sparse pendulum swing-up or a MuJoCo reach task. Record the substitution before looking at results.

## 4. Fixed experimental constants

- Planning horizon $H\in\{20,30\}$, fixed per task before the main sweep.
- Replanning every environment step; execute exactly one primitive action from each plan.
- Same action bounds and task reward for all methods.
- Same initial states, stored once and reused.
- Same CEM iterations, elite fraction, warm-start rule, and optimizer update equations.
- Total model trajectories per decision $N\in\{128,256,512\}$.
- Five planner seeds and 50 fixed initial states per task for the pilot.
- Episode count and truncation exactly matched.
- All compilation warm-up excluded from algorithm latency but reported separately.

## 5. Methods in the pilot

1. **FULL-white:** full per-step actions with independent Gaussian sampling; diagnostic weak baseline only.
2. **FULL-iCEM:** full per-step actions with iCEM colored noise and elite reuse; primary full-space control.
3. **ZOH-$k$:** $k\in\{2,4,8,16\}$.
4. **LIN-$k$:** $k\in\{2,4,8,16\}$.
5. **DCT-$k$:** $k\in\{2,4,8,16\}$.
6. **Validation-best fixed basis:** choose one basis/dimension on a disjoint validation initial-state set.
7. **Oracle-best per task/budget:** hindsight upper bound, not a deployable method.
8. **BFAP-lite:** probe all bases with 25% of the budget, eliminate utility-inferior bases, allocate the remaining 75% to the largest robust-mass LCB.

The full Cartesian product is not required immediately. Start with FULL-iCEM and LIN-$k$ on all tasks. Add ZOH and DCT only if the core effect appears.

## 6. Robust-mass diagnostic protocol

For every initial state and basis:

1. Save the first-iteration proposal batch before CEM adaptation.
2. Define a shared utility threshold from task-native success or the 90th percentile of the union of all basis proposals, with a prespecified slack.
3. Select up to 32 candidates spanning the return distribution.
4. Apply two coefficient perturbations at normalized scales $\sigma\in\{0.02,0.05\}$ relative to proposal standard deviation.
5. Estimate unperturbed elite fraction and robust elite fraction.
6. Log the same perturbations after the final CEM iteration to separate initial discoverability from local refinement.

The primary mechanism statistic is the **initial** robust mass. Final-iteration mass may merely reflect that the optimizer already found a good basin.

## 7. Capability-retention test

Run a separate high-budget reference at $N=4096$ or the largest feasible budget that produces stable returns. Use ten optimizer iterations only if the normal planner uses fewer; keep the reference identical across bases. Compute

$$
\kappa_{b,k}
=
\frac{\overline J^{\mathrm{high}}_{b,k}-\overline J_{\mathrm{random}}}
{\overline J^{\mathrm{high}}_{\mathrm{FULL}}-\overline J_{\mathrm{random}}}.
$$

A low-dimensional basis cannot support the primary claim on a task if its confidence interval includes values below 0.95. It may still be useful as a deliberately biased baseline.

## 8. Exact pilot matrix

### Stage P0 — implementation sanity

| Tasks | Methods | Budgets | Seeds | Initial states | Purpose |
|---|---|---:|---:|---:|---|
| 1 task | FULL-iCEM, LIN-4, LIN-8, LIN-16 | 256 | 2 | 10 | Verify decoding, budget accounting, action execution, and identical rewards. |

**Advance condition:** trajectories and returns match the full implementation when LIN-$H$ is used; rollout counters are exact; no decoder violates action bounds.

### Stage P1 — core falsification

| Tasks | Methods | Budgets | Seeds | Initial states | Approximate job cells |
|---|---|---:|---:|---:|---:|
| 3 | FULL-iCEM, LIN-2/4/8/16 | 128, 256, 512 | 5 | 50 | 225 |

The 225 cells can be grouped by seed and budget; vectorized evaluation means this is not 225 long training jobs.

### Stage P2 — explanation controls, only if P1 is positive

| Addition | Purpose |
|---|---|
| FULL-white and low-pass FULL | Quantify how much is explained by temporal correlation alone. |
| ZOH and DCT bases | Test whether the effect is basis-family general rather than spline-specific. |
| BFAP-lite | Test same-budget adaptive selection. |
| $N=4096$ high-budget reference | Capability retention and convergence of full-space search. |
| Rapid-switch counter-task | Verify that BFAP selects a finer basis when low-frequency restriction is genuinely harmful. |

## 9. Preregistered outcomes

### Primary outcome

Mean strict success difference between the best intermediate basis selected without test leakage and FULL-iCEM at $N=256$.

### Co-primary mechanism outcome

Cross-initial-state and cross-basis association between initial robust mass and planning success, controlling for best initial sample return, action total variation, and dimension.

### Secondary outcomes

- area under success-versus-log-budget curve;
- samples to first successful trajectory;
- return regret to the high-budget reference;
- action energy and total variation;
- planning latency and simulated transition count;
- BFAP-lite regret to the hindsight best basis.

## 10. Pilot decision table

| Observation | Decision |
|---|---|
| Inverted-U on at least two tasks; $\kappa\ge0.95$; robust mass predicts success; gains survive colored-noise control | **GO to full plan.** |
| Intermediate basis wins, but only because it lowers action energy or total variation | **NO-GO for current thesis.** A smooth-control application paper is a different project. |
| Fixed intermediate basis wins, but robust mass does not predict success | **Pause.** The mechanism is unsupported; do not launch a full BFAP paper. One small diagnostic revision is allowed, not an open-ended method search. |
| Full-space iCEM matches or beats every restricted basis at all tight budgets | **Immediate NO-GO.** |
| Effect appears only on reacher or one trivial task | **NO-GO.** |
| BFAP-lite loses to validation-best fixed basis after budget accounting | **Primary method is not justified.** A pure phenomenon paper would require much broader evidence and stronger theory. |

# Full Experimental Plan

## 1. Evidence chain

The complete paper should build evidence in this order:

1. **Controlled theorem and toy geometry:** nested action spaces can have monotone optimum but non-monotone finite-budget hit probability.
2. **Exact-model mechanism:** action dimension changes robust near-optimal mass and success on recognized state-control tasks.
3. **Adaptive method:** BFAP selects different bases by state/task and approaches the oracle basis at equal rollout cost.
4. **Cross-planner robustness:** the result holds for at least two optimizer families, not just one CEM implementation.
5. **Cross-environment robustness:** the result holds on smooth dynamics and contact/obstacle tasks, and BFAP chooses high resolution when required.
6. **Model-error robustness:** after exact-model success, repeat a subset with a learned ensemble dynamics model.
7. **Efficiency and limitations:** show where representation probing is worth its cost and where full-space planning dominates.

Skipping step 2 and going directly to a large learned model would make the causal story weaker.

## 2. Environment families

### Family A — exact-state, smooth or underactuated control

- DM Control `cartpole/swingup_sparse`;
- DM Control `reacher/hard`;
- DM Control `ball_in_cup/catch`;
- one rapid-switch or disturbance-recovery task, such as `finger/turn_hard` or a prespecified torque-reversal task supported by the stack.

### Family B — obstacle or contact-rich planning

Choose two or three from:

- PushT state benchmark [S05];
- MTP/Hydrax planar navigation or crane task [P02, S06–S08];
- MuJoCo cube reorientation or in-hand manipulation if the official model and success metric reproduce;
- a standard sparse pushing or reaching task from MuJoCo Playground [S04].

Do not add a custom task merely because standard tasks fail. A toy diagnostic environment is allowed only for visualizing the mechanism and cannot carry the main empirical claim.

### Family C — learned state dynamics, conditional extension

For two representative tasks, collect or use a fixed public transition dataset and train an ensemble probabilistic dynamics model. A PETS-style model is sufficient; the project does not need Dreamer-scale representation learning. Use identical model checkpoints across action representations. Evaluate true-environment return separately from model-predicted utility.

## 3. Planner families

1. **CEM family:** CEM and iCEM [P07–P08].
2. **MPPI family:** standard MPPI or Predictive Sampling plus a low-pass/GP-prior variant [P04, P06, P13, P27–P29].

MTP, CoVO-MPC, and C-Uniform should be integrated where task interfaces are compatible. At minimum, reproduce their central structured-sampling idea in the same codebase and state clearly when an official implementation cannot support a benchmark without material changes.

## 4. Main method matrix

| Group | Methods | Purpose | Priority |
|---|---|---|---:|
| Full-space references | random shooting, CEM, iCEM, MPPI | Basic optimization references | 1 |
| Strong full-space structure | colored-noise iCEM, GP-prior/low-pass MPPI, CoVO-MPC | Rule out rough white-noise explanation | 1 |
| Fixed temporal bases | ZOH, LIN, B-spline, DCT at multiple $k$ | Establish dimension and basis-family curves | 1 |
| Global/local structured proposals | MTP or faithful equivalent; C-Uniform if reproducible | Strong nearest-neighbor methods | 2 |
| Selection baselines | validation-best fixed basis, best dimension predicted by task horizon/action dimension, smoothness heuristic, elite-fraction heuristic | Test whether robust mass is needed | 1 |
| Proposed | BFAP-lite and BFAP successive-halving/refinement | Main method | 1 |
| Oracle analyses | per-state hindsight best basis; high-budget best basis | Quantify selection headroom | 1 |
| Optional learned decoder | PCA or autoencoder action basis trained on successful high-budget trajectories | Test whether learned images help beyond transparent bases | 3 |

## 5. Budget grid

Use a logarithmic rollout grid, adjusted for simulator speed:

$$
N\in\{64,128,256,512,1024,4096\}.
$$

The first five points define the practical finite-budget curve. The largest point is a capability/convergence reference and need not be run for every seed-task-method combination. Report both trajectory count and simulated state transitions $N\times H$.

## 6. Horizon and tolerance interventions

The mechanism predicts stronger compression benefits when the nominal action dimension $mH$ grows and when the success set narrows. Test this causally:

- horizon $H\in\{10,20,40,80\}$ where task semantics allow;
- terminal tolerance or sparse success threshold at three prespecified levels;
- action dimension through task variants or duplicated nuisance actuators in a **toy diagnostic only**, not as a headline benchmark;
- perturbation/noise level in dynamics or executed action.

Expected phase diagram:

- higher $H$ and tighter tolerance move the best finite-budget $k$ downward;
- larger rollout budget moves it upward;
- tasks requiring rapid control changes impose a lower bound on $k$ and can reverse the trend.

## 7. Diagnostic experiments that test mechanism

### D1. Basin-volume versus performance

For every basis and initial state, estimate initial robust mass from independently drawn proposals. Predict held-out planning success. Compare against:

- dimension $mk$;
- action total variation;
- spectral bandwidth;
- initial best return;
- elite fraction without perturbation;
- configuration-space coverage;
- local Hessian or covariance proxy around the final elite.

The mechanism is supported only if robust mass adds predictive value after these controls.

### D2. Success-set slices

For low-dimensional tasks, take a high-quality plan and two random or principal directions in coefficient space. Plot utility contours for coarse, intermediate, and full parameterizations using normalized coordinates. Show that the intermediate basis has a wider robust level set, while high-budget optimum remains similar.

### D3. Nuisance-direction injection

In a diagnostic simulator, augment the full action sequence with temporally oscillatory directions that cancel approximately in state space but must remain small to avoid constraints. The theorem predicts exponential loss of hit mass while optimal utility stays unchanged. This validates mechanism but cannot substitute for standard benchmarks.

### D4. High-frequency necessity

Use a task or state subset requiring rapid action reversal. The capability gate should reject coarse bases and BFAP should select higher $k$. This is essential evidence that the method is not a universal smoother.

### D5. Budget-dependent basis shift

For the same state distribution, verify that the best basis dimension increases with rollout budget. This is a stronger signature than a fixed intermediate optimum.

### D6. Learned-model error

With fixed learned dynamics, compare predicted robust mass to true-environment robustness. Analyze whether model error favors overly smooth bases. Report model exploitation separately.

## 8. Robustness tests

- action execution noise and state-estimation noise;
- dynamics parameter perturbations;
- held-out initial-state regions;
- held-out task within the same simulator family;
- alternative basis grids and perturbation scales;
- alternative optimizer hyperparameters and warm-start rules;
- task-native binary success versus return-derived threshold;
- simulator precision and batch size;
- deterministic versus stochastic proposal seeds.

## 9. Efficiency tests

- total simulator transitions to reach a target success rate;
- wall-clock per MPC decision, including probe and basis projection;
- GPU utilization and compilation overhead;
- BFAP probe fraction $\alpha\in\{0.1,0.2,0.3,0.4\}$;
- number of bases considered;
- successive halving versus one-shot selection;
- amortized warm-start and previous-basis persistence;
- CPU-host overhead and transfer volume.

## 10. Visualizations

1. Success versus basis dimension at multiple rollout budgets, with high-budget utility on a second panel.
2. Robust mass versus basis dimension, aligned with success curves.
3. Budget–dimension heatmap showing the best basis and BFAP selections.
4. Predicted versus observed success from the mass model, with held-out tasks highlighted.
5. Utility contour slices in normalized coefficient space.
6. Action trajectories and spectra for full, coarse, intermediate, and BFAP plans.
7. Capability-retention versus success-gain Pareto plot.
8. Per-state basis-selection timeline during an episode.
9. Failure cases where BFAP correctly or incorrectly selects coarse resolution.

## 11. Prioritized experiment matrix

### Tier 1 — mandatory main paper

| Dimensions | Values |
|---|---|
| Tasks | 6 tasks across two environment families |
| Planners | iCEM and MPPI/Predictive Sampling |
| Methods | full structured baseline, 3 fixed basis families × selected $k$, validation-best fixed, BFAP, oracle |
| Budgets | 128, 256, 512, 1024; high-budget reference on subset |
| Seeds | 10 for primary success tasks, 5 for expensive contact tasks if confidence intervals are sufficiently tight |
| Initial states | 100 fixed starts per state task; task-native episode protocol for contact tasks |

### Tier 2 — mechanism and robustness

Horizon/tolerance phase diagram, D1–D5 diagnostics, execution noise, and held-out initial-state regions.

### Tier 3 — conditional extensions

Learned dynamics, learned action basis, additional contact tasks, and real-time deployment. These must not delay a clean state-based paper.

## 12. Reproducibility requirements

- release exact initial-state files, task XML/version hashes, and simulator versions;
- central rollout counter used by every method;
- one configuration file per figure/table;
- deterministic seed mapping from task × method × budget × replicate;
- raw episode-level success/return logs, not only aggregated curves;
- scripts that regenerate statistical tables and all figures;
- capability-reference runs stored separately to prevent accidental test-time use;
- public list of excluded failed tasks and reasons.

# Dataset and Baseline Inventory

## 1. Primary benchmark inventory

| Resource | Role | Why chosen | Official source | Pilot or full |
|---|---|---|---|---|
| DeepMind Control Suite | State-based continuous-control benchmark | Recognized tasks, exact simulator state, sparse/hard variants, modest memory footprint | [S01] | Pilot and full |
| MuJoCo / MJX | Physics and GPU-batched simulation | Supports independent GPU workers and vectorized model rollouts without memory pooling | [S02–S03] | Pilot and full |
| MuJoCo Playground | Maintained task collection and MJX examples | Provides newer manipulation/locomotion tasks if stable in the selected version | [S04] | Full, optional |
| PushT / Diffusion Policy benchmark | Contact-rich planar pushing | Standard public task with a meaningful terminal success region; state mode avoids pixel cost | [S05] | Full |
| Hydrax | JAX sampling-based MPC library | Practical exact-model implementations and GPU batching; supports CEM/MPPI-style methods and knot controls | [S06] | Pilot substrate |
| MTP code/project | Structured global/local planning baseline | Strong nearest neighbor using model tensors and interpolated trajectories | [P02, S08] | Full baseline |
| Predictive Sampling / MuJoCo MPC | Simple official sampling baseline | Transparent reference for implementation and control-knot studies | [P13, S07] | Pilot or full |

## 2. Backup benchmark inventory

| Resource | Backup | Why chosen | Official source |
|---|---|---|---|
| D4RL Maze2D and AntMaze | BriCoRe and CRRP | Canonical offline navigation datasets with coverage/stitching variation | [D09] |
| OGBench pointmaze, antmaze, and manipulation | BriCoRe and CRRP | Modern benchmark centered on offline goal-conditioned RL and long-horizon tasks | [S09] |
| IQL implementation | BriCoRe | Strong and stable offline learner that can be held fixed while data change | [D10] |
| TD3+BC implementation | BriCoRe | Simple algorithmic control against IQL-specific effects | [D11] |
| SoRB / test-time graph search | CRRP | Strong point-landmark planning baselines | [R05, R07] |

## 3. Primary baseline inventory and use policy

| Baseline | Required comparison | Implementation policy |
|---|---|---|
| Random shooting | Basic sanity and high-variance lower bound | Implement in shared codebase. |
| CEM | Standard black-box optimizer | Implement in shared codebase; validate against an official example. |
| iCEM | Strong finite-budget full-space baseline | Prefer official code or a line-by-line faithful port; colored noise and elite reuse are mandatory. |
| MPPI or Predictive Sampling | Second optimizer family | Use official MuJoCo/JAX implementation where possible. |
| GP-prior or low-pass MPPI | Strong temporal-correlation control | Use official algorithm if task integration is feasible; otherwise reproduce the documented kernel/filter exactly. |
| CoVO-MPC | Principled covariance-design baseline | Use compatible public code; if unavailable for a task, report a faithful covariance schedule on shared code. |
| MTP | Strong structured global/local baseline | Use official repository and supported tasks first. Do not silently reimplement a weakened approximation. |
| C-Uniform | Configuration-space coverage baseline | Conditional on stable code/task support; otherwise include in analysis and state the integration limitation. |
| Fixed ZOH/LIN/B-spline/DCT | Representation controls | Shared decoder library, exact same planner. |
| Validation-best fixed basis | Strong practical hyperparameter baseline | Select on disjoint validation states with the same tuning budget as BFAP. |
| Hindsight oracle basis | Headroom only | Never reported as a deployable baseline; no test-time leakage into BFAP. |

## 4. Version-freezing protocol

Before any full run, record:

- git commit for every external repository;
- MuJoCo, MJX, JAX, CUDA, driver, and Python versions;
- task XML/model hashes;
- GPU model and power limit;
- deterministic and nondeterministic kernel settings;
- exact environment wrappers and termination conditions;
- whether reward and success are native or derived.

A benchmark should be dropped rather than silently modified when its official code cannot reproduce the reported baseline behavior.

# Compute and Wall-Clock Budget for 8x RTX 4090

## 1. Hardware assumptions

- Eight separate RTX 4090 cards, 24 GB each.
- No single job may assume more than 24 GB VRAM.
- No tensor/model parallelism is required.
- Each GPU runs independent task, method, budget, or seed workers.
- Host RAM: 128 GB recommended; 64 GB is the practical minimum for the primary pilot.
- Local NVMe: 500 GB free recommended for the complete project; the primary alone should fit within 250 GB.

## 2. Per-run resource estimates

| Workload | VRAM | GPU-hours per job unit | Host RAM per worker | Storage per job | Notes |
|---|---:|---:|---:|---:|---|
| DM Control/MJX pilot, one task-seed-method bundle | 2–6 GB | 0.25–1.0 | 2–6 GB | 50–300 MB | Compilation can dominate the first job; reuse executables/config shapes. |
| Contact task exact MPC | 6–12 GB | 1–4 | 4–10 GB | 0.2–1 GB | Batch size should be tuned below OOM with 20% VRAM headroom. |
| High-budget capability reference | 8–16 GB | 2–8 | 4–10 GB | 0.2–1 GB | Run only on selected task/basis pairs. |
| Learned dynamics training | 4–10 GB | 2–8 | 4–8 GB | 0.2–1 GB checkpoint | Independent ensemble members can occupy different GPUs. |
| D4RL/OGBench IQL run | 3–8 GB | 1.5–6 | 4–12 GB | 0.2–2 GB | Depends on update count and encoder size. |
| Graph construction for BriCoRe | CPU-dominant or <4 GB | 0.2–2 | 16–64 GB shared | 1–20 GB | Use approximate landmarks; do not build dense all-pairs graphs. |

## 3. Pilot budget

| Component | Aggregate GPU-hours | Eight-GPU wall-clock | Storage |
|---|---:|---:|---:|
| Implementation sanity and profiling | 5–15 | 1–3 h | <1 GB |
| Core P1 sweep | 35–70 | 5–10 h | 3–8 GB |
| Robust-mass perturbations | 15–30 | 2–5 h | 1–4 GB |
| High-budget capability references | 10–25 | 2–5 h | 1–3 GB |
| Controls and reruns | 10–30 | 2–6 h | 2–5 GB |
| **Total** | **60–120** | **8–20 compute hours** | **5–15 GB** |

The 1–3 day calendar target includes installation, JAX compilation, correctness checks, and one controlled rerun. It does not assume perfect first-run code.

## 4. Full primary budget

| Phase | Aggregate GPU-hours | Expected wall-clock with eight GPUs | Priority |
|---|---:|---:|---:|
| Exact-model core across 6 tasks, 2 planners, main methods | 900–1,400 | 5–8 days | Mandatory |
| Mechanism diagnostics and phase diagrams | 350–600 | 2–4 days | Mandatory |
| Robustness, held-out states, runtime studies | 250–450 | 1.5–3 days | Mandatory |
| High-budget references and oracle analyses | 200–350 | 1–2 days | Mandatory but sparse |
| Learned-model extension | 250–500 | 1.5–3 days | Conditional |
| Final reruns and missing cells | 150–300 | 1–2 days | Reserve |
| **Total** | **2,000–3,200** | **11–18 days** | — |

These estimates assume GPU-saturated vectorized simulation. CPU-bound MuJoCo tasks may extend wall-clock even when nominal GPU-hours are low. Profile before launching the full grid.

## 5. Eight-GPU scheduling plan

### Pilot

- **GPU 0–2:** one pilot task each, FULL and LIN basis grid.
- **GPU 3–4:** replicate seeds and high-budget capability checks.
- **GPU 5:** robust perturbation diagnostics.
- **GPU 6:** low-pass/colored-noise controls.
- **GPU 7:** integration tests, failure reproduction, and held-out initial states.

### Full experiments

Use a queue with no cross-GPU process. Assign:

- GPUs 0–3 to exact-model main matrix;
- GPUs 4–5 to diagnostics and high-budget references;
- GPU 6 to second planner/integration-heavy baselines;
- GPU 7 to learned-model training or reruns.

After the exact-model matrix completes, reassign all eight GPUs to seeds and robustness. Store job manifests so failed runs are resumed, not duplicated.

## 6. Run-count sanity check

A naive Cartesian product can explode. The prioritized design should use:

- six tasks;
- two planners;
- roughly eight main method groups after pruning clearly dominated dimensions;
- four practical budgets;
- five to ten seeds.

This is 1,920–3,840 task-method-budget-seed cells. A “cell” should vectorize many initial states and episodes. High-budget references and full dimension curves are run only on a subset. Do not run every basis family at every dimension on every task after pilot trends identify dominated regions.

## 7. Backup budgets

- **BriCoRe pilot:** 80–240 GPU-hours; full 1,800–3,500 GPU-hours.
- **CRRP pilot:** 70–180 GPU-hours if a frozen policy is available; full 1,500–3,000 GPU-hours.

The backups are alternatives, not parallel full projects. Running all three full plans would exceed the rapid-paper objective.

# Ablations, Statistics, and Fairness Controls

## 1. Fairness principles

### Equal information

All primary methods observe the same state, task reward, dynamics model, horizon, constraints, and warm-start trajectory. BFAP cannot use test-set labels, future true states, or high-budget oracle outcomes.

### Equal planning resources

Count:

- every candidate rollout;
- every perturbation rollout;
- every basis probe;
- every CEM/MPPI refinement rollout;
- model-ensemble members if each requires a separate propagation.

Report both candidate trajectories and simulated state transitions. Runtime matching is secondary to exact rollout matching but must also be reported.

### Equal task

Keep identical:

- terminal success set and tolerance;
- episode horizon;
- primitive-action execution count;
- replanning frequency;
- action magnitude and rate bounds;
- collision and safety constraints;
- reward scaling and discounting.

### Equal tuning

Use the same validation states and tuning budget for:

- fixed basis and dimension;
- iCEM/MPPI hyperparameters;
- BFAP probe fraction, perturbation scale, and utility slack.

No method may receive per-test-task tuning that competitors do not receive.

## 2. Essential primary ablations

| Ablation | Question answered | Failure interpretation |
|---|---|---|
| Remove robust perturbation; use elite fraction | Is robustness necessary beyond near-optimal frequency? | If equal, simplify claim to elite mass; do not overclaim robustness. |
| Replace mass with dimension heuristic | Is the estimator doing more than choosing a middle $k$? | If equal on held-out tasks, method novelty weakens substantially. |
| Replace mass with smoothness/TV heuristic | Are gains simply due to smooth action plans? | If equal, basin mechanism unsupported. |
| Remove utility gate | Does mass alone over-select coarse bases? | Expected to fail on rapid-switch tasks; confirms need for capability preservation. |
| Fixed best basis per task | Is statewise adaptation needed? | If fixed basis wins, paper may be a phenomenon study rather than an adaptive method. |
| Fixed best basis per budget | Is adaptation merely budget selection? | BFAP should still help across heterogeneous states. |
| No warm start | Is previous-plan projection essential? | Report sensitivity; not a novelty claim. |
| Equal coefficient count with random dense decoder | Is improvement from lower dimension or structured temporal image? | Distinguishes dimension from basis inductive bias. |
| Same image, reparameterized scaling | Is the mass statistic sensitive only to coordinate scaling? | Normalize proposals; equivalent images should give similar calibrated results. |
| Matched total variation/action norm | Does damping explain success? | Primary claim fails if gain disappears. |
| High-frequency-required task | Can BFAP preserve capability? | If it never chooses fine bases, method is not adaptive. |
| Alternative perturbation distribution | Is robust mass stable to Gaussian versus bounded perturbations? | Severe instability weakens mechanism. |

## 3. Statistical plan

### Unit of analysis

The primary independent unit is a fixed initial state × planner seed × task episode. Batched candidate trajectories within one MPC decision are not independent replicates.

### Primary model

For binary success, fit a mixed-effects logistic regression:

$$
\mathrm{logit}\,P(Y=1)=
\beta_0+eta_1\log k+eta_2(\log k)^2
+\beta_3\log N
+\beta_4\log k\log N
+\gamma_{\mathrm{task}}
+u_{\mathrm{seed}}+u_{\mathrm{init}}.
$$

The preregistered signatures are:

- $\beta_2<0$ at tight budgets on affected tasks;
- $\beta_4>0$, indicating the optimal dimension shifts upward with budget.

A generalized additive model may be used for visualization, but inference should retain a prespecified parametric test.

### Pairwise effects

- Paired bootstrap over initial states and seeds for BFAP versus each strong baseline.
- Wilson intervals for success rates.
- Bootstrap confidence intervals for return and area under the budget curve.
- Holm correction within each preregistered family of primary comparisons.
- Report absolute success percentage points, relative sample reduction, and effect sizes; do not rely on p-values alone.

### Mechanism model

Predict held-out success using:

$$
\mathrm{logit}\,P(Y=1)
=
\theta_0+	heta_1\log\widehat\rho
+\theta_2\log k
+\theta_3\mathrm{TV}
+\theta_4J_{\mathrm{best,probe}}
+\theta_5\mathrm{coverage}+	ext{random effects}.
$$

Report leave-one-task-out predictive deviance, calibration, and the incremental value of $\widehat\rho$. The mechanism claim is weak if $\theta_1$ is unstable or adds negligible held-out prediction.

### Seed count

Use at least ten seeds for final cheap state-based success experiments. Five seeds may be accepted for expensive contact tasks only when each seed evaluates many paired initial states and confidence intervals are narrow. Never report only three seeds for the central claim.

## 4. Multiple-comparison discipline

Predeclare:

- three primary tasks or a fixed six-task full suite;
- the primary budget $N=256$;
- BFAP versus FULL-iCEM as the main comparison;
- robust mass versus success as the co-primary mechanism test;
- all other basis families and budgets as secondary.

This prevents selecting whichever basis, budget, or tolerance happens to look best.

## 5. Negative-result value

A well-executed negative result remains informative if it demonstrates one of the following:

- colored-noise full-space planners erase apparent dimension benefits;
- high-budget utility loss, not basin mass, explains restricted-basis success;
- robust mass fails to predict adaptive optimization after CEM updates;
- action-space compression helps only on low-bandwidth tasks and cannot be selected reliably.

Such a result may support an analysis note or benchmark report, but it does not justify continuing toward the proposed main-conference paper without a new, independently novel claim.

# Risk Register and Kill Criteria

## 1. Primary risk register

| Risk | Probability | Impact | Early indicator | Mitigation | Binding kill condition |
|---|---|---|---|---|---|
| Fixed structured controls already match BFAP | Medium-high | High | Validation-best basis equals or exceeds BFAP | Improve budget allocation only if mechanism is already positive; compare per-state heterogeneity | BFAP loses after exact rollout accounting on four of six tasks and has no held-out-task advantage. |
| Full iCEM/low-pass baseline erases effect | Medium | High | FULL-white loses but FULL-iCEM does not | Treat colored noise as mandatory from pilot start | No ≥10-point success gain on two pilot tasks. |
| Coarse basis loses real capability | Medium | High | $\kappa<0.95$ | Utility gate, finer basis grid | Winning basis fails capability floor. |
| Robust mass estimator is too sparse | Medium | High | Almost all counts zero at practical budgets | Use near-optimal task thresholds, beta-binomial confidence, importance/rare-event diagnostics | Mechanism statistic cannot be estimated without more rollouts than it saves. |
| Threshold is circular | Medium | High | Weak bases look robust around weak returns | Shared task-native/cross-basis threshold and high-budget calibration | Results reverse under a shared threshold. |
| Gains are smoothness or low energy | Medium | High | Action TV/energy predicts all performance | Matched constraints and strong spectral controls | Gain vanishes when matched. |
| Only one task family works | Medium | High | Positive only on reacher-like tasks | Add contact/rapid-switch tasks | Fewer than two environment families support the effect. |
| Integration cost dominates | Medium | Medium | More than two days before one official task reproduces | Use Hydrax/Predictive Sampling substrate; drop incompatible baselines transparently | Pilot cannot reproduce one task and baseline within three calendar days. |
| Learned-model extension fails | Medium | Medium | Model exploitation dominates | Keep exact-model paper core; analyze model error | Not a kill if exact-model story is strong; drop learned-model claim. |
| Recent prior art is a functional duplicate | Low-medium | Critical | New paper selects action basis using success probability and utility floor | Immediate literature re-audit | Exact duplicate found before submission. |

## 2. Primary stop conditions

Stop the primary project immediately when any of these occurs:

1. The pilot effect is absent on two of three tasks against FULL-iCEM.
2. The best intermediate basis has capability retention below 0.95.
3. Gains disappear under matched total variation/action energy or low-pass controls.
4. Robust near-optimal mass does not predict success beyond best probe return and dimension.
5. BFAP's probing overhead consumes more rollouts than the selected basis saves.
6. The effect remains confined to one trivial target-reaching environment.
7. Adversarial prior-art search finds a published or accepted method with the same input/output, criterion, adaptive procedure, and empirical claim.

Only one tightly scoped repair is allowed for an implementation or estimator bug. Do not retry a scientifically failed one-shot pilot by changing tasks, thresholds, and definitions until a positive result appears.

## 3. Backup A stop conditions

Stop BriCoRe if:

- bridge-preserving subsets do not beat random/return subsets on at least two stitching-heavy tasks;
- causal removal of low-return high-bridge transitions is no worse than matched controls;
- results depend on one graph discretization;
- ReDOR or simple coverage selection matches the method;
- improvements require extra synthetic transitions or more gradient updates.

## 4. Backup B stop conditions

Stop CRRP if:

- no region-width inverted-U appears on two tasks;
- exact final success does not improve over point-graph baselines;
- the gain comes from more primitive steps or a looser terminal goal;
- region predecessor estimates are uncalibrated and false inclusion drives failure;
- Abstract Value Iteration or skill-chain initiation sets already implement the same functional method after closer inspection.

# Paper Narrative and Venue Fit

## 1. Intended narrative

### Problem

Sampling-based planners often search a full per-time-step action sequence because it is nominally the most expressive. Under a tight rollout budget, however, this may make the useful action set vanishingly hard to discover.

### Surprising observation

On narrow-tolerance tasks, adding action degrees of freedom can decrease strict success even though high-budget attainable utility is unchanged or higher. Success peaks at an intermediate temporal resolution and the optimum shifts with the rollout budget.

### Mechanism

The planner sees proposal-normalized robust near-optimal mass, not set inclusion. Restricted temporal images remove nuisance directions and enlarge the relative preimage of success; excessive restriction introduces approximation regret.

### Method

BFAP probes nested action bases, removes those that cannot meet a shared utility floor, estimates robust near-optimal mass under an exactly charged budget, and allocates the remaining rollouts to the most discoverable feasible representation.

### Evidence chain

1. mathematical construction;
2. exact-model phase diagram;
3. robust-mass prediction;
4. same-budget adaptive selection;
5. strong structured-sampling controls;
6. cross-task and cross-planner robustness;
7. explicit high-frequency and model-error failure cases.

## 2. Likely reviewer questions and required answers

| Reviewer question | Required answer in the paper |
|---|---|
| Why is this not just smoothing? | Full-space colored-noise/low-pass controls, matched TV/energy, multiple basis families, and a task where BFAP selects high frequency. |
| Why not tune $k$ once? | Per-state and per-budget heterogeneity; BFAP beats validation-best fixed $k$ on held-out states/tasks at equal rollout cost. |
| Is volume parameterization-dependent? | Yes; the operational object is proposal-normalized hit mass. Equivalent-image reparameterization ablations test calibration. |
| Does a coarse basis lower attainable reward? | Capability-retention reference and utility gate. |
| Is the theory too trivial? | Keep theorem modest, then earn scientific value through a predictive phase diagram and mechanism diagnostics. |
| Does it work with learned models? | Conditional extension; exact-model result remains the clean causal core. |
| Why AI rather than classical control? | The contribution concerns finite-budget black-box planning, adaptive representation choice, and model-based decision search across benchmark tasks; venue framing should emphasize learning/planning methodology, not hardware control. |

## 3. Venue fit

| Venue | Fit | Conditions |
|---|---|---|
| ICLR | Strong if representation geometry, finite-budget phenomenon, and held-out prediction are central | Requires broad tasks and a clean mechanistic story, not an application-specific controller. |
| NeurIPS | Strong if theory/optimization and extensive empirical analysis are balanced | Strong baselines, statistical rigor, and generality across planners are necessary. |
| ICML | Strong if the selection principle and finite-budget theory are technically crisp | Must separate clearly from existing proposal-design and latent-action work. |
| CoRL | Strong for contact-rich planning and real-time MPC evidence | Would benefit from manipulation/locomotion tasks; real hardware is not required but may be expected by some reviewers. |
| RSS | Plausible if planning/control novelty and trajectory evidence dominate | Needs a robotics-focused formulation and strong structured-sampling comparisons. |
| TMLR | Good fallback for a thorough mechanism and benchmark study | Less deadline pressure; suitable if results are solid but not sufficiently broad for a top conference. |
| L4DC | Good focused venue for finite-budget control representation and theory | Strong fit if empirical scope is smaller and control theory is stronger. |
| AAAI / IJCAI | Plausible for the offline-RL backups | The primary may fit, but the closest reviewer community is more likely at ICML/NeurIPS/CoRL. |

No venue or oral outcome is promised. A potential oral-level story requires the phase diagram and mechanism to feel inevitable after the fact yet surprising before the experiment; a small performance bump from splines is far below that bar.

# Two Backup Directions

## Backup A transition plan — BriCoRe

Switch to BriCoRe only after the BFAP pilot is killed by evidence, not merely delayed by engineering. The fastest transition is:

1. use D4RL/OGBench state datasets already downloaded for GCRL-related work;
2. implement raw-state landmark graph and sampled source-goal reachability;
3. run the causal bridge-removal test before building the full coreset optimizer;
4. train IQL on 20% subsets selected by random, return, k-center, and bridge score;
5. stop unless the causal diagnostic and learner performance agree.

A strong BriCoRe paper would be about **dataset topology as a causal resource**, not another offline RL objective.

## Backup B transition plan — CRRP

Switch to CRRP only if a reliable frozen goal-conditioned policy and OGBench pipeline are already available. Begin with exact maze predecessor visualizations. Do not train separate options or use pixels. The 2026 set-abstraction, quasimetric-map, spectral-subgoal, and subset-goal literature [R13–R16] makes this a **high-novelty-risk backup**. The first result must show that a moderately wide intermediate region increases the empirical predecessor set and exact final success under an unchanged terminal set and fixed primitive horizon. It must also beat point ensembles, ordinary graph search, AQM-style reachability maps, and bottleneck-point subgoals on the mechanism diagnostic. If any of those controls match it, stop.

## Comparative trigger table

| Evidence after primary pilot | Next action |
|---|---|
| BFAP passes all gates | Continue BFAP; do not split compute across backups. |
| BFAP phenomenon exists but method does not beat tuned fixed basis | Consider a narrower phenomenon paper only if phase-diagram evidence is unusually strong; otherwise test BriCoRe. |
| BFAP fails because full-space strong samplers dominate | Test BriCoRe causal bridge-removal pilot. |
| BriCoRe fails topology causal test | Test CRRP only if the frozen-policy infrastructure is ready. |
| CRRP also fails | **Global NO-GO.** Do not force the seed into LLMs, robotics hardware, or a custom benchmark. |

# Verified Bibliography

The entries below were checked against official proceedings pages, OpenReview records, journal pages, arXiv records, or official project repositories available on **2026-08-25**. “Published” means that a proceedings or journal record was located; “preprint” does not imply peer review. Repository entries are included only when they are needed to reproduce the proposed pilots.

## Planning, action representation, and sampling-based control

- **[P01]** Chuyuan Tao, Fanxin Wang, Haolong Jiang, Jia He, Yiyang Chen, and Qinglei Bu. “[Sampling Strategy Design for Model Predictive Path Integral Control on Legged Robot Locomotion](https://arxiv.org/abs/2601.01409).” *arXiv preprint*, 2026.

- **[P02]** An T. Le, Khai Nguyen, Minh Nhat Vu, João Carvalho, and Jan Peters. “[Model Tensor Planning](https://openreview.net/forum?id=fk1ZZdXCE3).” *Transactions on Machine Learning Research*, published 2025; presented through the TMLR Journal-to-Conference track at ICLR 2026. [arXiv](https://arxiv.org/abs/2505.01059).

- **[P03]** O. Goktug Poyrazoglu, Yukang Cao, and Volkan Isler. “[C-Uniform Trajectory Sampling for Fast Motion Planning](https://arxiv.org/abs/2409.12266).” *IEEE International Conference on Robotics and Automation (ICRA)*, published 2025. [IEEE record](https://ieeexplore.ieee.org/document/11127482/).

- **[P04]** Piotr Kicki. “[Low-pass Sampling in Model Predictive Path Integral Control](https://arxiv.org/abs/2503.11717).” *arXiv preprint*, 2025.

- **[P05]** Zeji Yi, Chaoyi Pan, Guanqi He, Guannan Qu, and Guanya Shi. “[CoVO-MPC: Theoretical Analysis of Sampling-based MPC and Optimal Covariance Design](https://proceedings.mlr.press/v242/yi24b.html).” *Learning for Dynamics and Control Conference (L4DC), PMLR 242*, published 2024. [arXiv](https://arxiv.org/abs/2401.07369).

- **[P06]** Joe Watson and Jan Peters. “[Inferring Smooth Control: Monte Carlo Posterior Policy Iteration with Gaussian Processes](https://proceedings.mlr.press/v205/watson23a.html).” *Conference on Robot Learning (CoRL 2022), PMLR 205*, published 2023.

- **[P07]** Cristina Pinneri, Shambhuraj Sawant, Sebastian Blaes, Jan Achterhold, Joerg Stueckler, Michal Rolinek, and Georg Martius. “[Sample-efficient Cross-Entropy Method for Real-time Planning](https://proceedings.mlr.press/v155/pinneri21a.html).” *Conference on Robot Learning (CoRL 2020), PMLR 155*, published 2021.

- **[P08]** Homanga Bharadhwaj, Kevin Xie, and Florian Shkurti. “[Model-Predictive Control via Cross-Entropy and Gradient-Based Optimization](https://proceedings.mlr.press/v120/bharadhwaj20a.html).” *Learning for Dynamics and Control (L4DC), PMLR 120*, published 2020.

- **[P09]** Mohak Bhardwaj, Balakumar Sundaralingam, Arsalan Mousavian, Nathan D. Ratliff, Dieter Fox, Fabio Ramos, and Byron Boots. “[STORM: An Integrated Framework for Fast Joint-Space Model-Predictive Control for Reactive Manipulation](https://proceedings.mlr.press/v164/bhardwaj22a.html).” *Conference on Robot Learning (CoRL 2021), PMLR 164*, published 2022.

- **[P10]** Jacob Sacks and Byron Boots. “[Learning Sampling Distributions for Model Predictive Control](https://proceedings.mlr.press/v205/sacks23a.html).” *Conference on Robot Learning (CoRL 2022), PMLR 205*, published 2023.

- **[P11]** James Power and Dmitry Berenson. “[Learning a Generalizable Trajectory Sampling Distribution for Model Predictive Control](https://doi.org/10.1109/TRO.2024.3512440).” *IEEE Transactions on Robotics*, published 2024. [Official project page](https://thomaspower.net/project/more/).

- **[P12]** Juan Alvarez-Padilla, John Z. Zhang, Sofia Kwok, John M. Dolan, and Zachary Manchester. “[Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control](https://arxiv.org/abs/2409.10469).” *IEEE International Conference on Robotics and Automation (ICRA)*, published 2025. [Project page](https://whole-body-mppi.github.io/).

- **[P13]** Taylor A. Howell, Nimrod Gileadi, Saran Tunyasuvunakool, Kevin Zakka, Tom Erez, and Yuval Tassa. “[Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo](https://arxiv.org/abs/2212.00541).” *arXiv software/technical preprint*, 2022.

- **[P14]** Zhengyao Jiang, Tianjun Zhang, Michael Janner, Yueying Li, Tim Rocktäschel, Edward Grefenstette, and Yuandong Tian. “[Efficient Planning in a Compact Latent Action Space](https://openreview.net/forum?id=cA77NrVEuqn).” *International Conference on Learning Representations (ICLR)*, published 2023. [arXiv](https://arxiv.org/abs/2208.10291).

- **[P15]** Chenyu Yang, Davide Liconti, and Robert K. Katzschmann. “[VQ-ACE: Efficient Policy Search for Dexterous Robotic Manipulation via Action Chunking Embedding](https://arxiv.org/abs/2411.03556).” *arXiv preprint*, 2024.

- **[P16]** Hongyi Zhou, Weiran Liao, Xi Huang, Yucheng Tang, Fabian Otto, Xiaogang Jia, Xinkai Jiang, Simon Hilber, Ge Li, Qian Wang, Ömer Erdinç Yağmurlu, Nils Blank, Moritz Reuss, and Rudolf Lioutikov. “[BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning](https://openreview.net/forum?id=rQCl1sf62w).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2025. [arXiv](https://arxiv.org/abs/2506.06072).

- **[P17]** Xiaoshen Han, Haoyu Xiong, Haonan Chen, Chaoqi Liu, Antonio Torralba, Yuke Zhu, and Yilun Du. “[B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations](https://arxiv.org/abs/2607.09648).” *arXiv preprint*, 2026.

- **[P18]** Markus Walker, Daniel Frisch, and Uwe D. Hanebeck. “[Sample-Efficient and Smooth Cross-Entropy Method Model Predictive Control Using Deterministic Samples](https://arxiv.org/abs/2510.05706).” *American Control Conference (ACC)*, published 2026; preprint first posted 2025.

- **[P19]** Fabian Schramm, Pierre Fabre, Nicolas Perrin-Gilbert, and Justin Carpentier. “[Reference-Free Sampling-Based Model Predictive Control](https://arxiv.org/abs/2511.19204).” *IEEE International Conference on Robotics and Automation (ICRA)*, published 2026; preprint first posted 2025.

- **[P20]** Nicholas N. Sun, Gregory G. Droge, César A. Uribe, and Magnus Egerstedt. “[Adaptive Parameterized Model Predictive Control](https://doi.org/10.1109/LCSYS.2024.3492581).” *IEEE Control Systems Letters*, published 2024.

- **[P21]** R. Cagienard, P. Grieder, E. C. Kerrigan, and M. Morari. “[Move Blocking Strategies in Receding Horizon Control](https://doi.org/10.1016/j.jprocont.2007.01.001).” *Journal of Process Control* 17(6), published 2007.

- **[P22]** Emilio Conal Campana, Christian Boysen, Steffen E. Mattsson, and Nils Görtz. “[Model Predictive Control with Dynamic Move Blocking](https://arxiv.org/abs/2308.07854).” *European Control Conference (ECC)*, published 2024.

- **[P23]** Russ Tedrake, Ian R. Manchester, Mark Tobenkin, and John W. Roberts. “[LQR-Trees: Feedback Motion Planning via Sums-of-Squares Verification](https://groups.csail.mit.edu/robotics-center/public_papers/Tedrake10.pdf).” *International Journal of Robotics Research* 29(8), published 2010.

- **[P24]** Mark M. Tobenkin, Ian R. Manchester, and Russ Tedrake. “[Invariant Funnels around Trajectories using Sum-of-Squares Programming](https://groups.csail.mit.edu/robotics-center/public_papers/Tobenkin11.pdf).” *18th IFAC World Congress*, published 2011.

- **[P25]** Anirudha Majumdar and Russ Tedrake. “[Funnel Libraries for Real-Time Robust Feedback Motion Planning](https://arxiv.org/abs/1601.04037).” *International Journal of Robotics Research*, published 2017.

- **[P26]** Renhao Wang, Shijun Zhang, Qinghua Sun, Zhi Zeng, and Xiaohong Guan. “[Model-based Reinforcement Learning for Parameterized Action Spaces](https://proceedings.mlr.press/v235/wang24ah.html).” *International Conference on Machine Learning (ICML), PMLR 235*, published 2024.

- **[P27]** Grady Williams, Paul Drews, Brian Goldfain, James M. Rehg, and Evangelos A. Theodorou. “[Information-Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving](https://arxiv.org/abs/1707.02342).” *IEEE Transactions on Robotics*, published 2018.

- **[P28]** Marin Kobilarov. “[Cross-Entropy Motion Planning](https://doi.org/10.1177/0278364912444543).” *International Journal of Robotics Research* 31(7), published 2012.

- **[P29]** Bogdan Vlahov, Jason Gibson, David D. Fan, Patrick Spieler, Ali-akbar Agha-mohammadi, and Evangelos A. Theodorou. “[Low Frequency Sampling in Model Predictive Path Integral Control](https://arxiv.org/abs/2404.03094).” *IEEE Robotics and Automation Letters* 9(5), published 2024. [DOI](https://doi.org/10.1109/LRA.2024.3382530).

## Reachability, subgoals, and skill composition

- **[R01]** George Dimitri Konidaris and Andrew G. Barto. “[Skill Discovery in Continuous Reinforcement Learning Domains using Skill Chaining](https://proceedings.neurips.cc/paper/2009/hash/621bf66ddb7c962aa0d22ac97d69b793-Abstract.html).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2009.

- **[R02]** Akhil Bagaria and George Konidaris. “[Option Discovery using Deep Skill Chaining](https://openreview.net/forum?id=B1gqipNYwH).” *International Conference on Learning Representations (ICLR)*, published 2020.

- **[R03]** Akhil Bagaria, Jason K. Senthil, Matthew Slivinski, and George Konidaris. “[Skill Discovery for Exploration and Planning using Deep Skill Graphs](https://proceedings.mlr.press/v139/bagaria21a.html).” *International Conference on Machine Learning (ICML), PMLR 139*, published 2021.

- **[R04]** Kishor Jothimurugan, Steve Hsu, Osbert Bastani, and Rajeev Alur. “[Robustly Learning Composable Options in Deep Reinforcement Learning](https://www.ijcai.org/proceedings/2021/0380.pdf).” *International Joint Conference on Artificial Intelligence (IJCAI)*, published 2021.

- **[R05]** Benjamin Eysenbach, Ruslan Salakhutdinov, and Sergey Levine. “[Search on the Replay Buffer: Bridging Planning and Reinforcement Learning](https://arxiv.org/abs/1906.05253).” *arXiv preprint*, 2019.

- **[R06]** Elliot Chane-Sane, Cordelia Schmid, and Ivan Laptev. “[Goal-Conditioned Reinforcement Learning with Imagined Subgoals](https://proceedings.mlr.press/v139/chane-sane21a.html).” *International Conference on Machine Learning (ICML), PMLR 139*, published 2021. [arXiv](https://arxiv.org/abs/2107.00541).

- **[R07]** Evgenii Opryshko, Junwei Quan, Claas Voelcker, Yilun Du, and Igor Gilitschenski. “[Test-Time Graph Search for Goal-Conditioned Reinforcement Learning](https://openreview.net/forum?id=mxXm8jqgds).” *International Conference on Machine Learning (ICML)*, published 2026. [arXiv](https://arxiv.org/abs/2510.07257).

- **[R08]** Archit Sharma, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn. “[Autonomous Reinforcement Learning via Subgoal Curricula](https://arxiv.org/abs/2107.12931).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2021.

- **[R09]** Youngwoon Lee, Joseph J. Lim, Anima Anandkumar, and Yuke Zhu. “[Adversarial Skill Chaining for Long-Horizon Robot Manipulation via Terminal State Regularization](https://arxiv.org/abs/2111.07999).” *Conference on Robot Learning (CoRL 2021), PMLR 164*, published 2022.

- **[R10]** Kishor Jothimurugan, Osbert Bastani, and Rajeev Alur. “[Abstract Value Iteration for Hierarchical Reinforcement Learning](https://proceedings.mlr.press/v130/jothimurugan21a.html).” *International Conference on Artificial Intelligence and Statistics (AISTATS), PMLR 130*, published 2021.

- **[R11]** Tom Jurgenson, Or Avner, Edward Groshev, and Aviv Tamar. “[Sub-Goal Trees — A Framework for Goal-Based Reinforcement Learning](https://proceedings.mlr.press/v119/jurgenson20a.html).” *International Conference on Machine Learning (ICML), PMLR 119*, published 2020. [arXiv](https://arxiv.org/abs/2002.12361).

- **[R12]** Kaiqiang Ke, Shenghong He, Chengdong Xu, Yuheng Luo, Xiangyuan Lan, and Chao Yu. “[Adaptive Coarse-to-Fine Subgoal Refinement for Long-Horizon Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2605.28127).” *arXiv preprint*, 2026.

- **[R13]** Fabian Wurzberger, Sebastian Gottwald, Zeqiang Zhang, and Daniel Alexander Braun. “[Hierarchical Goal Abstractions via Learned Subset Relations](https://openreview.net/forum?id=Qoh16QHG24).” *International Conference on Machine Learning (ICML)*, published 2026.

- **[R14]** Anthony Kobanda, Waris Radji, Odalric-Ambrym Maillard, and Rémy Portelas. “[Adaptive Quasimetric Mapping: Principled Topological Abstraction for Robust Offline Goal-Conditioned Navigation](https://openreview.net/forum?id=uM1kfO79EB).” *International Conference on Machine Learning (ICML)*, published 2026.

- **[R15]** Hebin Liang, Yi Ma, Chenjun Xiao, Zibin Dong, Zilin Cao, Fei Ni, Yifu Yuan, and Jianye Hao. “[Bottleneck-Guided Spectral Subgoals For Offline Goal-Conditioned RL](https://openreview.net/forum?id=l4Q8dGGHVC).” *International Conference on Machine Learning (ICML)*, published 2026.

- **[R16]** Simon Ståhlberg and Hector Geffner. “[First-Order Representation Languages for Goal-Conditioned RL](https://ojs.aaai.org/index.php/AAAI/article/view/40960).” *AAAI Conference on Artificial Intelligence*, published 2026, 40(43):36394–36402. [DOI](https://doi.org/10.1609/aaai.v40i43.40960); [arXiv](https://arxiv.org/abs/2512.19355).

## Offline reinforcement learning, data selection, and trajectory stitching

- **[D01]** Yiqin Yang, Quanwei Wang, Chenghao Li, Hao Hu, Chengjie Wu, Yuhua Jiang, Dianyu Zhong, Ziyou Zhang, Qianchuan Zhao, Chongjie Zhang, and Bo Xu. “[Fewer May Be Better: Enhancing Offline Reinforcement Learning with Reduced Dataset](https://openreview.net/forum?id=zqtql1YmlS).” *International Conference on Learning Representations (ICLR)*, published 2025. [arXiv](https://arxiv.org/abs/2502.18955).

- **[D02]** Seungho Baek, Taegeon Park, Jongchan Park, Seungjun Oh, and Yusung Kim. “[Graph-Assisted Stitching for Offline Hierarchical Reinforcement Learning](https://proceedings.mlr.press/v267/baek25a.html).” *International Conference on Machine Learning (ICML), PMLR 267*, published 2025. [arXiv](https://arxiv.org/abs/2506.07744); [project page](https://qortmdgh4141.github.io/projects/GAS/).

- **[D03]** Guanghe Li, Yixiang Shan, Zhengbang Zhu, Ting Long, and Weinan Zhang. “[DiffStitch: Boosting Offline Reinforcement Learning with Diffusion-based Trajectory Stitching](https://arxiv.org/abs/2402.02439).” *International Conference on Machine Learning (ICML)*, published 2024.

- **[D04]** Tianyu Gu, Rishabh Joshi, Jialu Li, and Daniel P. Palomar. “[Stitching Sub-Trajectories with Conditional Diffusion Model for Goal-Conditioned Offline Reinforcement Learning](https://arxiv.org/abs/2402.07226).” *AAAI Conference on Artificial Intelligence*, published 2024.

- **[D05]** Ambedkar Dukkipati, Ranga Shaarad Ayyagari, Bodhisattwa Dasgupta, Parag Dutta, and Prabhas Reddy Onteru. “[Active Reinforcement Learning Strategies for Offline Policy Improvement](https://ojs.aaai.org/index.php/AAAI/article/view/33803).” *AAAI Conference on Artificial Intelligence*, published 2025. [arXiv](https://arxiv.org/abs/2412.13106).

- **[D06]** Kajetan Schweighofer, Andreas Radler, Marius-Constantin Dinu, Markus Hofmarcher, Vihang Patil, Angela Bitto-Nemling, Hamid Eghbal-zadeh, and Sepp Hochreiter. “[A Dataset Perspective on Offline Reinforcement Learning](https://proceedings.mlr.press/v199/schweighofer22a.html).” *Conference on Lifelong Learning Agents (CoLLAs), PMLR 199*, published 2022. [arXiv](https://arxiv.org/abs/2111.04714).

- **[D07]** Zeyu Jia, Alexander Rakhlin, Ayush Sekhari, and Chen-Yu Wei. “[Offline Reinforcement Learning: Role of State Aggregation and Trajectory Data](https://proceedings.mlr.press/v247/jia24a.html).” *Conference on Learning Theory (COLT), PMLR 247*, published 2024. [arXiv](https://arxiv.org/abs/2403.17091).

- **[D08]** Allen Nie, Yannis Flet-Berliac, Deon R. Jordan, William Steenbergen, and Emma Brunskill. “[Data-Efficient Pipeline for Offline Reinforcement Learning with Limited Data](https://arxiv.org/abs/2210.08642).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2022.

- **[D09]** Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, and Sergey Levine. “[D4RL: Datasets for Deep Data-Driven Reinforcement Learning](https://arxiv.org/abs/2004.07219).” *arXiv benchmark release*, 2020.

- **[D10]** Ilya Kostrikov, Ashvin Nair, and Sergey Levine. “[Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8).” *International Conference on Learning Representations (ICLR)*, published 2022.

- **[D11]** Scott Fujimoto and Shixiang Shane Gu. “[A Minimalist Approach to Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2021/hash/a8166da05c5a094f7dc03724b41886e5-Abstract.html).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2021.

- **[D12]** Zhao-Heng Yin and Pieter Abbeel. “[Offline Imitation Learning Through Graph Search and Retrieval](https://www.roboticsproceedings.org/rss20/p054.html).” *Robotics: Science and Systems (RSS XX)*, published 2024. [arXiv](https://arxiv.org/abs/2407.15403).

## Adjacent mechanisms used in elimination

- **[E01]** Ananya Kumar, Tengyu Ma, and Percy Liang. “[Understanding Self-Training for Gradual Domain Adaptation](https://proceedings.mlr.press/v119/kumar20c.html).” *International Conference on Machine Learning (ICML), PMLR 119*, published 2020. [arXiv](https://arxiv.org/abs/2002.11361).

- **[E02]** Haoxiang Wang, Bo Li, and Han Zhao. “[Understanding Gradual Domain Adaptation: Improved Analysis, Optimal Path and Beyond](https://proceedings.mlr.press/v162/wang22n.html).” *International Conference on Machine Learning (ICML), PMLR 162*, published 2022.

- **[E03]** Haoxiang Wang, Bo Li, and Han Zhao. “[Gradual Domain Adaptation: Theory and Algorithms](https://jmlr.org/papers/v25/23-1180.html).” *Journal of Machine Learning Research* 25, published 2024.

- **[E04]** Zhan Zhuang, Yu Zhang, and Ying Wei. “[Gradual Domain Adaptation via Gradient Flow](https://openreview.net/forum?id=iTTZFKrlGV).” *International Conference on Learning Representations (ICLR)*, published 2024.

- **[E05]** Akriti Jain and Aparna Garimella. “[Modeling Contextual Passage Utility for Multihop Question Answering](https://aclanthology.org/2025.ijcnlp-short.37/).” *IJCNLP-AACL, Short Papers*, published 2025.

- **[E06]** Andre Bacellar. “[BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering](https://arxiv.org/abs/2604.03384).” *arXiv preprint*, 2026.

- **[E07]** Akari Asai, Kazuma Hashimoto, Hannaneh Hajishirzi, Richard Socher, and Caiming Xiong. “[Learning to Retrieve Reasoning Paths over Wikipedia Graph for Question Answering](https://openreview.net/forum?id=SJgVHkrYDH).” *International Conference on Learning Representations (ICLR)*, published 2020.

- **[E08]** Uri Alon and Eran Yahav. “[On the Bottleneck of Graph Neural Networks and its Practical Implications](https://openreview.net/forum?id=i80OPhOCVH2).” *International Conference on Learning Representations (ICLR)*, published 2021. [arXiv](https://arxiv.org/abs/2006.05205).

- **[E09]** Jake Topping, Francesco Di Giovanni, Benjamin P. Chamberlain, Xiaowen Dong, and Michael M. Bronstein. “[Understanding Over-Squashing and Bottlenecks on Graphs via Curvature](https://openreview.net/forum?id=7UmjRGzp-A).” *International Conference on Learning Representations (ICLR)*, published 2022. [arXiv](https://arxiv.org/abs/2111.14522).

- **[E10]** Jiawei Zhao, Yifei Zhang, Beidi Chen, Florian Schäfer, and Anima Anandkumar. “[InRank: Incremental Low-Rank Learning](https://arxiv.org/abs/2306.11250).” *arXiv preprint*, 2023.

- **[E11]** Enric Boix-Adsera, Etai Littwin, Emmanuel Abbe, Samy Bengio, and Joshua Susskind. “[Transformers Learn Through Gradual Rank Increase](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4d69c1c057a8bd570ba4a7b71aae8331-Abstract-Conference.html).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2023. [arXiv](https://arxiv.org/abs/2306.07042).

- **[E12]** Changmin Yu, Neil Burgess, Maneesh Sahani, and Samuel J. Gershman. “[Successor-Predecessor Intrinsic Exploration](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e6f2b968c4ee8ba260cd7077e39590dd-Abstract-Conference.html).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2023. [arXiv](https://arxiv.org/abs/2305.15277).

- **[E13]** Ahmed Touati and Yann Ollivier. “[Learning One Representation to Optimize All Rewards](https://proceedings.neurips.cc/paper/2021/hash/076a0c97d09cf1a0ec3e19c7f2529f2b-Abstract.html).” *Advances in Neural Information Processing Systems (NeurIPS)*, published 2021. [arXiv](https://arxiv.org/abs/2103.07945).

## Benchmarks, datasets, and official software

- **[S01]** Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez, Yazhe Li, Diego de Las Casas, David Budden, Abbas Abdolmaleki, Josh Merel, Andrew Lefrancq, Timothy Lillicrap, and Martin Riedmiller. “[DeepMind Control Suite](https://arxiv.org/abs/1801.00690).” *arXiv benchmark/technical report*, 2018. [Official repository](https://github.com/google-deepmind/dm_control).

- **[S02]** Emanuel Todorov, Tom Erez, and Yuval Tassa. “[MuJoCo: A Physics Engine for Model-Based Control](https://mujoco.org/).” *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, published 2012; official software site linked.

- **[S03]** Google DeepMind. “[MJX Documentation](https://mujoco.readthedocs.io/en/stable/mjx.html).” *Official software documentation*, accessed 2026-08-25.

- **[S04]** Google DeepMind. “[MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground).” *Official open-source benchmark repository*, accessed 2026-08-25.

- **[S05]** Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song. “[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://diffusion-policy.cs.columbia.edu/).” *Robotics: Science and Systems (RSS)*, published 2023; official project includes the PushT benchmark.

- **[S06]** Vince Kurtz. “[Hydrax: GPU-Accelerated Sampling-Based Model Predictive Control in JAX](https://github.com/vincekurtz/hydrax).” *Open-source software*, accessed 2026-08-25.

- **[S07]** Google DeepMind. “[MuJoCo MPC](https://github.com/google-deepmind/mujoco_mpc).” *Official open-source software*, accessed 2026-08-25.

- **[S08]** An T. Le, Khai Nguyen, Minh Nhat Vu, João Carvalho, and Jan Peters. “[Model Tensor Planning Official Implementation](https://github.com/anindex/mtp).” *Open-source software accompanying [P02]*, accessed 2026-08-25.

- **[S09]** Seohong Park, Kevin Frans, Benjamin Eysenbach, and Sergey Levine. “[OGBench: Benchmarking Offline Goal-Conditioned RL](https://openreview.net/forum?id=M992mjgtil).” *International Conference on Learning Representations (ICLR)*, published 2025. [arXiv](https://arxiv.org/abs/2410.20092); [official repository](https://github.com/seohongpark/ogbench).

# Search Log

## Retrieval window and scope

- **Retrieval date:** 2026-08-25.
- **Primary coverage:** 2023–2026, including recent preprints and 2026 OpenReview/arXiv records available by the retrieval date.
- **Backward tracing:** 2007–2022 for control parameterization, move blocking, funnels, skill chaining, graph search, offline-RL datasets, and foundational benchmarks.
- **Domains searched:** sampling-based model-predictive control, motion planning, model-based RL, action representation, imitation learning, hierarchical and goal-conditioned RL, offline RL and dataset selection, information retrieval, domain adaptation, graph learning, and neural-network optimization.
- **Preferred evidence:** official proceedings and journal pages; OpenReview; PMLR; NeurIPS proceedings; AAAI and IJCAI proceedings; ACL Anthology; RSS proceedings; IEEE records; JMLR; arXiv; official project pages and repositories.

## Search sequence

The search followed four passes.

1. **Breadth pass.** Build a mechanism-level synonym map and generate 16 candidates without committing to a subfield.
2. **Duplicate-hunting pass.** For each plausible candidate, search alternative terminology and neighboring application areas with the explicit goal of finding a functional duplicate.
3. **Backward/forward pass.** Trace recent papers to the foundational methods they cite and search for later methods that extend the same mechanism.
4. **Execution pass.** Verify benchmark availability, official code, per-run memory plausibility, and whether a 1–3 day pilot can distinguish the claim.

## Major query families

The table records representative query families rather than every syntactic variation. Quoted phrases, singular/plural variants, method acronyms, exact titles, author names, and venue-specific domain filters were also used.

| ID | Major query family | Years emphasized | Purpose and result |
|---|---|---:|---|
| Q01 | `success set`, `successful action set`, `success basin`, `capture basin`, `near-optimal set volume`, `preimage volume` + planning/control | 2018–2026 | Searched for an existing action-proposal-space success-mass objective. Found abundant state-space reachability and robustness work, but no exact BFAP combination. |
| Q02 | `backward reachable set`, `predecessor set`, `region of attraction`, `viability kernel`, `funnel composition` | 2009–2026 | Established the formal state-space relatives: LQR-trees, invariant funnels, funnel libraries, skill initiation sets. |
| Q03 | `action parameterization`, `trajectory parameterization`, `control knots`, `spline controls`, `B-spline MPC` | 2018–2026 | Found extensive fixed structured-control work, including MTP, whole-body MPPI, Reference-Free MPC, B-spline policies, and the 2026 interpolation study. Eliminated fixed splines as a standalone novelty. |
| Q04 | `low-frequency sampling`, `low-pass MPPI`, `colored noise CEM`, `smooth control prior` | 2018–2026 | Found iCEM, GP priors, low-frequency MPPI, and low-pass sampling. These became mandatory baselines and controls. |
| Q05 | `learned sampling distribution MPC`, `latent action planning`, `compact action space`, `normalizing flow MPC` | 2020–2026 | Found TAP and learned proposal distributions. Eliminated a generic learned-latent-action paper. |
| Q06 | `adaptive action representation`, `adaptive action dimension`, `adaptive knots`, `adaptive temporal resolution MPC` | 2018–2026 | Searched directly for online representation selection. Found adjacent adaptive parameterized MPC and dynamic move blocking, but not the same normalized success-mass selector. |
| Q07 | `move blocking`, `dynamic move blocking`, `control horizon compression`, `adaptive blocking MPC` | 2007–2026 | Identified classical deterministic-control precedents. These require BFAP to distinguish finite-budget sampling geometry from constraint-count reduction alone. |
| Q08 | `CEM trajectory optimization`, `MPPI covariance design`, `low-discrepancy samples`, `deterministic samples MPC` | 2012–2026 | Located CEM motion planning, iCEM, CoVO-MPC, STORM, deterministic samples, C-Uniform, and MTP. Defined the strongest planning-baseline set. |
| Q09 | `action chunks`, `adaptive control frequency`, `action persistence`, `commitment length` | 2021–2026 | Confirmed that fewer decision points and temporal abstraction are crowded. Retained action repeat/chunking only as ablations. |
| Q10 | `skill chaining`, `initiation set`, `termination set`, `subgoal region`, `composable options` | 2009–2026 | Found Skill Chaining, Deep Skill Chaining, Deep Skill Graphs, composable options, and adversarial skill chaining. Reduced CRRP's novelty score. |
| Q11 | `goal-conditioned graph search`, `replay-buffer graph`, `imagined subgoals`, `test-time graph search` | 2019–2026 | Found SoRB, imagined subgoals, subgoal trees, and recent test-time graph search. Established point-landmark and graph-planning baselines for CRRP. |
| Q12 | `set-valued subgoal`, `goal region`, `adaptive subgoal radius`, `coarse-to-fine subgoal`, `learned subset relation`, `quasimetric map`, `spectral bottleneck subgoal` | 2020–2026 | Found the 2026 coarse-to-fine preprint plus ICML 2026 learned subset relations, adaptive quasimetric mapping, and spectral bottleneck subgoals, and AAAI 2026 subset-valued goal languages [R12–R16]. CRRP survives only with the unchanged-final-goal, fixed-horizon predecessor-volume inverted-U claim. |
| Q13 | `offline RL reduced dataset`, `dataset selection`, `dataset pruning`, `coreset` | 2021–2026 | Found ReDOR and data-efficiency work. Eliminated “less data is better” as a novel headline. |
| Q14 | `offline RL bridge transitions`, `graph connectivity`, `articulation state`, `betweenness`, `trajectory stitching` | 2022–2026 | Found GAS, DiffStitch, SSD, graph-search imitation, and active data acquisition. Preserved a narrow gap for bridge-preserving *subset* selection without synthetic transitions. |
| Q15 | `offline RL trajectory quality coverage`, `state aggregation`, `trajectory data` | 2020–2026 | Found D4RL, dataset-perspective analyses, and theory on trajectory data. Motivated strict coverage and marginal-distribution controls for BriCoRe. |
| Q16 | `OGBench`, `offline goal-conditioned RL benchmark`, `AntMaze`, `Maze2D` | 2020–2026 | Verified recognized benchmark families and public repositories for both backups. |
| Q17 | `gradual domain adaptation`, `intermediate domains`, `optimal adaptation path`, `gradient flow` | 2020–2026 | Found a mature theory and algorithm literature; eliminated relay-domain adaptation. |
| Q18 | `bridge passage`, `contextual passage utility`, `reasoning path retrieval`, `multi-hop retrieval` | 2019–2026 | Found graph reasoning-path retrieval, contextual utility, and BridgeRAG. Eliminated bridge retrieval as duplicate-prone. |
| Q19 | `successor predecessor exploration`, `backward empowerment`, `predecessor entropy` | 2021–2026 | Found SPIE and forward-backward representations. Eliminated predecessor/successor intrinsic exploration. |
| Q20 | `GNN relay nodes`, `virtual nodes`, `over-squashing`, `rewiring`, `edge subdivision` | 2020–2026 | Found established bottleneck and rewiring literature. Eliminated GNN relays. |
| Q21 | `incremental rank`, `dynamic rank`, `low-rank then full-rank`, `rank growth training` | 2021–2026 | Found InRank and gradual rank-growth analyses. Eliminated temporary low-rank continuation. |
| Q22 | `diffusion restart`, `reheating`, `fixed-NFE schedule`, `noise reinjection` | 2022–2026 | Found a crowded sampler-design area; no clean, low-confound rapid paper advantage. Eliminated. |
| Q23 | `active learning bridge nodes`, `graph connectivity`, `articulation point labels`, `topology-aware active learning` | 2018–2026 | Found mature centrality/topology-aware selection work. Eliminated despite low compute cost. |
| Q24 | `safe Bayesian optimization continuation`, `safe-set expansion`, `intermediate feasible points` | 2015–2026 | Mechanism remained plausible but weaker as an AI narrative and benchmark story; parked rather than shortlisted. |
| Q25 | Exact-title and citation searches for every shortlisted closest work | 2007–2026 | Verified titles, authors, venue/status, official links, and code availability where relevant. |

## Venue-by-venue audit for the primary direction

| Venue or source family | What was inspected | Result for BFAP novelty |
|---|---|---|
| ICLR / OpenReview | Compact latent actions, action representation, offline data reduction, goal-conditioned benchmarks, adaptive subgoals, gradual adaptation | TAP is a close representation-space neighbor; no located ICLR paper combined success-preimage mass, utility retention, and same-budget basis selection. |
| ICML / PMLR | Goal-conditioned planning, imagined subgoals, offline-RL data/stitching, parameterized actions, learned goal subsets, adaptive quasimetrics, spectral bottleneck subgoals, and trajectory/data theory | Strong overlap around latent actions and offline graphs, but no exact primary duplicate. The 2026 set-abstraction papers [R13–R15] materially weaken CRRP. |
| NeurIPS proceedings | Action tokenization, offline RL baselines, skill curricula, predecessor/successor exploration, gradual rank growth | BEAST and related action compression make fixed B-spline/action-token novelty untenable. No direct adaptive basin-mass planner was found. |
| AAAI / IJCAI | Offline trajectory stitching, active offline data acquisition, composable options, and first-order subset-valued goals | Relevant mainly to backups; R16 narrows CRRP, while no direct BFAP match was located. |
| ACL / EMNLP / IJCNLP-AACL | Multi-hop retrieval, bridge passages, passage utility | No direct control/planning duplicate. The search eliminated retrieval as a cleaner vehicle because its bridge mechanism is already explicit. |
| CVPR / ICCV / ECCV | Visuomotor representations, action tokenization, video and imitation-learning action models | Adjacent learned-action representations exist, but the pilot deliberately avoids pixels and large imitation datasets. No exact BFAP match located. |
| CoRL | iCEM, STORM, GP action priors, learned sampling distributions, skill and manipulation work | Closest empirical community. Establishes demanding structured-sampler baselines. |
| RSS | PushT/diffusion-policy benchmark, motion planning, graph-search imitation | Strong benchmark and robotics context, but no exact success-mass basis selector found. |
| ICRA / RA-L / TRO | Spline-reduced whole-body control, Reference-Free MPC, C-Uniform, generalizable sampling distributions, low-frequency MPPI | The densest direct prior-art region. It eliminates “splines help” as novelty and defines the critical audit boundary. |
| L4DC / control journals | CoVO-MPC, Grad+CEM, adaptive parameterized MPC, move blocking | Shows that covariance, gradient refinement, and adaptive parameter count are established. BFAP must win through the explicit utility-constrained hit-mass mechanism. |
| TMLR | Model Tensor Planning | MTP is the strongest structured global/local trajectory-sampling neighbor and must be included in the main comparison if its code can be integrated fairly. |
| IJRR / foundational robotics | CEM motion planning, LQR-trees, funnels | Establishes that capture regions and robust funnels are old in state space; BFAP's novelty must remain in finite-budget proposal-space geometry. |

## Backward and forward tracing notes

- Structured-action planning papers repeatedly trace backward to CEM/MPPI, smooth action priors, low-discrepancy sampling, and control blocking. This is why BFAP does not claim a new trajectory basis.
- Recent action-tokenization and B-spline-policy papers trace forward from action chunking and interpolation toward imitation learning. They do not by themselves test the finite-budget expressivity–hit-mass inversion.
- Funnel and skill-chain papers establish compositional state-space predecessor sets. They are conceptually close to the seed but functionally different from selecting an action-sequence decoder for a black-box planner.
- Offline stitching papers separate disconnected support from nominal transition quality. ReDOR and GAS make any generic data-reduction or graph-stitching claim insufficient for BriCoRe.
- The newest relevant 2026 records were treated cautiously: an arXiv timestamp or OpenReview record was not upgraded to a peer-reviewed publication unless an official acceptance/proceedings record was found.

## Reproducibility of the search

A researcher reproducing the search should:

1. rerun Q01–Q16 with date filters covering the six months preceding submission;
2. search the exact proposed title terms `basin-first action parameterization`, `success-preimage mass MPC`, `utility-constrained action basis selection`, and close synonyms;
3. inspect citing papers for [P01]–[P05], [P10], [P14], [P16]–[P22], [D01]–[D04], and [R01]–[R07];
4. scan the newest ICLR, ICML, NeurIPS, CoRL, RSS, ICRA, RA-L, TRO, TMLR, and L4DC records;
5. compare functional inputs, outputs, objective, selector information, rollout accounting, and empirical claim rather than relying on keyword distance.

## Known limitations

- Search-engine and indexing delays can hide very recent, withdrawn, anonymous, or newly accepted work.
- OpenReview status can change after retrieval; every recent OpenReview entry must be rechecked at submission time.
- Some control papers use terminology such as move blocking, control parameterization, or basis-function optimization rather than “action representation,” so the search cannot guarantee exhaustive coverage.
- A negative search result is not evidence that no duplicate exists. The novelty verdict is therefore conditional and is paired with an empirical kill gate rather than treated as settled fact.
- Compute estimates are engineering estimates based on state-based JAX/MuJoCo-style workloads and must be updated after the first profiler run. They are not literature-derived performance guarantees.

## Final audit record

The search supports a **pilot-level GO**, not a full-project commitment. The primary direction remains defensible only at the intersection of four elements that the located literature does not jointly supply:

1. a normalized robust near-optimal success-preimage statistic in action-representation coordinates;
2. an explicit high-budget utility-retention constraint that blocks trivial task attenuation;
3. same-rollout-budget online selection among nested temporal action representations;
4. cross-task evidence that the statistic predicts a non-monotonic expressivity–success phase diagram.

Failure to establish any one of these elements converts BFAP into prior-art-adjacent structured sampling and triggers the kill criteria in Section 15.
