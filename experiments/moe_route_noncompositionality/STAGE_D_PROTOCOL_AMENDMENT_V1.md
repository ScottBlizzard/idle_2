# Binding Stage D Implementation Amendment v1

Status: **FROZEN BEFORE STAGE D OUTCOMES**  
Date frozen: 2026-08-28  
Parent protocol: [`PREREGISTRATION.md`](PREREGISTRATION.md)  
Machine-readable companion: [`STAGE_D_FROZEN.yaml`](STAGE_D_FROZEN.yaml)

This amendment resolves implementation ambiguities in the parent protocol. It does not change the research question, models, datasets, primary score, route counts, top-level thresholds, compute caps, anti-rescue rules, or the prohibition on Stage C/A. Where the parent text is less specific, this amendment is binding. Where the two conflict, the stricter rule applies and execution stops for review.

## 1. Canonical terminology

| Canonical term | Binding meaning |
| --- | --- |
| standard route | The model-selected routed-expert set at the unmodified state |
| alternative route | One equal-cardinality Gumbel-top-k set from the frozen top-16 pool |
| route pair | One ordered alternative at the earlier layer and one at the later layer |
| single effect | Logit-margin change caused by one forced alternative route |
| joint effect | Logit-margin change caused by the ordered route pair |
| interaction residual | Joint effect minus the two measured single effects |
| reversal event | The H1 or H2 sign pattern defined in the parent protocol |
| matched null | A counterfactual joint effect formed by replacing an observed interaction residual with residuals from fixed nearest matched donors |
| transport gap | Difference between equal-budget direct-joint and independent-single selection success rates |
| compatibility predictor | The structured, deployable-feature model frozen in Section 9 |
| problem cluster | One retained problem trajectory, the only resampling unit |

No synonym changes these definitions in code or reports.

## 2. Immutable inputs and identifiers

- Dataset revisions are the revisions resolved and written by `datasets` at preflight. Their fingerprints and row counts are saved to `results/discovery/config_resolved.json` before generation.
- GSM8K stable ID is `sha256(question UTF-8)`.
- MATH-500 stable ID is `unique_id` when present and non-empty; otherwise it is `sha256(problem UTF-8)`.
- Rows are sorted lexicographically by `(stable_id, original_row_index)`. Duplicate stable IDs are a protocol error; they are not deduplicated silently.
- Dataset code is `0` for GSM8K and `1` for MATH-500.
- A problem belongs to exactly one five-fold split: after stable sorting, fold is `problem_ordinal mod 5`. Fold membership never depends on correctness, token probability, or route outcome.

## 3. Generation and answer verification

Each candidate is generated separately so that its random stream is independent of the length of other candidates. For problem ordinal `p` and sample index `s`, the generation seed is

`20260828 + 1,000,003 * dataset_code + 10,007 * p + s`.

The frozen decoding parameters remain those in `THRESHOLDS.yaml`. Prompts use the checkpoint chat template and request a concise derivation followed by one explicit final answer.

### GSM8K

- Gold is the substring after the final `####` in the reference answer.
- Prediction is extracted, in order, from the last `#### ...`, the last `Final answer ...`, or the last finite decimal/integer token in the response.
- Both sides remove commas, surrounding currency/percent symbols, surrounding whitespace, and a terminal period.
- They are parsed as exact decimal rationals. Equality is exact; no floating tolerance is used.

### MATH-500

- Gold is the dataset `answer` field when present; otherwise the final balanced `\\boxed{...}` expression in `solution`.
- Prediction is the final balanced `\\boxed{...}` expression; if absent, the final `Final answer:` span.
- Equivalence uses the isolated Stage D environment with `math-verify==0.8.0`, `sympy==1.13.1`, and `antlr4-python3-runtime==4.11.*` pinned in `requirements-stage-d.txt`.
- Parsing and verification are limited to two seconds per comparison. Parse failure, ambiguity, timeout, exception, or a non-Boolean verifier result is incorrect.

The first verified-correct sample by sample index is retained. Verifier failures are logged without reference-answer text in the run log. No manual correction is allowed.

## 4. Fragile-token selection

Teacher forcing uses the exact retained response token IDs, excluding any terminal chat-template token. A token is eligible only if all conditions hold:

1. it belongs to the assistant response rather than the prompt;
2. its decoded surface after Unicode NFKC normalization and whitespace stripping is non-empty;
3. at least one Unicode character has category beginning with `L` or `N`;
4. its character span ends before the frozen final-answer span begins;
5. its standard correct-token probability is at most `0.50`.

The final-answer span begins at the last valid `####` marker for GSM8K and at the last balanced `\\boxed{` or `Final answer:` marker for MATH-500. If no marker exists, it begins at the start of the extracted prediction. Offset mapping is computed from decoded token prefixes and must round-trip to the retained text; failure excludes the trajectory.

Select the eligible token with minimum standard probability. Ties within `1e-12` go to the earliest response-token index. One problem contributes at most one token.

