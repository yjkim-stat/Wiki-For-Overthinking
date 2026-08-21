"""Questions that span more readings than any one of them answers.

    python -m pipelines.enrich.synthesis add --question "..." \
        [--concept <slug>] [--paper <id>] [--topic <slug>]
    python -m pipelines.enrich.synthesis list

The queue had three kinds — a paper, a talk, an entity — and each is one record
answered from its own material. The work that actually moves an archive forward
is the other shape: *read these twelve and tell me whether X*. There was nowhere
to put that, so it happened inside a session, was validated by nothing, could not
be handed to the next night, and survived only in a commit message.

This is the fourth kind, and the thing that makes it worth having is where the
answer goes. **A settled synthesis is a finding** — the group's own position,
recorded through `enrich/findings.py` and checked by the validator that owns
them. There is no second path into `data/findings/`.

**Leaving a question open is a real answer.** The evidence often does not settle
things, and a task that demanded a statement would be asking the reader to
invent one. An answer may instead say in `unresolved` why it could not be
settled; the task is archived carrying that reason, where the next session finds
it.

**Nothing here writes an answer.** The pipeline calls no model, and a finding
whose author was a counter would not be the group's position — which is the one
property that makes `data/findings/` worth keeping apart from the literature.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from ..common import config as config_mod
from ..common import paths as P
from ..common.config import Config
from ..common.log import get
from ..common.schema import title_fingerprint
from ..common.store import RecordStore
from .queue import Queue

_LOG = get(__name__)

SYNTHESIS_OUTPUT_SCHEMA: dict[str, Any] = {
    "statement": (
        "string - one sentence somebody could disagree with, settling the "
        "question. Leave empty if the evidence does not settle it"
    ),
    "kind": "string - one of: decision (the group chose) | fact (it established)",
    "rationale": "string - what settled it, and against which evidence",
    "concepts": ["string - entity names this bears on"],
    "papers": ["string - canonical ids of archived papers it rests on"],
    "references": ["string - ids of recorded external references, if any"],
    "topics": ["string - tracked topic slugs"],
    "supersedes": "string - id of a finding this replaces, if any",
    "unresolved": (
        "string - required *instead of* `statement` when the evidence does not "
        "settle the question: what is missing, and what would settle it"
    ),
}


def instructions(question: str, language: str = "en") -> str:
    return (
        f"{question}\n\n"
        "The evidence below is every archived record this question was filed "
        "against — readings, entity definitions and settled findings. Answer "
        "from those, and from the archive around them if you need to look.\n\n"
        "**If they settle it**, write one sentence somebody could disagree "
        "with, and say in `rationale` what settled it. Name the papers it rests "
        "on in `papers`; they are checked against the archive, so cite what is "
        "there rather than what you remember.\n\n"
        "**If they do not**, leave `statement` empty and say in `unresolved` "
        "what is missing and what would settle it. That is a real answer and it "
        "is recorded as one. A statement hedged until it cannot be argued with "
        "is worse than an honest open question, because nothing later can tell "
        "the two apart.\n\n"
        f"Write in {language}. Return one JSON object matching the schema "
        "exactly, with no prose around it."
    )


def _excerpt(text: str, limit: int = 400) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def gather(
    cfg: Config,
    store: RecordStore,
    *,
    concepts: list[str],
    papers: list[str],
) -> tuple[list[dict], list[str], list[str]]:
    """The records a question is to be answered from, with their own words.

    Returns ``(evidence, topics, problems)``. A named record that is not in the
    archive is a problem rather than an omission: a question filed against
    evidence that does not exist would be answered from memory, which is the one
    thing this whole arrangement is built to prevent.
    """
    evidence: list[dict] = []
    topics: set[str] = set()
    problems: list[str] = []

    for slug in concepts:
        concept = store.load_concept(slug)
        if concept is None:
            problems.append(f"no such entity: {slug}")
            continue
        topics.update(concept.topics)
        evidence.append(
            {
                "kind": "concept",
                "id": concept.slug,
                "title": concept.name,
                "note": _excerpt(concept.definition),
                "sources": concept.mention_count,
            }
        )

    for paper_id in papers:
        paper = store.load_paper(paper_id)
        if paper is None:
            problems.append(f"not in the archive: {paper_id}")
            continue
        topics.update(paper.topics)
        summary = store.load_paper_summary(paper_id)
        evidence.append(
            {
                "kind": "paper",
                "id": paper.id,
                "title": paper.title,
                "note": _excerpt(
                    summary.one_liner if summary else paper.abstract
                ),
                "read": summary is not None,
            }
        )

    return evidence, sorted(topics), problems


def file_question(
    cfg: Config,
    question: str,
    *,
    concepts: list[str] | None = None,
    papers: list[str] | None = None,
    topics: list[str] | None = None,
    queue: Queue | None = None,
) -> str:
    """File one synthesis task. Returns its id, or ``""`` if it was not filed."""
    question = " ".join((question or "").split())
    if len(question) < 12:
        raise ValueError("a question that short cannot be answered or argued with")

    store = RecordStore(cfg.layout)
    queue = queue or Queue(cfg.layout, cfg=cfg)
    evidence, derived, problems = gather(
        cfg, store, concepts=concepts or [], papers=papers or []
    )
    if problems:
        raise ValueError(
            "the question names evidence the archive does not have:\n  - "
            + "\n  - ".join(problems)
        )

    known = {topic.slug for topic in cfg.topics}
    wanted = [t for t in (topics or derived) if t in known]

    return queue.enqueue(
        kind="synthesis",
        # Content-addressed on the question, so filing the same one twice is one
        # task — and so a session leaving a question for the next night cannot
        # accumulate duplicates of its own asking.
        item_id=f"q:{title_fingerprint(question)}",
        topics=wanted,
        language=cfg.language,
        instructions=instructions(question, cfg.language),
        output_schema=SYNTHESIS_OUTPUT_SCHEMA,
        payload={"question": question, "evidence_count": len(evidence)},
        attachments={"evidence": evidence},
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.enrich.synthesis",
        description="Ask a question that spans more readings than one.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="file a question")
    p_add.add_argument("--question", required=True)
    p_add.add_argument("--concept", action="append", dest="concepts", default=[])
    p_add.add_argument("--paper", action="append", dest="papers", default=[])
    p_add.add_argument("--topic", action="append", dest="topics", default=[])

    p_list = sub.add_parser("list", help="questions waiting for an answer")
    p_list.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    cfg.layout.ensure()
    queue = Queue(cfg.layout, cfg=cfg)

    if args.command == "add":
        try:
            task_id = file_question(
                cfg,
                args.question,
                concepts=args.concepts,
                papers=args.papers,
                topics=args.topics,
                queue=queue,
            )
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        if not task_id:
            print("already asked, or the queue is at its cap", file=sys.stderr)
            return 1
        print(task_id)
        return 0

    if args.command == "list":
        rows = []
        for task_id in queue.pending_ids(kind="synthesis"):
            task = queue.load(task_id) or {}
            rows.append(
                {
                    "task_id": task_id,
                    "question": (task.get("payload") or {}).get("question", ""),
                    "evidence": len((task.get("attachments") or {}).get("evidence", [])),
                    "topics": task.get("topics") or [],
                }
            )
        if args.json:
            print(json.dumps(rows, indent=2, ensure_ascii=False))
        elif not rows:
            print("no questions waiting")
        else:
            for row in rows:
                print(f"{row['task_id']}\t{row['evidence']} source(s)\t{row['question']}")
        return 0

    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
