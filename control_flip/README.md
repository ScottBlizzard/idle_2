# Control-Flip Diagnostic

This directory contains a falsification-first diagnostic for the proposed
**controller-conditioned stochasticity** research seed.

Each benchmark pair describes the same two root actions:

- one action ends at a known utility;
- one action leads to a public chance event and then a choice among terminal
  utilities.

The only difference inside a pair is who makes the post-chance choice. In the
`self` member, the focal agent chooses and therefore maximizes utility. In the
`opponent` member, an adversary chooses and therefore minimizes focal-agent
utility. The generator enforces

```text
opponent-controlled branching value < safe value < self-controlled branching value
```

so the exact optimal root action flips while all transition probabilities and
terminal utilities remain unchanged.

## Files

- `generate_benchmark.py`: deterministic paired-data generator and exact solver.
- `run_model.py`: batched local Hugging Face inference with resumable JSONL output.
- `evaluate.py`: pair-aware metrics, bootstrap confidence intervals, error taxonomy,
  paired prompt comparisons, crossed-factor breakdowns, and Markdown report generation.
- `analyze_reasoning.py`: audits generated calculations for unexpected MAX/MIN calls.
- `run_server.sh`: safe launcher that refuses occupied GPUs.
- `launch_matrix.sh`: launches the reserved-GPU model matrix without touching occupied cards.
- `tests/test_benchmark.py`: generator and solver invariants.
- `results/v2`: 7,200 raw generations and the complete final analysis.

## Quick start

```bash
python generate_benchmark.py --pairs 180 --seed 20260826 --output data/control_flip.jsonl
python -m unittest discover -s tests -v

CUDA_VISIBLE_DEVICES=4 python run_model.py \
  --data data/control_flip.jsonl \
  --model /path/to/model \
  --model-id qwen \
  --prompt-mode direct \
  --output outputs/qwen.direct.jsonl

python evaluate.py --data data/control_flip.jsonl --predictions outputs/*.jsonl \
  --output-dir analysis
```

## Pre-registered kill criteria

The seed is a **NO-GO** if any of the following holds after at least 120 pairs:

1. a strong open model reaches at least 90% pair accuracy with ordinary zero-shot
   chain-of-thought;
2. direct prompting errors are almost entirely parsing failures;
3. errors do not show a controller-insensitive pattern (choosing the same root
   action in both pair members);
4. a one-line Bellman scaffold closes at least 80% of the direct-to-oracle gap,
   leaving no robust failure after instruction clarification.

Passing the diagnostic is necessary but not sufficient for an ICLR paper. A GO
requires a systematic controller-insensitive failure across model scales and
domains that survives explicit reasoning prompts.

## Completed v2 result

The fully crossed v2 experiment used 180 pairs (six domains x three difficulty
levels x ten pairs), four open Qwen-family models, and five prompt modes. It is a
**NO-GO for the original robust-failure claim**: ordinary compact chain-of-thought
reached 90.6% pair accuracy on Qwen3.5-4B and 97.2% on Qwen3.5-9B.

A narrower prompt-interference observation survived: on Qwen3.5-9B, the generic
Bellman template reduced pair accuracy from 97.2% to 78.9% and produced explicit
wrong-operator calls in 11.1% of items. See `CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`
and `results/v2/analysis/REPORT.md` for the decision and limitations.
