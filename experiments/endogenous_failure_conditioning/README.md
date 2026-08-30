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
8. `wait_and_run_pilot.sh` uses only physical GPUs 4--7 after 18 consecutive ten-second
   idle observations and an independent last-moment check.
9. `continue_after_models.sh` connects the CPU-only model download to the safe GPU
   watcher; a failed model download terminates before GPU allocation.

V1 never entered inference because Gemma access was gated; see
[`V1_ACCESS_FAILURE.md`](V1_ACCESS_FAILURE.md).
