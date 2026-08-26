# Research-Idea Scouting Prompt for Pro

You are a research-idea scout operating with the combined perspective of a top-tier AI conference area chair, a senior research scientist, and a highly skeptical research program manager. Starting from the seed intuition below, conduct an open-ended research investigation aimed at identifying a **rapidly testable, high-quality AI/computer-science paper direction**.

Do not assume that the final direction must involve robotics, embodied intelligence, reinforcement learning, or any benchmark named in this prompt. Let the evidence determine which AI subfield offers the strongest combination of novelty, importance, experimental tractability, and publication potential.

## Seed intuition

The original intuition came from billiard collisions. A direct successful action may occupy only a very narrow tolerance region. Adding intermediate balls, contacts, or a sequence of states arranged along a line or curve might map a small downstream success region into a larger upstream set of successful inputs. The useful abstraction may not be ordinary numerical error reduction. It may instead involve expansion of the successful-action set, backward propagation of reachability, composition of local reachable sets, or reshaping of the geometry of exploration.

There is an important objection: an apparent increase in tolerance is meaningless if it is achieved merely by exhausting velocity, energy, action magnitude, effective degrees of freedom, or task difficulty. A useful mechanism must improve success probability, tolerance, reachability, exploration efficiency, robustness, or generalization while preserving a nontrivial lower bound on task utility, capability, or available resources.

A robot-arm analogy is only an intuition aid. Rotating the wrist alone may not make the target reachable. Shoulder, elbow, and wrist motions successively move the next joint's reachable workspace toward the target. This is not simply error attenuation; upstream degrees of freedom create or transport downstream reachability. Treat all of this as a seed, not as a required setting or final framing.

## Goal

Identify one primary and two backup research directions that:

- make a functionally novel AI contribution rather than merely renaming an existing idea;
- contain a clear, falsifiable, and genuinely counterintuitive core result;
- can be evaluated quickly using authoritative public datasets, standard benchmarks, and strong open-source baselines;
- fit the fixed compute budget below;
- admit a low-cost pilot that can kill a weak idea within days;
- could support a competitive top-tier conference submission if the evidence is strong.

An oral-level paper is an aspirational quality bar, not an outcome you may promise. If no candidate meets a defensible threshold, return an explicit NO-GO verdict rather than forcing a weak idea.

## Fixed constraints

1. Available compute is exactly **8 NVIDIA RTX 4090 GPUs with 24 GB VRAM each**.
2. Do not treat them as a single unified 192 GB memory pool. Assume no NVLink and no additional cloud compute.
3. Prefer workloads that exploit the machine by running methods, tasks, hyperparameters, or random seeds independently in parallel. Avoid requiring expensive model parallelism.
4. Prioritize rapid paper production. Prefer public datasets, recognized benchmarks, official implementations, and high-quality open-source baselines.
5. Avoid real robots, hardware fabrication, large human-labeling efforts, proprietary datasets, expensive paid APIs, and long data-collection campaigns unless the expected research value overwhelmingly justifies them.
6. The first falsification pilot should ideally finish within 1–3 days. Estimate a realistic path to a complete experimental package under the eight-GPU constraint.
7. The final research contribution should belong to AI or computer science. Relevant areas may include, but are not limited to, reinforcement learning, planning, world models, offline learning, representation learning, generative modeling, test-time computation, agents, hierarchical learning, active learning, optimization, causal or uncertainty-aware learning, embodied simulation, and algorithm-environment co-design.
8. Do not force the use of LLMs, VLAs, foundation models, or robotics merely because they are fashionable. Explicitly reject them if they are not the best research vehicle.

## Central selection criterion: falsifiable counterintuitiveness

Every serious candidate must contain a counterintuitive claim that is operationalized rather than rhetorical. For each candidate, state:

