# Current Research Status

Last updated: 2026-08-31

## Lineage trace-exposure kill test — 2026-08-31

The post-hoc GSM8K anomaly was converted into a separately frozen 240-call no-trace
baseline before any new output existed. On corrector-problem pairs that the corrector
solved independently, externally presented same-lineage wrong traces caused 18.55 points
more damage than cross-lineage traces (problem-clustered 95% CI 11.69--25.53), and source
wrong-answer retention was 20.56 points higher (CI 13.76--27.34). Assistant-history
effects were directionally stronger.

The binding automatic decision is nevertheless **`NO_GO_ENGINEERING`**. Five of 240
no-trace generations genuinely hit the frozen 768-token limit, producing a 2.083%
parser-or-truncation rate against a 2% ceiling. This is not a parser bug and the threshold
will not be weakened after observing the effect. The parent
`KILL_NO_SELECTION_REVERSAL` decision remains unchanged.

The signal is retained as justification for designing a new clean cross-provider
confirmation with concise matched outputs and answer/content/style interventions. The
current run does not authorize style/content separation automatically and is not itself
an active paper seed.

- Collision audit: [`../audits/LINEAGE_ERROR_ATTRACTOR_COLLISION_AUDIT.md`](../audits/LINEAGE_ERROR_ATTRACTOR_COLLISION_AUDIT.md)
- Frozen kill test: [`../../experiments/endogenous_failure_conditioning/NO_TRACE_BASELINE_PROTOCOL.md`](../../experiments/endogenous_failure_conditioning/NO_TRACE_BASELINE_PROTOCOL.md)
- Chinese results report: [`../../experiments/endogenous_failure_conditioning/NO_TRACE_BASELINE_RESULTS_ZH.md`](../../experiments/endogenous_failure_conditioning/NO_TRACE_BASELINE_RESULTS_ZH.md)
- Automatic gate: [`../../experiments/endogenous_failure_conditioning/results/no_trace_baseline_v1/results/FINAL_GATE.json`](../../experiments/endogenous_failure_conditioning/results/no_trace_baseline_v1/results/FINAL_GATE.json)

## Endogenous-failure reset — 2026-08-30

The project still has **no authorized active paper seed**, but the search is no longer an
undifferentiated hold. The earlier trajectory-fault-gain candidate is now killed by direct
collisions in controlled deletion-versus-replacement intervention, reasoning-trajectory
selection, and agent fault injection. The redundancy-conditioned edit-dose candidate is
also killed before experiment because redundancy and entanglement do not identify the
claimed signs without specifying aggregation structure.

The completed `THEORY-FIRST FALSIFIER` for **endogenous failure conditioning** is now
closed. Published self-correction comparisons can confound correction capability with the
difficulty of each model's selected failure tail, but the frozen common-bank experiment did
not produce the preregistered model-size ordering reversal. The automatic decision is
`KILL_NO_SELECTION_REVERSAL`.

The crossed matrix did reveal a strong negative Qwen2.5×Qwen3 lineage interaction across
both wrappers and both datasets, consistent with cross-lineage correction outperforming
same-lineage correction. This is retained only as an anomaly source, not a paper seed:
MATH-500 suffered 52.71% parser-or-truncation failure under the equal 768-token budget,
the evidence is within one provider, and no equal-budget router comparison was authorized.

- Binding reset: [`../audits/CONTRADICTION_FIRST_SEED_RESET_2026-08-30.md`](../audits/CONTRADICTION_FIRST_SEED_RESET_2026-08-30.md)
- Theory and kill design: [`../theory/ENDOGENOUS_FAILURE_CONDITIONING_NOTE.md`](../theory/ENDOGENOUS_FAILURE_CONDITIONING_NOTE.md)

### Pilot final status

The original Qwen2.5×Gemma v1 grid stopped before inference because the frozen Gemma
repositories are gated and unavailable both locally and on the 4090 host. No correction
outcome was generated. An outcome-blind v2.1 amendment replaces the grid with Qwen2.5
3B/7B and Qwen3 4B/8B, narrowing the first claim to a within-provider lineage
interaction. All scientific thresholds remain unchanged, and a positive result still
requires cross-provider replication.