## 5. Layers and random streams

For OLMoE's asserted 16 MoE layers, upward nearest rounding of the parent relative-depth template resolves exactly to:

- near-early: `(3,5)`;
- medium: `(3,8)`;
- far: `(3,13)`;
- late: `(8,13)`.

For dataset code `d`, problem ordinal `p`, layer `l`, and draw counter `a`, Gumbel sampling uses

`20260828 + 1,000,003*d + 10,007*p + 101*l + a`.

The counter begins at zero separately for each problem and layer and advances after every accepted or rejected draw. Candidate ordering is acceptance order. Expert IDs inside each route are sorted ascending. The code never receives target probability, token ID, answer text, or verifier output when constructing routes.

## 6. Primary intervention grid and controls

The primary 49-condition grid is unchanged. Every primary condition is evaluated with state-recomputed gate weights and the correct-token logit margin.

The following secondary controls are fixed and do not enter H1--H4 gates:

- fixed standard-state gate weights for the six diagonal pairs `(a_k,b_k)`;
- same-index expert identities at both layers using each earlier-layer alternative where cardinalities permit, six conditions;
- one outside-top-16 route per layer, sampled uniformly without replacement from experts ranked 17--64 with the same seed formula plus offset `50,000`, evaluated as two singles and one joint;
- six second-layer identity permutations `(a_k,b_(k+1 mod 6))` with recomputed weights, already present in the primary 36 joints and therefore requiring no extra forward pass.

Controls stop rather than expand if their construction is impossible. They may diagnose a primary effect but cannot rescue a failed primary gate.

## 7. Matched-null construction for H1 and H2

For each of the 36 primary route pairs, define the covariate vector before looking at its joint outcome:

1. earlier and later alternative router-score sums;
2. earlier and later overlap fractions with the standard route;
3. overlap fraction between the two alternatives;
4. earlier and later single-intervention final-residual norms;
5. normalized layer separation.

Within the same model, dataset, problem, token, and layer pair, standardize continuous covariates across the 36 pairs using mean and sample standard deviation. Zero-variance coordinates are set to zero. A donor must be a different ordered pair; it may share one route identity because changing either member breaks the original ordered compatibility assignment while permitting closer covariate balance. Distance is Euclidean distance in the standardized vector. The three nearest donors are selected with ties broken by `(distance, donor_i, donor_j)`.

For observed pair `(i,j)` with single effects `delta_i`, `delta_j`, each donor contributes the synthetic null joint effect

`delta_i + delta_j + donor_interaction_residual`.

The matched-null reversal probability for the observed pair is the mean of the three corresponding sign indicators. Thus the null preserves the observed single effects while breaking the assignment of a pair-specific compatibility residual. Matching uses no data from another problem.

Balance is the mean absolute standardized covariate difference over all observed--donor links and is always reported coordinate by coordinate. A dataset/layer cell is invalid if fewer than three donors exist or if fewer than 10 problem clusters and 32 eligible observed route pairs exist for the relevant reversal direction. Balance cannot be used to select another distance, donor count, or subgroup after outcomes are visible.

H1/H2 effect is the problem-weighted observed reversal rate minus the problem-weighted matched-null probability. Each problem receives equal weight regardless of its number of eligible route pairs.

## 8. H3: equal-budget transport failure

Both selectors receive exactly 12 outcome-scored candidates per problem and layer pair:

- independent-single selector: the six earlier-layer and six later-layer single interventions; it selects the highest measured single effect at each layer, and the already measured joint grid supplies the selected pair's evaluation;
- direct-joint selector: the six diagonal pairs `(a_k,b_k)` and six cyclic pairs `(a_k,b_(k+1 mod 6))`; it selects the highest measured joint effect.

Ties go to the lexicographically smaller route indices. Selection is an oracle diagnostic and cannot be called deployable.

Success means the selected joint route has positive correct-token logit-margin change. H3 effect is the problem-level direct-joint success rate minus the independent-single success rate. The numerical meaning of "often enough" is frozen as at least `10.0` percentage points, with its 95% problem-clustered bootstrap lower bound strictly above zero. Mean and median logit-margin gaps are reported but do not replace the binary primary effect.

## 9. H4: compatibility prediction

All predictors use only the feature allowlist written before data loading:

- the L2-normalized standard residual-stream input to the earlier intervened layer at the selected position, compressed to 32 dimensions by a fixed Gaussian random projection generated from seed `20260828`;
- layer indices and normalized separation;
- the two 64-dimensional route multi-hot vectors;
- standard-route multi-hot vectors;
- candidate and standard router-score summaries;
- within-layer standard overlap and cross-layer candidate overlap;
- cross-fitted predictions of the two single effects.

Raw correct-token ID, target probability, target logit, answer text, verifier result, measured held-out single effect, and measured held-out joint effect are forbidden features. A schema assertion stops on any unexpected column.

