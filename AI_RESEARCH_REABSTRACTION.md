# Executive Verdict

**Retrieval date:** 2026-08-25 (Asia/Tokyo)  
**Available compute:** exactly eight independent NVIDIA RTX 4090 GPUs with 24 GB VRAM each; no NVLink, no pooled memory, and no assumed cloud compute.  
**Binding source:** `AI_research_reabstraction_prompt.md` (265 lines; SHA-256 `86fc640608a329c33e1752a1abe1495f2bd12cae8267badc47cb38d58ffa71af`).  
**Audited failed formalization:** `AI_RESEARCH_IDEA_LANDSCAPE(1).md` (1,988 lines; SHA-256 `a26c6aeea8b48283201cd1d5f2e65ca769177b1dc7b1250639e1cf7925929019`).

## Final decision

> **NO-GO: RE-ABSTRACTION NOT YET ACHIEVED**

The original intuition survives as a legitimate scientific question, but none of the 20 mechanism-diverse candidates generated in this investigation passes all required gates simultaneously. The strongest candidate is not BFAP. It is a solution-preserving **semantic relay compilation** idea: add definitional proof-interface variables or logically entailed factors to a neural SAT/CSP representation so that a fixed-compute neural solver can propagate useful consequences through shorter semantic routes without changing the projected solution set. This is a genuine relay in form. It nevertheless fails the current primary-direction standard because its broad qualitative prediction is already substantially predictable from three converging literatures:

1. **Neural SAT augmentation:** G4SATBench reports that training on CNFs augmented with CDCL learned clauses can make both satisfiability and satisfying-assignment prediction markedly easier for GNN solvers [P03].
2. **SAT-preserving resolution augmentation:** *Augment with Care* compares equal-size random and resolution-based additions and finds a large advantage for the semantics-preserving resolution transformations [P04].
3. **Extended resolution:** 2026 work on extended-resolution clause learning dynamically introduces definitional variables to improve proof search on difficult formula families [P06].

The remaining micro-gap—whether **unique-extension semantic interfaces beat topology-matched vacuous rewiring, ordinary implied clauses, extra message-passing depth, and preprocessing-matched symbolic controls under exactly equal end-to-end cost**—is scientifically crisp, but it is not yet a paper direction. It is one bounded falsification question. A positive answer would require a second novelty audit before any full program is authorized.

## Decisions on the failed report's three recommendations

| Previous direction | Functional classification after re-audit | Decision | Reason |
|---|---|---|---|
| **BFAP** | Restriction mechanism | **Eliminate as a primary direction; retain only as infrastructure/restriction controls** | It removes temporal action degrees of freedom, imposes smoother or lower-frequency images, and then selects the best restriction. Its finite-budget advantage is the standard approximation-versus-search trade-off already surrounding move blocking, control knots, compact latent actions, colored/low-pass proposals, and covariance design [A01–A08]. |
| **BriCoRe** | Mostly restriction disguised as relay | **Eliminate as a paper direction** | It deletes data under a subset budget. Bridge preservation is an informative selection criterion, but the intervention is still pruning/coreset design; gains can be explained by data regularization, support preservation, or better subset quality. |
| **CRRP** | Genuine relay family | **Eliminate for novelty, retain as conceptual precedent** | Set-valued subgoals, initiation regions, predecessor sets, skill chains, replay-graph search, and goal-region abstractions already instantiate the core function. A new radius/region-width sweep would be a familiar tuning curve. |

## What this investigation established

**Verified conclusion 1 — BFAP was misclassified.** The failed report's own mechanism says a decoder “removes nuisance directions,” enlarging normalized hit mass while accepting approximation error. That is precisely the binding definition of restriction. Calling the retained utility “capability preservation” improves experimental hygiene but does not turn deletion of choices into route creation.

**Verified conclusion 2 — the most faithful new abstraction is computationally extended formulation, not action compression.** A real relay should add an interface or auxiliary state while preserving the meaningful endpoint and its attainable solution set. Definitional variables, semantic equivalence classes, symmetry-orbit moves, lifted Markov states, and proof interfaces satisfy that form much better than temporal action bases.

**Verified conclusion 3 — nearly every clean relay abstraction is a mature algorithmic archetype.** The search repeatedly mapped candidates to established families: extended formulations and clause learning; level-set/symmetry teleportation; nonreversible lifted MCMC; annealed and sequential Monte Carlo; transposition tables and semantic DAG search; lemma generation; execution decomposition; homotopy; graph rewiring; and skill chaining [P03–P09, G01–G08, D01–D08, M01–M05].

**Inference — the unresolved issue is a conservation problem.** When an intermediate structure creates a shortcut, it usually pays for the shortcut by one of five mechanisms: it performs extra computation, exposes derived information, expands representational capacity, restricts the search space, or relaxes the endpoint. A publishable re-abstraction must isolate route creation after charging all five.

## Gate table

| Gate | BFAP | Semantic relay compilation | Gauge-orbit teleportation | Semantic quotient DAG search |
|---|---:|---:|---:|---:|
| Re-abstraction | **Fail** | Pass | Pass | Pass |
| Functional novelty | Fail | **Unresolved / below threshold** | **Fail: direct duplicate** | **Fail: crowded/direct recent overlap** |
| Invariance | Fail | Conditional pass | Strong pass | Weak/conditional |
| Surprise | Fail | **Below threshold** | Fail | Fail |
| Mechanism discrimination | Conditional | Strong | Strong | Conditional |
| 1–3 day falsifiability | Pass | Pass | Pass | Conditional |
| Recognized benchmarks | Pass | Pass | Pass | Pass |
| 8×4090 feasibility | Pass | Pass | Pass | Conditional |
| Breadth | Moderate | High | High | High |
| Clean story | Familiar trade-off | Potentially clean | Already occupied | Already occupied |
| **Primary authorization** | **No** | **No; one bounded probe only** | **No** | **No** |

## Evidence language used below

- **[V] Verified fact:** checked against a primary proceedings, journal, OpenReview, ACL Anthology, arXiv, or official repository record available by the retrieval date.
- **[J] Literature-supported judgment:** synthesis supported by several verified sources.
- **[I] Inference:** a reasoned conclusion that is not itself an established result.
- **[H] Hypothesis:** an untested prediction.
- **[D] Decision:** a binding project-management judgment under the supplied gates and constraints.

# Forensic Audit of the BFAP Formalization

## 1. What BFAP actually changes

The failed report defines a full action sequence $U\in\mathcal U^H$ and a decoder

$$
D_k:\mathbb R^{mk}\rightarrow \mathcal U^H,
$$

where $k<H$ denotes fewer temporal knots or basis coefficients. It then studies

$$
\mathcal Z_{k,\tau}(x)=D_k^{-1}(\mathcal S_\tau(x)),
$$

and an operational hit probability under a proposal distribution. The proposed mechanism is that a restricted decoder removes oscillatory or otherwise unhelpful directions, so a larger fraction of samples land near useful trajectories. The same report gives the box-model factor

$$
\rho_{\mathrm{full}}
\approx
\prod_{i=1}^{r}\frac{\delta_i}{R_i}
\prod_{j=1}^{n}\frac{\eta_j}{R_j},
$$

then argues that deleting $n$ nuisance directions multiplies hit mass by $\prod_j R_j/\eta_j$.

This is mathematically coherent. It is also unambiguously a restriction mechanism. The decoder's image is a subset of the full action-sequence space:

$$
\operatorname{Im}(D_k)\subseteq \mathcal U^H.
$$

The improvement comes from eliminating directions. The high-budget capability floor attempts to show that the removed directions were not important on the evaluated tasks. That does not alter the functional classification: it is a well-controlled restriction, not an added route.

## 2. Why the finite-budget inversion is predictable

BFAP emphasizes that

$$
J_H^*(x)\ge J_k^*(x)
$$

while a restricted representation can have higher finite-budget success. This is not a paradox to a researcher familiar with black-box optimization, MPC, or statistical learning. A larger decision space can contain a better optimum yet be harder to search under a finite sample budget. The literature already treats temporal correlation, smooth priors, action knots, compact latent actions, low-frequency sampling, covariance shaping, and move blocking as ways to make action-sequence search easier [A01–A08].

The default expert prediction after seeing the fair setup is therefore already:

> A coarse representation underfits; a full representation is expensive to explore; an intermediate representation can win at finite budget, and the winning resolution moves upward with more samples.

That is exactly the qualitative curve BFAP proposes. A new normalized hit-mass statistic may explain the curve, and an adaptive selector may exploit it, but neither changes the underlying mechanism. The binding prompt explicitly rejects a primary contribution whose headline is “an intermediate amount of a hyperparameter is optimal” or “fewer dimensions act as regularization.”

## 3. The capability-retention gate is necessary but not novel

The failed report's capability ratio

$$
\kappa_k=
\frac{J_{k,\mathrm{high}}^*-J_{\mathrm{random}}}
{J_{H,\mathrm{high}}^*-J_{\mathrm{random}}}
$$

is good hygiene. It blocks an especially weak result in which a coarse controller succeeds only because the task no longer demands rapid or high-amplitude behavior. However, a threshold such as $\kappa_k\ge0.95$ merely says that the restriction was mild on the chosen benchmark distribution. It does not prove equality of attainable output sets, equality of best attainable utility, or route creation.

At most it supports the claim:

> A particular restricted family approximates the useful part of the full family well enough for these tasks.

That is useful engineering and perhaps a solid control result in the right setting. It does not meet the requested relay standard.

## 4. The robust-preimage statistic is parameterization-dependent

The failed report correctly notes that raw Euclidean volume is not comparable across dimensions and therefore defines proposal-normalized mass. This operationalizes discoverability, but it also makes the object depend on:

- decoder scaling and coordinate chart;
- proposal family and covariance;
- perturbation distribution and normalization;
- threshold construction;
- warm start and optimizer iteration;
- basis family and knot placement.

A covariance-optimized full-space method can change the same mass without changing the decoder image [A03]. A learned proposal can concentrate probability on useful full-space trajectories [A04]. Colored or low-pass proposals can suppress high-frequency nuisance directions while leaving per-step action coordinates present [A01, A02, A05]. Consequently, a BFAP win can be reinterpreted as a particular proposal-design choice rather than evidence of a new geometric object.

## 5. The adaptive method is representation selection

BFAP-lite spends a probe budget across bases, estimates utility and robust mass, rejects low-capability bases, and allocates remaining samples to the selected basis. Functionally, it is a bandit or successive-halving selector over existing control representations. The binding prompt explicitly states that a learned or online selector over familiar representations is not enough to rescue a predictable mechanism.

The strongest practical baseline would be a portfolio planner that allocates the same samples directly across multiple full-space proposal kernels, including low-pass, colored, spline-induced, and covariance-adapted proposals. If such a portfolio matches BFAP, the “basis” interpretation disappears. If it does not, the result may still be a useful representation-selection paper, but not the requested relay contribution.

## 6. Current literature collision

| Work | Verified function | Collision with BFAP |
|---|---|---|
| iCEM [A01] | Temporally correlated action sampling, elite reuse, and population decay for sample-efficient real-time planning. | Already shows that changing temporal proposal structure can greatly reduce finite-budget sample demand. |
| Inferring Smooth Control [A02] | Gaussian-process action priors for smooth Monte Carlo control. | Directly changes temporal trajectory geometry and removes rough proposals. |
| CoVO-MPC [A03] | Optimizes sampling covariance and analyzes convergence. | Shows that proposal geometry, not decoder dimension alone, controls finite-budget success. |
| TAP [A04] | Plans in a compact learned latent action space. | Direct compact-action representation precedent. |
| Low-pass MPPI [A05] | Filters temporal perturbations to suppress high-frequency components. | Very close functional explanation for why full white-noise action search can fail. |
| Move Blocking [A06] | Holds input moves fixed over blocks to reduce online decision variables. | Classical direct precedent for temporal dimension reduction. |
| Dynamic Move Blocking [A07] | Changes block structure online. | Weakens any novelty claim based on adapting temporal resolution. |
| Model Tensor Planning [A08] | Uses structured global trajectory samples and local exploitation. | Strong modern neighbor for structured, interpolated finite-budget planning. |

No single source needs to implement the exact robust-mass statistic for the qualitative claim to be familiar. Functional novelty is evaluated on the problem, mechanism, and predicted outcome, not on whether an identical symbol or selector appears.

## 7. Binding decision on BFAP

**[D] ELIMINATE BFAP AS A PRIMARY DIRECTION. RETAIN ONLY AS INFRASTRUCTURE/BASELINES.**

Retained components:

- full versus ZOH/linear/spline/DCT action representations as restriction controls;
- colored-noise and low-pass proposals as strong non-dimensional controls;
- exact rollout accounting and capability-retention measurements as fairness tools;
- proposal-normalized hit mass as a diagnostic, not a contribution claim.

Not authorized:

- a BFAP paper centered on an intermediate-dimensional optimum;
- an adaptive basis selector as the main novelty;
- a “less control, more success” headline;
- a large benchmark study intended to elevate the same trade-off.

## 8. What would have been required for a rescue

A rescue would require an experiment in which the relay system has the **same exact action-sequence image** as the direct system, the same action dimension, the same proposal family after marginalization, and the same model calls, yet intermediate interfaces create new finite-budget routes. Ordinary basis restriction cannot satisfy this. A possible example would be an auxiliary-state optimizer whose marginal action distribution has identical support and capacity but whose nonreversible lifted dynamics reach successful modes faster. That abstraction immediately maps to mature lifted-MCMC and auxiliary-variable methods, which is one reason BFAP cannot be rescued simply by changing vocabulary [M01, M02].

# The Preserved Core: Restriction versus Relay

## 1. Static preimages are insufficient

Let a direct system be a map $F:\mathcal U\rightarrow\mathcal Y$ and let $S\subseteq\mathcal Y$ be the meaningful success set. Its successful upstream set is

$$
\mathcal P_F(S)=F^{-1}(S).
$$

A relay composition is

$$
F_R=G_L\circ G_{L-1}\circ\cdots\circ G_1.
$$

Merely observing

$$
\mu\big(F_R^{-1}(S)\big)>\mu\big(F^{-1}(S)\big)
$$

is not enough. The composition could enlarge the preimage by collapsing many upstream choices, weakening $S$, using extra information, adding computation, or increasing capacity. Static maps conceal these payments.

The scientifically relevant object is therefore an **algorithmic reachability set under an invariance ledger**. For algorithm $A$, budget $B$, instance $x$, random seed/perturbation $\omega$, and unchanged success criterion $S(x)$, define

$$
\mathcal R_A(x,B)=
\{\omega:A(x;B,\omega)\in S(x)\}.
$$

A relay effect exists only when

$$
\Pr_\omega[\omega\in\mathcal R_{A_R}(x,B)]
>
\Pr_\omega[\omega\in\mathcal R_{A_D}(x,B)]
$$

while the final task, attainable solutions, information, capacity, and end-to-end resources are credibly matched.

## 2. Relay conservation ledger

A useful decomposition for an observed gain is

$$
\Delta_{\mathrm{obs}}
=
\Delta_{\mathrm{route}}
+
\Delta_{\mathrm{restriction}}
+
\Delta_{\mathrm{information}}
+
\Delta_{\mathrm{compute}}
+
\Delta_{\mathrm{capacity}}
+
\Delta_{\mathrm{endpoint}}
+
\varepsilon.
$$

The requested contribution requires evidence that $\Delta_{\mathrm{route}}>0$ after driving the other named terms to zero or measuring and controlling them tightly. This is the **relay conservation test**.

| Term | Typical disguised source of gain | Required control |
|---|---|---|
| $\Delta_{\mathrm{restriction}}$ | Lower rank, fewer decisions, action smoothing, data pruning, constrained decoding | Exact solution-set/image equality or a high-budget capability and support-matching test |
| $\Delta_{\mathrm{information}}$ | Generated lemmas, verifier labels, execution traces, hidden states, privileged models | Give the direct method the same derivable information or charge its derivation |
| $\Delta_{\mathrm{compute}}$ | More expansions, compiler calls, solver preprocessing, model samples, refinement rounds | End-to-end FLOPs/calls/wall-clock and preprocessing-matched comparisons |
| $\Delta_{\mathrm{capacity}}$ | Extra latent variables, parameters, agents, memory tokens, branches | Parameter, activation-memory, and effective-state-capacity controls |
| $\Delta_{\mathrm{endpoint}}$ | Wider goal, approximate equivalence, more permissive verifier | Exact success criterion and projected solution equality |
| $\Delta_{\mathrm{route}}$ | Reusable semantic interface, nonreversible lift, exact state quotient, compositional predecessor transport | Mechanism-specific control that preserves structure but destroys relay semantics |

## 3. A strong relay archetype

The strongest formal archetype found is an **exact extended representation**. Let the original instance be $x$ with solution set $\mathcal S(x)$. A relay compiler introduces auxiliary variables $y$ and constraints or transitions $D_x$:

$$
R(x)=(x,D_x),
$$

with projection $\pi$ satisfying

$$
\pi\big(\mathcal S(R(x))\big)=\mathcal S(x).
$$

The strict form has unique extensions:

$$
\forall s\in\mathcal S(x),\qquad
\left|\{z\in\mathcal S(R(x)): \pi(z)=s\}\right|=1.
$$

Unique extension blocks a cheap explanation based on multiplying the number of acceptable auxiliary assignments. The relay is meaningful only if producing $D_x$ does not solve the task or expose a label, and if compiler cost is charged.

This archetype captures extended resolution, auxiliary-variable factor graphs, lifted Markov chains, and exact semantic state quotients. It is much closer to the billiard intuition than BFAP: the intermediate object is added, not obtained by deleting upstream choices.

## 4. The relay tax

The search reveals a recurring difficulty:

> To shorten a computational route, an intermediate representation often has to encode a consequence that the direct algorithm would otherwise need to derive.

That consequence is not new Shannon information if it is a deterministic function of the input, but it is **computed information**. Its derivation has a cost. If a compiler generates a powerful clause, lemma, subgoal, canonical state, or transport map, the compiler may have performed the hard part of the task. A fair relay paper must therefore distinguish:

- **representation-only relay:** cheap, local, label-free transformation;
- **precomputation relay:** expensive derivation moved outside the reported solver;
- **oracle relay:** privileged consequence, proof, or equivalence relation;
- **restriction relay:** representation that deletes difficult branches;
- **true route relay:** intermediate interface provides reusable local composition at lower total cost.

## 5. Preserved research question

The re-abstracted research question is:

> **Does there exist a cheap, information-neutral, solution-set-preserving intermediate representation that increases fixed-budget algorithmic reachability for an AI solver, and whose gain cannot be reproduced by generic shortcut topology, extra computation, extra capacity, or search-space restriction?**

