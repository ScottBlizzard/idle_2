# Stage E Execution Status

Updated: 2026-08-28 16:52 Asia/Hong_Kong

Status: **QUEUED — NO SCIENTIFIC RESULT**

## Completed preparation

- Implemented the frozen OLMoE route-intervention harness for eight trajectories, one layer pair, and two alternatives per layer.
- Added standard-route replay, full-versus-layer-boundary-suffix comparison, deterministic reruns, equal-cardinality assertions, and a one-hour hard timeout.
- Stored all artifacts under `/mnt/sdb/ccj/idle_2/moe_route_noncompositionality`; the nearly full system disk is not used for model weights or results.
- Downloaded all three `allenai/OLMoE-1B-7B-0924-Instruct` weight shards and verified exact byte sizes and SHA-256 digests before admitting them to the Hugging Face cache.

## Resource-safety events

The 4090 server repeatedly launched unrelated jobs across all eight GPUs after apparently idle snapshots. The exclusive launcher correctly refused to start when it observed an occupied target GPU. A separate shared-GPU smoke attempt was tried only after setting a model-memory cap; another job entered during model loading and the attempt ended in CUDA OOM. It produced no result files and is not a Stage E observation.

Shared-GPU execution is now prohibited. No unrelated process has been stopped or modified.

## Active safe queue

Remote watcher:

- status file: `/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/queue/status.txt`;
- log: `/mnt/sdb/ccj/idle_2/moe_route_noncompositionality/queue/wait_and_run.log`;
- target: physical GPU 7, keeping this project within the preferred GPU 4–7 range;
- admission: zero CUDA compute processes across the whole server for 180 consecutive seconds;
- runtime guard: poll the target GPU every five seconds and terminate only the Stage E process group if a foreign process appears;
- conflict retries: at most three;
- maximum queue wait: twelve hours.

Codex heartbeat `monitor-moe-stage-e` checks the queue every 15 minutes. On `COMPLETE`, it must retrieve and validate results, write the Stage E report, commit, and push. On any terminal failure, it must preserve the failure and publish a failure report. It may not enter Stage D.