The v2.1 public bank is frozen at 480 unique errors over 60 common GSM8K and 60 common
MATH-500 problems. All four exact correctors completed 960 cells each, yielding the full
3,840-cell matrix with matching local hashes. The frozen gate found no qualifying
selection reversal. Although all four lineage interactions had the same negative sign and
95% intervals excluding zero, the global bad parse-or-truncation rate was 27.55% versus a
2% ceiling; 1,012 of 1,920 MATH-500 cases hit the quality definition, primarily by reaching
the output-token limit. No router test or cross-provider expansion is authorized.

- Executable amendment: [`../../experiments/endogenous_failure_conditioning/PILOT_PROTOCOL_AMENDMENT_V2.md`](../../experiments/endogenous_failure_conditioning/PILOT_PROTOCOL_AMENDMENT_V2.md)
- V1 access record: [`../../experiments/endogenous_failure_conditioning/V1_ACCESS_FAILURE.md`](../../experiments/endogenous_failure_conditioning/V1_ACCESS_FAILURE.md)
- V2.1 preflight: [`../../experiments/endogenous_failure_conditioning/results/error_bank_v2_1_qwen_lineages/PREFLIGHT_LOCAL.json`](../../experiments/endogenous_failure_conditioning/results/error_bank_v2_1_qwen_lineages/PREFLIGHT_LOCAL.json)
- Chinese final report: [`../../experiments/endogenous_failure_conditioning/RESULTS_REPORT_ZH.md`](../../experiments/endogenous_failure_conditioning/RESULTS_REPORT_ZH.md)
- Automatic final gate: [`../../experiments/endogenous_failure_conditioning/results/pilot_v2_1_qwen_lineages/results/FINAL_GATE.json`](../../experiments/endogenous_failure_conditioning/results/pilot_v2_1_qwen_lineages/results/FINAL_GATE.json)

## Binding decision

The **conditionally irrelevant competing-operator interference** confirmatory seed is a **NO-GO**.

All 49 primary cells, three diagnostic suites, exact replay, and the two-way structured-state interventions completed for six independent model families plus one Qwen positive control. The machine-generated verdict is `NO_GO_STOP_CURRENT_SEED`; all required result cells are complete.

## What the experiment found

Gemma 2 9B was the only diagnostically admissible family. Under Pack A, adding the inactive competing operator reduced pair accuracy from 81.5% to 63.0% (D−C = −18.5 points; Holm-adjusted p = 0.0388). Wrong-operator execution increased, correcting the operator state rescued all four eligible wrong decisions, and reverse injection damaged four correct decisions.

The result did not survive the binding wording replication. Pack B retained only a −5.6-point effect, approximately 30% of the Pack-A magnitude, below both the 7-point and 70%-retention thresholds. Every other independent family failed the preregistered 65% baseline-capability requirement. There were therefore zero admissible negative families and zero admissible positive families.

## Interpretation

The run identifies a real but **single-model, wording-sensitive, causally manipulable local signal**. It does not establish a robust cross-family mechanism, sign heterogeneity, or a publishable ICLR contribution.

The frozen rule now applies: do not add models, prompts, subgroups, parsers, or benchmarks to rescue this seed. A GameBench expansion is not authorized. Further work must begin from a genuinely new hypothesis rather than a larger sweep around the same treatment.

## Canonical evidence

- Chinese confirmatory report: [`../../experiments/operator_interference/RESULTS_REPORT_ZH.md`](../../experiments/operator_interference/RESULTS_REPORT_ZH.md)
- Machine-generated final gate: [`../../experiments/operator_interference/results/FINAL_GATE.json`](../../experiments/operator_interference/results/FINAL_GATE.json)
- Primary metrics: [`../../experiments/operator_interference/results/primary/summary.csv`](../../experiments/operator_interference/results/primary/summary.csv)
- Paired contrasts: [`../../experiments/operator_interference/results/primary/contrasts.csv`](../../experiments/operator_interference/results/primary/contrasts.csv)
- Diagnostic summaries: [`../../experiments/operator_interference/results/diagnostics/`](../../experiments/operator_interference/results/diagnostics/)
- Intervention summary: [`../../experiments/operator_interference/results/interventions/intervention_summary.csv`](../../experiments/operator_interference/results/interventions/intervention_summary.csv)
- Frozen protocol: [`../../experiments/operator_interference/PREREGISTRATION.md`](../../experiments/operator_interference/PREREGISTRATION.md)
- Completed novelty audit: [`../audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md`](../audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md)