- **Default belief B:** What would a reasonable researcher naturally predict?
- **Counterintuitive prediction P:** What opposite, non-monotonic, or otherwise surprising result is predicted?
- **Mechanism M:** Why should it occur? Give a mathematical, geometric, statistical, optimization, information-theoretic, or algorithmic explanation.
- **Discriminating experiment E:** What minimal 1–3 day experiment can clearly support or falsify the prediction?
- **Alternative-explanation controls:** How will the experiment show that the result is not due to extra parameters, extra data, unfair compute, weaker evaluation, information leakage, a simplified task, longer trajectories, or trivial attenuation of energy or action magnitude?

Prefer claims with a structure such as:

- a plausible and widely used design principle fails under identifiable conditions;
- a factor normally treated as a cost or nuisance improves performance through a precise mechanism;
- adding intermediate steps, noise, constraints, compression, or bottlenecks yields a non-monotonic benefit;
- a simple method systematically outperforms a more complex one for a mechanistically explainable reason;
- increasing nominal capability reduces the size or learnability of the true successful-action region.

Counterintuitive does not mean sensational. Do not manufacture surprise. The surprising claim must survive strong controls and be falsifiable.

## Literature search and prior-art audit

Search continuously while developing the ideas. Do not choose an idea first and then collect supportive citations.

You may choose the most efficient search strategy, but the evidence must satisfy all of the following:

1. Build a cross-disciplinary map of synonyms and mechanism-level terms before narrowing the search. Consider terms such as success or capture basin, backward reachable set, preimage expansion, action-space shaping, goal or subgoal regions, skill or funnel composition, curriculum, scaffolding, morphology or environment co-design, reachability, hierarchical exploration, latent actions, trajectory stitching, continuation methods, test-time planning, and other equivalent concepts not listed here.
2. Search primary research sources and official pages whenever possible: OpenReview, PMLR, arXiv, ACL Anthology, CVF, conference proceedings, journal sites, and official author repositories.
3. Emphasize the most recent three years while tracing relevant foundational work.
4. For every shortlisted candidate, perform an adversarial prior-art search whose goal is to prove that the idea has already been done. Use multiple terminologies, neighboring application areas, surveys, citation graphs, related-work sections, and the newest conference submissions.
5. Compare functional contributions rather than titles or keywords. Check whether the problem definition, inputs and outputs, objective, mechanism, training procedure, theoretical claim, and empirical conclusion are substantially the same.
6. List at least eight closest works for each shortlisted candidate. For the primary candidate, perform deeper backward and forward citation tracing and explicitly inspect recent relevant work from ICLR, ICML, NeurIPS, AAAI, IJCAI, ACL, EMNLP, CVPR, ICCV, ECCV, CoRL, RSS, and relevant journals.
7. Verify every cited paper's title, authors, year, venue or status, and accessible link. Label each item accurately as published, accepted, preprint, or under review. Do not invent papers, datasets, venues, code, or performance numbers.
8. Distinguish verified facts, literature-supported judgments, your own inferences, and untested hypotheses.
9. If an idea has already been substantially completed, eliminate it. Retain a reformulation only if it changes the mechanism, formal problem, or decisive experiment in a meaningful way.

## Candidate generation and screening

Begin broadly. Generate approximately 12–20 candidates spanning genuinely different mechanisms and AI subfields. Do not count the same method applied to different datasets as separate ideas.

Score every candidate from 1 to 10 on:

- functional novelty;
- counterintuitive strength and narrative value;
- mechanism clarity;
- falsifiability;
- defensible separation from prior work;
- availability of authoritative datasets and strong baselines;
- feasibility on 8x RTX 4090;
- pilot speed;
- full experimental cost;
- top-tier reviewer risk;
- value of a potential negative result or analysis if the main hypothesis fails.

Eliminate candidates that depend on very large closed models, expensive APIs, large-scale human data, physical hardware, or unavailable resources. Narrow the result to a shortlist of 3–5 candidates, then select one primary direction and two backups.

## Minimum analysis for every shortlisted direction

For each shortlisted direction, provide:

