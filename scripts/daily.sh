#!/usr/bin/env bash
# One full cycle: collect, then rebuild everything that can be rebuilt.
#
#   scripts/daily.sh              # normal run
#   scripts/daily.sh --dry-run    # collect and score, write nothing
#
# Any summaries queued by the collection step stay queued: draining the queue
# is the agent's job (see CLAUDE.md), and this script does not wait for it.
# Run it again after the queue is drained to fold the results in.

set -euo pipefail

CODE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$CODE_ROOT"

PYTHON="${PYTHON:-python3}"

# A --root in "$@" has to reach every stage, not only the first one. Collecting
# into one tree and then rebuilding another is the failure this guards: both
# commands exit 0, the deployment gains records that never render, and the code
# checkout gains an archive it was never supposed to hold.
#
# RA_WM_ROOT needs none of this -- it is read by every entry point already.
DEPLOYMENT=()
previous=""
for arg in "$@"; do
  case "$arg" in
    --root=*) DEPLOYMENT=("$arg") ;;
    *) [ "$previous" = "--root" ] && DEPLOYMENT=(--root "$arg") ;;
  esac
  previous="$arg"
done
# Expand to nothing at all when empty, rather than to one empty argument.
root_args=(${DEPLOYMENT[@]+"${DEPLOYMENT[@]}"})

echo "==> collecting"
"$PYTHON" -m pipelines.run_daily "$@"

# A dry run writes nothing, so there is nothing to render.
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ]; then
    exit 0
  fi
done

echo
echo "==> rendering"
"$PYTHON" -m pipelines.render ${root_args[@]+"${root_args[@]}"}

echo
echo "==> queue"
"$PYTHON" -m pipelines.enrich.queue ${root_args[@]+"${root_args[@]}"} stats
