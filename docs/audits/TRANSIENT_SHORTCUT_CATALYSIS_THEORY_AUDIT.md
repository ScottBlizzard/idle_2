# Transient Shortcut Catalysis: Hostile Theory, Novelty, and Significance Audit

**Audit date:** 2026-08-29  
**Repository:** [ScottBlizzard/idle_2](https://github.com/ScottBlizzard/idle_2)  
**Requested destination:** `D:\ICLR_2\TRANSIENT_SHORTCUT_CATALYSIS_THEORY_AUDIT.md`  
**Execution constraint:** No experiment was run; no GPU was touched. In particular, physical GPUs 0–7 and all foreign processes were left untouched.

## Source order and scope

The following repository files were read first, in the requested order, before older material was consulted:

1. [`docs/theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md`](https://github.com/ScottBlizzard/idle_2/blob/main/docs/theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md)
2. [`analysis/transient_shortcut_phase_transition/README.md`](https://github.com/ScottBlizzard/idle_2/blob/main/analysis/transient_shortcut_phase_transition/README.md)
3. [`analysis/transient_shortcut_phase_transition/explore_catalytic_ode.py`](https://github.com/ScottBlizzard/idle_2/blob/main/analysis/transient_shortcut_phase_transition/explore_catalytic_ode.py)
4. [`analysis/transient_shortcut_phase_transition/explore_xor.py`](https://github.com/ScottBlizzard/idle_2/blob/main/analysis/transient_shortcut_phase_transition/explore_xor.py)
5. [`docs/audits/ORAL_SEED_LITERATURE_ROLE_REAUDIT.md`](https://github.com/ScottBlizzard/idle_2/blob/main/docs/audits/ORAL_SEED_LITERATURE_ROLE_REAUDIT.md)
6. [`docs/current/CURRENT_STATUS.md`](https://github.com/ScottBlizzard/idle_2/blob/main/docs/current/CURRENT_STATUS.md)

Older repository material was not used to revive closed MoE, bracket-steering, planning, uncertainty, operator-interference, or related rejected seeds.

---

# 1. Executive verdict

## Terminal verdict

# **HOLD_REQUIRES_GENERAL_LAW**

The scalar theorem is **mathematically repairable** and does establish a real asymptotic optimization separation: under one deliberately favorable shared multiplicative bottleneck, clean-only learning remains near its small-initialization plateau for a logarithmic horizon, permanent shortcut training never learns the deployment path, and shortcut exposure followed by removal can make deployment learning succeed within the same logarithmic horizon.

That result is not yet an ICLR Oral-level scientific law. The current narrative makes three claims that the proof does not support:

1. **There is no intrinsic upper withdrawal boundary in the scalar state.** Continued shortcut exposure does not poison or erase the catalytic state. After arbitrarily long shortcut training, an additional fresh \(O(\log(1/\varepsilon))\) clean window still succeeds. The stated “late boundary” is only a remaining-budget boundary.
2. **The proved trigger is not near shortcut saturation.** For the theorem's \(\bar v\le 1/4\), the shortcut output is bounded by \(21/128\), so its residual is at least \(107/128\). The proof withdraws after reaching a constant-scale shared state, not near saturation.
3. **Permanent exposure is not proved harmful relative to clean-only learning at the matched logarithmic horizon.** Both fail, but the permanent trajectory can retain a larger deployment output, of order \(\varepsilon^2\), than the clean trajectory's order \(\varepsilon^3\). The theorem is “transient succeeds while two controls fail,” not a positive/neutral/negative phase law.

No primary paper located through 2026-08-29 proves the exact shared-bottleneck clean/permanent/transient asymptotic separation. Therefore the seed is **not rejected for direct collision**. However, essentially every surrounding ingredient is already occupied: shortcut-first dynamics, gradient starvation, privileged training-only signals, staged removal, bias-first debiasing, gradient-based auxiliary-task gating, dynamic curricula, critical periods, and teacher-signal annealing. The irreducible residual would have to be a theorem that a temporary, test-time-invalid signal can **durably improve the future clean vector field**, with a prospective statistic that predicts positive, zero, and negative transfer beyond ordinary gradient alignment or Relative Transfer.

## Claim status at a glance

| Candidate statement | Audit status | Binding interpretation |
|---|---|---|
| Exact gradient flows | **Correct** | Gradients and signs are correct for full-batch continuous-time gradient flow on squared loss. |
| Core and shortcut invariants | **Correct** | Both conserved quantities re-derive exactly. |
| Exact identity \(u(v)\) | **Correct** | \(u=\varepsilon e^{2(v-\varepsilon)}\) follows from \(d(\log u-2v)/dt=0\). |
| Shortcut no-crossing and boundedness | **Correct after explicit global argument** | The shortcut output remains below one; parameters are globally bounded. |
| Clean-only logarithmic-horizon lower bound | **Correct, and can be strengthened** | For \(t\le 1/(4\varepsilon)\), deployment loss is at least \(1/2-8\varepsilon^3\). |
| Permanent-shortcut deployment failure | **Correct** | Uniformly over all shortcut-training times, deployment loss is \(1/2-O(\varepsilon^2)\). |
| Threshold time \(\Theta(\log(1/\varepsilon))\) | **Correct with explicit constants** | \((2/3)\log(\bar v/\varepsilon)\le \tau_{\bar v}\le(4/3)\log(\bar v/\varepsilon)\). |
| Post-withdrawal \(O(\log(1/\varepsilon)+\log(1/\delta))\) | **Correct after repairing the proof** | A two-phase argument is required; the note's single \(c_\delta\) line does not itself prove logarithmic dependence on \(1/\delta\). |
| Common total horizon | **Correct for gradient-flow time/update horizon** | The repaired theorem uses exactly one common \(T_\varepsilon\). It does not match exact FLOPs. |
| “Withdrawal near saturation” | **Not proved** | The formal threshold is far from saturation. |
| “Late exposure becomes intrinsically harmful” | **Not proved and false in this scalar system** | Only the amount of clean time left becomes insufficient. |
| General help/neutral/harm law | **Absent** | The scalar architecture hard-wires the positive case. |
| XOR state trigger | **Weak exploratory evidence only** | Four correlations, ten seeds, post-hoc threshold selection, tiny loss gains, saturated accuracy; no preregistered law. |
| ICLR Oral significance | **Not yet** | Requires a general rate-transfer theorem and prospective negative controls before any natural-task experiment. |

---

# 2. Corrected formal theorem and proof audit

## 2.1 Model and hidden assumptions

The deployment/core model is

\[
f_c(a,u)=a u^2,
\qquad
L_c(a,u)=\frac12(1-a u^2)^2.
\]

The shortcut-exposed training model is

\[
f_s(a,u,v)=a(u^2+v),
\qquad
L_s(a,u,v)=\frac12(1-a(u^2+v))^2.
\]

Both start from

\[
a(0)=u(0)=v(0)=\varepsilon>0.
\]

The theorem relies on all of the following assumptions:

- a scalar target exactly equal to \(1\);
- population/full-batch squared loss;
- deterministic continuous-time gradient flow;
- no stochastic gradient noise, momentum, weight decay, normalization, clipping, or finite-step instability;
- exactly equal, positive, small initialization for all three parameters;
- an explicitly shared multiplicative parameter \(a\) between the deployment and shortcut paths;
- an even core parameterization \(u^2\), so the sign of \(u\) is irrelevant but the sign of \(a\) is decisive;
- direct observability of the shortcut-specific state \(v\) for the trigger;
- matched gradient-flow time, not matched exact arithmetic cost;
- deployment evaluation after deleting \(v\), without any shortcut available at test time.

The sign assumption is scientifically material. Linearizing the shortcut phase near the origin and ignoring the higher-order \(u^2\) term gives

\[
\dot a\approx v,\qquad \dot v\approx a.
\]

The growing mode is \(a+v\propto e^t\). Positive equal initialization selects the favorable positive branch. If \(a_0+v_0<0\), the growing mode drives \(a\) negative, making the deployment output \(a u^2\) point in the wrong direction. If \(a_0=-v_0\), the growing mode is absent. Standard symmetric random initialization is therefore not covered.

## 2.2 Gradient flows

Let

\[
e_c=1-a u^2,
\qquad
e_s=1-a(u^2+v).
\]

The clean/core gradient flow is

\[
\dot a=e_c u^2,
\qquad
\dot u=2e_c a u,
\qquad
\dot v=0.
\]

The shortcut-exposed gradient flow is

\[
\dot a=e_s(u^2+v),
\qquad
\dot u=2e_s a u,
\qquad
\dot v=e_s a.
\]

These equations are correct.

## 2.3 Exact invariants

### Core phase

\[
\frac{d}{dt}\left(a^2-\frac12u^2\right)
=2a(e_cu^2)-u(2e_cau)=0.
\]

With equal initialization,

\[
\boxed{a^2-\frac12u^2=\frac12\varepsilon^2.}
\]

Equivalently,

\[
a^2=\frac12(u^2+\varepsilon^2).
\]

### Shortcut phase

\[
\begin{aligned}
\frac{d}{dt}\left(a^2-v^2-\frac12u^2\right)
&=2ae_s(u^2+v)-2v(e_sa)-u(2e_sau)\\
&=0.
\end{aligned}
\]

Thus

\[
\boxed{a^2-v^2-\frac12u^2=-\frac12\varepsilon^2,}
\]

or

\[
a^2=v^2+\frac12u^2-\frac12\varepsilon^2.
\]

Because the shortcut residual will remain positive and \(u\ge\varepsilon\), this implies the useful stronger inequality

\[
\boxed{a\ge v.}
\]

The theory note only needs a weaker constant-factor bound, but the exact relation is available.

## 2.4 Exact shortcut relation \(u(v)\)

During shortcut training,

\[
\frac{d}{dt}(\log u-2v)
=\frac{\dot u}{u}-2\dot v
=2e_sa-2e_sa=0.
\]

Therefore

\[
\boxed{u(v)=\varepsilon\exp(2(v-\varepsilon)).}
\]

This identity does not require an informal division by \(\dot v\); it follows as a conserved quantity and remains valid globally along the positive solution.

## 2.5 Monotonicity, no crossing, and global boundedness

Let

\[
z_s=a(u^2+v).
\]

Then

\[
\begin{aligned}
\dot z_s
&=\dot a(u^2+v)+a(2u\dot u+\dot v)\\
&=(1-z_s)\left[(u^2+v)^2+a^2(1+4u^2)\right].
\end{aligned}
\]

Writing

\[
Q_s=(u^2+v)^2+a^2(1+4u^2)>0,
\]

we have

\[
\frac{d}{dt}(1-z_s)=-(1-z_s)Q_s,
\]

and hence, for every finite time on the maximal solution,

\[
1-z_s(t)=(1-z_s(0))\exp\left(-\int_0^t Q_s(r)\,dr\right)>0.
\]

For sufficiently small \(\varepsilon\), \(z_s(0)=\varepsilon^2+\varepsilon^3<1\). Thus the shortcut output cannot cross one, \(e_s>0\), and \(a,u,v\) are all increasing.

Global existence needs a separate boundedness argument. Since \(a\ge v\) and \(z_s>a v\),

\[
v^2\le av<1,
\]

so \(v<1\). The exact identity then yields

\[
u\le \varepsilon e^{2(1-\varepsilon)}\le e^2\varepsilon.
\]

If \(\varepsilon\le1/4\), the shortcut invariant gives

\[
a^2
=v^2+\frac12(u^2-\varepsilon^2)
<1+\frac{e^4}{32}.
\]

Define

\[
A_*:=\sqrt{1+\frac{e^4}{32}}.
\]

Then shortcut trajectories satisfy

\[
0<a\le A_*,\qquad 0<u\le e^2\varepsilon,\qquad 0<v<1
\]

uniformly over all training times. This closes the no-crossing argument and proves global existence.

## 2.6 Permanent-shortcut deployment bound

The deployment output while training permanently on \(L_s\) is

\[
y_c=a u^2.
\]

Using the global bounds,

\[
0\le y_c\le A_*e^4\varepsilon^2.
\]

Let

\[
C_p:=A_*e^4.
\]

Then, uniformly over every shortcut-training horizon \(t\ge0\),

\[
\boxed{
\frac12-C_p\varepsilon^2
\le L_c(t)
\le\frac12.
}
\]

The upper bound uses \(0\le y_c<1\); the lower bound follows from

\[
\frac12(1-y_c)^2=\frac12-y_c+\frac12y_c^2\ge\frac12-y_c.
\]

This correctly proves permanent-shortcut deployment failure as \(\varepsilon\to0\). It does **not** prove that permanent exposure is worse than clean-only exposure at the same logarithmic horizon.

At full shortcut convergence, one can sharpen the picture. Since \(u=O(\varepsilon)\), the invariant gives \(a-v\to0\), while \(a(v+u^2)\to1\); hence \(a,v\to1\), \(u/\varepsilon\to e^2\), and

\[
a u^2\sim e^4\varepsilon^2.
\]

Thus permanent exposure leaves a small but larger deployment signal than the \(O(\varepsilon^3)\) clean signal at logarithmic time. It starves the deployment path in the sense of failing to make it non-vanishing, not in the stronger sense of making it worse than clean-only at that horizon.

## 2.7 Threshold existence and time scaling

Fix

\[
0<\bar v\le\frac14,
\qquad 0<\varepsilon<\bar v.
\]

Let \(\tau_{\bar v}\) be the first time \(v=\bar v\). For \(v\in[\varepsilon,\bar v]\),

\[
u^2=\varepsilon^2e^{4(v-\varepsilon)}\le e\varepsilon^2.
\]

The invariant implies

\[
v\le a
\le \sqrt{\frac{e+1}{2}}\,v
<\frac32v.
\]

Also, using \(e<3\),

\[
\begin{aligned}
z_s
&=a(v+u^2)\\
&\le \frac32v(v+3v^2)\\
&\le \frac{21}{128}<\frac14.
\end{aligned}
\]

Therefore \(e_s=1-z_s\ge3/4\), and

\[
\frac34v\le\dot v=e_sa\le\frac32v.
\]

Integration gives the explicit threshold bounds

\[
\boxed{
\frac23\log\frac{\bar v}{\varepsilon}
\le \tau_{\bar v}
\le \frac43\log\frac{\bar v}{\varepsilon}.
}
\]

This is the claimed logarithmic amplification time. It also shows why “near saturation” is inaccurate: throughout the theorem's trigger interval, the shortcut residual remains at least \(107/128\).

At withdrawal,

\[
\boxed{u_\tau=\varepsilon e^{2(\bar v-\varepsilon)}}
\]

and

\[
\boxed{a_\tau^2=\bar v^2+\frac12(u_\tau^2-\varepsilon^2).}
\]

## 2.8 Post-withdrawal invariant and convergence

After switching to the clean objective, the new core invariant is determined by the switch state:

\[
\begin{aligned}
d_\tau
&:=a_\tau^2-\frac12u_\tau^2\\
&=\bar v^2-\frac12\varepsilon^2.
\end{aligned}
\]

If \(\varepsilon\le\bar v\), then

\[
d_\tau\ge\frac12\bar v^2,
\qquad
 a(t)\ge c:=\frac{\bar v}{\sqrt2}
\]

for the entire clean phase.

Let

\[
y=a u^2.
\]

Under clean flow,

\[
\dot y=(1-y)(u^4+4a^2u^2).
\]

Because \(y(\tau)<1\), it remains below one and increases monotonically.

### Phase I: reach a constant deployment margin

As long as \(y\le1/2\),

\[
\frac{d}{dt}\log u=2(1-y)a\ge c.
\]

Define

\[
U:=(2c)^{-1/2}.
\]

If \(u\ge U\), then \(y=a u^2\ge cU^2=1/2\). Therefore the time required to reach \(y\ge1/2\) is at most

\[
\boxed{
t_1\le c^{-1}\log_+\frac{U}{u_\tau}.
}
\]

### Phase II: exponential residual contraction

Let \(r=1-y\). Once \(y\ge1/2\),

\[
\dot r=-r(u^4+4a^2u^2).
\]

Moreover,

\[
u^4+4a^2u^2\ge4ay\ge2c.
\]

Hence

\[
r(s)\le\frac12e^{-2cs},
\qquad
L_c(s)=\frac12r(s)^2\le\frac18e^{-4cs}.
\]

The additional time required to reach \(L_c\le\delta\) is at most

\[
\boxed{
t_2\le\frac{1}{4c}\log_+\frac{1}{8\delta}.
}
\]

Thus the post-withdrawal duration is bounded by

\[
\boxed{
t_{\mathrm{post}}
\le
c^{-1}\log_+\frac{U}{u_\tau}
+\frac{1}{4c}\log_+\frac{1}{8\delta}.
}
\]

Since \(u_\tau\ge\varepsilon\), this is

\[
O_{\bar v}\!\left(\log\frac1\varepsilon+\log\frac1\delta\right).
\]

This two-phase proof is the required repair. The note's argument “\(d\log u/dt\ge c_\delta\) until loss \(\delta\)” is enough when \(\delta\) is treated as a fixed constant, but by itself it does not justify a uniform logarithmic dependence on \(1/\delta\); its lower rate deteriorates as \(\sqrt\delta\).

## 2.9 Clean-only lower bound

For clean-only training, let \(y=a u^2\). Then

\[
\dot y=(1-y)(u^4+4a^2u^2),
\]

so \(y<1\) and \(u\ge\varepsilon\). The core invariant gives

\[
a^2=\frac12(u^2+\varepsilon^2)\le u^2,
\]

hence \(a\le u\). Therefore

\[
\dot u=2(1-y)au\le2u^2.
\]

Comparison with \(\dot w=2w^2\), \(w(0)=\varepsilon\), gives

\[
u(t)\le\frac{\varepsilon}{1-2\varepsilon t}
\]

while the denominator is positive. For

\[
t\le\frac{1}{4\varepsilon},
\]

we obtain

\[
u(t)\le2\varepsilon,
\qquad a(t)\le2\varepsilon,
\qquad y(t)\le8\varepsilon^3.
\]

Consequently,

\[
\boxed{
\frac12-8\varepsilon^3
\le L_c^{\mathrm{clean}}(t)
\le\frac12,
\qquad t\le\frac{1}{4\varepsilon}.
}
\]

This is stronger than merely saying the clean loss is \(1/2-o(1)\) at a logarithmic horizon. It also makes clear that clean escape is on an inverse-initialization scale, not a logarithmic scale.

## 2.10 Repaired matched-horizon theorem with explicit constants

Define

\[
\log_+(x):=\max\{0,\log x\}.
\]

### Theorem: matched-horizon transient shortcut separation

Fix any

\[
\bar v\in(0,1/4],
\qquad
\delta\in(0,1/2).
\]

Let

\[
c=\frac{\bar v}{\sqrt2},
\qquad
U=(2c)^{-1/2},
\]

\[
B_{\bar v,\delta}
=
\frac1c\log_+U
+
\frac{1}{4c}\log_+\frac{1}{8\delta},
\]

and

\[
K_{\bar v,\delta}
=
\frac43+rac1c+B_{\bar v,\delta}.
\]

Let

\[
A_* = \sqrt{1+\frac{e^4}{32}},
\qquad
C_p=A_*e^4.
\]

A sufficient explicit small-initialization threshold is

\[
\varepsilon_0
=
\min\left\{
\bar v,
\frac14,
e^{-1},
\frac{1}{16K_{\bar v,\delta}^2},
\left(\frac{1/2-\delta}{16}\right)^{1/3},
\sqrt{\frac{1/2-\delta}{2C_p}}
\right\}.
\]

For every \(0<\varepsilon<\varepsilon_0\), define the **common** horizon

\[
T_\varepsilon
=K_{\bar v,\delta}\log\frac1\varepsilon.
\]

Compare the following three trajectories from the same initialization and in the same parameterization \((a,u,v)\):

1. **Clean-only:** train on \(L_c\) for all \(T_\varepsilon\), with \(v\) frozen.
2. **Permanent shortcut:** train on \(L_s\) for all \(T_\varepsilon\).
3. **Transient shortcut:** train on \(L_s\) until the first time \(v=\bar v\), then train on \(L_c\) until \(T_\varepsilon\).

Then

\[
\boxed{L_c^{\mathrm{transient}}(T_\varepsilon)\le\delta,}
\]

while

\[
\boxed{
\frac12-8\varepsilon^3
\le L_c^{\mathrm{clean}}(T_\varepsilon)
\le\frac12,
}
\]

and

\[
\boxed{
\frac12-C_p\varepsilon^2
\le L_c^{\mathrm{permanent}}(T_\varepsilon)
\le\frac12.
}
\]

In particular, the clean and permanent controls both have loss greater than \(\delta\), whereas the transient trajectory reaches loss at most \(\delta\).

### Proof sketch with all budget terms

The shortcut threshold satisfies

\[
\tau_{\bar v}\le\frac43\log\frac1\varepsilon.
\]

The post-withdrawal bound is

\[
t_{\mathrm{post}}
\le
\frac1c\log\frac1\varepsilon+B_{\bar v,\delta}.
\]

Since \(\log(1/\varepsilon)\ge1\),

\[
\tau_{\bar v}+t_{\mathrm{post}}
\le K_{\bar v,\delta}\log\frac1\varepsilon=T_\varepsilon.
\]

The loss remains non-increasing after reaching \(\delta\). The condition \(\varepsilon\le1/(16K^2)\), together with \(\log(1/\varepsilon)\le\varepsilon^{-1/2}\), ensures

\[
T_\varepsilon\le\frac{1}{4\varepsilon},
\]

so the clean lower bound applies. The remaining two components of \(\varepsilon_0\) make the clean and permanent lower bounds strictly larger than \(\delta\).

### What “matched” means

The theorem genuinely uses one total gradient-flow horizon \(T_\varepsilon\) for all methods and one parameterization. It therefore matches idealized optimization time and, under an Euler discretization with common step size, matches the number of updates. It does **not** exactly match arithmetic operations, because evaluating and differentiating the shortcut branch incurs extra work. Any natural-task experiment would have to match examples, optimizer steps, and either FLOPs or explicitly report the small additional shortcut cost.

## 2.11 Late-withdrawal lemma: correct but misinterpreted

Suppose shortcut training runs for an arbitrary duration and is then followed by a clean interval of length \(s_\varepsilon\). At the switch,

\[
a_s\le A_*,
\qquad
u_s\le e^2\varepsilon.
\]

During the clean phase the invariant gives

\[
a^2=a_s^2-\frac12u_s^2+\frac12u^2\le A_*^2+\frac12u^2.
\]

Let

\[
B_*:=\sqrt{A_*^2+1/2}.
\]

As long as \(u\le1\),

\[
\frac{d}{dt}\log u=2(1-au^2)a\le2B_*.
\]

If

\[
s_\varepsilon=o\!\left(\log\frac1\varepsilon\right),
\]

then a bootstrap gives

\[
u_{\mathrm{end}}
\le e^2\varepsilon e^{2B_*s_\varepsilon}
=\varepsilon^{1-o(1)}\to0,
\]

and therefore

\[
L_c\to\frac12.
\]

The lemma is valid. Its interpretation must be corrected:

- it is a **remaining-clean-time lower bound**;
- it is not evidence that the shortcut state becomes toxic;
- it is not a state-triggered upper phase boundary;
- it would hold for many warm starts whenever a non-vanishing deployment coordinate still needs logarithmic amplification.

Indeed, if the shortcut has ever reached \(v\ge\bar v\), then at any later switch the post-clean invariant is

\[
a^2-\frac12u^2=v_s^2-\frac12\varepsilon^2
\ge\bar v^2-\frac12\varepsilon^2.
\]

The same \(O(\log(1/\varepsilon)+\log(1/\delta))\) post-clean guarantee still applies, no matter how long the shortcut was maintained. There is therefore **no intrinsic upper withdrawal boundary in the scalar model**.

## 2.12 Claims stronger than the proof

The following language must not appear as a theorem consequence without additional work:

- “withdrawal near shortcut saturation”;
- “the shortcut becomes harmful after a state phase transition”;
- “permanent exposure is worse than clean-only at the same logarithmic horizon”;
- “the trigger predicts the optimal withdrawal time”;
- “the theorem applies under random initialization”;
- “the same mechanism holds in ordinary deep networks”;
- “the exact three-way separation is a general law of transient supervision.”

The defensible theorem-level claim is narrower:

> In one positively initialized shared-multiplicative normal form, shortcut training can raise a shared state from \(O(\varepsilon)\) to \(\Theta(1)\) in logarithmic time while leaving the deployment-specific factor at \(O(\varepsilon)\); removing the shortcut then changes deployment learning from an inverse-initialization escape to a logarithmic escape, whereas never removing it leaves deployment output vanishing.

That statement is mathematically real. It is not yet a law.

---

# 3. Literature collision audit

## 3.1 Claim-by-claim occupancy map

| Candidate claim fragment | Prior art that already occupies it | Residual status |
|---|---|---|
| Easier/spurious features are learned first and can suppress harder invariant features | Gradient Starvation; Simplicity Bias; Complexity Matters; LaBonte–Muthukumar XOR theory; NTK eigenfunction analysis | **Occupied foundation.** Not novel by itself. |
| Training-only information can accelerate or improve the test-time model | LUPI; TRAM; auxiliary-modality learning; knowledge distillation; HiLL | **Occupied foundation and algorithms.** |
| Use an initially useful but later undesirable signal, then pivot/remove/reweight it | BAM; Learning from Failure; JTT; MaskTune; DFR; FeAT; scheduled sampling; DAgger | **Heavily occupied algorithmic pattern.** |
| Adapt the curriculum or auxiliary weight from training-state transfer | Du et al. gradient similarity; Graves et al. learning-progress curriculum; Ding–Ye Relative Transfer/TDCS | **Direct local-trigger collision.** |
| A curriculum can yield a provable optimization advantage | Weinshall et al.; Abbe–Cornacchia–Lotfi; continuation/homotopy work | **Occupied theorem class.** |
| Early exposure can permanently shape later multimodal learning | Critical-period literature | **Occupied temporal-mechanism foundation.** |
| Exact clean/permanent/transient shared-bottleneck asymptotic separation | No direct theorem located | **Potentially new but currently stylized.** |
| A prospective statistic predicts durable improvement of the *future clean vector field*, beyond current gradient transfer | No direct theorem located; closest pressure comes from Relative Transfer and NTK/plasticity work | **Narrow residual opportunity.** |
| A genuine positive/neutral/negative state law with an intrinsic upper withdrawal boundary | Not established by the scalar theorem; XOR evidence is post hoc | **Missing.** |

## 3.2 Role definitions

- **DIRECT THEOREM COLLISION:** already proves essentially the same mathematical statement and mechanism.
- **DIRECT ALGORITHMIC COLLISION:** already implements the same operational strategy or trigger, even if its theorem differs.
- **POSITIVE ADVERSARY:** a nearby result that supports plausibility but raises the novelty or generality bar.
- **MECHANISM FOUNDATION:** owns an ingredient that must be credited rather than claimed.
- **MANDATORY BASELINE:** must be experimentally compared if the project later reaches a natural-task stage.
- **UNEXPLAINED ANOMALY:** a serious negative or opposite phenomenon that the proposed law must predict.

No work below is classified as a direct theorem collision with the repaired scalar separation.

## 3.3 Primary-literature collision matrix

| Work | Exact primary scope | Role | Collision judgment |
|---|---|---|---|
| [Tyler LaBonte & Vidya Muthukumar, **“SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model”** (arXiv, submitted 2026-06-29, rev. 2026-07-03)](https://arxiv.org/abs/2606.30444) | End-to-end analysis of online minibatch SGD with logistic loss for a two-layer ReLU network on Boolean-hypercube XOR plus a linear spurious feature. Proves exponential shortcut-first learning, coupled signal/spurious dynamics, suppression of the XOR signal, and phase transitions. | **POSITIVE ADVERSARY** | This is the strongest current theory neighbor. It owns shortcut-first exponential growth and signal suppression, but it does not prove that early removal beats clean-only or establish the clean/permanent/transient shared-state separation. |
| [Yongqiang Chen, Wei Huang, Kaiwen Zhou, Yatao Bian, Bo Han & James Cheng, **“Understanding and Improving Feature Learning for Out-of-Distribution Generalization”** (NeurIPS 2023)](https://arxiv.org/abs/2304.11327) | Shows ERM can learn both spurious and invariant features, with faster spurious learning under stronger correlation; OOD objectives rarely learn new features. Introduces FeAT, which retains and augments features iteratively. | **POSITIVE ADVERSARY** | Directly challenges any claim that ERM simply never learns the core. FeAT is a mandatory conceptual comparator for “retain useful state while forcing new features.” |
| [Zhikai Ding & Ziyi Ye, **“Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics”** (arXiv, 2026-08-18)](https://arxiv.org/abs/2608.17268) | Defines Relative Transfer from first-order gradient dynamics and derives Transfer-aware Dynamic Curriculum Sampling, adjusting difficulty sampling throughout LLM post-training. | **DIRECT ALGORITHMIC COLLISION** | A local “benefit minus lost clean step” trigger reduces exactly to its Relative Transfer boundary. Any claimed transition statistic must go beyond current-gradient transfer and predict durable future-rate change. |
| [Harsh Nilesh Pathak & Randy Paffenroth, **“Principled Curriculum Learning using Parameter Continuation Methods”** (2025; ICML 2025 Beyond First-Order Methods workshop)](https://arxiv.org/abs/2507.22089) | Connects curriculum learning to parameter continuation/homotopy and proposes theoretically justified continuation optimization for neural networks. | **MECHANISM FOUNDATION** | Occupies the broad “easy path reshapes optimization” story, but not training-only shortcut removal or shared-bottleneck starvation. |
| [Yu Xia, Canwen Xu, Zhewei Yao, Julian McAuley & Yuxiong He, **“Learning to Hint for Reinforcement Learning”** (arXiv, 2026-04-01)](https://arxiv.org/abs/2604.00698) | Jointly trains a hinter and GRPO reasoner. Defines hint reliance and proves lower reliance implies stronger transfer from hinted success to no-hint success; uses transfer-weighted rewards. | **DIRECT ALGORITHMIC COLLISION** | Occupies adaptive training-only hints whose utility is judged by no-hint transfer. The residual here must be a distinct optimization-catalysis theorem, not “hints help then disappear.” |
| [Kanghui Tian, Siyuan Liu, Ziang Yan, Sheng Xia, Shuai Dong & Yi Wang, **“ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation”** (arXiv, 2026-06-04)](https://arxiv.org/abs/2606.05718) | Replaces answer-side privileged teacher information with recoverable visual cues and an internal cue-recovery mechanism, preserving the inference interface while reducing train–test privilege mismatch. | **MANDATORY BASELINE** | A current privileged-supervision neighbor: it argues that the *recoverability and geometry* of the training-only cue matter, not merely its short-term usefulness. It does not prove transient optimization catalysis. |
| [Michael Kleinman, Alessandro Achille & Stefano Soatto, **“Critical Learning Periods for Multisensory Integration in Deep Networks”** (CVPR 2023 Highlight)](https://arxiv.org/abs/2210.04643) | Shows early correlated multisensory exposure can determine later integration; deep linear networks can have critical periods while shallow ones do not. Introduces source sensitivity. | **POSITIVE ADVERSARY** | Supports early-state path dependence but also supplies opposite temporal phenomena: temporary deprivation can cause irreversible harm. A general law must predict both. |
| [Jinwoo Lim, Suhyun Kim & Soo-Mook Moon, **“Shortcut Features as Top Eigenfunctions of NTK: A Linear Neural Network Case and More”** (NeurIPS 2025; arXiv posted 2026)](https://arxiv.org/abs/2602.03066) | Defines features as NTK eigenfunctions; shows imbalanced-cluster shortcut features can have larger eigenvalues and persist after training, with extensions to ReLU networks and ResNet-18. | **MECHANISM FOUNDATION** | Supports spectral-rate explanations for shortcut preference. It also makes the lazy/linear negative control mandatory: fixed-kernel learning should not exhibit the proposed representation catalyst. |
| [Mohammad Pezeshki, Sékou-Oumar Kaba, Yoshua Bengio, Aaron Courville, Doina Precup & Guillaume Lajoie, **“Gradient Starvation: A Learning Proclivity in Neural Networks”** (NeurIPS 2021)](https://arxiv.org/abs/2011.09468) | Dynamical-systems theory for feature imbalance when fitting one predictive feature suppresses gradients for others; proposes spectral decoupling. | **MECHANISM FOUNDATION** | Owns the starvation part of the story. Novelty cannot be claimed for “easy path fits the residual and suppresses the hard path.” |
| [Harshay Shah, Kaustav Tamuly, Aditi Raghunathan, Prateek Jain & Praneeth Netrapalli, **“The Pitfalls of Simplicity Bias in Neural Networks”** (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/hash/6cfe0e6127fa25df2a0ef2ae1067d915-Abstract.html) | Establishes the tendency of networks to rely on simpler predictive features, with synthetic and image evidence. | **MECHANISM FOUNDATION** | Occupies the broad simplicity-first explanation. |
| [GuanWen Qiu, Da Kuang & Surbhi Goel, **“Complexity Matters: Feature Learning in the Presence of Spurious Correlations”** (ICML 2024)](https://arxiv.org/abs/2403.03375) | Controls spurious-feature complexity/correlation; finds simpler or stronger spurious features slow core learning, subnetworks may specialize, and spurious features are not forgotten; analyzes one-hidden-layer ReLU XOR. | **POSITIVE ADVERSARY** | Very close on feature-time-scale mechanics. It raises the bar for claiming a new XOR/shortcut phase story and documents limitations of debiasing methods that exploit early spurious learning. |
| [Nihal Murali, Aahlad Puli, Ke Yu, Rajesh Ranganath & Kayhan Batmanghelich, **“Beyond Distribution Shift: Spurious Features Through the Lens of Training Dynamics”** (TMLR 2023)](https://arxiv.org/abs/2302.09344) | Defines harmful versus benign spurious features by relative learnability and detects harmful shortcuts from early-layer training dynamics. | **MECHANISM FOUNDATION** | Occupies state-based shortcut diagnostics and the claim that relative learning speed—not merely correlation—determines harm. |
| [Vladimir Vapnik & Rauf Izmailov, **“Learning Using Privileged Information: Similarity Control and Knowledge Transfer”** (JMLR 2015)](https://www.jmlr.org/papers/v16/vapnik15b.html) | Formalizes training-only privileged information and mechanisms that can accelerate student learning through similarity correction and direct transfer. | **MECHANISM FOUNDATION** | The broad “information absent at test time accelerates learning” claim is long occupied. |
| [Mark Collier, Rodolphe Jenatton, Effrosyni Kokiopoulou & Jesse Berent, **“Transfer and Marginalize: Explaining Away Label Noise with Privileged Information”** (ICML 2022)](https://proceedings.mlr.press/v162/collier22a.html) | TRAM transfers privileged information through weight sharing and marginalizes it at test time. | **DIRECT ALGORITHMIC COLLISION** | Directly occupies shared-parameter use of training-only features. It does not prove transient optimization catalysis, but it is a mandatory conceptual and empirical comparator. |
| [Yu Shen, Xijun Wang, Peng Gao & Ming Lin, **“Auxiliary Modality Learning with Generalized Curriculum Distillation”** (ICML 2023)](https://proceedings.mlr.press/v202/shen23f.html) | Selects auxiliary modalities and performs curriculum distillation when only the main modality is available at test time. | **DIRECT ALGORITHMIC COLLISION** | Direct neighbor for training-only modality schedules and optimizer-path explanations. |
| [Yunshu Du, Wojciech Czarnecki, Siddhant Jayakumar, Razvan Pascanu & Balaji Lakshminarayanan, **“Adapting Auxiliary Losses Using Gradient Similarity”** (arXiv 2018)](https://arxiv.org/abs/1812.02224) | Uses cosine similarity between main and auxiliary gradients to gate auxiliary losses; establishes convergence to main-task critical points under its conditions. | **DIRECT ALGORITHMIC COLLISION** | Occupies the obvious state-adaptive rule “use auxiliary gradients only while aligned.” |
| [Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman & Chelsea Finn, **“Gradient Surgery for Multi-Task Learning”** (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/hash/3fe78a8acf5fda99de95303940a2420c-Abstract.html) | PCGrad projects away conflicting task-gradient components. | **MANDATORY BASELINE** | Any natural auxiliary/shortcut experiment must compare against explicit conflict handling. |
| [Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone & Qiang Liu, **“Conflict-Averse Gradient Descent for Multi-task Learning”** (NeurIPS 2021)](https://proceedings.neurips.cc/paper/2021/hash/9d27fdf2477ffbff837d73ef7ae23db9-Abstract.html) | CAGrad optimizes average loss while regularizing worst local task improvement, with convergence guarantees. | **MANDATORY BASELINE** | Another required gradient-conflict comparator if a multi-objective implementation is used. |
| [Daphna Weinshall, Gad Cohen & Dan Amir, **“Curriculum Learning by Transfer Learning: Theory and Experiments with Deep Networks”** (ICML 2018)](https://proceedings.mlr.press/v80/weinshall18a.html) | Gives a convex linear-regression curriculum analysis and connects example difficulty/transfer to convergence, then evaluates CNN curricula. | **MECHANISM FOUNDATION** | Occupies transferability-based explanations for curriculum benefit. |
| [Emmanuel Abbe, Elisabetta Cornacchia & Aryo Lotfi, **“Provable Advantage of Curriculum Learning on Parity Targets with Mixed Inputs”** (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4c8ce3c63f6b66d6811c6d67c68e487b-Abstract-Conference.html) | Proves a curriculum advantage for parity targets with mixed input distributions. | **POSITIVE ADVERSARY** | Shows that asymptotic curriculum separations on parity-like targets are already possible; novelty must come from the training-only shared-bottleneck mechanism and its predictive law. |
| [Alex Graves, Marc G. Bellemare, Jacob Menick, Rémi Munos & Koray Kavukcuoglu, **“Automated Curriculum Learning for Neural Networks”** (ICML 2017)](https://proceedings.mlr.press/v70/graves17a.html) | Uses learning progress as a reward to a nonstationary bandit that selects curriculum components. | **DIRECT ALGORITHMIC COLLISION** | Occupies adaptive state/progress-based scheduling at the algorithmic level. |
| [Alessandro Achille, Matteo Rovere & Stefano Soatto, **“Critical Learning Periods in Deep Networks”** (ICLR 2019)](https://openreview.net/forum?id=BkeStsCcKQ) | Shows temporary early deficits can have lasting effects and that sensitivity depends on onset, duration, and width. | **MECHANISM FOUNDATION** | The proposed law must explain why some early exposures help while other temporary interventions irreversibly hurt. |
| [Jordan Ash & Ryan P. Adams, **“On Warm-Starting Neural Network Training”** (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/hash/288cd2567953f06e460a33951f55daaf-Abstract.html) | Demonstrates that warm starts can reduce wall-clock optimization yet impair generalization relative to fresh initialization. | **UNEXPLAINED ANOMALY** | Direct warning that an “amplified state” is not automatically beneficial. A law must distinguish optimization speed from plasticity/generalization damage. |
| [Shibhansh Dohare, J. Fernando Hernandez-Garcia, Qingfeng Lan, Parash Rahman, A. Rupam Mahmood & Richard S. Sutton, **“Loss of Plasticity in Deep Continual Learning”** (Nature 2024)](https://www.nature.com/articles/s41586-024-07711-7) | Shows across continual supervised and reinforcement-learning settings that prolonged training can reduce the ability to optimize subsequent objectives, accompanied by larger weights, dead/saturated units, and lower effective representation rank. | **UNEXPLAINED ANOMALY** | A durable state change can make later learning slower rather than faster. Any clean-rate law must predict this negative regime and cannot equate shared-state amplification with preserved plasticity. |
| [Junhyun Nam, Hyuntak Cha, Sungsoo Ahn, Jaeho Lee & Jinwoo Shin, **“Learning from Failure: Training Debiased Classifier from Biased Classifier”** (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/hash/eddc3427c5d77843c2253f1e799fe933-Abstract.html) | Exploits the fact that biased/easy features dominate early and uses a biased model's failures to train a debiased model. | **DIRECT ALGORITHMIC COLLISION** | Occupies “deliberately use early biased learning to enable later robust learning,” although with paired models rather than one shared bottleneck. |
| [Gaotang Li, Jiarui Liu & Wei Hu, **“Bias Amplification Enhances Minority Group Performance”** (TMLR; arXiv 2023/2024)](https://arxiv.org/abs/2309.06717) | BAM first amplifies bias using per-example auxiliary variables, then upweights errors and continues training the same model; includes a class-accuracy-gap stopping rule. | **DIRECT ALGORITHMIC COLLISION** | This is the closest algorithmic reduction: intentionally amplify a bad/easy signal, then pivot using a state rule. The scalar theorem must provide a distinct general mechanism, not just a cleaner toy for BAM-like staging. |
| [Evan Z. Liu, Behzad Haghgoo, Annie S. Chen, Aditi Raghunathan, Pang Wei Koh, Shiori Sagawa, Percy Liang & Chelsea Finn, **“Just Train Twice”** (ICML 2021)](https://proceedings.mlr.press/v139/liu21f.html) | Stage one identifies likely minority/error examples; stage two upweights them without full group labels. | **MANDATORY BASELINE** | Required two-stage robustness baseline. |
| [Saeid Asgari, Aliasghar Khani, Fereshte Khani, Ali Gholami, Linh Tran, Ali Mahdavi Amiri & Ghassan Hamarneh, **“MaskTune”** (NeurIPS 2022)](https://proceedings.neurips.cc/paper_files/paper/2022/hash/93be245fce00a9bb2333c17ceae4b732-Abstract-Conference.html) | Masks features already used by the trained model and fine-tunes to force exploration of alternatives. | **MANDATORY BASELINE** | Required “learn easy feature, then remove access and learn another” comparator. |
| [Polina Kirichenko, Pavel Izmailov & Andrew Gordon Wilson, **“Last Layer Re-Training is Sufficient for Robustness to Spurious Correlations”** (ICLR 2023)](https://openreview.net/forum?id=THOOBy1uWVH) | Shows ERM representations can contain useful core features and that retraining the last layer on balanced data can yield robustness. | **MANDATORY BASELINE** | Challenges any claim that shortcut training necessarily prevents useful core representation learning. |
| [Haotian Ye, James Zou & Linjun Zhang, **“Freeze then Train: Towards Provable Representation Learning under Spurious Correlations and Feature Noise”** (AISTATS 2023)](https://proceedings.mlr.press/v206/ye23a.html) | Gives theory showing when spurious/noisy features impede representation learning and proposes freezing salient unsupervised features before supervised training. | **POSITIVE ADVERSARY** | A provable two-phase representation-learning neighbor that raises the theoretical bar. |
| [Andrew Saxe, James McClelland & Surya Ganguli, **“Exact Solutions to the Nonlinear Dynamics of Learning in Deep Linear Neural Networks”** (ICLR 2014)](https://arxiv.org/abs/1312.6120) | Derives exact deep-linear learning dynamics, stage-like transitions, plateaus, and depth-dependent time scales. | **MECHANISM FOUNDATION** | Small-initialization plateaus and multiplicative time-scale separation are not new ingredients. |
| [Enric Boix-Adsera, Etai Littwin, Emmanuel Abbe, Samy Bengio & Joshua Susskind, **“Transformers Learn Through Gradual Rank Increase”** (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4d69c1c057a8bd570ba4a7b71aae8331-Abstract-Conference.html) | Analyzes stage-like rank growth and saddle-to-saddle dynamics in transformers. | **MECHANISM FOUNDATION** | Supports broader slow-manifold/escape interpretations but does not provide transient shortcut catalysis. |
| [Samy Bengio, Oriol Vinyals, Navdeep Jaitly & Noam Shazeer, **“Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks”** (NeurIPS 2015)](https://proceedings.neurips.cc/paper/2015/hash/e995f98d56967d946471af29d7bf99f1-Abstract.html) | Gradually replaces ground-truth previous tokens with model-generated tokens during training. | **DIRECT ALGORITHMIC COLLISION** | Occupies scheduled removal of a training-only teacher signal. Its domain and objective differ, but the broad operational pattern is not new. |
| [Alex Lamb et al., **“Professor Forcing”** (NeurIPS 2016)](https://arxiv.org/abs/1610.09038) | Adversarially aligns teacher-forced and free-running recurrent dynamics. | **MANDATORY BASELINE** | Relevant whenever the natural bridge uses train/test conditioning mismatch. |
| [Stéphane Ross, Geoffrey Gordon & Drew Bagnell, **“A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning”** (AISTATS 2011)](https://proceedings.mlr.press/v15/ross11a.html) | DAgger iteratively mixes expert supervision with learner-induced states to remove train/test distribution mismatch. | **DIRECT ALGORITHMIC COLLISION** | Occupies progressive withdrawal/mixing of teacher guidance under a deployment-policy objective. |
| [Syed Muhammad Raza, Omer Tariq & Jeongbae Son, **“Anti-Shortcut Distillation via Temporal Negative Knowledge Transfer”** (arXiv, 2026-08-12, rev. 2026-08-14)](https://arxiv.org/abs/2608.11789) | Uses early-teacher versus final-teacher feature trajectories to identify shortcut directions and pushes the student away from them. | **MANDATORY BASELINE** | A current temporal-shortcut method that makes trajectory-based shortcut diagnostics a required comparator, although it suppresses rather than temporarily exploits shortcuts. |

## 3.4 Literature conclusion

The exact theorem is not directly occupied. The paper cannot, however, sell any of the following as its main novelty:

- shortcuts are learned faster;
- easy features starve hard features;
- privileged features can help training and disappear at test time;
- curricula can accelerate optimization;
- biased learning can be exploited in a two-stage method;
- a gradient-alignment statistic can decide when auxiliary training helps;
- teacher signals can be scheduled or removed;
- early training states can have lasting effects.

The only plausible theorem-level residual is:

> A prospectively measurable change in the learner's representation or tangent geometry, induced by a test-time-invalid signal, predicts a durable increase or decrease in the subsequent clean-task contraction/escape rate after the signal is removed, and this prediction remains nontrivial after matching current gradient transfer.

That statement is not yet proved.

---

# 4. General-law attempt

## 4.1 Exact switching-time sensitivity for two vector fields

Let

\[
F(\theta)=-\nabla L_c(\theta)
\]

be the clean vector field and

\[
H(\theta)=-\nabla L_s(\theta)
\]

be the shortcut-exposed vector field. Let \(\Phi_F^t\) and \(\Phi_H^t\) denote their flows. For a fixed total horizon \(T\) and one switch at time \(\tau\), define

\[
J_T(\tau)
=L_c\!\left(
\Phi_F^{T-\tau}(\Phi_H^\tau(\theta_0))
\right).
\]

Let

\[
x_\tau=\Phi_H^\tau(\theta_0),
\qquad
y_\tau=\Phi_F^{T-\tau}(x_\tau).
\]

Differentiating the endpoint and using the flow pushforward identity

\[
D\Phi_F^s(x)F(x)=F(\Phi_F^s(x))
\]

gives

\[
\boxed{
J_T'(\tau)
=
\lambda_\tau^\top\big(H(x_\tau)-F(x_\tau)\big),
}
\]

where

\[
\boxed{
\lambda_\tau
=D\Phi_F^{T-\tau}(x_\tau)^\top\nabla L_c(y_\tau).
}
\]

This identity is exact. It also explains why a universal local transition law is difficult:

- \(\lambda_\tau\) depends on the entire future clean trajectory;
- it depends on the final horizon \(T\);
- it depends on the switch state and basin;
- it transports local shortcut perturbations through the clean flow Jacobian;
- its sign is generally schedule-dependent.

An exact “integrated early benefit minus lost clean time” identity is possible by integrating \(J_T'(\tau)\), but the integrand is an adjoint sensitivity, not a schedule-independent local observable.

## 4.2 Local reduction to Relative Transfer

Let

\[
g_c=\nabla L_c,
\qquad
g_s=\nabla L_s.
\]

If the remaining clean-flow tangent map is approximated by the identity, then \(\lambda_\tau\approx g_c(x_\tau)\), and

\[
\begin{aligned}
J_T'(\tau)
&\approx g_c^\top(-g_s+g_c)\\
&=\|g_c\|^2-g_c^\top g_s.
\end{aligned}
\]

Define Relative Transfer

\[
\mathrm{Re}(c,s)
=\frac{g_c^\top g_s}{g_c^\top g_c}.
\]

Then

\[
J_T'(\tau)
\approx\|g_c\|^2(1-\mathrm{Re}(c,s)).
\]

The local boundary is therefore exactly

\[
\mathrm{Re}(c,s)=1.
\]

This is the quantity formalized and operationalized by Ding and Ye. A proposed law based only on accumulated gradient alignment, transfer, or “helpful update minus the clean update that was sacrificed” is therefore not new.

The scalar construction does not isolate a beyond-Relative-Transfer effect. At initialization,

\[
\mathrm{Re}(c,s)
=\frac{1}{5\varepsilon}+1+o(1),
\]

because the shortcut gradient updates the shared \(a\) coordinate by order \(\varepsilon\), while the clean gradient updates it only by order \(\varepsilon^2\). Thus ordinary first-order transfer already predicts that shortcut updates are initially more useful for current clean loss than clean updates. The theorem's novelty cannot rest on merely discovering that early shortcut gradients help.

## 4.3 A narrower candidate: durable clean-rate amplification

For a squared-loss clean task with residual vector \(r\), prediction Jacobian \(J_c\), and empirical clean NTK

\[
K_c=J_cJ_c^\top,
\]

clean gradient flow obeys

\[
\dot L_c=-\|\nabla L_c\|^2.
\]

Define the residual-aligned clean contraction rate

\[
\boxed{
\kappa_c(\theta,r)
=
\frac{r^\top K_c(\theta)r}{\|r\|^2}
=
\frac{\|\nabla L_c(\theta)\|^2}{2L_c(\theta)}.
}
\]

Then

\[
\frac{d}{dt}\log L_c=-2\kappa_c
\]

under clean gradient flow.

Let the excess shortcut field be

\[
A(\theta)=H(\theta)-F(\theta).
\]

To distinguish a representation change from immediate clean-loss transfer, hold the clean residual direction fixed and define the prospective representation-rate derivative

\[
\boxed{
\Gamma_{\mathrm{repr}}(\theta;r)
=
\frac{r^\top(D_AK_c(\theta))r}
{r^\top K_c(\theta)r}.
}
\]

This is not offered as an established new metric. It is the narrowest surviving theorem candidate after the literature audit.

### Scalar interpretation

For the scalar deployment predictor \(f_c=a u^2\),

\[
K_c=\|\nabla f_c\|^2=u^4+4a^2u^2.
\]

Initially,

\[
K_c(0)=5\varepsilon^4.
\]

At a fixed \(v=\bar v\),

\[
a=\Theta(1),
\qquad
u=\Theta(\varepsilon),
\]

so

\[
K_c=\Theta(\varepsilon^2).
\]

The shortcut has therefore amplified the future clean contraction scale by a factor \(\Theta(\varepsilon^{-2})\), even though the deployment output remains vanishing. This is the cleanest mechanistic description of what the toy actually proves.

## 4.4 Positive, neutral, and harmful cases a general theorem would need

A publishable law must predict all three signs **before observing final clean outcomes**.

### Positive transient exposure

A sufficient theorem would need conditions resembling all of the following:

1. The clean trajectory begins near a slow manifold or multiplicative bottleneck.
2. The shortcut field has a growing mode whose projection onto a shared representation coordinate increases a certified clean contraction/escape rate.
3. The shared-state change lies in the same clean basin and has the correct sign.
4. The rate gain persists after the shortcut is removed.
5. The gain is large enough to offset the clean updates sacrificed during exposure.
6. The shortcut's own residual eventually suppresses further useful updates, creating a reason to switch.

In a local normal form, let \(b\) be a shared bottleneck and \(q\) the deployment-specific slow coordinate. Suppose the clean escape rate is \(\lambda_c(b)\), while the shortcut linearization has an unstable eigenpair \((\lambda_s,e_s)\). A signed catalytic coupling is

\[
\mathcal C
=
\left(\nabla_b\lambda_c(b_0)^\top P_be_s\right)
\left\langle e_s,\theta_0\right\rangle.
\]

The scalar construction hard-wires \(\mathcal C>0\). A genuine theorem would prove that \(\mathcal C>0\), together with basin and persistence conditions, yields a speedup after matching current Relative Transfer and total horizon.

### Neutral exposure

The law must reject at least the following:

- **Independent shortcut parameters:** the excess shortcut field acts in a subspace that does not change the clean Jacobian or slow mode, so \(D_AK_c=0\).
- **Exact lazy/linear regime:** \(K_c\) is fixed, so no representation-rate amplification is possible. Any advantage must reduce to current gradient transfer or data reweighting.
- **Shortcut sharing only the label:** if it does not alter the deployment representation or clean tangent geometry, it cannot be a catalyst in the proposed sense.

These cases may still reduce training loss or starve the clean path, but they should show **no positive catalytic phase** once immediate Relative Transfer and compute are matched.

### Harmful exposure

The law must also identify at least two distinct harmful mechanisms:

- the shortcut changes the shared state so that \(\Gamma_{\mathrm{repr}}<0\), reducing the clean contraction rate;
- the shortcut increases a norm or tangent eigenvalue but moves the state into the wrong clean basin, wrong sign branch, inactive-unit region, or low-plasticity regime.

The second case shows why a scalar kernel-rate increase alone cannot be sufficient. A same-basin/sign certificate or a basin-wide clean PL/escape condition is required.

## 4.5 Why the current scalar theorem is favorable rather than general

The construction makes the desired effect nearly inevitable once its equations are chosen:

- the shortcut appears linearly as \(v\), while the deployment path is quadratic as \(u^2\);
- both paths multiply the same \(a\);
- shortcut training has a linear unstable \((a,v)\) mode;
- clean-only training is trapped by the invariant \(a\asymp u\), creating \(\dot u\asymp u^2\);
- shortcut training raises \(a\) to constant order without raising \(u\) beyond a constant multiple of \(\varepsilon\);
- removal converts \(\dot u\) from quadratic escape to exponential growth;
- all signs are initialized on the favorable branch.

This is not an invalid theorem. It is a normal-form existence proof. It becomes a scientific law only if a broader, architecture-independent condition identifies when real networks locally reduce to this favorable normal form and when they do not.

## 4.6 New prediction required for novelty

The minimum nontrivial prediction is:

> Among two shortcut interventions matched on current Relative Transfer, shortcut accuracy/margin, total updates, and immediate clean-loss change, the intervention that produces larger positive, persistent clean-rate amplification should require fewer post-withdrawal clean updates; an independent or lazy control with zero amplification should not benefit, and an anti-core intervention with negative amplification should be harmed.

This prediction is not equivalent to “tune the withdrawal time on validation.” It is prospective, comparative, and falsifiable. The current theorem does not prove it, and the current XOR check does not test matched-Relative-Transfer interventions.

## 4.7 Status of the XOR evidence

The nonlinear XOR script is appropriately labeled exploratory. It uses:

- ten deterministic seeds;
- a width-8 tanh MLP;
- exact full-distribution gradients;
- four shortcut correlations \(0.70,0.90,0.99,1.00\);
- a fixed 1,000-step main probe;
- a sweep of withdrawal steps;
- three margin thresholds \(0.25,0.40,0.60\).

The common margin threshold \(0.40\) selected different switch steps across the four correlations and improved mean clean loss by roughly \(6.3\times10^{-4}\) to \(7.6\times10^{-4}\), with 8–9 paired-seed wins out of ten. Accuracy was already 1.0 in the long-horizon setting. The threshold was chosen after inspecting the same toy system, and the reported extra-gradient/core-gradient cosine was already strongly negative at the trigger.

This is a useful existence clue, not a prospective validation of a law. It cannot bridge the scalar theorem to natural networks because it does not yet distinguish:

- durable representation-rate amplification;
- ordinary gradient transfer/conflict;
- loss-tail acceleration after accuracy saturation;
- architecture-specific tanh conditioning;
- post-hoc threshold selection.

---

# 5. Oral-level reviewer simulation

## 5.1 Strongest reviewer reduction — one sentence

> You hand-built an auxiliary path that directly multiplies the slow core parameter, let that easy path inflate the parameter, and then removed it; the alleged late “phase transition” is only that a fixed budget leaves too few clean steps.

## 5.2 Strongest defensible rebuttal — one sentence

> The logarithmic-versus-inverse-initialization separation isolates a real dynamical phenomenon—test-time-invalid supervision can durably improve the future clean vector field—but it becomes a general result only after a prospective rate-transfer theorem predicts positive, neutral, and harmful cases beyond gradient alignment.

## 5.3 Best case for acceptance

The strongest possible paper arc, after successful theory extension, would be:

1. a clean theorem showing a training-only signal changes the clean contraction/escape geometry, rather than merely reducing current loss;
2. an exact three-way asymptotic separation as an illustrative normal form;
3. a prospective state statistic derived from the theorem and explicitly separated from Relative Transfer;
4. negative controls that vanish in independent and lazy models and reverse under anti-core coupling;
5. one preregistered natural-task falsification showing the same statistic predicts the sign of transfer under matched compute.

That could be conceptually strong because the question is broader than robustness: when does temporary supervision alter the optimization geometry of the task that remains after the supervision disappears?

## 5.4 Best case for rejection

A skeptical reviewer can currently reject on all of the following grounds:

- **Tautological coupling:** the shared multiplier is placed exactly where it must be to accelerate the core.
- **Branch selection:** favorable positive initialization is assumed rather than explained.
- **No intrinsic upper boundary:** continued exposure preserves, rather than destroys, the warm start.
- **No harmful permanent phase at the theorem horizon:** permanent and clean both fail, but permanent is not shown worse.
- **Trigger mismatch:** the theorem's trigger is far from saturation and not derived from an optimality condition.
- **Local novelty collision:** early utility is already predicted by Relative Transfer, which diverges at initialization in the scalar model.
- **Post-hoc nonlinear evidence:** the XOR threshold was selected after inspection, with small loss gains and saturated accuracy.
- **Occupied algorithmic landscape:** LUPI, auxiliary modality learning, BAM, JTT, MaskTune, FeAT, dynamic curricula, gradient gating, scheduled sampling, and DAgger already cover most operational variants.
- **No natural bridge yet:** there is no demonstrated pre-outcome quantity that survives width, optimizer, task, or shortcut construction.

## 5.5 Significance judgment

The current contribution is **more than an algebra trick but less than a general law**. The asymptotic separation is worth preserving as a theorem example. It is not, by itself, an Oral-level paper because the architecture encodes the mechanism, the state trigger does not define an upper phase boundary, and the key observable has not been separated from existing transfer metrics.

The correct strategic decision is not to discard the seed and not to run a broad experiment sweep. It is to hold the seed at theory-only status until one of the following happens:

- a general shared-representation/clean-rate theorem is proved and survives the four required negative controls; or
- the theorem attempt collapses to Relative Transfer, generic continuation, gradient conflict, or a tautological value function, in which case the seed should be terminated.

---

# 6. Stage-0 authorization

## Not authorized under this verdict

A Stage-0 experiment is **not specified**, because the binding verdict does not authorize experiments.

No GPU work is permitted at this stage. In particular:

- GPUs 0–3 remain forbidden;
- GPUs 4–7 remain unused for this seed;
- foreign processes must not be touched;
- no natural benchmark sweep, threshold tuning, width sweep, optimizer sweep, or shortcut-construction sweep is authorized.

The next action is analytical only.

---

# 7. Binding next action

The next permitted action is to write and attempt to prove a **general clean-rate-amplification theorem** for two training vector fields or a shared representation. It must:

1. distinguish immediate gradient transfer from durable change in subsequent clean dynamics;
2. recover the scalar theorem as a special positive case;
3. produce a neutral result for independent shortcuts and fixed-kernel/lazy models;
4. produce a harmful result for an anti-core shared update or wrong-basin branch;
5. state a prospective statistic measurable without final clean validation outcomes;
6. show that the statistic is not Relative Transfer, gradient cosine, generic continuation, or a renamed closed operator-interference claim;
7. yield at least one new cross-intervention prediction under matched Relative Transfer;
8. be re-audited against current primary literature before any GPU experiment is authorized.

A reasonable theorem target is not “\(\Gamma_{\mathrm{repr}}\) is always sufficient.” It is a restricted normal-form or basin theorem in which a shortcut-induced change in a certified clean contraction/escape rate persists for a stated interval and dominates the opportunity cost. Failure to obtain a non-tautological theorem should terminate the seed rather than trigger more toy sweeps.

---

# 8. Machine-readable decision block

```yaml
terminal_verdict: HOLD_REQUIRES_GENERAL_LAW
mathematics_status: REPAIRABLE_WITH_EXPLICIT_CONSTANTS
direct_theorem_collision_found: false
exact_three_way_separation_status: VALID_AFTER_REPAIR
intrinsic_upper_withdrawal_boundary_proved: false
permanent_exposure_harm_relative_to_clean_proved: false
prospective_general_law_established: false
relative_transfer_collision_for_local_trigger: true
stage0_authorized: false
gpu_execution_authorized: false
allowed_gpu_ids: []
next_permitted_action: >-
  Prove and adversarially audit a general two-vector-field or shared-representation
  clean-rate-amplification theorem that predicts positive, neutral, and harmful
  transient supervision beyond Relative Transfer, including independent-shortcut,
  lazy/linear, shared-label-only, and anti-core negative controls.
forbidden_next_actions:
  - Run a GPU experiment.
  - Tune the XOR margin threshold further.
  - Expand into a broad benchmark sweep.
  - Claim withdrawal near saturation from the current theorem.
  - Claim an intrinsic help-to-harm state transition from the late-time lemma.
  - Revive closed operator-interference or other repository-level NO-GO seeds.
```