## Historical context

The earlier controller-insensitive-planning seed was also a NO-GO: compact chain-of-thought solved it too well. The subsequent broad algorithmic-prompting interpretation was narrowed by the novelty audit because correct-constraint harm, constrained-CoT harm, instruction interference, and prompt-dependent model reversals were already occupied. The now-completed factor-isolation experiment was the sole authorized test of the remaining competing-operator mechanism.

## Latest candidate decision

The conditional **decision-calibrated uncertainty for learned planners** pivot is now also **`NO_GO_BEFORE_EXPERIMENT`**. A second three-agent audit found a decisive July 2026 collision: *Learning from World Feedback: Why Model Uncertainty Fails as a Risk Signal in Model-Based RL* already demonstrates calibrated world models whose internal uncertainty is weakly aligned with constraint-boundary risk, degraded safety when used as a penalty, and strong gains from an outcome-supervised failure predictor. Earlier risk-aware MPC, reachability, conformal safety, and decision-calibration work occupies the proposed method components.

No Stage 0 benchmark or Safety-Gym/GPUDrive run is authorized for this seed. Compute availability was verified and is not the reason for stopping; the experiment was stopped because it would reproduce an occupied phenomenon before specifying a distinct estimator or theorem.

- Binding collision audit: [`../audits/DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md`](../audits/DECISION_CALIBRATED_UQ_COLLISION_AUDIT.md)
- Preceding broad-principle audit: [`../audits/VIABILITY_ALIGNED_PLANNING_INTERNAL_AUDIT.md`](../audits/VIABILITY_ALIGNED_PLANNING_INTERNAL_AUDIT.md)

The repository currently has no authorized active paper seed. Any continuation must begin with a new, separately audited theorem or estimator rather than a renamed version of task-relevant uncertainty, boundary risk, or outcome prediction.

## New divergence-seed decision

The Pro-generated **Closed-Loop Bracket Steering / Behavioral Lie Closure** seed is also **`NO_GO_AS_CURRENTLY_FORMULATED`** after independent mathematical, literature, and engineering review.

The exact four-step activation loop appears literally unoccupied, but the central mechanism does not survive causal inspection. At a fixed transformer layer and token position, the suffix observes only the loop's final hidden-state displacement. Exact final-displacement replay must reproduce its logits, while direct injection of the already-computed Lie bracket should recover the second-order effect more simply. Exiting the instantaneous two-vector span is classical Lie closure and does not establish a capability beyond a time-varying nonlinear source-field controller.

The advertised 34–60 GPU-hour protocol is also undercounted: the proposed triple/layer/scale/orientation matrix creates 6,048–23,760 conditions before prompt replication, model-native brackets require transformer-suffix double backward, standard AxBench scoring conflicts with the no-proprietary-API rule, and several mandatory nonlinear baselines require nontrivial ports.

Do not launch the proposed Stage 0. A narrower source-only zero-shot bracket-feature question is retained only as a HOLD and is not an authorized experiment.

- Binding three-reviewer audit: [`../audits/CLOSED_LOOP_BRACKET_STEERING_AUDIT.md`](../audits/CLOSED_LOOP_BRACKET_STEERING_AUDIT.md)

The repository still has no authorized active paper seed.

## Real-actuation carrier reset

A targeted reset searched frozen source controllers, stateful inference and agents, diffusion schedules, memory, compression, low-rank composition, and sparse routing for a carrier with a genuine “cannot hand-place the cue ball” restriction. The broad search is now closed: every generic path/control carrier was either exactly occupied or reduced to dynamic routing, planning, information gain, risk sensitivity, or final-state control.

At that checkpoint, one much narrower hypothesis advanced to **`ADVANCE_TO_PREREGISTRATION_ONLY`**:

