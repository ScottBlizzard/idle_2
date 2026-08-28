# Stage E Execution Status

Updated: 2026-08-28 18:18 Asia/Hong_Kong

Status: **ENGINEERING PASS — NO SCIENTIFIC INTERPRETATION — STAGE D NOT AUTHORIZED**

## Binding outcome

The intervention harness and the outcome-blind generation-throughput pilot jointly pass every Stage E engineering gate frozen in [`THRESHOLDS.yaml`](THRESHOLDS.yaml). This result establishes implementation correctness and compute feasibility only. It does not test H1–H5 and contains no publishable scientific result.

Stage D remains unauthorized because [`PREREGISTRATION.md`](PREREGISTRATION.md) explicitly authorizes Stage E only. A separate binding decision is required before discovery execution.

## Intervention engineering evidence

- Model: `allenai/OLMoE-1B-7B-0924-Instruct`, BF16, one exclusive RTX 4090.
- Resolved architecture: 16 layers, 64 routed experts, top-8 routing; tested layers 3 and 5.
- Workload: 8 engineering trajectories and 72 standard/single/joint conditions.
- Standard replay maximum absolute logit error: `0.0` (threshold `1e-4`).
- Cached-versus-uncached maximum absolute logit error: `0.0` (threshold `1e-4`).
- Deterministic rerun maximum absolute logit error: `0.0` (threshold `1e-6`).
- Wall time including model loading: `149.3981 s`; upper-bound GPU use: `0.04150 h`.
- Projected intervention time: `0.99791 h` for discovery and `2.39497 h` for the confirmation proxy, or `3.39288 h` total.

The 72 route effects are engineering diagnostics only. They must not be used to select hypotheses, layer pairs, route constructions, or thresholds.

## Generation-throughput evidence

- Frozen datasets: GSM8K test and MATH-500 test.
- Frozen decoding: 4 samples/problem, temperature `0.7`, top-p `0.95`, top-k `0`, maximum 768 new tokens.
- Pilot size: 2 deterministically selected problems per dataset, 4 problems and 16 generations total.
- Observed generated length: 157–425 tokens; mean `264.69` tokens.
- Conservative speed statistic: maximum per-problem seconds/token, `0.0104836 s/token`.
- Projection evaluates 4 × 768 tokens for each of 64 target trajectories per dataset and model.
- Projected generation time: `1.14508 h` for discovery and `2.74820 h` for the confirmation proxy.
- Projected model-load overhead: `0.04704 h`.
- Raw full projection: `7.33321 h`.
- Frozen 25% engineering guardband: `9.16651 h`, below the 12-hour discovery-plus-confirmation cap.
- Cumulative Stage E upper bound: `0.09193 GPU h`, below the 1-hour gate.

## Scope limitation

The compute projection assumes the target 64 retained trajectories per dataset and model. It does not estimate how many extra problems may be required when none of four generated candidates is correct. Stage D, if separately authorized, must enforce its cumulative six-hour hard stop and report an inadmissible cell rather than weaken the retention requirement.

The DeepSeek confirmation estimate remains a `2.4×` active-parameter proxy rather than a direct timing measurement. The 25% guardband provides engineering slack but is not a formal upper bound.

## Resource integrity

- Both runs used physical GPU 7 only after 180 consecutive seconds with no CUDA process and less than 512 MiB allocated memory.
- The intervention watcher terminated after success.
- A foreign process entered GPU 7 only after the generation pilot completed; it was not stopped or modified.
- GPUs 0–3 were never used by this project.
- All server artifacts remain under `/mnt/sdb/ccj/idle_2/moe_route_noncompositionality`.

## Canonical artifacts

- [`results/stage_e/stage_e_summary.json`](results/stage_e/stage_e_summary.json)
- [`results/stage_e/conditions.csv`](results/stage_e/conditions.csv)
- [`results/stage_e/diagnostics.json`](results/stage_e/diagnostics.json)
- [`results/stage_e_generation/stage_e_generation_summary.json`](results/stage_e_generation/stage_e_generation_summary.json)
- [`results/stage_e_generation/generation_records.jsonl`](results/stage_e_generation/generation_records.jsonl)
- [`RESULTS_REPORT_ZH.md`](RESULTS_REPORT_ZH.md)

Local copies match the server byte-for-byte by SHA-256. The exact hashes are recorded in the results report.
