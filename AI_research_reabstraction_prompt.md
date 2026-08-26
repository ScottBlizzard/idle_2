# Research-Idea Re-Abstraction Prompt for Pro

You are acting as a top-tier AI research program designer, an adversarial literature reviewer, and a skeptical ICLR/NeurIPS area chair. Your task is not to polish an existing idea. Your task is to determine whether the original intuition below admits a genuinely non-obvious, rapidly testable AI contribution after a previous formalization collapsed into a familiar dimensionality/regularization trade-off.

You will receive an attached document named `AI_RESEARCH_IDEA_LANDSCAPE.md`. Read it completely. Treat it as a **failed first formalization, a source of literature leads, and an object for adversarial critique**—not as an authoritative recommendation and not as an anchor that must be repaired.

Conduct continuous web and literature search while reasoning. The final output must be one self-contained Markdown document, not a conversational answer.

## 1. Original intuition

The seed came from billiards. Suppose a direct shot into a pocket has a narrow successful input region. Placing an intermediate ball behind the target ball may make a broader range of upstream contacts lead to the same final success. Extending this into a line or curve of intermediate contacts suggests that intermediate structure may enlarge the upstream preimage of a fixed downstream success set.

The intended mechanism is **not ordinary numerical error attenuation**. A result is uninteresting if tolerance improves merely because velocity, energy, action magnitude, effective degrees of freedom, task difficulty, resolution, or final utility has been reduced. The central question is whether intermediate structure can create, transport, compose, redirect, or reshape reachability so that more upstream perturbations lead to the same meaningful endpoint without exhausting the transmitted value.

A robot-arm analogy illustrates the distinction. Wrist rotation alone may not reach an object. Shoulder and elbow motions do not merely attenuate wrist error; they move the downstream reachable workspace and create routes that did not exist for the wrist alone. However, robotics is only an intuition aid. Do not assume the final direction must involve robots, embodied AI, control, or reinforcement learning.

## 2. Why the previous BFAP direction is provisionally rejected

The attached report selected Basin-First Adaptive Planning (BFAP): choose an intermediate-dimensional temporal action basis because a full per-time-step action space may be too difficult to search under a finite rollout budget.

Before generating new directions, perform a forensic audit of this decision. The current objection is:

1. “Too few dimensions underfit, too many dimensions are difficult to optimize, and an intermediate dimension is best” is a standard approximation–optimization or bias–variance trade-off.
2. Spline controls, control knots, temporal abstraction, action repeat/chunking, low-frequency sampling, latent actions, covariance shaping, and adaptive control resolution already occupy the neighboring literature.
3. A capability-retention threshold is good experimental hygiene but is not necessarily novelty.
4. A robust-preimage statistic plus online basis selection may be judged as a diagnostic plus hyperparameter tuning.
5. Experiments that only vary basis dimension, smoothness, and rollout budget are structurally likely to produce insights about compression and regularization rather than the original relay mechanism.

Do not assume this critique is correct merely because it appears in the prompt. Verify it adversarially against current literature. Then issue one of three decisions:

- **ELIMINATE BFAP** as a primary direction;
- **RETAIN ONLY AS INFRASTRUCTURE/BASELINE**;
- **RESCUE**, but only if you can formulate a qualitatively stronger claim that cannot be reduced to “an intermediate amount is best,” smoothing, dimensionality reduction, regularization, or automatic hyperparameter selection.

A rescue must state exactly what new experiment would make an expert unable to predict the result from the standard approximation–optimization trade-off. Merely adding more benchmarks, a learned selector, a theorem about hit probability, or a new metric is insufficient.

## 3. Binding conceptual distinction: restriction versus relay

Use the following distinction throughout the investigation.

### Restriction mechanism

The method removes choices, narrows a hypothesis/action/search space, smooths trajectories, reduces rank, reduces decision frequency, adds regularization, or weakens the task. Search becomes easier because capability or effective freedom is reduced.

### Relay mechanism

