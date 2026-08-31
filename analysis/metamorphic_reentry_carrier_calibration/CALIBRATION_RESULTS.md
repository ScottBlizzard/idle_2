# Carrier calibration results

Status: **closed after capability-only calibration**

No longitudinal checkpoint curve was acquired or inspected.

## Attempt 1 — key-value lookup, target first versus last

The final Pythia-410M seed-1 checkpoint completed 512 records.

| split | target first | target last |
|---|---:|---:|
| discovery template | 66.41% | 83.59% |
| held-out template | 91.41% | 72.66% |

The predeclared 70% all-cell gate failed. The representation imbalance also makes this a
poor carrier for attributing a later sign change to a training phase rather than ordinary
position sensitivity.

## Attempt 2 — addition associativity

The same final checkpoint completed 192 records over a balanced 48/48 true/false bank.
Moving only parentheses kept operands, order, operators, truth, and answer labels fixed.
Both left- and right-associated forms scored 50.00%. The carrier failed the 70% gate.

## Decision

Do not run any PolyPythias longitudinal discovery. The public checkpoint suite ends at
410M for the nine-seed release, and this model is not capable enough for the clean tasks.
Further simplification would approach lexical copying and weaken the scientific object.
