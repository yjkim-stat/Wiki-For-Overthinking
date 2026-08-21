"""Repositories waiting for somebody to decide whether they are worth citing.

    python -m pipelines.candidates fetch              # search GitHub, file what is new
    python -m pipelines.candidates list
    python -m pipelines.candidates show <id>
    python -m pipelines.candidates promote <id> --quoted "the passage relied on"
    python -m pipelines.candidates drop <id> --reason "why not"

A third lane, alongside `inbox/` and `requests/`, and for the same reason both
of those exist: something arrives that is not yet a record, and a person decides
what it becomes.

**Why the decision cannot be automated away.** A repository's destination is a
`Reference`, whose two required fields are `retrieved_at` and `quoted` — the
date somebody looked, and the passage they relied on. Those fields are what make
the record a citation instead of a rumour, and neither can be filled by a
collector: a scraped description is not a passage anybody relied on. `promote`
therefore requires `--quoted` and refuses without it. That is the whole design.

**A repository is never evidence.** It cannot become a paper, and nothing here
touches `Concept.evidence`. Promotion writes a `Reference` through the same
store as `references add`, so the rule that references never promote a wiki
entity holds without this module having to restate it.

**A decision is permanent, a repository is not.** Dropping writes the candidate
to `candidates/dropped/` with the reason, and a dropped id is never offered
again — so a daily run does not re-file what somebody already declined, however
many times GitHub returns it. That is why `file_new` is here rather than in the
collector: what is new is a fact about the decisions, not about the search.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .collect import github
from .common import config as config_mod
from .common.config import Config
from .common.log import get
from .common.schema import Reference, utcnow
from .common.store import RecordStore

_LOG = get(__name__)


def _write(path: Path, data: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def _seen_ids(cfg: Config) -> set[str]:
    """Every candidate already decided about, or already waiting.

    All three directories, not just `pending/`: re-filing something dropped
    would make the drop meaningless, and re-filing something promoted would
    offer a repository the archive already cites.
    """
    layout = cfg.layout
    seen: set[str] = set()
    for directory in (layout.candidates_pending, layout.candidates_promoted, layout.candidates_dropped):
        if directory.exists():
            seen.update(p.stem for p in directory.glob("*.json"))
    return seen


def file_new(cfg: Config, found: list[github.Candidate]) -> list[github.Candidate]:
    """Write the candidates nobody has ruled on yet. Returns what was filed."""
    seen = _seen_ids(cfg)
    filed = []
    for candidate in found:
        if candidate.id in seen:
            continue
        _write(cfg.layout.candidates_pending / f"{candidate.id}.json", candidate.to_dict())
        filed.append(candidate)
    if filed:
        _LOG.info("candidates: filed %d new, %d already ruled on", len(filed), len(found) - len(filed))
    return filed


def _load(cfg: Config, candidate_id: str) -> tuple[github.Candidate, Path] | tuple[None, None]:
    path = cfg.layout.candidates_pending / f"{candidate_id}.json"
    if not path.exists():
        return None, None
    return github.Candidate.from_dict(json.loads(path.read_text(encoding="utf-8"))), path


def promote(cfg: Config, candidate_id: str, *, quoted: str, kind: str = "code") -> Reference | None:
    """Turn a candidate into a reference. The quotation is not optional."""
    candidate, path = _load(cfg, candidate_id)
    if candidate is None:
        return None
    store = RecordStore(cfg.layout)
    reference = Reference(
        id=candidate.id,
        url=candidate.url,
        title=candidate.full_name,
        publisher="github.com",
        kind=kind,
        retrieved_at=utcnow()[:10],
        quoted=quoted,
    )
    store.save_reference(reference)
    data = candidate.to_dict()
    data["decided_at"] = utcnow()
    data["decision"] = "promoted"
    _write(cfg.layout.candidates_promoted / f"{candidate.id}.json", data)
    path.unlink()
    _LOG.info("promoted %s -> %s", candidate.full_name, reference.id)
    return reference


def drop(cfg: Config, candidate_id: str, *, reason: str) -> bool:
    """Decline a candidate, permanently. The reason is the record."""
    candidate, path = _load(cfg, candidate_id)
    if candidate is None:
        return False
    data = candidate.to_dict()
    data["decided_at"] = utcnow()
    data["decision"] = "dropped"
    data["reason"] = reason
    _write(cfg.layout.candidates_dropped / f"{candidate.id}.json", data)
    path.unlink()
    return True


def pending(cfg: Config) -> list[github.Candidate]:
    directory = cfg.layout.candidates_pending
    if not directory.exists():
        return []
    rows = [
        github.Candidate.from_dict(json.loads(p.read_text(encoding="utf-8")))
        for p in sorted(directory.glob("*.json"))
    ]
    return sorted(rows, key=lambda c: -max(c.scores.values(), default=0.0))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="deployment root the archive lives in")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("fetch", help="search GitHub and file what is new")
    sub.add_parser("list", help="candidates waiting for a decision")
    p_show = sub.add_parser("show", help="one candidate in full")
    p_show.add_argument("candidate_id")
    p_promote = sub.add_parser("promote", help="record it as a reference")
    p_promote.add_argument("candidate_id")
    p_promote.add_argument(
        "--quoted",
        required=True,
        help="the passage you actually relied on -- not the whole README",
    )
    p_promote.add_argument("--kind", default="code")
    p_drop = sub.add_parser("drop", help="decline it, with the reason")
    p_drop.add_argument("candidate_id")
    p_drop.add_argument("--reason", required=True)

    args = parser.parse_args(argv)
    cfg = config_mod.load(root=args.root) if args.root else config_mod.load()

    if args.command == "fetch":
        if not github.enabled(cfg):
            print("github is disabled in config/sources.yaml", file=sys.stderr)
            return 1
        filed = file_new(cfg, github.collect(cfg))
        print(f"{len(filed)} new candidate(s)")
        for candidate in filed:
            print(f"  {candidate.id}  {candidate.full_name}")
        return 0

    if args.command == "list":
        rows = pending(cfg)
        if not rows:
            print("nothing pending")
            return 0
        for candidate in rows:
            best = max(candidate.scores.values(), default=0.0)
            print(
                f"{candidate.id}  {best:5.2f}  {candidate.stars:>6}*  "
                f"{candidate.full_name}\n    {candidate.description[:100]}"
            )
        return 0

    if args.command == "show":
        candidate, _ = _load(cfg, args.candidate_id)
        if candidate is None:
            print(f"no such pending candidate: {args.candidate_id}", file=sys.stderr)
            return 1
        print(json.dumps(candidate.to_dict(), ensure_ascii=False, indent=2))
        return 0

    if args.command == "promote":
        reference = promote(cfg, args.candidate_id, quoted=args.quoted, kind=args.kind)
        if reference is None:
            print(f"no such pending candidate: {args.candidate_id}", file=sys.stderr)
            return 1
        print(reference.id)
        return 0

    if args.command == "drop":
        if not drop(cfg, args.candidate_id, reason=args.reason):
            print(f"no such pending candidate: {args.candidate_id}", file=sys.stderr)
            return 1
        print(f"dropped {args.candidate_id}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
