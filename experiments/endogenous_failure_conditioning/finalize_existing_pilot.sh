#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: $0 REPO_DIR BANK_DIR RUN_DIR CONFIG" >&2
  exit 2
fi

REPO_DIR="$(readlink -f "$1")"
BANK_DIR="$(readlink -f "$2")"
RUN_DIR="$(readlink -m "$3")"
CONFIG="$(readlink -f "$4")"
SCRIPT_DIR="$REPO_DIR/experiments/endogenous_failure_conditioning"
PYTHON_BIN="${PYTHON_BIN:-python}"

if [[ ! -f "$RUN_DIR/PIDS.txt" ]]; then
  echo "missing PIDS.txt: $RUN_DIR" >&2
  exit 3
fi

while true; do
  active=0
  while read -r token; do
    pid="${token#pid=}"
    [[ "$token" == pid=* ]] || continue
    if kill -0 "$pid" 2>/dev/null; then
      cmd="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)"
      if [[ "$cmd" == *run_corrector.py* && "$cmd" == *"$RUN_DIR"* ]]; then
        active=$((active + 1))
      fi
    fi
  done < <(tr ' ' '\n' < "$RUN_DIR/PIDS.txt")
  echo "active_correctors=$active"
  [[ "$active" -gt 0 ]] || break
  sleep 60
done

complete=1
for model in qwen25_3b qwen25_7b qwen3_4b qwen3_8b; do
  [[ -f "$RUN_DIR/outputs/$model.manifest.json" ]] || complete=0
done

if [[ "$complete" -eq 1 ]]; then
  if [[ ! -f "$RUN_DIR/results/FINAL_GATE.json" ]]; then
    "$PYTHON_BIN" "$SCRIPT_DIR/analyze_pilot.py" \
      --bank "$BANK_DIR/error_bank.jsonl" \
      --outputs "$RUN_DIR/outputs" \
      --config "$CONFIG" \
      --result "$RUN_DIR/results" \
      > "$RUN_DIR/analyze.log" 2>&1
  fi
  echo "pilot complete: $RUN_DIR/results/FINAL_GATE.json"
  exit 0
fi

echo "one or more legacy correctors ended without a completion manifest; invoking resumable shared launcher"
for attempt in 1 2 3 4 5; do
  set +e
  bash "$SCRIPT_DIR/launch_shared_pilot.sh" "$REPO_DIR" "$BANK_DIR" "$RUN_DIR" "$CONFIG"
  status=$?
  set -e
  [[ "$status" -eq 0 ]] && exit 0
  if [[ "$status" -eq 3 || "$status" -eq 8 || "$status" -eq 20 || "$status" -eq 21 ]]; then
    echo "shared resume attempt $attempt deferred/failed with status $status; retrying in 60 seconds"
    sleep 60
  else
    exit "$status"
  fi
done
echo "shared resume exhausted five engineering attempts" >&2
exit 40
