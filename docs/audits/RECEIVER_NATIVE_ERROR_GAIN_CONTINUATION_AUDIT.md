# Receiver-native error gain after the causal no-go

Status: **`NO_GO_SEMANTIC_REWRITE_AS_ORAL_SEED — ONE_MECHANISM_AUDIT_HOLD`**.

## The contradiction we actually found

The same frozen data now supports two statements:

1. Across different source errors, receiver NLL strongly predicts whether the receiver
   retains the source's specific wrong answer.
2. Within the same source error, changing only natural whitespace realization successfully
   changes receiver NLL but does not measurably change error retention.

This is a predictive–interventional gap. It falsifies the simplest “native-looking text is
an error-gain channel” story. It does not show that every semantic realization is causally
irrelevant.

## Candidate explanations

### H1: surface fluency is the causal carrier

This was the preregistered whitespace experiment. The manipulation passed, but the paired
effect was `+0.625pp` with a confidence interval spanning approximately `−1.9pp` to
`+3.3pp`. H1 is closed for the tested natural-layout range.

### H2: NLL proxies semantic error-state compatibility

Two traces can have the same final wrong answer while encoding different decompositions,
intermediate states, shortcuts, and first-error locations. A receiver may inherit an error
when those state transitions agree with its own conditional policy. Whole-trace NLL would
then be predictive because it partially measures this compatibility, while whitespace NLL
changes would be causally inert.

This remains possible, but “semantic compatibility” is not yet an identified variable. A
semantic rewrite can silently change error localization, step granularity, salience,
readability, anchoring, or the computational graph. Without an executable equivalence
criterion, a positive rewrite experiment would not isolate H2.

### H3: source difficulty and answer anchoring confound the association

Some wrong solutions may simply be harder to diagnose, more coherent, or closer to the
receiver's own likely answer. These properties can simultaneously lower receiver NLL and
increase retention without NLL or style causing the retention. This is currently at least
as plausible as H2.

## Literature-role audit

### Direct adversaries

- [Do explanations generalize across large reasoning models?](https://arxiv.org/abs/2601.11517)
  already measures whether transferred explanations induce the same behavior in other
  models, including convergence on incorrect answers. A generic “wrong CoTs transfer”
  claim is occupied.
- [Style over Substance](https://arxiv.org/abs/2504.01738) explicitly separates stylistic
  reasoning patterns from correctness during distillation and reports benefits even when
  synthetic traces lead to wrong answers. A generic “style matters independently of
  correctness” claim is occupied, although its intervention is training rather than
  inference-time correction.
- [Same Question, Different Answers](https://arxiv.org/abs/2607.22554) studies behavior
  changes under meaning-preserving paraphrases across math and factual tasks. A generic
  semantic-paraphrase instability benchmark is occupied.
- [Structure Enables Effective Self-Localization of Errors](https://arxiv.org/abs/2602.02416)
  shows that discrete semantic thought boundaries materially change error localization and
  correction. A generic “structured rewrites improve correction” method is occupied.

### Mechanism foundations and mandatory baselines

- [In Their Own Words](https://arxiv.org/abs/2509.22230) makes rationale generation
  receiver-specific by filtering teacher proposals through student token probabilities.
  It is the closest positive adversary for any distributional-alignment claim.
- [The Role of Feedback Alignment in Self-Distillation](https://arxiv.org/abs/2606.11173)
  argues that step-aligned feedback works because it targets failure locations rather than
  forcing an alternative derivation. This supports structural rather than surface
  compatibility.
- [The Potential of CoT for Reasoning](https://openreview.net/forum?id=uwuSD63wbe)
  measures the contribution of partial trace segments to later correctness and transfers
  them across models. Any new score must beat segment potential, not only whole-trace NLL.
- [GRACE: Discriminator-Guided Chain-of-Thought Reasoning](https://openreview.net/forum?id=2MiTZxLFA9)
  starts from the fact that language models can assign high likelihood to incorrect steps
  and learns a correctness discriminator. Any “error-state compatibility margin” must be
  separated from step correctness scoring.
- [FormInv](https://openreview.net/pdf/657c5bcd8bd576918be38354490f8814ee73c499.pdf)
  provides a recent semantic-invariance measurement protocol for formal mathematical
  paraphrases and is a mandatory robustness baseline.

### Theory prior

- [LLM Reasoning Is Latent, Not the Chain of Thought](https://arxiv.org/abs/2604.15726)
  explicitly argues that surface trace, latent trajectory, and serial compute must be
  disentangled. Our predictive–interventional gap is consistent with this prior, so the
  broad interpretation is not new by itself.

## Why the obvious semantic rewrite is not authorized

A plan that asks one model to paraphrase each wrong trace, ranks rewrites by receiver NLL,
and measures correction would be easy to run but weak to interpret:

- NLL selection would also select changed reasoning structure;
- semantic equivalence judges are least reliable exactly where the source reasoning is
  wrong;
- answer preservation does not imply first-error or state-transition preservation;
- paraphrase instability, explanation transfer, structural correction, and
  student-aligned rationale work already supply obvious baselines and neighboring claims;
- a positive result would not establish whether NLL, readability, step boundaries,
  answer salience, or graph compatibility caused the effect.

Scaling this design across providers would therefore produce a larger but still
under-identified paper.

## The sole retained mechanism audit

One question remains worth theory-first inspection, not GPU execution:

> Do student-friendly rationale methods succeed because they lower token surprise, or
> because student participation changes the semantic reasoning path and local error-state
> transitions?

A separating design would require at least three independently constructed objects for the
same executable reasoning graph:

1. a surface-likelihood intervention that changes NLL while preserving the graph;
2. a graph intervention that changes local state compatibility while matching NLL;
3. a negative control that changes readability/step boundaries without changing either.

It must prospectively verify graph equivalence and compare against RSD, segment potential,
step correctness discrimination, and structured error localization. Until such a
construction exists, this is a mechanism-audit hold rather than an active seed.

## Binding decision

Do not launch semantic rewrites, new providers, training sweeps, or larger benchmarks for
the current error-gain seed. The current work is a clean negative result plus a useful
diagnostic warning: observational trace likelihood should not be interpreted as a causal
control variable.

For an ICLR Oral target, the next active seed must either supply a formally identifiable
error-state intervention that clears the above collisions, or leave this carrier entirely.