This is a valid question. The current search does not identify a candidate that both answers it nontrivially and clears the novelty/surprise bar.

# Search Strategy, Synonym Map, and Coverage

## 1. Retrieval protocol

The search was iterative and adversarial. Candidate generation and duplicate hunting were interleaved rather than selecting a subfield first. The retrieval cutoff is **2026-08-25 JST**. The search emphasized 2023–2026, then traced foundational mechanisms backward.

Primary/official sources were preferred:

- OpenReview and official ICLR pages;
- PMLR for ICML, AISTATS, CoRL, L4DC, and related venues;
- NeurIPS proceedings;
- ACL Anthology;
- AAAI/IJCAI proceedings;
- journal pages and DOI records;
- arXiv for recent preprints and 2026 records not yet in proceedings;
- official repositories for reproducibility checks.

Functional duplication was judged by input, output, invariants, algorithm, source of improvement, theoretical claim, and decisive experiment—not by title similarity.

## 2. Mechanism synonym map

| Seed component | Search terms | Mature neighboring families located |
|---|---|---|
| Enlarged upstream success set | success preimage, attraction basin, capture basin, initiation set, predecessor set, backward reachable set | funnels, skill chaining, reachability, goal-conditioned graph search |
| Added intermediate structure | auxiliary variables, extension variables, bridge variables, latent interfaces, factor splitting, proof interfaces | extended resolution, factor graphs, variable splitting, data augmentation |
| Route transport | relay states, compositional search, transposition, state quotient, semantic merging | DAG search, dynamic programming, graph-of-thought methods |
| Same target through stages | continuation, homotopy, annealing, bridge distributions, tempering | curriculum/continuation, SMC, AIS, diffusion bridges |
| Same function through new coordinates | gauge symmetry, function-preserving transformation, level-set move, teleportation | neural teleportation, symmetry optimization, invariant LoRA optimization |
| Added dynamical state | lifted Markov chain, momentum variable, nonreversible sampler, auxiliary-variable MCMC | HMC, involutive MCMC, nonreversible/lifted sampling |
| Error-correcting relay | redundant representation, syndrome, checksum, internal error correction | coding-inspired networks, fault-tolerant neural computation |
| Logical relay | implied constraints, resolvents, lemmas, proof compression, extended formulations | CDCL clause learning, extended resolution, neural theorem proving |
| Semantic interface | canonical execution state, program residual, partial execution, state abstraction | execution-guided decoding, program decomposition, synthesis-debug loops |
| Data bridge | graph articulation transition, trajectory stitching, connectivity-preserving subset | offline-RL data selection, graph-assisted stitching, synthetic stitching |
| Representation bridge | model stitching, adapter alignment, latent transport, intermediate checkpoint | model merging, re-basin, representation alignment |

## 3. Subfields explicitly inspected

Planning and MPC; model-based RL; goal-conditioned and hierarchical RL; offline RL; neural combinatorial optimization; SAT/CSP solving; automated theorem proving; program synthesis; code generation; LLM test-time search; neural optimization; parameter-efficient fine-tuning; GNN expressivity and rewiring; probabilistic sampling; diffusion/flow sampling; representation learning; model stitching/merging; domain adaptation; error-correcting computation; and quality-diversity/evolutionary search.

## 4. Adversarial search procedure per serious candidate

For each candidate that reached the provisional shortlist:

1. State the function without the billiard metaphor.
2. Search direct terminology and at least three neighboring terminologies.
3. Find foundational work and current 2023–2026 records.
4. Compare exact invariants and budget accounting.
5. Identify the closest qualitative conclusion, not merely the closest method name.
6. Ask whether an informed expert could predict the proposed sign of the result.
7. Search for a topology/compute/capacity-equivalent control already used in adjacent work.
8. Classify residual uncertainty explicitly.

## 5. Coverage limits

- Search indexing can lag very recent anonymous or newly accepted work.
- OpenReview status can change; recent submissions are labeled as submissions/preprints unless an acceptance record was verified.
- Classical literature in SAT, constraint programming, MCMC, and optimization is too large for a claim of exhaustive coverage.
- “No exact duplicate located” is not proof of novelty.
- Some 2026 works may have only arXiv records by the retrieval date.
- The investigation intentionally favors false-negative project decisions over launching a familiar paper under a new metaphor.

# Literature Landscape

## 1. Restriction and proposal shaping are already mature

Sampling-based planning is explicitly sensitive to temporal proposal structure. iCEM uses temporally correlated samples and reuse mechanisms [A01]. Gaussian-process priors induce smooth control trajectories [A02]. CoVO-MPC changes covariance to improve sampling convergence [A03]. TAP plans in a compact latent action space [A04]. Low-pass MPPI suppresses high-frequency action components [A05]. Classical and dynamic move blocking reduce or adapt the number of independent control moves [A06, A07]. MTP mixes structured global trajectories with local optimization [A08].

**[J] Consequence:** a lower-dimensional or smoother action representation that wins at finite budget is not a relay anomaly. It is an established restriction/proposal-design effect.

## 2. Exact auxiliary structure is a real relay—but an old one

In SAT and constraint solving, adding implied clauses, extension variables, auxiliary factors, or redundant constraints can preserve the original solution set while changing proof or propagation complexity. Extended resolution is a foundational proof-system example [P09]. Modern extended-resolution clause learning dynamically introduces definitional variables [P06]. Classical constraint programming has long used auxiliary variables and implied constraints to reshape propagation.

**[J] Consequence:** “add intermediate variables without changing projected solutions” is the right abstraction, but not a new mechanism by itself.

## 3. Neural SAT already shows semantic augmentation effects

NeuroSAT established GNN-based satisfiability prediction from weak supervision [P01], and QuerySAT extended neural message passing toward assignment production [P02]. G4SATBench then systematically benchmarked multiple graph representations and GNN solvers [P03]. Its clause-learning augmentation study is a direct collision: learned clauses change formula structure while preserving satisfiability and make neural prediction substantially easier. *Augment with Care* provides an even cleaner semantic-versus-random comparison for SAT-preserving transformations [P04].

The 2026 ICLR paper on GNN expressivity for SAT sharpens the theoretical context: message-passing/WL-bounded models face fundamental distinguishability limits [P05]. NeuRes learns resolution-style proofs [P07]. Recent SAT augmentation and hybrid solver work further crowds the space [P10, P11].

**[J] Consequence:** a paper cannot claim novelty for “logical shortcuts help GNN SAT solvers.” The only residual question is whether a specific exact interface produces an effect not explained by known clause augmentation, graph rewiring, or precomputed proof work.

## 4. Generic graph shortcuts are a strong alternative explanation

GNN rewiring research shows that effective resistance, bottlenecks, and over-squashing affect information propagation [P08]. An auxiliary clause or variable changes graph topology, degree, effective resistance, path length, and feature multiplicity even when it preserves logical solutions. Therefore a semantic relay experiment needs a topology-matched but logically vacuous control; otherwise the mechanism can be “better communication graph,” not logical composition.

## 5. Function-preserving optimization moves are already teleportation

Neural Teleportation moves parameters through function-preserving reparameterizations [G01]. Symmetry Teleportation explicitly travels along a loss level set to improve subsequent optimization [G02]. Later work studies convergence/generalization under parameter symmetries, level-set teleportation, null-space gradient projections, and invariant low-rank adaptation [G03–G06]. 2026 work on Balanced LoRA and optimizer basis dependence makes the gauge story even more explicit [G07, G08].

**[J] Consequence:** gauge-orbit moves are perhaps the purest mathematical relay found—same function, same loss, new route—but the mechanism is directly occupied.

## 6. Semantic state merging is now explicit in LLM search

Tree of Thoughts and Graph of Thoughts expanded language-model reasoning beyond a single chain [D01, D02]. RAP and LATS integrate world-model or tree-search structure [D03, D04]. Recent methods directly target redundant semantic states: FETCH merges semantically similar tree nodes [D05]; Latent Semantic Clustering groups equivalent outputs efficiently [D06]; Atom of Thoughts constructs and contracts DAG-like atomic states [D07]; and GraphPO explicitly merges semantically equivalent reasoning paths into a DAG and reallocates budget under matched token/response budgets [D08].

**[J] Consequence:** semantic quotient search is not an open headline. Its main unresolved issue is the cost and reliability of the equivalence relation, not whether merging duplicate states can save search.

## 7. Other genuine relays map to mature archetypes

- Lifted and nonreversible samplers add auxiliary state while preserving a target marginal [M01, M02].
- Annealing and sequential Monte Carlo use intermediate distributions to reach difficult targets.
- Program decomposition and execute-debug loops create intermediate executable interfaces [M03, M04].
- Recursive theorem proving and lemma generation create proof relays [M05].
- Skill chaining and predecessor-set planning compose reachability regions.
- Gradual domain adaptation transports predictors across intermediate distributions.
- Homotopy and continuation transport optimization trajectories across objectives.
- GNN virtual nodes and rewiring create communication shortcuts.
- Quality-diversity methods preserve stepping stones that direct objective search might discard.

These validate the general seed. They also make a generic “intermediate states help” paper indefensible.

## 8. Current 2026 reformulation trend

Very recent preprints use LLMs or structured intermediate representations to reformulate optimization and constraint models [P12, P13]. These do not exactly duplicate unique-extension semantic relay compilation for neural SAT, but they show that “representation-level reformulation makes solving easier” is an active and obvious research direction, further reducing surprise.

# Eliminated Predictable Directions

| Direction | Functional classification | Strongest attractive claim | Why eliminated |
|---|---|---|---|
| BFAP/action bases | Restriction | Full action space contains better plans yet loses at finite samples. | Predictable approximation–search trade-off; extensive action-parameterization prior art. |
| Bridge-preserving offline-RL subset | Restriction | Keep low-return bridges instead of high-return data. | Fixed-cardinality pruning remains data selection; bridge value is adjacent to stitching and coverage literature. |
| Set-valued predecessor relays | Genuine relay | Wider intermediate regions enlarge exact final reachability. | Skill chaining, goal regions, replay graphs, and predecessor composition already cover the function; width sweep is tuning. |
| Fixed spline/low-pass MPC | Restriction | Smooth temporal structure increases hit probability. | Directly established [A01, A02, A05–A08]. |
| Compact/learned latent actions | Restriction | Smaller learned search coordinates preserve useful actions. | TAP and action-tokenization literature already occupy it [A04]. |
| Semantic relay compilation | Genuine relay | Exact auxiliary interfaces help fixed-depth neural solvers. | Best near-miss, but qualitative result is predictable from clause augmentation, extended resolution, and rewiring [P03–P09]. |
| Gauge-orbit teleportation | Genuine relay | Same function and loss, different parameter representative, better future optimization. | Exact direct literature uses the same mechanism and vocabulary [G01–G08]. |
| Semantic quotient DAG search | Genuine relay | Merge equivalent histories to share suffixes and reallocate fixed search. | Classical graph search plus current LLM methods already do it [D01–D08]. |
| Lifted nonreversible search | Genuine relay | Auxiliary momentum/direction increases target hit rate with same stationary marginal. | Mature MCMC/sampling theory [M01, M02]. |
| Annealed/SMC bridge distributions | Genuine relay | Intermediate distributions prevent rare-target collapse. | Foundational mature family; direct functional duplicate. |
| Meet-in-the-middle program synthesis | Genuine relay | Forward and backward partial programs meet at semantic interfaces. | Classical bidirectional search plus neural program-synthesis decomposition; surprise low. |
| Lemma relays in theorem proving | Genuine relay | Derived intermediate theorems shorten proof reachability. | Foundational proof engineering and current neural lemma/proof generation [M05]. |
| Execution-state canonicalization | Genuine relay | Many textual prefixes collapse to the same machine state. | Execution-guided synthesis, partial execution, and synthesize-execute-debug loops already use the interface [M03, M04]. |
| Error-correcting latent interfaces | Unclear | Redundant internal code maps more perturbations back to the same semantic output. | Usually pays with extra width, tokens, or compute; exact capacity matching removes the redundancy. |
| Temporary expansion/network morphism | Restriction/capacity confound | Train through a larger function-preserving network and collapse at inference. | Extra train-time parameters/FLOPs and extensive overparameterization/network-morphism precedent. |
| Modular latent transport/model stitching | Unclear | Intermediate translator increases compatibility of frozen modules. | Adapter capacity and extra training information dominate; model stitching/alignment is crowded. |
| Homotopy/continuation training | Genuine staging relay | A sequence of easier equivalent or deformed problems reaches the final optimum. | Mature continuation/curriculum family; explicitly forbidden as an easy answer. |
| GNN relay nodes/rewiring | Genuine communication relay | Auxiliary nodes create shorter message paths. | Virtual-node, rewiring, and over-squashing literature already treats it [P08]. |
| Gradual-domain bridges | Genuine relay | Intermediate domains transport a predictor to the same target. | Mature gradual-domain-adaptation theory; intermediate data may add information. |
| Projection relays in constrained generation | Usually restriction | Interleaved projections keep samples on a useful manifold. | Frequently narrows feasible trajectories; plug-and-play/projection methods are crowded. |
| Intermediate-checkpoint model merging | Genuine relay | Bridge models transport neuron alignment between distant endpoints. | Mode connectivity, re-basin, model stitching, and merging literature; extra checkpoints/data confound. |
| Quality-diversity stepping stones | Genuine relay | Preserve intermediate behaviors that objective-only search discards. | Stepping-stone/novelty/QD research is established; endpoint and archive compute are difficult to match. |

# Candidate Generation and Relay Classification

The 20 candidates below are mechanism-distinct. Application renamings were not counted as separate candidates.

| ID | Candidate | Subfield | Classification | One-line discrimination |
|---:|---|---|---|---|
| C01 | BFAP/action-basis planning | MPC/planning | Likely restriction disguised as relay | Remove temporal degrees of freedom; test whether effect survives exact image equality—it cannot. |
| C02 | Bridge-preserving offline-RL subset | Offline RL | Likely restriction disguised as relay | Fixed subset deletion; compare to full data and support/regularization controls. |
| C03 | Set-valued predecessor relays | GCRL/HRL | Genuine relay | Same final goal; intermediate regions compose backward reachable sets. |
| C04 | Semantic relay compilation | Neural SAT/CSP | Genuine relay | Add unique-extension semantic interfaces; exact projected solution set. |
| C05 | Gauge-orbit teleportation | Neural optimization | Genuine relay | Move on exact function/loss orbit before further updates. |
| C06 | Semantic quotient DAG search | LLM inference | Genuine relay | Merge equivalent states, preserve answer set, reuse downstream search. |
| C07 | Lifted nonreversible search | Sampling/optimization | Genuine relay | Add momentum/direction state while preserving target marginal. |
| C08 | SMC/annealed bridge distributions | Generative inference | Genuine relay | Compose intermediate distributions with same final target. |
| C09 | Meet-in-the-middle neural synthesis | Program synthesis | Genuine relay | Match forward/backward partial semantic states. |
| C10 | Lemma-relay theorem proving | Automated reasoning | Genuine relay | Add derived propositions that shorten proof composition. |
| C11 | Execution-state canonicalization | Code generation | Genuine relay | Collapse syntactic histories to future-relevant execution state. |
| C12 | Error-correcting latent interfaces | Representation learning | Unclear | Needs redundancy; capacity/compute equality may remove benefit. |
| C13 | Function-preserving temporary expansion | Neural training | Likely restriction/capacity confound | Extra train-time degrees and FLOPs; collapse later does not erase resource advantage. |
| C14 | Modular latent transport | Model composition | Unclear | Translator may add capacity/information rather than route geometry. |
| C15 | Homotopy/continuation path | Optimization | Genuine relay but forbidden/mature | Intermediate objectives transport iterates to same final objective. |
| C16 | GNN auxiliary relay nodes | Graph learning | Genuine relay | Added graph interfaces shorten message routes. |
| C17 | Gradual-domain relay path | Domain adaptation | Genuine relay | Intermediate distributions transport a model across shift. |
| C18 | Interleaved projection relay | Diffusion/constrained generation | Usually restriction | Projection often removes candidate trajectories; test exact support equality. |
| C19 | Bridge-checkpoint model merging | Model merging | Genuine relay | Intermediate models transport alignment between endpoints. |
| C20 | Quality-diversity stepping stones | Evolutionary search | Genuine relay | Archive preserves routes discarded by direct fitness search. |

## Hard-gate rule

A candidate must score at least 7/10 on both **functional novelty** and **non-obvious prediction** before average score is considered. This prevents high feasibility and benchmark availability from rescuing a familiar idea. No candidate meets that rule after the adversarial audit.

# Candidate Scorecard

Scores are 1–10, where 10 is favorable. “Reviewer safety” means low risk of a fatal novelty or fairness objection. The mean is descriptive only; the hard gates dominate.