The method introduces intermediate maps, interfaces, states, representations, constraints, verifiers, modules, distributions, or compositional stages that create or transport routes to an unchanged meaningful endpoint. Its benefit survives controls showing that it is not explained by lower capability, extra information, extra computation, extra supervision, a relaxed endpoint, or a smaller effective search space.

The preferred contribution is a relay mechanism. A candidate is not rescued by calling a restriction a “relay.” Functionally classify it.

For every shortlisted candidate, provide an **invariance ledger** covering:

- final objective and success criterion;
- attainable output/solution set;
- best attainable utility at high budget;
- model and parameter capacity;
- total test-time and training compute;
- number of model/environment calls;
- data and supervision;
- information available to the method;
- horizon, executed steps, and opportunities to replan;
- energy/action/path-length or analogous resource quantities;
- wall-clock and memory budget.

Prefer comparisons in which the direct and relay systems have exactly the same attainable final solution set and comparable dimension. When exact equality is impossible, quantify the mismatch and design controls that can falsify a capability-reduction explanation. A vague claim of “approximately matched capacity” is not enough.

## 4. Forbidden easy answers

Do not select a primary direction whose headline can be reduced to any of the following:

- an intermediate value of a hyperparameter is optimal;
- less control, less data, fewer tokens, fewer dimensions, lower rank, or more smoothing acts as regularization;
- action chunking or temporal abstraction improves long-horizon behavior;
- curricula, subgoals, or intermediate supervision help difficult tasks;
- adding noise or constraints sometimes helps;
- a learned selector chooses among existing representations;
- a new metric correlates with performance;
- a larger benchmark study confirms a familiar trade-off;
- a method wins because it performs more search, uses extra calls, sees privileged information, or weakens the endpoint;
- the same old mechanism is moved to a fashionable application such as VLA, LLM agents, diffusion, or world models.

These topics may appear as baselines or eliminated directions. They may become part of a candidate only if the candidate makes a stronger functional claim that survives the invariance ledger and is not predictable from the familiar explanation.

## 5. Required surprise standard

Every serious candidate must specify:

- **Default expert belief B:** what a well-informed researcher would predict after seeing the full fair setup;
- **Counterprediction P:** a result that is not a disguised monotonic or inverted-U tuning curve;
- **Relay mechanism M:** a mathematical, geometric, statistical, information-theoretic, optimization, causal, or algorithmic explanation;
- **Decisive falsifier F:** a cheap result that would refute M rather than merely show weak average performance;
- **Restriction control R:** the strongest experiment showing that the effect is not compression, smoothing, capacity loss, regularization, or task relaxation;
- **Prior-art collision test C:** the closest functional duplicate and the exact difference in problem, mechanism, and decisive evidence.

Reject rhetorical surprise. Ask whether a skeptical expert could predict the qualitative result before seeing any data. If yes, the candidate needs a stronger claim or must be eliminated.

## 6. Search scope and adversarial novelty audit

Search continuously rather than selecting an idea first and collecting supportive citations later.

