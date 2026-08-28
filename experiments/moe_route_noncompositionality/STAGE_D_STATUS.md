# Stage D Execution Status

Updated: 2026-08-28 19:00 Asia/Hong_Kong

Status: **CORRECTED OUTCOME-BLIND PREFLIGHT RUNNING — SCIENTIFIC DISCOVERY NOT YET AUTHORIZED**

## Binding state

Stage E passed its engineering gate. A separate authorization audit now permits implementation and outcome-blind preflight under [`STAGE_D_PROTOCOL_AMENDMENT_V1.md`](STAGE_D_PROTOCOL_AMENDMENT_V1.md), but it does not yet permit the 64-trajectory discovery acquisition.

The first preflight attempt (`stage_d_preflight_v1`) was deliberately terminated before producing a gate because Transformers warned that generation did not receive an explicit attention mask while the checkpoint uses the same token ID for padding and end-of-sequence. Its partial directory and log are preserved and cannot support authorization.

The corrected preflight (`stage_d_preflight_v2`) supplies an all-ones attention mask for every unpadded generation, writes to a new directory, and uses physical GPU 4 only after the required 180-second exclusive-idle check. It may validate engineering structure but may not aggregate or interpret H1--H4 route effects.

## Frozen implementation

- Authorization audit: [`STAGE_D_AUTHORIZATION_AUDIT.md`](STAGE_D_AUTHORIZATION_AUDIT.md)
- Binding amendment: [`STAGE_D_PROTOCOL_AMENDMENT_V1.md`](STAGE_D_PROTOCOL_AMENDMENT_V1.md)
- Machine-readable configuration: [`STAGE_D_FROZEN.yaml`](STAGE_D_FROZEN.yaml)
- Frozen local implementation commit: `cb0b6f2` and its ancestors beginning with `77044e6`
- Unit tests: 17 remote tests pass, including the pinned MATH-500 equivalence verifier and parameter matching.

## Next automatic transition

Only `PREFLIGHT_GATE.json` with status `STAGE_D_PREFLIGHT_PASS` can create the one-run `STAGE_D_RUN_AUTHORIZATION.json`. The discovery watcher must then select only physical GPUs 4--7, wait for 180 seconds of exclusive idleness, enforce the six-hour cumulative cap, and stop without entering Stage C regardless of the scientific outcome.