> In a frozen MoE, route substitutions that are independently beneficial under single-layer counterfactual evaluation may become harmful when applied jointly, so local route preferences may be invalid credit signals for multi-layer router updates.

This is no longer a claim about path-dependent capability. It is a proposed failure law for an existing counterfactual-routing diagnostic. No GPU experiment is authorized until a frozen implementation-level preregistration passes review.

- Binding reset and three-reviewer audit: [`../audits/REAL_ACTUATION_CARRIER_RESET.md`](../audits/REAL_ACTUATION_CARRIER_RESET.md)
- Draft diagnostic preregistration: [`../../experiments/moe_route_noncompositionality/PREREGISTRATION.md`](../../experiments/moe_route_noncompositionality/PREREGISTRATION.md)

At the intermediate Stage E checkpoint, the sole candidate passed its engineering gate while Stages D, C, and A remained unauthorized. The route harness achieved zero replay, cache, and deterministic-rerun error across 72 engineering conditions. A separate outcome-blind GSM8K/MATH-500 generation pilot produced a guarded discovery-plus-confirmation projection of `9.16651 GPU h`, below the frozen 12-hour cap; cumulative Stage E use was `0.09193 GPU h`.

This is a feasibility result, not evidence for route non-compositionality. The projection assumes 64 target trajectories per dataset/model and uses a `2.4×` DeepSeek runtime proxy; extra failed generation attempts remain governed by the six-hour Stage D hard stop.

A binding implementation amendment has now authorized code construction and outcome-blind preflight, not scientific discovery. It freezes stable identifiers, answer verification, fragile-token filtering, random streams, matched-null donors, an equal-budget numerical H3, parameter-matched H4 baselines, 10,000 problem-clustered bootstrap resamples, the 32-test BH family, and the six-hour hard stop.

The first preflight attempt was intentionally aborted after an explicit attention-mask warning and remains preserved as an invalid engineering attempt. The corrected v2 acquisition then completed with two retained trajectories per dataset, but its automatic gate returned `NO_GO_STAGE_D_PREFLIGHT`. MATH-500 stable IDs contain slash characters; using those opaque IDs directly as shard names created nested directories that the one-level validator glob did not discover. No route-effect value was inspected during diagnosis.

A filesystem-safe SHA-256 shard mapping and recursive validator check were implemented and v3 passed every outcome-blind structural gate. The first authorized discovery launch then hit a network timeout before model loading; a cached offline retry progressed to GSM8K problem 22 with 9 retained problems before exposing a byte-level BPE prefix-decoding bug in token-to-character offsets. Both failed attempts and all partial sealed outputs are preserved, and no route-effect value was inspected.

Preflight v5 passed, and the full Stage D discovery acquisition retained 64 GSM8K and 64 MATH-500 trajectories. The automatic discovery gate is now `NO_GO_NO_INTERACTION_LAW`: zero of four layer-pair regimes passed H1--H4 on both datasets, versus three required. H1/H2 reversal excesses were generally near zero, H4 compatibility correlations ranged only from `-0.063` to `0.040`, and the few positive H3 point estimates did not survive the complete 32-test family. The successful run passed its compute gate at approximately 3.13 hours.

All 128 shard checksums and four final artifact hashes pass locally. Engineering retries for CPU oversubscription and NumPy JSON serialization are preserved and disclosed; they did not alter frozen statistics or thresholds. Stage C/A remain unauthorized, and the current MoE route non-compositionality seed is closed rather than expanded.

