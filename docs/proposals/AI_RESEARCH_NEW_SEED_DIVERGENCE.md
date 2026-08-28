# AI_RESEARCH_NEW_SEED_DIVERGENCE

**Audit date:** 28 August 2026

**Repository audited:** [ScottBlizzard/idle_2](https://github.com/ScottBlizzard/idle_2)

**Literature-search cutoff:** 28 August 2026
**Decision vocabulary:** **KILL** = do not experiment; **HOLD** = unresolved but not presently strong enough to spend the main budget; **ADVANCE** = run only the stated preregistered kill test, not “begin the paper.”

This document is a clean research reset. It treats every repository-level NO-GO as binding, does not reinterpret failed results as “promising,” and does not transfer a rejected principle into a new domain under different terminology.

## 1. Executive verdict

### Verdict: **one idea is worth a kill test; zero ideas are presently paper-ready**

The search produced:

- **One ADVANCE:** **Seed A — Closed-Loop Bracket Steering: second-order behavioral accessibility outside the first-order steering span.**
- **One HOLD, not shortlisted:** **Output-Equivalence Multiplicity Valley in supervised reasoning.**
- **Fifteen KILL decisions** spanning language-model search, retrieval, diffusion sampling, mixture-of-experts routing, continual learning, mechanistic interpretability, multimodal reasoning, model editing, agent memory, masked-diffusion decoding, multi-agent critique, and symmetry-based data augmentation.

The repository leaves no ambiguity about the starting boundary. The operator-interference seed is stopped because its only admissible causal signal failed the binding transfer test; the calibrated-uncertainty seed is stopped before experimentation because a July 2026 paper and substantial earlier work already occupy both its central phenomenon and obvious remedies; the broad viability/option-preservation family is not available as a new principle; and the algorithmic-prompting inversion is not recoverable by changing prompts or domains. citeturn494898view0turn391566view0turn391566view2turn391566view4turn391566view6turn391566view8

The surviving seed is deliberately narrow:

> **Can a closed sequence of state-dependent activation controls whose first-order action cancels create a reproducible, predictable behavior displacement outside every matched static steering span?**

This is not a claim that “order matters,” that nonlinear steering is useful, or that Lie brackets exist. All three are already occupied. Recent work already uses activation-level commutators as order-sensitivity diagnostics, models feed-forward blocks as local steering fields, analyzes update-order effects through Lie brackets, learns nonlinear state-dependent steering fields, and performs feedback or ODE-based activation control. citeturn794313search0turn794313search1turn595905search7turn595905academia33turn595905academia35turn595905search2

Seed A remains worth a **cheap falsification experiment** only because it asks for a stronger and operationally distinct result:

1. the intervention is a **zero-first-order group-commutator loop**;
2. the observed displacement must have a substantial component outside the instantaneous span of the source controls;
3. the direction and sign must be predicted out of sample by a Lie-bracket estimator;
4. reversal of the loop must reverse the leading behavioral effect;
5. the effect must scale quadratically with intervention size;
6. matched static, nonlinear, direct-target, and equal-step baselines must fail to reproduce the same behavior–utility trade-off;
7. the result must replicate across at least two model families and public natural-language tasks.

A result weaker than this is not a paper seed. It is an illustration of classical nonlinear control inside a transformer.

The overall confidence that Seed A survives Stage 0 is **low-to-moderate**. Its value is not that success is likely, but that the central mechanism can be killed cleanly in less than three days and at substantially less than the available compute ceiling.

## 2. Negative-space map

### 2.1 Bindingly closed regions

| Conceptual region | Why it is closed | What would **not** reopen it |
|---|---|---|
| Controller-insensitive, viability-aligned, option-preserving, continuation-preserving, empowerment-like, reachability-like, or recoverability-oriented planning | The repository audit reduces these formulations to established stochastic viability, chance constraints, reachability, empowerment, attainable-utility preservation, and related safe/robust planning formalisms. citeturn391566view2turn391566view3 | A new name, a new robot simulator, a language-agent domain transfer, a new scalar score, or a learned approximation to an existing viability quantity. |
| Scalar uncertainty misaligned with downstream boundary risk | The latest seed’s empirical phenomenon and obvious method components were already occupied before experimentation, including direct outcome prediction, risk-aware planning, and conformal/safety variants. citeturn391566view0turn391566view1 | Replacing “collision” with “failure,” predicting risk with another network, adding Monte Carlo samples, or calling the scalar “decision-calibrated.” |
| Outcome-supervised failure prediction | A direct supervised predictor is already the obvious strongest baseline and was part of the collision that stopped the seed. citeturn391566view1 | A different architecture, calibration loss, confidence head, or downstream benchmark. |
| Algorithmic prompting inversion | The repository audit found that the initial formulation was confounded and that neighboring literatures already cover instruction interference, harmful reasoning, and prompt-induced degradation. citeturn391566view4turn391566view5 | More prompts, more models, more domains, or redefining “algorithm” to mean a stylistic instruction. |
| Conditionally irrelevant competing-operator interference | The frozen experiment produced a local causal effect in one admissible setting, but the binding transfer pack failed; the repository explicitly forbids rescue sweeps. citeturn391566view8turn391566view9 | Added prompt packs, relaxed baseline admissibility, post-hoc subgroups, extra model families, or a renamed “operator collision.” |
| Error shaping as a general principle | Directing variation into task-tolerant directions is already expressible through invariance, equivariance, robust control, covariance shaping, tangent-space methods, and established representation geometry. The synthesis itself warns against promoting the billiards intuition into a universal new law. citeturn494898view1turn391566view2 | Applying the same geometry to diffusion, agents, quantization, or robotics without a new theorem and unmistakable phenomenon. |
| “Current success versus future position” as a new principle | In planning it reduces to value, reachability, continuation sets, or option preservation; in sequence modeling it collides with exposure bias, process supervision, recoverability, and sequence-level objectives. | A second head, a continuation metric, or outcome-conditioned reweighting. |

### 2.2 Broader occupied regions found during the reset

The reset also eliminated several attractive-looking abstractions that were not explicitly named in the repository.

| Region searched | What the literature already supplies | Residual status |
|---|---|---|
| **Test-time reasoning diversity** | Prefix regeneration, prefix consistency, redundancy pruning, diversity-aware search, and adaptive allocation already target correlated reasoning traces rather than treating samples as independent. citeturn524362search1turn524362search18turn426843academia37 | A “lineage-adjusted pass@k” or “insurance branch” is a computational refinement, not a new principle. |
| **Retrieval evidence multiplicity** | Controlled 2026 work directly studies duplicate, paraphrastic, and genuinely diverse retrieval sets; set selection, deduplication, and diversity-aware retrieval are active method families. citeturn524362search11turn524362search20turn524362search24turn524362search14 | “Independent evidence families” is already occupied. |
| **Agent-memory insurance** | Recent systems explicitly arbitrate retention versus consolidation, preserve raw records, maintain topic documents, and combine compact summaries with recoverable evidence. citeturn426843search6turn426843search14turn426843search2turn426843search10 | Keeping one raw fallback span is a design choice inside an occupied architecture space. |
| **Masked-diffusion commitment order** | August 2026 work directly shows that answer tokens can commit before reasoning support and proposes gates or learned commitment policies; earlier work already studies deferred commitment and order policies. citeturn426843search3turn426843search27turn426843search19turn426843search15turn426843academia36 | “Postpone the hard token” and “shorten horizon after surprise” are occupied. |
| **Nonlinear activation steering** | State-dependent vector fields, ODE flows, invertible nonlinear transformations, and feedback controllers are already public. citeturn595905academia33turn595905academia35turn595905search2turn595905search19 | Nonlinearity, adaptivity, and feedback are not novelty. |
| **Commutator/order diagnostics** | Activation Wilson loops, feed-forward commutator defects, and Lie-bracket analyses of sequential updates already establish order sensitivity and curvature as useful diagnostics. citeturn794313search0turn794313search1turn595905search7 | A result that merely detects noncommutativity is occupied. |
| **Multiple reasoning paths in post-training** | Recent work studies path divergence, SFT gradient conflict, diversity preservation, problem-versus-solution diversity, and hybrid SFT/RL objectives. citeturn426843academia35turn426843search16 | The exact *non-monotonic route-count valley* is not clearly occupied, but its most likely explanations are. |

### 2.3 The remaining plausible opening

Only one residual mechanism appears both technically sharp and cheap enough to test:

> **Second-order behavioral accessibility:** a closed, zero-first-order sequence of two state-dependent activation controls may generate a behavior-relevant displacement outside the static span of either control.

Let \(h\) be a residual-stream state and let \(U(h)\) and \(V(h)\) be smooth activation-control fields. Define the closed loop

\[
\mathcal C_\epsilon
=
\Phi^V_{-\epsilon}
\circ
\Phi^U_{-\epsilon}
\circ
\Phi^V_{\epsilon}
\circ
\Phi^U_{\epsilon},
\]

where maps are applied from right to left. Under the standard Lie-bracket convention

\[
[U,V](h)=J_V(h)U(h)-J_U(h)V(h),
\]

the local displacement is

\[
\mathcal C_\epsilon(h)-h
=
\epsilon^2[U,V](h)+O(\epsilon^3).
\]

Let

\[
\mathcal S(h)=\operatorname{span}\{U(h),V(h)\}
\]

and define the orthogonal bracket residual

\[
r_\perp(h)
=
\left(I-P_{\mathcal S(h)}\right)[U,V](h),
\qquad
\rho(h)=
\frac{\|r_\perp(h)\|_2}
{\|[U,V](h)\|_2+\delta}.
\]

The open question is not whether \([U,V]\) can be nonzero. The open question is whether \(r_\perp\) is **large, behaviorally meaningful, predictable, reproducible, and algorithmically useful** in real frozen language models after the strongest nonlinear baselines are given equal data and equal intervention budget.

This is a narrow opening. It closes immediately if the apparent effect is an Euler-integration artifact, a probe artifact, ordinary activation magnitude, pair-selection overfitting, or something a direct nonlinear target field reproduces.

## 3. Broad candidate generation

The candidate search covered seventeen hypotheses across fifteen AI/ML areas. Compute figures are estimates for an initial falsification run, not full-paper budgets.

### C1. Family-correlated search saturation — language-model inference

**One-sentence hypothesis.** At fixed rollout count, the probability of solving a reasoning problem is controlled by the number of semantically independent solution families rather than the raw number of sampled chains.

**Counterintuitive element.** Eight visibly different chains can contain less usable information than two chains whose early semantic commitments differ.

**Causal intervention.** Hold model, prompts, verifier, token budget, and sample count fixed; force candidate allocation across early semantic-prefix clusters instead of sampling all continuations from the highest-scoring prefix.

**Cheapest falsification experiment.** On 200 verified math/code items, generate eight rollouts per item, cluster by early reasoning state, and compare ordinary best-of-\(N\), self-consistency, stratified-prefix sampling, and a direct Monte Carlo oracle.

**Likely strongest baseline.** Prefix Consistency, redundancy-pruned self-consistency, and an equal-budget MCTS or adaptive rollout allocator.

**Most likely prior-art collision.** Diversity-aware test-time scaling, prefix regeneration, and thought-chain redundancy pruning already attack correlated samples directly. citeturn524362search1turn524362search18turn426843academia37

**Estimated compute and wall-clock.** 4–8 GPU-hours; 4–10 wall-clock hours with four independent 4090s.

**Preliminary novelty score.** 1.5/5.

**Likely publication ceiling.** Benchmark or workshop result unless coupled to a genuinely new estimator theorem.

**Status.** **KILL.** The residual is an estimator/allocator detail inside an occupied test-time-search space.

### C2. Evidence-family saturation — retrieval-augmented generation

**One-sentence hypothesis.** RAG reliability depends on the number of independent evidence lineages, not the number of retrieved passages.

**Counterintuitive element.** Adding five highly relevant paraphrases can make an answer less reliable than adding one moderately relevant source with independent provenance.

**Causal intervention.** Construct retrieval sets with identical token count and average relevance but vary duplication, paraphrase family, and provenance diversity.

**Cheapest falsification experiment.** Use a public multi-hop QA set, synthesize duplicate/paraphrase controls, and compare answer accuracy and citation support under fixed \(k\).

**Likely strongest baseline.** Diversity-aware set selection, DPP/MMR retrieval, byte-level deduplication, and a direct evidence-entailment selector.

**Most likely prior-art collision.** A 2026 controlled study already manipulates duplicate, paraphrastic, and diverse retrieval sets, while set-selection and deduplication methods directly optimize the same issue. citeturn524362search11turn524362search20turn524362search24turn524362search14

**Estimated compute and wall-clock.** 2–6 GPU-hours; under one day.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Replication note.

**Status.** **KILL.**

### C3. Early semantic-branch insurance — diffusion or generative sampling

**One-sentence hypothesis.** Under a fixed denoising budget, preserving several coarse semantic hypotheses until mid-trajectory yields better mode coverage than repeatedly perturbing one already committed latent.

**Counterintuitive element.** Spending steps on a lower-scoring early branch can outperform refining the apparently best sample.

**Causal intervention.** Fork the same latent at matched compute at early, middle, or late denoising times; keep total function evaluations and guidance calls identical.

**Cheapest falsification experiment.** Use a public latent-diffusion model on class-conditional or compositional prompts; measure semantic mode coverage, reward, and within-family correlation.

**Likely strongest baseline.** Particle/SMC diffusion, diversity-promoting sampling, restart methods, and verifier-guided beam or tree sampling.

**Most likely prior-art collision.** The intervention is a standard delayed-commitment/diversity allocation problem in diffusion search; any result is likely a scheduler comparison unless a new cross-model law appears.

**Estimated compute and wall-clock.** 8–24 GPU-hours; 8–20 hours.

**Preliminary novelty score.** 2/5.

**Likely publication ceiling.** Workshop or narrow generative-model poster.

**Status.** **KILL.** The idea reduces to branch allocation and more effective samples.

### C4. Insurance-expert routing — mixture of experts

**One-sentence hypothesis.** A router should deliberately retain a lower-scoring generalist expert on uncertain tokens because its error correlation with specialized experts is lower.

**Counterintuitive element.** Sending some tokens to an apparently weaker expert can improve worst-case accuracy.

**Causal intervention.** Reserve one expert as a low-correlation fallback while holding expert calls, FLOPs, and parameter count fixed.

**Cheapest falsification experiment.** Fine-tune a small public sparse MoE on mixed-domain classification or language modeling and compare top-\(k\), load-balanced routing, and correlation-aware fallback routing.

**Likely strongest baseline.** Standard load balancing, auxiliary-loss routing, router ensembles, expert dropout, and direct dense fallback.

**Most likely prior-art collision.** Expert redundancy, load balancing, dropout, fallback routing, and routing-aware robustness already instantiate the same ensemble logic; recent work also directly intervenes on MoE experts for behavior control. citeturn794313search17

**Estimated compute and wall-clock.** 12–40 GPU-hours; one to two days.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Systems ablation.

**Status.** **KILL.**

### C5. Dormant-plasticity reserve — continual or online learning

**One-sentence hypothesis.** Continual learners should preserve a small inactive parameter subspace that is only recruited after distribution change.

**Counterintuitive element.** Deliberately underusing current capacity can improve future adaptation.

**Causal intervention.** Freeze or regularize a matched fraction of units during early tasks and release them after a detected shift.

**Cheapest falsification experiment.** Split-CIFAR or a small nonstationary RL benchmark with fixed total parameters and compute; compare reserved units, random resets, and continual backprop.

**Likely strongest baseline.** ReDO, continual backprop, elastic/expandable networks, unit resets, and plasticity-preserving regularizers.

**Most likely prior-art collision.** The mechanism is reserve capacity plus plasticity preservation, a mature continual-learning idea.

**Estimated compute and wall-clock.** 16–48 GPU-hours; one to two days.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Incremental continual-learning result.

**Status.** **KILL.**

### C6. Compensation-triggered circuit switch — mechanistic interpretability

**One-sentence hypothesis.** Standard component ablations systematically underestimate causal reliance because the model recruits backup circuits only after the intervention.

**Counterintuitive element.** Removing a component can make another component appear causal even though it was inactive in the unperturbed run.

**Causal intervention.** Compare infinitesimal graded interventions, hard ablations, path patching, and simultaneous multi-site interventions while measuring circuit recruitment.

**Cheapest falsification experiment.** Run a small transformer on a known algorithmic or language task and measure activation changes and causal effects across intervention magnitudes.

**Likely strongest baseline.** Path patching, causal scrubbing, graded ablations, and direct multi-component intervention.

**Most likely prior-art collision.** The Hydra-effect/self-repair literature directly studies compensation after ablation; the remaining work is attribution methodology rather than a new mechanism.

**Estimated compute and wall-clock.** 8–24 GPU-hours; under one day.

**Preliminary novelty score.** 1.5/5.

**Likely publication ceiling.** Interpretability workshop unless a new identifiable estimator is proved.

**Status.** **KILL.**

### C7. Set-valued grounding before verbalization — multimodal reasoning

**One-sentence hypothesis.** A vision-language model should retain several mutually compatible visual groundings until linguistic reasoning resolves them, rather than committing to one box or region early.

**Counterintuitive element.** Less confident early grounding can produce more accurate final reasoning.

**Causal intervention.** Hold the vision encoder and language model fixed; pass either one top grounding, a calibrated set of alternatives, or a direct supervised grounding distribution into the reasoner.

**Cheapest falsification experiment.** Use a public visual question-answering or referring-expression benchmark with controlled ambiguous scenes.

**Likely strongest baseline.** Direct supervised grounding, beam/set prediction, region marginalization, and explicit perceive-then-reason pipelines.

**Most likely prior-art collision.** This reduces to latent-variable marginalization, set prediction, and delayed commitment in multimodal reasoning; recent work already targets perception–reasoning separation and visual forgetting.

**Estimated compute and wall-clock.** 12–30 GPU-hours; one day.

**Preliminary novelty score.** 2/5.

**Likely publication ceiling.** Multimodal poster only if a broad causal failure is found.

**Status.** **KILL.**

### C8. Output-equivalence multiplicity valley — supervised reasoning

**One-sentence hypothesis.** With total training tokens and problem count fixed, training on two or three semantically distinct correct solution families can generalize worse than training on one family or on many families.

**Counterintuitive element.** More valid solutions would first hurt and then help: a “few-route valley,” not a monotonic diversity benefit.

**Causal intervention.** For the same verified problems, vary the number \(K\) of distinct solution algorithms while fixing total target tokens, answer labels, optimizer steps, and problem frequency.

**Cheapest falsification experiment.** Generate verified algorithmic or math solutions in \(K\in\{1,2,4,8\}\) route families; train 100M–500M transformers or LoRA-tune a 1.5B model; evaluate answer accuracy, route transfer, gradient covariance, and hidden-state invariance.

**Likely strongest baseline.** Route-conditioned SFT, sequence-level marginal likelihood over references, answer-only RL/GRPO, PCGrad or gradient surgery, and an equal-token control using more distinct problems rather than more solutions per problem.

**Most likely prior-art collision.** Path-diversity, SFT-conflict, diversity-preservation, and dataset-diversity papers already occupy the obvious explanations. “SFT Conflicts, RL Coexists” directly attributes failures to gradient interference, while recent hybrid SFT/RL work already uses multiple solution paths. citeturn426843academia35turn426843search16

**Estimated compute and wall-clock.** 30–100 GPU-hours; two to four days.

**Preliminary novelty score.** 2.5/5.

**Likely publication ceiling.** ICLR poster only if the non-monotonic law replicates on natural tasks and survives route conditioning, answer-only learning, and equal-token controls.

**Status.** **HOLD.** The exact curve may be unreported, but the likely mechanism is already known. Do not spend the main budget without a sharper theorem or a pre-existing verified multi-route dataset.

### C9. Direction-only feedback versus magnitude feedback — preference learning and optimization

**One-sentence hypothesis.** When feedback magnitudes are poorly calibrated across examples, repeated sign-consistent pairwise feedback can outperform richer scalar rewards at equal information budget.

**Counterintuitive element.** Throwing away magnitude information can improve optimization.

**Causal intervention.** Generate paired and scalar feedback from the same latent noisy utility; keep comparisons and labels information-matched.

**Cheapest falsification experiment.** Fine-tune a small policy or reward model under controlled heteroscedastic noise and compare scalar regression, ranking loss, sign-only updates, and an oracle-calibrated scalar baseline.

**Likely strongest baseline.** Pairwise preference optimization, ordinal regression, signSGD, robust regression, and per-source reward normalization.

**Most likely prior-art collision.** This is a standard consequence of ordinal feedback and magnitude miscalibration.

**Estimated compute and wall-clock.** 4–12 GPU-hours; under one day.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Didactic experiment.

**Status.** **KILL.**

### C10. Edit-batch multiplicity valley — model editing

**One-sentence hypothesis.** Two or three related knowledge edits can interfere more severely than either a single edit or a large coherent edit batch that reveals a shared subspace.

**Counterintuitive element.** A larger edit batch could be easier than a small batch.

**Causal intervention.** Hold facts, token budget, rank, and update count fixed while varying the number of semantically related edits and whether the shared subspace is estimated jointly.

**Cheapest falsification experiment.** Use CounterFact or MQuAKE with a 1–7B open model and compare sequential, batch, and low-rank joint editing.

**Likely strongest baseline.** MEMIT, AlphaEdit, sequential-edit regularizers, and direct joint fine-tuning.

**Most likely prior-art collision.** Batch editing, edit interference, task-vector geometry, and shared low-rank update methods already cover the proposed mechanism.

**Estimated compute and wall-clock.** 8–24 GPU-hours; under one day.

**Preliminary novelty score.** 1.5/5.

**Likely publication ceiling.** Model-editing ablation.

**Status.** **KILL.**

### C11. Recoverability-weighted failed traces — self-correction and verifier learning

**One-sentence hypothesis.** A failed reasoning trace should be weighted by how many local revisions can still repair it, not merely by its final outcome.

**Counterintuitive element.** Two equally wrong traces may have radically different training value.

**Causal intervention.** Estimate local repairability through fixed-budget prefix resampling and use it to weight process supervision.

**Cheapest falsification experiment.** On verified math/code traces, compare outcome labels, direct process labels, repairability weighting, and a direct supervised failure predictor.

**Likely strongest baseline.** Process reward models, direct error localization, prefix consistency, direct Monte Carlo repair probability, and outcome-only RL.

**Most likely prior-art collision.** This is precisely a recoverability/value-of-prefix estimator and fails the repository’s direct-Monte-Carlo and direct-predictor checks; recent prefix-consistency methods already use resampling evidence. citeturn524362search1turn391566view3

**Estimated compute and wall-clock.** 12–30 GPU-hours; one day.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Incremental process-supervision result.

**Status.** **KILL.**

### C12. Raw-evidence insurance span — agent memory

**One-sentence hypothesis.** A compressed agent memory should reserve a small raw-evidence span chosen for query-shift coverage rather than summarize every event.

**Counterintuitive element.** One uncompressed exception can be more valuable than a longer learned summary.

**Causal intervention.** Under the same memory-token budget, compare all-summary, all-raw retrieval, hybrid raw-plus-summary, and an oracle retention selector.

**Cheapest falsification experiment.** Run LongMemEval-style or multi-session QA with controlled future queries that target information lost during compression.

**Likely strongest baseline.** Retain-versus-consolidate policies, LeanMem-style sparse memory, agent-native raw records, and query-time retrieval from the full transcript.

**Most likely prior-art collision.** Recent systems already formalize retention versus consolidation and hybrid raw/compact storage. citeturn426843search6turn426843search14turn426843search2turn426843search10

**Estimated compute and wall-clock.** 4–16 GPU-hours; one day.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Memory-system ablation.

**Status.** **KILL.**

### C13. Commitment-order gating — masked-diffusion language models

**One-sentence hypothesis.** A diffusion language model should delay token commitment when support from neighboring latent variables is not yet available.

**Counterintuitive element.** Solving the apparently easiest token first can reduce final correctness.

**Causal intervention.** Keep denoising steps fixed and replace confidence-first commitment with frontier-gated, deferred, or learned ordering.

**Cheapest falsification experiment.** Evaluate a public masked-diffusion LM on arithmetic or code completion with token-order traces.

**Likely strongest baseline.** Answer-first diagnostics, Deferred Commitment Decoding, learned token-commitment policies, and oracle order.

**Most likely prior-art collision.** The exact phenomenon and obvious remedy are directly occupied by 2026 work on commitment order. citeturn426843search3turn426843search27turn426843search19turn426843search15turn426843academia36

**Estimated compute and wall-clock.** 8–20 GPU-hours; one day.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Replication.

**Status.** **KILL.**

### C14. Deliberately undercomplete proposer — multi-agent critique

**One-sentence hypothesis.** A proposer can elicit a more diagnostic critic by intentionally withholding one decisive step rather than presenting its best complete solution.

**Counterintuitive element.** A weaker first answer could improve the final answer.

**Causal intervention.** At equal total tokens, compare complete proposals, randomly truncated proposals, strategically omitted proposals, and direct targeted questions to the critic.

**Cheapest falsification experiment.** Use public math/code tasks and two open models in proposer–critic–revision loops.

**Likely strongest baseline.** Debate, adversarial critique, intentionally flawed-solution training, direct error localization, and active query selection.

**Most likely prior-art collision.** The idea reduces to active teaching, adversarial critique, and information-seeking dialogue; a direct targeted critic prompt is the obvious stronger baseline.

**Estimated compute and wall-clock.** 4–16 GPU-hours; one day.

**Preliminary novelty score.** 1/5.

**Likely publication ceiling.** Prompting/debate ablation.

**Status.** **KILL.**

### C15. Closed-loop bracket accessibility — activation steering and internal computation

**One-sentence hypothesis.** Two state-dependent activation controls can have a closed commutator loop whose first-order action cancels but whose second-order displacement changes model behavior in a direction outside their entire matched static span.

**Counterintuitive element.** Four control actions with zero first-order sum can create a stable, sign-reversible behavioral change that neither control nor any static combination can produce.

**Causal intervention.** Apply \(+U,+V,-U,-V\) as numerical flows at a fixed residual-stream location; compare the reversed loop, static source-span oracle, random zero-sum loops, constant-field controls, and direct nonlinear target steering.

**Cheapest falsification experiment.** Learn smooth concept fields on frozen 2–3B models, compute their bracket with JVPs, preregister three source-pair/target triples on a development model, and confirm the predicted sign, \(\epsilon^2\) scaling, and out-of-span displacement on a second model family.

**Likely strongest baseline.** Direct target steering, Steering Vector Fields, ODESteer, feedback control, INNSteer/FLAS, and an optimized static source-span oracle.

**Most likely prior-art collision.** Every ingredient around it is occupied: Wilson-loop diagnostics, feed-forward commutator defects, Lie-bracket order effects, nonlinear vector-field steering, and closed-loop control. The residual difference is active second-order behavioral accessibility outside the first-order span. citeturn794313search0turn794313search1turn595905search7turn595905academia33turn595905academia35turn595905search2turn595905search19

**Estimated compute and wall-clock.** 25–60 GPU-hours for Stage 0; 12–24 wall-clock hours using four GPUs. A one-to-two-week confirmation package is estimated at 120–220 GPU-hours.

**Preliminary novelty score.** 3/5 before Stage 0, falling to 1/5 if direct nonlinear steering matches it.

**Likely publication ceiling.** Strong ICLR poster if the causal law, span expansion, and useful control advantage replicate; oral potential only if there is a clean theorem and cross-family behavioral consequence.

**Status.** **ADVANCE TO STAGE 0 ONLY.**

### C16. Partial-orbit closure gap — representation learning and augmentation

**One-sentence hypothesis.** Training on a small non-closed subset of a symmetry orbit can generalize worse than no augmentation, whereas completing the orbit restores invariance.

**Counterintuitive element.** Two valid augmentations could be worse than zero or many.

**Causal intervention.** Fix total samples and vary whether observed transformations form a generating set, a non-closed subset, or a full group orbit.

**Cheapest falsification experiment.** Rotated-MNIST/CIFAR plus one public text transformation benchmark; compare standard networks, equivariant networks, and consistency regularization.

**Likely strongest baseline.** Group-equivariant architectures, full-orbit augmentation, augmentation weighting, and direct invariance regularization.

**Most likely prior-art collision.** Group closure, orbit coverage, augmentation bias, and symmetry mismatch are established theory; a non-monotonic curve alone is unlikely to be a contribution.

**Estimated compute and wall-clock.** 12–30 GPU-hours; one day.

**Preliminary novelty score.** 2/5.

**Likely publication ceiling.** Theory/augmentation workshop.

**Status.** **KILL.**

### C17. Mode-count valley — conditional generative modeling

**One-sentence hypothesis.** Under matched entropy and sample count, a conditional generator may learn two or three disconnected valid modes less reliably than either one mode or a dense family of valid modes.

**Counterintuitive element.** More ambiguity can eventually make generation easier.

**Causal intervention.** Construct distributions with controlled mode count, separation, support topology, and total entropy; train diffusion/flow models at fixed compute.

**Cheapest falsification experiment.** Synthetic mixtures plus a compositional image benchmark with verified mode labels.

**Likely strongest baseline.** Exact mixture likelihood, mode-balanced sampling, entropy regularization, and a direct latent-mixture model.

**Most likely prior-art collision.** Mode collapse, disconnected-support topology, score-field phase transitions, and mixture identifiability already cover the likely explanations; the natural-benchmark bridge is weak.

**Estimated compute and wall-clock.** 12–40 GPU-hours; one to two days.

**Preliminary novelty score.** 2/5.

**Likely publication ceiling.** Theory workshop unless a natural cross-domain law appears.

**Status.** **KILL.**

## 4. Literature collision table

The six candidates below were the strongest before the final collision audit.

| Candidate | Closest primary papers | Exact conceptual overlap | Exact remaining difference | Substantive or cosmetic? | Final status |
|---|---|---|---|---|---|
| **C15 — Closed-loop bracket accessibility** | [Inverse-Free Wilson Loops for Transformers](https://arxiv.org/abs/2510.08648); [First-Order Predictable but Pairwise Fragile](https://arxiv.org/abs/2607.16821); [Feed-Forward Steering in Transformer Residual Dynamics](https://arxiv.org/abs/2608.02071); [Steering Vector Fields](https://arxiv.org/abs/2602.01654); [ODESteer](https://arxiv.org/abs/2602.17560) | Wilson loops use activation commutators to diagnose order sensitivity; the pairwise-fragility paper uses Lie brackets to predict update order; feed-forward steering treats blocks as local fields and measures commutator defects; SVF and ODESteer provide state-dependent nonlinear controls. citeturn794313search0turn794313search1turn595905search7turn595905academia33turn595905academia35 | Use the **group commutator itself as a controlled inference-time intervention**, require its displacement to lie substantially outside the source-field span, predict the effect out of sample, and show a behavior–utility advantage over every equal-budget static and nonlinear baseline. | **Potentially substantive, but only conditionally.** If the result is merely noncommutativity, quadratic scaling, or a qualitative order effect, it is cosmetic and already implied by the cited work. | **ADVANCE** to one preregistered kill test. |
| **C8 — Output-equivalence multiplicity valley** | [Reasoning Path Divergence](https://arxiv.org/abs/2510.26122); [SFT Conflicts, RL Coexists](https://arxiv.org/abs/2608.03573); [Preserving Diversity in Supervised Fine-Tuning](https://arxiv.org/abs/2408.16673); [Generalization in LLM Problem Solving](https://arxiv.org/abs/2604.15306); [Dynamic Policy Optimization with Multiple Solution Paths](https://arxiv.org/abs/2604.08926) | These works already study path diversity, SFT collapse or gradient conflict, diversity-preserving objectives, distinct-problem versus multi-solution supervision, and post-training on multiple solution paths. citeturn426843academia35turn426843search16 | A controlled **non-monotonic law in the number of verified equivalent algorithms** at fixed problems, tokens, and optimization steps, with a mechanism predicting why \(K=2\) or \(4\) is worse than both \(K=1\) and large \(K\). | **Uncertain.** The curve could be new, but unless it survives route labels, answer-only RL, sequence-level marginalization, gradient surgery, and distinct-problem controls, the difference is an ordinary one-to-many/SFT-conflict effect. | **HOLD.** |
| **C1 — Family-correlated search saturation** | [Prefix Consistency](https://arxiv.org/abs/2605.07654); [Slim-SC](https://arxiv.org/abs/2509.13990); [Diversity-Aware Test-Time Scaling / ADAPT](https://arxiv.org/abs/2506.04611); confidence-aware self-consistency and adaptive rollout-allocation work | All treat reasoning samples as non-independent, regenerate or compare prefixes, prune redundant chains, or allocate computation according to diversity/confidence. citeturn524362search1turn524362search18turn426843academia37 | An explicit genealogy-adjusted effective-sample-size estimator and lineage quota. | **Cosmetic/computational.** The estimator may be useful, but the mechanism and intervention are occupied and a direct Monte Carlo/clustered baseline is obvious. | **KILL.** |
| **C12 — Raw-evidence insurance span** | [Retain or Consolidate?](https://arxiv.org/abs/2607.17545); [LeanMem](https://arxiv.org/abs/2608.03463); [Are We Ready for an Agent-Native Memory System?](https://arxiv.org/abs/2606.24775); [ScrapMem](https://arxiv.org/abs/2605.03804); [Maintainable Topic Documents](https://arxiv.org/abs/2606.10677) | These systems already separate raw records from abstractions, decide what to retain or consolidate, maintain compact persistent documents, and evaluate long-term memory under budget. citeturn426843search6turn426843search14turn426843search2turn426843search10turn426843search32 | Force the memory to keep exactly one raw “insurance span” selected for query-shift coverage. | **Cosmetic.** This is a retention policy inside an occupied hybrid-memory design space, and full raw retrieval plus an oracle selector are immediate baselines. | **KILL.** |
| **C13 — Commitment-order gating in diffusion LMs** | [Answer First, Reason Later](https://arxiv.org/abs/2608.05687); [Deferred Commitment Decoding](https://arxiv.org/abs/2601.02076); [The Path Matters](https://arxiv.org/abs/2605.24697); [Premature Commitment in Diffusion Language Models](https://openreview.net/forum?id=xe6TPinNwJ); [Commitment Before Realization](https://arxiv.org/abs/2608.08082) | The papers directly analyze when tokens become fixed, show that early answer commitment can outrun supporting reasoning, and propose deferred, gated, or learned commitment schedules. citeturn426843search3turn426843search27turn426843search19turn426843search15turn426843academia36 | Recast the policy as preserving an acceptable continuation corridor after unpredictable commitments. | **Purely cosmetic.** The formulation, intervention, and evaluation are already present. | **KILL.** |
| **C2 — Evidence-family saturation in RAG** | [How Retriever Redundancy and Diversity Impact RAG Effectiveness](https://arxiv.org/abs/2608.13956); [Shifting from Ranking to Set Selection for RAG](https://arxiv.org/abs/2507.06838); [DF-RAG](https://arxiv.org/abs/2601.17212); [Byte-Exact Deduplication in RAG](https://arxiv.org/abs/2605.09611) | Controlled duplicate/paraphrase/diversity experiments and retrieval-set optimization already target evidence redundancy, source coverage, and duplicate-induced waste. citeturn524362search11turn524362search20turn524362search24turn524362search14 | Call a provenance cluster an “evidence lineage” and estimate its effective sample size. | **Cosmetic.** The vocabulary changes; the problem, intervention, and strongest baselines do not. | **KILL.** |

### Collision verdict

Only C15 retains a possibly substantive delta, and even that delta is a **conjunction of requirements**, not a paper claim granted in advance. C8 retains a factual uncertainty—whether the route-count curve is genuinely non-monotonic—but not enough novelty confidence or dataset readiness to justify immediate execution. The other four are already occupied at the level of formulation, intervention, and baseline.


## 5. Reviewer red-team

Only Seed A is marked ADVANCE.

### Seed A — strongest skeptical ICLR objection

> **“This is the Baker–Campbell–Hausdorff formula and classical nonholonomic control applied to activation steering. Recent papers already supply activation commutators, Lie-bracket order diagnostics, state-dependent steering fields, ODE steering, and feedback control. A four-step loop will inevitably exhibit a second-order residual in a nonlinear system. The reported behavior change will either be numerical integration error, a learned-probe artifact, activation-norm mismatch, or something a direct nonlinear target controller can match more simply.”**

This objection is strong. It is not answered by a statistically significant accuracy delta.

### Experiment that would validate the objection

The objection is validated—and the seed is killed—if any of the following occurs:

1. **No geometric isolation.** The loop displacement is mostly inside \(\operatorname{span}\{U,V\}\), or an optimized static source-span intervention matches it.
2. **No second-order law.** The observed behavior scales approximately linearly with \(\epsilon\), fails to reverse under loop reversal, or changes materially with numerical integrator step size.
3. **No out-of-sample prediction.** \(g_T(h)^\top[U,V](h)\), or the corresponding finite-output estimator, does not predict the sign and rank of held-out behavioral effects.
4. **Probe construction explains the result.** The effect appears for MLP-gradient fields but disappears for model-native output-gradient fields, or vice versa, with no coherent explanation.
5. **Ordinary nonlinear steering subsumes it.** ODESteer, SVF, INNSteer/FLAS, a direct target field, or a four-step open-loop optimizer matches the target effect and utility at equal labels, forward/backward calls, and intervention norm.
6. **Pair fishing explains it.** The result requires testing hundreds of source pairs and reporting a few uncorrected successes, or the selected pair does not transfer from discovery model to confirmation model.
7. **Only a toy task works.** The effect is clear in an analytic vector field or synthetic token classifier but absent on natural text and public behavioral benchmarks.
8. **The source fields drift.** The “closed” loop leaves large first-order source-attribute changes, so its apparent target effect is ordinary additive steering.
9. **The model family is singular.** The effect appears in one architecture, checkpoint, or layer but not a second model family under the same preregistered protocol.

### Result required to survive the objection

Seed A survives Stage 0 only if all of the following are true:

- **Two-family replication:** the locked effect appears in at least two independently trained model families.
- **Three confirmed triples:** at least three preregistered source-pair/target triples satisfy all gates after development selection is frozen.
- **Quadratic scaling:** over at least three safe intervention scales, the log–log slope of target effect versus \(\epsilon\) lies in \([1.7,2.3]\).
- **Sign reversal:** reversing the loop reverses the target-effect sign on at least 70% of held-out examples and in the aggregate for every confirmed triple.
- **Bracket prediction:** held-out sign prediction is at least 70%, and Spearman correlation between predicted and observed effect is at least \(0.50\), with a bootstrap 95% lower bound above \(0.25\).
- **Out-of-span geometry:** median \(\rho\ge 0.35\), and an equal-norm optimized source-span oracle recovers less than 80% of the target effect at matched source drift.
- **Negative controls:** constant fields, shuffled labels, random matched-norm fields, and zero-bracket analytic controls yield effects statistically indistinguishable from zero after multiplicity correction.
- **Numerical convergence:** RK2 and RK4 agree within 10% on effect size, while halving step size changes the estimate by less than 10%.
- **Useful consequence:** at least one of the following holds:
  1. the bracket basis reaches a held-out target without target-field training while all equal-information static baselines fail; or
  2. under equal target labels, it improves the target-effect/source-drift Pareto area by at least 10% over the best direct nonlinear controller.
- **Natural-task confirmation:** the result survives at least one public behavioral benchmark rather than only probe scores.

### Why the contribution would not merely be an existing method under a new name

It would be distinct only if the paper establishes all three levels below:

1. **A causal empirical law:** zero-first-order closed controls produce predictable, reversible, second-order behavior changes in frozen transformers.
2. **An identifiability test:** the behavior is tied to the bracket residual outside the source span, not to norm, integration error, or generic nonlinearity.
3. **An algorithmic consequence:** a small library of learned controls gains usable behavioral directions through Lie closure that the strongest equal-information static and nonlinear baselines do not recover.

Wilson-loop and feed-forward-commutator papers establish diagnostics of curvature or order sensitivity; the sequential-update paper establishes pairwise order effects; SVF, ODESteer, INNSteer, and feedback-control papers establish nonlinear or closed-loop steering. They do not, on the evidence found, jointly establish an inference-time **closed commutator as an active behavior synthesizer**, prove that the resulting behavioral displacement is outside the source-control span, and demonstrate an equal-budget control advantage. citeturn794313search0turn794313search1turn595905search7turn595905academia33turn595905academia35turn595905search2turn595905search19

That boundary is narrow enough that Stage 0 must be treated as an attempted falsification, not the beginning of a positive narrative.

## 6. Final shortlist

### Seed A. **Can Zero-Net Activation Loops Create New Behavioral Control Directions?**

#### 1. Precise title-like research question

**Behavioral Lie Closure in Frozen Transformers: Can Zero-First-Order Activation Loops Reach Behavior Directions Outside Static Steering Spans?**

#### 2. One-sentence publishable claim

> Across independently trained transformer families, a closed commutator loop of two context-dependent activation fields produces predictable, sign-reversible, second-order behavior changes outside their static steering span, and a bracket-augmented control basis improves multi-attribute steering at fixed labels, intervention steps, activation norm, and utility.

The sentence is publishable only if every clause is supported. Dropping “outside their static steering span” or “fixed labels and intervention steps” makes the result too close to existing work.

#### 3. Why the result would be counterintuitive

Most activation-steering practice treats controls as vectors or smooth directions whose effects are composed additively or optimized directly. Under that mental model, applying \(+U,+V,-U,-V\) should approximately cancel. The seed predicts that cancellation occurs only at first order. State dependence and curvature leave a structured second-order residual; reversing the loop reverses it. A model could therefore exhibit a stable behavior change even though the nominal control sum is zero and neither source control points toward that behavior.

The striking result is not “a nonlinear network is nonlinear.” It is:

- the effect has a prescribed quadratic scaling law;
- its sign is predictable before executing the loop;
- the displacement lies outside the source span;
- it survives matched nonlinear baselines;
- it produces a useful control direction rather than merely a hidden-state difference.

#### 4. Closest prior work and exact novelty boundary

The closest works are:

1. [Inverse-Free Wilson Loops for Transformers](https://arxiv.org/abs/2510.08648), which uses activation-level commutators and curvature-like diagnostics to identify order sensitivity.
2. [Feed-Forward Steering in Transformer Residual Dynamics](https://arxiv.org/abs/2608.02071), which treats feed-forward blocks as local steering fields and uses commutator defects to assess additive-flow approximations.
3. [First-Order Predictable but Pairwise Fragile](https://arxiv.org/abs/2607.16821), which analyzes order sensitivity of sequential task updates with Lie brackets.
4. [Steering Vector Fields](https://arxiv.org/abs/2602.01654), which replaces fixed vectors with context-dependent differentiable fields.
5. [ODESteer](https://arxiv.org/abs/2602.17560), [Activation Steering with a Feedback Controller](https://arxiv.org/abs/2510.04309), and [INNSteer](https://arxiv.org/abs/2606.08454), which already occupy multi-step, feedback, and nonlinear steering. citeturn794313search0turn794313search1turn595905search7turn595905academia33turn595905academia35turn595905search2turn595905search19

The exact novelty boundary is:

> **Not** commutator measurement, order sensitivity, nonlinear steering, ODE integration, feedback, or multi-attribute composition.
> **Only** active group-commutator steering that demonstrates behaviorally useful Lie-closure directions outside all matched first-order source spans, with out-of-sample prediction and equal-budget superiority.

If a paper can be honestly summarized as “we apply Lie brackets to activation steering,” it should not be submitted.

#### 5. Proposed mechanism

Let \(M\) be a frozen transformer and \(h_\ell(x)\in\mathbb R^d\) the residual-stream state at a fixed layer \(\ell\).

For a behavioral concept \(c\), construct a smooth scalar score \(f_c(h)\). Two field constructions must be tested:

1. **Probe-gradient field**
   \[
   U_c(h)=
   \frac{\nabla_h f_c(h)}
   {\|\nabla_h f_c(h)\|_2+\eta},
   \]
   where \(f_c\) is a small, regularized nonlinear probe trained on frozen activations.

2. **Model-native output field**
   \[
   U_c(h)=
   \frac{\nabla_h \mathcal L_c(M_{\ell:}(h))}
   {\|\nabla_h \mathcal L_c(M_{\ell:}(h))\|_2+\eta},
   \]
   where \(\mathcal L_c\) is a differentiable logit-level objective defined from public labels or token sets.

The two constructions separate model geometry from probe-induced curvature.

For source concepts \(a,b\), define \(U=U_a\) and \(V=U_b\). Estimate

\[
[U,V](h)
=
J_V(h)U(h)-J_U(h)V(h)
\]

using Jacobian–vector products, without materializing dense Jacobians. Then integrate the closed loop

\[
\mathcal C_\epsilon
=
\Phi^V_{-\epsilon}
\circ
\Phi^U_{-\epsilon}
\circ
\Phi^V_{\epsilon}
\circ
\Phi^U_{\epsilon}.
\]

The central predictions are:

\[
\mathcal C_\epsilon(h)-h
=
\epsilon^2[U,V](h)+O(\epsilon^3),
\]

\[
\mathcal C_\epsilon^{\mathrm{reverse}}(h)-h
=
-\epsilon^2[U,V](h)+O(\epsilon^3),
\]

and, for a target behavior score \(s_t\),

\[
\Delta s_t
\approx
\epsilon^2
\nabla_h s_t(h)^\top[U,V](h).
\]

The mechanism is meaningful only when

\[
\rho(h)=
\frac{\|(I-P_{\mathcal S(h)})[U,V](h)\|_2}
{\|[U,V](h)\|_2+\delta}
\]

is substantial and predicts the target effect. A large bracket entirely inside \(\mathcal S(h)\) is not new accessibility; it is a complicated way to reproduce the source span.

#### 6. Rival explanations

At least the following rival explanations must be preregistered:

1. **Integration artifact:** Euler or large-step numerical error creates a fake residual.
2. **Probe artifact:** nonlinear probe curvature, not transformer computation, creates the bracket.
3. **Norm artifact:** the four-step loop simply injects more total activation energy.
4. **Layer mismatch:** additions at different integration substeps are not meaningfully comparable.
5. **Source drift:** first-order source effects do not truly cancel.
6. **Generic Hessian effect:** any matched nonlinear perturbation produces the same target change.
7. **Pair-selection overfitting:** a large search over field pairs guarantees apparent third-concept effects.
8. **Classifier leakage:** the target evaluation probe shares training data or architecture with the source fields.
9. **Decoder sensitivity:** a small hidden-state difference is amplified stochastically but not behaviorally stable.
10. **Known controller equivalence:** a direct SVF/ODE/feedback controller reaches the same point with no bracket-specific advantage.
11. **Prompt-specific routing:** the effect is caused by a few lexical templates or refusal phrases.
12. **Model-specific pathology:** one checkpoint has unusually curved representations.

Each rival has a corresponding control below.

#### 7. Controlled causal experiment

##### 7.1 Models

Use two primary model families from the start:

- **Gemma-2-2B-it**
- **Qwen2.5-3B-Instruct**

A third architecture, such as Pythia-2.8B or another public 2–3B decoder-only transformer, is optional only after the two-family gate is passed. Stage 0 must not begin with 7–9B models or a broad architecture sweep.

Both primary models fit comfortably on a 24 GB card in BF16 with batch-size-one gradient/JVP evaluation and activation checkpointing. This is an engineering estimate, not a promise; the implementation must measure peak allocated memory during the smoke test.

##### 7.2 Public data and concept fields

Use a locked subset of [AxBench](https://arxiv.org/abs/2501.17148) concepts for field construction and automated behavior scoring, supplemented by one natural behavioral benchmark:

- [SteeringSafety](https://arxiv.org/abs/2509.13450) for helpfulness/refusal trade-offs; or
- [TruthfulQA](https://arxiv.org/abs/2109.07958) for truthfulness-related confirmation.

AxBench exists specifically to compare representation-steering methods and supplies public concept data and evaluation infrastructure; SteeringSafety evaluates safety steering and utility trade-offs. citeturn833044search0turn794313search25

Use three disjoint partitions:

- **field-train:** learn source and target scorers;
- **discovery-dev:** estimate brackets and select exactly three candidate triples;
- **locked-confirmation:** never used for pair selection, threshold tuning, layer selection, or \(\epsilon\) selection.

The discovery stage may evaluate a matrix of source pairs, but multiplicity correction is mandatory. The exact three triples, layer, scales, and scorer definitions are frozen before the confirmation model is run.

##### 7.3 Interventions

For each source pair \((U,V)\), run:

1. **Forward loop:** \(+U,+V,-U,-V\).
2. **Reverse loop:** \(+V,+U,-V,-U\).
3. **Static source-span oracle:** optimize \(\alpha U(h)+\beta V(h)\) on discovery-dev under matched final activation norm and source drift.
4. **Four-step static control:** apply frozen \(U(h_0)\) and \(V(h_0)\) values in the same four-step schedule; because the fields are constant, the bracket should vanish.
5. **Random zero-sum loop:** random fields matched in per-step norm and smoothness.
6. **Label-shuffled fields:** source probes trained on shuffled labels.
7. **Direct target vector:** a standard mean-difference or linear steering vector using the same target labels.
8. **Direct target SVF:** state-dependent target field with the same target labels.
9. **ODESteer or equivalent multi-step nonlinear target control:** equal number of field evaluations and equal total integration budget.
10. **Unconstrained activation perturbation oracle:** a small dev-optimized perturbation with the same norm, used only as an upper bound.
11. **No-intervention and repeated-forward controls.**

All methods receive the same prompts, decoding seed, maximum new tokens, field-training labels, and number of forward/backward field evaluations. If one method uses four field evaluations, the others receive four. A baseline may not be weakened to preserve the bracket method’s advantage.

##### 7.4 Numerical protocol

- Integrate with both RK2 and RK4.
- Use at least three intervention scales selected on discovery-dev.
- Require no significant fluency collapse or runaway activation norm.
- Record the full hidden-state path and per-step source/target scores.
- Verify the analytic/JVP bracket against finite-difference estimates on a small batch.
- Include an analytic toy vector field with known nonzero bracket and a constant-field system with exact zero bracket as unit tests.
- Use deterministic greedy or fixed-seed sampling for the primary causal analysis; stochastic generation is secondary.
- Save model revision, tokenizer revision, dataset hashes, prompt IDs, layer, random seed, dtype, integrator, tolerances, and all norms in a machine-readable manifest.

#### 8. Natural public benchmark

The natural bridge is a two-part benchmark:

1. **Controlled steering:** AxBench concept pairs, because it permits broad concept coverage and automated held-out scoring.
2. **Behavioral utility:** SteeringSafety or TruthfulQA, because a hidden-state effect that does not survive a public behavioral task is insufficient.

The paper cannot rely only on synthetic vector fields, token classifiers, or bespoke prompts.

#### 9. Strong baselines and equal-compute rules

The mandatory baseline set is:

- zero intervention;
- individual \(U\) and \(V\);
- all optimized static combinations \(\alpha U+\beta V\);
- random and label-shuffled zero-sum loops;
- constant-field loop;
- direct target mean-difference vector;
- direct target linear probe gradient;
- direct target SVF;
- ODESteer or an equivalent multi-step adaptive controller;
- INNSteer or FLAS if implementation is stable within the 72-hour envelope;
- four-step open-loop optimization with the same number of field evaluations;
- target-supervised activation perturbation upper bound.

Equal-compute rules:

- identical model and tokenizer;
- identical prompt and decoding budgets;
- identical source and target labels;
- identical number of field evaluations;
- identical total intervention substeps;
- matched final activation norm and, separately, matched path-integrated norm;
- no target-test labels for field-pair selection;
- no larger evaluator or proprietary judge for the proposed method;
- the direct-target baseline receives every target label used by the bracket method;
- all reported pair selection uses development data and is confirmed once.

#### 10. Primary and secondary metrics

##### Primary metrics

1. **Held-out target behavior effect**
   \[
   \Delta_t =
   \mathbb E[s_t(y_{\mathrm{loop}})-s_t(y_{\mathrm{base}})].
   \]

2. **Out-of-span accessibility ratio**
   \[
   \rho =
   \frac{\|(I-P_{\mathcal S})[U,V]\|}
   {\|[U,V]\|+\delta}.
   \]

3. **Bracket prediction accuracy**
   - sign accuracy of \(\nabla s_t^\top[U,V]\);
   - Spearman correlation between predicted and observed example-level effect.

4. **Reversal consistency**
   \[
   \Delta_t^{\mathrm{forward}}
   \approx
   -\Delta_t^{\mathrm{reverse}}.
   \]

5. **Quadratic scaling exponent**
   from a log–log regression of \(|\Delta_t|\) on \(\epsilon\).

6. **Pareto area**
   under target improvement versus source-attribute drift or utility loss.

##### Secondary metrics

- source-concept drift for \(a\) and \(b\);
- KL divergence from unsteered logits;
- perplexity or token-level NLL;
- generation fluency and repetition;
- refusal false-positive and false-negative rates;
- TruthfulQA or benchmark accuracy;
- activation norm and path length;
- layer-to-layer transfer;
- prompt-template transfer;
- concept-pair sparsity;
- runtime and peak VRAM.

#### 11. Required ablations

1. Layer sweep restricted to three preregistered candidate layers.
2. Field construction: MLP-gradient versus model-native output-gradient.
3. Probe capacity and regularization.
4. Normalized versus unnormalized fields.
5. Euler, RK2, and RK4.
6. One, three, and five safe \(\epsilon\) scales.
7. Forward versus reversed loop.
8. Constant-field versus state-dependent field.
9. Full bracket versus source-span projection versus orthogonal residual only.
10. Source-pair order.
11. Dev-selected versus randomly chosen pairs.
12. Same-model confirmation versus cross-model confirmation.
13. Static source-span oracle.
14. Direct target vector, SVF, and ODE controller.
15. Matched final norm versus matched path-integrated norm.
16. Greedy decoding versus fixed-seed sampling.
17. Target-probe architecture independence.
18. Prompt paraphrases and held-out templates.
19. Field training-set size.
20. Removing any one loop segment, which should destroy the clean commutator signature.

#### 12. OOD and stress tests

- **Model-family OOD:** discover on Gemma, confirm on Qwen without retuning; then swap directions if time.
- **Prompt OOD:** held-out paraphrase templates and topic domains.
- **Layer OOD:** neighboring layers using the same frozen settings.
- **Scale OOD:** one \(\epsilon\) just outside the fitted range to test the breakdown of the quadratic approximation.
- **Field OOD:** source fields learned from one prompt family and evaluated on another.
- **Behavior OOD:** confirm at least one target through an independent public metric rather than the training scorer.
- **Adversarial norm control:** random perturbations with equal final and path-integrated norms.
- **Integrator stress:** tighter tolerances and step subdivision.
- **Decoding stress:** greedy, low-temperature, and fixed-seed sampling.
- **Utility stress:** benign-helpfulness prompts to detect overrefusal or generic style drift.

#### 13. Preregistered Stage 0 kill test

Stage 0 is a single discovery–confirmation protocol.

**Discovery model:** Gemma-2-2B-it.

**Confirmation model:** Qwen2.5-3B-Instruct.

**Fields:** 8–12 locked AxBench concepts.

**Candidate layers:** three fixed middle-to-late residual-stream layers.

**Scales:** three safe scales selected before confirmation.

**Discovery output:** exactly three ordered source-pair/target triples, one layer per triple, one scale range, and frozen evaluation code.
**Confirmation:** one run; no reselection, no threshold relaxation, no prompt additions.

The Stage 0 report must contain:

- all tested pairs, not only successes;
- multiplicity-adjusted confidence intervals;
- full numerical-control results;
- direct and nonlinear baseline tables;
- per-model and pooled results;
- machine-readable manifests;
- a binding GO/NO-GO decision.

#### 14. Quantitative GO/NO-GO thresholds

**GO only if every condition below passes:**

| Gate | Required result |
|---|---|
| Replication | At least 3/3 preregistered triples pass on both model families. |
| Effect size | At least \(0.20\) standardized target-score units or 5 percentage points, whichever metric is preregistered, without more than 2 percentage points utility loss on the matched public task. |
| Reversal | Aggregate sign reverses for every triple; example-level sign reversal at least 70%. |
| Scaling | Estimated exponent in \([1.7,2.3]\) with no evidence that a linear model fits equally well. |
| Prediction | Held-out sign accuracy at least 70%; Spearman \(r\ge0.50\), bootstrap 95% lower bound \(>0.25\). |
| Geometry | Median \(\rho\ge0.35\); 75th percentile \(\rho\ge0.50\). |
| Span baseline | Best static source-span oracle recovers under 80% of the target effect at matched source drift and norm. |
| Numerical controls | RK2/RK4 differ by under 10%; halving step size changes effect by under 10%; constant-field and analytic-zero controls are null. |
| Multiplicity | All significance claims survive Benjamini–Hochberg FDR \(q=0.05\) over discovery tests and untouched confirmation. |
| Direct nonlinear baseline | Bracket basis improves target/utility Pareto area by at least 10%, or reaches a target under a zero-target-training setting that all equal-information baselines fail to reach. |
| Natural benchmark | At least one confirmed effect survives SteeringSafety, TruthfulQA, or another locked public task. |
| Compute | Stage 0 completes within 60 GPU-hours. |

**Automatic NO-GO if any of these occurs:**

- fewer than three triples survive confirmation;
- no reversed-sign effect;
- scaling is first-order or unstable;
- the bracket residual is mostly in the source span;
- an equal-budget direct nonlinear controller matches the result;
- only probe scores move while public behavior does not;
- pair selection leaks confirmation data;
- the result requires a larger model, proprietary judge, or extra labels;
- the central effect is present only in one checkpoint or one prompt family;
- the computation exceeds 60 GPU-hours before the central gate is passed.

No threshold may be relaxed after seeing confirmation results.

#### 15. Estimated GPU memory, GPU-hours, and wall-clock time

| Component | Peak VRAM estimate | GPU-hours | Wall-clock with parallelism |
|---|---:|---:|---:|
| Environment, data extraction, activation cache smoke tests | 8–14 GB/GPU | 2–4 | 2–4 h |
| Field training and validation | 10–16 GB/GPU | 4–8 | 2–4 h |
| JVP/bracket and numerical-control tests | 12–20 GB/GPU | 6–12 | 3–6 h |
| Gemma discovery matrix | 12–20 GB/GPU | 8–16 | 4–8 h on 2–4 GPUs |
| Qwen locked confirmation | 12–20 GB/GPU | 8–16 | 4–8 h on 2–4 GPUs |
| Strong baselines and analysis | 12–20 GB/GPU | 6–12 | 4–8 h |
| **Stage 0 total** | **under 24 GB/GPU target** | **34–60** | **12–24 h active compute; under 72 h end-to-end** |

A full initial evidence package, if Stage 0 passes, is estimated at 120–220 GPU-hours over one to two weeks. That package would add a third model family, more public concepts, independent scorer architectures, and complete strong-baseline replication. It should not begin before Stage 0 passes.

#### 16. Likely publication ceiling if everything works

- **Only a hidden-state geometric effect:** workshop or reject.
- **Cross-model causal law, but direct nonlinear baselines match:** borderline ICLR poster at best.
- **Causal law plus reliable out-of-span prediction and a useful bracket basis:** credible ICLR poster.
- **Clean theorem, broad cross-family replication, and a result that materially changes how compositional activation control is designed:** strong poster; oral is plausible but remains a low-probability ceiling, not the expected outcome.

#### 17. Weakest link that could still kill the paper

The weakest link is **algorithmic consequence**. The second-order residual is mathematically expected in state-dependent nonlinear fields. Even if it is measured perfectly, an ICLR reviewer can still say:

> “Interesting geometry, but a direct nonlinear target controller gets the same behavior more simply.”

Therefore, the paper dies unless bracket closure either reaches behavior directions unavailable under equal-information direct controls or produces a reproducibly better target–utility frontier. Geometry alone is not enough.

## 7. Cross-seed comparison

Only one seed survived into the final shortlist. C8 remains a HOLD and is deliberately excluded from the shortlist because its most likely explanation is already covered by SFT-conflict and diversity literature.

| Dimension | Seed A — Closed-Loop Bracket Steering |
|---|---|
| Novelty | **3/5 before Stage 0.** Narrow but real residual boundary; falls to 1/5 if static or nonlinear baselines match. |
| Counterintuitive strength | **5/5.** A zero-first-order closed loop causing sign-reversible behavior outside the source span is easy to state and visually compelling. |
| Causal identifiability | **5/5.** Reversal, \(\epsilon^2\) scaling, JVP prediction, span projection, and constant-field controls provide unusually sharp tests. |
| Speed of falsification | **5/5.** Numerical or baseline failure should be visible within the first 24–52 hours. |
| Engineering burden | **3/5.** Autograd/JVP hooks and numerical integration are nontrivial, but the system is frozen-model inference rather than training a large model. |
| Fit to eight RTX 4090 GPUs | **5/5.** Stage 0 needs at most four GPUs concurrently and remains well below the hardware ceiling. |
| Strength of public baselines | **4/5.** SVF, ODESteer, feedback control, INNSteer/FLAS, AxBench, and SteeringSafety make the test hard to game. |
| Dependence on proprietary systems | **5/5.** None required. Models, datasets, metrics, and evaluators can remain open. |
| ICLR fit | **4/5.** The seed combines internal computation, causal intervention, representation geometry, and a possible control algorithm. |
| Plausible oral potential | **2/5 before evidence.** It rises only if a theorem and broad control consequence survive; the default ceiling is poster. |

## 8. Binding recommendation

### **RUN SEED A;**

Run exactly one preregistered Stage 0 experiment on **Closed-Loop Bracket Steering**.

Do **not** run C8 in parallel. C8 requires nontrivial verified multi-route data construction and is much more vulnerable to an “ordinary gradient conflict” dismissal. It has a slower path to a decisive NO-GO and weaker causal identifiability. It should remain documented as a HOLD, not silently converted into a side project.

The decision is based on four properties:

1. **The novelty boundary is explicit.** The seed dies unless it demonstrates active second-order accessibility outside matched first-order spans and beats strong nonlinear controls.
2. **The intervention is causal and reversible.** Loop reversal, scale laws, and analytic controls make post-hoc storytelling difficult.
3. **The compute is modest.** A decisive result fits within 60 GPU-hours and the first 72 hours.
4. **Failure is informative.** A NO-GO would close the remaining gap between recent Lie-bracket diagnostics and active activation control, preventing a longer project based on a merely mathematical curiosity.

The binding stop rule is:

> If the locked Qwen confirmation does not satisfy every Stage 0 gate, issue `NO_GO_BRACKET_STEERING` and return to the human mechanism discussion. Do not rescue the seed with more concepts, models, layers, prompts, scales, or weaker baselines.

## 9. First 72-hour execution plan

### 9.1 Repository structure

Create a clean branch or a new top-level research directory without modifying the frozen historical experiments:

```text
research/bracket_steering/
├── README.md
├── pyproject.toml
├── uv.lock                         # or a fully pinned requirements lock
├── configs/
│   ├── models/
│   │   ├── gemma2_2b.yaml
│   │   └── qwen25_3b.yaml
│   ├── data/
│   │   ├── axbench_stage0.yaml
│   │   └── behavioral_confirm.yaml
│   ├── fields/
│   │   ├── probe_gradient.yaml
│   │   └── model_native.yaml
│   └── stage0.yaml
├── data/
│   ├── manifests/
│   ├── raw/                        # gitignored
│   └── processed/                  # gitignored
├── src/bracket_steering/
│   ├── __init__.py
│   ├── model_hooks.py
│   ├── activation_cache.py
│   ├── concept_data.py
│   ├── fields.py
│   ├── jvp.py
│   ├── brackets.py
│   ├── integrators.py
│   ├── interventions.py
│   ├── baselines.py
│   ├── generation.py
│   ├── metrics.py
│   ├── statistics.py
│   └── manifests.py
├── scripts/
│   ├── 00_download.py
│   ├── 01_extract_activations.py
│   ├── 02_train_fields.py
│   ├── 03_unit_numerics.py
│   ├── 04_smoke_pair.py
│   ├── 05_discovery_gemma.py
│   ├── 06_freeze_confirmation.py
│   ├── 07_confirm_qwen.py
│   ├── 08_run_baselines.py
│   └── 09_analyze_stage0.py
├── tests/
│   ├── test_analytic_bracket.py
│   ├── test_constant_field_zero.py
│   ├── test_loop_reversal.py
│   ├── test_jvp_finite_difference.py
│   ├── test_integrator_convergence.py
│   ├── test_norm_matching.py
│   ├── test_split_integrity.py
│   └── test_manifest_replay.py
├── preregistration/
│   ├── STAGE0_PROTOCOL.md
│   ├── THRESHOLDS.yaml
│   └── FROZEN_CONFIRMATION.json
├── results/
│   ├── smoke/
│   ├── discovery/
│   ├── confirmation/
│   └── baselines/
└── reports/
    ├── STAGE0_DECISION.md
    └── STAGE0_DECISION.json
```

Historical repository documents and experiment outputs remain read-only.

### 9.2 Environment

Pin:

- Python 3.11;
- PyTorch and CUDA versions validated on RTX 4090;
- `transformers`, `accelerate`, `datasets`, `safetensors`;
- `torch.func` for JVP/VJP/HVP operations;
- one intervention library only if needed, preferably `pyvene` or a minimal native hook layer;
- `scikit-learn`, `scipy`, `pandas`, `pyarrow`, `statsmodels`;
- `pytest`, `hypothesis`, `ruff`, and `mypy`;
- deterministic kernels where feasible.

Record:

- exact model and tokenizer revisions;
- Hugging Face dataset revisions;
- CUDA driver and GPU model;
- dtype, attention implementation, and deterministic settings;
- SHA-256 hashes of every processed split;
- all random seeds;
- every confirmation parameter in `FROZEN_CONFIRMATION.json`.

No proprietary API or LLM judge is permitted in Stage 0.

### 9.3 Phase-by-phase schedule

#### Hours 0–4: protocol freeze and repository skeleton

1. Create `research/bracket_steering/`.
2. Write `STAGE0_PROTOCOL.md` before implementation.
3. Encode every GO/NO-GO threshold in `THRESHOLDS.yaml`.
4. Select the two model revisions and download manifests.
5. Define field-train, discovery-dev, and locked-confirmation split rules.
6. Define the multiplicity correction and bootstrap procedure.
7. Add a machine-readable terminal state:
   - `NOT_STARTED`
   - `NUMERICS_FAILED`
   - `DISCOVERY_FAILED`
   - `CONFIRMATION_FAILED`
   - `BASELINE_FAILED`
   - `STAGE0_GO`

**Output:** protocol commit. No experiment may change the thresholds after this commit.

#### Hours 4–10: data and model smoke test

1. Acquire AxBench and the chosen behavioral confirmation benchmark.
2. Verify licenses, task IDs, labels, and deterministic preprocessing.
3. Load Gemma and Qwen independently on two GPUs.
4. Identify three candidate residual-stream layers from architecture-relative positions—e.g., 40%, 60%, and 75% depth—without behavior-based tuning.
5. Cache activations for a small field-train subset.
6. Measure peak VRAM and tokens/second.
7. Test deterministic generation and replay.

**Automatic stop:** if either primary model cannot perform activation-gradient/JVP evaluation below 23 GB VRAM after batch-size-one and checkpointing, switch once to a smaller public model in the same family. A second resource failure ends Stage 0 as `NUMERICS_FAILED`; do not jump to quantized approximate gradients without a new protocol.

#### Hours 10–18: field implementations and analytic unit tests

1. Implement probe-gradient fields.
2. Implement model-native output-gradient fields.
3. Implement normalized and unnormalized variants.
4. Implement JVP bracket computation.
5. Build an analytic two-dimensional vector-field fixture with a known nonzero bracket.
6. Build a constant-field fixture with exactly zero bracket.
7. Verify:
   - JVP versus finite differences;
   - forward versus reverse sign;
   - second-order scaling;
   - RK2/RK4 convergence;
   - norm matching;
   - split integrity.

**Automatic stop at hour 18:** all numerical tests must pass with relative error below 5% on the analytic fixture and below 10% on a tiny transformer smoke fixture. Failure ends the seed. No model-scale run is allowed with unvalidated bracket numerics.

#### Hours 18–26: one-pair transformer smoke test

1. Train two source fields and one independent target scorer on Gemma.
2. Run one layer, one ordered pair, and three scales on 50–100 prompts.
3. Execute all negative controls:
   - reverse loop;
   - constant fields;
   - random zero-sum fields;
   - label-shuffled fields;
   - static source-span oracle;
   - no intervention.
4. Compare RK2 and RK4.
5. Plot:
   - observed versus predicted effect;
   - log effect versus log \(\epsilon\);
   - source drift;
   - out-of-span ratio;
   - norm-matched controls.

**Automatic stop at hour 26:** stop as `NUMERICS_FAILED` if the reverse loop does not reverse the analytic target direction, the fitted exponent lies outside \([1.5,2.5]\), RK2/RK4 disagree by more than 15%, or the constant-field control is non-null.

This smoke gate is intentionally looser than the final gate; it tests implementation, not novelty.

#### Hours 26–38: Gemma discovery run

1. Train 8–12 source fields on the locked field-train split.
2. Evaluate the ordered source-pair matrix on discovery-dev at three layers and three scales.
3. Compute:
   - bracket norm;
   - \(\rho\);
   - target-gradient alignment;
   - observed target effect;
   - source drift;
   - utility.
4. Correct all exploratory \(p\)-values with Benjamini–Hochberg.
5. Select exactly three triples using the preregistered rule:
   - high predicted bracket-target alignment;
   - \(\rho\ge0.35\);
   - low source drift;
   - no failed negative control;
   - concept diversity across triples.
6. Freeze:
   - triples;
   - layers;
   - scale range;
   - field checkpoints;
   - prompts;
   - metric code;
   - confirmation seeds.

Write `FROZEN_CONFIRMATION.json` and commit it.

**Automatic stop at hour 38:** if fewer than three discovery triples pass the *discovery* gates, issue `DISCOVERY_FAILED`. Do not widen the concept set, add models, or relax \(\rho\).

#### Hours 38–50: locked Qwen confirmation

1. Rebuild corresponding fields on Qwen using the same data protocol.
2. Run only the three frozen triples.
3. Use the frozen layers by relative depth and frozen scales after norm normalization.
4. Run all negative controls and static span baselines.
5. Compute confirmation confidence intervals and prediction metrics.
6. Do not inspect intermediate results to modify the run.

**Automatic stop at hour 50:** if any of the three triples fails the replication, reversal, scaling, prediction, or geometry gate, write `CONFIRMATION_FAILED` and stop. Do not proceed to broad baselines or a third model.

#### Hours 50–60: strong equal-budget baselines

Only if confirmation passes:

1. Train direct target mean-difference and linear fields.
2. Train direct target SVF.
3. Run ODESteer or the simplest faithful multi-step nonlinear baseline.
4. If stable and available within the environment, add INNSteer or FLAS.
5. Run the optimized static source-span oracle.
6. Match:
   - labels;
   - substeps;
   - field evaluations;
   - final norm;
   - path-integrated norm;
   - prompt and decoding budget.
7. Construct target-effect/source-drift Pareto curves.

**Automatic stop at hour 60:** if the bracket method does not meet the 10% Pareto-area or zero-target-training accessibility condition, write `BASELINE_FAILED`. A clean geometric effect may be archived, but the paper seed is dead.

#### Hours 60–67: independent analysis

Only if all earlier gates pass:

1. Re-run statistics from raw result files, not notebook state.
2. Bootstrap by prompt and by concept triple.
3. Verify multiplicity correction.
4. Produce:
   - scaling plots;
   - reversal plots;
   - predicted-versus-observed plots;
   - span decomposition;
   - Pareto fronts;
   - per-model and pooled tables;
   - negative-control summary.
5. Check for scorer dependence using an independent evaluator.
6. Audit data leakage and confirmation manifest integrity.

#### Hours 67–72: binding decision

Write:

- `reports/STAGE0_DECISION.md`
- `reports/STAGE0_DECISION.json`

The report must state exactly one terminal decision:

- `STAGE0_GO`, or
- `NO_GO_BRACKET_STEERING`.

A `STAGE0_GO` authorizes only a one-to-two-week confirmation package. It does not authorize paper writing, broad model sweeps, or oral-level claims.

### 9.4 Exact automatic stopping point

The default stopping point is **hour 50**, immediately after locked second-family confirmation. Most likely failures should terminate there or earlier.

The absolute stopping point is **60 GPU-hours or hour 60**, whichever occurs first. If the direct nonlinear baseline gate has not passed by that point, the seed is `NO_GO_BRACKET_STEERING`.

No additional model, concept, layer, prompt family, scale, or benchmark may be added after a failed gate. That is the binding anti-rescue rule.
