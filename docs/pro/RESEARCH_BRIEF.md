# Research Brief for the Next ICLR Seed

**Repository:** [ScottBlizzard/idle_2](https://github.com/ScottBlizzard/idle_2)  
**Brief date:** 30 August 2026

**Project state:** one theory-first falsifier; no authorized active paper seed

## 1. Mission

Find a new AI research seed whose central claim could plausibly support an ICLR Oral-level paper if it is true. “Oral-level” is a selection bar, not a promised outcome. The desired seed must combine:

1. a concise, counterintuitive empirical or theoretical claim;
2. a mechanism that rules out the most obvious explanation;
3. broad relevance beyond one prompt, model, benchmark, or implementation;
4. a decisive low-cost falsification test;
5. a credible path from the first figure to a complete paper under the available compute.

We do **not** need to preserve the billiards carrier, MoE routing, planning, agents, mechanistic interpretability, or any other prior domain. The billiards discussion is useful only insofar as it suggests transferable structures that survive a novelty audit.

## 2. Hard operating constraints

- Target venue: ICLR; a narrow incremental benchmark or tuning trick is insufficient.
- Hardware: an 8× RTX 4090 server exists, but the project is currently authorized to use only physical GPUs 4--7: at most four independent 24 GB cards concurrently.
- No physical robot dependency. GPU-only simulation is allowed only if it is fast, standardized, and scientifically necessary.
- Prefer open-weight models, public datasets, official evaluators, and strong reproducible baselines.
- The first kill test should normally fit within 4 GPU-hours. A serious discovery package should normally fit within roughly 40 GPU-hours unless a stronger justification is explicit.
- Do not rely on unavailable closed data, proprietary traces, human annotation at scale, or API-only frontier models for the core claim.
- Literature must be searched through the current date. Recent 2025--2026 arXiv/OpenReview work is especially important.
- A scientific threshold cannot be relaxed after looking at outcomes. Local positive cells from a failed registered family are not a new seed by default.

## 3. Binding negative space

The following families are closed for this project unless a proposed claim is demonstrably different in mechanism, intervention, and strongest baseline—not merely in terminology or application domain.

| Closed family | Binding reason | Do not revive it by |
|---|---|---|
| Controller-insensitive / viability-, reachability-, option-, or continuation-preserving planning | Broad formulations reduce to established robust planning, stochastic viability, reachability, empowerment, chance constraints, and long-horizon value | moving it to a new simulator, adding a scalar score, or renaming the continuation set |
| Resettable failure with retained learning | Agent rewind, iterative learning, verifier-guided repair, safe reset RL, and related work occupy the general mechanism | saying “failure is informative,” adding memory, or cost-matching retries |
| Decision-calibrated uncertainty for learned planners | A direct 2026 collision already shows calibrated model uncertainty can fail as a boundary-risk signal and that outcome-supervised failure prediction is stronger; surrounding risk-aware and conformal methods are mature | another calibration loss, uncertainty head, risk predictor, or benchmark transfer |
| Algorithmic prompting / inactive competing-operator interference | A local causal signal failed the binding wording transfer; other model families lacked admissible capability | more prompt packs, post-hoc model selection, or renaming interference |
| Generic error shaping into task-tolerant directions | Invariance, equivariance, covariance shaping, tangent geometry, and robust control already capture the broad principle | applying the same geometry to a fashionable carrier without a new law |
| Closed-loop bracket activation steering | At a fixed layer the proposed loop collapses to its final displacement; the operational intervention, theorem, and matched baseline case were missing, while neighboring commutator and nonlinear-steering work is occupied | demonstrating only order sensitivity, noncommutativity, quadratic scaling, or nonlinear steering |
| Counterfactual route non-compositionality in frozen MoEs | The complete registered Stage D experiment found no reproducible interaction law and no deployable compatibility predictor | rescuing selected H3 cells, changing layer bins, relaxing multiplicity, or adding models after the NO-GO |

Other heavily occupied regions already audited include retrieval redundancy/diversity, reasoning-sample genealogy, raw-versus-compressed agent memory, masked-diffusion commitment order, output-path diversity and SFT conflict, recoverability-weighted failed traces, ordinary model editing interference, and generic multi-agent critique.

The latest negative-space search additionally closes continuation-family scoring, diagnosable tool interfaces, failure-conditioned action value, redundancy-conditioned intervention strength, verifier-burden transfer, incumbent/insurance preservation, and downstream maintainability of currently successful patches as standalone headlines. See [`../audits/NEGATIVE_SPACE_ORAL_SEED_SEARCH.md`](../audits/NEGATIVE_SPACE_ORAL_SEED_SEARCH.md). These mechanisms may appear as components, but not as the claimed novelty without a distinct separating law.

A later three-track reassessment does not reopen those broad claims, but corrects the stronger statement that the snooker source is exhausted. It retains one theory-first question: under matched tools, model, tokens, and verification budget, can extra locally verifiable workflow nodes reverse the usual horizon penalty by removing a high-coupling error-propagation bottleneck? This is `ONE_THEORY_FIRST_HOLD`, not an active seed. It requires a prospectively estimable propagation gain and a separation theorem beyond AgentEval/CoT2Graph features before any GPU work. See [`../audits/SNOOKER_DEEP_MECHANISM_REASSESSMENT.md`](../audits/SNOOKER_DEEP_MECHANISM_REASSESSMENT.md).

## 4. Current sole falsifier: the diagonal is not a scaling law

The current candidate did not come from another direct snooker mapping. It begins from a
published inverse-scaling claim in self-correction. Existing comparisons often report

\[
P(\mathrm{repair}\mid\text{generator}=\text{corrector}=m,
\text{ model }m\text{ initially failed}).
\]

This diagonal statistic mixes repair competence, the difficulty distribution of errors
that survive each generator, and self/other role gating. A deterministic model in
[`../theory/ENDOGENOUS_FAILURE_CONDITIONING_NOTE.md`](../theory/ENDOGENOUS_FAILURE_CONDITIONING_NOTE.md)
constructs strict positive scaling at every fixed difficulty while own-failure correction
strictly decreases. The common-error-bank ranking has the opposite sign.

Selection bias alone is not an Oral contribution. The only high-ceiling residual is
**relational error depth**: after holding the exact error and wrapper fixed, error
repairability may depend on the generator--corrector pairing because related models share
blind spots. A weaker complementary corrector may then repair an error that a stronger
related corrector cannot. This must survive direct comparison with ICLR 2026 *Variation in
Verification*, COLM 2026 *Self-Correction Bench*, controlled role-label studies, and ICML
2025 *Correlated Errors in Large Language Models*.

The public `YefanZhou98/LLMVerify-Generator` bundle already supplies about 619,000 labeled
trajectories from 15 generators. A frozen 4×4 crossed-repair pilot is specified in
[`../../experiments/endogenous_failure_conditioning/PILOT_PROTOCOL.md`](../../experiments/endogenous_failure_conditioning/PILOT_PROTOCOL.md).
Promotion requires a stable generator-family-by-corrector-family interaction and a
held-out equal-call-budget complementarity router gain. A standardized ranking reversal
without those results is only an audit.

## 5. Latest completed experiment: what it actually teaches

The frozen-MoE Stage D study completed successfully on 64 retained GSM8K and 64 retained MATH-500 trajectories. It tested four layer-pair regimes and four registered hypotheses:

- H1/H2: directional reversal excess beyond matched nulls;
- H3: equal-budget advantage of direct joint selection over independently selected local routes;
- H4: out-of-sample prediction of route compatibility from deployment-available features.

The automatic result was `NO_GO_NO_INTERACTION_LAW`:

- 0/4 regimes passed H1--H4 on both datasets; the requirement was at least 3/4.
- H1/H2 effects were generally near zero.
- A few H3 point estimates were positive, but none survived the full 32-test family.
- H4 Spearman correlations ranged from `-0.063` to `0.040`, versus a frozen requirement of at least `0.40`.
- The successful run took about 3.13 hours and passed the compute gate.

Therefore the failure is scientific, not a lack of compute or engineering completion. The useful meta-lesson is that a visually appealing analogy can produce a precise intervention yet still lack a stable population-level law. The next seed must earn its mechanism before receiving more scale.

## 6. Source intuitions that remain available—but are not claims

The snooker discussion generated several useful question forms. They may inspire candidates but confer no novelty:

- A longer or apparently more complex path can align execution variation with a broad acceptable set rather than reduce total error.
- A locally harder action can preserve safer downstream branches.
- External state can reset while internal knowledge accumulates.
- Adding control dimensions can make execution less reliable because magnitude, direction, and system response become coupled.
- In highly uncertain multi-body interactions, control may shift from predicting a unique microstate to shaping a macro-event distribution.
- Experts often delay an irreversible or high-variance intervention until an initiation region and a fallback are both available.
- The best action may be one whose failure state remains strategically favorable, not merely one with maximum immediate success probability.

Each of these is already adjacent to mature literatures. A candidate is valuable only if it exposes a narrower contradiction, missing law, identifiable failure mode, or algorithmic consequence that current formalisms and direct baselines do not absorb.

## 7. Required idea bar

A candidate should be rejected unless it can answer all of the following:

1. **Surprise:** What is the one-sentence result that a knowledgeable reviewer would not already expect?
2. **Mechanism:** What observable or theorem distinguishes the proposed cause from ordinary capacity, optimization, variance, calibration, scaling, or distribution shift?
3. **Closest collision:** Which three to five primary papers come closest, and what exact experiment would they already predict?
4. **Non-cosmetic delta:** Does the proposal change the scientific claim, intervention, and winning baseline—or only the vocabulary/carrier?
5. **Killability:** What preregistered result would make us stop in one day?
6. **Algorithmic consequence:** If the phenomenon is true, what method follows that is not an obvious extra predictor, reweighting rule, search heuristic, or regularizer?
7. **Breadth:** Why should researchers outside the chosen benchmark care?
8. **Paper arc:** What are the likely first three figures, and how do they build one argument rather than a benchmark collection?

An idea that is merely publishable, fashionable, or easy to run should still be rejected. Conversely, a risky idea is acceptable if the first test is cheap and the upside is genuinely high.

## 8. Desired output from the next scout

The scout should first diverge across multiple AI subfields, then independently kill weak candidates through current literature, theory, and baseline analysis. It should recommend **at most one** seed for experiment. `NO_GO_NEED_NEW_SEED` is a valid and preferred answer if nothing clears the bar.

The final deliverable must be a single self-contained Markdown document, not scattered chat notes.
