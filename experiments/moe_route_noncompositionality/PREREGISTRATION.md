# Preregistration: Counterfactual Route Non-Compositionality in Frozen MoEs

Status: **DRAFT — NOT AUTHORIZED TO RUN**

Date frozen: 2026-08-28

Parent audit: [`../../docs/audits/REAL_ACTUATION_CARRIER_RESET.md`](../../docs/audits/REAL_ACTUATION_CARRIER_RESET.md)

## 1. Question

Do equal-compute expert-route substitutions that improve a frozen MoE language model under separate, single-layer counterfactual evaluation retain their sign when applied jointly across layers?

The experiment tests a credit-assignment assumption, not a general claim that paths have independent causal power.

## 2. Falsifiable hypotheses

For a retained correct next token and score \(S\), let \(S_0\) be the standard-router score, \(S_i(a)\) the score after forcing route set \(a\) at layer \(i\), \(S_j(b)\) the analogous score at layer \(j\), and \(S_{ij}(a,b)\) the joint score.

\[
\Delta_i(a)=S_i(a)-S_0,\qquad
\Delta_j(b)=S_j(b)-S_0,
\]

\[
\Delta_{ij}(a,b)=S_{ij}(a,b)-S_0,
\]

\[
I_{ij}(a,b)=\Delta_{ij}(a,b)-\Delta_i(a)-\Delta_j(b).
\]

- **H1 — beneficial-to-harmful reversal:** pairs with \(\Delta_i>0\) and \(\Delta_j>0\) have \(\Delta_{ij}<0\) more often than matched null pairs.
- **H2 — harmful-to-beneficial reversal:** pairs with \(\Delta_i\le0\) and \(\Delta_j\le0\) have \(\Delta_{ij}>0\) more often than matched null pairs.
- **H3 — transport failure:** independently selecting the best single-layer route at each of two layers underperforms direct joint selection often enough to invalidate additive route credit.
- **H4 — predictable compatibility:** a cross-fitted predictor using only information available before the correct next token is revealed predicts joint utility beyond single effects and router scores.
- **H5 — algorithmic consequence:** a path-aware update or selector improves held-out next-token NLL and free-generation accuracy over independent counterfactual preference updates at equal active-expert compute.

H1–H4 form the diagnostic stage. H5 is the paper-relevance gate. H1–H4 without H5 do not authorize a paper program.

## 3. Information regimes

### Analysis-only oracle information

The retained correct next token may be used to:

- define the evaluation score;
- stratify tokens by standard-model confidence;
- label route outcomes in the training split for a compatibility predictor;
- compute diagnostic upper bounds.

### Deployable information

The held-out route selector may use only:

- current hidden states;
- standard router logits and margins;
- layer indices and layer separation;
- candidate expert identities and standard expert overlap;
- single-route effects predicted without the held-out correct token;
- features learned from the training split.

The held-out correct token, reference answer, verifier result, or future generated text may not select a route. Any method using them is an oracle diagnostic and cannot support H4 or H5.

## 4. Models

### Discovery

- Checkpoint: `allenai/OLMoE-1B-7B-0924-Instruct`
- Precision: BF16 unless a frozen operation requires FP32.
- Expected architecture: 16 transformer layers, 64 routed experts, top-8 activation.
- Device target: one RTX 4090.

### Locked confirmation

- Checkpoint: `deepseek-ai/DeepSeek-V2-Lite-Chat`
- Precision: BF16.
- Expected architecture: 27 transformer layers, 64 routed experts with 6 selected plus shared experts.
- Device target: two RTX 4090s using deterministic tensor/model sharding.

Before execution, the implementation must assert the model configuration. A mismatch is a protocol error and stops the run; it does not permit silent layer remapping.

## 5. Datasets and trajectory construction

- `openai/gsm8k`, test split.
- `HuggingFaceH4/MATH-500`, test split.

For each model and dataset:

1. Sort examples by stable dataset identifier.
2. Generate exactly four candidate solutions per problem with frozen decoding settings from `THRESHOLDS.yaml`.
3. Use a deterministic local answer extractor and exact or dataset-standard answer equivalence.
4. Retain the first verified-correct trajectory by sample index.
5. Continue until 64 independent correct trajectories are retained or the full locked split is exhausted.
6. If a model yields fewer than 48 correct trajectories on either dataset, that model–dataset cell is diagnostically inadmissible; do not replace the dataset.

The primary statistical unit is a problem trajectory, not a token or route pair.

## 6. Token selection

Within each retained correct trajectory:

1. Consider assistant-response tokens only.
2. Exclude whitespace-only, pure punctuation, and final answer-format delimiters using a frozen token filter.
3. Compute the standard model's probability for the retained next token.
4. Select the single eligible token with the lowest standard correct-token probability.
5. Require probability \(\le0.50\); otherwise the trajectory has no fragile token and is excluded before route interventions.

Only one token per problem enters the primary analysis. This prevents long trajectories from dominating the sample count.

## 7. Layer pairs

The primary layer-pair template uses relative depths:

- near-early: `(0.20, 0.30)`;
- medium: `(0.20, 0.55)`;
- far: `(0.20, 0.85)`;
- late: `(0.55, 0.85)`.

Map each relative depth to the nearest eligible MoE layer, with ties rounded upward. Shared-only or dense-only layers are ineligible. The mapping script must write exact zero-based indices to `results/config_resolved.json` before any intervention result is computed. The confirmation mapping is determined mechanically by the same rule and may not be tuned.

## 8. Candidate route construction

For each selected token and layer under the unmodified standard trajectory:

