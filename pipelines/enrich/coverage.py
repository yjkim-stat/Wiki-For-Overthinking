"""What we have of a day, against what that day held.

Every other counter in this system measures what it found. None of them could
tell the difference between "arXiv announced nothing today" and "we failed to
read what arXiv announced today", and those look identical in a log: a small
number, no error. This is the ledger that tells them apart.

Three counts per category-day, and they are three different questions:

``announced``
    What the listing page says the day holds. arXiv's own number, not ours.
``listed``
    How many of those identifiers we actually paginated through. Short of
    ``announced`` means we stopped early — a page cap, a dead host mid-crawl.
``captured``
    How many of those we hold an abstract for. Short of ``listed`` means the
    identifiers are known and the abstracts are not, which is the cheap gap to
    close because we know exactly what to ask for.

A gap is not an error and is not repaired in one run. It is a debt, recorded so
that later runs can pay it down and so that a person can see it. A day whose
`announced` never gets matched is telling you something real about the source,
and silently retrying forever would hide it.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field

from ..common.paths import Layout
from ..common.schema import utcnow
from ..common.store import read_jsonl, rewrite_jsonl


@dataclass
class DayCoverage:
    """One category on one announcement day."""

    category: str
    day: str  # ISO date; "" when the page did not say which day it was
    announced: int = 0
    listed: int = 0
    captured: int = 0
    checked_at: str = field(default_factory=utcnow)

    @property
    def key(self) -> tuple[str, str]:
        return (self.category, self.day)

    @property
    def listing_gap(self) -> int:
        """Identifiers the day holds that we have never seen."""
        return max(0, self.announced - self.listed)

    @property
    def abstract_gap(self) -> int:
        """Identifiers we have seen but hold no abstract for."""
        return max(0, self.listed - self.captured)

    @property
    def complete(self) -> bool:
        return self.listing_gap == 0 and self.abstract_gap == 0


def path_for(layout: Layout):
    return layout.index / "coverage.jsonl"


def load(layout: Layout) -> dict[tuple[str, str], DayCoverage]:
    """Every recorded day, keyed by ``(category, day)``."""
    rows: dict[tuple[str, str], DayCoverage] = {}
    for raw in read_jsonl(path_for(layout)):
        try:
            row = DayCoverage(
                category=str(raw.get("category", "")),
                day=str(raw.get("day", "")),
                announced=int(raw.get("announced", 0)),
                listed=int(raw.get("listed", 0)),
                captured=int(raw.get("captured", 0)),
                checked_at=str(raw.get("checked_at", "")),
            )
        except (TypeError, ValueError):
            # A malformed row is one day's bookkeeping, not the ledger.
            continue
        if row.category:
            rows[row.key] = row
    return rows


def record(layout: Layout, updates: list[DayCoverage]) -> dict[str, int]:
    """Merge ``updates`` into the ledger and rewrite it.

    A day's counts only ever go up. A later run that paginated fewer pages must
    not erase what an earlier one established — the ledger is a high-water mark
    of what has been seen, not a snapshot of the last run.
    """
    rows = load(layout)
    for update in updates:
        existing = rows.get(update.key)
        if existing is None:
            rows[update.key] = update
            continue
        existing.announced = max(existing.announced, update.announced)
        existing.listed = max(existing.listed, update.listed)
        existing.captured = max(existing.captured, update.captured)
        existing.checked_at = update.checked_at or existing.checked_at

    ordered = sorted(rows.values(), key=lambda r: (r.category, r.day))
    rewrite_jsonl(path_for(layout), [asdict(r) for r in ordered])
    return {
        "days": len(ordered),
        "incomplete": sum(1 for r in ordered if not r.complete),
    }


def gaps(layout: Layout) -> list[DayCoverage]:
    """Days that are short, worst first.

    Ordered by what is missing rather than by date, so a run that can only
    afford a bounded amount of repair spends it where the hole is biggest.
    """
    return sorted(
        (row for row in load(layout).values() if not row.complete),
        key=lambda r: -(r.listing_gap + r.abstract_gap),
    )


def summarize(layout: Layout) -> dict[str, int]:
    """Counts for a run's result dict."""
    rows = list(load(layout).values())
    return {
        "days": len(rows),
        "incomplete_days": sum(1 for r in rows if not r.complete),
        "missing_listings": sum(r.listing_gap for r in rows),
        "missing_abstracts": sum(r.abstract_gap for r in rows),
    }
