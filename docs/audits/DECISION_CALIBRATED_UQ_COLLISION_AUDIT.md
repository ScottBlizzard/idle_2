# Decision-Calibrated World-Model Uncertainty: Collision Audit

Audit date: 2026-08-28  
Method: three independent agents audited the preregistration, compute environment, and strongest prior work; the primary agent then verified the decisive sources directly.  
Binding verdict: **`NO_GO_BEFORE_EXPERIMENT`**

## One-sentence argument

The proposed experiment should not be launched because its residual empirical claim—ordinary world-model accuracy or uncertainty diagnostics can be misaligned with downstream constraint-boundary risk, while outcome-grounded risk prediction is more useful for planning—has already been demonstrated directly, and its proposed method components are established in risk-aware planning, reachability, and decision-aware calibration.

## Terminology ledger

| Canonical term | Definition used here | Rejected variants or overclaims |
|---|---|---|
| task-agnostic diagnostic | Aggregate MSE, NLL, CRPS, marginal residual coverage, trace/log-determinant, or ensemble disagreement evaluated without the downstream failure event | “the complete conditional distribution is calibrated” |
| boundary-crossing risk | Probability that a candidate trajectory enters a failure or low-value set | generic “uncertainty” |
| outcome risk critic | A supervised predictor of a world-observed failure or reachability label | “new boundary-aware estimator” unless a distinct estimator is specified |
| decision calibration | Calibration or uncertainty representation evaluated with respect to downstream decisions or losses | “first task-aware uncertainty” |
| direct Monte Carlo | Directly sampling a learned predictive model and evaluating whether each rollout crosses the specified boundary | “naive baseline” |

The distinction in the first row is binding. NLL is a proper score, but a competitive aggregate NLL is not proof that the full conditional predictive distribution is calibrated. If both the complete conditional distribution and the downstream boundary were correct, integrating that distribution over the failure set would produce the correct risk by definition.

## Candidate that was audited

The narrow candidate inherited from the previous audit was:

> Models with similar aggregate NLL/CRPS, residual coverage, or scalar uncertainty can rank candidate plans differently from their true downstream boundary-crossing risk; a boundary-conditioned estimator may recover the risk more sample-efficiently than direct Monte Carlo under a fixed rollout budget.

The intended Stage 1 experiment would have used a learned world model, a future safety/value boundary, MPC-style candidate selection, task-agnostic uncertainty baselines, direct Monte Carlo, and an outcome or boundary-aware risk estimate in a vectorized navigation environment.

## Decisive direct collision

