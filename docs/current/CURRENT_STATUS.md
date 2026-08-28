# Current Research Status

Last updated: 2026-08-28

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

One much narrower hypothesis advances to **`ADVANCE_TO_PREREGISTRATION_ONLY`**:

> In a frozen MoE, route substitutions that are independently beneficial under single-layer counterfactual evaluation may become harmful when applied jointly, so local route preferences may be invalid credit signals for multi-layer router updates.

This is no longer a claim about path-dependent capability. It is a proposed failure law for an existing counterfactual-routing diagnostic. No GPU experiment is authorized until a frozen implementation-level preregistration passes review.

- Binding reset and three-reviewer audit: [`../audits/REAL_ACTUATION_CARRIER_RESET.md`](../audits/REAL_ACTUATION_CARRIER_RESET.md)
- Draft diagnostic preregistration: [`../../experiments/moe_route_noncompositionality/PREREGISTRATION.md`](../../experiments/moe_route_noncompositionality/PREREGISTRATION.md)

The repository still has no authorized active paper seed. The sole candidate has now passed its Stage E engineering gate, but Stages D, C, and A remain unauthorized. The route harness achieved zero replay, cache, and deterministic-rerun error across 72 engineering conditions. A separate outcome-blind GSM8K/MATH-500 generation pilot produced a guarded discovery-plus-confirmation projection of `9.16651 GPU h`, below the frozen 12-hour cap; cumulative Stage E use was `0.09193 GPU h`.

This is a feasibility result, not evidence for route non-compositionality. The projection assumes 64 target trajectories per dataset/model and uses a `2.4×` DeepSeek runtime proxy; extra failed generation attempts remain governed by the six-hour Stage D hard stop. A separate binding authorization is required before any discovery execution.

- Stage E report: [`../../experiments/moe_route_noncompositionality/RESULTS_REPORT_ZH.md`](../../experiments/moe_route_noncompositionality/RESULTS_REPORT_ZH.md)
- Final engineering status: [`../../experiments/moe_route_noncompositionality/STAGE_E_STATUS.md`](../../experiments/moe_route_noncompositionality/STAGE_E_STATUS.md)
