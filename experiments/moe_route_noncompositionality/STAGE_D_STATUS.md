# Stage D Execution Status

Updated: 2026-08-29 00:11 Asia/Hong_Kong

Status: **PREFLIGHT v5 PASSED — DISCOVERY WAITING FOR STABLE GPU**

## Binding state

Stage E passed its engineering gate. Outcome-blind preflight v3 subsequently passed every structural check and authorized one Stage D discovery acquisition. No H1--H4 value has been inspected, and Stage C/A remain unauthorized.

The discovery has not reached a scientific gate. Two versioned, preserved startup/acquisition attempts ended for engineering reasons:

1. `stage_d_discovery_attempt1_network_timeout` stopped before model loading because the tokenizer attempted a Hugging Face network request. The cached tokenizer was independently verified, so subsequent launches use offline mode.
2. The offline attempt loaded the model and reached GSM8K problem 22, with 9 retained problems, before strict token-to-character validation rejected a byte-level BPE prefix-decoding mutation. Its 18 sealed shard/checksum files and full log are preserved; no route-effect value was inspected.

Corrected preflight v4 then exposed a second boundary assumption: decoded text need not re-encode to the same non-canonical BPE segmentation. Its failed output and log are preserved. This is also an engineering failure, not a scientific gate.

The final repair incrementally decodes the bytes represented by the original generated token IDs. A character spanning multiple BPE tokens is assigned to the token that completes it, producing monotone surfaces without re-tokenization. It changes neither the frozen eligibility rule nor any hypothesis threshold.

## Validation and transition

- 19 local tests pass.
- 19 tests pass in the isolated remote Stage D environment, including the pinned MATH equivalence verifier.
- The actual cached OLMoE tokenizer passes 5,000 deterministic random-ID decoding trials.
- Failed outputs and their authorization/log records remain immutable and versioned.

Outcome-blind preflight v5 passed every structural gate. Two discovery launches then safely aborted because GPU 4 was only transiently idle before a foreign workload returned; no discovery directory was created. The watcher now requires its own 180-second continuous-idle window before invoking the launcher's independent 180-second check. A source-hash-bound authorization will be recreated for this queue-only repair, after which discovery will wait on physical GPU 4--7 under unchanged scientific thresholds.

See [`STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md`](STAGE_D_DISCOVERY_ENGINEERING_RETRIES.md) for the incident ledger.
