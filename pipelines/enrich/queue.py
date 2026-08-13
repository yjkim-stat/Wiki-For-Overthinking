"""The summarization work queue.

This is the seam between the deterministic pipeline and whatever writes the
summaries. ``run_daily.py`` files a task; the daily Claude Code session (or a
future API backend) answers it; ``render.py`` consumes the answer.

A task file is self-contained on purpose — instructions, output schema and all
the source material in one place — so that whoever picks it up needs no other
context and no access to the rest of the repository.

Command line:

    python -m pipelines.enrich.queue stats
    python -m pipelines.enrich.queue list --kind paper
    python -m pipelines.enrich.queue next
    python -m pipelines.enrich.queue show <task_id>
    python -m pipelines.enrich.queue complete <task_id> --file result.json
    cat result.json | python -m pipelines.enrich.queue complete <task_id> --stdin
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterator

from ..common import config as config_mod
from ..common.log import get
from ..common import paths as P
from ..common.paths import Layout, fs_id
from ..common.schema import utcnow
from ..common.store import read_json, write_json

_LOG = get(__name__)

TASK_VERSION = 1

_REQUIRED_FIELDS = {
    "paper": ["one_liner", "problem", "contributions", "method"],
    "video": ["one_liner", "abstract", "key_points"],
    "concept": ["definition"],
}

_LIST_FIELDS = {
    # `topics` is optional and only honoured for a hand-filed PDF, where the
    # reader decides which tracked topics the document belongs to.
    "paper": ["contributions", "concepts", "methods", "datasets", "tags", "topics"],
    "video": [
        "chapters",
        "key_points",
        "referenced_papers",
        "concepts",
        "methods",
        "datasets",
        "tags",
    ],
    "concept": ["aliases", "related"],
}

_KINDS = tuple(_REQUIRED_FIELDS)

#: What a reading may say it was based on. ``document`` is a claim the task can
#: check; ``abstract`` is one it cannot, and does not need to.
READING_BASIS = ("document", "abstract")


def _check_reading_basis(
    result: dict, attachments: dict[str, Any] | None
) -> list[str]:
    """Whether a paper reading says what it was based on, and may say it.

    Asked of every paper task and answerable only by the reader: nothing in the
    pipeline can observe whether a PDF was opened. What the task *can* do is
    refuse the one direction that is checkable — a reading cannot have been
    based on a document that was never attached to it.
    """
    basis = result.get("read_from")
    if basis is not None and not isinstance(basis, str):
        return ["field `read_from` must be a string"]
    basis = (basis or "").strip()

    if basis and basis not in READING_BASIS:
        return [
            f"field `read_from` must be one of {', '.join(READING_BASIS)} "
            f"(got '{basis}')"
        ]
    if attachments is None:
        return []

    if attachments.get("pdf_path"):
        if not basis:
            return [
                "missing or empty required field: read_from — this task "
                "attached a document, so say whether you read it ('document') "
                "or worked from the abstract ('abstract')"
            ]
    elif basis == "document":
        return [
            "`read_from` says 'document', but this task attached none — a "
            "reading cannot be based on a document it was never given"
        ]
    return []


def validate_result(
    kind: str,
    result: Any,
    topics: list[str] | None = None,
    attachments: dict[str, Any] | None = None,
) -> list[str]:
    """Check a submitted result against the contract. Returns error strings.

    ``topics`` is the task's own topic list. It is optional so the two-argument
    signature keeps working, but without it the ``relevance`` keys cannot be
    checked against anything — a paper's relevance decides which topic page it
    renders under, and a key naming a slug the task does not have renders
    nowhere at all.

    ``attachments`` is the task's own attachment block, and the same reasoning
    applies to ``read_from``: whether a reading had to open a document is a fact
    about the task, not about the answer, so a validator that cannot see the
    task cannot tell a true claim from a false one.

    The three states are distinct on purpose. ``None`` means no context was
    given and only the value itself is checked. ``{}`` means the task carried no
    document — nothing to open, so nothing is required, but claiming to have
    read one is rejected. A block with ``pdf_path`` means the reader was handed
    a document and has to say whether they used it.
    """
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["result must be a JSON object"]

    if kind not in _REQUIRED_FIELDS:
        return [f"unknown task kind: {kind}"]

    for name in _REQUIRED_FIELDS[kind]:
        value = result.get(name)
        if value is None or (isinstance(value, (str, list)) and not value):
            errors.append(f"missing or empty required field: {name}")

    for name in _LIST_FIELDS[kind]:
        if name in result and not isinstance(result[name], list):
            errors.append(f"field `{name}` must be a list")

    if kind == "paper":
        relevance = result.get("relevance", {})
        if relevance and not isinstance(relevance, dict):
            errors.append("field `relevance` must be an object keyed by topic slug")
        else:
            # Which topics a paper belongs to is settled in one of two ways, and
            # only one of them is authoritative here.
            #
            # A collected paper was scored, so the task's topics *are* the
            # answer: relevance must cover them exactly. A hand-filed PDF is the
            # other case — its task carries every tracked topic as a menu,
            # because the reader is the one deciding, and their answer is itself
            # filtered against the real topic list when it is applied. There is
            # nothing settled to require coverage against, so coverage is not
            # required. A key outside their answer is still wrong, because it
            # renders nowhere.
            declared = result.get("topics")
            reader_assigned = isinstance(declared, list)
            allowed = set(declared) if reader_assigned else set(topics or [])
            required = set() if reader_assigned else set(topics or [])

            if topics or reader_assigned:
                keys = set(relevance or {})
                for extra in sorted(keys - allowed):
                    errors.append(
                        f"`relevance` names '{extra}', which is not one of this "
                        f"paper's topics: {', '.join(sorted(allowed)) or '(none)'}"
                    )
                for missing in sorted(required - keys):
                    errors.append(f"`relevance` is missing an entry for '{missing}'")
                for slug, text in (relevance or {}).items():
                    if slug in allowed and not str(text).strip():
                        errors.append(f"`relevance['{slug}']` is empty")

        errors.extend(_check_reading_basis(result, attachments))

        bibliography = result.get("bibliography")
        if bibliography is not None:
            if not isinstance(bibliography, dict):
                errors.append("field `bibliography` must be an object")
            else:
                if not isinstance(bibliography.get("authors", []), list):
                    errors.append("field `bibliography.authors` must be a list")
                year = bibliography.get("year", 0)
                if not isinstance(year, int) or isinstance(year, bool):
                    errors.append("field `bibliography.year` must be an integer")

    if kind == "concept":
        declared = result.get("kind")
        if declared and declared not in ("concept", "method", "dataset"):
            errors.append(
                f"field `kind` must be concept, method or dataset (got '{declared}')"
            )

    if kind == "video":
        for index, chapter in enumerate(result.get("chapters", []) or []):
            if not isinstance(chapter, dict):
                errors.append(f"chapters[{index}] must be an object")
                continue
            # Required, not defaulted: a chapter exists so a reader can jump to
            # it, and a missing timestamp rendered as 0:00 is indistinguishable
            # from a legitimate first chapter. Wrong is worse than absent here.
            # `bool` is a subclass of `int`, so it is excluded explicitly.
            if "start_s" not in chapter:
                errors.append(f"chapters[{index}].start_s is required")
            elif not isinstance(chapter["start_s"], (int, float)) or isinstance(
                chapter["start_s"], bool
            ):
                errors.append(f"chapters[{index}].start_s must be a number")

    return errors


class Queue:
    """File-backed queue of pending and completed summarization tasks."""

    def __init__(self, layout: Layout, max_pending: int | None = None) -> None:
        self.layout = layout
        self.max_pending = max_pending

    # -- paths --------------------------------------------------------------
    @staticmethod
    def task_id(kind: str, item_id: str) -> str:
        return f"{kind}__{fs_id(item_id)}"

    def pending_path(self, task_id: str) -> Path:
        return self.layout.queue_pending / f"{task_id}.json"

    def done_path(self, task_id: str) -> Path:
        return self.layout.queue_done / f"{task_id}.json"

    def archive_path(self, task_id: str) -> Path:
        return self.layout.queue_archive / f"{task_id}.json"

    # -- producing ----------------------------------------------------------
    def enqueue(
        self,
        *,
        kind: str,
        item_id: str,
        topics: list[str],
        language: str,
        instructions: str,
        output_schema: dict[str, Any],
        payload: dict[str, Any],
        attachments: dict[str, Any] | None = None,
    ) -> str:
        """File a task.

        Returns its id when a new task was filed, and ``""`` otherwise — which
        includes the case where a task was already pending and has been brought
        up to date in place. A refresh writes, but it does not add anything to
        the backlog, and callers count what the backlog gained.
        """
        task_id = self.task_id(kind, item_id)
        pending = self.pending_path(task_id)

        # An answered task is never rewritten. A reader may have worked from the
        # version they were given, and replacing its material underneath them
        # would make the answer describe something else.
        if self.done_path(task_id).exists():
            return ""

        task = {
            "task_version": TASK_VERSION,
            "task_id": task_id,
            "kind": kind,
            "item_id": item_id,
            "topics": topics,
            "language": language,
            "created_at": utcnow(),
            "instructions": instructions,
            "output_schema": output_schema,
            "payload": payload,
            "attachments": attachments or {},
        }

        if pending.exists():
            return self._refresh(pending, task)

        if self.max_pending is not None and self.count_pending() >= self.max_pending:
            _LOG.warning(
                "queue is at its cap of %d pending tasks; skipping %s",
                self.max_pending,
                task_id,
            )
            return ""

        write_json(pending, task)
        _LOG.info("queued %s", task_id)
        return task_id

    def _refresh(self, pending: Path, task: dict) -> str:
        """Bring a waiting task up to date with the record it was built from.

        A task used to be whatever its record looked like on the day it was
        filed, for ever. That is wrong in the one direction that matters: a
        document can arrive after the task, and then the reader is handed a
        paper's abstract while the PDF sits on disk beside it — and, because the
        prompt and the schema are chosen by whether a document is attached, is
        also asked the wrong question and given nowhere to record the answer.
        The correct task was rebuilt on every render and discarded on every
        render by the guard this replaces.

        Two things are kept rather than rebuilt. ``created_at``, because it is
        how long this item has been waiting and nothing else records that; a
        task that quietly became newer would corrupt any ordering built on it.
        And nothing at all if the rebuild is identical — a render over an
        unchanged archive must not rewrite the queue, for the same reason it
        must not rewrite a concept record.
        """
        stored = read_json(pending) or {}
        task["created_at"] = stored.get("created_at") or task["created_at"]
        if stored == task:
            return ""
        write_json(pending, task)
        _LOG.info("refreshed %s", task["task_id"])
        return ""

    # -- consuming ----------------------------------------------------------
    def count_pending(self) -> int:
        return sum(1 for _ in self.layout.queue_pending.glob("*.json"))

    def pending_ids(self, kind: str | None = None) -> list[str]:
        ids = []
        for path in sorted(self.layout.queue_pending.glob("*.json")):
            if kind and not path.name.startswith(f"{kind}__"):
                continue
            ids.append(path.stem)
        return ids

    def load(self, task_id: str) -> dict | None:
        for path in (
            self.pending_path(task_id),
            self.done_path(task_id),
            self.archive_path(task_id),
        ):
            data = read_json(path)
            if data:
                return data
        return None

    def complete(self, task_id: str, result: dict[str, Any]) -> Path:
        """Record a finished task, moving it from pending to done."""
        pending = self.pending_path(task_id)
        task = read_json(pending)
        if not task:
            raise FileNotFoundError(f"no pending task with id '{task_id}'")

        # Both context arguments come from the task rather than the answer, so
        # a claim the answer makes about itself can be checked against what was
        # actually handed over. `attachments` is passed as stored — `{}` is a
        # task that carried no document, and is not the same as no context.
        errors = validate_result(
            task["kind"],
            result,
            task.get("topics") or None,
            task.get("attachments"),
        )
        if errors:
            raise ValueError(
                f"result for '{task_id}' is invalid:\n  - " + "\n  - ".join(errors)
            )

        task["completed_at"] = utcnow()
        task["result"] = result
        done = self.done_path(task_id)
        write_json(done, task)
        pending.unlink(missing_ok=True)
        _LOG.info("completed %s", task_id)
        return done

    def iter_done(self, kind: str | None = None) -> Iterator[dict]:
        for path in sorted(self.layout.queue_done.glob("*.json")):
            if kind and not path.name.startswith(f"{kind}__"):
                continue
            data = read_json(path)
            if data:
                yield data

    def reopen(self, task_id: str) -> Path:
        """Return a completed task to pending, keeping its material.

        For a reader who spots their own mistake before ``render`` consumes the
        answer. Completion is otherwise one-way, and that pushes people toward
        editing ``data/`` by hand — which bypasses the validator entirely, and
        is how a wrong alias once fused two distinct entities in a live archive.

        Once ``render`` has applied the result the task is archived, and
        re-answering it would not undo what was folded into the records. That
        case is refused, and the error says what to do instead.
        """
        done = self.done_path(task_id)
        if not done.exists():
            if self.archive_path(task_id).exists():
                raise ValueError(
                    f"'{task_id}' has already been applied by render; edit the "
                    "record in data/ or re-collect the item instead"
                )
            raise FileNotFoundError(f"no completed task with id '{task_id}'")

        task = read_json(done) or {}
        # Only the answer is dropped. The instructions, schema and source
        # material are what made the task answerable, and they are unchanged.
        task.pop("result", None)
        task.pop("completed_at", None)
        pending = self.pending_path(task_id)
        write_json(pending, task)
        done.unlink(missing_ok=True)
        _LOG.info("reopened %s", task_id)
        return pending

    def archive(self, task_id: str) -> None:
        """Move a consumed task out of ``done`` so it is not applied twice."""
        done = self.done_path(task_id)
        if done.exists():
            target = self.archive_path(task_id)
            target.parent.mkdir(parents=True, exist_ok=True)
            done.replace(target)

    def stats(self) -> dict[str, int]:
        def by_kind(directory: Path, kind: str) -> int:
            return sum(1 for _ in directory.glob(f"{kind}__*.json"))

        stats = {"pending": self.count_pending()}
        for kind in _KINDS:
            stats[f"pending_{kind}s"] = by_kind(self.layout.queue_pending, kind)
        stats["done"] = sum(1 for _ in self.layout.queue_done.glob("*.json"))
        stats["archived"] = sum(1 for _ in self.layout.queue_archive.glob("*.json"))
        return stats


# ---------------------------------------------------------------------------
# Command line
# ---------------------------------------------------------------------------


def _build_queue(root: Path | None = None) -> Queue:
    cfg = config_mod.load(root)
    cfg.layout.ensure()
    return Queue(cfg.layout)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.enrich.queue",
        description="Inspect and complete summarization tasks.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("stats", help="counts of pending, done and archived tasks")

    p_list = sub.add_parser("list", help="list pending task ids")
    p_list.add_argument("--kind", choices=list(_KINDS))
    p_list.add_argument("--limit", type=int, default=0, help="0 means no limit")
    p_list.add_argument("--json", action="store_true", help="emit full task objects")

    p_next = sub.add_parser("next", help="print the oldest pending task")
    p_next.add_argument("--kind", choices=list(_KINDS))

    p_show = sub.add_parser("show", help="print one task by id")
    p_show.add_argument("task_id")

    p_done = sub.add_parser("complete", help="submit a result for a task")
    p_done.add_argument("task_id")
    source = p_done.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", type=Path, help="path to a JSON result")
    source.add_argument("--stdin", action="store_true", help="read JSON from stdin")

    p_reopen = sub.add_parser(
        "reopen",
        help="return a completed task to pending so its result can be corrected",
    )
    p_reopen.add_argument("task_id")

    args = parser.parse_args(argv)
    queue = _build_queue(args.root)

    if args.command == "stats":
        print(json.dumps(queue.stats(), indent=2))
        return 0

    if args.command == "list":
        ids = queue.pending_ids(args.kind)
        if args.limit:
            ids = ids[: args.limit]
        if args.json:
            print(json.dumps([queue.load(i) for i in ids], indent=2, ensure_ascii=False))
        else:
            for task_id in ids:
                task = queue.load(task_id) or {}
                title = (task.get("payload") or {}).get("title", "")
                print(f"{task_id}\t{title}")
        return 0

    if args.command == "next":
        ids = queue.pending_ids(args.kind)
        if not ids:
            print("{}")
            return 0
        print(json.dumps(queue.load(ids[0]), indent=2, ensure_ascii=False))
        return 0

    if args.command == "show":
        task = queue.load(args.task_id)
        if task is None:
            print(f"no such task: {args.task_id}", file=sys.stderr)
            return 1
        print(json.dumps(task, indent=2, ensure_ascii=False))
        return 0

    if args.command == "complete":
        raw = sys.stdin.read() if args.stdin else args.file.read_text(encoding="utf-8")
        try:
            result = json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"result is not valid JSON: {exc}", file=sys.stderr)
            return 1
        try:
            path = queue.complete(args.task_id, result)
        except (FileNotFoundError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(path)
        return 0

    if args.command == "reopen":
        try:
            path = queue.reopen(args.task_id)
        except (FileNotFoundError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(path)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
