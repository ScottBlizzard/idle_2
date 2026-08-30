# Receiver-native error gain: whitespace-only causal kill test

Status: **frozen before candidate likelihood scoring and before every new correction outcome**.

## Claim under test

The post-hoc diagnostic found that a wrong trace's likelihood under the receiver predicts
retention of its specific wrong answer. This experiment tests a deliberately narrower
causal claim:

> Holding the ordered sequence of every non-whitespace character, the wrong answer, the
> arithmetic content, the problem, and the receiver fixed, a naturally formatted
> realization that has lower receiver NLL causes more source-error retention than a
> matched higher-NLL realization.

This is a kill test, not a paper-scale validation. Passing authorizes a cross-provider and
semantic-paraphrase design; failing closes the whitespace-channel version of the mechanism.

## Collision boundary

Prior work already covers model-family error correlation, transfer of correct and wrong
reasoning, and model-specific/student-aligned rationale distillation. The proposed residual
is not “same-family models share errors.” It is the controlled dual-use hypothesis that a
receiver-friendly reasoning channel can amplify an unchanged error.

## Frozen source and scope

- Source bank SHA-256: `ae0fcf6d04ed7c3374fa37bb5d1a7874d8eefddbca77056598bd79c95a26e57b`.
- Parent model config SHA-256: `c3ce5803da434b9d3a6436e06c57814b51f997d27975c65bdd79aa35a9e8103a`.
- Diagnostic result SHA-256: `24f35d22f90b04e5c957dbc7ecbc0548cbb6aeb8ab70873d146cf066303d6453`.
- Domain: GSM8K only.
- Problems: the 30 problem keys with the smallest SHA-256 digest of the problem key,
  selected without reference to correction outcomes.
- Traces: all four frozen generator errors for each selected problem (`120` traces).
- Receivers: the exact four cached Qwen2.5/Qwen3 revisions from the parent config.
- Main wrapper: external-neutral only.

## Intervention library

Each source trace is deterministically rendered into 12 layout candidates. Candidates may
only alter whitespace runs at existing token boundaries: ordinary spacing, existing line
breaks, and whitespace following sentence/step punctuation. The library includes the raw
trace, normalized/flat layouts, single- and double-line step layouts, and two- or four-space
indentation. It never inserts, removes, changes, or reorders a non-whitespace character.

For every candidate, the builder must verify:

```python
re.sub(r"\s+", "", candidate) == re.sub(r"\s+", "", source_trace)
```

Duplicate rendered strings are removed deterministically. Any trace with fewer than four
unique candidates makes the manipulation gate fail.

## Outcome-blind likelihood selection

For each `(source trace, receiver)` cell, score every candidate with the same plain-text
prefix used in the diagnostic. Compute token-mean NLL over the candidate trace only.

Among candidate pairs whose receiver token counts differ by at most two, select the pair
with maximum NLL separation. The lower-NLL member is `high_native`; the higher-NLL member
is `low_native`. Tie-breaking is lexical on frozen variant identifiers. Correction outcomes
must not exist when this selection is performed.

Expected selected cells: `120 traces × 4 receivers = 480`, yielding `960` correction calls.

### Binding manipulation gate

Correction generation is authorized only if all conditions hold:

1. all `480` trace-receiver cells have a token-matched pair;
2. every source trace has at least four unique candidates;
3. the median paired NLL gap is at least `0.10` nats/token;
4. at least `75%` of cells have an NLL gap of at least `0.05` nats/token;
5. every selected pair passes the exact non-whitespace identity check and token-count
   difference ceiling.

Failure returns `KILL_INSUFFICIENT_WHITESPACE_ACTUATION` and forbids correction calls.

## Correction generation

Use the parent system prompt and external-neutral correction request, replacing only the
proposed solution with the selected rendering. Decode greedily with `1024` maximum new
tokens. Each exact receiver runs on one GPU. Outputs are resumable and record prompt hash,
model revision, generated-token count, and selected-candidate hashes.

## Frozen analysis and gate

Primary outcome: exact retention of any frozen source wrong answer. Secondary outcome:
GSM8K correctness. Parse using the existing frozen verifier.

For each outcome, compute `high_native - low_native` as a paired contrast and a 10,000-draw
problem-cluster bootstrap interval. Report corrector-specific paired contrasts.

Engineering quality requires parser-or-truncation failure at or below `2%`. The scientific
gate passes only if:

1. primary retention contrast is at least `+0.08`;
2. its problem-cluster 95% interval is strictly above zero;
3. at least three of four correctors have a positive retention contrast;
4. a problem/corrector/generator-controlled logistic model gives a negative coefficient
   for continuous NLL gap direction (lower NLL predicts more retention), with a
   problem-cluster 95% interval below zero.

Decisions, in binding order:

- quality failure: `NO_GO_ENGINEERING`;
- primary or robustness failure: `KILL_NO_CAUSAL_ERROR_GAIN`;
- pass: `ADVANCE_CROSS_PROVIDER_CAUSAL_REPLICATION`.

Accuracy is secondary and cannot rescue a failed retention gate. Thresholds and source
selection may not be modified after candidate likelihoods or correction outcomes are read.

