# ALGORITHMIC PROMPTING NOVELTY AUDIT

**Repository:** [`ScottBlizzard/idle_2`](https://github.com/ScottBlizzard/idle_2)
**Branch:** `main`
**Pinned reference:** [`239d56cbffb14054c70b96fc8cdf689181f6f32f`](https://github.com/ScottBlizzard/idle_2/tree/239d56cbffb14054c70b96fc8cdf689181f6f32f)
**Audit date:** 2026-08-27
**Audit stance:** falsification first; archive documents were treated as provenance, not as current evidence.

The ten required repository files were read in full before recommendations were formed. The audit also inspected the evaluator and launch path where necessary to diagnose parsing, decoding, and benchmark-construction risks. Literature searches covered chain-of-thought harm, overthinking, test-time scaling, algorithmic and programmatic prompting, instruction interference, negation, prompt sensitivity, inverse scaling, strategic/minimax reasoning, procedural overconstraint, automation analogies, and model-relative prompt transfer. Primary papers, official proceedings pages, official model cards, and official code repositories are linked directly.

---

## 1. Executive verdict

# **PIVOT — interesting phenomenon but the current claim is wrong**

The fixed experiment establishes a **real descriptive ranking difference** for the exact benchmark, prompts, parser, and Qwen checkpoints that were run. In particular, Qwen3.5-9B performs substantially worse under the repository's generic Bellman prompt than under compact CoT, whereas Qwen3-8B shows the opposite ordering. That observation is worth preserving.

It does **not** yet establish that “algorithmic prompting,” “correct procedural scaffolding,” or “more explicit reasoning” caused the difference. The prompts jointly change operator inventory, wording, verbosity, line structure, output-format compatibility, and negative wording. The trace analysis is correlational. The benchmark generator also creates a shortcut in which controller identity is perfectly aligned with optimal action type and, because action order is fixed, with optimal action position. Several reported cells rely heavily on fallback parsing rather than the requested final-answer field.

More importantly, the broad scientific story is already heavily occupied:

- [Qi et al. (2026), *On the Paradoxical Interference between Instruction-Following and Task Solving*](https://arxiv.org/abs/2601.22047) shows that adding self-evident constraints—including method and structure constraints derived from a model's own successful answer—can reduce task success across mathematics, multi-hop QA, and code, with controls for instruction length and arrangement.
- [Khan (2025/2026), *You Don't Need Prompt Engineering Anymore: The Prompting Inversion*](https://arxiv.org/abs/2510.22251) directly compares ordinary CoT with a more constrained rule-based CoT and reports a model-generation reversal: the constrained prompt helps GPT-4o but hurts GPT-5, accompanied by overconstraint and hyper-literalism errors.
- [Darshan and Divekar (2026), *When Gradients Collide*](https://arxiv.org/abs/2605.26046) shows that individually optimized instructions can become harmful when combined in one prompt, explicitly identifying inference-time instruction interference.
- Multiple earlier lines already show CoT harm, self-correction harm, overthinking degradation, negation-specific inverse scaling, and prompt-dependent model-rank reversals.

Therefore the publishable target cannot be “detailed prompts sometimes hurt,” “reasoning can hurt,” “better models need simpler prompts,” or “prompt effects differ by model.” Those are collision claims.

A narrow residual question remains open enough to justify **one tightly gated smoke test**:

> Does adding a conditionally irrelevant competing control operator, while holding procedural detail, token budget, polarity, output schema, arithmetic, and task instance fixed, causally induce oracle-verifiable wrong-operator execution—and can the sign of that interference replicate across genuinely independent model families?

That is a different claim from ordinary prompt sensitivity only if all three parts survive: **factor isolation, executable process diagnosis, and independent-family replication**. The current repository has none of those three at publication strength.

### Decision summary

| Question | Audit answer |
|---|---|
| Is the original controller-insensitive-failure hypothesis alive? | No. It was correctly killed by the preregistered compact-CoT threshold. |
| Is the 9B Bellman-versus-CoT difference merely fabricated? | No. It is a valid descriptive result for the frozen run. |
| Does the result identify “algorithmicity” as the cause? | No. The causal treatment is undefined and heavily aliased. |
| Is cross-model prompt-effect reversal novel by itself? | No. Closely related reversals and model-relative prompt effects are already documented. |
| Is wrong MAX/MIN execution potentially useful? | Yes, as a mechanism hypothesis, not yet as causal evidence. |
| Should a large sweep begin now? | No. Only the one-day, factor-controlled gate in Section 5 is justified. |

---

## 2. Claim decomposition

The current evidence becomes much clearer when split into claims of increasing strength. Only the first two descriptive claims survive without qualification.

### C0. The original controller-insensitive-failure claim

**Claim:** models fail to update the root action when only the post-chance controller flips.

**Status:** rejected by the repository's own binding gate. Compact CoT reaches 90.6% pair accuracy on Qwen3.5-4B and 97.2% on Qwen3.5-9B. The reset logic was appropriate: a broad capability-deficit story cannot survive when the same checkpoints solve the paired task under a compact prompt.

**Consequence:** none of the earlier Seeds A/B/C or broad “models ignore control structure” narratives should be revived under new terminology. The binding negative conclusions in [`AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/docs/audits/AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md) remain in force.

### C1. A fixed-condition descriptive ranking on Qwen3.5-9B

**Claim:** on the frozen 180-pair benchmark and current implementation, generic Bellman prompting performs worse than compact CoT on Qwen3.5-9B.

**Status:** supported descriptively.

- Compact CoT pair accuracy: 97.2%.
- Generic Bellman pair accuracy: 78.9%.
- Paired difference: -18.3 percentage points.
- Reported bootstrap 95% confidence interval: [-24.4, -12.2].
- Discordant-pair direction: 36 CoT-only successes versus 3 Bellman-only successes.

The effect is too large to dismiss as a one- or two-item fluctuation. However, the estimand is **“this exact Bellman string plus its format and parser versus this exact compact-CoT string plus its format and parser.”** It is not yet “algorithmic detail.”

### C2. A model-dependent sign change within the tested Qwen set

**Claim:** the Bellman-minus-CoT contrast changes sign across tested checkpoints.

**Status:** descriptively supported but scientifically underidentified.

- Qwen3.5-9B: Bellman is 18.3 points worse.
- Qwen3-8B: Bellman is 12.8 points better.
- Qwen3.5-4B: difference is approximately -1.1 points and compatible with zero.
- Qwen2.5-Math-7B: difference is approximately -6.1 points and compatible with zero.

This is not yet a clean scale effect. Checkpoint family, architecture, tokenizer, chat template, post-training data, reasoning style, and parameter count all vary together. Qwen3-8B versus Qwen3.5-9B is not a controlled scaling pair. The defensible wording is **checkpoint-dependent sign heterogeneity within related Qwen lineages**, not “inverse scaling” and not “larger models are harmed.”

### C3. Correct algorithmic scaffolding is the harmful treatment

**Claim:** a correct Bellman scaffold itself makes the 9B model worse than a less explicit reasoning prompt.

**Status:** not identified.

Both the compact-CoT and Bellman prompts are algorithmic. They differ in at least the following dimensions:

1. whether both MAX and MIN are introduced;
2. whether only the applicable operator is foregrounded;
3. whether a named Bellman-style procedure is described;
4. instruction length and tokenization;
5. sentence and line structure;
6. conditional-rule density;
7. output-format pressure;
8. lexical choice and operator labels;
9. the amount of irrelevant-but-correct information;
10. in the local-operator condition, explicit negative wording.

A treatment called “algorithmicity” has no operational definition in the current matrix. The compact prompt may simply be a better-matched algorithmic prompt.

### C4. Competing-operator interference is the mechanism

**Claim:** mentioning both applicable and inapplicable operators causes the model to execute the wrong one.

**Status:** suggestive, not causal.

The operator audit reports that 11.1% of Qwen3.5-9B Bellman generations contain an explicit unexpected MAX/MIN call; accuracy is 45.0% on those generations versus 95.0% on “clean” generations, and 57.9% of Bellman errors contain an unexpected call. This is a useful localization signal.

But the analysis does not establish mediation or causality:

- The regex detects only a narrow set of forms such as `min(`, `minimum(`, `max(`, and `maximum(`; prose paraphrases and implicit selection are missed.
- A wrong operator in a generated trace can be a **downstream symptom** of an earlier controller misread rather than the cause of the final error.
- Trace text is a post-treatment variable and may not faithfully reveal the latent computation used for the final token.
- The “positive operator only” comparison changes several prompt factors and has extreme fallback-parser dependence, so it is not a clean removal intervention.
- There is no intervention that inserts, removes, or corrects the operator step while preserving the rest of the generated computation.

The proper claim is: **wrong-operator text is associated with errors in one model/prompt cell.**

### C5. The effect is general across independent model families

**Claim:** non-monotonic algorithmic-prompt effects generalize beyond Qwen.

**Status:** unsupported. All four tested checkpoints are Qwen-lineage models. Model-family independence is currently zero.

A paper cannot use four Qwen checkpoints as four independent replications. At best they are four related implementation contexts.

### C6. The effect is relevant outside a synthetic arithmetic shell

**Claim:** the mechanism matters in real planning, games, tool use, or agentic decision making.

**Status:** unsupported.

The six “semantic domains” are surface skins over the same compact arithmetic tree. They are useful for detecting lexical brittleness but are not six independent task domains. No public benchmark, natural interaction loop, or real tool environment has yet reproduced the effect.

### C7. The current benchmark isolates one control variable without shortcuts

**Claim:** because only controller identity changes within a pair, success requires genuine MAX/MIN control reasoning.

**Status:** only partially true.

The paired construction does isolate controller text within each pair, but the generator creates a global shortcut:

- self-control always makes the branching action optimal;
- opponent-control always makes the safe action optimal;
- the safe root action is always listed first;
- the branching root action is always listed second.

Thus a model can map controller wording directly to action type or action position without carrying out the chance backup. This does not explain why one prompt hurts more than another by itself, but it makes pair accuracy an invalid stand-alone measure of operator execution and weakens any mechanistic claim.

### What survives after decomposition

The surviving empirical kernel is narrow:

> On one synthetic paired benchmark, one Qwen checkpoint shows a large negative Bellman-versus-compact-CoT prompt contrast, another related checkpoint shows a positive contrast, and explicit wrong-operator text is enriched among errors in the harmed checkpoint.

Everything beyond that sentence requires new evidence.

---

## 3. Nearest-work collision table

### Ingredient definitions

The requested contribution ingredients are abbreviated as follows:

- **I1:** a correct algorithmic scaffold makes a model worse than a less explicit reasoning prompt;
- **I2:** the direction of the effect reverses across model families or scales;
- **I3:** paired counterfactual tasks isolate one control variable;
- **I4:** generated traces expose incorrect operator execution;
- **I5:** a causal prompt-factor ablation separates operator competition from general proceduralization.

“**All**” means the paper directly tests essentially that ingredient. “**Some**” means it contains a materially adjacent result but not the exact ingredient. “**None**” means it does not supply the ingredient. The table deliberately uses conservative classifications: thematic similarity is not counted as completion.

| Primary work | What it already establishes | I1 | I2 | I3 | I4 | I5 | Collision judgment |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| [Qi et al., 2026, *On the Paradoxical Interference between Instruction-Following and Task Solving*](https://arxiv.org/abs/2601.22047) | Adds self-evident constraints extracted from each model's own successful output; task success falls across math, multi-hop QA, and code. Includes method/structure constraints, length-matched paraphrase controls, instruction-order variants, constraint-count/type analyses, and attention/error analyses across many families and scales. | Some | Some | None | Some | Some | **Closest collision with the broad claim.** It already makes “correct explicit constraints can damage task solving” non-novel. It does not isolate competing operators or paired control flips. |
| [Khan, 2025/2026, *You Don't Need Prompt Engineering Anymore: The Prompting Inversion*](https://arxiv.org/abs/2510.22251) | Compares standard CoT with a more constrained rule-based “Sculpting” CoT on GSM8K. Sculpting helps GPT-4o but hurts GPT-5; qualitative traces attribute failures to hyper-literalism, rejected inference, and overconstraint. | **All** | **All** within one model lineage/generation sequence | None | Some | None | **Direct collision with “non-monotonic procedural prompting” and model-relative transfer.** Methodological limitations do not erase the priority claim. |
| [Darshan & Divekar, 2026, *When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges*](https://arxiv.org/abs/2605.26046) | Separates optimization-time gradient dilution from inference-time instruction interference. Individually optimized rubric instructions become worse than a generic prompt when combined; decomposition and process diagnostics localize the failure. | Some | Some | None | Some | Some | Strong collision with “individually correct instructions can compete when jointly presented.” It is not operator-specific and does not show sign reversal of the same prompt treatment. |
| [Liu et al., ICML 2025, *Mind Your Step (by Step)*](https://arxiv.org/abs/2410.21333) | Shows systematic CoT harm on implicit statistical learning, visual recognition, and exception-containing pattern tasks, with heterogeneous effects across tasks and models. | Some | Some | None | None | None | Kills any generic “CoT can hurt” novelty claim. The task theory differs from control-operator interference. |
| [Li et al., NeurIPS 2025, *When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs*](https://arxiv.org/abs/2505.11423) | Across 15 models and instruction-following benchmarks, explicit CoT often reduces constraint compliance; error and attention analyses show reasoning can divert focus from simple requirements. | Some | Some | None | Some | None | Collides with “extra reasoning harms instruction execution” and with attention-based explanations, but not with paired operator control. |
| [Jin et al., 2025, *Reasoning Can Hurt the Inductive Abilities of Large Language Models*](https://arxiv.org/abs/2505.24225) | Controlled hidden-rule games show CoT/reasoning models can underperform non-reasoning counterparts; the paper diagnoses several failure modes and tests targeted interventions. | Some | Some | Some | Some | Some | A close methodological neighbor for controlled reasoning harm, but it does not isolate one controller variable or competing backup operators. |
| [Ghosal et al., NeurIPS 2025, *Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models*](https://arxiv.org/abs/2506.04210) | Sequentially extending reasoning initially helps and then degrades performance; parallel reasoning performs better under matched inference budget. | None | Some | None | Some | None | Collides with non-monotonic test-time compute, not with correct procedural content. It prevents framing the result merely as “more thinking is worse.” |
| [Huang et al., ICLR 2024, *Large Language Models Cannot Self-Correct Reasoning Yet*](https://openreview.net/forum?id=IkmD3fKBPQ) | Intrinsic self-correction without external feedback can lower reasoning accuracy; extra corrective scaffolding is not monotonically useful. | Some | Some | None | Some | None | Collides with “a nominally helpful reasoning procedure can make answers worse.” No operator-factor isolation. |
| [Costarelli et al., 2024, *Evaluating Strategic Reasoning Abilities of LLM Agents* / GameBench](https://arxiv.org/abs/2406.06613) | Evaluates base, CoT, and Reasoning-via-Planning agents across nine games. Scaffolding rankings vary by model/game; aggregate benefits do not imply universal per-game benefit. [Code](https://github.com/Joshuaclymer/GameBench). | Some | Some | None | None | None | Collides with universal planning-scaffold benefit and is the best next public environment. It does not provide the desired causal operator experiment. |
| [Jia et al., NeurIPS 2025, *Large Language Model Strategic Reasoning Evaluation through Behavioral Game Theory*](https://arxiv.org/abs/2502.20432) | Across 22 models and behavioral games, CoT is not universally effective and model scale alone does not determine strategic reasoning. | Some | Some | None | None | None | Collides with broad model-size and strategy-prompt claims; not a process-mechanism study. |
| [Jang et al., 2023, *Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts*](https://proceedings.mlr.press/v203/jang23a.html) | Negated prompts show inverse scaling across OPT and GPT-3 sizes, with larger models often more impaired by negation. | None | **All** for a negation treatment | Some | None | None | Makes negative wording and scale-dependent polarity effects a known confound, not a novelty source. |
| [Truong et al., 2023, *An Analysis of Language Models on Negation Benchmarks*](https://aclanthology.org/2023.starsem-1.10/) | Documents weak lexical and inferential handling of negation across language-model benchmarks. | None | Some | None | None | None | Reinforces that “never apply MIN” can create an independent negation problem. |
| [Sclar et al., ICLR 2024, *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design*](https://arxiv.org/abs/2310.11324) | Meaning-preserving formatting variations can move accuracy by up to 76 points, and preferred formats correlate weakly across models. | None | Some | None | None | None | **Critical null explanation.** A single prompt-pair ranking is ordinary prompt sensitivity until semantic factors are orthogonally manipulated. |
| [Mizrahi et al., TACL 2024, *State of What Art? A Call for Multi-Prompt LLM Evaluation*](https://aclanthology.org/2024.tacl-1.52/) | Model rankings and conclusions vary across prompt formulations; recommends multi-prompt evaluation rather than a single arbitrary prompt. | None | Some | None | None | None | Makes one-wording-per-condition evidence unacceptable for a strong model-comparison claim. |
| [Wei et al., 2023, *Inverse Scaling Can Become U-Shaped*](https://arxiv.org/abs/2211.02011) | Some inverse-scaling trends reverse again at larger scale, and elicitation methods can alter the curve. | None | **All** for scale-dependent direction changes on other tasks | None | None | None | Prevents treating a sign change across sizes as novel without a new mechanism and controlled family design. |
| [Coleman et al., 2023, *In-context Interference in Chat-based Large Language Models*](https://arxiv.org/abs/2309.12727) | Demonstrates interference between information accumulated in conversational context, reducing retention/performance. | None | Some | None | None | None | Terminological neighbor only. It concerns contextual-memory interference, not competing procedures. |
| [Chen et al., 2026, *Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning*](https://arxiv.org/abs/2605.06840) | Extracts search trees from four-in-a-row traces, fits computational planning models, and causally prunes trace segments; deep trace content often does not drive final moves. | None | Some | None | Some | Some | Raises the evidentiary bar for trace claims: readable reasoning text is not enough; interventions must show that the step drives behavior. |
| [Lin et al., ACL 2025, *Transparent Assessment of LLM Reasoning in Games* / GAMEBoT](https://aclanthology.org/2025.acl-long.378/) | Decomposes game reasoning into verifiable intermediate subproblems and evaluates structured CoT across eight games. [Project](https://visual-ai.github.io/gamebot/). | None | Some | None | Some | None | Adjacent process-evaluation work. It reduces novelty of “evaluate intermediate game reasoning,” but not operator competition. |

### Positive algorithmic-prompting literature is also relevant

Two foundational lines establish the default expectation that explicit procedures should help:

- [Zhou et al., ICLR 2023, *Teaching Algorithmic Reasoning via In-Context Learning*](https://arxiv.org/abs/2211.09066) reports large gains from algorithmic prompting on arithmetic and symbolic procedures.
- [Chen et al., TMLR 2023, *Program of Thoughts Prompting*](https://arxiv.org/abs/2211.12588) improves numerical reasoning by externalizing computation into executable programs.

These papers do not collide with the harm result. They matter because a strong contribution would need to explain **when the usual positive effect reverses**, not merely show one negative cell.

### Human-factors analogies do not supply an LLM mechanism

- [Wegner (1994), *Ironic Processes of Mental Control*](https://pubmed.ncbi.nlm.nih.gov/8121959/) concerns counterintentional effects of human thought suppression.
- [Parasuraman and Riley (1997), *Humans and Automation: Use, Misuse, Disuse, Abuse*](https://journals.sagepub.com/doi/10.1518/001872097778543886) and [Skitka, Mosier, and Burdick (1999), *Does Automation Bias Decision-Making?*](https://doi.org/10.1006/ijhc.1999.0252) concern human overreliance on automated aids.

They may motivate labels such as “ironic operator activation” or “scaffold-induced automation bias,” but importing those labels would not be evidence. A transformer is not a human monitoring process, and the model is not deferring to an external automated recommendation. These literatures should appear, if at all, as analogies after an LLM-specific causal mechanism is demonstrated.

### Collision conclusion

No located work contains **all five** requested ingredients in one design. That leaves a narrow conjunction gap. But three important qualifications follow:

1. **I1 alone is already known.** Correct or self-evident procedural constraints can hurt.
2. **I2 alone is already known.** Prompt effects and constrained-versus-simple rankings can reverse across models or scales.
3. **The potentially new material is the conjunction of I3–I5 with independent-family replication:** a genuinely paired control-variable task, an oracle-verifiable wrong-operator process failure, and a causal factorial that separates operator competition from generic procedural load.

Ordinary prompt sensitivity is not the novelty gap. The materially different claim would be a **specific, intervention-supported failure mode of conditional operator selection**.

---
## 4. Confound and diagnosticity audit

### 4.1 What the current implementation does and does not already control

Several possible objections are weaker than they first appear:

- **The 9B compact-CoT versus Bellman contrast uses the same model, same paired items, same chat-template code path, greedy decoding, and the same scaffold token ceiling.** Arithmetic-instance difficulty and stochastic sampling therefore cannot directly create the 18.3-point within-model contrast.
- The launch path does not enable the optional thinking mode, so the two 9B prompt cells were not intentionally run under different thinking settings.
- The main 9B CoT and Bellman cells have high explicit `FINAL` parsing rates, so the main 18.3-point contrast is not obviously a fallback-parser hallucination.

Those controls do **not** rescue the mechanism. Other cells used to argue for operator competition are much less secure. In [`summary.csv`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/results/v2/analysis/summary.csv), for example:

- Qwen3.5-9B positive-operator output is parsed through fallback on about 98.6% of items;
- Qwen3.5-9B local-operator output uses fallback on about 81.7%;
- Qwen3-8B compact CoT uses fallback on about 72.5%;
- Qwen2.5-Math-7B compact CoT uses fallback on about 96.9%.

Consequently, the main 9B ranking can be treated as a descriptive fact, but the current positive/local ablations and much of the cross-checkpoint pattern cannot be treated as clean causal evidence.

### 4.2 Confound-by-confound destruction tests

| Plausible simpler explanation | Can it explain the present evidence? | Minimal controlled experiment that resolves it | Failure criterion |
|---|---|---|---|
| **Unequal prompt length or verbosity** | Yes. The prompts differ in token count, number of clauses, line layout, conditional density, and output instructions. Length alone is not the only issue; procedural load is bundled with semantic content. | Use a preregistered 2×2 design: compact vs procedural crossed with single applicable operator vs dual competing operators. Match within each tokenizer to the same line count and within two input tokens using neutral, non-operator padding. Repeat the primary dual-versus-single contrast with a second independently written padding set. | The negative effect disappears, changes sign, or is comparable to the filler-to-filler variation. |
| **Chat-template or thinking-mode differences** | Within the frozen 9B comparison, probably not the main cause; across families, absolutely plausible. Native templates can change role tokens, BOS/EOS handling, and reasoning activation. | Pin `transformers`, tokenizer revision, model revision, and chat-template text. Explicitly disable any native thinking mode. Save the fully rendered prompt and token IDs for every generation. Put all experimental content in one user turn unless the official card requires a system role. Run a 12-pair template audit comparing the native template with a plain single-turn formulation before interpreting family differences. | A family effect appears only under one template or thinking flag. |
| **Output truncation** | Not ruled out. The runner stores generated-token counts but does not elevate `finish_reason`, EOS status, or truncation to a primary diagnostic. Different prompts can consume different output budgets. | Give every condition the same 192-token cap, record EOS/finish status, input tokens, output tokens, and whether the JSON grammar closed. Repeat every truncated item at 384 tokens as a diagnostic only. | More than 0.5% truncation overall, more than a 1-point truncation-rate difference between primary cells, or recovery of the treatment effect when the cap is raised. |
| **Fallback parsing or output-format compatibility** | Yes for positive/local ablations and several non-9B cells; less likely for the main 9B CoT-Bellman contrast. A parser that scans the last action mention can turn reasoning verbosity into apparent accuracy. | Primary evaluation must use a strict grammar-constrained schema with no fallback. Invalid schema counts as wrong. Report task accuracy, schema validity, and semantic accuracy after manual review separately. Run an unconstrained-format audit on a small fixed subset to ensure the grammar itself does not reverse the prompt contrast. | The effect is absent among strictly valid outputs, or is explained by differential validity/fallback rates. |
| **Prompt wording rather than algorithmicity** | Yes. One wording per condition cannot distinguish a semantic factor from a phrase preference. | Prewrite two semantically equivalent prompt packs by independent authors. Hash both before inference. Run all primary cells with Pack A and replicate the key single-versus-dual procedural contrast with Pack B. Also replace `MAX/MIN` with opaque locally defined operator labels. | The effect fails to keep its sign or at least 70% of its magnitude under the independent wording and neutral labels. |
| **Qwen-specific formatting or post-training behavior** | Yes. The current four checkpoints are one broad lineage. | Run six non-Qwen instruction-tuned families, one checkpoint per independent organization/architecture line, with official native templates and no quantization. Keep Qwen3.5-9B only as a positive-control reproduction, not as an independent replication. | Fewer than two non-Qwen families show the preregistered negative effect, or all non-Qwen effects are near zero. |
| **Arithmetic difficulty differences** | It cannot explain the within-item prompt contrast because every prompt sees the same numbers. It can explain why “unexpected-operator” generations have lower accuracy: harder items may both trigger wrong traces and cause wrong answers. | Recompute every intermediate quantity with an oracle. Analyze wrong-operator incidence within the same item across prompt cells. Add a lookup variant in which the post-chance candidate values are supplied, eliminating arithmetic while retaining operator selection. | Wrong-operator enrichment disappears in the lookup condition or after item fixed effects. |
| **Contamination from mentioning both MAX and MIN** | This is not merely a nuisance; it is the most plausible surviving mechanism. The current positive-only comparison is not cleanly matched. | In the 2×2 matrix, compare procedural-dual against procedural-single while holding structure and token count fixed; estimate the operator-inventory main effect and its interaction with proceduralization. Use opaque labels whose max/min meanings are randomized across pairs. | No negative dual-operator effect, no interaction, or no increase in oracle-verified wrong-operator execution. |
| **Negative-instruction effects from “never apply” or “do not use”** | Yes for the local-operator condition. Negation is known to create scale-dependent failures. It does not directly explain a generic Bellman prompt that only states conditional rules, but it can falsely make a local ablation look mechanistic. | Add a polarity cell that is identical to the single-operator procedural prompt except for an explicit prohibition of the other operator. Match it to an affirmative sentence of equal length. Treat this contrast as secondary and separate from the dual-operator contrast. | Harm appears only in the negative-prohibition cell; classify the phenomenon as negation sensitivity rather than operator competition. |
| **Benchmark-generation shortcut** | Yes, and it is serious. In the current generator, controller identity predicts optimal action type, and fixed action order predicts optimal action position. A model can pass without executing the tree. | Replace “safe versus branching” with two root actions having identical tree structure. Generate values until one action wins under operator X and the other under operator Y. Randomize action labels, action order, controller labels, and the mapping from opaque operator names to max/min independently for every pair. | Accuracy remains high under controller-to-position probes, or a classifier using only controller text and action metadata predicts the answer above chance. |
| **A pair changes more than one semantic fact** | The current pair text is intended to change only controller identity, but lexical formulations such as “maximizes” and “minimizes” also directly reveal the answer rule. | Use locally defined opaque roles. Present the operator definitions once and change only the controller token between paired items. Verify byte-level diff of each pair and publish it. | Any pair differs outside the controller token span, excluding unavoidable checksums/IDs. |
| **Deterministic-decoding instability** | Greedy decoding removes sampling variance but GPU kernels, batching, precision, and near-tied logits can still change tokens. It is very unlikely to produce a stable 18-point gap alone, but exact reproducibility is cheap to test. | Re-run a stratified 10% of outputs with shuffled batch order and on a second GPU using identical software. Hash generated token IDs. If hashes differ, force batch size 1 and deterministic kernels, then rerun the primary cells. A low-temperature multi-seed study is secondary, not a substitute for exact greedy reproducibility. | More than 0.5% token-level disagreement under exact greedy replication or any treatment-sign change. |
| **Multiple comparisons** | Yes for inferential interpretation. The surviving Bellman effect was investigated after the original seed failed, and many prompt/model comparisons are available. A nominal bootstrap interval does not correct post-selection. | Freeze a new analysis plan with at most three confirmatory contrasts: dual-vs-single under procedural prompting, the 2×2 interaction, and negative-prohibition vs affirmative control. Apply Holm correction within each model; treat domains, difficulty, and all other comparisons as exploratory. | The primary contrast does not survive the preregistered hierarchy or relies on an unregistered subgroup. |
| **Selective reporting or survivor bias** | Plausible. The repository reports the matrix, which is good, but the scientific narrative focuses on the most dramatic checkpoint after a prior hypothesis was killed. | Commit the benchmark hash, prompt hashes, model revisions, parser, exclusions, and GO rule before running. Publish every model×prompt cell, all invalid outputs, all repeated runs, and the frozen analysis script regardless of outcome. | Any model, prompt, or item is removed after outcomes are seen without a preregistered mechanical rule. |
| **Model capability floor or ceiling** | Yes. Low baselines can make a harmful effect invisible; saturated baselines can make a helpful effect impossible. Cross-model sign differences can therefore be mathematical rather than mechanistic. | Use three prespecified difficulty strata and report effects within each. Count a family toward the replication gate only if its single-operator procedural baseline has at least 65% pair accuracy and at least three errors, while still reporting every family. | The sign reversal exists only because one cell is at floor or ceiling, or disappears in the overlapping-capability stratum. |
| **The operator trace is unfaithful or merely post-hoc** | Yes. A written wrong operator may rationalize an already chosen answer. | Use a two-stage trace intervention. Stage 1 emits a strict intermediate operator/value table. Stage 2 consumes that frozen table and chooses the root action. For every wrong Stage-1 table, create a twin in which only the operator and oracle-selected values are corrected, then rerun Stage 2. | Correcting the intermediate does not rescue the final action, or the final action ignores both correct and wrong injected tables. |
| **The six semantic domains are independent replications** | No. They are lexical skins around the same mathematical template. Treating them as six domains would inflate generality. | Call them “skins,” not domains. Generate distinct numerical trees, cluster uncertainty by paired tree, and reserve claims of domain transfer for a public benchmark. | The result is driven by one skin or vanishes after stripping domain prose. |
| **Prompt-name priming, especially “Bellman”** | Plausible. A named algorithm may activate learned text patterns that are not the intended computation. | Remove all algorithm names from confirmatory prompts. Compare opaque operator labels with literal `MAX/MIN` only as a secondary lexical generalization test. | Harm appears only when “Bellman,” `MAX`, or `MIN` is literally named. |
| **Action-order and label-token effects** | Yes in the existing generator. Some labels are easier to copy and the first/last option can be favored. | Randomize root-action order and label assignment per pair; use equal-length labels; ensure each label is optimal equally often under each controller across the test set. Include action position as a prespecified covariate. | A position-only or label-only baseline exceeds 55%, or the prompt effect is confined to one action position. |
| **Arithmetic margin or tie sensitivity** | Yes. Near ties can amplify tiny calculation differences and floating-point formatting. | Define low/medium/high margin strata in exact rational arithmetic; prohibit ties; print probabilities and values in a canonical format; evaluate with exact fractions internally. | The effect exists only in near-tie items or disappears when margins are widened. |
| **Checkpoint size is mistaken for causal scale** | Yes. Current checkpoints differ in far more than parameter count. | Do not make a scale claim in the smoke test. A later scale study must use at least three checkpoints from the same training lineage with matched post-training recipe, if such checkpoints exist. | Any manuscript attributes the Qwen3-vs-Qwen3.5 difference to size without a controlled lineage. |

### 4.3 Diagnosticity ranking

The current observation is not equally vulnerable to every objection. The highest-priority threats are:

1. **undefined treatment:** “algorithmic prompting” is not isolated;
2. **single-lineage evidence:** no independent-family replication;
3. **benchmark shortcut:** controller maps to action type/position;
4. **parser-dependent ablations:** positive/local controls are not clean;
5. **post-treatment trace inference:** wrong-operator text is associative;
6. **nearest-work collision:** general constrained-prompt harm and prompt-effect reversal are already documented.

Length, truncation, and greedy nondeterminism matter, but they are secondary. Fixing those alone would not produce an ICLR contribution.

### 4.4 What would falsify the operator-competition story immediately

The operator-competition story should be abandoned—not repaired by renaming—if any of the following occurs in the one-day gate:

- the dual-operator penalty disappears after token/structure matching;
- the effect is present only with literal `MAX/MIN` or negative wording;
- strict parsing removes the effect;
- non-Qwen families do not reproduce it;
- wrong-operator incidence does not rise under the dual prompt;
- correcting the structured intermediate does not rescue the final decision;
- symmetric action trees eliminate the effect;
- the result does not replicate under the second prompt wording.

---

## 5. Minimal one-day smoke-test protocol

### 5.1 What this gate is allowed to decide

The smoke test has one job: decide whether the residual **competing-operator interference** hypothesis merits a public-benchmark study. It is not a miniature paper, a leaderboard sweep, or a search for a flattering model. It must answer four questions simultaneously:

1. Does a dual-rule scaffold hurt relative to a single-applicable-rule scaffold after length, structure, output format, arithmetic, and wording are controlled?
2. Does that treatment specifically increase oracle-verifiable execution of the inactive operator?
3. Does the sign of the treatment vary across genuinely independent model families rather than only across Qwen checkpoints?
4. Does a minimal intervention on the intermediate operator state change the final decision?

A failure on any of the first three blocks the current project. A failure on the fourth blocks the mechanistic claim even if a descriptive prompt contrast survives.

### 5.2 Pair budget: 60 pairs total, 54 confirmatory

Use **no more than 60 paired examples**:

- **6 engineering pairs**, visible during implementation and excluded permanently from inference;
- **54 sealed confirmatory pairs**, never inspected through model outputs before prompt, parser, thresholds, and analysis code are committed.

The 54 confirmatory pairs should form a balanced `6 × 3 × 3` design:

- six lexical skins;
- three arithmetic/margin levels;
- three independently sampled tree instances per skin×level cell.

The six skins remain presentation variants, not six scientific domains. Every confidence interval and test must cluster at the underlying paired-tree ID.

### 5.3 Replace the shortcut-bearing generator

The existing safe-action/branch-action construction must not be reused. Generate two root actions with the **same topology**. For root action \(a\), chance outcome \(j\), and continuation option \(k\), define

\[
Q_o(a)=\sum_j p_{a,j}\,o\!\left(v_{a,j,1},\ldots,v_{a,j,K}\right),
\]

where \(o\) is the active post-chance operator. Every action must have the same number of chance outcomes and continuation options; probabilities, number formatting, text length, and nesting depth must be balanced.

Accept a generated tree only when the optimal root action flips cleanly:

\[
\arg\max_a Q_{\mathrm{large}}(a) \neq
\arg\max_a Q_{\mathrm{small}}(a),
\]

with no ties and a prespecified minimum root-value margin in both controller variants. Half of the pairs should have root action P optimal under `select-larger`, and half should have root action Q optimal; the orientation should reverse under `select-smaller`. Balance any unavoidable odd count within each difficulty stratum as closely as possible.

For every pair, independently randomize:

- root-action order;
- equal-length action labels;
- opaque controller labels;
- opaque operator labels;
- which opaque operator means “select larger” versus “select smaller”;
- lexical skin;
- value and probability formatting within a canonical grammar.

The numerical payload, root-action order, labels, and prose must be identical inside a pair except for one audited **active-controller span**. Store and publish a byte-level diff. A trivial classifier given only the controller label, action labels, action order, and non-numerical metadata must remain at chance; this check should be part of benchmark generation, not an afterthought.

Use exact rational arithmetic internally. Printed decimals may be used only when they round-trip to the exact oracle values. Reject ties, values within the forbidden margin, and cases for which two displayed numbers become equal after formatting.

### 5.4 Minimal prompt-factor matrix

Do not compare another collection of loosely related prompts. Use one preregistered matrix with four primary cells and one diagnostic polarity cell.

| Cell | Procedural detail | Operator inventory | Polarity | Purpose |
|---|---|---|---|---|
| **A. Compact–single** | Low | Only the active rule is stated | Affirmative | Compact algorithmic reference. |
| **B. Compact–dual** | Low | Active and inactive rules are stated conditionally | Affirmative | Tests whether competition appears without a long procedure. |
| **C. Procedural–single** | High | Only the active rule is stated; the inactive-rule slot is replaced by neutral matched text | Affirmative | Clean procedural baseline and primary accuracy anchor. |
| **D. Procedural–dual** | High | Active and inactive rules are both stated conditionally | Affirmative | Primary competing-operator treatment. |
| **E. Procedural–single–prohibition** | High | Active rule plus an explicit prohibition of the inactive rule | Negative | Separates operator competition from negation/ironic-instruction effects. |

The primary estimands are:

\[
\Delta_{\text{dual}\mid\text{procedural}}=\mathrm{Acc}(D)-\mathrm{Acc}(C)
\]

and the factorial interaction

\[
\Delta_{\text{interaction}}=
[\mathrm{Acc}(D)-\mathrm{Acc}(C)]-
[\mathrm{Acc}(B)-\mathrm{Acc}(A)].
\]

The polarity contrast \(\mathrm{Acc}(E)-\mathrm{Acc}(C)\) is secondary. If only E is harmful, the surviving phenomenon is negative-instruction sensitivity, not competing-operator interference.

#### Prompt-matching rules

For each model tokenizer:

- equalize A/B and C/D/E to the same number of rendered lines;
- equalize the compared cells to within two input tokens using a frozen list of semantically inert filler phrases;
- use the same examples, same schema, same answer labels, same maximum output budget, and same user/system role placement;
- remove the word `Bellman` and all other algorithm names from confirmatory prompts;
- use opaque operator names in the primary run; literal `MAX/MIN` is only a secondary lexical-generalization check;
- do not use `never`, `ignore`, `do not`, or equivalent negative forms outside Cell E;
- do not include demonstrations; this gate tests instruction scaffolds, not example selection;
- keep the answer request identical across all cells.

Create two independently written prompt packs. **Pack A** contains all five cells. **Pack B** is committed before inference and replicates only the key C/D contrast. Pack B should preserve the factor definitions but change surface wording, sentence order, and neutral padding. The second pack is not a prompt search: both packs are run and reported regardless of result.

### 5.5 Six independent open-weight model families

Run one checkpoint from each of six independent organizations/lineages. Do not count derivative distillations, two checkpoints sharing a base, or multiple sizes from one family as independent replications.

| Family | Exact checkpoint | Approximate BF16 inference footprint on one 24 GB 4090 | Role in the gate |
|---|---|---:|---|
| Meta Llama | [`meta-llama/Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | ~16 GB weights; ~18–21 GB practical peak at batch 1 and ≤2k context | Large mainstream decoder family; custom community license, so call it open-weight rather than OSI-open. |
| Google Gemma | [`google/gemma-2-9b-it`](https://huggingface.co/google/gemma-2-9b-it) | ~18–19 GB weights; ~21–23.5 GB practical peak | Tightest fit; use batch 1, short context, SDPA, and no retained hidden states. Abort rather than silently quantize if the frozen setup does not fit. |
| Mistral | [`mistralai/Mistral-7B-Instruct-v0.3`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | ~14–15 GB weights; ~17–20 GB practical peak | Independent Mistral lineage and tokenizer/template. |
| Microsoft Phi | [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct) | ~7.5–8 GB weights; ~10–13 GB practical peak | Smaller high-capability family; useful for testing whether the effect is tied to capacity. |
| Ai2 OLMo | [`allenai/OLMo-2-1124-7B-Instruct`](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct) | ~14 GB weights; ~17–20 GB practical peak | Independently trained, unusually transparent family. |
| IBM Granite | [`ibm-granite/granite-3.1-8b-instruct`](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct) | ~16 GB weights; ~19–22 GB practical peak | Independent enterprise instruction-tuned family. |

These are engineering estimates, not guarantees. Peak memory varies with `transformers` version, attention backend, allocator fragmentation, vocabulary/logit buffers, and the exact rendered sequence length. Before the sealed run, load every pinned revision on its assigned GPU and complete the six engineering pairs. The confirmatory configuration must use:

- BF16 weights without quantization;
- one process and one model per GPU;
- no tensor parallelism, CPU offload, or model sharding;
- batch size 1 for Gemma and a fixed batch size no larger than 4 elsewhere;
- context length no greater than 2,048 tokens;
- `eval()` and inference mode;
- the official tokenizer and native chat template, with native “thinking” or hidden-reasoning modes explicitly disabled where supported;
- one frozen `transformers`, CUDA, PyTorch, and attention-backend environment;
- exact model and tokenizer revisions recorded in the manifest.

Qwen3.5-9B may be rerun only as a **positive-control reproduction**. It must not count as a seventh independent family and must not be allowed to satisfy the replication threshold.

### 5.6 Use all eight independent GPUs without pooling memory

The hardware layout should be embarrassingly parallel:

| GPU | Workload |
|---:|---|
| 0 | Llama-3.1-8B-Instruct, all Pack A cells plus Pack B C/D. |
| 1 | Gemma-2-9B-it, same matrix. |
| 2 | Mistral-7B-Instruct-v0.3, same matrix. |
| 3 | Phi-4-mini-instruct, same matrix. |
| 4 | OLMo-2-1124-7B-Instruct, same matrix. |
| 5 | Granite-3.1-8B-instruct, same matrix. |
| 6 | Frozen Qwen3.5-9B positive-control reproduction on the new benchmark and a small preregistered subset of the old benchmark. |
| 7 | Exact-replay audit, shuffled-order audit, unconstrained-output audit, and the two-stage trace intervention; models are loaded sequentially. |

No model spans GPUs. There is no NVLink assumption, distributed inference, pooled KV cache, or shared-memory dependency. The six family jobs can run concurrently; GPU 7 executes diagnostics as soon as a family completes its primary cells.

For seven models including the Qwen positive control, Pack A requires

\[
54\text{ pairs}\times2\text{ controller variants}\times5\text{ cells}\times7
=3{,}780
\]

generations. Pack B C/D adds

\[
54\times2\times2\times7=1{,}512
\]

generations. The total is 5,292 short deterministic generations before the small replay and trace-intervention subsets. With a 192-token ceiling, pre-staged weights, and one model per 4090, this is comfortably a one-day workload; the run should stop rather than expand if engineering problems consume the day.

### 5.7 Parsing, schema, and truncation controls

The current fallback parser must not be used for primary inference. All five prompt cells should produce the same grammar-constrained JSON object, for example:

```json
{
  "active_controller": "ROLE_1",
  "controlled_nodes": [
    {"node": "N1", "operator": "OP_X", "selected_value": "12/5"}
  ],
  "root_action_values": {
    "ACTION_P": "37/10",
    "ACTION_Q": "19/5"
  },
  "final_action": "ACTION_Q"
}
```

The schema should require:

- the controller copied from the task;
- an operator label for every controlled node;
- one selected continuation value per controlled node;
- one root value per action;
- exactly one final action from the allowed label set.

Controls:

1. Use the same grammar and `max_new_tokens=192` in every cell.
2. Record the fully rendered prompt, input token IDs, output token IDs, input/output lengths, EOS status, stop reason, schema validity, and wall-clock time.
3. Count invalid or truncated output as wrong in the primary analysis. Never infer the answer from the last action mention.
4. Report three distinct rates: strict end-to-end accuracy, schema-valid rate, and semantic accuracy among schema-valid outputs.
5. Repeat every truncated output at 384 tokens only as a diagnostic; the repeated result does not replace the primary outcome.
6. Run a small frozen unconstrained-output audit on 12 pairs per family. This checks whether grammar enforcement itself reverses the C/D contrast; it is not a second primary endpoint.
7. Blindly inspect all invalid outputs, all cases in which the reported intermediate values disagree with the oracle, and a 10% random sample of otherwise clean generations.

An oracle should classify each failure into mutually prioritized categories:

1. controller-copy error;
2. inactive-operator execution;
3. correct operator but wrong selected continuation;
4. chance-weighting/arithmetic error;
5. correct action values but wrong root comparison;
6. schema/format failure;
7. unclassifiable.

Publish the deterministic classifier and retain the raw output for every classification. A narrow operator-error regex is not sufficient.

### 5.8 Minimal process intervention

Trace inspection alone cannot support causality. Use a two-stage intervention on the procedural-dual condition D for a preregistered subset consisting of:

- every D item with an oracle-verified wrong operator;
- a size-matched random sample of D items with a correct operator;
- the corresponding C items for the same pair IDs.

**Stage 1** emits only the structured controller/operator/value table. **Stage 2** receives the original task plus the frozen Stage-1 table and selects the root action; it is forbidden to recompute controlled-node values.

For each wrong Stage-1 table, construct a twin that changes only:

- the operator label at the affected node; and
- the selected value implied by the oracle.

Keep all other text, ordering, values, and tokens identical where possible. Feed both the original and corrected tables to Stage 2. The primary intervention outcome is the paired change in correct final action. Also inject a deliberately wrong operator into a matched sample of clean tables to test the reverse direction.

This does not prove that free-form CoT is faithful. It tests a narrower executable claim: **when the operator state is made an explicit input to the decision stage, correcting that state causally rescues decisions.** Without this intervention, “unexpected MAX/MIN appears in the trace” remains a correlational annotation.

### 5.9 Decoding and reproducibility controls

Primary decoding is greedy: `do_sample=False`, temperature and top-p unset, and no beam search. Determinism should still be checked rather than assumed.

- Re-run a stratified 10% of primary generations with shuffled item order on GPU 7.
- Re-run the same subset on a second physical GPU after unloading its original model.
- Compare generated token-ID hashes, not only parsed answers.
- If disagreement exceeds 0.5%, rerun the affected family at batch size 1 with deterministic kernels before using it in the gate.
- Record GPU ID, driver, CUDA, PyTorch, `transformers`, attention backend, and model revision for every shard.

Do not add temperature seeds to the first gate. Sampling variance is a separate study and would multiply the matrix before the causal treatment is even validated.

### 5.10 Statistical analysis

#### Primary unit and outcome

The primary unit is a **paired tree**, not an individual prompt completion. For each cell, pair accuracy is 1 only when both controller variants choose the correct root action. Item accuracy is secondary.

For each model, report:

- pair and item accuracy for A–E;
- all discordant counts for C versus D;
- \(D-C\) in percentage points;
- a two-sided exact McNemar test on pair correctness;
- a 95% paired cluster-bootstrap confidence interval over the 54 pair IDs;
- a 90% interval used only for the smoke-gate decision and clearly labeled as such;
- schema validity, truncation, and each oracle error category by cell.

Estimate the 2×2 effects using a conditional logistic model or GEE with pair-clustered uncertainty:

- procedural-detail main effect;
- dual-operator main effect;
- procedural×dual interaction.

The confirmatory family-level contrasts are exactly:

1. D versus C;
2. `(D-C) - (B-A)`;
3. E versus C.

Apply Holm correction to these three contrasts within each model. Do not correct across models by pretending that all six tests are one discovery pool; instead, use the family replication rule below. Report every unadjusted and adjusted value.

Do not pool thousands of completions and claim a tiny standard error. The six model families are the replication contexts. Any pooled hierarchical estimate must be secondary to the full per-family forest plot.

Pack B is a robustness replication, not another opportunity to select a preferred result. Report the Pack-B C/D effect, its paired interval, and its magnitude relative to Pack A for every family.

### 5.11 Public benchmark after—and only after—the synthetic gate

The next benchmark should be [GameBench](https://arxiv.org/abs/2406.06613), using its [official code repository](https://github.com/Joshuaclymer/GameBench). Begin with **Hive** and **Santorini**, because both are public, deterministic, adversarial strategy environments with natural opponent-response reasoning. Add Sea Battle only later as a stochastic stress test.

The public-benchmark study should not merely paste the five synthetic prompts into full games. Construct a preregistered state-level action-selection evaluation:

1. sample legal, nonterminal states from the official environment;
2. use the environment and a fixed shallow-search oracle to identify candidate actions and opponent-response backups;
3. retain states with a unique oracle-preferred action and an adequate value margin;
4. present identical states under factor-matched single-rule and dual-rule scaffolds;
5. score legal-action rate, oracle action quality, and verifiable search-step/operator errors;
6. run paired state-level inference before any full-game aggregate such as win rate or Bradley–Terry score.

GameBench already reports that scaffolds and models behave differently across games. Therefore “prompt rankings vary by game/model” would not be new. The public stage is justified only to test transport of the **specific operator-interference mechanism** from synthetic trees to natural adversarial planning.

---

## 6. GO/NO-GO thresholds

These thresholds must be committed before the 54 sealed pairs are generated. They are intentionally strict because the surrounding broad phenomenon is already known.

### 6.1 Diagnostic admissibility gate

A model can count toward scientific replication only if all of the following hold:

1. **Strict JSON validity:** at least 99% in both C and D.
2. **Truncation:** no more than 0.5% in either C or D, with an absolute C/D gap no greater than 1 percentage point.
3. **Usable baseline range:** C pair accuracy is at least 65%, with at least three C errors; this avoids counting floor and near-perfect ceiling comparisons as evidence of sign reversal.
4. **No shortcut:** the metadata-only controller/action-position probe is no better than 55% pair accuracy, and each action label/position is optimal equally often up to the prespecified balancing tolerance.
5. **Exact replay:** no more than 0.5% token-ID mismatch in the greedy replay audit after any required batch-size-1 rerun.
6. **Oracle integrity:** all 54 pairs pass independent exact-arithmetic validation, pair-diff validation, and minimum-margin checks.
7. **Template stability:** the sign of D-C does not reverse in the frozen 12-pair plain-versus-native-template diagnostic.

A family failing one condition is still reported but is marked **diagnostically inadmissible** and cannot satisfy a scientific threshold.

### 6.2 Scientific gate for the current project

Advance to the public GameBench stage only if **all** of the following are met:

#### A. Replicated harm

- At least **two diagnostically admissible non-Qwen families** have \(D-C\leq-10\) percentage points under Pack A.
- For both, the paired 90% confidence interval lies entirely below zero.
- For at least one, the paired 95% confidence interval lies entirely below zero.
- The Holm-adjusted D-vs-C test is below 0.10 in both and below 0.05 in at least one. The relaxed 0.10 criterion is acceptable only for this fixed smoke gate; the full study must use conventional confirmatory standards.

#### B. Independent wording robustness

For each of the two negative families:

- Pack B has the same sign;
- its absolute effect is at least 7 percentage points; and
- its magnitude is at least 70% of the corresponding Pack-A effect, unless the Pack-A estimate exceeds 20 points, in which case a 10-point Pack-B effect is sufficient.

#### C. Genuine sign heterogeneity

At least **one different diagnostically admissible non-Qwen family** must have \(D-C\geq+8\) percentage points, with its paired 90% confidence interval entirely above zero, on Pack A and the same sign on Pack B.

Without this positive family, the present “non-monotonic/model-relative transfer” project is not justified. A consistent negative operator-competition effect could motivate a separately re-audited project, but it must not be rescued under the current novelty claim.

#### D. Operator-specific process link

Across each negative family:

- D increases oracle-verified inactive-operator execution by at least 8 percentage points relative to C;
- the increase accounts for at least 30% of the excess D errors relative to C; and
- in the two-stage intervention, correcting the wrong operator/value table rescues at least 50% of eligible wrong final actions, with a paired improvement of at least 20 percentage points over the uncorrected twin.

The deliberate wrong-operator injection should also reduce accuracy in the expected direction. A one-way correction effect without a reverse injection effect is weaker and must be treated as exploratory.

#### E. Factor specificity

- The procedural×dual interaction has the predicted negative sign in both negative families.
- The effect survives opaque operator labels and omission of all algorithm names.
- D-C is not explained by schema validity or truncation differences.
- Harm is not confined to Cell E. If E alone is harmful, classify the result as negation sensitivity.
- The effect is present in at least two of the three difficulty strata and is not restricted to near-tie cases.

### 6.3 Automatic NO-GO conditions

Stop the current project after the smoke test if any of the following occurs:

- fewer than two independent non-Qwen families reproduce the negative D-C contrast;
- no independent non-Qwen family shows the preregistered positive contrast;
- the apparent reversal is created by floor, ceiling, invalid output, or template differences;
- the effect disappears under Pack B;
- literal `MAX/MIN`, the word `Bellman`, or negative prohibition is necessary;
- the symmetric generator removes the effect;
- wrong-operator execution does not increase under D;
- correcting the operator state does not change the final action;
- exact greedy replay is unstable enough to change conclusions;
- the result survives only in Qwen3.5-9B;
- an unregistered prompt, subgroup, parser, or exclusion is needed to cross a threshold.

Do not respond to a failed gate by increasing model count, adding prompt variants, weakening confidence intervals, or searching for a favorable benchmark. That would convert a diagnostic experiment into selection.

### 6.4 What a smoke-test GO does—and does not—authorize

Passing the gate authorizes exactly one next step: the preregistered Hive/Santorini state-level GameBench experiment. It does not authorize an ICLR claim, a broad model-scale story, or a large benchmark sweep.

A full project should be terminated if the synthetic effect fails to transfer to at least one public game under strict paired state-level evaluation. Conversely, public transfer without the synthetic causal process link supports only ordinary prompt sensitivity, which is already crowded.

---

## 7. Reviewer-style rejection risks

### 7.1 Likely decision if the current repository result were submitted as the main paper

A skeptical ICLR reviewer could reject the current version without disputing any of the reported percentages:

> The paper shows that two non-equivalent prompts produce different accuracy on one templated benchmark and one related model lineage. The proposed treatment, “algorithmic prompting,” is not isolated; the strongest ablations are parser-dependent; the benchmark admits a controller-to-action shortcut; and the trace evidence is correlational. Meanwhile, recent work already shows that correct constraints, constrained CoT, and additional reasoning can hurt in model-dependent ways. The result is an interesting observation but does not yet identify a novel mechanism or establish generality.

That rejection would be technically fair. The following risks are ordered by how quickly they would sink the paper.

| Rank | Rejection risk | Why it is fatal or near-fatal now | Minimum evidence needed to answer it |
|---:|---|---|---|
| 1 | **The headline is already known.** | Qi et al., Khan, Darshan and Divekar, and the broader CoT-harm literature already cover correct-constraint harm, overconstraint, instruction interference, and model-relative reversals. Calling the effect “algorithmic prompting inversion” would overclaim priority. | State a narrower operator-selection mechanism; cite the collisions prominently; demonstrate I3–I5 jointly rather than selling I1/I2. |
| 2 | **“Algorithmicity” is an undefined treatment bundle.** | Compact CoT and Bellman differ in many semantic and surface factors. No causal statement can be attached to their raw difference. | The preregistered 2×2 compact/procedural × single/dual matrix, plus the polarity cell and independent wording pack. |
| 3 | **The benchmark can be solved by a shortcut.** | Controller identity predicts whether the first safe action or second branching action is optimal. High pair accuracy therefore does not prove tree backup or operator execution. | Symmetric root-action trees, randomized labels/order/operator mapping, metadata-only probes at chance, and exact pair-diff validation. |
| 4 | **Four Qwen checkpoints are not four replications.** | Shared lineage, tokenizer conventions, post-training influences, and formatting tendencies can explain the pattern. | At least two negative and one positive admissible replications among independent non-Qwen families, under the frozen family-level gate. |
| 5 | **The mechanism ablations are entangled with parsing.** | Positive/local prompt cells often fail to emit the required `FINAL` format, and the fallback parser scans the last action mention. A verbose prompt can change apparent accuracy without changing task belief. | One strict schema, no fallback, invalid-as-wrong primary analysis, unconstrained-format audit, and separate validity/truncation reporting. |
| 6 | **Generated reasoning is not causal evidence.** | Wrong MAX/MIN text can be rationalization, a symptom of controller confusion, or an incomplete regex hit. Trace–accuracy association does not establish mediation. | Structured oracle classification plus corrected/wrong intermediate-state interventions that move final decisions in both directions. |
| 7 | **One wording per factor invites prompt cherry-picking.** | Prompt sensitivity can be larger than the claimed effect, and preferred formats transfer poorly between models. | Two independently authored, frozen prompt packs; same-sign and magnitude-retention threshold; all prompts reported. |
| 8 | **The phenomenon was selected after a different seed failed.** | The exploratory transition is scientifically legitimate, but nominal intervals from the same matrix do not erase post-selection. Reviewers will suspect survivor bias. | A fresh sealed benchmark, three confirmatory contrasts only, frozen thresholds, Holm correction, and publication of all outcomes. |
| 9 | **The “scale reversal” language is causally invalid.** | Qwen3-8B and Qwen3.5-9B differ in generation, architecture/post-training, tokenizer behavior, and size. | Use “checkpoint-dependent heterogeneity” now. Any future scale claim requires at least three sizes from one matched training lineage. |
| 10 | **Six skins are presented as six domains.** | Rephrasing the same tree does not demonstrate planning, game, tool-use, or semantic-domain transfer. | Treat skins only as lexical blocks and reproduce the mechanism on paired states from a public environment. |
| 11 | **A synthetic-only effect may be prompt pathology with no external importance.** | Even a clean operator-conflict result can be too narrow for ICLR if it never affects natural decisions. | Preregistered GameBench transfer in Hive/Santorini with legal-state oracles, paired state-level effects, and process errors. |
| 12 | **The public benchmark could destroy diagnosticity.** | Full-game win rate mixes state distribution, exploration, opponent strength, context growth, illegal moves, and stochasticity. A null or positive aggregate cannot identify the operator mechanism. | Begin with controlled state-level action selection and a fixed shallow-search oracle; use full games only as secondary ecological validation. |
| 13 | **Capability floors and ceilings can manufacture sign changes.** | A weak model cannot be harmed much; a saturated model cannot improve much. Apparent family reversal may simply reflect available headroom. | Baseline admissibility range, difficulty-stratified effects, and a sign that survives the overlapping-capability stratum. |
| 14 | **A named-algorithm lexical prior may be the whole effect.** | “Bellman,” `MAX`, and `MIN` may evoke memorized templates or formatting conventions unrelated to control reasoning. | Opaque labels in the primary test and literal labels only as a secondary generalization check. |
| 15 | **Negation may masquerade as competition.** | “Never apply” and similar language has a documented failure literature, including inverse-scaling patterns. | Isolate Cell E; do not use negative wording in A–D; reject the competition story if E alone is harmful. |
| 16 | **Arithmetic error may masquerade as operator error.** | Hard items can independently increase both arithmetic failures and suspicious trace text. | Exact oracle decomposition, item-fixed comparisons, and the lookup variant that supplies controlled-node candidate values. |
| 17 | **The 54-pair smoke test is not the final evidentiary sample.** | It is enough for a large gated signal but not for precise population claims, many interactions, or game-level generality. | Treat it as a termination gate. A passing result needs a larger preregistered confirmatory set and public-benchmark replication. |
| 18 | **Reproducibility can fail at the model-template layer.** | Model cards, gated licenses, tokenizer revisions, and default chat-template changes can silently alter prompts. | Pin revisions and software; store rendered text/token IDs; publish manifests, output hashes, and exact environment files. |

### 7.2 Claims that must not appear in a submission based on the current evidence

The following formulations would invite an immediate rejection:

- “Correct algorithms confuse larger models.”
- “Bellman prompting exhibits inverse scaling.”
- “Reasoning models overthink minimax.”
- “LLMs systematically execute the wrong controller.”
- “Six domains demonstrate broad planning generalization.”
- “Trace evidence proves operator competition.”
- “More detailed prompts are worse for strong models.”

Each sentence either outruns the design or collides with existing work. The current data support a fixed prompt×checkpoint observation, not any of those general laws.

### 7.3 What would make the result reviewable rather than merely curious

A reviewer needs a causal chain, not another prompt leaderboard:

1. **Factor:** adding the inactive competing operator causes a paired accuracy change after all obvious prompt factors are matched.
2. **Process:** that treatment raises a precisely defined wrong-operator state.
3. **Intervention:** correcting that state rescues the decision, and injecting it damages a clean decision.
4. **Replication:** the negative effect and a true sign reversal appear in independent families under a second wording.
5. **Transport:** the process recurs on a public adversarial-planning benchmark.

If any link is missing, the safest interpretation reverts to ordinary prompt sensitivity or instruction interference—both already established literatures.

---

## 8. Final narrow claim, if any

### No defensible final contribution claim exists at the pinned commit

The current evidence is not sufficient for a paper-level narrow claim. The strongest honest result statement is descriptive:

> On the repository's frozen synthetic benchmark, Qwen3.5-9B is less accurate under one generic Bellman prompt than under one compact-CoT prompt, while Qwen3-8B shows the opposite ranking; suspicious inactive-operator text is enriched among Qwen3.5-9B Bellman errors.

That statement is accurate but not a defensible ICLR contribution because neither the treatment nor the mechanism is identified and the broad phenomenon has close prior art.

### Candidate hypothesis for the pivot—not a claim yet

> **Conditionally irrelevant competing operator rules may induce oracle-verifiable wrong-operator execution, and the sign of that interference may differ across independently trained model families.**

The hypothesis deliberately excludes “larger,” “more capable,” “reasoning model,” “Bellman,” and “inverse scaling.” Those interpretations require evidence that the proposed smoke test does not provide.

### Three experiments required before the hypothesis can become a submission claim

1. **Factor-isolated paired synthetic experiment.** Replace the generator shortcut; run the sealed A–E matrix with strict schema, matched prompts, opaque labels, exact arithmetic, and a second wording pack. This establishes whether operator inventory—not length, procedure, negation, wording, or parsing—causes the effect.
2. **Independent-family process and intervention experiment.** Execute the six-family gate, classify oracle-verifiable intermediate errors, and perform corrected/wrong operator-table interventions. This establishes replication, sign heterogeneity, and an executable process link.
3. **Public adversarial-planning transfer experiment.** Reproduce the same factor and process signature on paired Hive/Santorini states from GameBench before reporting full-game performance. This establishes that the finding is not confined to one synthetic arithmetic shell.

Without all three, an ICLR reviewer can reasonably reduce the result to a known prompt-interference phenomenon plus a benchmark artifact.

---

## 9. Bibliography with direct links

### 9.1 Required repository evidence at the pinned commit

1. ScottBlizzard/idle_2, [`docs/current/CURRENT_STATUS.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/docs/current/CURRENT_STATUS.md).
2. ScottBlizzard/idle_2, [`experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md).
3. ScottBlizzard/idle_2, [`experiments/control_flip/README.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/README.md).
4. ScottBlizzard/idle_2, [`experiments/control_flip/results/v2/analysis/REPORT.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/results/v2/analysis/REPORT.md).
5. ScottBlizzard/idle_2, [`experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md).
6. ScottBlizzard/idle_2, [`experiments/control_flip/results/v2/analysis/summary.csv`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/results/v2/analysis/summary.csv).
7. ScottBlizzard/idle_2, [`experiments/control_flip/results/v2/analysis/prompt_comparisons.csv`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/results/v2/analysis/prompt_comparisons.csv).
8. ScottBlizzard/idle_2, [`experiments/control_flip/run_model.py`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/run_model.py).
9. ScottBlizzard/idle_2, [`experiments/control_flip/generate_benchmark.py`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/generate_benchmark.py).
10. ScottBlizzard/idle_2, [`docs/audits/AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/docs/audits/AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md).

### 9.2 Additional implementation evidence inspected

11. ScottBlizzard/idle_2, [`experiments/control_flip/evaluate.py`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/evaluate.py).
12. ScottBlizzard/idle_2, [`experiments/control_flip/analyze_reasoning.py`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/analyze_reasoning.py).
13. ScottBlizzard/idle_2, [`experiments/control_flip/launch_matrix.sh`](https://github.com/ScottBlizzard/idle_2/blob/239d56cbffb14054c70b96fc8cdf689181f6f32f/experiments/control_flip/launch_matrix.sh).
14. ScottBlizzard/idle_2, [pinned repository tree](https://github.com/ScottBlizzard/idle_2/tree/239d56cbffb14054c70b96fc8cdf689181f6f32f).

### 9.3 Correct constraints, instruction interference, and overconstraint

15. Qi et al. (2026), [*On the Paradoxical Interference between Instruction-Following and Task Solving*](https://arxiv.org/abs/2601.22047).
16. Khan (2025/2026), [*You Don't Need Prompt Engineering Anymore: The Prompting Inversion*](https://arxiv.org/abs/2510.22251).
17. Darshan and Divekar (2026), [*When Gradients Collide: Failure Modes of Multi-Objective Prompt Optimization for LLM Judges*](https://arxiv.org/abs/2605.26046).
18. Coleman et al. (2023), [*In-context Interference in Chat-based Large Language Models*](https://arxiv.org/abs/2309.12727).

### 9.4 Chain-of-thought harm, overthinking, and test-time degradation

19. Liu et al. (2025), [*Mind Your Step (by Step): Chain-of-Thought Can Reduce Performance on Tasks Where Thinking Makes Humans Worse*](https://arxiv.org/abs/2410.21333).
20. Li et al. (2025), [*When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs*](https://arxiv.org/abs/2505.11423).
21. Jin et al. (2025), [*Reasoning Can Hurt the Inductive Abilities of Large Language Models*](https://arxiv.org/abs/2505.24225).
22. Ghosal et al. (2025), [*Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models*](https://arxiv.org/abs/2506.04210).
23. Huang et al. (ICLR 2024), [*Large Language Models Cannot Self-Correct Reasoning Yet*](https://openreview.net/forum?id=IkmD3fKBPQ).
24. Chen et al. (2026), [*Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning*](https://arxiv.org/abs/2605.06840).

### 9.5 Algorithmic prompting, programmatic reasoning, and process evaluation

25. Zhou et al. (ICLR 2023), [*Teaching Algorithmic Reasoning via In-Context Learning*](https://arxiv.org/abs/2211.09066).
26. Chen et al. (TMLR 2023), [*Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks*](https://arxiv.org/abs/2211.12588).
27. Wei et al. (2022), [*Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*](https://arxiv.org/abs/2201.11903).
28. Lin et al. (ACL 2025), [*Transparent Assessment of LLM Reasoning in Games: A Rule-Based Approach*](https://aclanthology.org/2025.acl-long.378/); [GAMEBoT project](https://visual-ai.github.io/gamebot/).

The audit did not locate a primary Program-of-Thought paper that already combines a **correct executable scaffold becoming harmful**, paired controller counterfactuals, wrong conditional-operator traces, and a causal operator-versus-proceduralization ablation. That absence does not restore novelty to generic scaffold harm; the nearest collisions above already occupy it.

### 9.6 Prompt sensitivity, model-relative transfer, and inverse scaling

29. Sclar et al. (ICLR 2024), [*Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying about Prompt Formatting*](https://arxiv.org/abs/2310.11324).
30. Mizrahi et al. (TACL 2024), [*State of What Art? A Call for Multi-Prompt LLM Evaluation*](https://aclanthology.org/2024.tacl-1.52/).
31. Wei et al. (2023), [*Inverse Scaling Can Become U-Shaped*](https://arxiv.org/abs/2211.02011).

### 9.7 Negation and negative-instruction effects

32. Jang et al. (2023), [*Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts*](https://proceedings.mlr.press/v203/jang23a.html).
33. Truong et al. (2023), [*An Analysis of Language Models on Negation Benchmarks*](https://aclanthology.org/2023.starsem-1.10/).

### 9.8 Strategic reasoning, minimax-adjacent evaluation, and public transfer

34. Costarelli et al. (2024), [*GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents*](https://arxiv.org/abs/2406.06613); [official code](https://github.com/Joshuaclymer/GameBench).
35. Jia et al. (2025), [*Large Language Model Strategic Reasoning Evaluation through Behavioral Game Theory*](https://arxiv.org/abs/2502.20432).
36. Lin et al. (2025), [GAMEBoT project and benchmark materials](https://visual-ai.github.io/gamebot/).

The located strategic-reasoning literature documents model/game/scaffold heterogeneity and decomposable game errors, but it does not already provide the requested paired, one-controller-variable, wrong-MAX/MIN causal design. This is why the public benchmark is a transfer test rather than the source of the novelty claim.

### 9.9 Human negation, ironic process, and automation analogies

37. Wegner (1994), [*Ironic Processes of Mental Control*](https://pubmed.ncbi.nlm.nih.gov/8121959/).
38. Parasuraman and Riley (1997), [*Humans and Automation: Use, Misuse, Disuse, Abuse*](https://journals.sagepub.com/doi/10.1518/001872097778543886).
39. Skitka, Mosier, and Burdick (1999), [*Does Automation Bias Decision-Making?*](https://doi.org/10.1006/ijhc.1999.0252).

These sources are analogical only. They do not warrant attributing human ironic control or automation bias to language models.

### 9.10 Exact model cards for the smoke test

40. Meta, [`meta-llama/Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).
41. Google, [`google/gemma-2-9b-it`](https://huggingface.co/google/gemma-2-9b-it).
42. Mistral AI, [`mistralai/Mistral-7B-Instruct-v0.3`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3).
43. Microsoft, [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct).
44. Allen Institute for AI, [`allenai/OLMo-2-1124-7B-Instruct`](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct).
45. IBM, [`ibm-granite/granite-3.1-8b-instruct`](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct).

---

**Bottom line:** preserve the observed Qwen prompt ranking as an exploratory fact, abandon the broad “algorithmic prompting inversion” story, and run only the sealed factor-isolation gate. The project earns further compute only if independent families, an actual sign reversal, and an operator-state intervention all survive together.
