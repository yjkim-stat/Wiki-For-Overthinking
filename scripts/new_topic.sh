#!/usr/bin/env bash
# Create a new topic from the template.
#
#   scripts/new_topic.sh "Causal Inference"
#   scripts/new_topic.sh "Single-Cell Genomics" single-cell
#
# Writes config/topics/<slug>.yaml with the slug and name filled in. Edit the
# keywords before the next run: the template's placeholders match nothing.

set -euo pipefail

usage() {
  echo "usage: $0 \"Topic Name\" [slug]"
  echo
  echo "Creates config/topics/<slug>.yaml from the template."
}

if [ $# -lt 1 ]; then
  usage >&2
  exit 64
fi

case "$1" in
  -h|--help|help) usage; exit 0 ;;
  -*) echo "unknown option: $1" >&2; usage >&2; exit 64 ;;
esac

NAME="$1"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$ROOT/config/topics/_template.yaml"

if [ $# -ge 2 ]; then
  SLUG="$2"
else
  SLUG="$(printf '%s' "$NAME" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
fi

if [ -z "$SLUG" ]; then
  echo "could not derive a slug from '$NAME'; pass one explicitly" >&2
  exit 65
fi

TARGET="$ROOT/config/topics/$SLUG.yaml"

if [ -e "$TARGET" ]; then
  echo "topic already exists: $TARGET" >&2
  exit 73
fi

if [ ! -f "$TEMPLATE" ]; then
  echo "missing template: $TEMPLATE" >&2
  exit 66
fi

sed -E \
  -e "s/^slug: .*/slug: $SLUG/" \
  -e "s/^name: .*/name: $NAME/" \
  "$TEMPLATE" > "$TARGET"

echo "created $TARGET"
echo
echo "Next: edit keywords.any, then run"
echo "  python3 -m pipelines.run_daily --topic $SLUG --dry-run"