- Stage E report: [`../../experiments/moe_route_noncompositionality/RESULTS_REPORT_ZH.md`](../../experiments/moe_route_noncompositionality/RESULTS_REPORT_ZH.md)
- Final engineering status: [`../../experiments/moe_route_noncompositionality/STAGE_E_STATUS.md`](../../experiments/moe_route_noncompositionality/STAGE_E_STATUS.md)
- Stage D execution status: [`../../experiments/moe_route_noncompositionality/STAGE_D_STATUS.md`](../../experiments/moe_route_noncompositionality/STAGE_D_STATUS.md)
- Binding Stage D amendment: [`../../experiments/moe_route_noncompositionality/STAGE_D_PROTOCOL_AMENDMENT_V1.md`](../../experiments/moe_route_noncompositionality/STAGE_D_PROTOCOL_AMENDMENT_V1.md)
- v2 preflight failure report: [`../../experiments/moe_route_noncompositionality/STAGE_D_PREFLIGHT_V2_FAILURE.md`](../../experiments/moe_route_noncompositionality/STAGE_D_PREFLIGHT_V2_FAILURE.md)
- Discovery engineering retry ledger: [`../../experiments/moe_route_noncompositionality/STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md`](../../experiments/moe_route_noncompositionality/STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md)
- Stage D Chinese report: [`../../experiments/moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md`](../../experiments/moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md)
- Analysis engineering amendment: [`../../experiments/moe_route_noncompositionality/STAGE_D_ANALYSIS_ENGINEERING_AMENDMENT.md`](../../experiments/moe_route_noncompositionality/STAGE_D_ANALYSIS_ENGINEERING_AMENDMENT.md)

## Post-divergence literature-role re-audit

The subsequent 15-candidate Pro divergence returned `NO_GO_NEED_NEW_SEED` and authorized no GPU work. A local re-audit corrected its overly binary use of neighboring literature: papers may be direct collisions, positive adversaries, mechanism foundations, mandatory baselines, or unexplained-anomaly sources.

Most candidates remain closed. The logical-token-clock idea is more directly occupied than initially reported because structure-aware shared position IDs and their length-generalization benefit are already established. One question is retained at **`ONE_THEORY_FIRST_HOLD`** rather than as an experiment:

> Does temporary exposure to a shortcut exhibit a prospectively predictable help-to-harm phase transition—initially scaffolding invariant feature learning through gradient alignment, then suppressing it after shortcut-margin saturation?

No GPU run is authorized. The next binding gate is analytical: demonstrate a non-empty beneficial regime, predict the sign transition and its location, distinguish it from privileged information/curriculum/hinting/bias amplification, and derive a consequence beyond validation-tuning a withdrawal schedule.

The initial deterministic CPU existence check found no beneficial regime in a deep linear factorization. A nonlinear XOR MLP then produced a weak long-horizon loss signal: short shortcut exposure slightly improved final core-distribution loss, while longer exposure became increasingly harmful; however, accuracy was saturated and a shorter training horizon did not yield a stable benefit. At that checkpoint the theory gate remained unpassed; the sharper construction below supersedes that interim status.

A sharper three-parameter gradient-flow model now supplies a proved stylized separation. The shortcut phase obeys two exact identities, including `u = epsilon * exp(2(v - epsilon))`. They imply that clean-only and permanent-shortcut training both retain order-one core loss on a logarithmic horizon, while withdrawing at a fixed shortcut-state threshold and continuing on the core objective reaches arbitrarily small fixed loss in logarithmic time. Deterministic integration across five initialization scales placed the best withdrawal time within roughly 10% of `log(1/epsilon)`.

The state-triggered form also transferred qualitatively to the nonlinear XOR probe. One common shortcut-aligned margin threshold (`0.40`) automatically selected withdrawal steps `55`, `22`, `17`, and `17` as shortcut correlation increased from `0.70` to `1.00`; every condition improved final clean loss, with 8--9 of 10 paired seeds winning. The threshold is exploratory and the gain is small with saturated accuracy.

The subsequent hostile Pro audit returned `HOLD_REQUIRES_GENERAL_LAW`. It repaired the theorem but showed that the scalar system has no intrinsic upper withdrawal boundary: continued shortcut exposure preserves the warm start, the formal trigger is far from shortcut saturation, and permanent exposure is not worse than clean-only at the matched logarithmic horizon.

A local generalization was then derived at exactly matched Relative Transfer. For a shortcut excess direction `A` satisfying `g^T A = 0`, the matched-time endpoint gap is

`-eta * s * D_A ||g||^2 + O(eta*s^2 + eta^2)`.

