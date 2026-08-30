# Outcome-blind resource-sharing amendment

This amendment was made before any correction outcome existed. It changes only
GPU scheduling and failure recovery; the frozen model revisions, error bank,
wrappers, prompts, deterministic decoding, analysis, and scientific gates are
unchanged.

- The obsolete launcher required GPUs 4--7 to be completely idle for 180
  seconds. That was an engineering precaution, not a scientific requirement.
- The shared launcher may use any physical GPU 0--7 when its measured free
  memory exceeds a model-specific conservative floor.
- It never stops or modifies another process. Contention may change wall-clock
  time, which is not an experimental outcome in this pilot.
- Transformer outputs are fsynced after every batch of two. An engineering
  failure can therefore resume by immutable `case_id` without regenerating
  completed cells.
- Allocation decisions are recorded in `RESOURCE_ALLOCATION.tsv` before model
  loading.
