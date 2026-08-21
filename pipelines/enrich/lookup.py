"""Narrow questions the archive cannot answer about itself.

    python -m pipelines.enrich.lookup add --subject spelling --about "C-LAP"
    python -m pipelines.enrich.lookup add --subject document --paper arxiv:2401.12345
    python -m pipelines.enrich.lookup list

Much of what sits unresolved in an archive is not *judgement* but *confirmation*.
Whether the published spelling is `C-LAP` or `CLAP`; whether `PAI-Bench` and
`PAIBench` are one benchmark; where a paper's PDF actually lives; whether a
method has published code. Each is one look at something outside the archive,
and there was nowhere to file that look — so it either happened inside a session
and evaporated, or never happened at all.

**Every answer must carry a reference, and that is the whole point.** A recorded
reference has a URL, a retrieval date and the passage relied on
(`enrich/references.py`). Requiring one is the only mechanical difference
between "I looked this up" and "I remember this" — the pipeline cannot tell those
apart any other way, and on a question whose entire value is that somebody
checked, it is the difference that matters.

**`unknown` is always a valid answer, and the only one that needs no reference.**
A lookup that failed is worth recording: the next session sees that it was tried
and what was tried, rather than asking again from nothing.

**A confirmed identity never edits `data/` here.** An alias is a merge
mechanism, and a wrong merge does not mislabel an entity — it fuses two, and the
fused note looks perfectly healthy afterwards. So a confirmed identity files a
definition revision for the surviving entity and the alias goes in through the
validator that owns aliases, with a reader looking at it.
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

#: What a lookup can be about. Closed, because each shape has a different
#: answer and a different thing to check about it.
SUBJECTS = ("spelling", "identity", "document", "artifact")

_ASKS = {
    "spelling": (
        "How is '{about}' spelled where it was published? Find the paper, "
        "repository or venue page that introduced it and read the name off "
        "that, not off a citation of it."
    ),
    "identity": (
        "Are these the same thing: {about}? Answer 'yes' or 'no' in `answer`, "
        "and say in `rationale` what settled it. If they are the same, the "
        "archive will ask separately for the alias — do not assume which name "
        "survives."
    ),
    "document": (
        "Where is the document for '{about}'? Put a direct http(s) URL to the "
        "PDF in `answer`. The archive will fetch it; do not paste its contents."
    ),
    "artifact": (
        "Is there published code, a model card or a dataset for '{about}'? "
        "Record what you find as a reference and name its id in `references`."
    ),
}

LOOKUP_OUTPUT_SCHEMA: dict[str, Any] = {
    "answer": (
        "string - the resolved value: the published spelling, a direct URL, or "
        "'yes'/'no'. Leave empty only when setting `unknown`"
    ),
    "unknown": (
        "boolean - true when it could not be established. Then `answer` is "
        "empty and no reference is required, but say in `rationale` what you "
        "looked at, so the next attempt starts from somewhere"
    ),
    "rationale": "string - one paragraph: what settled it, or what did not",
    "references": [
        "string - id of a recorded reference. **At least one is required** "
        "unless `unknown`. Record the page first with "
        "`pipelines.enrich.references add`; an answer without one cannot be "
        "told from a remembered answer"
    ],
}


def instructions(subject: str, about: str, language: str = "en") -> str:
    return (
        _ASKS[subject].format(about=about)
        + "\n\n"
        "**Record what you consulted as a reference and cite it.** An answer "
        "with no reference is refused, and that refusal is the only thing "
        "separating a page you read from a fact you recall.\n\n"
        "If you cannot establish it, set `unknown` and say what you tried. "
        "That is a real answer and it stops the next session repeating your "
        "search from nothing.\n\n"
        f"Write in {language}. Return one JSON object matching the schema "
        "exactly, with no prose around it."
    )


def file_lookup(
    cfg: Config,
    subject: str,
    about: str,
    *,
    paper: str = "",
    concept: str = "",
    queue: Queue | None = None,
) -> str:
    """File one lookup. Returns its task id, or ``""`` if it was already asked."""
    if subject not in SUBJECTS:
        raise ValueError(f"subject must be one of: {', '.join(SUBJECTS)}")
    about = " ".join((about or "").split())
    store = RecordStore(cfg.layout)

    topics: list[str] = []
    if paper:
        record = store.load_paper(paper)
        if record is None:
            raise ValueError(f"not in the archive: {paper}")
        topics = list(record.topics)
        about = about or record.title
    if concept:
        entity = store.load_concept(concept)
        if entity is None:
            raise ValueError(f"no such entity: {concept}")
        topics = topics or list(entity.topics)
        about = about or entity.name

    if not about:
        raise ValueError("a lookup needs something to be about")

    queue = queue or Queue(cfg.layout, cfg=cfg)
    return queue.enqueue(
        kind="lookup",
        # Content-addressed on the subject and what it is about, so the same
        # question asked twice is one task and a failed lookup is not silently
        # re-asked every night.
        item_id=f"{subject}:{title_fingerprint(about)}",
        topics=topics,
        language=cfg.language,
        instructions=instructions(subject, about, cfg.language),
        output_schema=LOOKUP_OUTPUT_SCHEMA,
        payload={
            "subject": subject,
            "about": about,
            "paper": paper,
            "concept": concept,
        },
        attachments={},
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.enrich.lookup",
        description="Ask for something the archive cannot answer about itself.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="file a lookup")
    p_add.add_argument("--subject", required=True, choices=SUBJECTS)
    p_add.add_argument("--about", default="")
    p_add.add_argument("--paper", default="")
    p_add.add_argument("--concept", default="")

    p_list = sub.add_parser("list", help="lookups waiting for an answer")
    p_list.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    cfg.layout.ensure()
    queue = Queue(cfg.layout, cfg=cfg)

    if args.command == "add":
        try:
            task_id = file_lookup(
                cfg, args.subject, args.about,
                paper=args.paper, concept=args.concept, queue=queue,
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
        for task_id in queue.pending_ids(kind="lookup"):
            payload = (queue.load(task_id) or {}).get("payload") or {}
            rows.append(
                {
                    "task_id": task_id,
                    "subject": payload.get("subject", ""),
                    "about": payload.get("about", ""),
                }
            )
        if args.json:
            print(json.dumps(rows, indent=2, ensure_ascii=False))
        elif not rows:
            print("no lookups waiting")
        else:
            for row in rows:
                print(f"{row['task_id']}\t{row['subject']:9}\t{row['about']}")
        return 0

    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
