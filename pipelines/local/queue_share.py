"""Stop a reading backlog from starving the wiki's own definition queue.

`render` files summary tasks first and definition tasks second, against one
shared `max_pending_tasks` cap. With any reading backlog at all the summaries
took every slot and no definition task was ever filed — 82 were generated here
in one run and none queued, logged only at WARNING level inside a run that
otherwise reported success.

It fails worst exactly when it matters most. A repository collecting actively
always has unread papers, so the wiki stops extending itself precisely while it
is accumulating the most evidence — and a self-extending wiki is what the
promotion threshold exists to serve.

The fix is a reserve rather than a reordering, because queueing definitions
first would simply invert which kind of work starves. The reserve is handed back
if definitions do not want it, so a render with no pending definitions files
exactly as many summaries as before.

See `docs/commit-local/0022-a-reading-backlog-starved-the-wiki.md`.
"""

from __future__ import annotations

from ..common.config import Config


def pending_cap(cfg: Config) -> int | None:
    """The configured ceiling on pending tasks, or None for no ceiling."""
    return (
        int((cfg.settings.get("summarize", {}) or {}).get("max_pending_tasks", 0))
        or None
    )


def summary_cap(cfg: Config) -> int | None:
    """How many slots summaries may take on the first pass.

    Half the cap, rounded in favour of reading. Definitions are generated *from*
    completed summaries, so the definition backlog is bounded by work already
    done and drains; the reading backlog is fed by collection and does not. The
    bounded queue is the one that can afford to wait.
    """
    cap = pending_cap(cfg)
    return cap if cap is None else (cap + 1) // 2


def pending_count(cfg: Config) -> int:
    """How many tasks are pending right now.

    `render` calls `queue_missing_summaries` twice — once against the reserve
    and once with the remainder — and each call returns how many records lack a
    summary, not how many tasks it filed. Summing the two returns therefore
    double-counts every record that was still unread on both passes: a steady
    backlog of 37 was reported as 74.

    Measuring the queue on either side of a call gives the number the field
    claims to hold. It is also the only number that stays honest when the cap
    binds and a task is dropped rather than filed.
    """
    return sum(1 for _ in cfg.layout.queue_pending.glob("*.json"))
