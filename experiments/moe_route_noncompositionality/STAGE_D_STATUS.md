# Stage D Execution Status

Updated: 2026-08-28 23:51 Asia/Hong_Kong

Status: **ENGINEERING RETRY — CORRECTED PREFLIGHT v4 REQUIRED**

## Binding state

Stage E passed its engineering gate. Outcome-blind preflight v3 subsequently passed every structural check and authorized one Stage D discovery acquisition. No H1--H4 value has been inspected, and Stage C/A remain unauthorized.

The discovery has not reached a scientific gate. Two versioned, preserved startup/acquisition attempts ended for engineering reasons:

1. `stage_d_discovery_attempt1_network_timeout` stopped before model loading because the tokenizer attempted a Hugging Face network request. The cached tokenizer was independently verified, so subsequent launches use offline mode.
2. The offline attempt loaded the model and reached GSM8K problem 22, with 9 retained problems, before strict token-to-character validation rejected a byte-level BPE prefix-decoding mutation. Its 18 sealed shard/checksum files and full log are preserved; no route-effect value was inspected.

The second issue is not a failed scientific hypothesis. Prefix-by-prefix decoding is not a valid character-boundary method when adjacent byte tokens jointly complete a Unicode character. The repair uses the fast tokenizer's full-sequence offset mapping and requires an exact decode/re-encode ID round trip. It changes neither the frozen eligibility rule nor any hypothesis threshold.

## Validation and transition

- 19 local tests pass.
- 19 tests pass in the isolated remote Stage D environment, including the pinned MATH equivalence verifier.
- The actual cached OLMoE tokenizer passes a multilingual split-token boundary check.
- Failed outputs and their authorization/log records remain immutable and versioned.

Because acquisition code changed after preflight v3, a new outcome-blind preflight v4 must pass before a fresh authorization is created. Once v4 passes, discovery will be relaunched on physical GPU 4--7 under the same 180-second exclusivity check and unchanged scientific thresholds.

See [`STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md`](STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md) for the incident ledger.
