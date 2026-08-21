#!/usr/bin/env bash
# Install (or remove) the scheduled collection job for one deployment.
#
#   scripts/install-cron.sh --print                 # show the line, change nothing
#   scripts/install-cron.sh --root /srv/archive     # install it
#   scripts/install-cron.sh --root /srv/archive --remove
#
# What this schedules is `scripts/daily.sh`: collect, score, store, render. It
# does NOT read papers -- that step needs a model in the loop and cron has no
# way to provide one. The queue grows until somebody opens a session and drains
# it, which is the intended shape and not a backlog to worry about.
#
# One line per deployment root, tagged so that re-running replaces it instead of
# adding a second one. Every other line in the crontab is carried through
# untouched.

set -euo pipefail

CODE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DAILY="$CODE_ROOT/scripts/daily.sh"

# Tests point this at a stub. Nothing else should set it.
CRONTAB="${RA_WM_CRONTAB_CMD:-crontab}"

SCHEDULE="0 8 * * *"
ROOT="${RA_WM_ROOT:-}"
LOG=""
ACTION="install"
FORCE=0

die() { echo "install-cron: $*" >&2; exit 2; }

usage() {
  sed -n '2,17p' "${BASH_SOURCE[0]}" | sed 's/^# \?//'
  cat <<'USAGE'

Options:
  --root PATH   deployment tree to collect into (default: $RA_WM_ROOT, else the
                code checkout -- see the warning it prints)
  --at EXPR     five-field cron schedule (default: "0 8 * * *", daily 08:00)
  --log PATH    where to append output (default: <root>/data/logs/cron.log)
  --print       write the crontab line to stdout and exit; touches nothing
  --remove      delete this root's line from the crontab
  --force       proceed even though the root does not exist yet
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    --root) [ $# -ge 2 ] || die "--root needs a path"; ROOT="$2"; shift 2 ;;
    --root=*) ROOT="${1#*=}"; shift ;;
    --at) [ $# -ge 2 ] || die "--at needs a schedule"; SCHEDULE="$2"; shift 2 ;;
    --at=*) SCHEDULE="${1#*=}"; shift ;;
    --log) [ $# -ge 2 ] || die "--log needs a path"; LOG="$2"; shift 2 ;;
    --log=*) LOG="${1#*=}"; shift ;;
    --print) ACTION="print"; shift ;;
    --remove) ACTION="remove"; shift ;;
    --force) FORCE=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "unknown argument: $1" ;;
  esac
done

# -- resolve the root ---------------------------------------------------------
if [ -z "$ROOT" ]; then
  ROOT="$CODE_ROOT"
  echo "install-cron: no --root and no RA_WM_ROOT; collecting into the code" >&2
  echo "  checkout at $CODE_ROOT. Records, wiki and archive will accumulate" >&2
  echo "  inside the repository you pull framework updates into. Pass --root" >&2
  echo "  to keep them apart." >&2
fi
# An absolute path, because cron runs from the user's home with no working
# directory of ours.
if [ -d "$ROOT" ]; then
  ROOT="$(cd "$ROOT" && pwd)"
elif [ "$FORCE" -eq 1 ]; then
  case "$ROOT" in /*) ;; *) ROOT="$PWD/$ROOT" ;; esac
else
  die "root does not exist: $ROOT (pass --force to schedule it anyway)"
fi

# cron reads an unescaped % as a newline and hands the command everything before
# it. A path holding one would be silently truncated.
case "$ROOT$LOG$SCHEDULE" in
  *%*) die "cron treats % specially; it cannot appear in a path or schedule" ;;
esac

[ -x "$DAILY" ] || die "not executable: $DAILY"

# Five fields, no more and no fewer. This is a shape check, not a validator --
# cron itself rejects a malformed field, but it does so silently at install time
# on some implementations.
read -r -a _fields <<<"$SCHEDULE"
[ "${#_fields[@]}" -eq 5 ] || die "--at wants five fields, got ${#_fields[@]}: $SCHEDULE"

[ -n "$LOG" ] || LOG="$ROOT/data/logs/cron.log"

# -- the interpreter ----------------------------------------------------------
# cron's PATH is famously not a login shell's. Resolving python3 now and pinning
# it is the difference between a job that runs and one that fails every night
# with "python3: not found" into a log nobody is reading yet.
PYTHON_BIN="$(command -v "${PYTHON:-python3}" || true)"
[ -n "$PYTHON_BIN" ] || die "cannot find ${PYTHON:-python3} on PATH"

MARKER="# ra-wm-schedule[$ROOT]"
LINE="$SCHEDULE PYTHON='$PYTHON_BIN' '$DAILY' --root '$ROOT' >> '$LOG' 2>&1 $MARKER"

if [ "$ACTION" = "print" ]; then
  printf '%s\n%s\n' "$MARKER" "$LINE"
  exit 0
fi

# -- read the existing crontab ------------------------------------------------
# Never replace a crontab we failed to read: that is how an unrelated job gets
# deleted by a tool that was only ever asked to add one.
set +e
CURRENT="$(LC_ALL=C "$CRONTAB" -l 2>/tmp/ra-cron-err.$$)"
STATUS=$?
ERR="$(cat /tmp/ra-cron-err.$$ 2>/dev/null)"; rm -f /tmp/ra-cron-err.$$
set -e
if [ "$STATUS" -ne 0 ]; then
  case "$ERR" in
    *"no crontab for"*) CURRENT="" ;;
    *) die "could not read the crontab ($ERR); nothing was changed. Use --print
  and install the line yourself if this host manages cron another way." ;;
  esac
fi

# Drop our own lines, keep every other one exactly as it was.
KEPT="$(printf '%s\n' "$CURRENT" | grep -vF "$MARKER" || true)"
# `grep -v` on empty input yields one empty line; strip leading/trailing blanks
# so an install into an empty crontab does not accumulate them.
KEPT="$(printf '%s\n' "$KEPT" | sed -e '/./,$!d')"

if [ "$ACTION" = "remove" ]; then
  if ! printf '%s\n' "$CURRENT" | grep -qF "$MARKER"; then
    echo "install-cron: no entry for $ROOT; nothing to remove"
    exit 0
  fi
  printf '%s\n' "$KEPT" | "$CRONTAB" -
  echo "install-cron: removed the entry for $ROOT"
  exit 0
fi

mkdir -p "$(dirname "$LOG")"

{
  [ -n "$KEPT" ] && printf '%s\n' "$KEPT"
  printf '%s\n%s\n' "$MARKER" "$LINE"
} | "$CRONTAB" -

cat <<SUMMARY
install-cron: scheduled
  when   $SCHEDULE
  root   $ROOT
  log    $LOG

Collection, scoring and rendering run on this schedule. Reading does not: open a
session and drain the queue when it suits you, then run daily.sh once more to
fold the readings in.

  $CODE_ROOT/scripts/daily.sh --root '$ROOT'
SUMMARY
