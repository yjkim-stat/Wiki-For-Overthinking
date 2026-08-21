"""What a night of reading did, written where the archive keeps its days.

    python -m pipelines.digest [--date YYYY-MM-DD]

`archive/daily/<date>.md` is written by `run_daily`, so a night that collected
nothing leaves no trace inside the archive at all. The reading, the definitions,
the questions settled — the actual work — survived only in a commit message,
which is outside the thing it is about and invisible to anybody browsing it.

This writes that page for the session rather than the collection, into the same
file, under its own heading. `run_daily` keeps the top of the page; a day with
both a collection and a session ends up with one page describing both, which is
what a reader wants from a directory of dates.

**Everything here is derived from the archive**, and that is the constraint that
shapes it. This command has no memory of the session and no way to acquire one:
it reads what the records now say and reports the difference a date makes. So it
can count the tasks answered today and the findings settled today, and it cannot
know which wiki note somebody wrote a paragraph in — nothing records that, and a
guess from a file's modification time would be wrong every time a render touched
the auto block.

So the page ends where the derivable facts end, and **anything written after
`<!-- session:end -->` is preserved for ever**, exactly as in a wiki note. That
is where a session says what only it knows. Re-running replaces the derived
block and leaves that prose alone.

## The last section is the point

*What was left unanswered* is the one part of this page that is an input rather
than a record. A pending queue, a definition its evidence has outgrown, a lookup
nobody could settle: those are what the next night starts from, and until now
they had to be rediscovered by running four commands and remembering what the
numbers meant.
"""

from __future__ import annotations

import argparse
import logging
import re
from datetime import date
from pathlib import Path

from .common import config as config_mod
from .common import log
from .common import paths as P
from .common.config import Config
from .common.store import RecordStore, write_text
from .enrich.queue import Queue
from .render import stale_analysis, stale_definitions, stale_findings

_LOG = log.get(__name__)

BEGIN = "<!-- session:begin -->"
END = "<!-- session:end -->"

_KIND_ORDER = ("paper", "video", "concept", "synthesis", "lookup")


def _on(stamp: str, day: date) -> bool:
    """Whether an ISO timestamp falls on ``day``. Empty is never today."""
    return bool(stamp) and stamp[:10] == day.isoformat()


def gather(cfg: Config, day: date) -> dict:
    """What the archive can say about one day, and what it is still owed."""
    store = RecordStore(cfg.layout)
    queue = Queue(cfg.layout)

    answered: dict[str, int] = {}
    for state in (queue.layout.queue_done, queue.layout.queue_archive):
        for path in sorted(state.glob("*.json")):
            task = queue.load(path.stem) or {}
            if _on(str(task.get("completed_at", "") or ""), day):
                answered[task.get("kind", "?")] = answered.get(task.get("kind", "?"), 0) + 1

    settled = [
        finding
        for finding in store.iter_findings()
        if finding.live and _on(finding.established_at, day)
    ]
    checked = [
        reference
        for reference in store.iter_references()
        if _on(reference.first_seen, day) or _on(reference.retrieved_at, day)
    ]

    pending: dict[str, int] = {}
    oldest = ""
    for task_id in queue.pending_ids():
        task = queue.load(task_id) or {}
        kind = task.get("kind", "?")
        pending[kind] = pending.get(kind, 0) + 1
        created = str(task.get("created_at", "") or "")
        if created and (not oldest or created < oldest):
            oldest = created

    return {
        "day": day,
        "answered": answered,
        "settled": settled,
        "checked": checked,
        "pending": pending,
        "oldest_pending": oldest,
        "stale_definitions": len(stale_definitions(cfg)),
        "stale_findings": len(stale_findings(cfg)),
        "stale_analysis": len(stale_analysis(cfg)),
    }


def render_section(facts: dict) -> str:
    """The derived block, between the markers. Never anything a person wrote."""
    day = facts["day"]
    lines = [BEGIN, "", f"## Session — {day.isoformat()}", ""]

    answered = facts["answered"]
    if answered:
        parts = [
            f"{answered[kind]} {kind}"
            for kind in _KIND_ORDER
            if answered.get(kind)
        ]
        parts += [
            f"{count} {kind}"
            for kind, count in sorted(answered.items())
            if kind not in _KIND_ORDER
        ]
        lines.append(f"Answered {sum(answered.values())} task(s): {', '.join(parts)}.")
    else:
        lines.append("No task was answered.")

    if facts["settled"]:
        lines += ["", f"**Settled {len(facts['settled'])}**"]
        for finding in facts["settled"]:
            label = "Decision" if finding.kind == "decision" else "Established"
            lines.append(f"- **{label}** — {finding.statement}")

    if facts["checked"]:
        lines += ["", f"**Checked outside the archive**"]
        for reference in facts["checked"]:
            lines.append(f"- [{reference.title or reference.url}]({reference.url})")

    # The part that is an input rather than a record.
    lines += ["", "**Left for the next night**", ""]
    pending = facts["pending"]
    if pending:
        for kind in _KIND_ORDER:
            if pending.get(kind):
                lines.append(f"- {pending[kind]} {kind} task(s) waiting")
        for kind, count in sorted(pending.items()):
            if kind not in _KIND_ORDER:
                lines.append(f"- {count} {kind} task(s) waiting")
        if facts["oldest_pending"]:
            lines.append(f"- the oldest has been waiting since {facts['oldest_pending'][:10]}")
    else:
        lines.append("- nothing is unread")

    for count, what in (
        (facts["stale_definitions"], "definition(s) their evidence has outgrown"),
        (facts["stale_findings"], "finding(s) their subject has outgrown"),
        (facts["stale_analysis"], "hand-written section(s) outgrown by their sources"),
    ):
        if count:
            lines.append(f"- {count} {what}")

    lines += ["", END, ""]
    return "\n".join(lines)


def write(cfg: Config, day: date | None = None) -> Path:
    """Write the session block into the day's page, keeping everything else."""
    day = day or date.today()
    page = cfg.layout.archive_daily / f"{day.isoformat()}.md"
    section = render_section(gather(cfg, day))

    existing = page.read_text(encoding="utf-8") if page.exists() else ""
    if BEGIN in existing and END in existing:
        # Replace in place. Re-running a digest must not stack copies of itself,
        # and must not disturb either `run_daily`'s half above it or whatever a
        # session wrote below.
        pattern = re.compile(
            re.escape(BEGIN) + ".*?" + re.escape(END) + r"\n?", re.DOTALL
        )
        updated = pattern.sub(section, existing, count=1)
    elif existing:
        updated = existing.rstrip() + "\n\n" + section
    else:
        updated = f"# Research digest — {day.isoformat()}\n\n" + section

    write_text(page, updated)
    _LOG.info("session digest written: %s", page)
    return page


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.digest",
        description="Record what a night of reading did, in the archive itself.",
    )
    parser.add_argument("--date", default="", help="YYYY-MM-DD (default: today)")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    args = parser.parse_args(argv)

    cfg = config_mod.load(args.root)
    log.setup(cfg.layout.logs, logging.DEBUG if args.verbose else logging.INFO)
    cfg.layout.ensure()

    day = date.fromisoformat(args.date) if args.date else date.today()
    print(write(cfg, day))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