| ID | Candidate | Novelty | Surprise | Seed fidelity | Invariance | Mechanism | Cheap falsifier | Benchmarks | 8×4090 | Beyond tuning | Reviewer safety | Breadth | Mean | Hard-gate result |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C01 | BFAP/action basis | 3 | 4 | 6 | 4 | 7 | 9 | 9 | 10 | 3 | 2 | 6 | 5.73 | Fail novelty, surprise, re-abstraction |
| C02 | Bridge-preserving data subset | 4 | 5 | 6 | 5 | 7 | 8 | 9 | 9 | 5 | 4 | 6 | 6.18 | Fail novelty/surprise; restriction |
| C03 | Set-valued predecessor relays | 4 | 5 | 9 | 7 | 8 | 8 | 8 | 9 | 7 | 3 | 8 | 6.91 | Fail novelty/surprise |
| **C04** | **Semantic relay compilation** | **6** | **6** | **9** | **9** | **9** | **9** | **8** | **9** | **9** | **5** | **8** | **7.91** | **Best near-miss; fails novelty/surprise thresholds** |
| C05 | Gauge-orbit teleportation | 2 | 3 | 9 | 10 | 9 | 9 | 8 | 10 | 8 | 1 | 8 | 7.00 | Exact functional collision |
| C06 | Semantic quotient DAG search | 3 | 4 | 8 | 5 | 8 | 7 | 9 | 7 | 7 | 2 | 8 | 6.18 | Recent direct collision; invariance weak |
| C07 | Lifted nonreversible search | 2 | 3 | 8 | 9 | 9 | 8 | 8 | 9 | 8 | 2 | 9 | 6.82 | Mature theory |
| C08 | SMC/annealed bridges | 1 | 2 | 8 | 9 | 9 | 8 | 8 | 9 | 7 | 1 | 9 | 6.45 | Foundational duplicate |
| C09 | Meet-in-the-middle synthesis | 3 | 4 | 9 | 8 | 9 | 8 | 8 | 8 | 8 | 3 | 7 | 6.82 | Mature search archetype |
| C10 | Lemma-relay proving | 2 | 3 | 9 | 7 | 9 | 7 | 8 | 7 | 8 | 2 | 9 | 6.45 | Mature theorem-proving function |
| C11 | Execution-state canonicalization | 3 | 4 | 8 | 6 | 8 | 7 | 8 | 7 | 7 | 3 | 8 | 6.27 | Existing execution-guided synthesis |
| C12 | Error-correcting latent interface | 5 | 6 | 8 | 4 | 7 | 6 | 6 | 7 | 7 | 4 | 8 | 6.18 | Capacity/compute confound unresolved |
| C13 | Temporary function-preserving expansion | 2 | 3 | 7 | 3 | 8 | 8 | 8 | 9 | 4 | 2 | 8 | 5.82 | Extra training capacity/FLOPs |
| C14 | Modular latent transport | 4 | 5 | 8 | 4 | 7 | 7 | 7 | 8 | 6 | 3 | 8 | 6.27 | Adapter/representation confounds |
| C15 | Homotopy/continuation | 2 | 3 | 8 | 8 | 9 | 8 | 9 | 9 | 7 | 2 | 9 | 6.73 | Mature and explicitly forbidden headline |
| C16 | GNN relay nodes/rewiring | 2 | 3 | 8 | 7 | 8 | 9 | 10 | 10 | 6 | 2 | 8 | 6.64 | Crowded direct mechanism |
| C17 | Gradual-domain bridge path | 2 | 3 | 8 | 6 | 8 | 7 | 8 | 7 | 6 | 2 | 8 | 5.91 | Mature adaptation family |
| C18 | Projection relays | 3 | 4 | 6 | 4 | 8 | 8 | 8 | 8 | 5 | 3 | 8 | 5.91 | Often restriction/support narrowing |
| C19 | Bridge-checkpoint merging | 4 | 5 | 8 | 5 | 7 | 7 | 7 | 8 | 7 | 3 | 8 | 6.27 | Mode-connectivity/merging crowd |
| C20 | QD stepping stones | 2 | 4 | 9 | 7 | 9 | 8 | 8 | 8 | 8 | 2 | 9 | 6.73 | Established stepping-stone mechanism |

## Score interpretation

C04 has the highest mean because it is faithful, controllable, cheap, and broad. It still fails. The novelty score of 6 reflects a real residual implementation gap but a crowded functional neighborhood. The surprise score of 6 reflects that the exact semantic-versus-topology result is uncertain, while the broad sign—useful implied structure helps bounded neural propagation—is already predictable. Under the binding prompt, a high mean cannot override those failures.

# Shortlist Deep Dives

## Shortlist 1 — Semantic Relay Compilation for Neural SAT/CSP

### One-sentence research question

Can a cheap, label-free compiler add **unique-extension semantic interface variables** to a SAT/CSP instance so that a fixed-compute neural solver reaches more correct solutions, even though the projected solution set, training data, supervision, model capacity, and end-to-end resource budget are unchanged?

### One-sentence counterintuitive headline

**A larger formula with more variables can be easier for a smaller fixed-compute neural solver—not because the task is relaxed or solved in preprocessing, but because exact intermediate semantic interfaces convert long logical dependencies into reusable local computation.**

### B/P/M/E formulation

- **Default belief B:** If two representations encode exactly the same solutions and the augmented one contains more variables and factors, a fixed-budget GNN should be neutral or worse after end-to-end compute matching; generic graph rewiring or additional message rounds should capture any communication benefit.
- **Counterprediction P:** A small set of unique-extension, semantically aligned interface variables yields higher OOD assignment validity and satisfiability accuracy than original CNFs, topology-matched vacuous extensions, random unique-extension variables, generic rewiring, extra depth, ordinary implied clauses, and CDCL learned clauses at the same total edge-message FLOPs and preprocessing-inclusive time.
- **Mechanism M:** The interfaces compile reusable intermediate propositions. They reduce a **logical propagation depth**—the number of local inference compositions required to transmit a decisive consequence—without changing projected satisfying assignments. The benefit should track logical-depth reduction after controlling for graph distance, degree, effective resistance, and added node count.
- **Discriminating experiment E:** Train identical neural SAT solvers on paired original and transformed formula families. Verify exact projection equality. Match end-to-end compute. Compare semantically meaningful extensions with graph-isomorphic or degree-matched semantically vacuous controls. The relay account survives only if semantic interfaces outperform every structural and computational control and their gain is predicted by logical-depth reduction.

### Direct and relay formalization

Let $F(X)$ be a CNF over original variables $X$ with solution set

$$
\mathcal S(F)=\{x:F(x)=1\}.
$$

A direct solver is

$$
\widehat x_D=A_\theta(F;B),
$$

where $B$ is the end-to-end inference budget, including all message-passing operations and any permitted preprocessing.

A relay compiler constructs auxiliary variables $Y$ and definitional constraints $D_F(X,Y)$:

$$
R(F)(X,Y)=F(X)\land D_F(X,Y).
$$

The minimum endpoint invariant is projected equality:

$$
\{x:\exists y, R(F)(x,y)=1\}=\mathcal S(F).
$$

The preferred strict invariant is unique extension:

$$
\forall x\in\mathcal S(F),\quad
\left|\{y:R(F)(x,y)=1\}\right|=1.
$$

The relay solver is

$$
(\widehat x_R,\widehat y_R)=A_\theta(R(F);B-C_R(F)),
$$

where $C_R(F)$ charges the compiler in the same budget units. Success is evaluated only on the original task:

$$
F(\widehat x_R)=1,
$$

or on the original SAT/UNSAT label. Auxiliary-variable correctness is diagnostic, not a relaxed endpoint.

A simple unique-extension interface is a definitional variable

$$
y\leftrightarrow \phi(X_S),
$$

encoded by standard channeling clauses. Candidate $\phi$ functions include conjunctions/disjunctions of recurring literal motifs, parity summaries on synthetic XOR families, or balanced subexpressions in a known generated circuit. The compiler must be local and label-free; it cannot call a complete solver to discover the target assignment or a final proof.

### Why this is not restriction

No original variable is fixed, deleted, or constrained beyond $F$. No satisfying assignment over $X$ is removed. Under unique extension, no satisfying assignment is multiplied into many acceptable auxiliary completions. The original endpoint and best attainable utility—finding an assignment in $\mathcal S(F)$ or correctly classifying satisfiability—are unchanged.

The method does add representational state. That is allowed for a relay only if capacity and computation are matched. The direct control therefore receives the same graph-size allowance through vacuous or random unique-extension nodes and the same total edge-message operations. Without those controls, “more hidden nodes” is an uncontrolled capacity increase.

### Minimal theoretical contribution that would be needed

A credible paper would need more than the trivial statement that shortcut clauses reduce graph distance.

**Proposition 1 — exact endpoint preservation.** For every compiler rule, prove projected solution equality; for the strict variant, prove unique extension.

**Proposition 2 — local propagation separation.** Construct a family $F_n$ and a cheap compiler $R$ such that a specified semantic consequence requires $\Omega(n)$ rounds of a local sound propagation process on $F_n$ but $O(\log n)$ or $O(1)$ rounds on $R(F_n)$, while topology-matched semantically vacuous extensions do not reduce the logical propagation depth.

A basic implication chain illustrates the idea:

$$
F_n=x_1\land\bigwedge_{i=1}^{n-1}(\neg x_i\lor x_{i+1}).
$$

The consequence $x_n$ is propagated sequentially. A balanced hierarchy of uniquely defined conjunction summaries can expose multiscale interfaces. This toy is not enough for a paper—the result is predictable—but it supplies an implementation sanity check.

**Proposition 3 — compute-aware condition.** Let $T(F,q)$ be the cost to answer query $q$ by a bounded local solver and $C_R(F)$ the compiler cost. A relay is computationally meaningful only when

$$
C_R(F)+T(R(F),q)<T(F,q)
$$

on the target distribution, not merely when the neural inference portion is shorter.

**Desired nontrivial theorem.** Identify a formula family where a fixed-width/depth neural message-passing architecture can exploit the extension but a graph-topology-only augmentation with the same unlabeled structure cannot. This is the hardest missing piece and one reason the direction is not authorized.

### Relationship to the billiard seed

Each auxiliary proposition is an intermediate contact/interface. A downstream logical requirement that is difficult to reach through a long chain acquires a larger upstream set of useful local messages because many partial assignments can be summarized into the same future-relevant proposition. Unlike BFAP, no original choice is deleted. Unlike ordinary subgoals, the interface is definitionally exact and does not relax the terminal condition.

The analogy breaks if the compiler computes a hard proof or target assignment. Then the “relay” is an oracle that already performed the difficult collision sequence.

### Closest-work audit

| Closest work | What it establishes | Functional collision | Residual difference that would have to carry novelty |
|---|---|---|---|
| NeuroSAT [P01] | GNN message passing can learn SAT classification and exhibit assignment-like behavior from weak supervision. | Establishes neural SAT substrate and local iterative computation. | Does not study exact semantic extensions or semantic-vs-topological controls. |
| QuerySAT [P02] | Goal-aware neural message passing targets satisfying assignments. | Direct benchmark/model for assignment reachability. | Representation is fixed; no relay compiler. |
| G4SATBench [P03] | Benchmarks neural SAT and shows clause-learning augmentation can greatly improve SAT and assignment prediction. | The broad claim “logically derived extra structure helps neural SAT” is directly observed. | Uses CDCL learned clauses; does not isolate unique-extension interfaces, exact end-to-end compute, or semantic-vs-topology causality. |
| Augment with Care [P04] | Uses satisfiability-preserving transformations; equal-size resolution additions strongly outperform random additions in representation learning. | Direct semantic-versus-random evidence for resolution structure. | Training augmentation/contrastive objective rather than persistent unique-extension inference representation; topology not fully matched. |
| GNN Expressive Power for SAT [P05] | Shows fundamental WL/GNN distinguishability limits for SAT and evaluates practical solvers. | Supplies the bounded-local-computation motivation. | Diagnoses limits rather than exact semantic relay compilation. |
| Extended Resolution Clause Learning via DIPs [P06] | Dynamically introduces definitional variables and improves classical SAT proof search. | Direct auxiliary-variable relay in the same logical domain. | Classical CDCL proof search rather than neural fixed-compute inference; no semantic-vs-topology neural test. |
| NeuRes [P07] | Learns resolution proof construction. | Neural solver explicitly manipulates proof steps/clauses. | Learns proof search rather than compiling exact fixed interfaces before a generic neural solver. |
| Effective-resistance rewiring [P08] | Graph rewiring can reduce information bottlenecks/over-squashing. | Strong alternative explanation for any augmented-factor-graph gain. | Ignores logical semantics; becomes the decisive control. |
| Extended Resolution Simulates DRAT [P09] | Formal connection between extended resolution and strong proof systems. | Establishes that extension variables can drastically change proof complexity. | Proof-system theory, not neural computation or matched empirical causal isolation. |
| MAS-SAT [P10] | Combines ML-assisted and standalone SAT solving, including learned-clause interactions. | Current hybrid-solving crowd around neural guidance and clause structure. | Different system objective; status must be treated as submission/preprint. |
| Target-Aware Data Augmentation for SAT Prediction [P11] | 2026 preprint on target-aware SAT augmentation. | Further reduces novelty for SAT-specific augmentation. | Not necessarily unique-extension semantic interfaces or matched topology. |
| LLM-guided constraint reformulation [P12] | Searches constraint-model reformulations to improve solver efficiency. | Same high-level statement: equivalent representation can make solving easier. | Uses LLM/evolutionary reformulation and classical solvers; not the narrow neural propagation mechanism. |
| IR2Solve [P13] | Uses structured intermediate representations for optimization autoformulation. | Crowds the “intermediate representation improves solving” narrative. | Different optimization domain and model pipeline. |

### Three strongest likely rejection reasons

1. **“G4SATBench and Augment with Care already showed this.”** This is the leading objection and currently valid for the broad claim. Only a strict semantic-versus-topology, unique-extension, end-to-end-compute separation could reopen novelty.
2. **“The compiler did the reasoning.”** If relay variables are chosen using CDCL traces, proof labels, target assignments, or expensive search, the gain is precomputation, not route geometry.
3. **“This is graph rewiring or extra hidden state.”** More factor nodes change receptive fields and capacity. If topology-matched vacuous extensions, generic rewiring, or extra depth match the gain, the semantic relay mechanism fails.

### Hypothetical 1–3 day falsification pilot

This is the **only pilot authorized later in Section 13**.

**Stage 0 — exact transformation sanity.** Generate small implication, XOR/parity, and repeated-subexpression CNFs. For each formula and every assignment when feasible, verify projected solution equality and unique extension. For larger formulas, use paired SAT checks with PySAT/CaDiCaL.

**Stage 1 — model/representation sanity.** Use one official G4SATBench-compatible model, preferably NeuroSAT or QuerySAT. Confirm original-representation performance and runtime on one synthetic family and one G4SATBench family.

**Stage 2 — mechanism matrix.** Compare:

1. original CNF;
2. semantic unique-extension relay;
3. topology-matched tautological/vacuous extension;
4. random unique-extension definitions;
5. effective-resistance or degree-matched generic rewiring;
6. original graph with extra message-passing rounds/width at matched edge-message FLOPs;
7. bounded-resolution implied clauses at matched factor budget;
8. CDCL learned clauses at matched factor budget.

**Primary outcome:** exact satisfying-assignment success on held-out larger formulas.  
**Co-primary mechanism outcome:** gain explained by reduction in logical propagation depth after controlling for graph diameter, effective resistance, degree, node count, and end-to-end time.

### Recommended benchmarks, metrics, and baselines

**Synthetic families:** implication chains; balanced Boolean circuits compiled to CNF; planted XOR/parity/Tseitin instances; repeated-motif k-SAT; small graph-coloring or scheduling CSPs only after the SAT pilot.

**Recognized benchmark:** G4SATBench train/easy/medium/hard formula families and official splits [P03, B01]. A later full study could include SAT Competition distributions, but the one-shot pilot should not incur solver-format complexity prematurely.

**Models:** NeuroSAT [P01], QuerySAT [P02], one modern G4SATBench architecture; NeuRes only if proof prediction becomes necessary [P07].

**Metrics:**

- SAT/UNSAT classification accuracy and calibration;
- valid satisfying-assignment rate;
- variable-level accuracy conditioned on SAT;
- OOD scaling by variable/clause count;
- message rounds to threshold performance;
- edge-message FLOPs;
- preprocessing CPU time;
- end-to-end wall-clock and peak memory;
- graph diameter, effective resistance, degree distribution, spectral gap;
- logical propagation depth or bounded-resolution depth proxy;
- robustness across random seeds and compiler tie-breaking.

### Pilot compute estimate

| Resource | Estimate |
|---|---:|
| Initial staged run count | 48–80 runs: 6–8 conditions × 1–2 models × 3–5 seeds |
| Per-run VRAM | 4–12 GB, depending on graph batching and hidden width |
| Aggregate GPU-hours | 60–140 |
| Eight-GPU compute wall time | 8–20 hours after installation; 1–3 calendar days including correctness checks |
| CPU requirement | 16–32 cores for CNF generation, SAT verification, and graph statistics |
| Host RAM | 64 GB workable; 128 GB preferred for concurrent graph preprocessing |
| Storage | 20–100 GB for generated formulas, transformed pairs, checkpoints, and message logs |

### Fairness controls and essential ablations

- Charge compiler CPU/GPU time and memory.
- Match total edge-message operations, not only number of GNN layers.
- Use identical train/validation/test original instances across representations.
- Keep labels and supervision identical; no proof traces in the proposed compiler.
- Verify projected solution equality for every generated instance.
- Match added node/edge count and degree distribution for vacuous controls.
- Include original graph with extra depth, width, and global attention at the same end-to-end budget.
- Include random and proof-agnostic unique-extension variables.
- Include ordinary implied clauses and CDCL learned clauses.
- Train representation-specific models and a mixed-representation model; do not claim test-time plug-in robustness without testing it.
- Report compiler failure/timeout rates and exclude no formula silently.
- Hold hyperparameter-search budget equal.

### Binding kill criteria

Stop immediately if any of the following occurs:

1. topology-matched vacuous extensions or generic rewiring are within 2 percentage points of semantic relays on the primary outcome;
2. extra message-passing compute on the original graph matches the relay under equal end-to-end cost;
3. CDCL learned clauses or bounded-resolution clauses match the proposed interfaces;
4. compiler preprocessing exceeds 15% of end-to-end time at the target scale or requires solver traces/labels;
5. projected solution equality or unique extension fails on any non-bug instance;
6. gains occur only on implication-chain toys and not on two independent G4SATBench families;
7. graph metrics explain the gain as well as or better than logical propagation depth;
8. a fresh literature audit finds a method with the same exact semantic/topology-controlled experiment.

### Reclassification trigger

This direction can be reclassified from **NO-GO near-miss** to **conditional paper-level GO** only if all of the following are observed:

- semantic relays beat every topology/compute/ordinary-clause control by at least 5 absolute success points and at least 0.3 pooled standard deviations on two formula families;
- the effect grows or remains stable under OOD size scaling;
- logical propagation depth predicts the gain beyond graph metrics;
- compiler cost is small and label-free;
- a post-pilot novelty audit still finds no functional duplicate.

A positive pilot alone is not sufficient.

### Evidence required by ambition tier

| Tier | Minimum evidence |
|---|---|
| Workshop/short paper | Exact toy separation; one G4SATBench family; topology-matched control; open paired-formula generator. |
| Solid main conference | Three formula families; two architectures; OOD scaling; full end-to-end compute matching; CDCL/resolution/rewiring controls; formal endpoint proof. |
| Potential standout | A nontrivial expressivity or proof-depth separation; semantic-vs-topology phase diagram; transfer across SAT and one additional CSP; compiler that generalizes without proof labels; held-out prediction of when relays help. |

### Current verdict

**[D] NO-GO AS A PAPER DIRECTION; ONE BOUNDED FALSIFICATION PILOT AUTHORIZED.**

The candidate is scientifically better than BFAP but does not currently clear the novelty/surprise gate.

## Shortlist 2 — Gauge-Orbit Teleportation for Stateful Optimizers

### One-sentence research question

Can exact function-preserving parameter transformations move a model to a different representative of the same function where a coordinate-dependent optimizer has a larger downstream basin, under matched parameter count, data, loss, and training FLOPs?

