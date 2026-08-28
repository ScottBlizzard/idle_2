# Stage D Execution Status

Updated: 2026-08-28 19:43 Asia/Hong_Kong

Status: **`NO_GO_STAGE_D_PREFLIGHT` — PIPELINE PAUSED — SCIENTIFIC DISCOVERY NOT AUTHORIZED**

## Binding state

Stage E passed its engineering gate. A separate authorization audit now permits implementation and outcome-blind preflight under [`STAGE_D_PROTOCOL_AMENDMENT_V1.md`](STAGE_D_PROTOCOL_AMENDMENT_V1.md), but it does not yet permit the 64-trajectory discovery acquisition.

The first preflight attempt (`stage_d_preflight_v1`) was deliberately terminated before producing a gate because Transformers warned that generation did not receive an explicit attention mask while the checkpoint uses the same token ID for padding and end-of-sequence. Its partial directory and log are preserved and cannot support authorization.

The corrected preflight (`stage_d_preflight_v2`) supplied an all-ones attention mask for every unpadded generation and completed its four acquisitions. Its automatic gate returned `NO_GO_STAGE_D_PREFLIGHT`: MATH-500 stable IDs contain slash characters, which created nested shard paths that the one-level validator glob did not discover. The acquisition recorded two MATH-500 trajectories, but the validator correctly observed zero and failed the count gate.

The v2 directory and log are preserved. No H1--H4 value was inspected. [`STAGE_D_PREFLIGHT_V2_FAILURE.md`](STAGE_D_PREFLIGHT_V2_FAILURE.md) contains the binding diagnosis.

## Frozen implementation

- Authorization audit: [`STAGE_D_AUTHORIZATION_AUDIT.md`](STAGE_D_AUTHORIZATION_AUDIT.md)
- Binding amendment: [`STAGE_D_PROTOCOL_AMENDMENT_V1.md`](STAGE_D_PROTOCOL_AMENDMENT_V1.md)
- Machine-readable configuration: [`STAGE_D_FROZEN.yaml`](STAGE_D_FROZEN.yaml)
- Frozen local implementation commit: `cb0b6f2` and its ancestors beginning with `77044e6`
- Unit tests: 17 remote tests pass, including the pinned MATH-500 equivalence verifier and parameter matching.

## Next automatic transition

The filesystem-safe correction is implemented and tested locally but has not been rerun. A new v3 preflight requires an explicit resumed authorization. No `STAGE_D_RUN_AUTHORIZATION.json` exists, no discovery watcher was launched, and Stage C/A remain unauthorized.
