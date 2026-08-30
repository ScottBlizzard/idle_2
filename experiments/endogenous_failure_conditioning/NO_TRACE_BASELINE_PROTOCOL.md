# No-trace baseline kill test

Status: **frozen after the v2.1 final gate and before any no-trace output exists**.

This is a post-hoc, new-experiment diagnostic. It cannot change the completed
`KILL_NO_SELECTION_REVERSAL` decision. Its only purpose is to distinguish trace-mediated
damage from ordinary shared capability blind spots on the 60 common GSM8K problems.

## Fixed intervention

- Use the exact four v2.1 corrector revisions and their frozen chat-template settings.
- Use the exact 60 common GSM8K questions in the frozen v2.1 error bank.
- Present each `(corrector, problem)` once with no proposed solution, for 240 calls.
- Keep the original system prompt byte-identical. The user content is:

```text
Problem:
{question}

No proposed solution is supplied. Solve the problem independently, show a careful derivation, and give the final answer in the required format.
```

- Greedy decoding, one continuation, 768 new-token budget, FP16, exact model revision.
- Gold answers remain evaluator-only.
- Existing v2.1 outputs are immutable and are joined only after the 240 baselines finish.

## Primary estimand

Let `B(c,p)=1` when corrector `c` solves problem `p` in the no-trace condition. Restrict
the primary analysis to these baseline-solvable corrector-problem pairs. For each frozen
error trace, define exposure damage as `1 - correction_success`.

The primary contrast is:

```text
external_neutral same-lineage damage - external_neutral cross-lineage damage
```

Inference uses 10,000 problem-clustered bootstrap draws with seed 20260830.

Secondary locked quantities are the corresponding assistant-history damage contrast and
same-minus-cross source-wrong-answer retention contrasts.

## Automatic decision

1. `NO_GO_ENGINEERING` if the no-trace parser-or-truncation rate exceeds 2%, an exact
   revision/hash check fails, fewer than 80 of 240 corrector-problem pairs are
   baseline-solvable, or any planned cell is missing.
2. `KILL_SHARED_BLIND_SPOTS` if external-neutral excess damage is below 5 percentage
   points or its problem-clustered 95% interval includes zero.
3. `KILL_NO_ATTRACTOR_RETENTION` if the damage gate passes but external-neutral excess
   retention is below 5 points or its interval includes zero.
4. `KILL_NOT_ROLE_ROBUST` if both external gates pass but assistant-history excess
   damage is non-positive.
5. `ADVANCE_STYLE_CONTENT_SEPARATION` only if all preceding gates pass.

An advance does not establish a paper. It authorizes one semantic-preserving trace-style
intervention designed to separate family-style familiarity from semantic error
alignment. No cross-provider or Oral-level claim is allowed from this test alone.