### One-sentence counterintuitive headline

**Two parameter states that compute exactly the same function and have exactly the same loss can train to different final predictors because the optimizer—not the objective—sees the coordinate basis.**

### B/P/M/E formulation

- **Default belief B:** Functionally identical parameterizations are interchangeable; an adaptive optimizer should largely absorb benign scale or basis changes.
- **Counterprediction P:** A function-preserving gauge move, especially an orthogonal rank-space rotation in a factorized update such as LoRA, changes Adam's coordinatewise second-moment geometry and can enlarge the set of subsequent updates that reach a good solution, even when factor norms, singular values, rank, current loss, and current function are identical.
- **Mechanism M:** The loss is gauge-invariant but coordinatewise optimizers are not gauge-equivariant. The relay moves along a level set into a chart with more favorable preconditioner–gradient alignment.
- **Discriminating experiment E:** Start from exactly gauge-equivalent factors, transport first-moment state consistently, control/reset second-moment state explicitly, and compare future optimization under Adam, SGD, Shampoo/Muon, and gauge-invariant LoRA optimizers. The effect should appear only for non-equivariant optimizers and should disappear for equivariant controls.

### Direct and relay formalization

For a factored update $\Delta W=BA$, let $Q\in O(r)$. The transformation

$$
B'=BQ,\qquad A'=Q^\top A
$$

preserves the exact adapted weight:

$$
B'A'=BQQ^\top A=BA.
$$

It also preserves Frobenius norms under orthogonal $Q$. A direct run continues from $(A,B)$; a relay run applies $Q$ and continues from $(A',B')$. With exact optimizer-state transport, a gauge-equivariant optimizer should produce equivalent function-space dynamics. Adam's coordinatewise second moments generally do not transform as a full covariance, so basis choice can matter.

### Why this is not restriction

No function is removed and no endpoint is relaxed. The current model output is exactly identical before and after the relay. Rank, parameter count, data, loss, and inference architecture are unchanged. This is one of the cleanest genuine relay mechanisms in the entire search.

### Minimal theory that would be needed

- Characterize optimizer equivariance under the relevant gauge group.
- Show that orthogonal gauge transformations preserve current function, factor norms, and rank while changing Adam's effective metric.
- Derive a local criterion for choosing $Q$ that improves expected descent or aligns the diagonal second-moment approximation with gradient covariance.
- Prove a null result for gauge-equivariant optimizers.

These are strong ingredients. They are also already central to the existing literature.

### Relationship to the billiard seed

The gauge move is an intermediate contact that changes the route but not the current state in function space. The same function is “handed off” to a different coordinate chart, where the next optimizer step can access a wider set of productive directions. This is a nearly ideal formal match to the seed.

### Closest-work audit

| Closest work | Function | Collision |
|---|---|---|
| Neural Teleportation [G01] | Function-preserving reparameterizations move networks in parameter space and alter subsequent optimization. | Direct broad mechanism duplicate. |
| Symmetry Teleportation [G02] | Travels long distances on a loss level set to accelerate future optimization. | Exact relay interpretation and headline already published. |
| Improving Convergence and Generalization Using Parameter Symmetries [G03] | Develops parameter-symmetry transformations and optimization effects. | Direct continuation of the same program. |
| Level Set Teleportation [G04] | Studies optimization by moving within a level set. | Occupies the general theoretical formulation. |
| Null-Space Gradient Projection Teleportation [G05] | Uses null-space movement to accelerate optimization. | Another exact function/loss-preserving route mechanism. |
| LoRA Done RITE [G06] | Designs invariant transformations/equilibration for LoRA optimization. | Direct low-rank factor gauge collision. |
| Balanced LoRA [G07] | Removes parameter invariance/imbalance to accelerate convergence. | Current 2026 factor-balance neighbor. |
| The Loss Does Not See the Basis, but Adam Does [G08] | Shows gauge-equivalent factorizations can diverge under Adam and develops equivariance theory. | The strongest 2026 collision with the exact counterprediction. |

### Three strongest rejection reasons

1. **“This is symmetry teleportation.”** Correct; the core mechanism and even the word “teleportation” are established.
2. **“The LoRA version is already invariant-optimizer work.”** LoRA Done RITE and related 2026 work directly study factor symmetries and coordinate dependence.
3. **“Any remaining contribution is a new $Q$ selector.”** A heuristic for choosing a gauge is an incremental optimizer method unless it establishes a qualitatively new theorem or large-scale phenomenon.

### Hypothetical 1–3 day pilot

Fine-tune a small transformer or linear/MLP model with rank-$r$ adapters under Adam. At a fixed checkpoint, create 16 random orthogonal gauges with identical $BA$, loss, norms, and predictions. Continue equal-FLOP training. Compare SGD, Adam, Shampoo/Muon, and LoRA Done RITE. Measure variation in convergence and final generalization. Add a deterministic gauge chosen from gradient/second-moment alignment.

This pilot is cheap—roughly 30–80 GPU-hours with 4–16 GB VRAM per run—but it would validate known theory rather than establish a new paper direction.

### Benchmarks, controls, and kill criteria

Use matrix sensing, small vision classification, and a modest language-model adaptation task. Controls must transport optimizer states correctly, compare random gauges, reset moments, and use equivariant optimizers. Kill if the effect appears under SGD after correct state transport, disappears after moment accounting, or reduces to factor balancing. More importantly, kill for novelty because direct prior art already exists regardless of a positive result.

### Evidence tiers

| Tier | What would be required beyond existing work |
|---|---|
| Workshop | New pedagogical benchmark or replication; not a new direction. |
| Solid main conference | A genuinely new symmetry group or optimizer theorem with consequential large-scale results. |
| Standout | A general gauge-covariant optimization framework that subsumes current methods and changes practical foundation-model training. |

### Current verdict

**[D] ELIMINATE. TRUE RELAY, DIRECTLY OCCUPIED.**

## Shortlist 3 — Semantic Quotient DAG Search for LLM Reasoning

### One-sentence research question

Can a fixed-budget language-model search merge distinct histories that induce the same future-relevant semantic state, thereby sharing suffix search and enlarging answer reachability without restricting the set of attainable final answers?

### One-sentence counterintuitive headline

**More diverse reasoning does not require more branches: collapsing semantically equivalent histories into one state can create more distinct future routes at the same token budget.**

### B/P/M/E formulation

- **Default belief B:** Merging paths risks deleting useful distinctions; tree search is safer because every history is retained.
- **Counterprediction P:** An exact or high-precision semantic quotient converts a redundant search tree into a DAG, freeing expansions for genuinely distinct states and improving answer success at fixed model-token and verifier-call budgets.
- **Mechanism M:** Multiple histories map to the same sufficient state for future transitions. Sharing downstream expansions increases unique-state coverage without reducing answer support.
- **Discriminating experiment E:** On an environment with exact state equivalence, compare tree search, history merging, random merging, embedding-based approximate merging, and direct graph search at equal expansions. Then test LLM reasoning with strict equivalence-oracle cost accounting.

### Direct and relay formalization

A tree state is a history $h_t=(a_1,\ldots,a_t)$. Let $\sigma(h_t)$ be a sufficient future-relevant state. Histories are equivalent when

$$
h\sim h'\quad\Longleftrightarrow\quad \sigma(h)=\sigma(h').
$$

Direct tree search stores each history separately. Quotient search operates on equivalence classes $[h]$ and shares outgoing expansions. If $\sigma$ is exact, every path to a final answer remains represented. The budget gain comes from avoiding duplicate suffix computation.

### Why this is not restriction in the exact case

Exact state merging does not remove any future action available from a history because equivalent histories have the same transition and reward structure. It removes duplicate *representations* of the same state, not distinct solutions. Approximate semantic merging, however, can be a restriction: false merges delete distinctions. That is the central invariance weakness in LLM applications.

### Minimal theory that would be needed

- Bound success probability improvement as a function of transposition rate under fixed expansions.
- Bound failure from false-positive merges and wasted budget from false-negative merges.
- Include equivalence-computation cost.
- Show a task family where quotienting yields exponential state savings while preserving reachability.

All of this closely resembles classical dynamic programming, graph search, bisimulation, and transposition-table analysis.

### Relationship to the billiard seed

Equivalent histories are multiple incoming balls striking the same relay state. Once they arrive, a downstream route can be reused. The upstream success set expands because more budget remains to explore distinct predecessors and successors. This is a faithful relay abstraction when equivalence is exact.

### Closest-work audit

| Closest work | Function | Collision |
|---|---|---|
| Tree of Thoughts [D01] | Searches over intermediate language states rather than one chain. | Establishes test-time branching/search substrate. |
| Graph of Thoughts [D02] | Represents reasoning as a graph with aggregation and transformation operations. | Direct graph rather than tree formulation. |
| RAP [D03] | Uses a language model as a world model in planning/search. | State/action planning over reasoning trajectories. |
| Language Agent Tree Search [D04] | Integrates tree search, environment feedback, and value estimation for agents. | Direct fixed-budget search neighbor. |
| FETCH / Don't Get Lost in the Trees [D05] | Merges semantically similar states to avoid over-exploration. | Direct semantic-state merging function. |
| Latent Semantic Clustering [D06] | Clusters semantically equivalent outputs using internal states to reduce redundant test-time compute. | Direct redundancy/semantic quotient mechanism. |
| Atom of Thoughts [D07] | Builds and contracts dependency DAGs into atomic Markov-like states. | Direct state contraction/DAG interface. |
| GraphPO [D08] | Merges semantically equivalent reasoning paths into DAG nodes and reallocates budget under matched token/response budgets. | Strongest 2026 direct collision with the exact proposed function. |

### Three strongest rejection reasons

1. **“GraphPO/FETCH already do semantic merging.”** This is a direct current collision, not a distant analogy.
2. **“The equivalence model is extra compute and privileged semantics.”** Embedding or LLM-based merging consumes tokens/FLOPs and can inject a stronger model.
3. **“False merges are restriction.”** In natural-language reasoning, exact Markov equivalence is rarely observable; approximate clustering may simply prune branches.

### Hypothetical 1–3 day pilot

Use exact-state environments first: small deterministic planning, program execution states, or theorem prover states. Compare tree search and transposition-aware DAG search at equal node expansions. Then add a small open model on GSM8K/MATH with embedding-based merging, charging embeddings and verifier calls. Measure unique semantic states, false-merge rate on executable/verifiable tasks, and success.

The exact-state result would mostly replicate classical graph-search benefits. The LLM result would collide with FETCH, LSC, AoT, and GraphPO. Estimated compute is 100–400 GPU-hours depending on model size; VRAM 16–24 GB per run for 7B-class models, making the one-shot pilot less attractive than C04.

### Benchmarks, controls, and kill criteria

Controls: random merges; lexical merges; exact execution-state merges; no-merge tree; graph search with transposition table; equal token, response, verifier, and embedding budgets; collision/false-merge audit. Kill if gains vanish after charging equivalence computation, exact-state transposition tables match, or approximate merging lowers answer support. Novelty is already killed by direct literature.

### Evidence tiers

| Tier | What would be required beyond existing work |
|---|---|
| Workshop | New benchmark for merge precision/recall; not a new main mechanism. |
| Solid main conference | A rigorous sufficient-state learner with strong false-merge guarantees and broad agent results. |
| Standout | A general semantic-bisimulation theory and scalable exact/verified quotient for open-ended reasoning. |

### Current verdict

**[D] ELIMINATE. TRUE RELAY IN EXACT ENVIRONMENTS; DIRECTLY CROWDED IN LLM REASONING.**

# Invariance Ledgers

## 1. Ledger template

Every direct-versus-relay comparison must report the following before results are interpreted:

| Invariant | Direct | Relay | Equality test | Failure consequence |
|---|---|---|---|---|
| Final objective |  |  | exact code/hash | Endpoint relaxation |
| Exact success criterion |  |  | paired evaluator | Different task |
| Attainable solution/output set |  |  | proof/enumeration/projection audit | Restriction or expansion |
| Best attainable utility |  |  | high-budget/oracle reference | Capability change |
| Data/supervision |  |  | file hashes and label audit | Extra information |
| Model/parameter capacity |  |  | parameter and activation counts | Extra capacity |
| Training compute |  |  | FLOPs/updates/wall-clock | Unequal learning budget |
| Test-time compute |  |  | calls/tokens/edge-messages/wall-clock | Unequal search budget |
| Model/environment calls |  |  | central counter | Hidden evaluations |
| Horizon/action/reasoning length |  |  | trace audit | Longer task budget |
| Information available |  |  | interface contract | Privileged state/oracle |
| Wall-clock/memory |  |  | profiler | Practical resource shift |
| Hyperparameter search |  |  | trial ledger | Tuning advantage |
| Stopping rule |  |  | preregistered | Selective termination |

## 2. Semantic relay compilation ledger

| Invariant | Direct condition | Relay condition | Binding test |
|---|---|---|---|
| Final objective | Solve/classify original $F(X)$ | Solve/classify original $F(X)$ after projection | Same evaluator on $X$ only |
| Success criterion | $F(\hat x)=1$ or correct SAT label | Same | Byte-identical evaluator |
| Solution set | $\mathcal S(F)$ | $\pi_X\mathcal S(R(F))$ | SAT equivalence checks; exhaustive small cases |
| Multiplicity | One original assignment | Prefer exactly one extension | Uniqueness solver checks |
| Data | Same original formula IDs/splits | Paired transformed versions | Manifest hashes |
| Labels/supervision | SAT labels/assignments only | Identical; no proof labels | Training-batch audit |
| Model parameters | Fixed architecture/parameter count | Same | Parameter count and checkpoint schema |
| Activation capacity | Original graph | Larger graph | Match with vacuous/random added nodes; report peak activations |
| Training compute | Fixed edge-message FLOPs and updates | Same | Hardware counters/analytical FLOP ledger |
| Test compute | Budget $B$ | $B-C_R(F)$ | Compiler-inclusive budget |
| Preprocessing | Parse original CNF | Compile interfaces | CPU time charged; complete-solver calls forbidden |
| Graph size/topology | Original | Augmented | Topology-matched controls |
| Information | Original clauses | Deterministic local definitions | Compiler code audit; no target/proof access |
| Hyperparameter tuning | Equal trials | Equal trials | Shared search manifest |
| Wall-clock/memory | Reported | Reported and matched where possible | Profiler, not just theoretical FLOPs |

**Most fragile invariant:** activation/state capacity. Adding variables gives the GNN more memory locations. The vacuous-extension control is therefore indispensable.

## 3. Gauge-orbit teleportation ledger

| Invariant | Direct | Relay | Binding test |
|---|---|---|---|
| Function | $f_{A,B}$ | $f_{Q^\top A,BQ}$ | Bitwise/float-tolerance prediction equality |
| Loss | $L$ | Same $L$ | Exact batch loss equality |
| Rank/parameters | Rank $r$ | Rank $r$ | Matrix ranks and counts |
| Factor norms | Baseline | Orthogonal gauge preserves norms | Frobenius/spectral checks |
| Data/supervision | Same batches/order | Same | Seeded dataloader |
| Training FLOPs | Fixed | Transformation cost charged | FLOP ledger |
| Optimizer state | Native | Explicitly transformed/reset by preregistered rule | State checksum and ablations |
| Inference model | Folded $BA$ | Identical folded $BA$ before continuation | Weight-product equality |
| Hyperparameter budget | Equal | Equal | Trial manifest |

This ledger can be extremely clean. Novelty, not invariance, kills the candidate.

## 4. Semantic quotient DAG ledger

| Invariant | Direct tree | Relay DAG | Binding test |
|---|---|---|---|
| Final answer set | All reachable leaves | Same if equivalence exact | Exhaustive exact-state audit |
| Model tokens | Budget $T$ | Includes summaries/merging | Token counter |
| Verifier calls | Budget $V$ | Same | Central call counter |
| Embedding/equivalence compute | None or baseline | Charged | FLOPs/wall-clock |
| State information | Full histories | Summarized/clustered states | Same source text; no stronger model |
| Search expansions | Fixed | Fixed after merge cost | Expansion ledger |
| False merges | None | Possible | Executable/verifiable ground truth |
| False splits | Tree duplicates | Possible | State-equivalence audit |
| Horizon | Same maximum reasoning depth | Same | Trace checker |
| Model capacity | Same generator/verifier | Same | Checkpoint hashes |

**Most fragile invariant:** attainable answer set. Approximate merging can delete valid futures; then it is a pruning/restriction method.

## 5. Reclassification rules

A candidate is reclassified from genuine relay to restriction if any of the following is true:

- projected solution/output equality fails;
- approximate merging or projection deletes reachable valid outputs;
- the method's gain depends on a lower-dimensional image or smaller candidate set;
- auxiliary multiplicity inflates the count of acceptable states without improving original-task success;
- the relay requires a privileged proof, target, state, or stronger model;
- preprocessing performs comparable work to directly solving the instance;
- matched topology/capacity controls reproduce the effect.

# Adversarial Novelty Audit

## 1. Audit standard

A candidate fails novelty when a prior method performs the same functional operation under a different name, even if the new proposal adds a metric, selector, fairness control, or application. A candidate fails surprise when the sign of the main result is already a straightforward consequence of established theory or empirical evidence.

## 2. BFAP collision test

BFAP's functional operation is “restrict or smooth temporal controls to increase finite-budget search efficiency, then adapt the restriction.” Move blocking, smooth priors, compact latent actions, low-pass sampling, covariance shaping, and structured trajectory proposals collectively cover every component [A01–A08]. The robust-mass diagnostic is new packaging around a familiar bias–search curve. **Result: novelty fail; surprise fail; re-abstraction fail.**

## 3. Semantic relay compilation collision test

### Broad claim

“Adding semantically derived, solution-preserving structure can improve neural SAT solving.”

This broad claim is already supported by G4SATBench clause-learning augmentation and *Augment with Care* [P03, P04]. Extended-resolution clause learning supplies the exact auxiliary-variable proof mechanism [P06]. **Broad claim: duplicate/predictable.**

### Narrow residual claim

“Unique-extension semantic interfaces outperform topology-matched vacuous extensions, generic rewiring, extra message-passing compute, ordinary resolvents, and CDCL learned clauses under compiler-inclusive resource equality; gain tracks logical propagation depth rather than graph metrics.”

No exact duplicate was located in the searched corpus. However:

- it is a conjunction of stricter controls and a particular representation family rather than a wholly new function;
- proof complexity predicts that useful extension variables can shorten derivations [P06, P09];
- GNN locality predicts that exposing intermediate consequences can help [P05, P08];
- existing empirical work already demonstrates semantic augmentation advantages [P03, P04].