1. Cover work through the current retrieval date, emphasizing 2023–2026 and tracing foundational work backward.
2. Search primary and official sources whenever possible: OpenReview, PMLR, NeurIPS proceedings, ACL Anthology, CVF, AAAI/IJCAI proceedings, RSS, journal pages, arXiv for recent preprints, and official repositories/project pages.
3. Search by function, not by the billiard metaphor. Build a synonym and mechanism map including success preimages, capture/attraction basins, predecessor and reachable sets, funnels, initiation sets, set-valued subgoals, continuation/homotopy, sequential Monte Carlo, multistage sampling, bridge variables, auxiliary variables, compositional search, intermediate verification, latent interfaces, modular inference, variable splitting, redundant parameterization, error-correcting computation, trajectory stitching, and terms discovered during search.
4. Search across planning, reinforcement learning, generative modeling, test-time computation, program synthesis, theorem proving, code generation, neural optimization, representation learning, causal learning, graph learning, diffusion/flow models, world models, agents, and other AI areas. Do not force any named area.
5. For each candidate, actively attempt to prove it already exists using alternative terminology, neighboring fields, related-work sections, citation graphs, and the newest conference records.
6. Functional duplication takes precedence over title similarity. Compare inputs, outputs, invariants, objective, algorithm, mechanism, theoretical statement, and empirical conclusion.
7. Verify title, authors, year, venue/status, and direct link for every cited work. Mark preprints and under-review work accurately. Never invent a paper, benchmark, implementation, or result.
8. Distinguish verified facts, literature-supported judgments, inferences, and untested hypotheses.
9. For each shortlisted candidate, list at least eight closest works. For the primary candidate, perform deeper backward/forward tracing and an explicit search of ICLR, ICML, NeurIPS, AAAI, IJCAI, ACL, EMNLP, CVPR, ICCV, ECCV, CoRL, RSS, L4DC, TMLR, and relevant journals.

An absence of search results is not proof of novelty. State residual uncertainty.

## 7. Candidate generation

Generate 15–25 candidates spanning genuinely different mechanisms and AI subfields. Do not count application swaps or renamed variants as separate candidates.

For each candidate, first classify it as:

- genuine relay;
- likely restriction disguised as relay;
- unclear and requiring a discriminating test.

Then score it from 1 to 10 on:

- functional novelty;
- strength of non-obvious prediction;
- fidelity to the original seed;
- invariance/control quality;
- mechanism clarity;
- cheap falsifiability;
- availability of authoritative benchmarks and strong baselines;
- feasibility with the fixed hardware;
- probability that experiments teach something beyond a tuning curve;
- top-tier reviewer risk;
- plausible breadth if the mechanism works.

Eliminate aggressively. A NO-GO outcome is preferable to a polished but predictable paper.

## 8. Fixed practical constraints

The available compute is exactly:

- 8 NVIDIA RTX 4090 GPUs;
- 24 GB VRAM per GPU;
- no NVLink and no assumption of pooled 192 GB memory;
- independent tasks, seeds, methods, and sweeps can run in parallel;
- heavy computation should run on GPUs;
- no additional cloud compute may be assumed.

The project should also satisfy:

1. No real robot or physical hardware requirement.
2. No expensive proprietary API, private dataset, large human-labeling effort, or long data-collection campaign.
3. Prefer public authoritative datasets, standard benchmarks, and strong open-source baselines.
4. The first decisive pilot should finish in 1–3 days after setup.
5. Prefer a full experimental package feasible in several weeks, not a foundation-model-scale campaign.
6. Avoid model parallelism when independent parallel runs are possible.
7. State realistic VRAM, GPU-hours, storage, RAM, engineering time, and wall-clock estimates.
8. The final contribution must be AI/computer science. It may use simulation, compact open models, offline datasets, or state-based environments.

An ICLR Oral is an aspirational quality bar, not a promised outcome. Explicitly distinguish:

- a workshop-level observation;
- a solid main-conference contribution;
- evidence that could make a paper a standout candidate.

Do not confuse more experiments with higher conceptual novelty.

## 9. Shortlist requirements

Narrow to 3–5 candidates, then recommend one primary and two backups only if they pass all gates.

For every shortlisted candidate provide:

1. One-sentence research question.
2. One-sentence counterintuitive headline result.
3. Formal direct-versus-relay setup.
4. Invariance ledger.
5. Explanation of why the mechanism is not restriction/regularization.
6. Minimal mathematical or algorithmic model.
7. Real relationship to the billiard seed.
8. Closest-work table with functional differences.
9. Three strongest rejection arguments.
10. A 1–3 day mechanism-discriminating pilot.
11. Benchmarks, datasets, metrics, and baselines.
12. Essential fairness controls and ablations.
13. Per-run VRAM, GPU-hours, run count, storage/RAM, and eight-GPU wall time.
14. Exact kill criteria.
15. What result would force reclassification from relay to restriction.
16. What evidence is needed for workshop, main conference, and standout status.

