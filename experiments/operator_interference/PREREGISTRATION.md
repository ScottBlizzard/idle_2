# Competing-Operator Interference: Frozen Smoke-Test Protocol

Status: pre-inference protocol. Confirmatory model outputs must not be inspected until this file, the generator, both prompt packs, the parser, and the analysis code are committed.

## Hypothesis under test

Adding a conditionally inactive competing operator may cause oracle-verifiable execution of that operator. The sign of the resulting accuracy effect may differ across independently trained model families.

This protocol does not test whether detailed prompts, chain-of-thought, Bellman prompts, or larger models are generally harmful.

## Data

- Six visible engineering pairs, excluded from every inferential result.
- Fifty-four confirmatory pairs in a balanced six-skin by three-difficulty by three-instance design.
- Two root actions have identical topology: two chance outcomes and the same number of candidate values at corresponding difficulty levels.
- Within each pair, the task payload differs only in the marked active-controller span.
- Action order, role semantics, operator semantics, values, and presentation labels are balanced independently.
- Exact rational arithmetic is the oracle. Ties and sub-threshold margins are rejected.
- A metadata-only role/action-order lookup must achieve no more than 55% item accuracy.

Confirmatory seed: `20260827`. This seed is frozen before the confirmatory file is generated.

## Prompt factors

Pack A contains five cells:

- A: compact, active operator only, affirmative;
- B: compact, active and inactive operators, affirmative;
- C: procedural, active operator only plus a neutral rule slot, affirmative;
- D: procedural, active and inactive operators, affirmative;
- E: procedural, active operator plus explicit prohibition of the inactive operator.

Pack B independently rewrites only C and D. Compared cells are token matched per tokenizer to within two input tokens using the frozen neutral-marker procedure in `prompts.py`. No confirmatory prompt contains `Bellman`; A–D contain no negative prohibition.

## Models

Primary independent families:

1. Meta Llama: `unsloth/Meta-Llama-3.1-8B-Instruct`, an accessible full-precision mirror of Meta Llama 3.1 8B Instruct;
2. Google Gemma: `unsloth/gemma-2-9b-it`, an accessible full-precision mirror of Gemma 2 9B IT;
3. Mistral: `mistralai/Mistral-7B-Instruct-v0.3`;
4. Microsoft Phi: `microsoft/Phi-4-mini-instruct`;
5. Ai2 OLMo: `allenai/OLMo-2-1124-7B-Instruct`;
6. IBM Granite: `ibm-granite/granite-3.1-8b-instruct`.

The two mirrors replace gated upstream repositories because the experiment server has no Hugging Face authentication. Their configuration and weight ancestry must be recorded before inference. Existing Qwen3.5-9B is a positive control and cannot satisfy an independent-family threshold.

All models use BF16, official/native chat templates, disabled native thinking where supported, greedy decoding, batch size one for primary structured inference, no quantization, no CPU offload, and no multi-GPU sharding. Model and tokenizer revisions are pinned in `model_manifest.json` before confirmatory inference.

## Primary outputs

The primary run uses grammar-constrained JSON with a common dynamic schema and `max_new_tokens=192`. Invalid or truncated outputs count as wrong. No fallback parser is allowed. Every record stores rendered text, input and output token IDs, schema status, EOS/length stop reason, software versions, GPU, and prompt/schema hashes.

Primary unit: paired tree. Pair accuracy is one only when both controller variants are correct.

Primary confirmatory contrasts per model:

1. D minus C in Pack A;
2. `(D-C) - (B-A)` in Pack A;
3. E minus C in Pack A.

Holm correction is applied to these three contrasts within each model. Pack B C/D is a mandatory wording replication, not a selectable alternative.

## Diagnostic admissibility

A family can count only if all conditions hold:

1. strict JSON validity is at least 99% in C and D;
2. truncation is at most 0.5% in each and differs by at most one percentage point;
3. C pair accuracy is at least 65% and contains at least three pair errors;
4. the metadata-only probe is at most 55%;
5. exact greedy replay mismatch is at most 0.5% after any batch-size-one rerun;
6. all pair, exact-arithmetic, and margin validations pass;
7. C/D sign does not reverse in the frozen 12-pair native-versus-plain-template diagnostic.

## Scientific GO gate

Proceed to a public GameBench study only if every block passes:

- At least two admissible non-Qwen families have Pack-A D-C at or below -10 points, both 90% paired intervals entirely below zero, at least one 95% interval below zero, and adjusted significance below the preregistered 0.10/0.05 thresholds.
- For both negative families, Pack B has the same sign, at least a 7-point effect, and at least 70% magnitude retention, with the preregistered exception for Pack-A effects over 20 points.
- A different admissible non-Qwen family has Pack-A D-C at or above +8 points with its 90% interval above zero and the same Pack-B sign.
- In each negative family, D raises inactive-operator execution by at least 8 points, explains at least 30% of excess D errors, and correcting the structured operator state rescues at least half of eligible wrong decisions with at least a 20-point paired improvement. Reverse wrong-operator injection must damage decisions in the expected direction.
- The procedural-by-dual interaction is negative in both negative families; the result survives opaque labels and both prompt wordings; schema validity, truncation, near ties, and Cell E do not explain it.

Any automatic NO-GO condition listed in `docs/audits/ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md` terminates the current seed. Failed thresholds may not be repaired by adding models, trying new prompts, selecting subgroups, or changing parsers.

## Authorized next stage

A complete GO authorizes only a preregistered state-level Hive/Santorini experiment using the official GameBench environment. It is not itself an ICLR contribution claim.
