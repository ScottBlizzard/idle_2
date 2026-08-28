# Stage D Discovery Engineering Retry Ledger

Date: 2026-08-28

This ledger records outcome-blind engineering failures before `FINAL_GATE.json`. Scientific route-effect fields were not inspected during either diagnosis.

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
- Repair: decode the complete generated sequence once, request the fast tokenizer's canonical `offset_mapping`, and require the decoded text to re-encode to the exact generated token IDs before using the offsets.

## Integrity decision

The repair preserves the frozen definition: an eligible token must have a non-whitespace/non-punctuation surface, occur before the final-answer span, and be selected by minimum teacher-forced probability with the frozen tie break. It only replaces an invalid implementation of character offsets with the tokenizer's canonical full-sequence offsets.

Since acquisition source code changed after preflight v3, the old authorization is preserved rather than reused. Corrected outcome-blind preflight v4 must pass before a new discovery authorization. Failed partial shards are not merged into the corrected run.
