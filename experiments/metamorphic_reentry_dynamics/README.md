# Metamorphic Re-entry Dynamics

This directory implements an anomaly-first Stage 0 over public PolyPythias training
checkpoints. It is intentionally not presented as an authorized paper seed.

```bash
python build_items.py
python -m unittest discover -s tests -v
python score_checkpoints.py --seed 1 --checkpoint step143000 --output results/preflight/seed1_step143000.jsonl
python analyze_stage0.py --discovery-dir results/discovery --output results/DISCOVERY_GATE.json
```

Read `PREREGISTRATION.md` and `FROZEN_CONFIG.json` before running. Confirmation seeds
must remain sealed unless the discovery gate explicitly returns
`DISCOVERY_PASS_CONFIRMATION_REQUIRED`.
