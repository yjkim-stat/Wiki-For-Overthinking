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

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PYTHON="${PYTHON:-python3}"

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
"$PYTHON" -m pipelines.render

echo
echo "==> queue"
"$PYTHON" -m pipelines.enrich.queue stats