**Result: exact novelty unresolved, but surprise below threshold.** A paper cannot be authorized merely because no one appears to have run this exact ablation table.

## 4. Gauge-orbit collision test

The proposed function—move to a function/loss-equivalent parameter representative to improve subsequent optimization—is the explicit subject of Neural Teleportation, Symmetry Teleportation, Level-Set Teleportation, parameter-symmetry optimization, and LoRA invariance work [G01–G08]. The 2026 basis/Adam paper states the exact phenomenon that the loss is basis-invariant while Adam is not [G08]. **Result: direct functional duplicate.**

## 5. Semantic quotient collision test

The proposed function—merge semantically equivalent reasoning states into a DAG to avoid redundant expansions—is directly present in FETCH and GraphPO; latent semantic clustering and Atom of Thoughts occupy adjacent forms [D05–D08]. **Result: direct recent duplicate.**

## 6. Cross-domain collision pattern

| Abstract relay operation | Mature name(s) |
|---|---|
| Add exact auxiliary variables | extended formulation, extended resolution, variable splitting |
| Move on equal-objective manifold | symmetry/level-set teleportation |
| Add momentum/direction state | lifted or nonreversible Markov chain |
| Pass through intermediate distributions | annealing, tempering, SMC, continuation |
| Merge equivalent histories | dynamic programming, transposition tables, bisimulation, semantic clustering |
| Add reusable proof states | lemmas, clause learning, theorem invention |
| Canonicalize intermediate execution | partial execution, execution-guided synthesis |
| Compose predecessor sets | skill chaining, funnels, subgoal regions |
| Preserve stepping stones | novelty search, quality diversity |

The seed is broad because it rediscovers a general algorithmic pattern. Breadth alone is not novelty.

## 7. Venue scan outcome

| Venue family | Mechanisms inspected | Outcome |
|---|---|---|
| ICLR/OpenReview | neural SAT expressivity, compact actions, parameter symmetries, goal abstractions | Direct neighbors in every leading candidate. |
| ICML/PMLR | SAT augmentation, graph rewiring, planning, LLM/agent search, program synthesis | Strong functional collisions and standard benchmarks. |
| NeurIPS | symmetry teleportation, test-time reasoning, theorem proving, neural optimization | Gauge and reasoning candidates crowded. |
| ACL/EMNLP | semantic clustering, efficient tree search, graph reasoning | Direct semantic-merging collision. |
| AAAI/IJCAI | graph-of-thoughts, constraint modeling, options, SAT/CSP | Additional functional duplication. |
| TMLR/journals | G4SATBench, control/planning methods | Strong SAT augmentation and action-parameterization evidence. |
| SAT/CP journals and conferences | extended resolution, redundant constraints, solver reformulation | Semantic-relay archetype is foundational. |

## 8. Backward and forward tracing

Backward tracing from C04 reaches extended formulations, resolution, auxiliary-variable encodings, and propagation-enhancing redundant constraints. Forward tracing reaches G4SATBench, SAT-preserving representation learning, 2026 extended-resolution solvers, target-aware SAT augmentation, and LLM-based model reformulation [P03–P13].

Backward tracing from C05 reaches parameter symmetries and function-preserving reparameterizations; forward tracing reaches teleportation, LoRA invariance, and optimizer basis-dependence [G01–G08].

Backward tracing from C06 reaches graph search, dynamic programming, transposition tables, and bisimulation; forward tracing reaches graph-of-thoughts, semantic clustering, state merging, AoT, and GraphPO [D01–D08].

## 9. Novelty conclusion

No candidate reaches the required combination:

$$
\text{functional novelty}\ge 7
\quad\land\quad
\text{surprise}\ge 7
\quad\land\quad
\text{invariance pass}.
$$

C04 is the only candidate worth one bounded existence test. The purpose of that test is not to “validate the paper.” It is to determine whether the residual semantic-versus-topology separation exists strongly enough to justify re-opening the novelty question.

# Primary Recommendation or NO-GO

## Binding decision

> **NO-GO: RE-ABSTRACTION NOT YET ACHIEVED**

No full experimental program is authorized. No primary title, method acronym, benchmark sweep, or paper narrative should be treated as selected.

## Why a NO-GO is the correct scientific output

1. **The old primary is disqualified at the mechanism level.** BFAP is restriction by construction.
2. **The cleanest genuine relay is directly occupied.** Gauge-orbit teleportation has exact prior art.
3. **The most fashionable relay is directly occupied.** Semantic quotient/DAG reasoning has explicit 2025–2026 methods.
4. **The best residual mechanism is predictable.** Semantic proof interfaces are adjacent to neural clause augmentation, graph rewiring, and extended resolution.
5. **A selector or metric cannot rescue the mechanism.** The binding prompt correctly forbids this move.
6. **Forcing a GO would optimize prose around a micro-gap rather than discover a new scientific object.**

## The unresolved theoretical question that must be answered first

Let $x$ be an instance, $\mathcal S(x)$ its exact solution set, $A$ a fixed-capacity algorithm, and $R$ a deterministic relay compiler. Find a nontrivial family satisfying all of the following:

1. **Endpoint equality**

$$
\pi\mathcal S(R(x))=\mathcal S(x).
$$

2. **No multiplicity trick**

$$
\forall s\in\mathcal S(x),\quad |\pi^{-1}(s)\cap\mathcal S(R(x))|=1
$$

or an equivalent correction for multiplicity.

3. **No privileged information**

$R$ uses only local, label-free computations available from $x$.

4. **End-to-end budget equality**

$$
C_R(x)+C_A(R(x))\le C_A(x),
$$

under a meaningful compute model and matched wall-clock/memory regime.

5. **Capacity equality**

The direct control receives matched representational state or an equivalent memory budget.

6. **Semantic-specific advantage**

The gain survives a topology-isomorphic or topology-matched transformation $R_0$ that preserves graph communication but destroys the proposed semantic interface.

7. **Non-predictable qualitative result**

The sign or scaling law is not already implied by known proof complexity, graph locality, or established augmentation evidence.

The unresolved part is item 7. Items 1–6 can be engineered. The current literature makes the likely sign of C04 unsurprising. A meaningful breakthrough would need an effect that contradicts a stronger default belief—for example, a semantic relay that helps even when it **does not shorten graph paths or classical propagation depth**, or one that yields a provable fixed-compute separation unavailable to conventional extended resolution. No such candidate has been identified.

## Authorized action

Only the mechanism-discriminating C04 pilot in the next section is authorized. It is capped, preregistered, and designed to terminate the idea. No method development beyond one implementation correction is allowed unless every pass condition is met.

# Minimal Mechanism-Discriminating Pilot

## 1. Status and objective

This is a **bounded existence test**, not the first phase of an assumed paper. Its sole objective is to determine whether semantic relay compilation has a large, semantic-specific effect after every obvious explanation is controlled. The pilot ends with **PASS-TO-REAUDIT** or **STOP**. It does not end with “the method works.”

The authorized question is:

> At exactly matched original solution sets, representational-state budgets, edge-message FLOPs, compiler-inclusive time, data, labels, and tuning budget, do unique-extension semantic interfaces improve neural SAT solving more than topology-only communication shortcuts and ordinary proof-derived clauses?

## 2. Preregistered hypotheses

Let $m=\text{SEM}$ denote semantic unique-extension relays, $m=\text{ORG}$ the original CNF, and $\mathcal C$ the set of all non-semantic controls.

**H1 — existence:**

$$
\Delta_{\mathrm{SEM,ORG}}
=
\mathbb E[Y_{\mathrm{SEM}}-Y_{\mathrm{ORG}}]>0.
$$

**H2 — semantic specificity:**

$$
\min_{c\in\mathcal C}
\mathbb E[Y_{\mathrm{SEM}}-Y_c]>0.
$$

**H3 — route mechanism:** after controlling for end-to-end cost and generic graph statistics, reduction in logical propagation depth predicts per-instance gain:

$$
\Delta Y_i
=\beta_0
+\beta_1\Delta d^{\mathrm{logic}}_i
+\beta_2\Delta d^{\mathrm{graph}}_i
+\beta_3\Delta R^{\mathrm{eff}}_i
+\beta_4\Delta C_i
+\epsilon_i,
$$

with $\beta_1<0$ in a convention where lower depth is better and with stronger out-of-sample predictive value than the graph-only model.

**H4 — OOD route retention:** the semantic-specific contrast does not shrink to zero when formula size exceeds the training range.

## 3. Relay compiler v0

The pilot permits only deterministic, local, label-free compilers. No CDCL trace, satisfying assignment, SAT/UNSAT label, learned selector, or target proof may be used to choose the proposed relay.

### 3.1 Exact interface forms

The initial compiler library contains:

1. **Balanced implication summaries.** For generated implication/circuit families, introduce variables representing balanced subexpressions rather than only adjacent chain links.
2. **Repeated-pair definitions.** For literal pairs or small motifs that recur above a fixed frequency threshold, add $y\leftrightarrow\phi(\ell_a,\ell_b)$, where $\phi$ is chosen by a preregistered deterministic rule.
3. **Parity summaries for planted XOR families.** Add a balanced hierarchy of auxiliary XOR summaries, then compile each definition into CNF. These summaries are generated from the known formula generator, not a target assignment.
4. **Circuit-gate interfaces.** Generate Boolean circuits first, then compare a flattened CNF with a unique-extension Tseitin-style representation that exposes gate outputs. Both representations encode the same original input/output relation.

Each proposed relay must satisfy projected equality and, where claimed, unique extension.

### 3.2 What is forbidden

- mining a final CDCL proof to choose relay variables;
- using learned clauses from a solver as the proposed method;
- selecting relays by validation accuracy;
- per-instance hyperparameter tuning;
- dropping original clauses or fixing original variables;
- changing satisfiability thresholds or assignment validity;
- giving the relay model more hidden width or more total edge-message operations.

## 4. Eight experimental conditions

| Code | Representation | Purpose |
|---|---|---|
| ORG | Original CNF/literal-clause graph | Direct baseline |
| SEM | Proposed unique-extension semantic interfaces | Relay hypothesis |
| RND-DEF | Same number/arity of unique-extension definitions placed on random literal motifs | Controls extra variables and definitional semantics without proof alignment |
| VAC | Fixed auxiliary variables plus tautological/semantically vacuous factors, degree/sign matched as closely as possible | Controls activation memory and communication nodes without useful logical relation |
| REWIRE | Generic communication-only or effective-resistance rewiring with matched added nodes/edges | Controls graph bottlenecks [P08] |
| DEPTH | Original representation with extra message-passing rounds or hidden width chosen to match SEM edge-message FLOPs and memory | Controls raw neural computation |
| RES | Bounded-width resolution clauses with the same added-factor budget | Controls ordinary entailed-clause preprocessing [P04] |
| CDCL | CaDiCaL/G4SATBench learned clauses capped to the same factor/edge and preprocessing budget | Strong prior-art upper baseline [P03] |

If exact degree/sign matching for VAC is infeasible, the pilot must report the mismatch and include RND-DEF plus REWIRE; it may not silently call VAC “topology matched.”

## 5. Formula families

### Family S0 — implication and Boolean-circuit sanity

Purpose: validate exactness and confirm that the neural implementation can exploit an obvious interface.

- implication chains of length 16–512;
- balanced versus flattened AND/OR circuits;
- repeated-subexpression circuits with controlled motif reuse;
- paired SAT/UNSAT variants created by endpoint clauses.

This family cannot support a paper claim. Failure here kills implementation; success here proves only that the code can detect a deliberately exposed route.

### Family S1 — planted XOR/parity/Tseitin

Purpose: stress long-range logical composition and connect to extended-resolution theory.

- satisfiable planted parity systems with known solution witnesses;
- minimally perturbed unsatisfiable counterparts;
- sizes chosen so brute-force checks are possible for the smallest tranche and CaDiCaL checks are cheap for the rest;
- balanced semantic summaries generated from the construction, not the solution.

Unsatisfiable formulas require special caution: an unsatisfiable formula entails every clause, so “implied clause” status alone is meaningless. The proposed interfaces must remain definitional and label-free, and evaluation must separate SAT and UNSAT instances.

### Family S2 — G4SATBench SR

The SR generator is the original NeuroSAT-style random paired-formula family. Use official easy and medium ranges first, then evaluate on the hard/larger range without retuning [P03, B01].

### Family S3 — G4SATBench 3-SAT

Use the official phase-transition 3-SAT generator and easy/medium/hard size ranges [P03]. This is the most direct comparison with the published clause-learning augmentation result.

### Conditional family S4 — one structured combinatorial encoding

Only after S0–S3 complete, add one of $k$-Clique, $k$-Dominating Set, or $k$-Vertex Cover from G4SATBench. This checks whether any effect is tied to random CNF statistics.

## 6. Models

### Pilot model A — NeuroSAT-compatible LCG

Use the official G4SATBench implementation and literal-clause graph representation where possible [P01, P03, B01]. Preserve the official message-passing block and losses before any method-specific changes.

### Conditional model B — QuerySAT or G4SATBench GGNN

If Model A passes the preregistered semantic-specific threshold, replicate with an assignment-oriented architecture [P02] or a second official G4SATBench baseline. Model B is not run merely to rescue a null Model A.

### Classical reference solvers

CaDiCaL verifies formulas and generates the CDCL baseline. A second exact solver through PySAT may be used for cross-checks. Classical solve time is not the neural primary outcome, but relay preprocessing must not make the formulas invalid or accidentally trivial for a classical solver.

## 7. Exactness verification protocol

For every transformed instance:

1. Verify $F\land\neg\exists Y R(F)$ is unsatisfiable in an appropriate miter construction.
2. Verify $R(F)\land\neg F$ is unsatisfiable after aligning original variables.
3. For unique extension, duplicate auxiliary variables $Y,Y'$ and test

$$
F(X)\land D_F(X,Y)\land D_F(X,Y')\land(Y\ne Y')
$$

for unsatisfiability.
4. Exhaustively enumerate all assignments for a random sample of small formulas and compare projected satisfying sets exactly.
5. Record solver version, seed, timeout, proof/certificate availability, and checksum.
6. Treat any unexplained mismatch as a compiler bug; no affected instance enters training or evaluation.

## 8. Compute matching

The unit of neural compute is the number of edge-message transformations times hidden-state width and linear-layer cost. A reproducible approximation is

$$
C_{\mathrm{msg}}
=\sum_{t=1}^{T}
\left(
|E_t|c_{\mathrm{edge}}(d)
+|V_t|c_{\mathrm{node}}(d)
\right).
$$

SEM generally has more vertices and edges, so it receives fewer rounds or narrower hidden states when necessary. DEPTH receives the largest original-graph configuration that fits within $\pm 3\%$ of SEM's analytical FLOPs and $\pm 5\%$ of measured wall-clock after warm-up. Both values are reported; neither substitutes for the other.

Compiler time is added to relay inference time. CDCL generation time is added to CDCL-condition time. Dataset compilation may be cached for training, but the paper must report amortized and per-instance costs separately; test-time or new-instance deployment uses non-amortized cost.

## 9. Training protocol

- Freeze one software environment, CUDA/PyTorch version, and G4SATBench commit.
- Use official optimizer/loss defaults for the first baseline reproduction.
- Select one shared hyperparameter set using ORG validation data; permit at most one representation-specific learning-rate adjustment selected from the same two-point grid for all conditions.
- Use identical formula IDs, batches, and label ordering across paired representations.
- Train three seeds in the first pass; expand to five only after the stage-gate threshold.
- Use early stopping on a preregistered original-task validation metric with identical patience and maximum steps.
- Record failed/diverged seeds; do not replace them without reporting.

## 10. Outcomes

### Primary outcome

For satisfiable formulas, **exact satisfying-assignment rate**:

$$
Y_i=\mathbb 1[F_i(\widehat x_i)=1].
$$

This avoids inflated variable-wise accuracy that does not produce a valid solution.

### Co-primary outcome

Semantic-specific paired contrast:

$$
\Delta_i^{\mathrm{sem}}
=Y_{i,\mathrm{SEM}}
-
\max\{Y_{i,\mathrm{RND\text{-}DEF}},Y_{i,\mathrm{VAC}},Y_{i,\mathrm{REWIRE}},Y_{i,\mathrm{DEPTH}},Y_{i,\mathrm{RES}},Y_{i,\mathrm{CDCL}}\},
$$

reported through model-based marginal contrasts rather than literally taking a noisy per-instance maximum.

### Secondary outcomes

- SAT/UNSAT classification accuracy and AUROC;
- variable-level assignment accuracy;
- iteration-to-validity curves;
- calibration;
- OOD size scaling;
- end-to-end latency and throughput;
- peak GPU/host memory;
- compiler cost and timeout rate;
- logical-depth and graph-statistic correlations;
- classical solver time as a diagnostic.

## 11. Logical propagation diagnostics

No single metric is trusted. Use three views:

1. **Generator-known depth** for S0/S1, such as circuit depth or parity-summary depth.
2. **Bounded unit-propagation depth** under controlled partial assignments.
3. **Bounded-resolution or implication-graph depth proxy** computed offline with a fixed budget. Solver traces may be used only for diagnosis, never for constructing SEM.

Generic graph diagnostics include shortest paths, diameter, average effective resistance, algebraic connectivity, degree moments, and factor-node arity. A semantic mechanism is credible only if logical diagnostics add predictive value beyond these.

## 12. Staged run matrix

### P0 — implementation and exactness

| Component | Conditions | Seeds | Families | Approx. GPU-hours |
|---|---:|---:|---:|---:|
| Baseline reproduction | ORG | 2 | S0, S2 | 4–10 |
| Transformation sanity | ORG, SEM, RND-DEF, VAC | 2 | S0 | 4–8 |
| Exactness/solver checks | all | n/a CPU | S0, small S1 | 0 GPU; 2–8 CPU-hours |

**P0 pass:** SEM solves the designed long-range S0 case better than ORG and all transformations pass exactness. P0 success has no novelty value.

### P1 — core falsification

| Component | Conditions | Seeds | Families | Approx. GPU-hours |
|---|---:|---:|---:|---:|
| Core matrix | 8 | 3 | S1, S2, S3 | 54–108 |
| Profiling | 8 | 1 | all | 4–8 |
| Graph/logical diagnostics | all | n/a CPU | all | 20–80 CPU-hours |

### P2 — conditional replication

Run only if P1 meets every PASS threshold:

| Component | Conditions | Seeds | Families | Approx. GPU-hours |
|---|---:|---:|---:|---:|
| Second architecture | 8 | 3 | best two families + S4 | 40–100 |
| Seed expansion | key 4 conditions | +2 | best two families | 16–40 |

