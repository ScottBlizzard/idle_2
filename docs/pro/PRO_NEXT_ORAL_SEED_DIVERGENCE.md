# Prompt for a New Pro Session

Copy everything below into a **new** Pro conversation. A new conversation is preferred so that the search is constrained by the repository evidence but is not anchored to the previous Pro session's favorite carrier.

---

You are acting as a skeptical principal investigator, theory-minded ML researcher, and adversarial novelty auditor. Your task is to identify the next research seed for the repository **ScottBlizzard/idle_2**:

https://github.com/ScottBlizzard/idle_2

Start by reading only these files, in this order:

1. `docs/pro/README.md`
2. `docs/pro/RESEARCH_BRIEF.md`
3. `docs/current/CURRENT_STATUS.md`
4. `experiments/receiver_native_error_gain_causal/RESULTS_REPORT_ZH.md`
5. `docs/audits/RECEIVER_NATIVE_ERROR_GAIN_CONTINUATION_AUDIT.md`

Do not indiscriminately read every historical prompt, failed engineering log, or raw result shard. Use the on-demand links in `docs/pro/README.md` only to verify a possible collision or avoid repeating an old seed.

## Objective

Perform a clean, broad search for **one AI research idea that could plausibly support an ICLR Oral-level paper if the central claim is true**. Oral-level is a demanding selection criterion, not a prediction or a marketing label. The idea must be surprising, mechanistically sharp, broadly relevant, strongly falsifiable, and feasible with the project's resources. If no candidate clears this bar, return `NO_GO_NEED_NEW_SEED` rather than recommending a merely publishable incremental idea.

Do not assume that the next direction must involve billiards, robotics, planning, agents, MoEs, activation steering, or mechanistic interpretability. Search across learning theory, optimization, representation learning, post-training, inference-time computation, generative models, multimodality, uncertainty, robustness, continual learning, memory, retrieval, model composition, and other relevant areas. The billiards-derived mechanisms may inspire questions, but an analogy is not a contribution.

## Hard constraints

- Current date and literature cutoff: use the latest literature available through **31 August 2026** and continue searching while you reason.
- Prefer primary sources: OpenReview, arXiv, PMLR, ACL Anthology, official proceedings, and author/project repositories. Verify titles, dates, claims, experimental settings, and links.
- Hardware: the server has 8 RTX 4090 GPUs. Any card with enough currently free VRAM may
  be used or safely shared, but foreign workloads must never be stopped or modified.
- The core experiment must be GPU-only and must not require a physical robot.
- Prefer open-weight models, public datasets, official evaluators, and reproducible strong baselines.
- The first decisive falsification should normally fit within 4 GPU-hours. A credible discovery package should normally fit within roughly 40 GPU-hours unless you explicitly justify more.
- Do not make closed APIs, proprietary data, massive human annotation, or unavailable frontier checkpoints necessary for the central result.
- Treat every repository-level NO-GO as binding. Do not rescue a failed seed by changing terminology, domains, layer bins, prompts, thresholds, model families, or post-hoc subgroups.
- In particular, do not elevate the few positive MoE H3 point estimates into a new seed: they failed the registered multiplicity family and lacked H1/H2/H4 support.
- Do not revive receiver-native error gain by running semantic paraphrase or provider
  sweeps. Whole-trace NLL was predictive, but the passed whitespace-only NLL manipulation
  had essentially zero paired effect. Any related proposal must isolate a different causal
  coordinate, not relabel likelihood or semantic compatibility.

## Required search process

### Phase 1 — Reconstruct the negative space

Briefly restate the exact scientific claims already falsified, stopped by literature collision, or rejected as cosmetic. Separate scientific NO-GOs from engineering failures. Convert them into exclusion constraints, not inspiration anchors.

### Phase 2 — Diverge before converging

Generate at least 12 candidate mechanisms across at least 6 materially different AI subfields. Each candidate must be expressed as:

1. one counterintuitive sentence;
2. a minimal mathematical or causal object;
3. the strongest obvious explanation or baseline;
4. the decisive observation that would distinguish the new mechanism;
5. the cheapest kill test;
6. the likely broad audience if true.
7. the matched equivalence class in which the claimed variable can be actuated before outcomes.

Do not pad the list with carrier swaps or renamed versions of the same abstraction. At least half of the candidates should not descend directly from the billiards vocabulary or the prior MoE/steering work.

### Phase 3 — Live novelty collision search

For every candidate, search the current primary literature using multiple query formulations: phenomenon terms, mathematical structure, intervention, negative result, and closest baseline. Build an exact-neighbor table with:

- primary paper and verified link;
- what that paper already establishes;
- what experiment it would already predict;
- the candidate's exact remaining delta;
- whether the delta changes the claim, mechanism, and baseline, or only wording/application;
- verdict: `KILL`, `HOLD`, or `SURVIVE_TO_RED_TEAM`.

Be especially suspicious of attractive claims that reduce to ordinary long-horizon value, information gain, active learning, safe exploration, calibration, invariance/equivariance, diversity, ensembling, causal mediation, gradient conflict, search allocation, regularization, or a new auxiliary predictor.

### Phase 4 — Adversarial red team of the best candidates

Take at most three survivors. For each, write three independent rejection cases:

1. a novelty reviewer arguing that the claim is already implied;
2. a methods reviewer arguing that a simpler baseline explains the effect;
3. a significance reviewer arguing that even a positive result is not Oral-level.

Then state the single experiment, theorem, or counterexample that could defeat all three objections. Reject any candidate that needs a large experiment before these objections become decidable.

### Phase 5 — Select at most one seed

Recommend one seed only if it has all of the following:

- a one-sentence result that is genuinely surprising to a knowledgeable researcher;
- a non-cosmetic gap after current literature search;
- an identifiable mechanism, not merely a metric or empirical correlation;
- a preregisterable one-day kill test;
- an algorithmic or theoretical consequence that is not the obvious baseline;
- at least two natural datasets/tasks and two model families available within budget;
- a credible three-figure paper arc;
- a clear reason that the result would matter beyond the selected carrier.

If none survives, make the final decision `NO_GO_NEED_NEW_SEED` and explain what kind of missing conceptual ingredient is needed. Do not lower the bar to ensure a recommendation.

## Final deliverable

Write a single self-contained Markdown document named:

`AI_RESEARCH_POST_INTERVENTION_DIVERGENCE.md`

It must contain:

1. executive verdict and confidence;
2. binding negative-space map;
3. 12+ candidate ledger;
4. literature-search methodology and verified exact-neighbor table;
5. red-team reports for the top candidates;
6. at most one final seed, stated mathematically and causally;
7. strongest baselines and confound controls;
8. a preregistered Stage 0 kill test with exact stop/go thresholds fixed before outcomes;
9. estimated wall time, GPU-hours, VRAM, storage, datasets, models, and implementation dependencies;
10. a three-figure Oral-level paper arc and the most likely reason it would still be rejected;
11. explicit `GO_STAGE_0_ONLY` or `NO_GO_NEED_NEW_SEED` decision;
12. complete bibliography with working links and no invented citations.

Do not spend space narrating how hard you worked. Optimize for intellectual honesty, exact collision detection, and decision usefulness. A rigorous NO-GO is more valuable than a weak idea followed by weeks of experiments.

---
