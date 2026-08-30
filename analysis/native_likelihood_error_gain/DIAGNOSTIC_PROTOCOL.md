# Native-likelihood error-gain diagnostic

Status: **post-hoc mechanism diagnostic, frozen before computing any receiver likelihood**.

The parent crossed-repair pilot and no-trace kill test remain closed under their own
binding gates. This diagnostic creates no new generation outcome. It asks whether the
observed same-lineage retention anomaly is better described by a continuous receiver
compatibility variable than by a categorical lineage label.

## Motivation and collision boundary

Prior work already establishes that:

- reasoning traces can transfer both correct and incorrect conclusions across models
  ([Pal et al., 2026](https://arxiv.org/abs/2601.11517));
- student-aligned, low-surprise reasoning traces can transfer more effectively, but the
  alignment is model-specific
  ([Kim et al., 2025](https://arxiv.org/abs/2509.22230));
- model families occupy distinct error spaces
  ([ErrorTrace, NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/hash/632bd15f4a957cb912f36bea7d19daea-Abstract-Conference.html));
- same/same-family/cross-family auditors already differ in effectiveness
  ([Chain-of-Models, 2026](https://arxiv.org/abs/2607.28636)).

Therefore “same-family models share errors” is not a contribution. The remaining narrow
question is whether a wrong trace's likelihood under the receiver predicts retention of
that trace's *specific wrong answer*. If so, methods that optimize student-friendly trace
compatibility have a measurable dual-use failure mode: the same high-gain channel that
supports correct transfer may also amplify erroneous transfer.

## Frozen score

Scope: the 240 GSM8K wrong traces in the v2.1 error bank and the exact four cached
corrector revisions.

For each `(trace, corrector)` pair, compute token-mean negative log likelihood of the raw
error response under the corrector, conditioned on this plain-text prefix:

```text
Problem:
{question}

Proposed solution:
```

Tokenize prefix and trace separately with the corrector tokenizer, concatenate their token
IDs, and score only trace tokens. Use FP16 weights and no truncation; fail if a sequence
exceeds 8192 tokens. Record exact model revision, token count, total NLL, mean NLL, and
output hash. This score is a distributional diagnostic, not the exact likelihood of the
chat-rendered correction prompt.

Total forward-pass cells: `240 traces × 4 receivers = 960`.

## Frozen analyses

Use existing GSM8K correction outputs. Primary outcome is retention of the source wrong
answer; correction accuracy is secondary.

1. Test whether same-lineage traces have lower mean NLL within corrector-problem strata.
2. Fit a problem-, corrector-, generator-, and wrapper-controlled logistic model for source
   wrong-answer retention with standardized mean NLL and same-lineage indicators.
3. Compare the same-lineage coefficient before and after adding NLL. Report percentage
   attenuation, but do not call it causal mediation.
4. Repeat separately for external-neutral and assistant-history wrappers.
5. Report corrector-specific slopes and leave-one-corrector-out stability.

The diagnostic is considered mechanistically promising only if, under external-neutral:

- lower NLL significantly predicts higher source-error retention with problem-clustered
  95% confidence excluding zero;
- same-lineage traces are lower-NLL on average; and
- adding NLL attenuates the same-lineage log-odds coefficient by at least 25% without
  reversing the NLL slope.

Failure closes the native-likelihood explanation. Passing only motivates a new causal
intervention; it does not authorize a paper claim or modify earlier gates.