Under the function-null condition `J A = 0`, the coefficient becomes `r^T (D_A K) r`, yielding explicit positive, neutral, and harmful examples. This result is mathematically valid but directly occupied by level-set teleportation, which maximizes gradient norm on a constant-loss level set, and by null-space teleportation, which implements the function-preserving version for neural networks. Long-horizon auxiliary weighting, good/bad/neutral decomposition, implicit auxiliary learning, and NTK alignment further occupy the surrounding interpretation.

The binding decision is therefore **`NO_GO_TRANSIENT_SHORTCUT_ORAL_SEED`**. The scalar theorem and local rate-shaping lemma remain technical notes, not an authorized paper seed. No GPU experiment is authorized.

- Pro divergence report: [`../proposals/AI_RESEARCH_ORAL_SEED_DIVERGENCE.md`](../proposals/AI_RESEARCH_ORAL_SEED_DIVERGENCE.md)
- Binding literature-role re-audit: [`../audits/ORAL_SEED_LITERATURE_ROLE_REAUDIT.md`](../audits/ORAL_SEED_LITERATURE_ROLE_REAUDIT.md)
- Exploratory existence checks: [`../../analysis/transient_shortcut_phase_transition/README.md`](../../analysis/transient_shortcut_phase_transition/README.md)
- Active theory note: [`../theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md`](../theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md)
- Hostile Pro audit: [`../audits/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_AUDIT.md`](../audits/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_AUDIT.md)
- General-law attempt and binding collision: [`../theory/DURABLE_CLEAN_RATE_AMPLIFICATION_NOTE.md`](../theory/DURABLE_CLEAN_RATE_AMPLIFICATION_NOTE.md)

## Negative-space search after transient-shortcut closure

A new local search re-derived candidate mechanisms from the complete snooker discussion instead of preserving the previous AI carriers. It tested eight translations: continuation-family robustness, diagnosable action interfaces, failure-conditioned value, redundancy-conditioned intervention strength, macro self-averaging, verifier-burden transfer, insurance-before-exploration, and future editability of present-equivalent code patches.

None clears the Oral-level novelty gate. The first seven reduce to direct or mature work in continuation transfer, semantic coverage, agent-interface operability, recoverability, adaptive branching, pruning/concentration, prover-verifier legibility, or incumbent-preserving search. The strongest apparent residual—currently correct patches with different downstream editability—was also closed after finding a 2026 controlled two-step dependent-PR study that directly measures downstream failures caused by the initial implementation.

The binding decision is **`NO_ORAL_SEED_FOUND`**. No Pro task and no GPU run are authorized. The next search must begin from a concrete contradiction between existing results, identify the hidden regime variable, and specify a separating intervention and one-day kill test before any experiment.

- Binding search report: [`../audits/NEGATIVE_SPACE_ORAL_SEED_SEARCH.md`](../audits/NEGATIVE_SPACE_ORAL_SEED_SEARCH.md)

## Deeper snooker-mechanism reassessment

A three-track reassessment corrected an overly broad interpretation of the preceding stop. The snooker source is not exhausted: preserving the exact game state and rules exposes fifteen concrete reversals, especially asymmetric legal-target handoff, object-identity changes near terminal scoring conditions, and stronger K-ball intervention under greater substitute-ball redundancy. These are retained as sources for matched expert-choice counterfactuals, not as AI claims.

Only one AI translation remains at `ONE_THEORY_FIRST_HOLD`: matched agent workflows may exhibit a sign reversal in the usual horizon penalty when extra locally verifiable nodes remove a high-coupling error-propagation bottleneck. AgentEval and CoT2Graph are strong adjacent work. The candidate must first provide a prospectively estimable propagation gain and a separation theorem beyond step count, token count, node accuracy, indegree, and existing propagation features.

This amendment does not authorize an active seed or GPU run. The current state is **`NO_ACTIVE_SEED — ONE_THEORY_FIRST_HOLD`**. A low-prior fail-stop compilation idea is retained only for red-team comparison against validators, abstention, postconditions, rollback, and AFT.

- Binding deeper reassessment: [`../audits/SNOOKER_DEEP_MECHANISM_REASSESSMENT.md`](../audits/SNOOKER_DEEP_MECHANISM_REASSESSMENT.md)

## Receiver-native error-gain diagnostic

