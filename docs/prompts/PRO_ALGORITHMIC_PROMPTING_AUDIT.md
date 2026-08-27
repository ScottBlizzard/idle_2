# Prompt for Pro: Algorithmic-Prompting Novelty and Diagnosticity Audit

Use a fresh Pro conversation. Give it the repository link and paste the prompt below.

---

You are conducting a falsification-first literature and experimental-design audit for a possible ICLR research seed. Do not brainstorm broadly and do not assume the seed is novel or valuable. Search the literature continuously while reasoning, prioritize primary sources, and provide direct links for every important collision claim.

## Required repository reading

Read these files completely before making recommendations:

1. `docs/current/CURRENT_STATUS.md`
2. `experiments/control_flip/CONTROL_FLIP_EXPERIMENT_REPORT_ZH.md`
3. `experiments/control_flip/README.md`
4. `experiments/control_flip/results/v2/analysis/REPORT.md`
5. `experiments/control_flip/results/v2/analysis/OPERATOR_AUDIT.md`
6. `experiments/control_flip/results/v2/analysis/summary.csv`
7. `experiments/control_flip/results/v2/analysis/prompt_comparisons.csv`
8. `experiments/control_flip/run_model.py`
9. `experiments/control_flip/generate_benchmark.py`

Use the older documents under `docs/audits/` only when needed to prevent revival of already rejected broad directions. Treat `docs/archive/` as provenance, not evidence for the current seed.

## Empirical fact pattern to audit

The completed paired experiment contains 180 pairs crossed over six semantic domains and three difficulty levels. Within each pair, only the post-chance controller changes; the exact optimal root action must flip.

The original controller-insensitive-failure claim is already rejected because compact CoT reaches 90.6% pair accuracy on Qwen3.5-4B and 97.2% on Qwen3.5-9B.

The surviving observation is non-monotonic algorithmic prompting:

- Qwen3.5-9B: compact CoT 97.2%, generic Bellman 78.9%; paired difference -18.3 percentage points, 95% CI [-24.4, -12.2].
- Qwen3-8B: compact CoT 63.9%, generic Bellman 76.7%.
- Qwen3.5-4B: compact CoT 90.6%, generic Bellman 89.4%.
- In Qwen3.5-9B Bellman generations, 11.1% of items contain an explicit unexpected MAX/MIN call; accuracy is 45.0% on those items versus 95.0% on clean items.
- A prompt containing only the applicable operator recovers Qwen3.5-9B pair accuracy to 85.0%, still below compact CoT.

## Questions you must answer

### A. Nearest-work collision audit

Search at least the following literatures and any adjacent terminology you discover:

- chain-of-thought hurting performance;
- overthinking and test-time-compute degradation;
- algorithmic prompting and program-of-thought failure;
- instruction interference and conflicting-instruction effects;
- negative instructions, negation, and ironic process effects in language models;
- prompt sensitivity and prompt-induced inverse scaling;
- minimax/MAX-MIN reasoning failures;
- procedural overconstraint, automation bias, and scaffold-induced errors;
- model-specific reasoning-template transfer.

For each nearest paper, state exactly whether it already contains all, some, or none of the following contribution ingredients:

1. a correct algorithmic scaffold makes a model worse than a less explicit reasoning prompt;
2. the direction of the effect reverses across model families or scales;
3. paired counterfactual tasks isolate one control variable;
4. generated traces expose incorrect operator execution;
5. a causal prompt-factor ablation separates operator competition from general proceduralization.

Do not call ordinary prompt sensitivity a novelty gap unless you can explain a materially different scientific claim.

### B. Adversarial interpretation audit

Try to destroy the current observation using simpler explanations:

- unequal prompt length or verbosity;
- chat-template or thinking-mode differences;
- output truncation and fallback parsing;
- prompt wording rather than algorithmicity;
- Qwen-specific formatting behavior;
- arithmetic difficulty differences;
- contamination from mentioning both MAX and MIN;
- negative-instruction effects from phrases such as “never apply”;
- benchmark-generation artifacts;
- deterministic decoding instability;
- multiple-comparison or selective-reporting effects.

For every plausible confound, name the minimal controlled experiment that would resolve it.

### C. Minimal cross-family smoke test

Design the smallest experiment that can decide whether a full project is justified. It must fit 8 independent RTX 4090 GPUs with 24 GB each and should finish within one day.

Specify:

- 4–6 genuinely independent open model families that fit the hardware, with exact checkpoints and memory expectations;
- no more than 60 paired examples for the first smoke test;
- the minimal prompt-factor matrix;
- parsing and truncation controls;
- paired statistical tests and uncertainty reporting;
- an explicit GO/NO-GO threshold;
- which established public planning, game, tool-use, or reasoning benchmark should be used next if the synthetic smoke test passes.

Do not recommend a large sweep before the smoke-test gate.

### D. Contribution verdict

Return exactly one verdict:

- `STOP — already known or diagnostic artifact`
- `PIVOT — interesting phenomenon but the current claim is wrong`
- `PROVISIONAL GO — a specific novelty gap survives`

If the verdict is `PROVISIONAL GO`, write the narrowest defensible one-sentence claim. Then list the three experiments without which an ICLR reviewer would reject it.

## Required output structure

1. Executive verdict
2. Claim decomposition
3. Nearest-work collision table
4. Confound and diagnosticity audit
5. Minimal one-day smoke-test protocol
6. GO/NO-GO thresholds
7. Reviewer-style rejection risks
8. Final narrow claim, if any
9. Bibliography with direct links

Be adversarial. The goal is to prevent wasted experiments, not to rescue the seed.

Write the complete output as one Markdown document named:

`ALGORITHMIC_PROMPTING_NOVELTY_AUDIT.md`

---