1. Take the 16 highest router-scored routed experts as the candidate pool.
2. Draw six equal-cardinality alternative expert sets using Gumbel-top-k with frozen seeds `0..5`.
3. Reject a draw identical to the standard expert set and advance the deterministic seed counter until six distinct alternatives are obtained or 100 draws are exhausted.
4. Keep the standard route separately.

The later-layer candidate expert identities are always defined on the unmodified standard state. Under a joint intervention, the same expert identities are forced at the perturbed state and their gate weights are renormalized using router scores at that actual state.

Secondary control: replay the standard-state gate weights to distinguish expert-identity interaction from gate-weight adaptation.

No candidate may be sampled using correct-token probability or any answer-dependent score.

## 9. Intervention grid

For every token and layer pair `(i,j)`:

- one standard pass;
- six single interventions at `i`;
- six single interventions at `j`;
- all 36 joint route pairs.

Total: 49 evaluated conditions per token and layer pair.

All runs use the same prefix KV cache up to the selected token and cache the hidden state immediately before the earlier intervened layer. The implementation must verify that an unmodified replay reproduces standard logits within the tolerance in `THRESHOLDS.yaml`.

## 10. Primary and secondary scores

### Primary

Correct-token logit margin:

\[
S=z_{y_t}-\max_{v\ne y_t}z_v.
\]

### Secondary

- correct-token log probability;
- correct-token probability;
- hidden-state displacement norm at the output of each intervened layer;
- final residual displacement norm;
- KL divergence from the standard next-token distribution;
- route overlap and router-score rank.

The primary claim must hold in logit margin. A probability-only effect is classified as a softmax artifact.

## 11. Matched nulls

For each observed route pair, construct matched comparisons within the same model, dataset, problem, token, and layer pair using bins for:

- each route's standard router-score sum;
- expert-set overlap with the standard route;
- overlap between the two alternative sets;
- single-intervention final residual norm;
- layer separation.

If exact matching is impossible, use preregistered nearest-neighbor matching with standardized covariates and report balance. The primary reversal excess is observed reversal rate minus matched-null rate.

Additional controls:

- identical route set forced at both layers where cardinalities permit;
- random expert sets from outside the top-16 pool;
- standard route replay;
- fixed versus state-recomputed gate weights;
- permutation of second-layer route identities within score/overlap bins.

## 12. Predictors and baselines

Use problem-level five-fold cross-fitting. No route pair from a held-out problem may enter predictor training.

Baselines:

1. additive predictor `delta_i + delta_j`;
2. router-score-only linear model;
3. single-effect plus overlap linear model;
4. generic two-layer MLP on all permitted features;
5. recurrent/path-aware predictor with the same parameter count as closely as practical;
6. standard router;
7. independently best predicted route at each layer;
8. direct joint-search oracle at identical candidate-evaluation budget;
9. final-layer-only counterfactual update;
10. independent multi-layer preference update.

The proposed compatibility model cannot claim novelty merely by outperforming linear additivity; it must beat the generic MLP and recurrent baseline.

## 13. Statistics

- Primary confidence intervals: problem-clustered bootstrap, 10,000 resamples.
- Discovery multiplicity: Benjamini–Hochberg over H1–H4 across four layer-pair regimes and two datasets.
- Confirmation: test only the signs and thresholds locked after discovery; Holm correction across the frozen primary hypotheses.
- Report all cells, including inadmissible cells and failures.
- Do not pool route pairs as independent observations.

## 14. Staged stopping rules

### Stage E — engineering gate

Budget: at most 1 GPU-hour on OLMoE.

Run 8 trajectories, one layer pair, and two alternatives per layer. Stop if:

- standard replay logit mismatch exceeds tolerance;
- forced route cardinality or shared-expert handling is incorrect;
- results change across identical deterministic reruns;
- the cached and uncached implementations disagree beyond tolerance;
- projected full diagnostic compute exceeds 12 GPU-hours for discovery plus confirmation.

Stage E has no scientific interpretation.

### Stage D — OLMoE discovery

Budget: cumulative at most 6 GPU-hours, including trajectory generation, intervention evaluation, statistics, predictor fitting, and deterministic reruns.

Stop with `NO_GO_NO_INTERACTION_LAW` unless all diagnostic thresholds in `THRESHOLDS.yaml` pass on both datasets and at least three of four layer-pair regimes.

### Stage C — locked DeepSeek confirmation

Budget: cumulative at most 12 GPU-hours across Stages E, D, and C, including trajectory generation, intervention evaluation, statistics, predictor fitting, and deterministic reruns.

No model, dataset, token rule, layer-pair template, candidate-pool size, route count, or threshold may change after Stage D. Stop with `NO_GO_NO_CROSS_MODEL_REPLICATION` unless all locked confirmation gates pass.

### Stage A — algorithmic consequence

Not authorized by this document. It requires a separate amendment after Stage C. A diagnostic-only result does not authorize free-generation sweeps or router training.

## 15. Anti-rescue rules

After any failed gate, do not add:

- models or datasets;
- easier tokens or alternative confidence bins;
- layer pairs;
- candidate routes;
- probability-only metrics;
- answer-aware route selectors;
- larger predictors;
- extra route evaluations;
- weaker baselines;
- post hoc subgroups.

A failed gate closes the candidate.

## 16. Required outputs

- `results/config_resolved.json`
- `results/engineering/replay_checks.json`
- `results/engineering/runtime.csv`
- `results/discovery/route_effects.parquet`
- `results/discovery/problem_summary.csv`
- `results/discovery/gates.json`
- `results/confirmation/route_effects.parquet`
- `results/confirmation/problem_summary.csv`
- `results/confirmation/gates.json`
- `results/FINAL_GATE.json`
- `RESULTS_REPORT_ZH.md`

The final gate must be generated automatically from `THRESHOLDS.yaml` and may not be edited manually.
