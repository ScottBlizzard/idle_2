# Endogenous Failure Conditioning Pilot

Current executable experiment: outcome-blind v2 Qwen2.5×Qwen3 crossed-repair pilot.

1. Read [`PILOT_PROTOCOL.md`](PILOT_PROTOCOL.md) and
   [`PILOT_PROTOCOL_AMENDMENT_V2.md`](PILOT_PROTOCOL_AMENDMENT_V2.md).
2. The frozen v2 config is
   [`FROZEN_CONFIG_V2_QWEN_LINEAGES.json`](FROZEN_CONFIG_V2_QWEN_LINEAGES.json).
3. `prepare_error_bank.py` downloads and hash-verifies the public sources, then freezes
   480 errors on 120 shared problems.
4. `preflight.py` verifies model revisions, chat templates, hashes, and context lengths.
5. `prepare_models.py` downloads the four frozen revisions into project-scoped `HF_HOME`
   before any GPU is allocated.
6. `run_corrector.py` runs one model and resumes by immutable case ID.
7. `analyze_pilot.py` scores only a complete 3,840-cell matrix and writes the automatic
   gate.
8. `launch_shared_pilot.sh` selects distinct physical GPUs 0--7 by measured free-memory
   floors and can safely resume batch-synced outputs without stopping foreign jobs.
9. `finalize_existing_pilot.sh` preserves the completed legacy launch, analyzes it after
   all correctors finish, and invokes the shared launcher only after an engineering failure.

V1 never entered inference because Gemma access was gated; see
[`V1_ACCESS_FAILURE.md`](V1_ACCESS_FAILURE.md).

V2.1 completed all 3,840 cells. Its binding decision is
`KILL_NO_SELECTION_REVERSAL`; see [`RESULTS_REPORT_ZH.md`](RESULTS_REPORT_ZH.md).