[Learning from World Feedback: Why Model Uncertainty Fails as a Risk Signal in Model-Based RL](https://arxiv.org/abs/2607.16591) (arXiv:2607.16591v1, 18 July 2026; accepted to the ICML 2026 RLxF workshop) already implements essentially this Stage 1 story:

- a partially observable navigation environment with hard collision boundaries;
- four learned world-model architectures under a fixed MPC planner;
- models spanning a two-fold MSE range but statistically equivalent planning quality;
- standard residual-quantile calibration tests passed by all four models (`p` between 0.10 and 0.32), while planning quality remained decoupled;
- ensemble dynamics uncertainty weakly aligned with collision proximity (`r = 0.108`, AUC `0.60`);
- penalizing dynamics uncertainty increased collision rate from `26%` to `34%`;
- an outcome-supervised collision predictor reached AUC `0.97` and reduced collision rate to `14%` without changing the world model or planner;
- robustness checks across random shooting, CEM, MPPI, TD-MPC, data scale, planner capacity, image observations, and a second POMDP;
- negative ranking-aware training experiments and an explicit argument that model uncertainty and sharp constraint-boundary risk have different support.

This paper is a workshop paper and does not settle every theoretical question. It nevertheless occupies the proposed empirical phenomenon, controlled domain, mechanism narrative, strongest obvious alternative, and intended practical conclusion. Repeating it in Safety-Gymnasium or GPUDrive would be a domain replication, not a new ICLR-level seed.

## Earlier work occupying the method components

| Proposed component | Existing primary work | Consequence |
|---|---|---|
| Predict violation probability from learned stochastic dynamics relative to a safety set | [RAZER, CoRL 2021](https://proceedings.mlr.press/v164/vlastelica22a/vlastelica22a.pdf) | Boundary-aware risk inside learned-model MPC is established. |
| Recursive future feasibility/safety boundary | [RCRL, ICML 2022](https://proceedings.mlr.press/v162/yu22d/yu22d.pdf); [RESPO, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/file/dca63f2650fe9e88956c1b68440b8ee9-Paper-Conference.pdf) | Reachability and feasible-set critics already express future safe continuation. |
| Learned distributional reachability certificate | [Distributionally Robust Policy Optimization, arXiv:2210.07553](https://arxiv.org/abs/2210.07553) | Quantile-aware reachability under model uncertainty is occupied. |
| Generative world model plus conformally calibrated safety probability | [How Safe Am I Given What I See?, L4DC 2024](https://proceedings.mlr.press/v242/mao24c.html) | The composite pipeline exists; the paper also reports that direct monolithic risk prediction can outperform it. |
| Failure-probability head with conformal chance-constrained search | [ConstrainedZero, IJCAI 2024](https://www.ijcai.org/proceedings/2024/0746.pdf) | Outcome-risk prediction integrated into planning is established. |
| World-model uncertainty, conformal thresholds, and latent reachability | [UNISafe, CoRL 2025](https://arxiv.org/abs/2505.00779) | The proposed combination is already represented in safe world-model RL. |
| Value-relevant world-model calibration | [Calibrated Value-Aware Model Learning, ICML 2025](https://proceedings.mlr.press/v267/voelcker25a.html) | Value-aware calibration is not an open label. |
| General decision-aware uncertainty/calibration | [Decision Calibration, NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/bbc92a647199b832ec90d7cf57074e9e-Abstract.html); [Utility-Directed Conformal Prediction, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0c6b452f1bbfb6905f6bac957d73b321-Abstract-Conference.html); [End-to-End Conformal Calibration for Optimization Under Uncertainty, TMLR 2025](https://openreview.net/forum?id=yM8qkT0f9H) | Statistical uncertainty should be shaped or assessed by downstream decision loss is already a mature principle. |

## Why the preregistered experiment is stopped

The preregistration reviewer required any candidate estimator to beat, at equal information and compute:

1. direct learned-model boundary-crossing Monte Carlo;
2. projected covariance or chance constraints;
3. expected value and CVaR;
4. a direct outcome/reachability critic trained on the same labels;
5. a conformalized risk critic;
6. equal-wall-clock Monte Carlo allowed to spend the candidate method's overhead.

It also required held-out curved, disconnected, and multimodal boundaries; independent noise directions; decision-level clustered confidence intervals; selection regret; and return-matched safety comparisons. Merely showing covariance rotation, higher trace with lower risk, or equal-moment multimodal counterexamples was explicitly classified as `NO_GO_CONSTRUCTED_DEMO`.

The literature collision arrives before any unique estimator, theorem, or finite-budget advantage has been specified. Therefore Stage 0 would only reproduce known geometry and Stage 1 would closely reproduce the July 2026 experiment. The correct falsification-first action is to stop before implementation rather than create an under-motivated benchmark and search post hoc for a difference.

## Compute audit

Compute is not the blocker. At audit time all eight RTX 4090 GPUs were idle, with approximately 24 GB free per card. The safe workspace is `/mnt/sdb/ccj/iclr_2/`; the server root disk is 97% full and must not host new experiment artifacts. Safety-Gymnasium and MuJoCo are available in the existing `aaai2` environment, whereas Brax and GPUDrive are not installed. Both A40 ports 10008 and 10009 refused connections.

No package was installed, no process was killed, and no experiment was launched during this read-only audit.

## Only possible escape hatch

A future seed would have to begin from a new theorem and estimator, not from this empirical claim. It would need all of the following before any natural-domain run is authorized:

1. a formal setting with a changing, learned recursive boundary whose estimation error is explicit;
2. a nontrivial estimator not reducible to direct boundary-crossing sampling, an outcome critic, a chance constraint, CVaR, or existing conformal decision calibration;
3. a finite-sample or planning-regret advantage over both direct Monte Carlo and an equally supervised outcome critic;
4. an explanation of when that advantage survives rare failures, multimodal predictive distributions, boundary shift, and amortized training cost;
5. a literature audit of the exact theorem and estimator, followed by a one-page preregistration.

That would be a genuinely new theory-algorithm seed. It is not an incremental revision of decision-calibrated world-model uncertainty.

## Binding decision

- Do not create `experiments/decision_calibrated_uq/` for the rejected seed.
- Do not launch Safety-Gymnasium, Brax, or GPUDrive experiments for it.
- Do not describe task-relevant uncertainty, boundary risk, outcome critics, or decision calibration as new principles.
- Preserve the billiards discussion as useful intuition and provenance, not as a novelty claim.
- Resume only with a separately audited estimator/theorem that satisfies the escape-hatch conditions above.
