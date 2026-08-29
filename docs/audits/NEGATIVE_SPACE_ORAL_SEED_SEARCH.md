# Negative-Space Search for a New Oral-Level Seed

**Date:** 30 August 2026

**Decision:** `NO_ORAL_SEED_FOUND`

**GPU authorization:** `0 GPU-hours`

**Strongest residual:** `CLOSED_BY_DIRECT_DOWNSTREAM_MAINTAINABILITY_COLLISION`

## Executive decision

This search did not find a new hypothesis that clears the project's Oral-level novelty bar. The result is not that the snooker discussion lacks useful structure. The result is that its most reusable structures already map cleanly onto mature AI concepts, while the one initially plausible residual—two currently correct code patches having different future editability—now has a direct 2026 controlled-study collision.

No experiment is authorized. The correct next move is a new contradiction-first search outside the occupied abstractions below, not a GPU sweep, a new carrier for the same principle, or another Pro prompt anchored on the billiards vocabulary.

## 1. Search method

The search deliberately began from the remaining source mechanisms rather than from fashionable AI subfields:

1. preserve a family of good continuations rather than only present success;
2. make failures diagnosable or safe rather than merely less frequent;
3. adapt intervention strength to redundancy in the remaining state;
4. control a macro-outcome when micro-outcomes are unpredictable;
5. force another agent or verifier to bear the difficult resolution step;
6. prefer a longer natural route whose variation lies inside an acceptable corridor;
7. distinguish states that have equal present value but unequal future editability.

For each translation, the test was not whether the exact phrase had appeared before. The test was whether the central phenomenon, intervention, and strongest baseline were already predicted by existing work. Nearby literature was classified as a direct collision, positive adversary, foundation, mandatory baseline, or unexplained anomaly.

## 2. Candidate ledger

| Candidate translation | Intended surprise | Closest occupied work | Decision |
|---|---|---|---|
| Continuation-family robustness | Equal present answer probability can hide a different number of independent successful continuations | RLTR explicitly truncates reasoning prefixes and measures whether another model can continue them; semantic-coverage work discounts redundant traces and selects a coverage portfolio | `KILL` |
| Diagnosable action interfaces | A lower-bandwidth interface can outperform a richer one because its errors reveal the correct correction direction | *Callability Is Not Operability* directly studies whether interfaces expose the state and semantics required for safe continuation under uncertainty | `KILL` |
| Failure-conditioned action value | Two actions with equal success probability differ because one failure state remains recoverable | Recoverability benchmarks and long-horizon planning already distinguish locally valid/currently successful actions by future completion feasibility | `KILL` |
| Redundancy-conditioned intervention strength | Aggressive intervention helps only when many fallback branches remain; sparse states require gentle intervention | Adaptive branching, semantic portfolio coverage, diversity-aware inference, and redundancy-aware pruning already predict the broad law | `KILL` |
| Macro self-averaging under random intervention | A stronger random intervention can make a macro-event more reliable even as individual outcomes become less predictable | Random pruning, wide-network concentration, ensemble/diversity, and population-control results make this a technical instance rather than a new AI law | `KILL` |
| Verifier-burden transfer | Among equally correct outputs, the better one makes errors easier for a weak verifier to detect | Prover-verifier games already optimize legibility and study correctness that is difficult for weaker verifiers to assess | `KILL` |
| Insurance-before-exploration | Preserve one reliable branch before a high-variance search step | Incumbent-preserving tree search, best-first/MCTS, rollback, and portfolio search already implement the mechanism | `KILL` |
| Future editability of present-equivalent patches | Two patches pass the same current tests, yet one causally makes later tasks harder | A 2026 controlled two-step PR-chain study directly measures downstream failures after agent- versus human-authored initial patches; SWE-CI, SWE-STEPS, RECAP, and patch-correctness work occupy the surrounding evaluation space | `KILL` |

## 3. Why the strongest apparent residual does not survive

### 3.1 Proposed residual

Let two patches \(p_1,p_2\) satisfy the same current task contract:

\[
T_0(p_1)=T_0(p_2)=1,
\]

and match on current semantic behavior, test coverage, static analysis, patch size, and conventional complexity. The proposed claim was that they could nevertheless have systematically different expected future edit cost:

\[
\mathbb{E}_{\tau\sim D_{future}}[C(\tau\mid p_1)]
\ne
\mathbb{E}_{\tau\sim D_{future}}[C(\tau\mid p_2)].
\]

This is an unusually faithful AI translation of the snooker idea that two current positions can be equally playable while differing in how broadly they support the next operation.

### 3.2 Initial identification problem

Historical future commits are not neutral counterfactuals. They were authored on top of the patch that actually entered the repository. Replaying them on a counterfactual patch mixes three effects:

- intrinsic editability of the initial patch;
- compatibility with a development path chosen after observing that patch;
- representational similarity to the human implementation on which later diffs were written.

Synthetic follow-up requests avoid literal diff replay but can silently encode the researcher's preferred abstraction and make the conclusion tautological. A credible design therefore needs downstream tasks fixed independently of which admissible initial patch is selected.

### 3.3 Direct collision

The residual is no longer merely adjacent to maintainability work. *Do AI Agents Write Less Maintainable Code Than Human Developers?* constructs controlled two-step pull-request chains in which the same dependent downstream task is attempted on top of either a human- or agent-authored initial implementation. It reports downstream resolve-rate drops and code-quality degradation after agent-authored code. This is the phenomenon and the key controlled intervention the residual intended to claim.

