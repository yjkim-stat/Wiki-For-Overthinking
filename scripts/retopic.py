#!/usr/bin/env python3
"""Re-score stored records against the current topic definitions.

Topics are matched at collection time. That is the right default — a run should
be reproducible from what the collectors saw — but it means an edit to
`config/topics/` only affects what arrives next. Adding a topic, or widening a
topic's keywords, leaves the existing archive describing the old editorial
decision.

This walks the stored papers and videos, re-scores each against the current
topics, and adds any slug that now accepts it.

**It only ever adds.** A slug already on a record stays, for two reasons. For a
hand-filed PDF the topics are the reader's judgement, and a keyword rule must
not overrule an editorial decision. For a collected item, removing a slug would
silently delete the archive page and the topic outputs built from it, which is a
destructive act a re-scoring pass should not perform. To drop a topic, delete
its file and let the renderer clean up.

Pass ``--topic`` to apply one slug only. That is the common case — a topic has
just been added and should be applied to what is already stored — and it keeps
the operation reviewable. Without it, every topic is re-scored, which will also
attach slugs a reader never assigned and for which the summary therefore has no
``relevance`` entry, so those topics' reports will list the paper with no text
explaining why it is there.

    python3 scripts/retopic.py --topic reasoning-interpretability
    python3 -m pipelines.render          # afterwards, to rebuild
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipelines.common import config as config_mod  # noqa: E402
from pipelines.common.store import RecordStore  # noqa: E402
from pipelines.enrich.score import score_against_topics  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="report what would change, write nothing"
    )
    parser.add_argument(
        "--topic",
        action="append",
        metavar="SLUG",
        help="only add this slug; repeatable. Omit to consider every topic.",
    )
    args = parser.parse_args()

    cfg = config_mod.load()
    if not cfg.topics:
        print("no topics defined; nothing to do")
        return 0
    wanted = set(args.topic or [])
    known = {t.slug for t in cfg.topics}
    unknown = wanted - known
    if unknown:
        print(f"unknown topic(s): {', '.join(sorted(unknown))}")
        return 2
    store = RecordStore(cfg.layout)

    def new_slugs(accepted: list[str], current: list[str]) -> list[str]:
        return [s for s in accepted if s not in current and (not wanted or s in wanted)]

    changed = 0
    for paper in store.iter_papers():
        _, _, accepted = score_against_topics(
            cfg.topics,
            title=paper.title,
            body=paper.abstract,
            authors=paper.authors,
            settings=cfg.settings,
        )
        added = new_slugs(accepted, paper.topics)
        if not added:
            continue
        changed += 1
        print(f"  + {','.join(added):28} {paper.title[:58]}")
        if not args.dry_run:
            paper.topics = list(paper.topics) + added
            store.save_paper(paper)

    for video in store.iter_videos():
        _, _, accepted = score_against_topics(
            cfg.topics,
            title=video.title,
            body=video.description,
            settings=cfg.settings,
        )
        added = new_slugs(accepted, video.topics)
        if not added:
            continue
        changed += 1
        print(f"  + {','.join(added):28} {video.title[:58]}")
        if not args.dry_run:
            video.topics = list(video.topics) + added
            store.save_video(video)

    verb = "would gain" if args.dry_run else "gained"
    print(f"\n{changed} record(s) {verb} a topic")
    if changed and not args.dry_run:
        print("run `python3 -m pipelines.render` to rebuild the archive and wiki")
    return 0


if __name__ == "__main__":
    sys.exit(main())
