# Endogenous Failure Conditioning in Multi-Stage LLM Evaluation

## Status

`PRIMARY THEORY-FIRST FALSIFIER`. This note replaces trajectory fault gain as the
leading candidate. It does not claim that post-failure deployment statistics are invalid.
It claims that they cannot, by themselves, identify a model's downstream diagnostic or
repair capability because every model induces a different failure cohort.

## 1. The estimand problem

Let model (m) first attempt item (X). Let (F_m=1) denote initial failure and let
(R_m=1) denote successful repair in a subsequent stage. A common reported statistic is

\[
S_m^{\mathrm{own}}=P(R_m=1\mid F_m=1).
\]

This is a useful end-to-end property of the deployed self-correction pipeline. It is not a
pure measure of correction capability. Expanding over latent error state (E) gives

\[
S_m^{\mathrm{own}}
=\int P(R_m=1\mid E=e,m)\,dP(E=e\mid F_m=1,m).
\]

Both the response function and the error distribution change with (m). A stronger model
can be a better corrector at every fixed error while displaying a lower correction rate on
its own errors because only more difficult errors survive its first stage.

## 2. Minimal sign-reversal construction

Let item difficulty be (d\sim\mathcal N(0,1)) and capability be (a). Define

\[
P(F=1\mid d,a)=\sigma(2(d-a))
\]

and

\[
P(R=1\mid F=1,d,a)=\sigma(-0.5+0.5a-2.5d).
\]

At every fixed (d), correction probability strictly increases with capability. Yet
numerical integration gives:

| capability | initial accuracy | correction on own failures | correction on common bank |
|---:|---:|---:|---:|
| -1 | 0.225 | 0.270 | 0.371 |
| 0 | 0.500 | 0.222 | 0.435 |
| 1 | 0.775 | 0.166 | 0.500 |
| 2 | 0.932 | 0.130 | 0.565 |

Thus the apparent scaling law changes sign when the error distribution is held fixed. The
construction is reproduced by
[`../../analysis/endogenous_failure_conditioning/simulate_reversal.py`](../../analysis/endogenous_failure_conditioning/simulate_reversal.py).

This is a standard selection/mixture phenomenon, not a new probability theorem. The paper
opportunity is an evaluation correction if real LLM conclusions reverse under a crossed
design.

## 3. Crossed error-bank design

For generator (g), corrector (c), item (x), erroneous trace (e), and presentation
role (r), measure

\[
Y_{g,c,x,e,r}=1\{\text{corrected final answer}\}.
\]

The minimum credible design crosses every retained error with every corrector:

1. generate multiple verifiably wrong traces from each model on a shared item pool;
2. retain error content before knowing correction outcomes;
3. present the same byte-identical error to all correctors;
4. randomize assistant-history, user-quoted, and tool-output wrappers separately, without
   describing an off-diagonal trace as genuinely produced by the current corrector;
5. fit item and error fixed effects, with generator, corrector, and role interactions;
6. report both the deployment diagonal (g=c) and standardized rows/columns on a common
   error distribution.

The crossed matrix separates three quantities that ordinary self-correction rates mix:

- **production selectivity:** which errors survive each generator;
- **repair competence:** which fixed errors each corrector can repair;
- **ownership/role gating:** whether the same content is trusted differently when framed
  as the model's own state or an external claim.

### What the diagonal cannot identify

Even under the restrictive additive model

\[
\operatorname{logit}M_{g,c}=\alpha_c-\beta_g,
\]

the deployment diagonal reveals only \(\alpha_m-\beta_m\). For any proposed sequence of
corrector abilities \(\{\alpha_m\}\), one can choose generator-tail difficulties
\(\{\beta_m\}\) that produces exactly the same observed diagonal. Therefore neither the
sign nor the magnitude of correction-capability scaling is identified from diagonal
data alone. A crossed matrix identifies corrector and generator main effects up to the
usual additive constant; its residuals then provide a direct test of relational depth.

## 4. Strongest collisions

- *Decomposing LLM Self-Correction* reports the motivating accuracy-correction paradox
  but compares correction on model-specific error cohorts and interprets the pattern as
  stronger models making deeper errors.