## 13. PASS-TO-REAUDIT criteria

All conditions are mandatory:

1. SEM exceeds ORG by at least **5 absolute percentage points** and **0.3 pooled standard deviations** on exact assignment success in at least two non-toy families.
2. SEM exceeds every topology/capacity/compute control by at least **2 points**, and the preregistered joint contrast is significant at two-sided $p<0.01$ or has a 99% bootstrap interval excluding zero.
3. SEM exceeds RES and CDCL under the matched added-factor/end-to-end budget on at least one family and is not worse on the second.
4. The effect persists or increases on OOD larger instances.
5. Logical-depth reduction improves held-out prediction of per-instance gain beyond graph-only features by a preregistered threshold, such as $\Delta R^2\ge0.05$ or a meaningful held-out log-likelihood gain.
6. Compiler time is no more than 15% of end-to-end relay time at target scale and uses no solver trace or target label.
7. Exactness tests have zero unexplained failures.
8. A fresh post-result novelty search finds no exact semantic/topology/compute-controlled duplicate.

## 14. STOP criteria

Any one is sufficient:

- SEM's gain is below 5 points on both S2 and S3;
- RND-DEF, VAC, REWIRE, or DEPTH matches SEM within 2 points;
- RES or CDCL matches SEM under fair cost;
- semantic benefit disappears under edge-message FLOP matching;
- compiler work is substantial or proof-guided;
- only S0/S1 synthetic families improve;
- exactness or unique-extension checks fail;
- benefit is explained by node count, degree, graph distance, or effective resistance;
- results require per-family or per-instance tuning;
- a direct functional duplicate is found.

## 15. Expected interpretation of each outcome

| Outcome | Interpretation | Decision |
|---|---|---|
| SEM = all controls | No relay effect | STOP |
| SEM > ORG, but REWIRE/DEPTH match | Generic communication/compute | STOP |
| SEM > topology controls, but RES/CDCL match | Known proof augmentation | STOP |
| SEM > all controls only on S0/S1 | Constructed toy effect | STOP or workshop diagnostic only |
| SEM > all controls on G4SATBench, but compiler costly | Precomputation trade | STOP |
| SEM passes every criterion | Potential semantic-specific relay | Re-run novelty audit; no automatic GO |

# Full Experimental Blueprint

## 1. Authorization status

**Not authorized under the present verdict.** This section is a conditional blueprint to prevent ad hoc expansion if the bounded pilot passes. It must not be started merely because the pilot shows a positive ORG comparison. Authorization requires every Section 13 PASS criterion and a fresh novelty audit.

## 2. Conditional research thesis

If reopened, the thesis would be:

> Exact semantic interfaces can change the fixed-compute reasoning class of neural constraint solvers without changing the projected solution set, and their benefit is governed by logical propagation depth rather than generic graph connectivity.

The paper must not claim that auxiliary variables, learned clauses, or graph rewiring are new. Its contribution would have to be the **causal semantic-versus-topology separation**, a compute-aware relay formalism, and a nontrivial theory/prediction that existing work does not provide.

## 3. Evidence chain

1. **Exactness:** prove and mechanically verify projected solution equality and unique extension.
2. **Toy separation:** show controlled logical-depth reduction on generated families.
3. **Causal control:** defeat matched random definitions, vacuous nodes, generic rewiring, extra depth, and ordinary clauses.
4. **OOD generalization:** train small, test larger and structurally shifted.
5. **Architecture transfer:** replicate across at least two neural solver families.
6. **Domain transfer:** reproduce the semantic-specific mechanism in one non-SAT CSP or optimization factor graph.
7. **Predictive mechanism:** predict instance-level gains from pre-run relay diagnostics.
8. **Cost closure:** demonstrate end-to-end advantage including compiler and memory.

## 4. Method family

### 4.1 Relay compiler

A conditional full method could select local Boolean interfaces from a bounded candidate set using a **task-independent structural objective**, not validation success. Possible scoring terms:

$$
q(r)=
\lambda_1\widehat{\Delta d}_{\mathrm{logic}}(r)
-\lambda_2\Delta C(r)
-\lambda_3\Delta M(r)
-\lambda_4\mathrm{Redundancy}(r).
$$

However, a selector is not itself sufficient novelty. The score must emerge from a theorem or strongly validated mechanism. A learned selector is forbidden until a fixed rule demonstrates the phenomenon.

### 4.2 Relay budget

Let $b$ be a maximum number of added interfaces or added edges. Main comparisons use fixed $b$ values chosen before test evaluation. A budget curve is an ablation, not the headline. The method should work at a sparse budget, ideally 1–10% added factors, to avoid the interpretation that it simply materializes a large proof closure.

### 4.3 Architecture interface

The same literal-clause or variable-clause GNN processes all CNF conditions. Auxiliary-variable type and clause type may be encoded only if matching controls receive the same type vocabulary. A separate bespoke relay network would create a capacity confound.

## 5. Environment and instance families

### Core SAT families

- G4SATBench SR and 3-SAT for direct comparison with published augmentation results [P03].
- G4SATBench CA/PS to test pseudo-industrial structure.
- G4SATBench $k$-Clique or $k$-Vertex Cover for combinatorial encoding shift.
- Planted parity/Tseitin and circuit families for mechanism control.
- Frozen SAT Competition subset for external validity, selected before final tuning.

### Conditional cross-domain family

Choose exactly one:

- graph coloring CSP with exact auxiliary color-conflict summaries;
- small scheduling CSP with exact cumulative-resource interface variables;
- binary ILP/factor-graph instances with unique-extension partial-sum variables.

The cross-domain transformation must preserve projected feasible solutions and be generated locally. Adding a second domain only after SAT causality is established prevents an expensive breadth-first fishing expedition.

## 6. Model families

| Family | Role | Why included |
|---|---|---|
| NeuroSAT/LCG [P01, P03] | Primary iterative GNN | Closest to published augmentation evidence |
| QuerySAT [P02] | Assignment-oriented solver | Tests exact-solution reachability |
| GGNN/GIN from G4SATBench [P03] | Architecture replication | Checks dependence on one message block |
| NeuRes [P07] | Optional proof model | Tests whether explicit proof modeling changes relay utility |
| CaDiCaL/Kissat | Classical references | Verification, learned-clause baseline, cost sanity |

## 7. Full representation matrix

Mandatory:

1. ORG;
2. SEM fixed-rule;
3. RND-DEF;
4. VAC;
5. REWIRE-effective-resistance;
6. DEPTH-FLOP-matched;
7. RES-bounded;
8. CDCL-budgeted.

Conditional ablations:

- unique extension versus many-to-one auxiliary completion;
- AND/OR versus XOR interfaces;
- local versus multiscale interfaces;
- same graph topology with permuted semantics;
- compiler without original clauses, explicitly labeled as a restriction control;
- relay budget;
- train-on-original/test-on-relay and mixed-representation training;
- symbolic unit-propagation versus neural message passing.

## 8. Main experiment matrix

A realistic conditional main paper could use:

- 4 SAT families;
- 8 representation conditions;
- 3 neural architectures;
- 5 seeds;
- one shared train range and two OOD test ranges.

This is 120 principal training runs, not $4\times8\times3\times5$ separately if each architecture/condition is trained on a mixture with family-stratified batches. Family-specific training is reserved for ablations. Each checkpoint evaluates all paired representations and sizes permitted by its training condition.

## 9. Mechanism experiments

### M1 — semantic permutation

Hold the auxiliary graph topology and definition arities fixed while permuting which literal motifs each definition summarizes. If proof alignment matters, performance should degrade smoothly with semantic misalignment while graph statistics remain constant.

### M2 — logical-depth intervention

Generate formula pairs with matched variable/clause counts and graph diameter but different known circuit/proof depth. Add relays that equalize logical depth. Test whether the direct gap closes.

### M3 — propagation-process comparison

Run unit propagation, bounded resolution, and neural message passing on the same representations. Determine whether neural gains mirror symbolic propagation or reveal a distinct learned phenomenon.

### M4 — relay removal at test time

Train on relay graphs and evaluate after deleting or corrupting interfaces. If performance remains, relays may be training augmentation/regularization rather than inference routes.

### M5 — capacity-matched memory nodes

Add communication-only memory nodes with identical count and degree. If they match semantic relays, the effect is representational memory.

### M6 — compiler budget scaling

Vary added interfaces logarithmically while holding total compute fixed. The expected publishable result is not an arbitrary inverted-U; it is a predictable relation to logical-depth reduction with a cost crossover.

## 10. Robustness and generalization

- larger variable/clause counts;
- different clause-to-variable ratios;
- satisfiable versus unsatisfiable stratification;
- generator shift across G4SATBench families;
- polarity and variable-renaming invariance;
- compiler tie-breaking seeds;
- label noise and partial-assignment perturbations;
- model-depth and hidden-width changes;
- hardware/runtime profiling across graph batch sizes.

## 11. Required negative results

A strong paper should include cases where semantic relays do **not** help:

- formulas whose decisive consequences are already local;
- formulas where added definitions do not reduce logical depth;
- high-compute models that can derive the same consequences directly;
- cases where graph expansion increases memory and hurts throughput;
- transformations that shorten graph distance but not logical depth;
- formulas where classical CDCL learned clauses dominate.

Without these, the mechanism is indistinguishable from generic augmentation.

## 12. Conditional completion criteria

A full paper is complete only when:

- exactness proofs and code are public;
- every core result includes end-to-end compute and memory;
- the semantic-specific contrast replicates across two architectures and three non-toy families;
- the mechanism model predicts held-out gains;
- a classical proof/propagation baseline is included;
- reviewers can reproduce paired transformations from original formula hashes;
- no conclusion depends on one seed, one synthetic generator, or one relay budget.

# Dataset and Baseline Inventory

## 1. Primary dataset inventory

| Dataset/family | Source | Task | Role | Pilot/full |
|---|---|---|---|---|
| Implication chains | New deterministic generator | Assignment/SAT | Implementation sanity and depth control | Pilot only |
| Flattened vs balanced circuits | New paired generator | Assignment/SAT | Exact known semantic-interface intervention | Pilot and mechanism appendix |
| Planted XOR/parity/Tseitin | New generator, verified by exact solver | Assignment/SAT/UNSAT | Long-range logical composition | Pilot and full |
| G4SATBench SR | Official G4SATBench [P03, B01] | SAT and assignment | Primary recognized random family | Pilot and full |
| G4SATBench 3-SAT | Official G4SATBench [P03, B01] | SAT and assignment | Direct comparison with clause augmentation | Pilot and full |
| G4SATBench CA and PS | Official G4SATBench [P03, B01] | SAT and assignment | Pseudo-industrial shift | Conditional full |
| G4SATBench $k$-Clique/$k$-Domset/$k$-Vercov | Official G4SATBench [P03, B01] | Encoded combinatorial SAT | Structured cross-family validation | Conditional full |
| Frozen SAT Competition subset | Official competition instances, frozen manifest | SAT/UNSAT | External validity | Full only |
| One non-SAT CSP | To be fixed only after pilot | Feasible assignment | Breadth test | Full only |

## 2. Dataset construction rules

- Every original formula has an immutable ID and SHA-256 hash.
- Every transformation records compiler version, rule, seed, added variables, added clauses, and exactness certificate status.
- Train/validation/test splits are defined on original formulas before transformation.
- Paired representations never cross splits.
- Difficulty bins use original-formula statistics and exact/classical solver diagnostics, not relay solver performance.
- Synthetic generator parameters and all random seeds are committed before main evaluation.
- Failed compiler instances remain in the manifest with failure reason.

## 3. Neural baseline inventory

| Baseline | Source | Use policy |
|---|---|---|
| NeuroSAT | [P01] | Required primary neural baseline |
| QuerySAT / Goal-Aware Neural SAT Solver | [P02, B02] | Required if exact assignment is the main endpoint and setup is stable |
| GGNN, GCN, or GIN from G4SATBench | [P03, B01] | At least one architecture replication |
| NeuRes | [P07] | Optional proof-oriented comparison, not required for pilot |
| Mixed-representation training | New control | Tests distribution-shift versus mechanism |
| Original graph with global node/attention | Control | Tests generic communication capacity |

## 4. Representation and preprocessing baselines

| Baseline | Purpose |
|---|---|
| Original LCG/VCG | Direct representation |
| G4SATBench CDCL learned-clause augmentation | Strong published functional neighbor |
| Equal-count random clauses where valid | Replicate semantic-versus-random pattern carefully |
| Bounded resolution closure | Ordinary implied-consequence baseline |
| Random unique-extension variables | Extra exact hidden state without alignment |
| Tautological/fixed-variable auxiliary graph | Semantically vacuous state/topology control |
| Effective-resistance rewiring [P08] | Generic over-squashing control |
| Additional message-passing depth/width | Compute/capacity control |
| Circuit/Tseitin standard encoding | Classical exact extended-formulation reference |

## 5. Exact and classical software

| Tool | Role |
|---|---|
| CaDiCaL [B03] | Exact verification, learned-clause traces, baseline solve time |
| PySAT [B04] | Solver API, formula manipulation, cross-checks |
| CNFgen [B05] | Standard random/combinatorial CNF generation where applicable |
| G4SATBench repository [B01] | Datasets, representations, model implementations |
| QuerySAT repository [B02] | Assignment-focused baseline |

## 6. Baseline omission rules

The project stops rather than omits a decisive control. Specifically:

- If G4SATBench clause augmentation cannot be reproduced, C04 cannot claim novelty.
- If topology/compute matching cannot be implemented credibly, the relay mechanism cannot be tested.
- If exact projection equality cannot be verified, the intervention cannot be called a relay.
- If compiler cost cannot be measured, end-to-end claims are prohibited.

# Compute and Wall-Clock Budget for 8x RTX 4090

## 1. Hardware model

The eight RTX 4090 cards are treated as eight independent 24 GB workers. No run may assume model/data parallelism across cards. Each GPU has its own process, dataloader, checkpoint directory, and deterministic seed. CPU preprocessing and exact solving are scheduled separately so that the host does not starve GPU jobs.

Assumed supporting resources for planning purposes:

- 32 logical CPU cores preferred;
- 64 GB host RAM minimum, 128 GB preferred;
- 1 TB free SSD preferred for the full conditional program;
- Linux, CUDA-compatible PyTorch, and containerized solver dependencies.

If the actual host is smaller, concurrency—not per-run scientific design—must be reduced.

## 2. Per-run estimates

| Workload | VRAM | GPU-hours/run | CPU/RAM notes |
|---|---:|---:|---|
| S0 small NeuroSAT training | 2–6 GB | 0.3–1.0 | Light |
| G4SATBench easy/medium one seed | 6–12 GB | 1–4 | Dataset-dependent batching |
| Large/OOD graph evaluation | 8–18 GB | 0.2–1.0 | May require smaller batches |
| QuerySAT one seed | 8–16 GB | 2–6 | Depends on official configuration |
| Graph diagnostics | 0 GPU | n/a | 8–32 CPU cores; effective resistance can dominate |
| Exactness verification | 0 GPU | n/a | Parallel solver jobs; strict timeouts |
| CDCL clause generation | 0 GPU | n/a | CPU time charged per formula |

These are planning ranges, not promises. P0 measures actual throughput before P1 is launched.

## 3. Pilot budget

| Stage | GPU-hours | Eight-GPU compute wall time | Calendar allowance | Storage |
|---|---:|---:|---:|---:|
| P0 | 8–18 | 1–3 h | 0.5–1 day | 5–15 GB |
| P1 | 58–116 | 8–16 h | 1–2 days | 20–60 GB |
| P2 conditional | 56–140 | 8–20 h | 1–2 days | 30–100 GB |
| **Total if all stages run** | **122–274** | **17–39 h** | **2–4 calendar days** | **55–175 GB** |

The binding “1–3 day” falsification target refers to P0+P1. P2 is a conditional replication and may extend beyond 72 hours if the environment setup is slow.

## 4. Pilot scheduling

### GPU workers 0–5

Run the six core training/evaluation queues, one representation condition per worker where possible. Rotate conditions between GPUs across seeds to avoid a card-specific confound.

### GPU workers 6–7

Use for baseline reproduction, profiling, reruns due to infrastructure failures, and conditional second-model checks. They are not a hidden extra tuning budget.

### CPU queue

- exactness checks;
- compiler and CDCL preprocessing;
- graph diagnostics;
- result aggregation.

A central SQLite/Parquet run ledger records start/end time, device, commit, seed, formula manifest, condition, and failure status.

## 5. Conditional full-program budget

| Component | Principal runs | Aggregate GPU-hours | Eight-GPU compute time |
|---|---:|---:|---:|
| Three architectures × eight conditions × five seeds | 120 | 360–960 | 2–5 days |
| Mechanism ablations | 80–160 | 240–800 | 1.5–4.5 days |
| OOD/cross-family evaluation | checkpoints only | 80–240 | 0.5–1.5 days |
| Cross-domain replication | 40–80 | 160–480 | 1–3 days |
| Failed-run reserve and profiling | — | 150–350 | 1–2 days |
| **Conditional total** | — | **990–2,830** | **6–16 pure compute days** |

Realistic calendar time is 3–6 weeks because implementation, exactness debugging, CPU bottlenecks, analysis, and preregistered stage decisions dominate. This is why the full blueprint is not authorized before the pilot.

## 6. Memory and storage controls

- Store model checkpoints only for best validation step and final step.
- Store per-formula outputs and summary message statistics; full hidden-state traces only for a stratified diagnostic subset.
- Compress CNFs and manifests; avoid duplicating originals across conditions.
- Cap concurrent effective-resistance computations.
- Report peak allocated VRAM and host RAM for each condition.
- If SEM requires materially lower batch size, include throughput and gradient-noise consequences; matching analytical FLOPs alone is insufficient.

## 7. Budget kill conditions

Stop or shrink the design if:

- one P1 training run exceeds 8 GPU-hours without a reproduced baseline;
- exactness checks consume more than 24 CPU-hours per 10,000 medium formulas;
- transformed graphs exceed 2× original memory at the preregistered relay budget;
- full hidden-state logging exceeds 500 GB;
- preprocessing prevents eight-worker saturation for more than half the scheduled time;
- a proposed fairness control would more than double the entire pilot without being decisive—then reduce families, not controls.

# Fairness Controls, Statistics, and Kill Criteria

## 1. Fairness hierarchy

The order is binding:

1. exact endpoint and solution-set equality;
2. equal information and supervision;
3. compiler-inclusive model/environment-call equality;
4. parameter and state-capacity controls;
5. edge-message FLOP equality;
6. measured wall-clock and memory;
7. equal tuning and stopping rules;
8. statistical precision.

