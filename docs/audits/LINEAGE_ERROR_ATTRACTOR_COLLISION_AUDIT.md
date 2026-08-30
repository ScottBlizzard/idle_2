# Lineage-conditioned error attraction: collision audit

Date: 2026-08-30  
Status: literature audit completed; only a narrow causal residual remains testable.

## Executive decision

The broad claim that models from the same family share errors or make poor mutual
auditors is **not novel enough** for an ICLR Oral seed. It is already covered from four
directions: correlated family errors, model-family error fingerprints, self-generated
text recognition, and same/same-family/cross-family auditing.

The completed Qwen2.5×Qwen3 pilot nevertheless leaves one narrow unresolved question:

> Holding the problem, corrector, chat role, and solve-from-scratch competence fixed,
> does exposure to a wrong trace cause more *new damage* when that trace comes from the
> corrector's own lineage than from another lineage?

This is materially narrower than “same-family models share blind spots.” It is also not
answered by the completed pilot because the pilot did not measure whether each corrector
could solve the same problem without seeing an error trace. A 240-call no-trace baseline
is therefore authorized as a **kill test**, not as confirmation of a new paper.

## What the completed pilot actually showed

On GSM8K, where parser/truncation failures were only 2.40%, same-lineage correctors
retained the source wrong answer more often than cross-lineage correctors:

| wrapper | same-lineage retention | cross-lineage retention | same-lineage accuracy | cross-lineage accuracy |
|---|---:|---:|---:|---:|
| external neutral | 62.29% | 45.00% | 17.92% | 32.50% |
| assistant history | 73.12% | 51.88% | 13.54% | 26.25% |

Problem-clustered bootstrap intervals exclude zero for both retention and accuracy
contrasts. However, the effect is asymmetric: most of the advantage comes from Qwen3
correcting Qwen2.5 errors. That is compatible with ordinary complementary capability and
does not by itself establish a relational error-attractor mechanism.

## Direct collisions

1. **Correlated Errors in Large Language Models** studies more than 350 models and finds
   that wrong answers are highly correlated, with provider and architecture as important
   predictors. This is the strongest existing explanation for shared blind spots and
   makes raw same-family correction differences non-novel.
   [Paper](https://arxiv.org/abs/2506.07962)

2. **ErrorTrace** explicitly maps model-family-specific error spaces and uses them for
   black-box lineage tracing. It establishes that families have stable, identifiable
   error cohorts; a paper whose only conclusion is “families fail differently” collides
   directly.
   [NeurIPS 2025 paper](https://papers.neurips.cc/paper_files/paper/2025/hash/632bd15f4a957cb912f36bea7d19daea-Abstract-Conference.html)

3. **Chain-of-Models** directly compares same-model, same-family, and different-family
   auditors inspecting another model's biased reasoning trace. Auditor identity matters,
   but the best auditor is bias-specific rather than universally cross-family. This
   occupies the practical “choose a heterogeneous auditor” result and requires any new
   work to identify a mechanism rather than merely a routing heuristic.
   [Paper](https://arxiv.org/abs/2607.28636)

4. **The Self-Correction Illusion** keeps an erroneous claim byte-identical and changes
   only its chat-template role. Relabeling a thought-internal claim as user, tool, or
   memory content raises correction by 23--93 percentage points. Any ownership result
   without role-matched controls is therefore invalid.
   [Paper](https://arxiv.org/abs/2606.05976)

5. **Large Language Models Are Overconfident in Their Own Responses** reports higher
   confidence for assistant-owned than byte-identical user-owned answers. This is an
   additional direct warning that apparent “self” effects can be role artifacts.
   [Paper](https://arxiv.org/abs/2606.03437)

## Positive adversaries and rival explanations

1. **Self-Generated Text Recognition** shows that models can sometimes recognize their
   own outputs, but quality heuristics, evaluation format, conversation structure, and
   domain strongly confound the effect. Training recognition also induces downstream
   self-preference. This makes latent authorship plausible, but demands quality- and
   role-controlled intervention.
   [Paper](https://arxiv.org/abs/2608.26159)

2. **LLM Evaluators Recognize and Favor Their Own Generations** links self-recognition
   with self-preference, providing a causal foundation for lineage-conditioned trust.
   [Paper](https://arxiv.org/abs/2404.13076)

3. **Self-Preference Bias in LLM-as-a-Judge** argues that lower perplexity and familiar
   text explain much of the apparent authorship effect. A surviving result must separate
   semantic error alignment from surface familiarity.
   [Paper](https://arxiv.org/abs/2410.21819)

4. **ReasonOps** identifies model-specific operator-sequence fingerprints in reasoning
   traces. This makes implicit source recognition technically credible, while also
   turning “styles are identifiable” into background rather than a contribution.
   [Paper](https://arxiv.org/abs/2605.29192)

5. **Reasoning that Travels** shows that cross-model trace transfer can arise from answer
   extraction, reasoning scaffolding, or receiver competence. These are mandatory rival
   mechanisms for any trace-exposure claim.
   [Paper](https://arxiv.org/abs/2605.28913)

6. **Answer-Centric or Reasoning-Driven?** finds a strong answer anchor: masking answer
   cues lowers performance even when a reasoning chain remains. Source-answer retention
   is therefore not by itself proof of lineage recognition.
   [Paper](https://arxiv.org/abs/2506.17630)

## Mandatory baselines

Any promotable experiment must include:

- the same corrector solving the same question with no proposed trace;
- byte-identical or semantically matched role controls;
- corrector and problem fixed effects, with problem-clustered inference;
- source-answer retention separated from generic wrong-answer changes;
- trace quality/length controls;
- at least one cross-provider replication before a general family claim;
- a manipulation that separates semantic content from detectable family style if the
  no-trace kill test survives.

## Residual falsifiable mechanism

Let `B(c,p)` be whether corrector `c` solves problem `p` with no trace. For an exposed
trace `t`, let `Y(c,p,t)` be correction success. On the baseline-solvable subset
`B(c,p)=1`, define damage as `1-Y`.

The residual hypothesis predicts:

1. externally presented wrong traces cause measurable damage relative to no trace;
2. same-lineage traces cause at least five percentage points more damage than
   cross-lineage traces on the same corrector-problem pairs;
3. the problem-clustered 95% interval for that excess damage excludes zero;
4. the direction repeats in assistant history; and
5. same-lineage excess retention of the source wrong answer accompanies the damage.

If these conditions fail, the anomaly is best explained by shared capability blind
spots, generic answer anchoring, or role effects and should be killed. If they pass, the
next experiment must manipulate trace style while preserving semantics; only a semantic
effect that survives role and style controls has plausible Oral-level depth.

## Search record and limitations

Searches covered self-correction, cross-model correction, same-family auditing,
correlated errors, reasoning-trace transfer, model-source recognition, answer anchoring,
and model-family error spaces, with emphasis on 2024--2026 primary papers. The configured
multi-source academic MCP tools were unavailable in this session; the OpenAlex fallback
was attempted but rate-limited (HTTP 429), so discovery used direct arXiv, OpenReview,
NeurIPS, and official paper pages. This is sufficient to reject the broad claim but not a
substitute for a final camera-ready systematic review.
