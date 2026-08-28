# Stage D Discovery Engineering Retry Ledger

Date: 2026-08-28

This ledger records outcome-blind engineering failures before `FINAL_GATE.json`. Scientific route-effect fields were not inspected during diagnosis.

## Attempt 1: network timeout

- Preserved remote result: `results/stage_d_discovery_attempt1_network_timeout`
- Preserved log: `queue/stage_d_discovery_attempt1_network_timeout.log`
- Failure: `AutoTokenizer.from_pretrained` attempted a Hub template-tree request and timed out before model loading.
- Diagnosis: the complete tokenizer and model are already cached; an offline tokenizer load succeeded independently.
- Repair: inherit `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1` at launch. No source, protocol, or threshold changed for this retry.

## Attempt 2: byte-level token boundary mapping

- Preserved remote result: `results/stage_d_discovery_attempt2_prefix_offset_failure`
- Preserved log: `queue/stage_d_discovery_attempt2_prefix_offset_failure.log`
- Engineering progress before failure: GSM8K problem 22 examined; 9 problems retained; 18 sealed shard/checksum files written.
- Failure: prefix-by-prefix decoding failed the string-concatenation round trip when a later byte token changed the decoded surface of an earlier prefix.
- Diagnosis: byte-level BPE prefix decoding is not prefix-stable for split Unicode characters.
- Initial repair: decode the complete generated sequence once, request the fast tokenizer's canonical `offset_mapping`, and require the decoded text to re-encode to the exact generated token IDs before using the offsets.

## Attempt 3: preflight v4 non-canonical BPE segmentation

- Preserved remote result: `results/stage_d_preflight_v4`
- Preserved log: `queue/stage_d_preflight_v4.log`
- Failure: a generated MATH-500 response decoded successfully but did not re-encode to the identical token-ID segmentation.
- Diagnosis: valid generated BPE sequences are not guaranteed to be the tokenizer encoder's unique canonical segmentation, so decode/re-encode equality was an invalid engineering invariant.
- Repair: convert every original token ID to its byte-alphabet token, decode bytes incrementally as UTF-8, assign a split character to its completing token, and verify that joined token surfaces equal the tokenizer's full decode.
- Validation: 19 tests pass locally and remotely; the cached OLMoE tokenizer also passed 5,000 deterministic random-ID sequences with exact full-decode agreement.

## Integrity decision

The repair preserves the frozen definition: an eligible token must have a non-whitespace/non-punctuation surface, occur before the final-answer span, and be selected by minimum teacher-forced probability with the frozen tie break. It only replaces invalid character-offset assumptions with monotone surfaces derived from the original generated IDs.

Since acquisition source code changed after preflight v4, the old authorization remains preserved rather than reused. Corrected outcome-blind preflight v5 must pass before a new discovery authorization. Failed partial shards are not merged into the corrected run.