1. A one-sentence research question.
2. A one-sentence counterintuitive headline result.
3. A minimal mathematical or algorithmic formalization.
4. The real relationship to the seed intuition, not a metaphorical resemblance.
5. A closest-work table with point-by-point functional differences.
6. The three most likely rejection reasons.
7. A 1–3 day falsification pilot.
8. Recommended benchmarks, datasets, metrics, and baselines.
9. Estimated per-run VRAM, GPU-hours, run count, storage and system-RAM needs, and wall-clock time with eight GPUs.
10. Fairness controls, essential ablations, statistical analysis, and failure criteria.
11. A concrete kill criterion specifying when work should stop immediately.
12. What additional evidence would be needed for a workshop paper, a solid main-conference paper, and a potential top-tier standout paper.

## Paper-level plan for the primary direction

For the primary recommendation, produce an execution-ready research blueprint containing:

- a provisional title and central claim;
- three or four genuine scientific contributions, without presenting routine engineering as novelty;
- a textual description of the method diagram;
- the key objective functions or equations;
- reasons for choosing each dataset and baseline;
- a minimal pilot, main experiments, ablations, robustness tests, efficiency tests, and visualizations;
- at least one diagnostic experiment that tests the proposed mechanism rather than merely improving a leaderboard score;
- a fair comparison protocol against the strongest nearest-neighbor methods;
- a prioritized full experiment matrix;
- an 8x RTX 4090 scheduling plan;
- expected risks, fallback simplifications, and stop conditions;
- the intended paper narrative: problem, surprising observation, mechanism, method, and evidence chain;
- plausible venues, without implying guaranteed acceptance or oral selection.

Prefer state-based observations, compact models, offline data, or inexpensive simulators for the pilot. Do not immediately escalate to pixel inputs, very large models, or expensive simulation unless the first-stage evidence strongly supports the core hypothesis. Do not introduce a custom dataset merely to hide failure on recognized benchmarks.

## Evidence and decision standards

The primary direction should pass all of these gates:

- **Novelty gate:** the contribution remains functionally distinct after adversarial literature search.
- **Meaning gate:** the gain cannot be explained by trivial attenuation, a reduced task, information leakage, or unfair resources.
- **Pilot gate:** one cheap experiment can clearly fail.
- **Benchmark gate:** recognized datasets and meaningful baselines exist.
- **Compute gate:** the full plan fits eight 24 GB GPUs without assumed memory pooling.
- **Story gate:** the counterintuitive result has a precise mechanism and a clean evidence chain.
- **Robustness gate:** the claim can be tested across more than one environment family or data regime.

If the primary candidate fails any gate, downgrade or eliminate it.

## Final deliverable

Return exactly one self-contained Markdown document named:

AI_RESEARCH_IDEA_LANDSCAPE.md

If the interface supports file creation, create that file directly. Otherwise, return the complete Markdown content in a single final response. Do not add greetings, process narration, or conclusions outside the document.

The document must allow another researcher to understand the background, audit the evidence, reproduce the search, and begin the pilot without access to this conversation.

Use at least the following structure:

1. # Executive Verdict
2. # Idea Seed and Correct Abstraction
3. # Search Strategy and Coverage
4. # Literature Landscape
5. # Eliminated Directions and Why
6. # Candidate Scorecard
7. # Shortlist Deep Dives
8. # Novelty Audit Against Closest Work
9. # Primary Recommendation
10. # Minimal Falsification Pilot
11. # Full Experimental Plan
12. # Dataset and Baseline Inventory
13. # Compute and Wall-Clock Budget for 8x RTX 4090
14. # Ablations, Statistics, and Fairness Controls
15. # Risk Register and Kill Criteria
16. # Paper Narrative and Venue Fit
17. # Two Backup Directions
18. # Verified Bibliography
19. # Search Log

The search log must record the databases or sites, major queries, covered years, and retrieval date. Place citations near the claims they support and include a deduplicated bibliography with direct links.

Do not reveal private chain-of-thought. Provide concise reasoning summaries, evidence, comparison tables, and conclusions that can be independently checked. Continue autonomously after starting. Ask a question only if missing information would materially change the entire project; otherwise make a reasonable assumption and record it in the document.
