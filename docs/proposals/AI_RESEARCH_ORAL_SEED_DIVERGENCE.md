# AI Research Oral Seed Divergence

**Repository:** `ScottBlizzard/idle_2`  
**Audit date and literature cutoff:** 29 August 2026  
**Requested output:** `AI_RESEARCH_ORAL_SEED_DIVERGENCE.md`  
**Binding terminal decision:** **`NO_GO_NEED_NEW_SEED`**

This document executes the divergence protocol in [`docs/pro/PRO_NEXT_ORAL_SEED_DIVERGENCE.md`](https://github.com/ScottBlizzard/idle_2/blob/main/docs/pro/PRO_NEXT_ORAL_SEED_DIVERGENCE.md) after reading the Pro packet, the research brief, the current repository status, the completed MoE Stage D report, and—only as a repetition blacklist—the previous 17-candidate divergence attempt. It treats every repository-level NO-GO as binding and does not revive any failed planning, reset, uncertainty, operator-interference, bracket-steering, generic error-shaping, or frozen-MoE seed through a carrier or terminology swap.

---

## 1. Executive verdict and confidence

### 1.1 Verdict

**No candidate found in this fresh search clears the full ICLR Oral seed bar. The binding decision is `NO_GO_NEED_NEW_SEED`. No GPU experiment is authorized.**

The search generated **15 mechanistically distinct candidates across 12 materially different subfields**. Every candidate was queried through five collision lenses: phenomenon, mathematical structure, intervention, negative or inversion result, and closest obvious baseline. Eleven candidates were killed by direct or mechanism-level primary-literature collisions; one was left on HOLD because its exact controlled experiment appears unreported but its contribution would be too predictable and narrow; three advanced to an adversarial red team and all three failed before compute.

The three near-misses were:

1. **Learned-model/numerical-solver cross-cancellation in diffusion.** The exact controlled statement—lower score error producing worse samples under a fixed coarse solver because learned-model error had been cancelling truncation error—was not found verbatim. However, model-specific solver optimization, empirical model-statistic solvers, first-order samplers with deliberately opposite-sign leading error, few-step joint model/schedule tuning, loss-adaptive schedules, and beneficial early endpoint decoding already occupy the mechanism and the obvious algorithmic consequence. A positive experiment would most likely be reviewed as a clean numerical-analysis illustration of an existing solver–model co-design principle, not a new Oral-level law.
2. **A temporary spurious feature as a training scaffold.** The exact claim that a deliberately introduced shortcut can improve final invariant OOD performance after being withdrawn was not found in the same controlled form. But shortcut learning dynamics, curriculum effects, training-only privileged information, hints, early-stopped auxiliary alignment, and results showing that removal of spurious features can itself hurt already make the direction highly confounded. The most plausible positive result would reduce to extra early signal or curriculum shaping; the resulting algorithm would be an ordinary schedule.
3. **A lossless token-refinement trap repaired by a logical-position quotient.** A deterministic invertible split of every logical symbol into microtokens, followed by a position-only rescue in which all microtokens inherit the same logical clock, remains a reasonably crisp controlled experiment. Yet tokenization sensitivity of reasoning, noncanonical-tokenization failures, tokenization-invariance training, byte/subword tradeoffs, positional length-generalization failures, and theory showing that even lossless tokenizations can change computational depth or conditioning make the result anticipated. The remaining delta is a neat causal demonstration, not yet a broad new principle.

### 1.2 Confidence

| Judgment | Confidence | Basis |
|---|---:|---|
| The repository negative space was reconstructed correctly | 0.96 | The current Pro packet and status files are explicit, and the latest MoE result is a completed scientific NO-GO rather than an unfinished run. |
| None of the 15 candidates currently clears all Oral-seed gates | 0.88 | All direct neighbors and obvious baselines materially compress the remaining deltas; the three strongest candidates each fail an independent significance review. |
| No unindexed paper anywhere states the top residual claims verbatim | 0.66 | Search coverage is broad and current through the cutoff, but no literature search can prove universal absence. The decision does not rely on such a proof: even granting exact-wording novelty, significance and algorithmic-consequence gates still fail. |
| Running one of the proposed cheap experiments now would be a good use of the project’s next GPU-hours | 0.12 | A positive result would not yet resolve the principal novelty and significance objections. |

### 1.3 Why a rigorous NO-GO is preferable here

The failed candidates are not merely “low confidence.” Their common defect is structural: **the first figure can be made surprising, but the third figure collapses into a mature baseline**—tune a solver to its model, schedule privileged guidance, choose a better tokenizer or positional encoding, use an invariant distillation loss, measure functional rather than parameter overlap, or preserve attention sinks. None currently supplies a new law plus a non-obvious consequence.

The missing ingredient is described precisely in Section 6. It is not another carrier. It is a new causal object that remains after matching function, information, compute, coordinates, optimizer state, and numerical method—and whose intervention implies something stronger than prediction, reweighting, regularization, routing, scheduling, or tuning.

---

## 2. Binding negative-space map

### 2.1 Scientific NO-GOs

| Closed family | Binding scientific conclusion | Exclusion imposed on this search |
|---|---|---|
| Controller-insensitive, viability-, reachability-, option-, continuation-, or failure-state-preserving planning | Broad versions reduce to robust planning, stochastic viability, reachability, empowerment, chance constraints, and long-horizon value; the repository’s compact-CoT carrier was also solved too well. | No new simulator, value head, continuation score, or renamed feasible set can count as a new mechanism. |
| Resettable failure with retained learning | Agent rewind, iterative repair, verifier-guided learning, safe resets, replay, and memory occupy the broad claim that external state can reset while internal learning accumulates. | No “failure is informative,” retry-cost matching, memory module, or benchmark transfer. |
| Decision-calibrated uncertainty for learned planners | A direct July 2026 collision already showed that calibrated world-model uncertainty can be weakly aligned with boundary risk, can worsen safety when used as a penalty, and can lose to outcome-supervised failure prediction. Surrounding risk-aware and conformal methods are mature. | No uncertainty head, calibration loss, risk predictor, conformal wrapper, or new safety environment. |
| Algorithmic prompting / conditionally irrelevant competing-operator interference | A local Gemma-2-9B effect was real and causally manipulable under Pack A, but failed the binding wording replication: Pack B retained only about 30% of the effect and all other families failed the capability gate. | No extra prompt packs, models, parsers, post-hoc subgroups, or a domain rename. |
| Generic error shaping into task-tolerant directions | Invariance, equivariance, covariance shaping, tangent geometry, robust control, and task-aware distortion already capture the general principle. | No fashionable application of the same projection or geometry without a distinct theorem, intervention, and winning baseline. |
| Closed-loop bracket activation steering | At a fixed layer and token position, the suffix observes only the final hidden-state displacement. Exact displacement replay is the correct matched baseline; direct injection of the computed bracket is simpler; leaving the instantaneous span is classical Lie closure. | No order-sensitivity, noncommutativity, quadratic-scaling, or nonlinear-steering demonstration by itself. |
| Counterfactual route non-compositionality in frozen MoEs | The registered Stage D study completed successfully and returned `NO_GO_NO_INTERACTION_LAW`: 0/4 regimes passed H1–H4 on both GSM8K and MATH-500; all 32 primary tests had BH-adjusted `q=1`; H4 correlations were approximately zero. | No rescue using selected positive H3 cells, new layer bins, relaxed multiplicity, extra models, or post-hoc compatibility features. |

The brief also marks as heavily occupied: retrieval redundancy/diversity, reasoning-sample genealogy, raw-versus-compressed agent memory, masked-diffusion commitment order, output-path diversity/SFT conflict, recoverability-weighted failed traces, ordinary model-editing interference, and generic multi-agent critique. These were treated as collision warnings rather than inspiration anchors.

### 2.2 Scientific failure versus engineering failure

The distinction matters because an engineering problem can justify rerunning the same scientific test, while a scientific NO-GO cannot.

**Scientific failures that bind:**

- The operator-interference effect did not transfer across wording and admissible model families.
- The uncertainty pivot was stopped before experiment because the central failure mode and stronger baseline were already published.
- The bracket mechanism collapsed under an exact final-displacement causal baseline independently of compute.
- The MoE route experiment completed its frozen acquisition and analysis and found no reproducible interaction law or predictor.

**Engineering incidents that do not constitute scientific evidence:**

- MoE preflight issues involving an attention-mask warning, slash-containing dataset IDs used as paths, a network timeout, byte-level BPE prefix offsets, CPU oversubscription, and NumPy JSON serialization were repaired or preserved as invalid attempts.
- No route-effect values were used to adapt the protocol during those repairs.
- The successful MoE run consumed about **3.13 hours**, below the six-hour gate; therefore the scientific failure cannot be attributed to missing compute.
- The bracket protocol’s original condition count and double-backward cost were under-estimated, but fixing that budget would not repair the final-displacement causal collapse.

### 2.3 Search-time exclusion rules derived from the NO-GOs

A candidate was rejected immediately if its central intervention could be rewritten as any of the following:

- choose an action whose future feasible set is larger;
- retain learning after a reset or failure;
- add a calibrated risk or uncertainty estimator;
- show that an irrelevant instruction/operator perturbs reasoning;
- project error into a tolerant or invariant direction;
- compose activation interventions whose final displacement is the only downstream state;
- infer a global MoE route from locally good route changes;
- improve performance by generic diversity, ensembling, retrieval allocation, memory compression, critique, or an auxiliary predictor.

None of the 15 candidates below depends on billiards, MoE routing, bracket steering, planning, learned-planner uncertainty, or competing-operator prompting. The previous 17-candidate document was consulted only to avoid regenerating its reasoning-family saturation, RAG saturation, branch-insurance, dormant-plasticity, compensation-circuit, set-valued grounding, output-equivalence valley, direction-only feedback, edit-multiplicity, recoverability, raw-evidence memory, masked-diffusion order, undercomplete proposer, bracket, orbit-closure, and mode-count candidates.

---

## 3. Candidate ledger

### C01 — Trainer-state hysteresis under source removal

**Subfield:** optimization and training dynamics.

**Counterintuitive claim.** Two models with identical parameters, activations, outputs, RNG state, and future data at a cut can acquire predictably different later behavior solely because one optimizer state remembers an earlier shortcut or source signal.

**Minimal mathematical or causal object.** Treat training as a stateful dynamical system

\[
z_t=(\theta_t,m_t,v_t,a_t),\qquad z_{t+1}=F(z_t,B_t),
\]

where `m`, `v`, and `a` include optimizer moments and other auxiliary state. The causal operation is a moment-only transplant

\[
\operatorname{do}(\theta=\theta^*,m=m^{(A)},v=v^{(A)})
\quad\text{versus}\quad
\operatorname{do}(\theta=\theta^*,m=m^{(B)},v=v^{(B)}).
\]

**Strongest obvious explanation or baseline.** The earlier source was already encoded in weights; residual data-order randomness explains divergence; reset merely changes effective learning rate.

**Decisive distinguishing observation.** At the cut, every function-space diagnostic is equal. A moment-only swap changes the sign or magnitude of later behavior under byte-identical future batches, while resetting or counter-transplanting moments removes the effect. A full-state recurrence predicts the future difference.

**Cheapest kill.** A small CNN on a controlled shortcut dataset and a tiny Transformer on a state-tracking task, with paired seeds and moment carry/reset/transplant. Kill if moment-only transplantation does not reproducibly move later OOD behavior after matched future updates.

**Broad audience if true.** Optimization, fine-tuning, continual learning, alignment, reproducibility, and checkpoint portability.

### C02 — Function-preserving neuron cloning makes component-level causal stories arbitrary

**Subfield:** mechanistic interpretability and symmetry.

**Counterintuitive claim.** A network can compute exactly the same function while the number and identity of “causally necessary neurons” changes by an arbitrary factor under a standard top-component ablation protocol.

**Minimal mathematical or causal object.** For a hidden unit with incoming vector `u` and outgoing weight `w`, replace it by `k` copies with the same incoming vector and outgoing weights `w/k`:

\[
w\,\sigma(u^\top x)=\sum_{j=1}^{k}\frac{w}{k}\sigma(u^\top x).
\]

This is a function-preserving refinement. Compare a coordinate-level attribution `A(θ)` with a quotient/subspace attribution `\bar A([θ])` defined on the function-preserving equivalence class.

**Strongest obvious explanation or baseline.** The attribution method is simply not invariant; use subspaces, groups, or a different circuit definition.

**Decisive distinguishing observation.** Exact cloning leaves logits and every input-output causal effect unchanged, but the apparent minimal top-`k` circuit grows with the cloning factor, while a grouped subspace intervention remains invariant.

**Cheapest kill.** Apply exact cloning to a one-hidden-layer MLP and one MLP block in GPT-2-small, verify machine-precision function equality, and rerun component-level necessity/sufficiency. Kill if the selected circuit is stable after matching intervention magnitude and grouping.

**Broad audience if true.** Interpretability, auditing, scientific reproducibility, model comparison, and causal explanation standards.

### C03 — Sparse-autoencoder reconstruction–causality inversion

**Subfield:** representation learning and sparse autoencoders.

**Counterintuitive claim.** Increasing SAE dictionary size can monotonically improve reconstruction while monotonically worsening the fidelity of interventions made in the learned feature coordinates.

**Minimal mathematical or causal object.** For dictionary size `K`, separate reconstruction

\[
R_K=\mathbb E\|h-D_KE_Kh\|_2^2
\]

from causal fidelity

\[
C_K=1-\frac{|\Delta \ell_{\text{SAE}}-\Delta \ell_{\text{ground truth}}|}{|\Delta \ell_{\text{ground truth}}|+\epsilon}.
\]

Feature splitting permits `R_K` to decrease while `C_K` decreases.

**Strongest obvious explanation or baseline.** Sparsity was mismatched; the intervention scale was wrong; larger dictionaries merely require grouping near-collinear latents.

**Decisive distinguishing observation.** Under matched active-latent count, intervention energy, and grouped-latent baselines, reconstruction ranking reverses causal ranking on synthetic features with known ground truth and on a real language-model behavior.

**Cheapest kill.** Train a dictionary-size sweep on a toy superposition model and one cached GPT-2 activation set; preregister monotonic rank reversal. Kill if grouping or subspace-aware decoding restores causal fidelity in the same order as reconstruction.

**Broad audience if true.** Interpretability, representation learning, model auditing, and feature-based steering.

### C04 — Invertibly overcomplete scratchpads can hurt length generalization

**Subfield:** reasoning supervision and sequence learning.

**Counterintuitive claim.** A fully correct scratchpad containing every intermediate state can generalize to shorter horizons than an invertibly equivalent delta-only trace that contains no less task information.

**Minimal mathematical or causal object.** Given `s_0`, the state trace `E_full=(s_1,…,s_T)` and transition trace `E_delta=(a_1,…,a_T)` with `a_t=s_t-s_{t-1}` are bijective. The candidate concerns the factorization of supervision, not information content:

\[
I(Y;E_{\rm full}\mid X)=I(Y;E_{\rm delta}\mid X),
\quad
G_{\rm OOD}(E_{\rm full})<G_{\rm OOD}(E_{\rm delta}).
\]

**Strongest obvious explanation or baseline.** Full traces are longer, create more token losses, alter position statistics, or make the next-token task locally easier; the effect is standard sequence-format inductive bias.

**Decisive distinguishing observation.** The gap survives identical sequence length, target count, FLOPs, optimizer updates, and an invertible online converter, and is predicted by a measurable state-tracking bottleneck rather than token difficulty.

**Cheapest kill.** Parity, modular addition, and one stack-like task with full versus delta encodings; small Transformer and recurrent baseline. Kill if compute/token matching or a simple positional baseline removes the effect.

**Broad audience if true.** Reasoning, chain-of-thought training, curriculum design, algorithmic generalization, and process supervision.

### C05 — Stronger multimodal alignment can erase useful synergy

**Subfield:** multimodal representation learning and information theory.

**Counterintuitive claim.** A representation can improve image–text retrieval as cross-modal alignment increases while becoming strictly worse on tasks whose answer exists only in the interaction between modalities.

**Minimal mathematical or causal object.** Use a partial-information decomposition of task information:

\[
I(Y;X_1,X_2)=I_{\rm red}+I_{\rm uniq,1}+I_{\rm uniq,2}+I_{\rm syn}.
\]

An alignment coefficient `λ` can increase redundant/shared information and suppress `I_syn`.

**Strongest obvious explanation or baseline.** Modality collapse, insufficient fusion capacity, or a retrieval/task tradeoff caused by an imbalanced objective.

**Decisive distinguishing observation.** Along a matched alignment-strength path, retrieval and cross-modal CKA increase, a controlled synergy task decreases, estimated synergistic information mediates the decline, and partial alignment restores the task without sacrificing the shared component.

**Cheapest kill.** A synthetic XOR-style multimodal task plus one public multimodal benchmark, with a small dual encoder/fusion model. Kill if a stronger fusion head or capacity-matched control removes the inversion.

**Broad audience if true.** Multimodal learning, contrastive learning, foundation-model alignment, federated multimodal systems, and representation evaluation.

### C06 — Parameter-orthogonal adapters can be functionally maximally interfering

**Subfield:** parameter-efficient fine-tuning and model composition.

**Counterintuitive claim.** Two adapters with exactly orthogonal parameter updates can interfere more than a nonorthogonal pair because composition is governed by input-conditioned functional geometry, not Euclidean weight geometry.

**Minimal mathematical or causal object.** Construct

\[
\langle \Delta\theta_1,\Delta\theta_2\rangle=0,
\]

but measure functional overlap

\[
\Gamma_x=\langle J_x\Delta\theta_1,J_x\Delta\theta_2\rangle
\]

and second-order nonadditivity

\[
\mathcal I_x=f_{\theta+\Delta_1+\Delta_2}(x)-f_{\theta+\Delta_1}(x)-f_{\theta+\Delta_2}(x)+f_\theta(x).
\]

**Strongest obvious explanation or baseline.** Adapter norms, scale, task similarity, or merge coefficient explains the result; orthogonalization damages the individual adapters.

**Decisive distinguishing observation.** Single-task behavior and update norms are preserved, parameter overlap is forced to zero, yet composition damage follows `Γ_x` or `\mathcal I_x` across held-out input distributions and formats.

**Cheapest kill.** Qwen2.5-0.5B or 1.5B LoRA pairs, orthogonalized against matched random controls, evaluated on two task pairs. Kill if functional overlap adds no predictive value beyond task identity, norms, and single-task performance.

**Broad audience if true.** Model merging, PEFT, continual learning, personalization, safety adapters, and modular foundation models.

### C07 — Better learned scores can sample worse under a fixed coarse solver

**Subfield:** generative modeling and numerical analysis.

**Counterintuitive claim.** Reducing learned score/velocity error can worsen finite-step sample quality because the original model error was cancelling the numerical solver’s truncation error.

**Minimal mathematical or causal object.** Let `Φ` be the exact probability-flow map and `Ψ_h(s_θ)` the numerical map. A local endpoint error can be decomposed as

\[
\delta_{\rm total}=\delta_{\rm model}+\delta_{\rm disc}+O(h^{p+1}),
\]

so

\[
\|\delta_{\rm total}\|^2=
\|\delta_{\rm model}\|^2+
\|\delta_{\rm disc}\|^2+
2\langle\delta_{\rm model},\delta_{\rm disc}\rangle.
\]

A negative cross-term permits a less accurate model to yield a more accurate coarse trajectory.

**Strongest obvious explanation or baseline.** Global score MSE weights the wrong times or directions; sample metrics are noisy; the supposedly better model simply changed stiffness or calibration; a model-specific solver fixes the issue.

**Decisive distinguishing observation.** In a controlled family `s_α=s_*+αe`, smaller `\|s_α-s_*\|` gives worse terminal error only at coarse NFE; the measured cross-term predicts the rank reversal; the ranking returns to the score-error order under a fine solver or exact integration.

**Cheapest kill.** Analytic Gaussian mixtures with exact scores plus one open CIFAR-10 checkpoint, two solvers, and a fixed low-NFE grid. Kill if the inversion disappears under local/time-weighted score error or if the cross-term cannot predict it prospectively.

**Broad audience if true.** Diffusion/flow models, neural ODEs, learned simulators, scientific ML, sampler benchmarking, and distillation.

### C08 — A temporary shortcut can scaffold invariant learning

**Subfield:** robustness, shortcut learning, and curricula.

**Counterintuitive claim.** Introducing a deliberately spurious but easy feature only during an early training phase, then removing or reversing it, can improve final invariant OOD accuracy over clean-only training at equal total compute.

**Minimal mathematical or causal object.** Let `x=(x_c,x_s)`, where `x_c` is causal and `x_s` is spurious. Train under

\[
P_A:\operatorname{corr}(x_s,y)=\rho>0,
\qquad
P_B:\operatorname{corr}(x_s,y)=0\ \text{or}\ <0.
\]

Compare the endpoint of `P_A→P_B` with `P_B→P_B` under matched updates, examples, and aggregate label information.

**Strongest obvious explanation or baseline.** The scaffold simply supplies extra early signal, creates a conventional easy-to-hard curriculum, improves conditioning, or changes effective initialization.

**Decisive distinguishing observation.** The benefit survives controls matched for mutual information, early loss reduction, gradient norm, and margin. Feature-subspace intervention shows that the temporary shortcut causes earlier class separation but is absent from the final predictor; a narrow withdrawal window is prospectively predicted by the dynamics.

**Cheapest kill.** A controlled Boolean/Colored-MNIST construction plus a small ResNet. Kill if core-feature duplication, label smoothing, easy examples, or any information-matched curriculum reproduces the gain.

**Broad audience if true.** Robust learning, curricula, representation dynamics, privileged information, distillation, and pretraining-to-finetuning transfer.

### C09 — Exact feature matching is weaker than quotient-level distillation

**Subfield:** knowledge distillation and representation geometry.

**Counterintuitive claim.** A student forced to match every teacher feature coordinate can acquire less capability than a student matching only representation invariants, even though exact matching appears to provide strictly more supervision.

**Minimal mathematical or causal object.** A teacher gauge transform

\[
h_T'=Qh_T,\qquad W_T'=W_TQ^{-1}
\]

leaves the output function unchanged. Coordinate loss `\|h_S-h_T\|^2` is gauge-dependent; Gram, CKA, subspace, or logit losses are quotient-defined.

**Strongest obvious explanation or baseline.** The student and teacher have different widths; a learned alignment layer or normalized feature loss is sufficient; logits are simply the correct target.

**Decisive distinguishing observation.** Random function-preserving gauges change the outcome of raw feature KD while invariant objectives remain stable. Exact geometry recovery can be dissociated from capability recovery.

**Cheapest kill.** CIFAR-100 or a small language-model distillation with synthetic orthogonal gauges and matched alignment layers. Kill if Procrustes alignment makes coordinate KD invariant and equally capable.

**Broad audience if true.** Distillation, representation transfer, model grafting, multimodal alignment, and interpretability.

### C10 — Duplicate topology changes the solution even when mean gradients match

**Subfield:** data curation and implicit optimization bias.

**Counterintuitive claim.** Two training streams with the same examples, exposure counts, empirical loss, and expected gradient can converge to different generalization because duplicate grouping changes only the covariance geometry of minibatch noise.

**Minimal mathematical or causal object.** Match

\[
\mathbb E[g_B(\theta)]=\mu(\theta)
\]

while changing

\[
\operatorname{Cov}[g_B(\theta)]=\Sigma_1(\theta)\neq\Sigma_2(\theta).
\]

The candidate asks whether a controlled duplicate topology selects a different interpolating solution through `Σ`, not through mean training signal.

**Strongest obvious explanation or baseline.** Data order, effective batch size, exposure frequency, or memorization of duplicates explains the result.

**Decisive distinguishing observation.** A paired batching construction matches every first-order quantity and exposure but changes covariance eigenspaces; generalization follows the predicted covariance geometry and is reproduced by injecting matched synthetic gradient noise.

**Cheapest kill.** An overparameterized matrix/MLP problem with analytic minima plus a small image classifier. Kill if shuffled order or an effective-batch-size control explains the endpoint.

**Broad audience if true.** Data deduplication, pretraining mixtures, SGD theory, curriculum, and reproducibility.

### C11 — Lossless token refinement creates a false positional clock

**Subfield:** tokenization and length generalization.

**Counterintuitive claim.** Deterministically splitting each logical symbol into an invertible pair of microtokens can improve in-distribution next-token loss yet destroy algorithmic length generalization; assigning both microtokens the same logical position can restore it without changing tokens, sequence length, targets, or FLOPs.

**Minimal mathematical or causal object.** Let `φ:Σ→Γ^r` be an injective fixed-length code. Physical positions advance as `rt,…,rt+r-1`; quotient positions use the logical coordinate and a phase:

\[
p(\phi_j(x_t))=(t,j).
\]

The hypothesis is

\[
G_{\rm OOD}(\phi, p_{\rm physical})
< G_{\rm OOD}(\mathrm{id})
\approx G_{\rm OOD}(\phi,p_{\rm logical}).
\]

**Strongest obvious explanation or baseline.** The refined sequence is longer, RoPE extrapolates farther, token frequency changes, or the model sees fewer logical examples per unit compute.

**Decisive distinguishing observation.** Refined-physical and refined-logical runs use identical token IDs, length, attention mask, targets, batch order, optimizer, and FLOPs; only position IDs differ. The logical clock recovers most of the atomic-token generalization gap, while frequency rescaling, NoPE, shifted grouping, and extra phase-capacity controls do not.

**Cheapest kill.** Two generated state-tracking tasks, a four-layer RoPE Transformer, five paired seeds, and exact train/test length grids. A fully preregistered version appears in Section 8.

**Broad audience if true.** Tokenization, long-context modeling, code and mathematical reasoning, byte-level models, multimodal tokenizers, and positional encoding.

### C12 — Teacher co-error topology dominates teacher accuracy in distillation

**Subfield:** ensemble and multi-teacher knowledge distillation.

**Counterintuitive claim.** Two teacher ensembles with identical per-teacher accuracy, calibration, confidence histograms, and pairwise average disagreement can yield sharply different students because the higher-order topology of their joint errors differs.

**Minimal mathematical or causal object.** For teacher errors `e_i(x)`, match marginals and selected pairwise statistics while varying a joint error tensor or covariance spectrum:

\[
\mathbb E[e_i],\ \operatorname{Var}(e_i),\ \overline{\operatorname{Corr}}(e_i,e_j)
\ \text{matched},
\qquad
\mathcal T(e_1,\ldots,e_M)\ \text{different}.
\]

**Strongest obvious explanation or baseline.** Teacher diversity/disagreement, ensemble entropy, class-wise accuracy, or student capacity explains the result.

**Decisive distinguishing observation.** A constructed teacher family matches all common scalar quality/diversity metrics but changes student generalization in the direction predicted by a preregistered co-error spectral or hypergraph statistic.

**Cheapest kill.** Synthetic soft-label teachers over CIFAR-10 features or a controlled multiclass Gaussian problem. Kill if pairwise disagreement, per-class accuracy, or aggregate teacher logits absorb the effect.

**Broad audience if true.** Distillation, ensembles, synthetic supervision, pseudo-labeling, and multi-agent/model collaboration.

### C13 — One strategically wrong demonstration can improve in-context learning

**Subfield:** in-context learning and machine teaching.

**Counterintuitive claim.** Replacing one correct demonstration with a deliberately inconsistent one can improve task accuracy by eliminating the model’s dominant shortcut hypothesis.

**Minimal mathematical or causal object.** Let `H` be an implicit hypothesis set and `h_s` a shortcut consistent with all positive demonstrations. A negative demonstration `d^-` is useful when

\[
H' = \{h\in H:h(d^-)=\text{recognized failure}\}
\]

removes `h_s` while preserving the target hypothesis.

**Strongest obvious explanation or baseline.** The negative example simply provides an error explanation, contrastive label, broader coverage, or better retrieval.

**Decisive distinguishing observation.** The inconsistent example helps only when it separates the target from a preregistered shortcut; random wrong labels and equally diverse correct examples hurt or do not help; internal prediction changes follow version-space elimination rather than confusion.

**Cheapest kill.** Synthetic classification/rule induction with open 1–3B models and a positive/strategic-negative/random-negative matched set. Kill if the gain disappears without natural-language error labels or is reproduced by another correct example.

**Broad audience if true.** Prompting, machine teaching, data selection, contrastive learning, and reasoning.

### C14 — Functionally identical checkpoints are not fine-tuning-equivalent under Adam

**Subfield:** optimizer equivariance and model reparameterization.

**Counterintuitive claim.** Two exactly function-equivalent checkpoints can separate at the first Adam update and converge to different predictors solely because a gauge transformation changes coordinates seen by the optimizer.

**Minimal mathematical or causal object.** Under a gauge action such as

\[
(U,V)\mapsto(UQ,VQ^{-\top}),\qquad UV^\top\ \text{fixed},
\]

ask whether optimizer update `\mathcal O` is equivariant:

\[
\mathcal O(g\cdot\theta,g\cdot s)=g\cdot\mathcal O(\theta,s).
\]

Coordinate-wise Adam generally is not.

**Strongest obvious explanation or baseline.** Floating-point error, unmatched optimizer-state transport, or a different effective learning rate creates the divergence.

**Decisive distinguishing observation.** The first-step separation survives exact state transport and high precision, while an equivariant optimizer keeps trajectories matched and restores the same implicit bias.

**Cheapest kill.** A factored matrix problem and one small Transformer fine-tuning run from a gauge-equivalent pair. Kill if exact transport of moments makes Adam equivariant to numerical precision.

**Broad audience if true.** Optimization, checkpoint conversion, merging, reproducibility, low-rank adaptation, and theory.

### C15 — Quantization can improve reasoning by perturbing attention sinks

**Subfield:** efficient inference and long-context systems.

**Counterintuitive claim.** A carefully chosen low-bit KV-cache perturbation can outperform FP16 on long-context reasoning because it attenuates non-informative sink keys rather than merely approximating them.

**Minimal mathematical or causal object.** Let `Q_b(K,V)` be a quantizer and define sink mass

\[
A_{\rm sink}=\sum_{t\in S}\operatorname{softmax}(qK^\top)_t.
\]

The causal proposal is a bit-allocation intervention that decreases sink mass while preserving task-relevant value directions.

**Strongest obvious explanation or baseline.** The apparent gain is evaluator noise, regularization, altered sampling, or additional effective context enabled by memory savings; preserving sink tokens at high precision is the established baseline.

**Decisive distinguishing observation.** At identical context and decoding, selective sink quantization improves exact task accuracy; restoring only sink keys to FP16 removes the gain; matched random-token quantization does not; attention mediation links the change to non-informative sink mass.

**Cheapest kill.** One 7–8B open model, RULER-style retrieval plus a reasoning subset, deterministic decoding, and sink-selective versus random-selective quantization. Kill if gains vanish under repeated exact evaluation or preserving sinks remains uniformly better.

**Broad audience if true.** LLM inference, quantization, long-context reasoning, attention theory, and hardware-aware modeling.

---

## 4. Literature-search methodology and verified exact-neighbor table

### 4.1 Search protocol

**Cutoff.** Searches used literature available through **29 August 2026**. Recent 2025–2026 work was treated as essential rather than optional.

**Source hierarchy.** Primary sources were preferred: arXiv abstract/full-text pages, OpenReview, PMLR/official proceedings, and author/project repositories. Surveys were used only to expand terminology and were not used as the decisive collision when a primary paper was available.

**Five query families per candidate.** Each candidate was searched under:

1. **Phenomenon:** plain-language statement of the surprising effect.
2. **Mathematical structure:** symmetry, covariance, cross-term, quotient, PID, error tensor, or state-space wording.
3. **Intervention:** transplant, reset, clone, split, gauge transform, score interpolation, schedule withdrawal, position reassignment, or selective quantization.
4. **Negative/inversion:** “better metric worse behavior,” “lossless but worse,” “orthogonal but interfering,” “identical function different training,” and related formulations.
5. **Closest baseline:** the most likely reviewer reduction—optimizer reset, subspace attribution, grouped SAE features, scratchpad granularity, partial alignment, functional task-vector geometry, bespoke solvers, curriculum/LUPI, invariant KD, SGD-noise covariance, tokenization robustness, teacher diversity, negative demonstrations, equivariant optimizers, or sink-preserving quantization.

**Decision rule.**

- **KILL:** a primary paper already states the central inversion, implements essentially the same intervention, or establishes the same mechanism and obvious consequence. A new carrier or cleaner plot is insufficient.
- **HOLD:** the exact controlled statement was not located, but the remaining delta is predictable, narrow, or lacks an Oral-level consequence. HOLD is not experiment authorization.
- **SURVIVE_TO_RED_TEAM:** the exact claim–intervention–baseline triple was not found in the first collision pass and the cheapest discriminating test remained small enough to analyze adversarially.

### 4.2 Representative multi-formulation query ledger

The table records representative formulations rather than every syntactic variation.

| ID | Phenomenon query | Mathematical query | Intervention query | Negative/inversion query | Closest-baseline query |
|---|---|---|---|---|---|
| C01 | identical weights, different later behavior | extended trainer state / optimizer memory | Adam moment transplant with fixed parameters | source removed but trait persists | optimizer reset under nonstationarity |
| C02 | same function, different causal circuit size | gauge symmetry / neuron cloning identifiability | function-preserving neuron split and ablation | mechanistic explanation non-identifiable | subspace-level causal intervention |
| C03 | lower SAE reconstruction, worse intervention | feature splitting / overcomplete dictionary | dictionary-size sweep and causal replacement | geometric recovery but causal inertness | grouped or subspace-aware SAE |
| C04 | more complete scratchpad, worse extrapolation | bijective state versus delta trace | invertible trace recoding | process supervision hurts length generalization | token/FLOP/position-matched CoT granularity |
| C05 | stronger multimodal alignment, worse fusion | PID synergy versus redundancy | alignment-strength intervention | retrieval improves while synergy task falls | partial alignment / modality-specific branches |
| C06 | orthogonal adapters interfere | parameter versus functional geometry | orthogonalize LoRA updates, then compose | zero weight overlap but high nonadditivity | tangent-space or Jacobian overlap |
| C07 | better score, worse finite-step samples | model error plus discretization error cross-term | controlled score interpolation under fixed solver | approximation error cancels truncation error | model-specific / bespoke diffusion solver |
| C08 | temporary shortcut improves robust endpoint | two-phase feature-learning dynamics | add then withdraw/reverse spurious feature | removing shortcut hurts / scaffold helps | curriculum, privileged information, hints |
| C09 | exact feature KD learns less capability | representation quotient / gauge invariance | teacher basis rotation under fixed function | geometry recovery without function recovery | Gram/CKA/logit distillation |
| C10 | same mean gradient, different generalization | minibatch-noise covariance geometry | duplicate grouping with matched exposures | deduplication/repetition nonmonotonicity | effective batch size and data-order controls |
| C11 | lossless token split hurts reasoning | refinement quotient / logical positional clock | assign paired subtokens the same logical position | tokenization-invariant information, non-invariant model | byte models, randomized positions, homotokens |
| C12 | same teacher accuracy, different student | joint error covariance/tensor | synthesize matched-marginal teacher ensembles | teacher consensus amplifies blind spots | teacher diversity/disagreement metrics |
| C13 | wrong example improves ICL | version-space elimination / machine teaching | strategic negative versus random negative demo | learn from mistakes in context | contrastive/error-labeled demonstrations |
| C14 | same function, different Adam fine-tuning | optimizer gauge equivariance | exact coordinate and state transport | loss invariant but optimizer basis-sensitive | equivariant preconditioner |
| C15 | low-bit KV beats FP16 | sink-mass mediation / rate–distortion | selectively quantize sink tokens | approximation noise improves reasoning | preserve-first/sink-aware mixed precision |

### 4.3 Exact-neighbor results: C01–C05

| ID | Verified closest primary work | What is already established and what it predicts | Exact remaining delta | Substantive or cosmetic? | Verdict |
|---|---|---|---|---|---|
| C01 | *Stored in Optimizer State, Valued by Later Training* [L01]; *Training Memory in Deep Neural Networks* [L02]; *Resetting the Optimizer in Deep RL* [L03] | Moment-only transplantation can leave parameters, hidden states, and outputs unchanged at a cut yet cause growing differences under source-free future updates; trainer-state carry/reset is already a formal causal object. These works predict the proposed divergence. | Specialize the carried signal to a transient shortcut and an OOD endpoint. | Cosmetic/application-level: the carrier and intervention are already direct. | **KILL** |
| C02 | *Everything, Everywhere, All at Once* [L06]; *Signed-Permutation Coordinate Transport* [L05]; *The Loss Does Not See the Basis, but Adam Does* [L04] | Mechanistic explanations and aligned subspaces can be non-identifiable; coordinate-indexed tools require an explicit gauge; function-equivalent parameterizations can differ under coordinate-dependent procedures. A clone-based circuit instability is predicted. | A particularly simple theorem showing arbitrary multiplication of top-`k` “necessary neurons.” | The theorem is clean but restates the known non-identifiability/gauge problem; the baseline is already quotient/subspace analysis. | **KILL** |
| C03 | *Subspace-Aware Sparse Autoencoders* [L07]; *ReSAE* [L08]; *From Geometric Recovery to Causal Validation* [L09] | Feature splitting is theoretically favored; lower raw variance recovery can coexist with better downstream cross-entropy recovery; geometrically matched SAE atoms can be causally inert. These works already separate reconstruction from causal utility. | A monotonic reconstruction–causal rank inversion under a single dictionary-size sweep. | Mostly a sharper benchmark plot; mechanism and remedy are already occupied. | **KILL** |
| C04 | *What Algorithms Can Transformers Learn?* [L10]; *On the “Induction Bias” in Sequence Models* [L11]; *Transformers Provably Learn CoT Reasoning with Length Generalization* [L12] | Scratchpad/format choice, intermediate supervision, sequence length, attention concentration, and model family materially change extrapolation. They predict that bijectively equivalent traces can have different learnability. | Exact full-state versus delta-trace comparison with token/FLOP/position matching and a causal bottleneck measure. | The control is substantive, but the likely conclusion—choose the factorization with the right inductive bias—is expected and not yet a broad law. | **HOLD** |
| C05 | *What to Align in Multimodal Contrastive Learning?* [L13]; *SynGR* [L14]; *PID-Guided Partial Alignment* [L15] | Standard alignment preferentially captures shared/redundant information; unique and synergistic components can be suppressed; partial/PID-guided alignment is already an algorithmic remedy. These papers predict an alignment–synergy tradeoff. | A monotone retrieval-up/synergy-down curve under a controlled alignment coefficient. | Cosmetic sharpening; claim, mechanism, and baseline are occupied. | **KILL** |

### 4.4 Exact-neighbor results: C06–C10

| ID | Verified closest primary work | What is already established and what it predicts | Exact remaining delta | Substantive or cosmetic? | Verdict |
|---|---|---|---|---|---|
| C06 | *When Do Task Vectors Interfere?* [L16]; *PermDoRA* [L17]; *Task Arithmetic in the Tangent Space* [L18] | Parameter geometry can be a weak predictor; functional nonadditivity is input- and format-conditioned; tangent/function-space structure matters. Orthogonal adapters can therefore still interfere. | Construct a deliberately parameter-orthogonal pair whose interference is prospectively ranked by Jacobian overlap. | Cleaner causal construction, but the scientific claim and winning baseline are direct. | **KILL** |
| C07 | *DPM-Solver-v3* [L20]; *Bespoke Solvers* [L21]; *Optimizing Few-Step Sampler* [L22]; *Entropy-Based… Loss-Adaptive Schedules* [L23]; *Are First-Order Diffusion Samplers Really Slower?* [L19]; *x-Prediction Is All You Need* [L24] | Solver error depends on model statistics and evaluation placement; solvers can be tailored to a pretrained flow; model and selected timesteps can be jointly tuned; schedules adapt to learned-model loss; opposite-sign leading errors and beneficial early stopping/endpoint decoding already overturn monotone “higher order/more integration is better” intuitions. | A controlled paired inversion in which a lower score-error model is worse specifically because a measurable negative model–discretization cross-term disappeared. | The residual claim is mathematically substantive and was not found verbatim, but the algorithmic consequence—co-design or adapt the solver—is already mature. | **SURVIVE_TO_RED_TEAM** |
| C08 | *Complexity Matters: Dynamics of Feature Learning…* [L25]; *On the Foundations of Shortcut Learning* [L26]; *Removing Spurious Features Can Hurt Accuracy* [L27]; *Learning to Hint for Reinforcement Learning* [L28]; temporary subword-boundary priors in *Decoupling the Benefits of Subword Tokenization…* [L35] | Spurious/core feature availability shapes learning dynamics; spurious features can persist; removing them can reduce accuracy; training-only hints/scaffolds and temporarily supplied structural priors can create transferable updates. These works predict strong path and schedule effects. | A strictly information-, loss-, gradient-, and compute-matched demonstration that an early deliberately spurious feature causally improves the later invariant representation after complete withdrawal. | Potentially substantive if all matching succeeds; no direct paper with this exact sign and intervention was found. | **SURVIVE_TO_RED_TEAM** |
| C09 | *Teacher Supervision over Representation Equivalence Classes* [L29]; *Normalized Feature Distillation* [L30] | Raw feature coordinates are not absolute; invariant geometry/logits are the proper targets; geometry recovery can fail to recover capability; normalization/alignment fixes coordinate artifacts. A teacher-gauge experiment is already predicted and substantially executed. | Repeat the quotient argument under a new student/teacher pair or task. | Cosmetic. | **KILL** |
| C10 | *Shape Matters: Understanding the Implicit Bias of the Noise Covariance* [L31]; *Internal Data Repetition Destroys Language Models* [L32]; *Prismatic Synthesis* [L33] | Noise covariance can select different solutions; repetition has nonmonotone compute-equivalent harm; gradient-space diversity predicts OOD generalization. A duplicate-topology effect through covariance is expected. | Match exposure, mean gradient, and common order statistics exactly while varying only covariance eigenspaces. | The control is useful, but the mechanism and practical conclusion are established. | **KILL** |

### 4.5 Exact-neighbor results: C11–C15

| ID | Verified closest primary work | What is already established and what it predicts | Exact remaining delta | Substantive or cosmetic? | Verdict |
|---|---|---|---|---|---|
| C11 | *Say Anything but This: When Tokenizer Betrays Reasoning in LLMs* [L34]; *Decoupling the Benefits of Subword Tokenization…* [L35]; *Byte Latent Transformer* [L36]; graph-tokenization depth/conditioning theory in *Lost in Tokenization* [L37]; *Randomized Positional Encodings* [L38]; *Language Models Are Not Equally Robust to Non-Canonical Tokenization across Languages* [L39]; homotoken training [L40]; and the controlled tokenizer metrics in *TokEval* [L41] | Language tokenization can materially change reasoning, throughput, inductive bias, and robustness even when surface content is recoverable; graph-tokenization theory shows that tokenization can also alter required Transformer depth or conditioning; positional OOD causes length cliffs; and training on alternative segmentations can induce tokenization robustness. These works predict a refinement penalty and a position-based mitigation. | Hold the refined token stream, targets, length, and FLOPs fixed and change only the position map from physical microsteps to a logical quotient; ideally prove a refinement-equivariance theorem. | The position-only causal delta is real and not located verbatim, but its direction and remedy are strongly anticipated. | **SURVIVE_TO_RED_TEAM** |
| C12 | *Single Teacher, Multiple Perspectives* [L42]; *Multi-Teacher Ensemble Distillation: A Mathematical Framework* [L43]; *Adaptive Group Robust Ensemble Knowledge Distillation* [L44] | Teacher diversity, correlated errors, consensus, and shared blind spots govern distillation; ensemble distillation can amplify subgroup harm; methods already weight diversity/compatibility. A co-error statistic is the obvious next refinement. | Match all common marginal and pairwise diversity metrics while varying higher-order error topology. | A cleaner statistic, not a new mechanism; likely an auxiliary predictor/weighting rule. | **KILL** |
| C13 | *LLMs Can Implicitly Learn from Mistakes In-Context* [L45]; *LC-ICL* [L46]; *Enhancing Few-Shot ICL by Leveraging Negative Samples* [L47] | Incorrect plus correct examples can outperform rationale-heavy or positive-only contexts; negative/error-labeled demonstrations are already used to improve ICL. These works predict the candidate’s sign. | Choose the wrong example by an explicit version-space/shortcut-separation criterion. | A selection heuristic layered on a direct phenomenon. | **KILL** |
| C14 | *The Loss Does Not See the Basis, but Adam Does* [L04]; *Signed-Permutation Coordinate Transport* [L05] | Adam separates gauge-equivalent initializations at the first step; equivariant optimizers remain matched; exact optimizer-state transport matters. This is the candidate. | Apply the same fact to a different checkpoint or downstream task. | Direct collision. | **KILL** |
| C15 | *KVQuant* [L48]; *When Attention Sink Emerges* [L49]; *Attention Sinks Are Provably Necessary…* [L50]; *Softpick* [L51]; *The Spike, the Sparse and the Sink* [L52]; *KVSink* [L53] | Sink tokens, outliers, quantization, and low-precision robustness are already linked; established methods preserve sinks, redesign attention to remove them, and analyze their functional role. KVSink directly studies the mutual influence of sinks and KV quantization. | Show that deliberately degrading sink precision—not preserving it—improves a fixed-context reasoning task through causal sink attenuation. | The sign is not the standard result, but it is a narrow reversal against a mature systems baseline and is likely evaluator/regularization-sensitive. It does not justify a separate seed. | **KILL** |

### 4.6 Phase-3 summary

- **KILL:** C01, C02, C03, C05, C06, C09, C10, C12, C13, C14, C15.
- **HOLD, not authorized:** C04.
- **SURVIVE_TO_RED_TEAM:** C07, C08, C11.

No candidate was advanced merely because its exact sentence did not appear in a title or abstract. Advancement required an unoccupied claim–mechanism–baseline triple and a cheap discriminating test.

---

## 5. Adversarial red-team reports for the three survivors

The purpose of this phase is not to make the candidates sound better. Each candidate is reviewed as though three skeptical ICLR reviewers had already read the strongest possible version of the paper. A candidate survives only if one compact test could simultaneously defeat the novelty, methods, and significance objections.

### 5.1 C07 — Learned-model error can cancel numerical-solver error

#### Candidate claim

Let the exact probability-flow ODE be

\[
\dot x(t)=f^\star(x(t),t),
\]

and let a learned field be

\[
\hat f_\theta=f^\star+e_\theta.
\]

For a fixed numerical solver \(\mathcal S_h\) with step size or time grid \(h\), write the endpoint error schematically as

\[
E_{\mathrm{end}}(\theta,h)
=
E_{\mathrm{model}}(\theta)
+
E_{\mathrm{num}}(h;f^\star)
+
E_{\mathrm{cross}}(e_\theta,h)
+
O(\|e_\theta\|^2+h^{p+1}).
\]

The proposed inversion is that a model with **smaller standalone vector-field error** can produce **worse few-step samples** because improving the model removes a favorable negative cross-term:

\[
\|e_{\theta_1}\|<\|e_{\theta_2}\|
\quad\text{but}\quad
E_{\mathrm{end}}(\theta_1,h)>E_{\mathrm{end}}(\theta_2,h),
\]

with the ordering reversing under sufficiently accurate integration. The mechanistic object is not generic “error shaping”; it is a measured interaction between a frozen learned field and a frozen discretization rule.

#### Novelty-reviewer objection

The literature already treats the learned diffusion/flow model and its solver as a coupled object. DPM-Solver-v3 estimates model statistics to reduce solver error [L20]; Bespoke Solvers explicitly tailor a solver to a pretrained flow [L21]; optimized few-step samplers jointly select model evaluations and solver parameters [L22]; loss-adaptive schedules use the learned model’s error profile [L23]. More damagingly, recent analyses already identify opposite-sign leading errors, nonmonotonic benefits from additional integration, endpoint-decoding effects, and model-parameterization-dependent overshoot [L19, L24].

A reviewer can therefore say: “You have isolated one Taylor cross-term behind a phenomenon that model-specific sampler design already exploits.” Unless the cross-term yields a qualitatively new prediction that existing local-error, truncation-error, and learned-solver analyses cannot make, the contribution is explanatory bookkeeping rather than a new research seed.

#### Methods-reviewer objection

The phrase “better score model” is underdetermined. Uniform score MSE, likelihood weighting, time-local error, Jacobian error, stiffness, and endpoint-relevant weak error can rank models differently. A reduction in \(\int \|e_\theta\|^2\,dt\) may change the field’s derivatives, Lipschitz constants, or solver stability region, so an endpoint inversion need not be a cross-term at all. FID and finite-sample image metrics add another source of rank instability. A convincing test must separate:

1. field approximation error;
2. ordinary truncation error on the exact field;
3. stability/stiffness changes caused by the learned field;
4. the proposed signed interaction term; and
5. endpoint decoding or metric noise.

Without an exact or near-exact reference solution, the decomposition is not identified.

#### Significance-reviewer objection

Even a clean positive result appears to imply the already-obvious prescription: validate samplers on the actual learned model, or co-design the time grid and solver with that model. That is already standard in the closest work [L20–L23]. A new scalar cross-term estimator would likely become another sampler-ranking diagnostic. This is useful, but it is not automatically a field-level conceptual shift or an Oral-level consequence.

#### One experiment/theorem that could defeat all three objections

A minimally adequate test would need both an **identifiable analytic system** and a **real-model transfer**, with all choices frozen before looking at outcomes.

**Analytic component.** Use a two-dimensional Gaussian-mixture probability flow with an exact score and high-accuracy reference trajectories. Construct a one-parameter learned-field family

\[
\hat f_\alpha=f^\star+\alpha e,
\]

where \(e(x,t)\) is fixed and its local derivatives are available. For Euler and Heun at 4, 8, and 64 function evaluations:

- compute exact endpoint weak error under fixed test functions;
- compute standalone learned-field error on the same state-time distribution;
- derive the leading signed model–discretization cross-term by a backward-error or modified-equation expansion;
- prospectively predict, before endpoint evaluation, the \(\alpha\)-interval in which decreasing \(|\alpha|\) worsens the coarse solver;
- verify that the inversion disappears with the 64-evaluation reference solver.

**Real-model component.** On one open CIFAR-10 diffusion/flow checkpoint, form a controlled interpolation between the checkpoint field and a calibrated residual perturbation. Freeze samples, seeds, time grids, decoder, and metrics. The analytic estimator must predict the ordering of at least three perturbation levels under two solvers, and the ordering must reverse or collapse under a high-accuracy solver. Local error, Jacobian norm, and stiffness-matched perturbation controls must fail to explain the effect.

A theorem establishing the sign of the leading cross-term for the analytic family, followed by a preregistered real-model rank prediction, would be the strongest version of the candidate.

#### Red-team disposition

**REJECT BEFORE COMPUTE.** The existence of cancellation is close to a one-step numerical-analysis observation once a learned field is inserted into a finite-order solver. The useful consequence—model-conditioned solver selection or co-design—is already heavily occupied. A successful synthetic theorem plus one CIFAR demonstration would likely be reviewed as a sharp explanation of known sampler behavior, not as a fresh Oral-level seed. The residual novelty is real but too narrow relative to the literature density.

---

### 5.2 C08 — A deliberately temporary shortcut can improve the final invariant representation

#### Candidate claim

Let data contain a core feature \(c\), a temporary scaffold \(s\), and label \(y\). During an early phase, \(s\) is predictive of \(y\); during the later phase and at test time it is absent, randomized, or anti-correlated. The candidate claims that there exists a controlled regime in which training with the early shortcut yields a better final invariant predictor than training only on the core signal:

\[
R_{\mathrm{OOD}}(\theta^{\mathrm{scaffold}}_T)
<
R_{\mathrm{OOD}}(\theta^{\mathrm{core}}_T),
\]

although the final predictor no longer causally relies on \(s\). The proposed mechanism is that the shortcut first moves the representation into a basin or feature-learning regime from which the core feature becomes easier to acquire; withdrawal then removes shortcut dependence while retaining the useful representational scaffold.

The counterintuitive claim is stronger than “curriculum helps” or “extra information helps”: the early feature must be **spurious with respect to the deployment distribution**, and its benefit must survive controls matching information, optimization ease, gradient scale, compute, and final shortcut reliance.

#### Novelty-reviewer objection

Shortcut-learning theory already emphasizes path dependence and competition between simple and complex features [L25, L26]. Removing spurious features can reduce accuracy [L27], and training-only hints or privileged signals can accelerate or redirect learning [L28]. A particularly close 2026 result temporarily injects subword-boundary priors—including end-boundary information that leaks future bytes—during byte-level pretraining and then returns to the baseline regime [L35]. Curriculum learning, learning using privileged information, auxiliary-task pretraining, feature annealing, and teacher forcing provide further nearby precedents.

A reviewer can therefore reduce the paper to: “An informative early curriculum helps optimization; then the cue is removed.” Calling the cue a shortcut does not by itself create a new mechanism. To survive, the candidate must show a benefit that cannot be reproduced by a core-feature duplicate, an easy-example curriculum, an auxiliary hint, increased early margin, or any matched optimization scaffold.

#### Methods-reviewer objection

The central intervention is extraordinarily confounded. A predictive shortcut changes at least:

- mutual information with the label;
- early loss and margin;
- gradient magnitude and direction;
- representation rank and conditioning;
- sample difficulty;
- effective curriculum;
- initialization-to-basin distance; and
- total exposure to useful supervision.

Matching only accuracy or total mutual information is insufficient. Moreover, “no final reliance” requires causal feature interventions, not merely low linear-probe accuracy. The withdrawal time can be tuned post hoc, creating a large researcher-degree-of-freedom problem. A positive result on Colored MNIST is particularly vulnerable to being dismissed as a constructed schedule artifact.

#### Significance-reviewer objection

The obvious method is a schedule: introduce an auxiliary cue, then anneal it away. Even if the schedule works, the practical message overlaps curriculum design, hints, privileged information, and pretraining. To reach Oral significance, the work would need a predictive law identifying **which otherwise-spurious cue**, **when to withdraw it**, and **why the induced representation transfers**—not just another regularizer or schedule selected on validation data.

#### One experiment/theorem that could defeat all three objections

A minimally credible test would require a synthetic system with an identifiable mechanism and a natural-domain replication.

**Synthetic causal construction.** Build a two-layer network task with a high-frequency/core feature and a simple temporary feature. Choose the data distribution so that gradient-flow dynamics can be approximated analytically. Compare:

1. **temporary shortcut:** predictive in phase A, independent or anti-correlated in phase B;
2. **core duplicate:** an equally predictive second view of the core feature;
3. **easy-core curriculum:** no shortcut, but examples selected to match phase-A loss and margin;
4. **hint/LUPI control:** an auxiliary training-only target with matched label information;
5. **gradient-matched control:** synthetic examples chosen online to match shortcut-run gradient norms and first-order loss descent; and
6. **compute-matched core-only baseline.**

Freeze the phase boundary prospectively using a predicted dynamical transition, not validation performance. At the boundary, perform feature-subspace surgery: remove the scaffold direction, transplant the remaining representation into a common head, and continue with identical phase-B data. The shortcut effect must remain after surgery, while direct interventions on \(s\) at the endpoint change predictions by less than a preregistered tolerance.

**Natural replication.** Repeat the signed prediction on one spurious-correlation benchmark such as Waterbirds or a tightly controlled texture/shape benchmark using two architecture families. All schedules, augmentations, and hyperparameters must be inherited from the synthetic prediction. The temporary-shortcut condition must outperform all matched scaffolds on worst-group accuracy, not merely average accuracy.

A theorem would need to identify a parameter regime where the shortcut increases acquisition of the core feature after withdrawal, while each matched control provably does not.

#### Red-team disposition

**REJECT BEFORE COMPUTE.** This candidate has the greatest intuitive surprise of the three, but its causal claim is not cheaply identifiable. The controls needed to distinguish a genuinely spurious scaffold from ordinary curriculum, privileged information, extra label information, or easier optimization are themselves a major research program. A synthetic positive would be easy to engineer and hard to trust; the temporary-boundary-prior result in [L35] also narrows the residual novelty, while a convincing natural transfer would no longer be a cheap Stage 0. The most likely practical output remains a cue-annealing schedule, which does not clear the required non-obvious-consequence gate.

---

### 5.3 C11 — Lossless token refinement fails because the model follows a physical rather than logical clock

#### Candidate claim

Let a logical sequence be \(z_{1:n}\). A lossless refinement map \(r\) replaces each logical symbol with an injective pair of microtokens,

\[
r(z_t)=(u_t,v_t),
\]

so that the original sequence can be recovered exactly. Standard positional indexing assigns the pair positions \(2t\) and \(2t+1\). The proposed intervention keeps the **microtoken identities, sequence length, attention mask, targets, data, and compute fixed**, but replaces physical positions with a logical quotient:

\[
\pi_{\mathrm{phys}}(u_t)=2t,
\qquad
\pi_{\mathrm{phys}}(v_t)=2t+1,
\]

versus

\[
\pi_{\mathrm{logic}}(u_t)=
\pi_{\mathrm{logic}}(v_t)=t,
\]

with a two-valued phase embedding distinguishing \(u_t\) from \(v_t\). The candidate predicts that physical indexing creates an avoidable length-generalization cliff, whereas logical indexing restores refinement equivariance:

\[
F_{\mathrm{logic}}(r(z_{1:n}))
\approx
F_{\mathrm{atomic}}(z_{1:n})
\quad\text{while}\quad
F_{\mathrm{phys}}(r(z_{1:n}))
\not\approx
F_{\mathrm{atomic}}(z_{1:n})
\]

outside the training-length range.

#### Novelty-reviewer objection

Tokenizer choice is already known to change reasoning, robustness, throughput, and structural inductive bias even when surface content is recoverable [L34–L36, L39–L41]. Cross-domain graph-tokenization theory further shows that a lossless tokenization can be ill-conditioned and can change the Transformer depth needed for the same computation [L37]. Positional schemes are known to govern length extrapolation [L38], while alternative-tokenization and homotoken training already improve tokenization robustness [L39, L40]. Byte-level and patch-based models explicitly decouple representational units from fixed tokenizer boundaries [L36].

A reviewer can therefore say that the result is predicted: doubling the physical clock pushes a model farther out of its trained positional regime, and dividing positions by two or adding segment phases is an ordinary position rescaling. The exact “same microtoken stream, different position quotient” intervention is cleaner than the closest literature, but the sign is not surprising enough on its own.

#### Methods-reviewer objection

Lossless refinement changes more than token identity unless the experiment is unusually strict. It changes sequence length, target placement, number of attention interactions, effective depth per logical step, token frequencies, embedding statistics, and positional frequency exposure. In the proposed position-only comparison, the logical quotient also creates repeated positions and adds a phase channel, which may increase capacity or alter attention symmetry. RoPE rescaling, ALiBi slope adjustment, NoPE, randomized positions, or simply training on longer physical positions could recover the same effect.

The method must therefore separate a true quotient-clock mechanism from generic position interpolation, extra phase capacity, or shifted grouping. It also needs a theorem specifying the architecture class and the exact equivariance being claimed.

#### Significance-reviewer objection

Even if logical positions rescue synthetic algorithmic tasks, the immediate recommendation is tokenizer-aware position IDs or position rescaling. That is an engineering fix, not necessarily a new theory of representation. Natural language lacks a unique logical token boundary, so the intervention may depend on an oracle segmentation. A broad paper would need a principled boundary estimator and transfer across natural language or multimodal tokenizations; that extension risks becoming another tokenizer/positioning method.

#### One experiment/theorem that could defeat all three objections

The strongest cheap test is a **position-only, exact-stream intervention** paired with a refinement-equivariance theorem.

**Theorem target.** For a restricted causal Transformer with a block-local microtoken encoder and logical-position attention, prove that there exists a parameter mapping from an atomic model to its two-token refinement such that hidden states at logical boundaries and output distributions are exactly preserved. Show that ordinary physical absolute/RoPE positions break this equivariance in a way that grows with extrapolation length, while a quotient position plus fixed phase restores it.

**Experiment.** Generate two algorithmic tasks—running parity and running sum modulo five. Train on logical lengths 16–64 and evaluate through 256. Use identical paired microtoken streams in every refined condition. Compare:

1. physical positions;
2. logical quotient positions plus fixed phase;
3. RoPE frequency rescaling without shared positions;
4. shifted shared-position grouping;
5. physical positions plus the same phase capacity; and
6. a NoPE or ALiBi positional-family replication.

The quotient intervention must rescue both tasks and two positional families, while the three mechanism controls recover only a small fraction of the gap. In-distribution accuracy and loss must remain matched. A natural follow-up would then need to predefine a non-oracle refinement—such as deterministic digit, byte, or image-patch subdivision—and make a prospective prediction about its generalization boundary.

#### Red-team disposition

**REJECT BEFORE COMPUTE.** This is the cleanest potential Stage 0 and the cheapest to falsify, but a positive outcome would still be read as a precise demonstration of known tokenization–position coupling. The expected fix—use logical positions, rescale the clock, or train for segmentation invariance—is close to existing positional and tokenization-robustness work [L34–L40]. The natural-domain expansion requires a defensible logical boundary, and without that expansion the result lacks an Oral-level paper arc. It remains a useful diagnostic experiment, not the next seed.

### 5.4 Oral-gate scorecard after red teaming

A checkmark means the candidate plausibly clears the item after the strongest charitable interpretation; a cross means it fails; a triangle means the case is conditional or incomplete.

| Oral gate | C07 solver cross-cancellation | C08 temporary shortcut | C11 logical token clock |
|---|---:|---:|---:|
| Counterintuitive sign survives literature | △ | ✓ | △ |
| Exact non-cosmetic novelty gap | △ | △ | △ |
| Mechanistic causal object is identifiable cheaply | ✓ | ✗ | ✓ |
| One-day decisive falsification is credible | ✓ | ✗ | ✓ |
| Consequence is not merely tune/schedule/reweight | ✗ | ✗ | ✗ |
| Two-task × two-family confirmation is realistic | △ | ✗ | △ |
| Three-figure Oral paper arc is credible | ✗ | △ | ✗ |
| Broad scientific importance beyond the carrier | △ | △ | △ |
| **Terminal result** | **REJECT** | **REJECT** | **REJECT** |

No candidate defeats all three reviewer classes with one cheap, decisive package.

---

## 6. Final-seed selection, mathematical standard, and missing conceptual ingredient

### 6.1 No final seed selected

There is **no surviving final seed**. Therefore this report does not rename a residual candidate as a project, does not issue a Stage-0 authorization, and does not allocate repository implementation work.

Let the Oral gate for candidate \(c\) be

\[
G(c)
=
G_{\mathrm{surprise}}(c)
\land G_{\mathrm{novelty}}(c)
\land G_{\mathrm{mechanism}}(c)
\land G_{\mathrm{cheap\ kill}}(c)
\land G_{\mathrm{nonobvious\ consequence}}(c)
\land G_{2\times2}(c)
\land G_{\mathrm{paper\ arc}}(c)
\land G_{\mathrm{breadth}}(c).
\]

The binding launch rule is

\[
\exists c:\ G(c)=1.
\]

For the present search,

\[
G(\mathrm{C07})=G(\mathrm{C08})=G(\mathrm{C11})=0.
\]

The failure is not that every residual claim is false. The failure is that none simultaneously has an unoccupied causal core, a decisive cheap test, a non-obvious consequence, and a credible Oral-level expansion.

### 6.2 What a genuinely new seed would need

The missing ingredient is a new **causal object**, not another carrier. A future seed should define an intervention variable \(z\) and an equivalence class \(\mathcal E\) such that competing explanations are matched by construction:

\[
\mathcal E
=
\left\{
\text{same task-relevant input–output function},
\text{same accessible information},
\text{same compute},
\text{same capacity},
\text{same coordinate gauge},
\text{same optimizer state},
\text{same numerical solver}
\right\}.
\]

A valid seed then needs two members \(a,b\in\mathcal E\) differing only in \(z\), with a prospectively predicted behavioral reversal:

\[
\operatorname{sign}
\left[
M(\operatorname{do}(z=z_a))-M(\operatorname{do}(z=z_b))
\right]
\]

predicted before the outcome is measured and reproduced across at least two tasks and two model families.

Four additional properties are required.

1. **Location prediction.** A theorem, estimator, or structural argument must predict where the reversal occurs, rather than merely measuring it afterward.
2. **Confound resistance.** Matching function, information, compute, gauge, optimizer, and numerics must not erase the effect.
3. **Non-obvious consequence.** The winning intervention must imply more than an auxiliary predictor, regularizer, reweighting rule, routing heuristic, curriculum, schedule, solver tuner, or hyperparameter selector.
4. **Compact falsification.** The first test must expose the central sign or kill it within the repository’s 4-GPU, approximately 4-GPU-hour Stage-0 envelope.

None of C07, C08, or C11 supplies all four. The next search should therefore begin from a different primitive rather than from diffusion solvers, shortcut schedules, or tokenizer clocks.

---

## 7. Strongest baselines and confound-control requirements

This section records the controls that any future candidate—and especially any attempted revival of the three red-team candidates—would have to defeat. They are requirements, not optional ablations.

### 7.1 Cross-domain baseline matrix

| Confound class | Required matching or control | Failure interpretation |
|---|---|---|
| **Task function** | Exact replay, function-preserving reparameterization, or matched logits on a prespecified support | The effect may be ordinary task-function change. |
| **Accessible information** | Match label mutual information, side-channel information, target entropy, and recoverability | The intervention may simply reveal more useful information. |
| **Compute** | Match updates, tokens, sequence interactions, function evaluations, wall-clock budget, and effective batch size | The effect may be a compute allocation difference. |
| **Capacity and scale** | Match parameter count, activation dimension, norm budget, auxiliary embeddings, and context length | The intervention may add capacity. |
| **Coordinate/gauge** | Apply exact state and optimizer transport or use invariant observables | Coordinate-indexed conclusions may be non-identifiable. |
| **Optimizer state** | Match or explicitly reset moments, schedulers, loss scalers, EMA, and RNG state | The effect may live in trainer memory rather than the proposed object. |
| **Numerics** | Match solver family, order, grid, precision, decoder, stopping rule, and reference integration | Numerical artifacts may produce the sign. |
| **Data trajectory** | Pair seeds, minibatch order, augmentation draws, and curriculum exposure | Path differences may arise from ordinary sampling noise. |
| **Selection and metrics** | Freeze primary metrics, corrections, stopping criteria, and all thresholds before inspection | The effect may be metric shopping or schedule tuning. |
| **External validity** | Replicate the signed prediction on two tasks and two model/algorithm families | A single constructed carrier cannot support a general claim. |

### 7.2 C07-specific controls

A solver-error study would need, at minimum:

- uniform, likelihood-weighted, and endpoint-adjoint-weighted field-error baselines;
- local Jacobian, Lipschitz, curvature, and stiffness measurements;
- exact or very high-accuracy reference trajectories;
- Euler, Heun, and one modern diffusion/flow solver under the same function-evaluation budget;
- fixed time grids versus model-adaptive grids;
- endpoint-decoding and early-stopping controls;
- perturbations matched in norm but orthogonal to the predicted cross-term direction;
- sample-quality metrics reported with paired confidence intervals and a metric-free analytic endpoint test; and
- a preregistered rank prediction rather than retrospective regression.

### 7.3 C08-specific controls

A temporary-shortcut study would need:

- a core-feature duplicate with matched early predictiveness;
- an easy-core curriculum with matched loss and margin;
- a training-only hint or privileged-information control;
- matched gradient norm, first-order loss decrease, updates, and label information;
- multiple fixed withdrawal times selected from theory rather than validation;
- endpoint feature intervention, counterfactual replacement, and subspace surgery demonstrating negligible final shortcut dependence;
- anti-correlated, randomized, and absent phase-B variants;
- worst-group rather than only average performance; and
- two architecture families with no condition-specific retuning.

### 7.4 C11-specific controls

A token-refinement study would need:

- the exact same paired microtoken stream, sequence length, masks, and targets in every primary comparison;
- physical versus logical position IDs as the only primary change;
- physical positions plus an equal-capacity phase embedding;
- RoPE frequency rescaling without shared positions;
- shifted or randomized grouping of shared positions;
- NoPE or ALiBi replication;
- equal updates, examples, tokens, attention interactions, and FLOPs;
- matched in-distribution loss and accuracy;
- evaluation at multiple absolute and relative extrapolation lengths; and
- a theorem or constructive parameter map defining the claimed refinement equivariance.

These controls explain why the three residuals cannot be promoted on intuition alone.

---

## 8. Counterfactual preregistered Stage-0 kill test

> **Status: NOT AUTHORIZED.** This protocol is included because the divergence prompt requires an exact cheap falsification design for the strongest residual. It is a counterfactual preregistration, not a `GO_STAGE_0_ONLY` decision. No run should begin under the terminal verdict in Section 11.

Among the rejected residuals, C11 offers the cleanest and cheapest falsification. The protocol below is deliberately strict enough that a routine “positions matter” result would not pass.

### 8.1 Name and single question

**Stage 0-R: Token-Refinement Clock Test**

Question:

> With the refined microtoken stream, sequence length, targets, data, and compute held fixed, can changing only the positional quotient remove a lossless-refinement length-generalization cliff in two tasks and two positional model families, while ordinary rescaling and extra-capacity controls fail?

### 8.2 Tasks and distributions

Use two procedurally generated causal sequence tasks.

1. **Running parity.** Each logical symbol is a bit. At every logical boundary, predict the parity of all bits seen so far.
2. **Running sum modulo five.** Each logical symbol is in \(\{0,1,2,3,4\}\). At every logical boundary, predict the cumulative sum modulo five.

Training logical lengths are sampled uniformly from \(16\) through \(64\). Fixed held-out evaluation sets contain 2,000 sequences for each length in

\[
\{32,64,96,128,192,256\}.
\]

No generated test example may appear in training. Dataset generators and hashes must be frozen before training.

### 8.3 Encodings and interventions

Let \(z_t\) be a logical symbol.

- **A — Atomic reference.** One token per logical symbol; ordinary position \(t\).
- **RP — Refined physical.** Deterministically encode \(z_t\) as the injective pair \((u_t,v_t)\); positions are \(2t\) and \(2t+1\).
- **RQ — Refined quotient.** Use the exact same token IDs and order as RP. Both tokens receive logical position \(t\), plus a fixed two-valued phase embedding identifying first versus second microtoken.
- **RF — Frequency-rescaled control.** Same tokens as RP; retain distinct physical positions but rescale the positional frequency or slope so that the largest logical clock value matches A.
- **RS — Shifted-quotient control.** Same tokens and phase capacity as RQ, but share positions across deliberately incorrect shifted pairs, e.g. the second microtoken of \(t\) with the first microtoken of \(t+1\).
- **RPP — Phase-capacity control.** Physical positions as in RP plus the same phase embedding used by RQ.

Targets are scored only at the second token of each legitimate pair in all refined conditions. Loss masks, attention masks, token streams, and target indices are bitwise identical across RP, RQ, RF, RS, and RPP except for the declared position map and phase input.

### 8.4 Model families

Use two small causal Transformer families with the same non-positional architecture:

- **RoPE family:** 3 layers, width 96, 4 heads, MLP width 384;
- **ALiBi family:** the same architecture with ALiBi replacing RoPE.

Use pre-layer normalization, tied input/output embeddings where applicable, no dropout, and no architecture-specific tuning. All refined conditions share parameter counts; where RQ/RPP/RS include a phase embedding, add an inert equal-parameter phase table to RP and RF so capacity is exactly matched.

### 8.5 Training protocol

- Optimizer: AdamW, learning rate `3e-4`, betas `(0.9, 0.98)`, weight decay `0.01`, 200-step linear warm-up, then cosine decay to `3e-5`. These values are frozen without an extrapolation pilot.
- Updates: exactly 4,000 per run.
- Batch: 128 generated sequences, length-balanced.
- Precision: BF16 where deterministic kernels permit; otherwise FP32.
- Seed pairing: three preregistered seeds for every condition; each paired run receives the same initialization after the declared positional parameters, minibatch sequence, and generated examples.
- No early stopping, no condition-specific hyperparameters, and no inspection of extrapolation results before every planned run and checksum is complete. Failure to reach the learnability gate is itself a kill, not permission to tune.

The primary confirmatory set is

\[
2\text{ tasks}\times2\text{ families}\times
\{A,RP,RQ,RF,RS,RPP\}\times3\text{ seeds}=72\text{ runs}.
\]

All 72 jobs and their launch order must be frozen before execution. The package has a 60-minute wall-clock and four-GPU-hour aggregate hard stop. Crossing that limit is an integrity-gate failure; updates or controls may not be reduced after launch.

### 8.6 Primary estimands

For task \(d\), model family \(m\), and evaluation length \(L\), let \(a_{d,m,c,L}\) be mean exact logical-state accuracy over the scored logical boundaries in condition \(c\). Final-boundary accuracy is reported as a secondary diagnostic. Define:

\[
\Delta^{\mathrm{cliff}}_{d,m,L}
=a_{d,m,A,L}-a_{d,m,RP,L},
\]

\[
\Delta^{\mathrm{rescue}}_{d,m,L}
=a_{d,m,RQ,L}-a_{d,m,RP,L},
\]

and rescue fraction

\[
q_{d,m,L}
=
\frac{a_{d,m,RQ,L}-a_{d,m,RP,L}}
{\max\{a_{d,m,A,L}-a_{d,m,RP,L},10^{-6}\}}.
\]

The primary confirmatory cells are the four task-by-family combinations at \(L=256\). Length \(128\) is a signed replication; other lengths characterize the curve.

### 8.7 Exact pass and kill thresholds

Every gate below is conjunctive. Failure of any gate is a Stage-0 kill.

1. **Learnability gate.** For every task and family, median exact sequence accuracy for A, RP, and RQ at all training-range lengths \(L\le64\) must be at least 98%. Otherwise the setup is undertrained or not comparable: **KILL**.

2. **Refinement-cliff gate.** In all four primary cells,

   \[
   \Delta^{\mathrm{cliff}}_{d,m,256}\ge25\text{ percentage points}.
   \]

   If the supposedly lossless physical refinement does not create a large cliff everywhere: **KILL**.

3. **Quotient-rescue gate.** In all four primary cells:

   \[
   \Delta^{\mathrm{rescue}}_{d,m,256}\ge20\text{ points},
   \qquad
   q_{d,m,256}\ge0.70.
   \]

   In addition, every one of the three paired-seed rescue differences must exceed 10 points, and the Holm-adjusted 95% hierarchical-bootstrap lower confidence bound for \(\Delta^{\mathrm{rescue}}\)—resampling seeds and then evaluation sequences—must exceed 10 points in every cell. Otherwise: **KILL**.

4. **Mechanism-specificity gate.** For each primary cell, define the best ordinary-control recovery

   \[
   b_{d,m}
   =
   \max_{c\in\{RF,RS,RPP\}}
   \left(a_{d,m,c,256}-a_{d,m,RP,256}\right).
   \]

   Require

   \[
   b_{d,m}\le0.25\,\Delta^{\mathrm{rescue}}_{d,m,256}
   \]

   in all four cells. If position rescaling, wrong grouping, or equal phase capacity recovers more than one quarter of the quotient rescue in any cell: **KILL**.

5. **Length-sign gate.** \(\Delta^{\mathrm{rescue}}_{d,m,L}>0\) for every task, family, and \(L\in\{96,128,192,256\}\), and the median rescue at \(L=128\) must be at least 10 points. Any sign reversal: **KILL**.

6. **In-distribution equivalence gate.** At \(L=64\), the absolute median accuracy difference between RP and RQ must be at most 2 points, and their mean held-out token loss must differ by at most 0.02 nats. Otherwise RQ may simply be an easier or higher-capacity in-distribution model: **KILL**.

7. **Run-integrity gate.** All prespecified seeds, controls, hashes, and metrics must complete within the hard resource cap. Missing conditions, divergent runs, or post-outcome replacements imply **KILL**, not an inconclusive pass.

Passing all seven gates would **not** authorize a paper direction. It would only reopen the novelty/theory audit and require a preregistered natural-domain prediction that does not depend on oracle logical boundaries.

### 8.8 Statistical and reporting rules

- Pair runs by seed and generated evaluation set.
- Use a paired hierarchical bootstrap with 10,000 resamples: resample the three seeds, then resample sequences within each selected seed.
- Apply Holm correction across the four primary quotient-rescue tests.
- Report all seeds, all lengths, median and individual-run values, confidence intervals, and exact failures.
- The code must emit a machine-readable gate table whose final value is the conjunction of the seven gates.
- No alternate metric, seed deletion, schedule extension, architecture change, or threshold relaxation may convert a failure into a pass.

---

## 9. Resource and dependency estimate

### 9.1 Binding allocation

Because the terminal decision is NO-GO, the authorized allocation is:

| Resource | Authorized amount |
|---|---:|
| GPU-hours | **0** |
| New repository implementation | **0** |
| Dataset acquisition | **0** |
| Stage-0 launches | **0** |

### 9.2 Counterfactual cost of the strongest residual test

The protocol in Section 8 is designed to fit the repository envelope if a future decision explicitly reopens it.

| Item | Counterfactual estimate |
|---|---|
| GPUs | 4 × RTX 4090, one independent run per GPU |
| Expected wall time | 35–60 minutes on four GPUs |
| Hard wall-time stop | 60 minutes |
| Hard aggregate budget | **≤4 GPU-hours** |
| Expected per-run footprint | ≤4 GB VRAM |
| Storage | ≤1 GB including final checkpoints, logs, and fixed evaluation sets |
| Data | Procedurally generated; no external dataset download |
| Software | Python, PyTorch, NumPy, SciPy; no custom CUDA dependency required |
| Determinism | Frozen package lock, RNG seeds, generator hashes, and paired minibatch manifests |
| Stop rule | Terminate the package at the hard cap; an incomplete gate set cannot pass |

The 72-run matrix is small because each network has roughly sub-million-scale parameters, training sequences are at most 128 physical microtokens, and only final checkpoints are retained. Batched multi-run execution or sequential job packing may be used only if it preserves independent optimizer states and exact manifests. The launcher must stop at 60 minutes even if some jobs remain; incompleteness is a kill.

### 9.3 Comparative cost of the rejected red-team tests

| Candidate | Cheapest honest package | Estimated GPU budget | Main dependency | Why cost does not rescue it |
|---|---|---:|---|---|
| C07 | Analytic Gaussian-mixture flow plus one open CIFAR checkpoint, three perturbation levels, two coarse solvers, one reference solver | 3.5–4 GPU-hours | PyTorch, an open diffusion/flow checkpoint, high-accuracy ODE reference | Cheap enough, but the scientific consequence is already occupied by model-specific solver design. |
| C08 | Synthetic feature-dynamics system plus a small Waterbirds/texture-shape replication and matched scaffold controls | At least 4 GPU-hours for a weak version; a credible version likely exceeds the envelope | PyTorch, torchvision, benchmark data, causal feature interventions | The necessary confound controls and natural transfer are not a cheap kill. |
| C11 | Exact-stream logical-position quotient test in Section 8 | ≤4 GPU-hours | PyTorch only | Cheap and decisive for the narrow claim, but a positive result would still lack an Oral-level novelty/significance arc. |

No external paid API, physical robot, frontier model, or closed dataset is required for any of these counterfactual tests.

---

## 10. Three-figure paper arcs and predicted rejection reasons

A candidate must support a coherent three-figure scientific story before Stage 0. The figures below are the strongest plausible arcs, followed by the rejection each would probably receive even if the central experiment worked.

### 10.1 C07 paper arc: cross-cancellation in learned differential equations

**Figure 1 — The inversion.** Across a controlled learned-field family, standalone score/vector-field error improves monotonically while few-step endpoint quality worsens over a predicted interval; high-accuracy integration removes the inversion.

**Figure 2 — The mechanism.** An analytic decomposition and measured signed cross-term predict the inversion across Euler and Heun, outperforming field MSE, local truncation error, stiffness, and Jacobian baselines.

**Figure 3 — The consequence.** A cross-term-aware solver or schedule restores correct model ranking on two diffusion/flow checkpoints and improves few-step sampling without retraining.

**Likely rejection.** “Interesting numerical explanation, but model-specific and bespoke solvers already adapt to pretrained field statistics; opposite-sign and nonmonotone solver effects are known. The proposed correction is another solver-selection criterion rather than a broad new learning principle.”

### 10.2 C08 paper arc: spurious features as transient training scaffolds

**Figure 1 — The counterintuitive endpoint.** A temporary spurious cue improves worst-group generalization after complete withdrawal, whereas core-only, core-duplicate, easy-curriculum, and hint controls do not.

**Figure 2 — The mechanism.** Feature-dynamics measurements and subspace surgery show that the cue moves the network into a basin that accelerates core-feature acquisition; the final predictor has negligible causal dependence on the cue.

**Figure 3 — The rule.** A theory-predicted withdrawal time and cue-selection criterion transfer to two natural spurious-correlation tasks and two architectures without tuning.

**Likely rejection.** “The intervention adds a curriculum or privileged feature; exact information/gradient matching is incomplete; the withdrawal schedule is selected from the same environment; the practical method is cue annealing. Synthetic dynamics do not establish a general principle, and the natural experiments are vulnerable to hidden shortcut dependence.”

### 10.3 C11 paper arc: refinement equivariance and the logical positional clock

**Figure 1 — The lossless-refinement cliff.** Exact content-preserving token subdivision creates a sharp length-generalization failure despite matched in-distribution performance.

**Figure 2 — The causal clock.** Keeping the entire refined stream fixed and replacing only physical with logical quotient positions rescues extrapolation; a theorem gives an exact or approximate refinement-equivariant parameter map; rescaling, phase-capacity, and wrong-grouping controls fail.

**Figure 3 — Beyond synthetic sequences.** The theorem predicts failure and rescue under deterministic digit/byte/patch refinements in two natural tasks and two positional architectures.

**Likely rejection.** “Tokenization and position sensitivity are well established; the synthetic result follows from doubling positional indices; logical boundaries are supplied by an oracle; the natural extension is a tokenizer/position engineering method. The conceptual advance beyond tokenization invariance and positional extrapolation is limited.”

### 10.4 Arc-level conclusion

All three arcs can produce a technically respectable workshop or focused conference paper under strong execution. None currently offers the combination of surprise, unoccupied mechanism, non-obvious consequence, and breadth required for the stated target. A polished three-figure narrative cannot compensate for a crowded causal core.

---

## 11. Binding terminal decision

```text
NO_GO_NEED_NEW_SEED
```

This verdict has the following operational meaning:

- **No candidate is designated as the next research seed.**
- **No `GO_STAGE_0_ONLY` authorization is issued.**
- **No GPU experiment, coding branch, benchmark download, or implementation sprint is authorized by this document.**
- C04 remains a non-authorized HOLD, not a fallback.
- C07, C08, and C11 are rejected residuals, not backup projects.
- The failed MoE, bracket-steering, planning, uncertainty, operator-interference, generic error-shaping, and other repository-sealed directions remain closed under all renamings and domain transfers.
- The next search must introduce a genuinely different causal primitive satisfying the standard in Section 6.2.

The correct scientific action is to seek a new seed rather than spend compute validating a narrow effect whose likely interpretation and method are already occupied.

---

## 12. Primary-source bibliography

### 12.1 Repository documents

- **[P01]** `docs/pro/README.md`, *PRO research program: reading order and protocol*. [GitHub](https://github.com/ScottBlizzard/idle_2/blob/main/docs/pro/README.md)
- **[P02]** `docs/pro/RESEARCH_BRIEF.md`, *Binding constraints and research brief*. [GitHub](https://github.com/ScottBlizzard/idle_2/blob/main/docs/pro/RESEARCH_BRIEF.md)
- **[P03]** `docs/pro/PRO_NEXT_ORAL_SEED_DIVERGENCE.md`, *Binding fresh-divergence prompt executed by this report*. [GitHub](https://github.com/ScottBlizzard/idle_2/blob/main/docs/pro/PRO_NEXT_ORAL_SEED_DIVERGENCE.md)
- **[P04]** `docs/current/CURRENT_STATUS.md`, *Repository scientific status and sealed directions*. [GitHub](https://github.com/ScottBlizzard/idle_2/blob/main/docs/current/CURRENT_STATUS.md)
- **[P05]** `experiments/moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md`, *Frozen-MoE Stage-D terminal results*. [GitHub](https://github.com/ScottBlizzard/idle_2/blob/main/experiments/moe_route_noncompositionality/STAGE_D_RESULTS_REPORT_ZH.md)
- **[P06]** `docs/proposals/AI_RESEARCH_NEW_SEED_DIVERGENCE.md`, *Prior divergence attempt consulted only as a repetition blacklist*. [GitHub](https://github.com/ScottBlizzard/idle_2/blob/main/docs/proposals/AI_RESEARCH_NEW_SEED_DIVERGENCE.md)

### 12.2 Literature

- **[L01]** Xu, *Stored in Optimizer State, Valued by Later Training: A Causal Account of Subliminal Trait Transfer* (2026). [arXiv:2608.20442](https://arxiv.org/abs/2608.20442)
- **[L02]** *Training Memory in Deep Neural Networks: Mechanisms, Evidence, and Measurement Gaps* (2026). [arXiv:2601.21624](https://arxiv.org/abs/2601.21624)
- **[L03]** *Resetting the Optimizer in Deep RL: An Empirical Study* (2023). [arXiv:2306.17833](https://arxiv.org/abs/2306.17833)
- **[L04]** *The Loss Does Not See the Basis, but Adam Does* (2026). [arXiv:2608.05136](https://arxiv.org/abs/2608.05136)
- **[L05]** *Signed-Permutation Coordinate Transport for RMSNorm Transformers* (2026). [arXiv:2606.31963](https://arxiv.org/abs/2606.31963)
- **[L06]** *Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?* (2025). [arXiv:2502.20914](https://arxiv.org/abs/2502.20914)
- **[L07]** *Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability* (2026). [arXiv:2606.06333](https://arxiv.org/abs/2606.06333)
- **[L08]** *ReSAE: Residualized Sparse Autoencoders for Multi-Layer Transformer Interventions* (2026). [arXiv:2605.27819](https://arxiv.org/abs/2605.27819)
- **[L09]** *From Geometric Recovery to Causal Validation: A Reproducible Audit of Sparse Autoencoder Features, from Superposition Geometry to Causal Inertness* (2026). [arXiv:2607.12166](https://arxiv.org/abs/2607.12166)
- **[L10]** *What Algorithms Can Transformers Learn? A Study in Length Generalization* (2023). [arXiv:2310.16028](https://arxiv.org/abs/2310.16028)
- **[L11]** *On the “Induction Bias” in Sequence Models* (2026). [arXiv:2602.18333](https://arxiv.org/abs/2602.18333)
- **[L12]** *Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization* (2025). [arXiv:2511.07378](https://arxiv.org/abs/2511.07378)
- **[L13]** *What to Align in Multimodal Contrastive Learning?* (2024). [arXiv:2409.07402](https://arxiv.org/abs/2409.07402)
- **[L14]** *SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation* (2026). [arXiv:2605.18920](https://arxiv.org/abs/2605.18920)
- **[L15]** *PID-Guided Partial Alignment for Multimodal Decentralized Federated Learning* (2026). [arXiv:2601.10012](https://arxiv.org/abs/2601.10012)
- **[L16]** *When Do Task Vectors Interfere? Mapping the Validity Boundaries of Weight-Space Composition* (2026). [arXiv:2608.09490](https://arxiv.org/abs/2608.09490)
- **[L17]** *PermDoRA — Understanding Adapter Interference in Language Models: Limits of Parameter-Space Geometry* (2026). [arXiv:2606.11262](https://arxiv.org/abs/2606.11262)
- **[L18]** *Task Arithmetic in the Tangent Space: Improved Editing of Pre-Trained Models* (2023). [arXiv:2305.12827](https://arxiv.org/abs/2305.12827)
- **[L19]** *Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach* (2025). [arXiv:2512.24927](https://arxiv.org/abs/2512.24927)
- **[L20]** *DPM-Solver-v3: Improved Diffusion ODE Solver with Empirical Model Statistics* (2023). [arXiv:2310.13268](https://arxiv.org/abs/2310.13268)
- **[L21]** *Bespoke Solvers for Generative Flow Models* (2023). [arXiv:2310.19075](https://arxiv.org/abs/2310.19075)
- **[L22]** *Optimizing Few-Step Sampler for Diffusion Probabilistic Model* (2024). [arXiv:2412.10786](https://arxiv.org/abs/2412.10786)
- **[L23]** *Entropy-Based Dimension-Free Convergence and Loss-Adaptive Schedules for Diffusion Models* (2026). [arXiv:2601.21943](https://arxiv.org/abs/2601.21943)
- **[L24]** *x-Prediction Is All You Need: Training-Free Accelerated Generation via Endpoint Decodability* (2026). [arXiv:2607.06114](https://arxiv.org/abs/2607.06114)
- **[L25]** *Complexity Matters: Dynamics of Feature Learning in the Presence of Spurious Correlations* (2024). [arXiv:2403.03375](https://arxiv.org/abs/2403.03375)
- **[L26]** *On the Foundations of Shortcut Learning* (2023). [arXiv:2310.16228](https://arxiv.org/abs/2310.16228)
- **[L27]** *Removing Spurious Features Can Hurt Accuracy and Affect Groups Disproportionately* (2020). [arXiv:2012.04104](https://arxiv.org/abs/2012.04104)
- **[L28]** *Learning to Hint for Reinforcement Learning* (2026). [arXiv:2604.00698](https://arxiv.org/abs/2604.00698)
- **[L29]** *Teacher Supervision over Representation Equivalence Classes* (2026). [arXiv:2607.03572](https://arxiv.org/abs/2607.03572)
- **[L30]** *Normalized Feature Distillation for Semantic Segmentation* (2022). [arXiv:2207.05256](https://arxiv.org/abs/2207.05256)
- **[L31]** *Shape Matters: Understanding the Implicit Bias of the Noise Covariance* (2020). [arXiv:2006.08680](https://arxiv.org/abs/2006.08680)
- **[L32]** *Internal Data Repetition Destroys Language Models* (2026). [arXiv:2606.24998](https://arxiv.org/abs/2606.24998)
- **[L33]** *Prismatic Synthesis: Gradient-based Data Diversification Boosts Generalization in LLM Reasoning* (2025). [arXiv:2505.20161](https://arxiv.org/abs/2505.20161)
- **[L34]** *Say Anything but This: When Tokenizer Betrays Reasoning in LLMs* (2026). [arXiv:2601.14658](https://arxiv.org/abs/2601.14658)
- **[L35]** *Decoupling the Benefits of Subword Tokenization for Language Model Training via Byte-level Simulation* (2026). [arXiv:2604.27263](https://arxiv.org/abs/2604.27263)
- **[L36]** *Byte Latent Transformer: Patches Scale Better Than Tokens* (2024). [arXiv:2412.09871](https://arxiv.org/abs/2412.09871)
- **[L37]** *Lost in Tokenization: Fundamental Trade-offs in Graph Tokenization for Transformers* (2026). [arXiv:2605.22471](https://arxiv.org/abs/2605.22471)
- **[L38]** *Randomized Positional Encodings Boost Length Generalization of Transformers* (2023). [arXiv:2305.16843](https://arxiv.org/abs/2305.16843)
- **[L39]** *Language Models Are Not Equally Robust to Non-Canonical Tokenization across Languages* (2026). [arXiv:2607.26831](https://arxiv.org/abs/2607.26831)
- **[L40]** *Training Language Models with Homotokens Leads to Delayed Overfitting* (2026). [arXiv:2601.02867](https://arxiv.org/abs/2601.02867)
- **[L41]** *TokEval: A Tokenizer Evaluation Suite* (2026). [arXiv:2608.18062](https://arxiv.org/abs/2608.18062)
- **[L42]** *Single Teacher, Multiple Perspectives: Teacher Knowledge Augmentation for Enhanced Knowledge Distillation* (ICLR 2025). [OpenReview](https://openreview.net/forum?id=DmEHmZ89iB)
- **[L43]** *Multi-Teacher Ensemble Distillation: A Mathematical Framework for Probability-Domain Knowledge Aggregation* (2026). [arXiv:2601.09165](https://arxiv.org/abs/2601.09165)
- **[L44]** *Adaptive Group Robust Ensemble Knowledge Distillation* (2024). [arXiv:2411.14984](https://arxiv.org/abs/2411.14984)
- **[L45]** *LLMs Can Implicitly Learn from Mistakes In-Context* (2025). [arXiv:2502.08550](https://arxiv.org/abs/2502.08550)
- **[L46]** *LC-ICL: Label-Guided Contrastive In-Context Learning for Robust Information Extraction* (2026). [arXiv:2606.29407](https://arxiv.org/abs/2606.29407)
- **[L47]** *Failures Are the Stepping Stones to Success: Enhancing Few-Shot In-Context Learning by Leveraging Negative Samples* (2025). [arXiv:2507.23211](https://arxiv.org/abs/2507.23211)
- **[L48]** *KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization* (2024). [arXiv:2401.18079](https://arxiv.org/abs/2401.18079)
- **[L49]** *When Attention Sink Emerges in Language Models: An Empirical View* (2024). [arXiv:2410.10781](https://arxiv.org/abs/2410.10781)
- **[L50]** *Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks* (2026). [arXiv:2603.11487](https://arxiv.org/abs/2603.11487)
- **[L51]** *Softpick: No Attention Sink, No Massive Activations with Rectified Softmax* (2025). [arXiv:2504.20966](https://arxiv.org/abs/2504.20966)
- **[L52]** *The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks* (2026). [arXiv:2603.05498](https://arxiv.org/abs/2603.05498)
- **[L53]** *KVSink: Understanding and Enhancing the Preservation of Attention Sinks in KV Cache Quantization for LLMs* (2025). [arXiv:2508.04257](https://arxiv.org/abs/2508.04257)

---

**Terminal token:** `NO_GO_NEED_NEW_SEED`
