# Stage D Authorization Audit

Date: 2026-08-28  
Decision: **AUTHORIZE IMPLEMENTATION AND OUTCOME-BLIND PREFLIGHT ONLY**  
Scientific execution: **NOT YET AUTHORIZED**

## One-sentence argument

Stage E shows that equal-cardinality OLMoE route interventions are reproducible and nominally affordable, but Stage D may acquire scientific outcomes only after every ambiguous analysis choice has been closed by an outcome-blind implementation amendment and the resulting pipeline passes deterministic unit, integration, leakage, and resource tests.

## Scope of this decision

This audit authorizes:

1. writing the binding Stage D implementation amendment;
2. implementing trajectory verification, fragile-token selection, route construction, interventions, matched nulls, cross-fitting, bootstrap inference, multiplicity correction, and automatic stopping;
3. running synthetic tests, hand-authored fixtures, and at most two outcome-blind real prompts per dataset for engineering validation;
4. measuring runtime and memory without aggregating or inspecting H1--H4 outcomes.

It does not authorize the 64-trajectory discovery acquisition, any scientific summary of real route effects, DeepSeek confirmation, hyperparameter tuning on outcomes, or Stage A training.

## Evidence supporting implementation authorization

- Stage E reproduced standard, cached, uncached, and deterministic logits with maximum absolute error `0.0` under the frozen tolerances.
- The intervention and generation pilots consumed at most `0.09193 GPU h` in total.
- The guarded Stage E projection was `9.16651 GPU h` across discovery and confirmation, below the cumulative `12 GPU h` cap.
- Physical GPUs 4--7 are currently the only authorized devices; GPUs 0--3 remain outside this project's control.

These observations establish engineering feasibility only. They do not support route non-compositionality.

## Blocking ambiguities found in the original preregistration

The original preregistration correctly fixed the scientific question, models, datasets, route budget, primary score, and top-level thresholds. It nevertheless left nine implementation choices that could change a result after outcomes were visible:

1. stable problem identifiers and duplicate handling;
2. dataset-specific answer extraction and equivalence;
3. the exact final-answer token exclusion rule;
4. the mapping from base seeds to problem, sample, layer, and Gumbel draw;
5. the matched-null donor population, distance, tie-break, and balance rule;
6. a numerical success definition for H3's phrase "often enough";
7. the proposed compatibility predictor and capacity-matched baselines;
8. the construction of one-sided bootstrap p-values and the Benjamini--Hochberg family;
9. the number and placement of secondary control interventions.

Running discovery before these choices were fixed would create researcher degrees of freedom. [`STAGE_D_PROTOCOL_AMENDMENT_V1.md`](STAGE_D_PROTOCOL_AMENDMENT_V1.md) closes them without weakening any threshold in [`THRESHOLDS.yaml`](THRESHOLDS.yaml).

## Authorization gates before scientific execution

The implementation may advance to `STAGE_D_RUN_AUTHORIZED` only if all of the following are machine-verifiable:

- the original Stage E artifact hashes match the recorded hashes;
- the resolved OLMoE architecture and layer pairs equal `(3,5)`, `(3,8)`, `(3,13)`, and `(8,13)`;
- answer verifiers pass frozen positive, negative, formatting, and timeout fixtures;
- token filtering is deterministic and never selects a final-answer delimiter;
- route candidates are identical across repeated runs and independent of outcome scores;
- every forced route preserves top-8 cardinality;
- standard replay, cached/uncached, and deterministic errors remain within the original tolerances;
- problem-fold splitting has no stable identifier in more than one fold;
- matched-null construction is deterministic, excludes the observed pair, and reports its balance;
- bootstrap and Benjamini--Hochberg code pass synthetic reference cases;
- result paths are absent before launch and the runner refuses overwrite;
- the runner enforces a cumulative six-hour wall-clock/GPU hard stop;
- the launcher accepts only physical GPUs 4--7 and starts only after 180 seconds of exclusive idleness.

Failure of an engineering item returns `NO_GO_STAGE_D_PREFLIGHT`; it cannot be repaired by changing a scientific threshold. Passing every item authorizes one frozen OLMoE discovery run.

## Reviewer-risk assessment

| Risk | Current status | Required control |
| --- | --- | --- |
| Trivial nonlinear perturbation explains reversals | Open | Matched interaction-residual null, fixed/recomputed gates, outside-pool and same-route controls |
| H3 wins only because joint search spends more evaluations | Closed by amendment | Both selectors receive exactly 12 scored candidates |
| H4 leaks the correct token | Open until tests | Problem-level cross-fitting and feature-schema allowlist |
| Predictor advantage is capacity rather than structure | Closed in design | Parameter-matched MLP and recurrent comparators, clustered CI on the difference |
| Sparse H1/H2 denominators inflate rates | Closed in design | Minimum problem and route-pair denominators; otherwise the cell fails |
| Post hoc favorable layers | Closed | Four mechanical layer pairs; the same three must pass on both datasets |
| Compute overrun from unsuccessful generations | Closed operationally | Six-hour hard stop and no replacement of an inadmissible cell |

## Decision boundary

The next legal action is implementation plus outcome-blind preflight. The first real discovery outcome must remain unread until the run terminates and the automatic gate file is sealed. If preflight passes, the authorization transition must be recorded in a separate machine-generated status file before the discovery launcher is allowed to start.

## 中文说明

Stage E 已经证明代码路径可行，但原协议仍有九个会影响结论的细节没有锁死。本审计只批准补协议、写代码和做不看科学结果的预检；只有所有预检通过，才允许一次性启动 Stage D。这里采用的定义均保持或收紧原阈值，没有为提高通过率而放宽标准。

