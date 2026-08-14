"""Things checked outside the archive, recorded so they can be checked again.

    python -m pipelines.enrich.references add --file reference.json
    python -m pipelines.enrich.references list [--kind code]
    python -m pipelines.enrich.references show <id>

The archive answers questions about itself. It cannot answer what a published
implementation actually does, what a model card claims, or how a venue spells
the name of a paper it accepted — and sessions go and find those things out.
Until now what they learned survived only inside a finding's prose, where the
next person could neither verify it nor find it again without repeating the
search from nothing.

**A reference is not a paper and must never become one.** `Concept.evidence`
counts papers and talks the archive has read, and that count is what promotes an
entity to a note of its own. If a blog post could contribute to it, nobody could
afterwards say what the wiki had grown from, and no deletion would undo that.
So these live in `data/references/`, nothing under `enrich/concepts.py` reads
them, and `tests/test_references.py` asserts both.

**Two fields make it a citation rather than a rumour.** `retrieved_at`, because
the web changes and an undated claim about a page cannot be checked against
anything. `quoted`, because a URL says a page was visited and not what it was
found to say — and when the page moves, the quotation is the only evidence left.
Both are required, which is friction on purpose: the alternative is a record
that looks like a citation and is not one.
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
from ..common.schema import Reference, normalize_url, reference_id, utcnow
from ..common.store import RecordStore

_LOG = get(__name__)

#: What sort of thing was consulted. A closed set, so that "what has this
#: archive been checking itself against" is a question the records can answer.
KINDS = (
    "code",
    "model-card",
    "docs",
    "blog",
    "proceedings-page",
    "dataset",
    "other",
)

_ISO_DATE_LENGTH = 10


def validate(result: Any) -> list[str]:
    """Check a proposed reference. Returns error strings; empty means valid."""
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["reference must be a JSON object"]

    url = str(result.get("url", "")).strip()
    if not url:
        errors.append("missing or empty required field: url")
    elif not normalize_url(url).startswith(("http://", "https://")):
        errors.append(f"`url` must be an http(s) address (got '{url}')")

    kind = str(result.get("kind", "")).strip()
    if kind and kind not in KINDS:
        errors.append(f"`kind` must be one of: {', '.join(KINDS)}")

    retrieved = str(result.get("retrieved_at", "")).strip()
    if not retrieved:
        errors.append(
            "missing or empty required field: retrieved_at — the web changes, and "
            "an undated claim about a page cannot be checked against anything. "
            "Use today's date if you have just read it"
        )
    elif len(retrieved) < _ISO_DATE_LENGTH:
        errors.append(f"`retrieved_at` must be an ISO date or timestamp (got '{retrieved}')")

    quoted = str(result.get("quoted", "")).strip()
    if not quoted:
        errors.append(
            "missing or empty required field: quoted — record the passage you "
            "actually relied on, not the whole page. When the page moves it is "
            "the only evidence that survives"
        )

    return errors


def record(cfg: Config, result: dict, store: RecordStore | None = None) -> Reference:
    """Validate and store a reference, folding a repeat of the same page onto it."""
    store = store or RecordStore(cfg.layout)
    errors = validate(result)
    if errors:
        raise ValueError("reference is invalid:\n  - " + "\n  - ".join(errors))

    url = normalize_url(str(result["url"]).strip())
    reference = Reference(
        id=reference_id(url),
        url=url,
        title=str(result.get("title", "")).strip(),
        publisher=str(result.get("publisher", "")).strip() or _publisher_of(url),
        kind=str(result.get("kind", "")).strip() or "other",
        retrieved_at=str(result["retrieved_at"]).strip(),
        quoted=str(result["quoted"]).strip(),
        snapshot=str(result.get("snapshot", "")).strip(),
    )

    existing = store.load_reference(reference.id)
    if existing is not None:
        # Content-addressed: the same page cited twice is one record. A second
        # visit legitimately updates what was quoted and when — a page changes,
        # and that is the whole reason `retrieved_at` exists — but the date it
        # was first seen is a fact about this archive and is kept.
        reference.first_seen = existing.first_seen
    store.save_reference(reference)
    _LOG.info("reference %s (%s)", reference.id, reference.url)
    return reference


def _publisher_of(url: str) -> str:
    """The host, as a last resort. Better than empty and worse than a name."""
    from urllib.parse import urlsplit

    return (urlsplit(url).hostname or "").removeprefix("www.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.enrich.references",
        description="Record something checked outside the archive.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="record a reference")
    source = p_add.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", type=Path, help="path to a JSON reference")
    source.add_argument("--stdin", action="store_true", help="read JSON from stdin")

    p_list = sub.add_parser("list", help="list references, newest first")
    p_list.add_argument("--kind", choices=KINDS)
    p_list.add_argument("--json", action="store_true")

    p_show = sub.add_parser("show", help="print one reference")
    p_show.add_argument("reference_id")

    sub.add_parser("stats", help="counts by kind")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    cfg.layout.ensure()
    store = RecordStore(cfg.layout)

    if args.command == "add":
        raw = sys.stdin.read() if args.stdin else args.file.read_text(encoding="utf-8")
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"reference is not valid JSON: {exc}", file=sys.stderr)
            return 1
        try:
            reference = record(cfg, payload, store)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(reference.id)
        return 0

    if args.command == "list":
        rows = sorted(
            store.iter_references(), key=lambda r: r.retrieved_at, reverse=True
        )
        if args.kind:
            rows = [r for r in rows if r.kind == args.kind]
        if args.json:
            print(json.dumps([r.to_dict() for r in rows], indent=2, ensure_ascii=False))
        else:
            for reference in rows:
                title = reference.title or reference.url
                print(f"{reference.id}\t{reference.kind}\t{title}")
        return 0

    if args.command == "show":
        reference = store.load_reference(args.reference_id)
        if reference is None:
            print(f"no such reference: {args.reference_id}", file=sys.stderr)
            return 1
        print(json.dumps(reference.to_dict(), indent=2, ensure_ascii=False))
        return 0

    if args.command == "stats":
        counts: dict[str, int] = {}
        for reference in store.iter_references():
            counts[reference.kind] = counts.get(reference.kind, 0) + 1
        print(json.dumps({"total": sum(counts.values()), "by_kind": counts}, indent=2))
        return 0

    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
