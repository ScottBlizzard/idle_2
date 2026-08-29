# Capability-Consequence Inversion Exploratory Audit

This directory preserves a negative result from the 2026-08-30 contradiction-first
search. It is not an active research seed.

The script audits the public `sungjuncho/agentdojo-trajectories` bundle using existing
utility/security labels and a frozen dictionary of externally mutating tools. It compares
exact task-and-attack pairs on which both Gemma 4 E4B IT and Qwen 3.5 9B fail utility.

The large raw difference in mutation-given-failure disappears after requiring both
models to avoid the benchmark security failure. The signal is therefore best explained
by AgentDojo's already-known capability-security inverse scaling, not a new general law
of conditional failure consequence.

Run from the repository root:

```powershell
python analysis\capability_consequence_inversion\explore_agentdojo.py `
  D:\ICLR_2\_scratch\agentdojo-trajectories
```

The dataset is scratch data and is intentionally not committed.