- *Self-Correction Bench* already holds error content fixed across internal and external
  presentation and identifies a large ownership/activation effect. It is a mandatory
  baseline and blocks any novelty claim based only on self-versus-other correction.
- *The Self-Correction Illusion* further isolates conversational role labels with
  byte-identical claims. Role randomization is therefore a control, not a contribution.
- *LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location*
  separates detection from correction. Error-location hints must be crossed rather than
  treated as a new mechanism.
- *Detection Without Correction* decomposes downstream response at matched benchmark
  difficulty, but it does not by itself identify capability scaling under endogenous
  model-specific failure cohorts.

No located work explicitly performs a generator-by-corrector crossed design to test
whether the reported capability--correction inverse scaling reverses after standardizing
the error distribution. This negative-space claim remains provisional.

## 5. One-day kill test

Use a single open within-family ladder first, for example four Qwen sizes that fit the
available 4090s, and two mechanically checked domains.

1. Sample 200--300 shared items from GSM8K and a frozen MATH-500 subset.
2. Generate up to three initial traces per item and model at frozen decoding settings.
3. Retain verifiably incorrect final answers; do not use an LLM judge for the primary
   label.
4. Construct a balanced bank across generator and item-difficulty strata.
5. Send every retained error to every corrector under two byte-identical role wrappers.
6. Compare the model's own-failure rate with standardized direct adjustment, common-item
   intersection, and an item/error fixed-effect model.

Automatic `KILL` if any holds:

- standardized correction rankings have the same direction and similar magnitude as the
  own-failure rankings;
- generator identity adds no explanatory power after item and trace observables;
- the apparent reversal is entirely a known role-label effect;
- fewer than two model sizes have enough errors for a balanced common bank;
- the result fails on a second domain or under an independently generated error bank.

## 6. Relational error depth: the only Oral-level residual

Selection-induced reversal alone is an evaluation audit. The stronger residual is that
error difficulty may not be a scalar property of the error. Let the standardized repair
matrix be

\[
M_{g,c}=P(\text{repair}\mid\text{error generated by }g,\text{ corrector }c),
\]

with the exact error content and presentation role held fixed across correctors. A scalar
difficulty model predicts an additive logit structure

\[
\operatorname{logit}P(\text{repair}_{e,c})=v_e+\alpha_c.
\]

The interesting alternative contains a stable relational residual

\[
\operatorname{logit}P(\text{repair}_{e,c})=v_e+\alpha_c+\eta_{g(e),c},
\]

where, for example, same-family or shared-post-training correctors have a penalty on the
generator's characteristic errors. A weaker but complementary corrector can then repair an
error that a stronger related model cannot.

This is adjacent to, but not identical with, correlated model errors and same-family
LLM-judge bias. *Correlated Errors in Large Language Models* shows that shared providers
and architectures induce common mistakes and that same-family judges can inflate model
accuracy. It does not test actual correction of a byte-identical erroneous trace or
separate error production, repair competence, and ownership. That paper is nevertheless a
mandatory mechanism foundation and may fully explain any observed family interaction.

The relational claim is killed if a model with error-instance fixed effects and corrector
skill leaves no reproducible generator-family-by-corrector-family interaction. If it
survives, an equal-call-budget router selected for complementarity must beat always using
the largest model, a random heterogeneous corrector, and an error-type router.

## 7. Oral threshold

A single correction-rate reversal is not enough. An Oral-level result would require:

1. at least two published-looking inverse or non-monotone post-failure scaling conclusions
   reverse after standardization;
2. a general identification statement showing what deployment-diagonal data can and
   cannot recover;
3. a reusable crossed evaluation protocol and public error bank;
4. a stable relational error-depth interaction beyond global error difficulty, correlated
   errors, and known same-family judge preference;
5. an operational consequence: a complementarity router that improves fixed-budget
   end-to-end accuracy over the largest corrector and heterogeneous-ensemble baselines.

The honest current estimate is higher than for trajectory fault gain, but still below an
active paper seed until the direct-collision audit and small crossed pilot pass.
