"""What the group settled, recorded as it is settled.

    python -m pipelines.enrich.findings add --file finding.json
    python -m pipelines.enrich.findings list [--kind decision] [--all]
    python -m pipelines.enrich.findings show <id>
    python -m pipelines.enrich.findings retire <old-id> --by <new-id>

Every other record in this repository came from a collector. This one comes
from a conversation: a decision the group took, or a judgement it reached
across several sources. Those are real knowledge and there was nowhere to put
them — a paper record cannot hold "we decided to stop tracking this", and the
wiki definition of a concept is written from its sources, not from the group's
own position on it.

**It goes through a validator for exactly the reason the queue does.** The
alternative is editing ``data/`` by hand, and a finding filed that way can
claim a topic that does not exist or a paper that was never collected, and
nothing would notice. Being able to say "the group established X" is only worth
anything if the record cannot quietly be wrong about what X attaches to.

**Nothing here is automatic, and it cannot be.** The pipeline never sees a
conversation — it never calls a model and has no transcript. Whoever is in the
conversation records the finding, deliberately, in the same way they answer a
reading task. That is a limitation of the architecture and also the right
behaviour: a fact worth keeping is worth someone choosing to keep.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from ..common import config as config_mod
from ..common.config import Config
from ..common import paths as P
from ..common.log import get
from ..common.schema import Finding, finding_id, utcnow
from ..common.store import RecordStore

_LOG = get(__name__)

KINDS = ("decision", "fact")
_LIST_FIELDS = ("concepts", "papers", "references", "topics")


def validate(cfg: Config, result: Any, store: RecordStore) -> list[str]:
    """Check a proposed finding. Returns error strings; empty means valid."""
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["finding must be a JSON object"]

    statement = str(result.get("statement", "")).strip()
    if not statement:
        errors.append("missing or empty required field: statement")
    elif len(statement) < 12:
        # A three-word statement is a label, and a label cannot be argued with
        # later. The point of the record is that somebody can disagree with it.
        errors.append("`statement` is too short to be a finding")

    kind = str(result.get("kind", "")).strip()
    if kind not in KINDS:
        errors.append(f"`kind` must be one of: {', '.join(KINDS)}")

    for name in _LIST_FIELDS:
        if name in result and not isinstance(result[name], list):
            errors.append(f"field `{name}` must be a list")

    # Topics are a closed set defined in config, so a wrong slug is a typo and
    # is rejected. Concepts are not: the wiki harvests them from summaries, and
    # a finding may legitimately name one before any paper has mentioned it.
    known = {topic.slug for topic in cfg.topics}
    for slug in result.get("topics") or []:
        if str(slug).strip() not in known:
            errors.append(
                f"`topics` names '{slug}', which is not a tracked topic: "
                f"{', '.join(sorted(known)) or '(none defined)'}"
            )

    for paper_id in result.get("papers") or []:
        if store.load_paper(str(paper_id)) is None:
            errors.append(
                f"`papers` names '{paper_id}', which is not in the archive — "
                "collect it first rather than referring to a record that is not there"
            )

    # The same check as `papers`, against a different store and for the same
    # reason: a citation naming a record nobody kept is one nobody can follow.
    # Record the page first, with `pipelines.enrich.references add`, so that
    # what the finding points at carries a date and a quotation.
    for ref_id in result.get("references") or []:
        if store.load_reference(str(ref_id)) is None:
            errors.append(
                f"`references` names '{ref_id}', which is not a recorded reference "
                "— add it with `pipelines.enrich.references add` first"
            )

    supersedes = str(result.get("supersedes", "")).strip()
    if supersedes and store.load_finding(supersedes) is None:
        errors.append(f"`supersedes` names an unknown finding: {supersedes}")

    return errors


def evidence_now(store: RecordStore, concepts: list[str]) -> int:
    """Distinct sources behind the entities a finding names.

    The union rather than the sum: two entities that share a paper have been
    established by one reading, not two, and counting it twice would make a
    finding look better supported the more entities it happens to mention.

    Zero when it names no entity the wiki has harvested — there is nothing to
    measure against, which is different from having measured nothing.
    """
    from .concepts import slug_for

    sources: set[tuple[str, str]] = set()
    for name in concepts:
        concept = store.load_concept(slug_for(name))
        if concept is None:
            continue
        for item in concept.evidence:
            sources.add((str(item.get("kind", "")), str(item.get("id", ""))))
    return len(sources)


def record(cfg: Config, result: dict, store: RecordStore | None = None) -> Finding:
    """Validate and store a finding, retiring whatever it supersedes."""
    store = store or RecordStore(cfg.layout)
    errors = validate(cfg, result, store)
    if errors:
        raise ValueError("finding is invalid:\n  - " + "\n  - ".join(errors))

    statement = str(result["statement"]).strip()
    finding = Finding(
        id=finding_id(statement),
        kind=str(result["kind"]).strip(),
        statement=statement,
        rationale=str(result.get("rationale", "")).strip(),
        concepts=[str(c).strip() for c in (result.get("concepts") or []) if str(c).strip()],
        papers=[str(p).strip() for p in (result.get("papers") or []) if str(p).strip()],
        references=[
            str(r).strip() for r in (result.get("references") or []) if str(r).strip()
        ],
        topics=[str(t).strip() for t in (result.get("topics") or []) if str(t).strip()],
        supersedes=str(result.get("supersedes", "")).strip(),
        established_at=utcnow(),
    )
    finding.established_against = evidence_now(store, finding.concepts)

    existing = store.load_finding(finding.id)
    if existing is not None:
        # Content-addressed: the same sentence twice is one finding, and the
        # second attempt updates its links rather than making a duplicate that
        # would double-count in every view.
        finding.established_at = existing.established_at
        finding.superseded_by = existing.superseded_by
        # Recording the same statement again *is* a revision — somebody looked
        # at it against what the archive now holds — so the count moves with it.
        # Keeping the original would report the revision as stale on arrival.

    store.save_finding(finding)
    if finding.supersedes:
        retire(cfg, finding.supersedes, finding.id, store)
    _LOG.info("recorded %s (%s)", finding.id, finding.kind)
    return finding


def retire(
    cfg: Config, old_id: str, new_id: str, store: RecordStore | None = None
) -> Finding:
    """Mark a finding as replaced, without deleting it.

    The old statement stays on disk. Why the group used to think otherwise is
    part of what a newcomer needs, and a log that quietly drops its own history
    cannot be audited.
    """
    store = store or RecordStore(cfg.layout)
    old = store.load_finding(old_id)
    if old is None:
        raise FileNotFoundError(f"no finding with id '{old_id}'")
    if store.load_finding(new_id) is None:
        raise FileNotFoundError(f"no finding with id '{new_id}'")
    if old_id == new_id:
        raise ValueError("a finding cannot supersede itself")

    old.superseded_by = new_id
    store.save_finding(old)
    return old


def live(store: RecordStore) -> list[Finding]:
    """Findings that have not been retired, newest first."""
    return sorted(
        (f for f in store.iter_findings() if f.live),
        key=lambda f: f.established_at,
        reverse=True,
    )


def summarize(store: RecordStore) -> dict[str, int]:
    rows = list(store.iter_findings())
    return {
        "findings": len(rows),
        "live": sum(1 for f in rows if f.live),
        "decisions": sum(1 for f in rows if f.live and f.kind == "decision"),
        "facts": sum(1 for f in rows if f.live and f.kind == "fact"),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.enrich.findings",
        description="Record what the group has settled.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="record a finding")
    source = p_add.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", type=Path, help="path to a JSON finding")
    source.add_argument("--stdin", action="store_true", help="read JSON from stdin")

    p_list = sub.add_parser("list", help="list findings, newest first")
    p_list.add_argument("--kind", choices=KINDS)
    p_list.add_argument("--all", action="store_true", help="include retired ones")
    p_list.add_argument("--json", action="store_true")

    p_show = sub.add_parser("show", help="print one finding")
    p_show.add_argument("finding_id")

    p_retire = sub.add_parser("retire", help="mark a finding as replaced")
    p_retire.add_argument("finding_id")
    p_retire.add_argument("--by", required=True, help="id of the finding that replaces it")

    sub.add_parser("stats", help="counts")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    cfg.layout.ensure()
    store = RecordStore(cfg.layout)

    if args.command == "add":
        raw = sys.stdin.read() if args.stdin else args.file.read_text(encoding="utf-8")
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"finding is not valid JSON: {exc}", file=sys.stderr)
            return 1
        try:
            finding = record(cfg, payload, store)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(finding.id)
        return 0

    if args.command == "list":
        rows = list(store.iter_findings()) if args.all else live(store)
        rows = sorted(rows, key=lambda f: f.established_at, reverse=True)
        if args.kind:
            rows = [f for f in rows if f.kind == args.kind]
        if args.json:
            print(json.dumps([f.to_dict() for f in rows], indent=2, ensure_ascii=False))
        else:
            for f in rows:
                mark = " (retired)" if not f.live else ""
                print(f"{f.id}\t{f.kind}\t{f.statement}{mark}")
        return 0

    if args.command == "show":
        finding = store.load_finding(args.finding_id)
        if finding is None:
            print(f"no such finding: {args.finding_id}", file=sys.stderr)
            return 1
        print(json.dumps(finding.to_dict(), indent=2, ensure_ascii=False))
        return 0

    if args.command == "retire":
        try:
            retire(cfg, args.finding_id, args.by, store)
        except (FileNotFoundError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
        print(f"{args.finding_id} retired by {args.by}")
        return 0

    if args.command == "stats":
        print(json.dumps(summarize(store), indent=2))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