Statistical significance cannot repair a broken invariant.

## 2. Units of analysis

- **Formula** is the primary observational unit.
- **Training seed** is a random effect/cluster, not an independent formula observation.
- **Generator family and size bin** are prespecified strata.
- Representations are paired transformations of the same original formula.
- Multiple solver iterations from one formula are not independent replicates.

## 3. Primary statistical model

For binary exact-assignment success $Y_{isrm}$ on formula $i$, seed $s$, representation $r$, and model $m$:

$$
\operatorname{logit}\Pr(Y_{isrm}=1)
=\alpha
+\beta_r
+\gamma_m
+\delta_{\mathrm{family}(i)}
+\eta\log n_i
+u_i+v_s
+\text{prespecified interactions},
$$

where $u_i$ and $v_s$ are random intercepts or, if mixed-model fitting is unstable, formula-clustered and seed-clustered bootstrap effects are used.

The primary contrast is SEM versus each control with a joint intersection-union requirement: SEM must beat all decisive controls, not merely one average baseline.

## 4. Mechanism model

Fit nested held-out prediction models for per-instance relay gain:

- **Cost-only:** graph size, measured time, memory;
- **Graph-only:** shortest paths, diameter, effective resistance, degree, spectral features;
- **Logic-only:** generator-known depth, unit-propagation depth, bounded-resolution depth;
- **Combined:** all features.

Use formula-level cross-validation split by generator seed and size range. The mechanism claim requires logic features to improve held-out prediction beyond graph and cost features, not merely correlate in-sample.

## 5. Effect sizes and uncertainty

Report:

- absolute percentage-point differences;
- odds ratios from paired models;
- pooled standardized effect sizes for continuous metrics;
- 95% and 99% cluster-bootstrap intervals;
- per-seed results;
- family-specific and pooled effects;
- calibration and runtime distributions, not just means.

The preregistered PASS threshold is stronger than conventional $p<0.05$ because the pilot is screening a highly vulnerable idea.

## 6. Multiple comparisons

Primary comparisons:

1. SEM versus ORG;
2. SEM versus RND-DEF;
3. SEM versus best topology/compute control;
4. SEM versus RES/CDCL.

Use Holm correction within these four contrasts or the stricter intersection-union rule. Secondary metrics are labeled exploratory. Do not search across relay definitions and report only the best; all compiler variants appear in the run ledger.

## 7. Seed discipline

- Three seeds are sufficient for the initial kill-oriented pilot.
- Five seeds are mandatory only after P1 passes.
- A failed/diverged seed is part of the result.
- Additional seeds cannot be added solely because a contrast narrowly misses significance; the stage rule determines expansion.
- Hardware assignment is rotated across seeds.

## 8. Hyperparameter fairness

- Baseline reproduction uses published defaults first.
- Shared grid: at most two learning rates, two hidden widths, and two message-round settings during P0; choose globally, not per representation.
- Any representation-specific parameter is selected with the same number of trials for every condition.
- Compiler relay budget and motif threshold are fixed using S0/S1 and never tuned on G4SATBench test outcomes.
- The CDCL and RES budgets are matched by added edges/factors and preprocessing cost, with both matching definitions reported.

## 9. Essential ablations

1. semantic alignment permutation;
2. unique extension versus auxiliary multiplicity;
3. original clauses retained versus replaced;
4. compiler cost charged versus ignored;
5. equal rounds versus equal edge-message FLOPs;
6. equal FLOPs versus equal wall-clock;
7. semantic factors removed after training;
8. random definitions with identical arity distribution;
9. graph rewiring with matched effective resistance;
10. ordinary resolution and CDCL learned clauses;
11. small versus large/OOD formulas;
12. at least two architectures if the pilot passes.

## 10. Global kill criteria

The entire research line is terminated—not merely revised—if:

- BFAP is reintroduced as primary through renamed “relay bases”;
- the strongest result is an inverted-U relay-budget curve;
- a learned selector is necessary before a fixed relay effect exists;
- endpoint equality is approximate or utility-dependent;
- preprocessing uses proofs/labels and is not cheaper than direct reasoning;
- generic topology or extra depth explains the gain;
- only one synthetic family improves;
- the claimed mechanism changes after seeing the results;
- current literature reveals an exact functional duplicate;
- total full-program estimate exceeds the eight-GPU budget without a prior decisive pilot.

## 11. Negative-result value

A clean null pilot would still establish a useful internal result:

- exact semantic interfaces do not beat matched communication state;
- neural SAT gains from learned clauses are primarily structural/compute/distributional under these controls;
- extended formulations do not create a free relay after charging compilation and memory;
- the billiard intuition needs a different abstraction.

That result should be documented internally, not stretched into a main-conference submission unless it exposes a broadly important failure mode with strong theory.

# Paper Narrative and Venue Fit

## 1. Present status

There is no authorized paper narrative because the verdict is NO-GO. The correct current output is this audit and the bounded pilot specification. Drafting an abstract or selecting a venue now would create commitment bias.

## 2. Conditional narrative if every gate reopens

### Problem

Neural combinatorial solvers are usually compared across architectures while the logical representation is treated as fixed. Exact equivalent formulations can radically alter local computation, but gains are easily confounded by extra state, graph shortcuts, solver preprocessing, or changed solution multiplicity.

### Counterintuitive observation

A larger unique-extension formula can be easier for a smaller fixed-compute neural solver than the original formula, even when a topology-matched larger graph, extra message rounds, and ordinary learned clauses do not help as much.

### Mechanism

Semantic proof interfaces reduce logical propagation depth and permit reusable local composition. The effect is distinct from generic graph connectivity and does not change projected solutions.

### Method

A cheap, label-free semantic relay compiler derived from a formal depth-reduction criterion.

### Evidence

Exact proofs; paired transformations; semantic/topology/compute controls; OOD scaling; two architectures; one cross-domain replication; end-to-end cost; held-out mechanism prediction.

## 3. Claims the paper must not make

- “Auxiliary variables improve SAT solving” as a new observation.
- “Learned clauses help GNNs” as a new result.
- “GNNs suffer from long-range dependencies” as novelty.
- “Our relay budget has an optimum” as the headline.
- “The projected solution set is similar” when exact equality is available.
- “Compute matched” while excluding compiler time or changed batch size.
- “Semantic” without topology-matched controls.
- “General AI reasoning” based only on implication chains and random 3-SAT.

## 4. Likely reviewer questions

| Reviewer question | Required answer |
|---|---|
| How is this different from G4SATBench learned-clause augmentation? | Unique-extension interface, compiler restrictions, topology/compute controls, and direct matched comparison. |
| How is this different from extended resolution? | Neural fixed-compute causal separation plus a new theorem or scaling law; otherwise it is not different enough. |
| Did preprocessing solve the instance? | Local compiler complexity, no proof traces, end-to-end cost, and direct solver comparison. |
| Are gains just graph rewiring? | Topology/degree/effective-resistance matched controls and semantic permutation experiment. |
| Are gains just extra hidden state? | Vacuous/random exact auxiliary nodes and memory-matched direct architecture. |
| Why not run more message-passing rounds? | Equal edge-message FLOPs/wall-clock depth baseline. |
| Does it work outside toy formulas? | G4SATBench OOD and structured combinatorial family. |
| Does it help classical solvers? | Report diagnostic; paper is about neural computation, not hiding classical regressions. |
| Is the main result predictable from proof complexity? | A genuinely surprising separation must be articulated; this is presently unresolved. |

## 5. Venue fit after a hypothetical pass

| Evidence level | Suitable outlet | Assessment |
|---|---|---|
| Toy separation + one SAT family | SAT/CP/NeurIPS workshop or neural reasoning workshop | Useful diagnostic, not main-conference novelty |
| Strong SAT study with matched controls but limited theory | AAAI/IJCAI, TMLR, specialized SAT/CP venue | Solid if execution is rigorous; still novelty-sensitive |
| Theory + multi-family OOD + two architectures | ICLR/ICML/NeurIPS main track | Plausible only after fresh collision audit |
| General theorem + SAT and another CSP + predictive mechanism | ICLR/ICML/NeurIPS standout territory | Would finally satisfy the requested ambition |

## 6. Current venue decision

**[D] Do not target a venue. Do not write the paper. Run at most the bounded pilot.**

# Two Backup Directions

## Backup A — Gauge-Orbit Teleportation

### Status

**Parked, not authorized.** It is a genuine relay with excellent invariance and cheap experiments, but the core function is directly occupied by Neural Teleportation, Symmetry Teleportation, Level-Set Teleportation, parameter-symmetry optimization, and gauge-invariant LoRA work [G01–G08].

### Reopening condition

Reopen only if a fundamentally new symmetry or operational setting is found where:

- existing teleportation/invariant-optimizer methods do not apply;
- the transformation preserves function, loss, parameter count, and optimizer information exactly;
- the result is not a new gauge-selection heuristic;
- a theory predicts a qualitatively different phenomenon, such as optimizer-state memory transport unavailable to all known equivariant methods;
- large-scale impact can be tested within the 8×4090 constraint.

### Fast transition plan if reopened

1. Reproduce symmetry teleportation and LoRA Done RITE.
2. Construct exact gauge-equivalent checkpoints.
3. Test optimizer-state transport under Adam versus equivariant controls.
4. Kill immediately if existing methods explain the effect.

### Why it is not a current backup paper

A backup should pass the gates with lower priority. This candidate fails novelty outright; it is a research theme to monitor, not a fallback submission.

## Backup B — Semantic Quotient DAG Search

### Status

**Parked, not authorized.** Exact state quotienting is a genuine relay, but current LLM work explicitly merges semantically equivalent states and reasoning paths [D05–D08]. Natural-language equivalence also creates a severe oracle/cost/restriction problem.

### Reopening condition

Reopen only in a domain with exact, cheap future-state equivalence that is not already standard transposition-table graph search, and where:

- the final answer set is proven unchanged;
- equivalence computation is included in the token/FLOP budget;
- the method creates a nontrivial new learning problem beyond duplicate detection;
- FETCH, LSC, AoT, GraphPO, and classical graph-search controls are implemented;
- the qualitative result is not simply “DAG beats tree when transpositions exist.”

### Fast transition plan if reopened

1. Choose executable states, theorem states, or deterministic agent states with exact hashes.
2. Compare tree and transposition-DAG search at identical expansions.
3. Add learned approximate equivalence only after the exact ceiling is known.
4. Stop if classical transposition tables capture the gain.

### Why it is not a current backup paper

The mechanism is already explicit in current literature and a fair LLM pilot is more expensive and less clean than C04.

## Comparative trigger table

| Trigger | C04 semantic relays | Backup A gauge | Backup B quotient DAG |
|---|---|---|---|
| Current novelty pass | No | No | No |
| Current surprise pass | No | No | No |
| Invariance quality | High conditional | Very high | Low–high depending on exactness |
| Cheapest clean pilot | **Yes** | Yes | No |
| Direct 2026 collision | Extended resolution/augmentation | Basis–Adam/gauge work | GraphPO/semantic clustering |
| Authorized now | **One bounded probe** | No | No |

# Verified Bibliography

## Citation policy

The bibliography below is keyed to the bracket identifiers used throughout the document. Titles, author lists, years, venues, publication status, and links were checked against primary records: official proceedings, OpenReview, ACL Anthology, PMLR, journal pages, arXiv records, or official software repositories. A work is called a **preprint** or **submission** when the primary record did not establish peer-reviewed acceptance as of **25 August 2026**. The bibliography is intentionally selective: it records the load-bearing works used in the decision, not every paper encountered during search.

## Sampling-based planning, trajectory parameterization, and action-space restriction