The Qwen-lineage correction anomaly has now yielded one active mechanism candidate at
**`PROMISING_REQUIRES_CAUSAL_INTERVENTION`**. Across all 960 frozen GSM8K
trace-by-receiver likelihood cells, same-lineage wrong traces were `1.3231` within-receiver
standard deviations lower in mean NLL than cross-lineage traces (problem-cluster bootstrap
95% CI `[-1.3983, -1.2502]`). Lower receiver NLL predicted retention of the source's
specific wrong answer after problem, corrector, generator, length, and lineage controls.
The external-neutral coefficient was `-1.0005` (95% CI `[-1.5013, -0.4998]`), and all
four leave-one-corrector-out coefficients remained negative.

Adding NLL attenuated the same-lineage log-odds coefficient by `126.9%` under the
external-neutral wrapper and `71.0%` under assistant history. This passes the frozen
post-hoc diagnostic gate, but it is not causal mediation and does not reopen either the
parent `KILL_NO_SELECTION_REVERSAL` decision or the no-trace baseline's
`NO_GO_ENGINEERING` gate.

The only authorized continuation is a small matched causal kill test that holds the wrong
answer and computational skeleton fixed while intervening on receiver-native trace
realization. Cross-provider scaling is unauthorized until that intervention passes.

- Frozen diagnostic: [`../../analysis/native_likelihood_error_gain/DIAGNOSTIC_PROTOCOL.md`](../../analysis/native_likelihood_error_gain/DIAGNOSTIC_PROTOCOL.md)
- Chinese results report: [`../../analysis/native_likelihood_error_gain/RESULTS_REPORT_ZH.md`](../../analysis/native_likelihood_error_gain/RESULTS_REPORT_ZH.md)
- Machine-readable result: [`../../analysis/native_likelihood_error_gain/results/v1/DIAGNOSTIC_RESULT.json`](../../analysis/native_likelihood_error_gain/results/v1/DIAGNOSTIC_RESULT.json)

## Receiver-native error-gain causal kill test

The authorized whitespace-only causal test is complete and bindingly returns
**`KILL_NO_CAUSAL_ERROR_GAIN`**. Its outcome-blind manipulation gate passed: all 480
trace-receiver cells had a pair whose receiver token counts differed by at most two, the
median NLL gap was `0.10684` nats/token against a `0.10` threshold, and `83.33%` exceeded
the `0.05` gap threshold. Every selected pair preserved the exact ordered sequence of all
non-whitespace characters.

All 960 correction calls completed with only `0.625%` parser-or-truncation failure. The
paired source-error-retention effect was only `+0.00625` (problem-cluster 95% CI
`[-0.01875, 0.03333]`) against a preregistered `+0.08` requirement. Corrector-specific
effects were `+0.01667`, `-0.01667`, `0`, and `+0.025`. Accuracy changed by `-0.0125`
(95% CI `[-0.0375, 0.0125]`).

Continuous receiver NLL remains strongly predictive across different source traces, but
the successful within-trace NLL intervention produced essentially no effect. The current
interpretation is therefore prognostic confounding by semantic/error structure, not a
surface-native causal channel. A post-hoc discordance audit found 33 high-native-only and
30 low-native-only retention cases among 480 pairs, with no stable NLL-gap dose response.

Do not scale this whitespace mechanism. A semantic-rewrite continuation is unauthorized
until a theory/literature gate defines verifiable computational-graph equivalence and a
novel prediction beyond student-aligned rationale distillation, explanation transfer,
error-space correlation, and answer anchoring.

- Frozen protocol: [`../../experiments/receiver_native_error_gain_causal/PREREGISTRATION.md`](../../experiments/receiver_native_error_gain_causal/PREREGISTRATION.md)
- Chinese results report: [`../../experiments/receiver_native_error_gain_causal/RESULTS_REPORT_ZH.md`](../../experiments/receiver_native_error_gain_causal/RESULTS_REPORT_ZH.md)
- Automatic final gate: [`../../experiments/receiver_native_error_gain_causal/results/v1/final_analysis/FINAL_GATE.json`](../../experiments/receiver_native_error_gain_causal/results/v1/final_analysis/FINAL_GATE.json)
