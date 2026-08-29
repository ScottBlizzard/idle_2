# Trajectory Fault Gain: Minimal Separation Note

## Status

`THEORY-FIRST CANDIDATE`.  This note proves only that deletion-based causal importance
and plausible-fault amplification are different estimands.  It does not prove that fault
gain transfers across natural fault distributions or improves a real model.

## 1. Three estimands

For a clean-correct trajectory \(\tau=(s_1,\ldots,s_T)\) and step \(i\), define:

1. **local correctness** \(C_i\): whether the observed \(s_i\) satisfies a step oracle;
2. **deletion importance**

   \[
   D_i=\ell(Y(\tau_{i\leftarrow\varnothing}),y^*)-
   \ell(Y(\tau),y^*);
   \]

3. **fault gain** under a frozen local fault channel \(Q_i\):

   \[
   G_i(Q_i)=\mathbb E_{\delta\sim Q_i}
   [\ell(Y(\tau_{i\leftarrow\delta}),y^*)-
   \ell(Y(\tau),y^*)].
   \]

Masking/removal estimates \(D_i\).  Intermediate fault injection estimates \(G_i\).
Even perfect estimation of the former does not identify the latter.

## 2. Four-way separation construction

Consider a binary target \(y^*=0\), zero-one loss, and a clean step value \(s=0\).
The continuation observes whether the step is absent, clean, or faulted to \(s=1\).
All four continuations below return the correct answer on the clean trajectory.

| continuation rule | absent | clean `s=0` | fault `s=1` | deletion importance \(D\) | fault gain \(G\) |
|---|---:|---:|---:|---:|---:|
| ignore/recompute | 0 | 0 | 0 | 0 | 0 |
| require presence, sanitize value | 1 | 0 | 0 | 1 | 0 |
| recompute if absent, trust if present | 0 | 0 | 1 | 0 | 1 |
| require and trust | 1 | 0 | 1 | 1 | 1 |

Therefore \((D,G)\) realizes every point in \(\{0,1\}^2\).  No deterministic function of
deletion importance can recover fault gain without an additional continuation assumption.

The third row is the practical novelty hinge.  A masking-based method calls the step
unimportant because the model compensates for its absence.  A realistic wrong value is
more dangerous than absence because downstream computation trusts a present value.
Examples include cached calculations, stale tool outputs, incorrectly populated fields,
and summaries that silently weaken a binding condition.

## 3. Clean-correct paths can reverse under faults

Let two trajectories \(\tau_A\) and \(\tau_B\) have identical clean loss, token budget,
and deletion importance.  Let \(\tau_A\) use the `recompute if absent, trust if present`
continuation and \(\tau_B\) use `ignore/recompute`.  Then

\[
\ell(Y(\tau_A),y^*)=\ell(Y(\tau_B),y^*)=0,
\qquad D_A=D_B=0,
\]

but under the same non-degenerate bit-flip fault channel,

\[
G_A>G_B=0.
\]

Thus clean outcome, local correctness, length, and deletion importance can all tie while
fault robustness differs maximally.  A reranker using any combination of only those tied
variables cannot recover the robust ordering in this construction.

This is a separation result, not yet a learning theorem.

## 4. What can and cannot transfer

Suppose the measured channels are \(Q^{(1)},\ldots,Q^{(m)}\).  For a deployment mixture

\[
Q_\alpha=\sum_{k=1}^m\alpha_kQ^{(k)},
\]

linearity of expectation gives

\[
G_i(Q_\alpha)=\sum_{k=1}^m\alpha_kG_i(Q^{(k)}).
\]

Therefore average-gain selection is justified for a known mixture, and
\(\min_\tau\max_k G_\tau(Q^{(k)})\) gives the standard robust choice over an unknown
mixture of measured channels.

There is **no** distribution-free guarantee for an unseen channel outside this convex
hull.  A paper must demonstrate held-out fault-family transfer empirically or state a
structural assumption connecting the channels.  Calling arbitrary synthetic corruptions
representative of natural errors is inadmissible.

## 5. Why this is not yet an Oral theorem

The four-way construction is elementary.  Its role is to protect the empirical question
from being dismissed as deletion-based causal importance under a new name.  Oral-level
substance would require at least one of:

1. a nontrivial condition under which gain rankings transfer across fault families;
2. a prospective estimator that predicts natural execution failures better than prefix
   failure forecasting, PRMs, and masking importance;
3. a demonstrated training reversal where locally cleaner/process-preferred trajectories
   are more fault-amplifying at matched clean accuracy and compute;
4. a cross-domain law connecting reasoning, code, and stateful tool execution.

## 6. Immediate falsification questions

Before GPU use, a 20-problem pipeline check must answer:

- Can steps and faults be generated without an LLM judge deciding the scientific label?
- Does `absent` actually trigger recomputation while `present but wrong` triggers trust in
  nontrivial numbers of trajectories?
- Do multiple clean-correct trajectories for the same problem exhibit a stable gain
  ordering?
- Does gain estimated from arithmetic faults predict a held-out structural or stale-state
  fault?
- Does the same distinction appear in executed tool/code state rather than only narrated
  chain of thought?

If the first two fail, the candidate should be killed before a model-scale run.