The compatibility predictor is a low-rank bilinear factorization model: each route multi-hot vector is averaged through an 8-dimensional learned expert embedding; a rank-8 bilinear interaction between the two route embeddings is conditioned by the projected hidden state, and added to the two cross-fitted single-effect predictions. Training minimizes mean squared error on joint logit-margin change.

Comparators are:

1. additive cross-fitted single-effect prediction;
2. router-score-only linear ridge regression;
3. single-effect plus overlap ridge regression;
4. a two-layer ReLU MLP on the identical feature vector;
5. a one-step GRU over the two route descriptors plus context;
6. the standard router and independent-best selectors where applicable.

The MLP hidden width and GRU hidden width are chosen mechanically as the largest integers whose trainable parameter count does not exceed the compatibility model's count; if exact equality is impossible, zero-valued unused parameters are appended so reported counts are equal. No width is tuned on outcomes.

Training uses AdamW, learning rate `1e-3`, zero weight decay, batch size `256`, at most `200` epochs, and early stopping after 20 epochs without improvement on a deterministic 10% training-problem validation subset. Within each outer training fold, the validation problems are those at ranks `0,10,20,...` after lexicographic stable-ID sorting. Seeds are `20260828`, `20260829`, and `20260830`; predictions are averaged. All preprocessing and single-effect models are fitted within each training fold.

Primary H4 metric is Spearman correlation between predicted and measured joint effects, computed within each held-out problem and then averaged with equal problem weights. H4 passes a dataset/layer cell only if:

- compatibility `rho >= 0.40`;
- its 95% problem-clustered bootstrap lower bound is at least `0.40`;
- its paired problem-clustered 95% lower confidence bound over the parameter-matched MLP is strictly above `0`;
- its paired problem-clustered 95% lower confidence bound over the parameter-matched GRU is strictly above `0`.

## 10. Bootstrap, p-values, and multiplicity

Use exactly 10,000 bootstrap resamples. For each dataset/layer cell, sample problem IDs with replacement and carry all of a sampled problem's route pairs. Seed is

`20260828 + 1,000,003*dataset_code + 101*layer_regime_index`.

Confidence intervals are percentile intervals at 95%. For a statistic `theta`, observed value `theta_hat`, and null boundary `theta_0`, the one-sided centered-bootstrap p-value is

`(1 + count(theta_b - theta_hat >= theta_hat - theta_0)) / 10001`.

For H1 and H2, `theta_0=0.10`; for H3, `theta_0=0.10`; for H4 correlation, `theta_0=0.40`. H4's single p-value is the maximum of the correlation, MLP-difference, and GRU-difference component p-values, implementing an intersection-union test.

Apply Benjamini--Hochberg at `q=0.05` once to the complete family of 32 p-values: four hypotheses times four layer-pair regimes times two datasets. Missing, invalid, or inadmissible cells receive p-value `1.0`.

A cell passes only if all point thresholds, confidence-bound requirements, denominator requirements, matching balance, and BH-adjusted significance requirements pass. Discovery succeeds only if the same at least three of four layer-pair regimes pass H1--H4 on both datasets. No alternative pooling rule is allowed.

## 11. Outcome sealing and hard stops

- Scientific outputs are written only to a new, absent `results/stage_d_discovery` directory.
- Per-problem shards are append-only and contain checksums. Resume may skip only a shard whose checksum and frozen configuration hash verify.
- During acquisition, the console and queue log may show only identifiers, counts, timing, memory, and engineering errors. Margins, reversal counts, correlations, and gates remain in sealed files until acquisition ends or the hard stop triggers.
- A monotonic timer begins before model loading. At six cumulative hours, the process saves the current shard, writes `NO_GO_NO_INTERACTION_LAW`, and exits. It does not substitute problems, reduce sample requirements, or relax a threshold.
- A foreign process appearing on the selected physical GPU terminates only this project's process group. It never terminates the foreign process.
- GPUs 0--3 are rejected by both watcher and launcher. Only one of physical GPUs 4--7 may be used for OLMoE discovery.

## 12. Automatic decisions

The only allowed terminal discovery decisions are:

- `GO_STAGE_C_ELIGIBLE`: all Stage D scientific gates pass, but Stage C remains separately unauthorized;
- `NO_GO_NO_INTERACTION_LAW`: an admissibility, scientific, multiplicity, or six-hour gate fails;
- `NO_GO_STAGE_D_PREFLIGHT`: implementation or outcome-blind preflight fails before scientific acquisition;
- `FAILED_INFRASTRUCTURE`: an external failure prevents a valid decision and no scientific definition is changed.

The machine-generated `FINAL_GATE.json` is immutable after creation. Human reports quote it; they do not override it.

## 13. Claim--evidence boundary

Passing Stage D would support only the claim that route utilities in frozen OLMoE exhibit reproducible, predictable cross-layer non-compositionality under the fixed diagnostic. It would not establish cross-model generality, improved language-model training, better free generation, or an ICLR-ready contribution. Those claims require the separately locked Stage C and Stage A evidence.