- **[A01]** Cristina Pinneri, Shambhuraj Sawant, Sebastian Blaes, Jan Achterhold, Joerg Stueckler, Michal Rolinek, and Georg Martius. **“Sample-efficient Cross-Entropy Method for Real-time Planning.”** Conference on Robot Learning 2020, published in PMLR 155, 2021. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v155/pinneri21a.html)
- **[A02]** Joe Watson and Jan Peters. **“Inferring Smooth Control: Monte Carlo Posterior Policy Iteration with Gaussian Processes.”** Conference on Robot Learning 2022, published in PMLR 205, 2023. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v205/watson23a.html)
- **[A03]** Zeji Yi, Chaoyi Pan, Guanqi He, Guannan Qu, and Guanya Shi. **“CoVO-MPC: Theoretical Analysis of Sampling-based MPC and Optimal Covariance Design.”** Learning for Dynamics and Control 2024, PMLR 242. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v242/yi24b.html)
- **[A04]** Zhengyao Jiang, Tianjun Zhang, Michael Janner, Yueying Li, Tim Rocktäschel, Edward Grefenstette, and Yuandong Tian. **“Efficient Planning in a Compact Latent Action Space.”** ICLR 2023. **Status:** peer-reviewed conference paper. [arXiv record](https://arxiv.org/abs/2208.10291)
- **[A05]** Piotr Kicki. **“LP-MPPI: Low-Pass Filtering for Efficient Model Predictive Path Integral Control.”** ICRA 2026. **Status:** accepted peer-reviewed conference paper. [arXiv record](https://arxiv.org/abs/2503.11717)
- **[A06]** Yutao Chen, Nicolò Scarabottolo, Mattia Bruschetta, and Alessandro Beghi. **“An Efficient Move Blocking Strategy for Multiple Shooting Based Nonlinear Model Predictive Control.”** IET Control Theory & Applications 14(2):343–351, 2020; arXiv version 2019. **Status:** peer-reviewed journal paper. [arXiv record](https://arxiv.org/abs/1909.09710) · [journal DOI](https://doi.org/10.1049/iet-cta.2019.0168)
- **[A07]** Valentina Breschi, Simone Formentin, and Alberto Leva. **“Model Predictive Control with Dynamic Move Blocking.”** 2023. **Status:** arXiv preprint. [arXiv record](https://arxiv.org/abs/2308.07854)
- **[A08]** An T. Le, Khai Nguyen, Minh Nhat Vu, João Carvalho, and Jan Peters. **“Model Tensor Planning.”** TMLR 2025. **Status:** accepted peer-reviewed journal paper. [arXiv record](https://arxiv.org/abs/2505.01059) · [OpenReview record](https://openreview.net/forum?id=fk1ZZdXCE3)

## Neural SAT, solution-preserving transformations, proof systems, and graph propagation

- **[P01]** Daniel Selsam, Matthew Lamm, Benedikt Bünz, Percy Liang, Leonardo de Moura, and David L. Dill. **“Learning a SAT Solver from Single-Bit Supervision.”** ICLR 2019. **Status:** peer-reviewed conference paper. [OpenReview record](https://openreview.net/forum?id=HJMC_iA5tm) · [arXiv record](https://arxiv.org/abs/1802.03685)
- **[P02]** Emīls Ozoliņš, Kārlis Freivalds, Andis Draguns, Elīza Gaile, Ronalds Zakovskis, and Sergejs Kozlovičs. **“Goal-Aware Neural SAT Solver.”** IJCNN 2022. **Status:** peer-reviewed conference paper. [arXiv record](https://arxiv.org/abs/2106.07162)
- **[P03]** Zhaoyu Li, Jinpei Guo, and Xujie Si. **“G4SATBench: Benchmarking and Advancing SAT Solving with Graph Neural Networks.”** Transactions on Machine Learning Research, 2024. **Status:** peer-reviewed journal paper. [arXiv record](https://arxiv.org/abs/2309.16941) · [OpenReview record](https://openreview.net/forum?id=7VB5db72lr)
- **[P04]** Haonan Duan, Pashootan Vaezipoor, Max B. Paulus, Yangjun Ruan, and Chris Maddison. **“Augment with Care: Contrastive Learning for Combinatorial Problems.”** ICML 2022, PMLR 162. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v162/duan22b.html)
- **[P05]** Saku Peltonen and Roger Wattenhofer. **“On the Expressive Power of GNNs for Boolean Satisfiability.”** ICLR 2026. **Status:** accepted peer-reviewed conference paper. [OpenReview record](https://openreview.net/forum?id=Q01JX3CuDx) · [arXiv record](https://arxiv.org/abs/2602.08745) · [official code](https://github.com/sakupeltonen/sat-expressivity)
- **[P06]** Sam Buss, Jonathan Chung, Vijay Ganesh, and Albert Oliveras. **“Extended Resolution Clause Learning via Dual Implication Points.”** Logical Methods in Computer Science 22(2), 2026. **Status:** peer-reviewed journal paper, published 25 May 2026. [LMCS record](https://lmcs.episciences.org/18269) · [arXiv record](https://arxiv.org/abs/2406.14190)
- **[P07]** Mohamed Ghanem, Frederik Schmitt, Julian Siber, and Bernd Finkbeiner. **“Learning Better Representations From Less Data For Propositional Satisfiability.”** NeurIPS 2024. **Status:** peer-reviewed conference paper. [arXiv record](https://arxiv.org/abs/2402.08365) · [OpenReview record](https://openreview.net/forum?id=VMsHnv8cVs)
- **[P08]** Mitchell Black, Zhengchao Wan, Amir Nayyeri, and Yusu Wang. **“Understanding Oversquashing in GNNs through the Lens of Effective Resistance.”** ICML 2023, PMLR 202. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v202/black23a.html)
- **[P09]** Randal E. Bryant and Marijn J. H. Heule. **“Extended Resolution Simulates DRAT.”** TACAS 2021. **Status:** peer-reviewed conference paper. [Springer/DOI record](https://doi.org/10.1007/978-3-030-79876-5_30)
- **[P10]** Chengdi Cao, Cho-Jui Hsieh, and Jason Cong. **“MAS-SAT: Synergizing ML-Assisted and Standalone Solvers for SAT Solving.”** ICLR 2026 submission. **Status:** OpenReview submission; this document does not assert acceptance. [OpenReview record](https://openreview.net/forum?id=EWT7ILOzjK)
- **[P11]** Eshed Gal, Uri Ascher, and Eldad Haber. **“Target-Aware Data Augmentation for SAT Prediction.”** 2026. **Status:** arXiv preprint, submitted 7 May 2026. [arXiv record](https://arxiv.org/abs/2605.06931)
- **[P12]** Kostis Michailidis, Dimos Tsouros, Nguyen Dang, and Tias Guns. **“LLM-Guided Evolutionary Search for Constraint Model Reformulation to Improve Solver Efficiency.”** 2026. **Status:** arXiv preprint, submitted 30 July 2026. [arXiv record](https://arxiv.org/abs/2607.28268)
- **[P13]** Penglin Zhu, Linhai Zhang, Jungang Xu, Xinchi Wei, and Xiuqi Wu. **“IR2Solve: Structured Intermediate Representations for Cost-Efficient Optimization Autoformulation.”** 2026. **Status:** arXiv preprint, submitted 31 July 2026. [arXiv record](https://arxiv.org/abs/2608.02641)

## Function-preserving symmetries, teleportation, and low-rank gauge invariance

- **[G01]** Marco Armenta, Thierry Judge, Nathan Painchaud, Youssef Skandarani, Carl Lemaire, Gabriel Gibeau Sanchez, Philippe Spino, and Pierre-Marc Jodoin. **“Neural Teleportation.”** Mathematics 11(2):480, 2023; original preprint 2020. **Status:** peer-reviewed journal paper. [arXiv record](https://arxiv.org/abs/2012.01118) · [journal record](https://www.mdpi.com/2227-7390/11/2/480)
- **[G02]** Bo Zhao, Nima Dehmamy, Robin Walters, and Rose Yu. **“Symmetry Teleportation for Accelerated Optimization.”** NeurIPS 2022. **Status:** peer-reviewed conference paper. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2022/hash/69f7750aa28f75fddf101da038f8b529-Abstract-Conference.html)
- **[G03]** Bo Zhao, Robert M. Gower, Robin Walters, and Rose Yu. **“Improving Convergence and Generalization Using Parameter Symmetries.”** ICLR 2024 oral. **Status:** peer-reviewed conference paper. [OpenReview record](https://openreview.net/forum?id=L0r0GphlIL)
- **[G04]** Aaron Mishkin, Alberto Bietti, and Robert M. Gower. **“Level Set Teleportation: An Optimization Perspective.”** AISTATS 2025, PMLR 258. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v258/mishkin25a.html) · [arXiv record](https://arxiv.org/abs/2403.03362)
- **[G05]** Zihao Wu, Juncheng Dong, Ahmed Aloui, and Vahid Tarokh. **“Teleportation With Null Space Gradient Projection for Optimization Acceleration.”** ICPR 2026, Lecture Notes in Computer Science. **Status:** peer-reviewed conference paper. [Springer record](https://link.springer.com/chapter/10.1007/978-3-032-31452-9_18) · [arXiv record](https://arxiv.org/abs/2502.11362)
- **[G06]** Jui-Nan Yen, Si Si, Zhao Meng, Felix Yu, Sai Surya Duvvuri, Inderjit S. Dhillon, Cho-Jui Hsieh, and Sanjiv Kumar. **“LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization.”** ICLR 2025. **Status:** peer-reviewed conference paper. [OpenReview record](https://openreview.net/forum?id=VpWki1v2P8) · [arXiv record](https://arxiv.org/abs/2410.20625)
- **[G07]** Valérie Castin, Kimia Nadjahi, Pierre Ablin, and Gabriel Peyré. **“Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence.”** ICML 2026. **Status:** accepted peer-reviewed conference paper. [arXiv record](https://arxiv.org/abs/2605.31484) · [OpenReview record](https://openreview.net/forum?id=kHInw3cjCP)
- **[G08]** Devender Singh. **“The Loss Does Not See the Basis, but Adam Does.”** 2026. **Status:** arXiv preprint, submitted 5 August 2026. [arXiv record](https://arxiv.org/abs/2608.05136)

## Tree, graph, and semantic-equivalence search for language-model reasoning

- **[D01]** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. **“Tree of Thoughts: Deliberate Problem Solving with Large Language Models.”** NeurIPS 2023. **Status:** peer-reviewed conference paper. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html)
- **[D02]** Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michal Podstawski, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, and Torsten Hoefler. **“Graph of Thoughts: Solving Elaborate Problems with Large Language Models.”** AAAI 2024. **Status:** peer-reviewed conference paper. [AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/29720)
- **[D03]** Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, and Zhiting Hu. **“Reasoning with Language Model Is Planning with World Model.”** EMNLP 2023. **Status:** peer-reviewed conference paper. [ACL Anthology](https://aclanthology.org/2023.emnlp-main.507/)
- **[D04]** Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang. **“Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models.”** ICML 2024, PMLR 235. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v235/zhou24r.html)
- **[D05]** Ante Wang, Linfeng Song, Ye Tian, Dian Yu, Haitao Mi, Xiangyu Duan, Zhaopeng Tu, Jinsong Su, and Dong Yu. **“Don’t Get Lost in the Trees: Streamlining LLM Reasoning by Overcoming Tree Search Exploration Pitfalls.”** ACL 2025 long paper. **Status:** peer-reviewed conference paper. [ACL Anthology](https://aclanthology.org/2025.acl-long.1167/)
- **[D06]** Sungjae Lee, Hoyoung Kim, Jeongyeon Hwang, Eunhyeok Park, and Jungseul Ok. **“Efficient Latent Semantic Clustering for Scaling Test-Time Computation of LLMs.”** Findings of EMNLP 2025. **Status:** peer-reviewed conference paper. [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.1310/) · [arXiv record](https://arxiv.org/abs/2506.00344)
- **[D07]** Fengwei Teng, Quan Shi, Zhaoyang Yu, Jiayi Zhang, Yuyu Luo, Chenglin Wu, and Zhijiang Guo. **“Atom of Thoughts for Markov LLM Test-Time Scaling.”** NeurIPS 2025. **Status:** peer-reviewed conference paper. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b1018f844177088c380e1143d55cdfb-Abstract-Conference.html)
- **[D08]** Yuliang Zhan, Xinyu Tang, Jian Li, Dandan Zheng, Weilong Chai, Jingdong Chen, Jun Zhou, Ge Wu, Wenyue Tang, and Hao Sun. **“GraphPO: Graph-based Policy Optimization for Reasoning Models.”** 2026. **Status:** arXiv preprint, submitted 17 June 2026. [arXiv record](https://arxiv.org/abs/2606.18954)

## Mature adjacent relay families

- **[M01]** Kirill Neklyudov, Max Welling, Evgenii Egorov, and Dmitry Vetrov. **“Involutive MCMC: a Unifying Framework.”** ICML 2020, PMLR 119. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v119/neklyudov20a.html)
- **[M02]** Tiange Liu, Nikola Surjanovic, Miguel Biron-Lattes, Alexandre Bouchard-Côté, and Trevor Campbell. **“AutoStep: Locally Adaptive Involutive MCMC.”** ICML 2025, PMLR 267. **Status:** peer-reviewed conference paper. [PMLR record](https://proceedings.mlr.press/v267/liu25br.html) · [arXiv record](https://arxiv.org/abs/2410.18929)
- **[M03]** Kensen Shi, Joey Hong, Yinlin Deng, Pengcheng Yin, Manzil Zaheer, and Charles Sutton. **“ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis.”** ICLR 2024. **Status:** peer-reviewed conference paper. [OpenReview record](https://openreview.net/forum?id=oTRwljRgiv) · [arXiv record](https://arxiv.org/abs/2307.13883)
- **[M04]** Kavi Gupta, Peter Ebert Christensen, Xinyun Chen, and Dawn Song. **“Synthesize, Execute and Debug: Learning to Repair for Neural Program Synthesis.”** NeurIPS 2020. **Status:** peer-reviewed conference paper. [NeurIPS proceedings](https://proceedings.neurips.cc/paper/2020/hash/cd0f74b5955dc87fd0605745c4b49ee8-Abstract.html) · [arXiv record](https://arxiv.org/abs/2007.08095)
- **[M05]** Haiming Wang, Huajian Xin, Zhengying Liu, Wenda Li, Yinya Huang, Jianqiao Lu, Zhicheng Yang, Jing Tang, Jian Yin, Zhenguo Li, and Xiaodan Liang. **“Proving Theorems Recursively.”** NeurIPS 2024. **Status:** peer-reviewed conference paper. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9de7a49945898da86e062e7029baa284-Abstract-Conference.html)

## Software, datasets, and generators

- **[B01]** Zhaoyu Li, Jinpei Guo, and Xujie Si. **G4SATBench official repository.** **Status:** public research code and benchmark implementation. [GitHub](https://github.com/zhaoyu-li/G4SATBench)
- **[B02]** LUMII Syslab. **QuerySAT official repository.** **Status:** public research code. [GitHub](https://github.com/LUMII-Syslab/QuerySAT)
- **[B03]** Armin Biere and contributors. **CaDiCaL SAT solver.** **Status:** maintained open-source SAT solver. [GitHub](https://github.com/arminbiere/cadical)
- **[B04]** Alexey Ignatiev and contributors. **PySAT: Python toolkit for prototyping with SAT oracles and encodings.** **Status:** maintained open-source toolkit. [Official documentation](https://pysathq.github.io/) · [GitHub](https://github.com/pysathq/pysat)
- **[B05]** Massimo Lauria and contributors. **CNFgen: generator of CNF formulas for proof-complexity and SAT experiments.** **Status:** open-source generator. [Official site](https://massimolauria.net/cnfgen/) · [GitHub](https://github.com/MassimoLauria/cnfgen)

# Search Log

## Retrieval window and audit date

- **Audit date:** 25 August 2026, Asia/Tokyo.
- **Literature window:** foundational work where necessary, with concentrated retrieval from 2022 through 25 August 2026.
- **Target venues and records:** ICLR, ICML, NeurIPS, AAAI, ACL/EMNLP, AISTATS, CoRL, L4DC, ICRA, ICPR, TMLR, LMCS, TACAS, official arXiv records, and official repositories.
- **Status rule:** accepted/published status was asserted only when the primary record established it. OpenReview-only work without a visible decision was labeled submission; 2026 arXiv-only work was labeled preprint.

## Source-document integrity record

The binding instruction and failed formalization were both read in full before candidate generation.

| File | Role in this investigation | Lines | Words | SHA-256 |
|---|---|---:|---:|---|
| `AI_research_reabstraction_prompt.md` | Binding instruction | 265 | 2,483 | `86fc640608a329c33e1752a1abe1495f2bd12cae8267badc47cb38d58ffa71af` |
| `AI_RESEARCH_IDEA_LANDSCAPE(1).md` | Failed first formalization to audit, never treated as an optimization anchor | 1,988 | 23,485 | `a26c6aeea8b48283201cd1d5f2e65ca769177b1dc7b1250639e1cf7925929019` |

## Search sequence

1. **Extracted the binding distinction.** The seed was rewritten as a question about enlarging the upstream preimage of a fixed downstream success set. Candidate mechanisms were required to add routes, interfaces, auxiliary states, or equivalent representations rather than merely remove degrees of freedom.
2. **Forensically audited the previous report.** BFAP, its decoder family, its adaptive selector, and its proposed theorem were checked against the restriction-versus-relay test before any new idea generation.
3. **Generated mechanism-diverse candidates before selecting a domain.** The search covered continuous control, neural combinatorial solving, optimization geometry, language-model inference, theorem proving, program synthesis, MCMC, model composition, representation interfaces, and offline RL.
4. **Ran collision searches by mechanism rather than by project name.** For each serious candidate, the search used synonyms for the functional role: exact reformulation, auxiliary variable, extension variable, function-preserving transformation, level-set move, semantic state merge, transposition, lifted chain, bridge distribution, execution decomposition, lemma invention, and learned clause.
5. **Traced backward and forward.** Foundational mechanism papers were paired with 2024–2026 forward neighbors to determine whether a seemingly new re-abstraction was already an active named family.
6. **Applied the hard gates.** Candidates were killed for restriction, endpoint mismatch, hidden information, compute mismatch, predictable prior-art consequence, weak benchmark fit, or inability to isolate mechanism.
7. **Stopped only after convergence.** Repeated searches across primary venues returned the same three occupied mechanism families: action restriction, function-preserving teleportation, and semantic-equivalence search. The remaining SAT/CSP formulation differed in controls but not enough in headline mechanism to authorize a paper program.

## Major query families

The following query families were run with title, mechanism, venue, and recent-year variants:

- `trajectory basis sampling MPC move blocking adaptive action parameterization`
- `low-frequency action sampling CEM MPPI spline trajectory latent action planning`
- `SAT learned clauses graph neural network augmentation`
- `SAT resolution-preserving augmentation contrastive learning`
- `extended resolution auxiliary variables neural SAT solver`
- `extension variables factor graph GNN SAT CSP`
- `solution-preserving reformulation neural combinatorial solver`
- `GNN SAT expressive power Weisfeiler Leman industrial SAT`
- `redundant constraints neural constraint satisfaction solver`
- `function-preserving neural network transformation optimization teleportation`
- `level-set teleportation parameter symmetry optimization`
- `LoRA gauge invariance rotation scaling optimizer Adam`
- `same loss different basis Adam factored model`
- `semantically equivalent states merge LLM tree search DAG`
- `semantic clustering test-time computation LLM reasoning`
- `reasoning DAG merge paths same token budget`
- `transposition table graph search language model`
- `lifted nonreversible MCMC auxiliary state exact target`
- `annealed bridge distribution sequential Monte Carlo rare target`
- `execution decomposition neural program synthesis intermediate state`
- `lemma generation recursive theorem proving subgoal`
- `set-valued subgoal reachability goal-conditioned RL 2025 2026`
- `capture region skill chaining learned predecessor set`
- `model stitching bridge checkpoint parameter alignment`
- `error-correcting latent interface modular neural network`

## Venue-by-venue coverage for the decisive near-miss

| Source family | What was checked | Main collision signal |
|---|---|---|
| TMLR / OpenReview | Neural SAT benchmarks and clause augmentation | G4SATBench already observes large gains from learned-clause augmentation [P03]. |
| ICML / PMLR | SAT-preserving augmentation and GNN rewiring | Label-preserving resolution transformations and topology rewiring are established [P04, P08]. |
| ICLR | Neural SAT expressivity and fixed-depth limits | The expressivity problem is now explicit and current [P05]. |
| LMCS / TACAS | Extended resolution and auxiliary proof variables | The exact proof-system mechanism of introducing definitional variables is established [P06, P09]. |
| NeurIPS | Neural resolution/proof learning | Neural models already derive and use clauses as proof objects [P07]. |
| 2026 arXiv / OpenReview | Current SAT augmentation, hybrid solving, and reformulation | The application neighborhood continues to fill [P10–P13]. |

## Backward and forward tracing notes

### BFAP and action restriction

Backward tracing reached classical move blocking and correlated/smooth proposal priors. Forward tracing reached compact latent actions, covariance-designed MPC, low-pass MPPI, and structured tensor planning [A01–A08]. These works differ in implementation, but they occupy the same functional role: making finite-budget planning easier by changing or restricting the action proposal family. The previous report’s own “utility-preserving restriction” proposition correctly described the mechanism it later misclassified as a relay.

### Semantic Relay Compilation

Backward tracing reached resolution, extended resolution, auxiliary-variable encodings, implied constraints, and propagation-enhancing reformulations. Forward tracing reached neural SAT clause augmentation, SAT-preserving representation learning, explicit GNN expressivity limits, 2026 extended-resolution solvers, target-aware SAT augmentation, hybrid ML/SAT solvers, and LLM-generated reformulations [P01–P13]. No exact paper was found that combines unique-extension interfaces, topology-matched semantic controls, and end-to-end compute matching. Nevertheless, the broad qualitative result—derived semantic structure can improve neural solving without changing satisfiability—is already observed and predicted by adjacent theory. That is why the direction remains only a falsification probe.

### Gauge-Orbit Teleportation

Backward tracing reached neural teleportation and level-set symmetry moves. Forward tracing reached explicit parameter-symmetry optimization, null-space teleportation, invariant LoRA optimization, balanced factor projections, and a 5 August 2026 preprint whose title states the basis/Adam dependence directly [G01–G08]. The functional duplicate is exact, not merely thematic.

### Semantic Quotient DAG Search

Backward tracing reached tree search, graph search, and transposition. Forward tracing reached tree/graph-of-thought methods, agent tree search, semantic-node clustering, Markov DAG contraction, and GraphPO’s explicit merging of semantically equivalent paths under matched response or token budgets [D01–D08]. A new paper would need a substantially different resource-neutral mechanism, not another clustering score or merge heuristic.

## Search limitations

1. **No proprietary citation database was available.** The audit used public primary records rather than exhaustive Scopus, Web of Science, or Dimensions citation graphs. An obscure workshop paper or in-press manuscript may therefore have been missed.
2. **2026 is still moving.** Preprint status, conference decisions, and repository versions may change after 25 August 2026. This document freezes the evidence at that date.
3. **OpenReview indexing is imperfect.** Some records expose titles and decisions inconsistently to automated retrieval. Where acceptance could not be established from a primary record, the work was conservatively labeled submission or preprint.
4. **No local runtime benchmark was executed.** The compute and wall-clock estimates are engineering forecasts based on model size, graph size, and public implementations. They must be replaced by measurements in Stage 0 of the bounded pilot.
5. **The absence claim is scoped.** The search did not find an exact implementation of the proposed unique-extension, semantic-versus-topology, end-to-end-compute experiment. It does not claim mathematical proof that no such work exists. The NO-GO follows because the intended qualitative headline is already functionally occupied and predictable, not because every experimental detail has appeared verbatim.

## Reproducibility of the literature audit

A rerun should:

1. start from the exact two file hashes recorded above;
2. freeze the audit date;
3. repeat the query families with the date suffixes `2025` and `2026`;
4. inspect primary records rather than search snippets;
5. label every 2026 work as accepted, published, submission, or preprint from the source itself;
6. search exact titles of [P03], [P04], [P06], [G02], [G06], [G07], [G08], [D05], [D06], and [D08];
7. repeat forward searches using the mechanism phrases `learned clauses`, `extension variables`, `level-set teleportation`, `parameter invariance`, and `semantically equivalent states`;
8. reopen the decision only if a candidate clears the fixed novelty and surprise thresholds rather than merely adding an implementation detail.

## Final audit record

| Item | Result |
|---|---:|
| Candidate mechanisms generated | 20 |
| Candidates sent to deep shortlist | 3 |
| Candidates passing all hard gates | 0 |
| Authorized primary paper directions | 0 |
| Authorized backup paper directions | 0 |
| Authorized experiments | 1 bounded mechanism-discriminating falsification probe |
| Final decision | **NO-GO: RE-ABSTRACTION NOT YET ACHIEVED** |

The search therefore ends with a disciplined negative result, not with BFAP renamed, not with an arbitrary domain choice, and not with a near-duplicate promoted by extra experimental polish. The unresolved scientific question is whether a cheap, information-neutral, capacity-neutral, and end-to-end-compute-neutral semantic interface can beat topology-only shortcuts and extra direct computation **for reasons not already explained by extended formulations, proof compilation, or graph rewiring**. Until that separation is demonstrated by the bounded pilot, a full paper program is not justified.