## 10. Primary-direction standard

Do not recommend a primary direction unless all of these gates pass:

- **Re-abstraction gate:** it preserves the relay question rather than collapsing into dimensionality tuning.
- **Novelty gate:** no functional duplicate is found after adversarial search.
- **Invariance gate:** capability, final objective, information, and compute are credibly matched.
- **Surprise gate:** an informed expert cannot trivially predict the qualitative result from a familiar trade-off.
- **Mechanism gate:** an experiment can distinguish the proposed relay explanation from restriction and regularization.
- **Pilot gate:** the mechanism can be killed within 1–3 days.
- **Benchmark gate:** recognized datasets and strong baselines exist.
- **Compute gate:** the full plan fits 8x24 GB GPUs without memory pooling.
- **Breadth gate:** if true, the mechanism plausibly transfers beyond one benchmark or application wrapper.
- **Story gate:** the paper has a clean problem → anomaly → mechanism → method → evidence chain.

If no candidate passes, output **NO-GO: RE-ABSTRACTION NOT YET ACHIEVED** and explain what unresolved theoretical question must be solved before experiments should begin.

## 11. Primary execution blueprint

If a primary candidate passes, provide:

- provisional title and central claim;
- three or four genuine scientific contributions;
- direct-versus-relay diagram described in text;
- mathematical definitions, objective functions, and predicted regimes;
- a mechanism-identification experiment, not merely a leaderboard comparison;
- strongest restriction, random-relay, capacity-matched, compute-matched, and information-matched controls;
- exact public datasets and official/open implementations;
- strongest nearest-neighbor baselines;
- one-day pilot, three-day pilot, and full experiment matrix;
- eight-GPU scheduling plan;
- statistical tests, confidence intervals, seed policy, and multiplicity controls;
- robustness and out-of-distribution tests;
- negative-result interpretation that does not permit narrative escape;
- stop conditions and fallback candidates;
- plausible venue fit without promising acceptance or Oral selection.

The first experiment should test the existence of the relay effect under invariance constraints. Do not begin by building a complex method.

## 12. Final deliverable

Return exactly one self-contained Markdown document named:

`AI_RESEARCH_REABSTRACTION.md`

If file creation is supported, create the file directly. Otherwise return the complete Markdown content in one final response. Do not add greetings, progress narration, or commentary outside the document.

Use at least this structure:

1. `# Executive Verdict`
2. `# Forensic Audit of the BFAP Formalization`
3. `# The Preserved Core: Restriction versus Relay`
4. `# Search Strategy, Synonym Map, and Coverage`
5. `# Literature Landscape`
6. `# Eliminated Predictable Directions`
7. `# Candidate Generation and Relay Classification`
8. `# Candidate Scorecard`
9. `# Shortlist Deep Dives`
10. `# Invariance Ledgers`
11. `# Adversarial Novelty Audit`
12. `# Primary Recommendation or NO-GO`
13. `# Minimal Mechanism-Discriminating Pilot`
14. `# Full Experimental Blueprint`
15. `# Dataset and Baseline Inventory`
16. `# Compute and Wall-Clock Budget for 8x RTX 4090`
17. `# Fairness Controls, Statistics, and Kill Criteria`
18. `# Paper Narrative and Venue Fit`
19. `# Two Backup Directions`
20. `# Verified Bibliography`
21. `# Search Log`

The document must be understandable and auditable without access to this conversation. Record retrieval date, databases/sites, major queries, covered years, and unresolved search gaps. Place citations near supported claims and include a deduplicated bibliography with direct links.

Do not reveal private chain-of-thought. Provide concise reasoning summaries, equations, evidence tables, falsifiers, and decisions that another researcher can independently inspect. Continue autonomously after starting. Ask a question only if missing information would materially change the entire investigation; otherwise make and record a reasonable assumption.
