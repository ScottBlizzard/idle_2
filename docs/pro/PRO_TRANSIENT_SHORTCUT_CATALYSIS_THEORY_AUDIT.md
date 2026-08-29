# Fresh-Pro Prompt — Transient Shortcut Catalysis Theory Audit

Use this prompt in a **new Pro conversation**, not the conversation that produced the earlier 15-candidate divergence report.

```text
You are conducting a hostile theory, novelty, and significance audit for a potential ICLR Oral-level machine-learning paper. Do not brainstorm broadly and do not propose a large experiment sweep. Your first job is to determine whether the current theorem-shaped seed is correct, genuinely new, and capable of supporting a general scientific law rather than a hand-constructed toy.

Repository
- GitHub: https://github.com/ScottBlizzard/idle_2
- Repository name: ScottBlizzard/idle_2
- The local checkout, if available, is D:\ICLR_2\idle_2_repo.

Read only these files first, in this exact order:
1. docs/theory/TRANSIENT_SHORTCUT_CATALYSIS_THEORY_NOTE.md
2. analysis/transient_shortcut_phase_transition/README.md
3. analysis/transient_shortcut_phase_transition/explore_catalytic_ode.py
4. analysis/transient_shortcut_phase_transition/explore_xor.py
5. docs/audits/ORAL_SEED_LITERATURE_ROLE_REAUDIT.md
6. docs/current/CURRENT_STATUS.md

Do not anchor on old rejected proposals. Consult older repository files only when needed to verify provenance or avoid reviving a closed claim.

The candidate claim
An easy training-only shortcut may act as a temporary optimization catalyst when it shares a multiplicative bottleneck with a harder invariant feature. Clean-only learning is slow near small initialization; permanent shortcut exposure solves the training objective through the easy path and starves the invariant path; state-triggered withdrawal preserves the amplified shared state and enables rapid invariant learning. The current scalar gradient-flow construction claims an asymptotic clean/permanent/transient separation, and an exploratory nonlinear XOR check finds that one shortcut-aligned margin threshold adapts withdrawal time across four shortcut strengths.

Audit requirements

A. Verify the mathematics line by line
- Re-derive both gradient flows, all invariants, the exact identity u(v), monotonicity/no-crossing of the shortcut output, the clean-only lower bound, the permanent-shortcut bound, the threshold-time scaling, the post-withdrawal convergence rate, and the late-withdrawal boundary.
- Check that all three methods are compared at a genuinely matched total horizon. State the theorem with explicit quantifiers and constants. Flag any claim that is stronger than the proof.
- Identify hidden sign, boundedness, initialization, loss, or continuous-time assumptions.
- If a repair is possible without changing the scientific mechanism, write the repaired theorem and proof sketch. If not, issue a mathematical NO-GO.

B. Search the current primary literature aggressively
- Search papers and official proceedings through the current date, not only the references already in the repository.
- Cover at minimum: shortcut/spurious-feature learning dynamics; learning using privileged information; hints and training-only modalities; auxiliary-task and multi-task optimization; curriculum/homotopy/continuation methods; critical learning periods; warm starts and plasticity; feature amplification or bias amplification; invariant-feature learning after ERM pretraining; gradient alignment/conflict; saddle or plateau escape; time-scale separation in deep linear/nonlinear networks; dynamic curriculum stopping; teacher forcing and scheduled removal.
- Verify titles, authors, dates, venues, and exact theorem/algorithm scope from primary sources.
- Treat literature by role rather than binary similarity. For every serious neighbor classify it as one of: DIRECT THEOREM COLLISION, DIRECT ALGORITHMIC COLLISION, POSITIVE ADVERSARY, MECHANISM FOUNDATION, MANDATORY BASELINE, or UNEXPLAINED ANOMALY.
- In particular, confront at least:
  * arXiv:2606.30444, SGD Provably Prioritizes a Shortcut Spurious Feature in the XOR Model;
  * arXiv:2304.11327, Understanding and Improving Feature Learning for Out-of-Distribution Generalization;
  * arXiv:2608.17268, Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics;
  * arXiv:2507.22089, Principled Curriculum Learning using Parameter Continuation Methods;
  * arXiv:2604.00698, Learning to Hint for Reinforcement Learning;
  * arXiv:2210.04643, Critical Learning Periods for Multisensory Integration in Deep Networks;
  * arXiv:2602.03066, Shortcut Features as Top Eigenfunctions of NTK.
- Do not reject the seed merely because neighboring work exists. Determine exactly what is occupied, what can be used as support or a baseline, and what irreducible statement—if any—remains new.

C. Decide whether the mechanism can be generalized
- The scalar model is deliberately favorable because the shortcut and invariant path share parameter a. Determine whether this makes the result tautological.
- Try to derive a broader condition on two training vector fields or a shared representation that predicts all three signs: helpful transient exposure, neutral exposure, and harmful exposure.
- A useful condition must be measurable before final clean outcomes and must reject at least these negative controls: an independent shortcut, a lazy/linear model, a shortcut sharing only the final label, and a shared parameter whose shortcut update points away from the core basin.
- Examine whether integrated early transfer minus lost clean-training time and later gradient starvation yields a schedule-independent transition law. Compare this directly with gradient alignment and Relative Transfer; do not rename an existing quantity.
- State what new prediction follows that is not simply “tune the withdrawal time on validation.”

D. Judge Oral-level significance before experiments
- Explain the strongest reviewer reduction in one sentence.
- Explain the strongest defensible rebuttal in one sentence.
- Decide whether the contribution could become a general law of transient supervision, or is only a clever constructed example.
- Require a plausible bridge to natural GPU-only tasks within at most 8x RTX 4090. The server constraint is physical GPUs 4–7 for this project when sharing the machine; GPUs 0–3 and foreign processes must never be touched. Do not run anything during this audit.
- Only if novelty and generality survive, specify one small preregisterable Stage-0 falsification experiment with a frozen state trigger, matched compute, clean-only/permanent/transient controls, independent-shortcut negative control, at least one natural dataset/model pair, and explicit GO/NO-GO thresholds. Do not provide a broad benchmark plan.

Required terminal verdict
Choose exactly one:
- GO_THEOREM_EXTENSION_AND_PREREGISTERED_STAGE0
- HOLD_REQUIRES_GENERAL_LAW
- NO_GO_DIRECT_COLLISION
- NO_GO_HAND_CONSTRUCTED_TRIVIALITY
- NO_GO_MATHEMATICAL_FAILURE

Output
Write one self-contained Markdown report to:
D:\ICLR_2\TRANSIENT_SHORTCUT_CATALYSIS_THEORY_AUDIT.md

The report must include:
1. Executive verdict.
2. Corrected formal theorem and proof audit.
3. Claim-by-claim literature collision matrix with primary links.
4. General-law attempt, including positive and negative cases.
5. Oral-level reviewer simulation: strongest case for and against.
6. If and only if authorized by the verdict, a single frozen Stage-0 design.
7. A final machine-readable decision block with the exact terminal verdict and the next permitted action.

Be adversarial. A beautiful toy theorem is not enough. Equally, do not discard a new mechanism merely because its foundations have prior literature. The central question is whether the exact three-way asymptotic separation plus a prospective state boundary constitutes a new and general scientific statement.
```
