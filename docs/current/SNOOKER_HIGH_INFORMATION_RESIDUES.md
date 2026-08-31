# High-Information Snooker Residues for Contradiction-First Research Search

**Status:** source-derived search packet, not an AI claim and not an experiment authorization  
**Prepared:** 31 August 2026  
**Primary source:** the 33-case `SNOOKER_LOSSLESS_ABSTRACTION_ATLAS.md` produced from the repository's billiards discussion  
**Repository:** [ScottBlizzard/idle_2](https://github.com/ScottBlizzard/idle_2)

## 1. Why this packet exists

The full source discussion contains many distinct mechanisms. Mapping all of them directly into AI vocabulary repeatedly erased the useful distinctions and produced familiar headlines: robustness, option preservation, risk-sensitive planning, uncertainty management, and long-horizon value.

This packet retains only five residues that contain more structure than those slogans. They were selected because they combine at least two of the following:

- an outcome can reverse value without changing its physical distribution;
- legal or reliable actions change discontinuously across a turn or rule transition;
- a supposed fallback participates in the current dynamics and can therefore become harmful;
- restricting a pre-contact route need not restrict the post-contact result set;
- an immediately valuable object can become harmful when consuming it irreversibly deletes future structure.

These residues are **question generators**. They confer no novelty, and billiards is not evidence that an AI analogue exists.

## 2. Binding exclusions inherited from prior work

The following broad readings are already closed and must not be revived:

- generic continuation-, option-, viability-, reachability-, or failure-state-preserving planning;
- resettable failure with retained learning;
- generic error shaping into task-tolerant directions;
- redundancy-conditioned intervention strength as a standalone headline;
- insurance-before-exploration or ordinary fallback preservation;
- ordinary long-horizon reward, risk-sensitive control, action-space compression, or first-mover advantage;
- another observational predictor without a prospective matched intervention;
- a new graph score, sampler, reranker, regularizer, or scheduler as the main contribution.

The latest free divergence search also returned `NO_GO_NEED_NEW_SEED`: 16 candidates across 13 subfields collided with current literature or reduced to an obvious method. Its best near-miss, signed-cycle frustration under matched local supervision, remained classical structural balance/frustration plus an expected repair heuristic. No GPU work was authorized.

The compact decision record is
[`../audits/POST_INTERVENTION_DIVERGENCE_DECISION.md`](../audits/POST_INTERVENTION_DIVERGENCE_DECISION.md).

The next search must therefore begin from a **contradiction between strong results**, not from a carrier or a mechanism name.

## 3. Residue A — Uncertain outcomes are owned by the first actor

### Concrete source situation

A player opens a red pack only after securing the current pot. The exact post-collision positions are not predictable, but several playable reds may emerge. The spread is valuable when the shooter pots the current ball and therefore chooses first from the new layout. A physically similar spread can be harmful when the current ball is missed and the opponent chooses first.

### Nontrivial contrast

Holding the distribution over post-intervention layouts approximately fixed, its strategic value can change sign solely because the identity of the first observer/selector/actor changes.

This is not simply “initiative is good.” The key conjunction is:

1. the intervention creates several substitute opportunities;
2. the exact opportunity is not known before the intervention;
3. the first actor can inspect the realized state and select the best available continuation;
4. failure of the current action can transfer that selection right to the opponent.

### Necessary conditions

- There must be real post-realization choice; a deterministic layout with one forced move does not qualify.
- The actors must value at least some realized opportunities differently or compete over them.
- Move order must be separable from the distribution over layouts.
- The current pot or rule transition must determine who acts first.

### Alternative explanations to defeat

- The shooter-owned condition may simply have a better physical spread.
- Potting may change cue-ball position as well as move order.
- One actor may be globally stronger rather than benefiting from first selection.
- The effect may reduce to an ordinary scalar continuation value after full-state expansion.

### Counterexample or reversal

If the post-intervention state has one forced continuation, if both actors share the same objective, or if a neutral mechanism allocates the opportunity independently of turn order, the ownership effect should vanish.

### Minimal causal object

A distribution over realized opportunity sets, the actor who observes and selects first, each actor's reliable action correspondence, and the transition that assigns selection rights.

### What an AI search must look for

Find two strong results concerning the same stochastic diversification, exploration, generation, retrieval, delegation, or intervention process:

- one where broader outcome support improves performance;
- another where similar broadening hurts, is neutral, or benefits an adversary;
- a hidden, prospectively actuable variable specifying who gets first conditional selection after the outcome is realized;
- a matched intervention that swaps selection ownership without changing the outcome generator.

Do not advance a candidate if the only conclusion is “give the agent, rather than the adversary, access to good samples.”

## 4. Residue B — Restricting a path is not restricting its post-contact image

### Concrete source situation

A defensive layout may appear to leave one visible escape route. That does not guarantee control of the opponent. If legal contact through that route restores reliable variation in speed, side, contact thickness, and cushion choice, the opponent may open the table or counter-snooker. A strong defense restricts not only paths to contact but the set of safe or advantageous states reachable after contact.

### Nontrivial contrast

Two constraints can leave the same number of visible or legal actions while producing radically different sets of post-success consequences. Conversely, a single visible action can recover many downstream control dimensions after an intermediate event.

### Necessary conditions

- Pre-contact or local action count must be distinguishable from the transition image after success.
- The constrained actor must regain meaningful controls after an intermediate event.
- Those restored controls must alter the opponent-facing consequence, not merely cosmetic trajectory details.
- Reliability is actor-specific; theoretical paths alone are insufficient.

### Alternative explanations to defeat

- The apparently unique route may not actually be unique.
- The effect may be ordinary model error about the transition function.
- The “restored dimensions” may be redundant and have no outcome consequence.
- A larger terminal set may be fully captured by standard reachability or empowerment.

### Counterexample or reversal

If all legal contacts map into the same contained terminal region, or if post-contact controls are too unreliable to use, one visible route can genuinely constrain the opponent.

### Minimal causal object

A staged transition with a pre-event reliable action set, an intermediate success/contact event, a post-event reliable control set, and the image of those controls in strategically classified terminal states.

### What an AI search must look for

Find apparently conflicting results about constrained decoding, tool restriction, policy shielding, interface narrowing, sandboxing, delegation, or structured reasoning:

- one result where reducing available actions improves safety or reliability;
- another where a similarly narrow interface fails because a permitted intermediate action reconstructs a large downstream consequence set;
- a matched intervention that holds local action count and task capability fixed while changing only the post-intermediate transition image.

Do not advance ordinary jailbreak, capability elicitation, reachability, or “agents route around constraints” claims without a new separating law.

## 5. Residue C — Turn transitions can change the type of problem the next actor must solve

### Concrete source situation

Near the last difficult red, the current player may forgo potting an easy color and instead use the color-on turn to create a safety. When the turn ends, the opponent becomes red-on and must address the difficult red. The action does not merely transfer a difficult state; it changes the legally admissible target class at the handoff.

### Nontrivial contrast

Two physically similar handoffs can impose different problems because the rule state changes which object or operation is legal for the incoming actor. The local action can therefore alter the **type of next problem**, not just its difficulty.

### Necessary conditions

- Legal target classes must alternate or depend on turn state.
- The current player must have a legal turn-ending action that preserves the difficult target.
- The incoming actor must not be free to choose the same easy target.
- The forgone immediate reward must be affordable.

### Source uncertainty requiring enrichment

The precise last-red/color layout, legal sequence, and expert-frequency claim are not preserved well enough to treat this as an established professional convention. It is a conditional mechanism extracted from the discussion. Any later empirical use must first verify the exact snooker sequence.

### Alternative explanations to defeat

- The non-potting color shot may simply create a spatially stronger safety.
- Expected score alone may explain the preference.
- The opponent may possess an easy red escape that removes the handoff asymmetry.

### Counterexample or reversal

Remove red–color alternation, permit the incoming player to select the easy color, make the red easy, or make the color points decisive. The preference should disappear.

### Minimal causal object

A physical state, player-to-move variable, legal-target state, turn-transition rule, and action-dependent mapping from the current legal class to the next actor's legal class.

### What an AI search must look for

Find two strong results about delegation, workflow handoffs, tool permissions, staged verification, multi-agent protocols, or sequential training:

- one where handing off an intermediate state reduces burden or improves modularity;
- another where handoff hurts or changes behavior despite a similar physical/informational state;
- a hidden variable determining the next actor's admissible objective, tool set, loss, or verification obligation;
- an intervention that swaps this admissible problem class while matching state information and compute.

Do not advance a candidate that merely says “assign hard tasks to another agent.”

## 6. Residue D — A fallback can become harmful because it participates in the intervention

### Concrete source situation

A near-pocket red appears to insure a pack split, but it is not an external backup. It may move during the collision, block the cue ball's exit, obscure another red, constrain the entry route, disappear, or become available to the opponent. Protecting it can make the current K shot worse.

### Nontrivial contrast

Adding or preserving a nominal fallback need not monotonically increase recoverability. Its value can become negative when the fallback shares the same dynamics as the intervention it is meant to insure.

### Necessary conditions

- The fallback must be endogenous rather than independently reserved.
- Preserving it must alter the current action set, transition, or outcome distribution.
- Its availability after the intervention must depend on visibility, ownership, or survival.
- The cost must not be reducible solely to consuming extra capacity.

### Alternative explanations to defeat

- The fallback may simply be low quality.
- More objects may increase collision noise without any special endogeneity.
- A standard resource-cost term may explain the entire effect.
- The option may remain useful but be outweighed by an unrelated current-pot penalty.

### Counterexample or reversal

An independently isolated fallback that cannot be affected by the intervention and remains owned by the same actor should recover ordinary nonnegative option value, aside from explicit reservation cost.

### Minimal causal object

A primary intervention, a nominal fallback resource, a participation relation connecting the fallback to the intervention dynamics, and post-intervention survival, visibility, accessibility, and ownership variables.

### What an AI search must look for

Find contradictions involving backup models, verifier fallbacks, reserved tools, redundant experts, recovery policies, memory checkpoints, or safety scaffolds:

- one result where an added fallback improves reliability;
- another where a superficially similar fallback degrades the primary process or disappears exactly when needed;
- a hidden participation variable that can be actuated while matching fallback quality, capacity, and nominal availability;
- a sign reversal between isolated and dynamically entangled fallback conditions.

Do not advance generic ensemble diversity, redundancy, interference, or resource competition.

## 7. Residue E — Consuming a locally valuable object can irreversibly delete the structure needed to remain viable

### Concrete source situation

When only pink and black remain and the trailing player still requires foul points, a hanging pink is not merely a six-point reward. Its continued presence may help construct a snooker or keep a legal scoring route alive. Potting it removes the object irreversibly and can end the practical route to winning even though the immediate reward is positive.

### Nontrivial contrast

An object can change from reward to structural resource without moving. Consuming it yields positive local reward while deleting the physical or legal constraints required for any viable continuation.

### Necessary conditions

- Exact score and termination state must make additional foul points necessary.
- The object must contribute materially to future constraint geometry or legal reachability.
- Consumption/removal must be irreversible.
- No substitute object may provide the same structure.

### Source uncertainty requiring enrichment

The exact score arithmetic, pink/black positions, and professional choice boundary require reconstruction. The residue is conditional and must not be presented as a verified universal snooker tactic.

### Alternative explanations to defeat

- The black's location, rather than pink preservation, may determine viability.
- Immediate pink points may already remove the need for a snooker.
- Keeping the pink may create no credible forcing geometry.
- A generic inventory or budget model may fully explain the decision.

### Counterexample or reversal

Pot the pink when six points eliminate the deficit, black alone supports the required snooker, pink does not contribute to constraint geometry, or failing to pot is too likely to end the frame immediately.

### Minimal causal object

A multi-role object, a local consumption reward, an irreversible deletion operator, a viability condition over later legal/physical structures, and substitute-resource availability.

### What an AI search must look for

Find contradictions around pruning, compression, context deletion, tool consumption, curriculum removal, scaffold retirement, model merging, or resource cleanup:

- one result where deleting an apparently solved or redundant component improves efficiency or generalization;
- another where similar deletion destroys future repair, verification, or adaptation despite matched current performance;
- a hidden role-state variable showing that the component is currently low-value but structurally necessary for a future constraint;
- an intervention that changes only structural participation or substitute availability, not current output quality.

Do not revive the repository's closed “successful patch harms future maintainability” or generic continuation-value claims.

## 8. Cross-residue combinations worth searching

The five residues should not be forced into one theory. Three combinations, however, create sharper contradiction templates:

1. **Ownership × endogenous fallback:** a fallback survives, but its value reverses depending on who selects it first after the intervention.
2. **Post-contact image × legal handoff:** a local constraint appears effective, but success changes the next stage's admissible action class and restores a wide consequence set.
3. **Legal handoff × irreversible role deletion:** consuming an easy resource changes both what remains physically possible and what the next actor is legally or procedurally required to do.

A candidate should use a combination only if each factor can be independently actuated. Otherwise the combination creates more confounding rather than more depth.

## 9. Ranking for the next search

| Priority | Residue | Why retained | Main risk |
|---:|---|---|---|
| 1 | A — first actor owns uncertain outcomes | Exact outcome distribution can change sign without changing its microstates | May reduce to standard first-mover or value-of-information theory |
| 2 | B — path restriction versus post-contact image | Separates local interface width from downstream consequence control | May reduce to reachability, empowerment, or ordinary sandbox escape |
| 3 | C — rule-induced problem-type handoff | Changes the next actor's admissible problem, not just state difficulty | Source case and AI carrier may be artificial |
| 4 | D — endogenous fallback | Violates monotone intuition that more fallback is safer | Interference and resource-cost literatures are broad |
| 5 | E — irreversible role reversal | Positive reward can delete the only future constraint resource | Easily collapses to continuation value or inventory planning |

## 10. Required research standard

For any proposed AI seed, require all of the following:

1. Two primary results that appear genuinely incompatible under their published explanations.
2. A hidden regime variable derived from one residue above.
3. A prospective intervention on that variable before outcomes.
4. An equivalence class matching the strongest alternative explanations.
5. A pre-specified qualitative sign reversal or phase boundary, not just a better correlation.
6. A scientific consequence stronger than another score, sampler, reranker, regularizer, or scheduler.
7. A one-day kill test within roughly four GPU-hours.
8. A credible two-carrier path if the first result survives.

`NO_GO_NEED_NEW_SEED` remains the correct answer if no contradiction survives these requirements.
