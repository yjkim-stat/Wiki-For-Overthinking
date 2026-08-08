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
    "paper": ["contributions", "concepts", "methods", "datasets", "tags"],
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


def validate_result(kind: str, result: Any) -> list[str]:
    """Check a submitted result against the contract. Returns error strings."""
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
            if not isinstance(chapter.get("start_s", 0), (int, float)):
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
        """File a task. Returns its id, or ``""`` if it was not filed."""
        task_id = self.task_id(kind, item_id)
        pending = self.pending_path(task_id)

        if pending.exists() or self.done_path(task_id).exists():
            return ""

        if self.max_pending is not None and self.count_pending() >= self.max_pending:
            _LOG.warning(
                "queue is at its cap of %d pending tasks; skipping %s",
                self.max_pending,
                task_id,
            )
            return ""

        write_json(
            pending,
            {
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
            },
        )
        _LOG.info("queued %s", task_id)
        return task_id

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

        errors = validate_result(task["kind"], result)
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
        "--root", type=Path, default=None, help="repository root (for testing)"
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

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