The narrower question—selecting the best future-editable patch among multiple currently correct agent patches—could still support a benchmark or method. It no longer supports the required headline novelty by itself. To become a new seed it would need a missing law that the two-step-chain result does not predict, plus a method that beats maintainability, minimality, complexity, technical-debt, and downstream-agent-evaluation baselines. No such law was found here.

## 4. Literature-role map

### Direct collisions

- [Beyond Correctness: Learning Robust Reasoning via Transfer](https://arxiv.org/abs/2602.08489): continuation of truncated reasoning prefixes is already an explicit robustness target.
- [Callability Is Not Operability: Controlled Interface Interventions for LLM Agents](https://arxiv.org/abs/2608.23628): controlled interface interventions already target the information needed for safe continuation.
- [Evaluating LLM Agents Beyond Local Edit Validity](https://openreview.net/pdf?id=bC0mNJcci4): evaluates whether a partially edited artifact remains completable, directly occupying recoverability beyond local success.
- [Do AI Agents Write Less Maintainable Code Than Human Developers?](https://openreview.net/pdf/27d79bcbcebc1802564722c5a2cb4f4aea638643.pdf): controlled dependent-PR chains directly occupy downstream maintainability of currently successful code.
- [Prover-Verifier Games improve legibility of LLM outputs](https://arxiv.org/abs/2407.13692): directly occupies the claim that correctness alone can make outputs harder for a weaker verifier to assess.

### Positive adversaries and mandatory baselines

- [Resource-Adaptive Foundation Model Reasoning via Semantic Coverage](https://openreview.net/pdf/6d04a89fd02babd4548353856256e3860580b43b.pdf): semantic rather than raw sample coverage is the correct adversary for any continuation-family or insurance-branch proposal.
- [Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search](https://arxiv.org/abs/2503.04412): mandatory baseline for redundancy-conditioned allocation of search effort.
- [On the Effect of Sampling Diversity in Scaling LLM Inference](https://proceedings.mlr.press/v337/wang26f.html): mandatory baseline for claims that diversity or branch redundancy changes test-time scaling.
- [SWE-CI](https://arxiv.org/abs/2603.03823) and [Beyond Isolated Tasks / SWE-STEPS](https://arxiv.org/abs/2604.03035): mandatory longitudinal baselines for any future code-editability claim.
- [RECAP](https://arxiv.org/abs/2608.13292): mandatory baseline for refinement, patch minimality, and the correctness--complexity tradeoff.

### Foundations

- Robust planning, stochastic viability, reachability, empowerment, chance constraints, and long-horizon value already formalize continuation-preserving action selection.
- Best-first search, MCTS, rollback, and anytime algorithms already formalize preserving an incumbent before risky exploration.
- Random pruning, concentration in wide networks, and ensemble methods already formalize micro-level uncertainty with macro-level stability.

### Unexplained anomalies

No anomaly survived that simultaneously had:

1. a precise contrast not predicted by the works above;
2. a causal intervention rather than a new scalar diagnostic;
3. a method-level consequence stronger than reweighting, reranking, or adding a predictor;
4. a credible first experiment under four RTX 4090 GPUs;
5. a plausible three-figure Oral-level paper arc.

## 5. Binding exclusions added by this search

Do not revive the following merely by changing the carrier:

- count or score successful reasoning continuations;
- prefer actions whose failures are recoverable;
- expose more action-relevant feedback through a tool interface;
- increase search/intervention strength when branch redundancy is high;
- retain an incumbent or insurance branch before exploration;
- optimize output legibility for a weaker verifier;
- evaluate current code patches by downstream task performance alone.

A future candidate may use one of these as a component, but its headline must be a distinct contradiction or law, and its primary intervention must separate it from the direct collisions above.

## 6. What would justify reopening future editability

The topic may be reopened only if all five conditions are specified before outcomes are inspected:

1. **Matched present state:** multiple patches are behaviorally equivalent under a substantially stronger contract than test passing.
2. **Patch-independent future:** follow-up tasks are fixed without conditioning on which patch is chosen and do not rely on replaying implementation-specific diffs.
3. **New predictor:** the proposed quantity predicts downstream cost after matching standard maintainability, complexity, minimality, test, and embedding-similarity measures.
4. **Causal manipulation:** directly changing the proposed quantity while preserving present behavior changes downstream success.
5. **New law:** the result is not merely “cleaner code is easier to maintain” or “agent code is worse than human code,” and it yields a non-obvious algorithm beyond reranking candidates.

Until those conditions are met analytically or through an already-existing natural experiment, GPU authorization remains zero.

## 7. Next research protocol

The next search should not ask Pro to “be more creative” over the same mechanism list. It should begin from contradictions in current AI evidence, for example two strong papers whose conclusions cannot both hold under an identifiable regime. The unit of search should be:

> **collision pair + hidden regime variable + separating intervention + one-day kill test**

Only a candidate that survives an exact-claim search and supplies a nontrivial causal intervention should receive a theory audit. Only after that audit should the project authorize a GPU smoke test.

## Final decision

`NO_ORAL_SEED_FOUND` is binding for this search. It is a useful stop: the project has eliminated another large semantic neighborhood before spending compute. There is no current Pro task and no authorized GPU experiment.
