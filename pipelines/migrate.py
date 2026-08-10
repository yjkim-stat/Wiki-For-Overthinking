"""Carry an archive between environments.

    python -m pipelines.migrate status
    python -m pipelines.migrate pack [--dest migration] [--tier all] [--move]
    python -m pipelines.migrate verify [--src migration]
    python -m pipelines.migrate unpack [--src migration] [--dry-run]

An archive travels along two channels, and the whole of this module exists
because they are not the same channel and only one of them is automatic.

**git carries the knowledge.** Every record the group has -- papers, seminars,
readings, concepts, findings, the queue, the dedup state, the coverage ledger --
is committed on purpose, along with the wiki and the analysis written under
`<!-- auto:end -->`. Clone the repository somewhere else and the archive is
already there. Nothing in this module is needed for that, and nothing in this
module can rescue it: work that was never pushed does not exist anywhere else.

**This bundle carries what git refuses to.** PDFs, announced-paper abstracts,
raw collector responses and run logs are gitignored -- heavy, re-fetchable in
principle, and in the case of documents not ours to redistribute. They are also
the part of the archive that a fresh container starts without.

The distinction that matters inside the bundle is not size, it is *what it
costs to lose the file*:

- ``irreplaceable`` -- a hand-filed PDF. Somebody chose it and put it in the
  inbox; no URL is recorded and nothing can fetch it again. Losing one loses
  the document permanently while the record that describes it stays behind,
  which is worse than an obvious gap.
- ``refetchable`` -- a fetched PDF, which has a ``pdf_url``, and the announced
  abstracts, which the coverage ledger re-pays automatically at one request per
  paper. Losing these costs network time, not evidence. Note that nothing
  re-fetches a PDF on its own once the record exists: it is a human's job.
- ``disposable`` -- raw collector responses and run logs. Useful for replaying
  a parsing bug, worthless afterwards.

``--tier`` packs cumulatively, so a constrained transfer can carry the first
tier alone and know exactly what it gave up.

Every file under every source root is inventoried; there is no sampling and no
cap. Whatever is deliberately skipped is listed in the manifest under
``skipped``, because a bundle that quietly omits something is worse than one
that is honestly partial.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from .common import config as config_mod
from .common.config import Config
from .common.log import get
from .common.paths import Layout
from .common.schema import utcnow
from .common.store import RecordStore

_LOG = get(__name__)

MANIFEST_NAME = "MANIFEST.json"
PAYLOAD_DIR = "payload"

TIERS = ("irreplaceable", "refetchable", "disposable")

# Anything the pipeline writes that git is told to ignore. Keeping this list
# here rather than reading .gitignore is deliberate: the point is what the
# archive needs, and a deployment that edits its ignore rules should not
# silently change what a migration carries.
_UNTRACKED_ROOTS = ("pdfs", "abstracts", "raw", "logs")


@dataclass
class Item:
    """One file, with the path it must be restored to."""

    path: str  # repository-relative, and where unpack puts it back
    size: int
    tier: str
    sha256: str = ""


@dataclass
class Plan:
    items: list[Item] = field(default_factory=list)
    skipped: list[dict] = field(default_factory=list)

    def of_tier(self, tiers: tuple[str, ...]) -> list[Item]:
        return [i for i in self.items if i.tier in tiers]


# -- git ---------------------------------------------------------------------


def _git(root: Path, *args: str) -> str:
    try:
        out = subprocess.run(
            ["git", *args],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def repo_state(root: Path) -> dict:
    """What git would carry, and whether it actually can.

    The most expensive way to lose an archive is not a dropped PDF: it is a
    container discarded while `main` was still behind the working tree. That
    failure is silent on both ends -- the bundle looks complete and the clone
    looks healthy -- so the check belongs here, before anything is copied.
    """
    branch = _git(root, "rev-parse", "--abbrev-ref", "HEAD")
    status = _git(root, "status", "--porcelain")
    upstream = _git(root, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    unpushed = 0
    if upstream:
        listing = _git(root, "rev-list", "--count", f"{upstream}..HEAD")
        unpushed = int(listing) if listing.isdigit() else 0
    return {
        "remote": _git(root, "config", "--get", "remote.origin.url"),
        "branch": branch,
        "head": _git(root, "rev-parse", "HEAD"),
        "upstream": upstream,
        "unpushed": unpushed,
        "dirty": [line for line in status.splitlines() if line.strip()],
    }


def _warn_about_git(state: dict) -> list[str]:
    problems = []
    if state["dirty"]:
        problems.append(
            f"{len(state['dirty'])} uncommitted change(s) in the working tree -- "
            "git carries none of them"
        )
    if not state["upstream"]:
        problems.append(f"branch '{state['branch']}' has no upstream; nothing is pushed")
    elif state["unpushed"]:
        problems.append(
            f"{state['unpushed']} commit(s) on '{state['branch']}' are not on "
            f"'{state['upstream']}' -- the new environment will not see them"
        )
    return problems


# -- planning ----------------------------------------------------------------


def _hand_filed(store: RecordStore) -> tuple[set[str], set[str]]:
    """``(hand_filed_paths, all_recorded_paths)``, repository-relative.

    A document is irreplaceable exactly when no URL exists for it, which is a
    fact about the record rather than about the file. Reading it from `data/`
    is what lets the two tiers be told apart at all.
    """
    hand_filed: set[str] = set()
    recorded: set[str] = set()
    for paper in store.iter_papers():
        if not paper.local_path:
            continue
        recorded.add(paper.local_path)
        if paper.is_local or not paper.pdf_url:
            hand_filed.add(paper.local_path)
    return hand_filed, recorded


def _rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def build_plan(cfg: Config, store: RecordStore) -> Plan:
    """Inventory every file the bundle could carry, with its tier."""
    layout: Layout = cfg.layout
    root = layout.root
    hand_filed, recorded = _hand_filed(store)
    plan = Plan()

    roots: list[tuple[Path, str]] = []
    for name in _UNTRACKED_ROOTS:
        directory = getattr(layout, name)
        roots.append((directory, "pdf" if name == "pdfs" else name))
    roots.append((layout.inbox, "inbox"))

    for directory, kind in roots:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*")):
            if not path.is_file():
                continue
            rel = _rel(path, root)

            if kind == "inbox":
                # The inbox holds a README that is tracked, and PDFs that are
                # not. Only the untracked ones are the migration's business.
                if path.suffix.lower() != ".pdf":
                    plan.skipped.append({"path": rel, "why": "tracked by git"})
                    continue
                tier = "irreplaceable"
            elif kind == "pdf":
                if rel in hand_filed:
                    tier = "irreplaceable"
                elif rel in recorded:
                    tier = "refetchable"
                else:
                    # On disk with no record pointing at it. Its provenance
                    # cannot be established, so it cannot be shown to be
                    # re-fetchable -- and the safe reading of "unknown" is the
                    # one that does not throw the file away.
                    tier = "irreplaceable"
            elif kind == "abstracts":
                tier = "refetchable"
            else:
                tier = "disposable"

            plan.items.append(Item(path=rel, size=path.stat().st_size, tier=tier))

    return plan


def _tiers_up_to(name: str) -> tuple[str, ...]:
    if name == "all":
        return TIERS
    return TIERS[: TIERS.index(name) + 1]


def _human(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024 or unit == "GB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GB"


def _totals(items: list[Item]) -> dict:
    out = {tier: {"files": 0, "bytes": 0} for tier in TIERS}
    for item in items:
        out[item.tier]["files"] += 1
        out[item.tier]["bytes"] += item.size
    return out


def _digest(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            sha.update(chunk)
    return sha.hexdigest()


def _record_counts(cfg: Config, store: RecordStore) -> dict:
    """A receipt for the git half, checked again at the far end.

    The bundle cannot verify that the clone arrived complete -- but these
    numbers can, because they were counted on this side of the move.
    """
    layout = cfg.layout
    return {
        "papers": sum(1 for _ in layout.papers.glob("*.json")) if layout.papers.exists() else 0,
        "videos": sum(1 for _ in layout.videos.glob("*.json")) if layout.videos.exists() else 0,
        "concepts": sum(1 for _ in layout.concepts.glob("*.json")) if layout.concepts.exists() else 0,
        "findings": sum(1 for _ in layout.findings.glob("*.json")) if layout.findings.exists() else 0,
        "queue_pending": sum(1 for _ in layout.queue_pending.glob("*.json")) if layout.queue_pending.exists() else 0,
        "papers_with_document": sum(
            1 for paper in store.iter_papers() if paper.local_path
        ),
        "topics": len(cfg.topics),
    }


# -- pack --------------------------------------------------------------------


def _place(source: Path, target: Path, move: bool) -> None:
    """Put ``source`` at ``target``, cheaply where the filesystem allows it.

    A hard link costs no disk, which matters: these containers have a fixed
    allowance and a copy of a PDF store can be the thing that fills it. The
    files are content-addressed and never rewritten in place, so two names for
    one inode is safe. ``--move`` is the destructive variant and is opt-in
    because a transfer that fails after a move has destroyed the original.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        target.unlink()
    if move:
        shutil.move(str(source), str(target))
        return
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


def pack(
    cfg: Config,
    dest: Path,
    *,
    tier: str = "all",
    move: bool = False,
    checksum: bool = True,
) -> dict:
    """Copy the untracked half of the archive into ``dest`` with a manifest."""
    root = cfg.layout.root
    store = RecordStore(cfg.layout)
    state = repo_state(root)
    problems = _warn_about_git(state)
    for problem in problems:
        _LOG.warning("git: %s", problem)

    plan = build_plan(cfg, store)
    wanted = _tiers_up_to(tier)
    items = plan.of_tier(wanted)
    dropped = [i for i in plan.items if i.tier not in wanted]

    payload = dest / PAYLOAD_DIR
    payload.mkdir(parents=True, exist_ok=True)

    for item in items:
        source = root / item.path
        target = payload / item.path
        _place(source, target, move)
        if checksum:
            item.sha256 = _digest(target)

    skipped = list(plan.skipped) + [
        {"path": i.path, "why": f"tier '{i.tier}' not requested"} for i in dropped
    ]
    manifest = {
        "created_at": utcnow(),
        "tool": "pipelines.migrate",
        "tier": tier,
        "repo": state,
        "git_warnings": problems,
        "records": _record_counts(cfg, store),
        "totals": _totals(items),
        "files": [vars(item) for item in items],
        "skipped": skipped,
    }
    (dest / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    _LOG.info(
        "packed %d file(s), %s, into %s",
        len(items),
        _human(sum(i.size for i in items)),
        dest,
    )
    return manifest


# -- verify and unpack -------------------------------------------------------


def load_manifest(src: Path) -> dict:
    path = src / MANIFEST_NAME
    if not path.exists():
        raise FileNotFoundError(f"no {MANIFEST_NAME} in {src}")
    return json.loads(path.read_text(encoding="utf-8"))


def verify(src: Path, *, checksum: bool = True) -> dict:
    """Check the payload against its own manifest. Touches no checkout."""
    manifest = load_manifest(src)
    payload = src / PAYLOAD_DIR
    missing, corrupt = [], []
    for entry in manifest["files"]:
        path = payload / entry["path"]
        if not path.exists():
            missing.append(entry["path"])
            continue
        if path.stat().st_size != entry["size"]:
            corrupt.append(entry["path"])
            continue
        if checksum and entry.get("sha256") and _digest(path) != entry["sha256"]:
            corrupt.append(entry["path"])

    extra = []
    if payload.exists():
        known = {entry["path"] for entry in manifest["files"]}
        for path in payload.rglob("*"):
            if path.is_file() and _rel(path, payload) not in known:
                extra.append(_rel(path, payload))

    result = {
        "files": len(manifest["files"]),
        "missing": missing,
        "corrupt": corrupt,
        "unlisted": extra,
        "ok": not missing and not corrupt,
    }
    level = _LOG.info if result["ok"] else _LOG.error
    level(
        "verify: %d file(s), %d missing, %d corrupt, %d unlisted",
        result["files"],
        len(missing),
        len(corrupt),
        len(extra),
    )
    return result


def unpack(cfg: Config, src: Path, *, dry_run: bool = False, checksum: bool = True) -> dict:
    """Restore a bundle into this checkout and check it against the records."""
    root = cfg.layout.root
    manifest = load_manifest(src)
    payload = src / PAYLOAD_DIR

    restored, missing, failed = 0, [], []
    for entry in manifest["files"]:
        source = payload / entry["path"]
        if not source.exists():
            missing.append(entry["path"])
            continue
        if checksum and entry.get("sha256") and _digest(source) != entry["sha256"]:
            failed.append(entry["path"])
            continue
        if not dry_run:
            _place(source, root / entry["path"], move=False)
        restored += 1

    result = {
        "restored": restored,
        "missing_from_bundle": missing,
        "checksum_failed": failed,
        "dry_run": dry_run,
    }
    if not dry_run:
        result["documents"] = check_documents(cfg)
        result["records"] = _compare_records(cfg, manifest)
    _LOG.info("unpack: %s", {k: v for k, v in result.items() if not isinstance(v, dict)})
    return result


def check_documents(cfg: Config) -> dict:
    """Does every record that claims a document actually have one?

    This is the question the migration is really asking, and it is answerable
    without the bundle: `data/` says which papers hold a file, and the
    filesystem says which files are there. A record pointing at a document that
    is not on disk is exactly the failure a migration produces.
    """
    store = RecordStore(cfg.layout)
    root = cfg.layout.root
    expected = missing = 0
    absent: list[str] = []
    for paper in store.iter_papers():
        if not paper.local_path:
            continue
        expected += 1
        if not (root / paper.local_path).exists():
            missing += 1
            if len(absent) < 20:
                absent.append(f"{paper.id} -> {paper.local_path}")
    return {"expected": expected, "missing": missing, "examples": absent}


def _compare_records(cfg: Config, manifest: dict) -> dict:
    """The receipt, re-counted here. A difference means git, not the bundle."""
    store = RecordStore(cfg.layout)
    here = _record_counts(cfg, store)
    there = manifest.get("records", {})
    return {
        "source": there,
        "here": here,
        "differences": {
            key: {"source": there.get(key), "here": here.get(key)}
            for key in sorted(set(there) | set(here))
            if there.get(key) != here.get(key)
        },
    }


# -- status ------------------------------------------------------------------


def status(cfg: Config) -> dict:
    store = RecordStore(cfg.layout)
    plan = build_plan(cfg, store)
    state = repo_state(cfg.layout.root)
    return {
        "repo": state,
        "git_warnings": _warn_about_git(state),
        "records": _record_counts(cfg, store),
        "totals": _totals(plan.items),
        "documents": check_documents(cfg),
    }


def _print_status(result: dict) -> None:
    print("git")
    repo = result["repo"]
    print(f"  branch     {repo['branch']} @ {repo['head'][:12] or '(none)'}")
    print(f"  upstream   {repo['upstream'] or '(none)'}")
    for warning in result["git_warnings"]:
        print(f"  WARNING    {warning}")
    if not result["git_warnings"]:
        print("  clean and pushed -- git will carry the knowledge")

    print("\nrecords carried by git")
    for key, value in result["records"].items():
        print(f"  {key:24} {value}")

    print("\nfiles carried by the bundle")
    for tier in TIERS:
        totals = result["totals"][tier]
        print(f"  {tier:16} {totals['files']:6} file(s)  {_human(totals['bytes'])}")

    documents = result["documents"]
    print(
        f"\ndocuments: {documents['expected']} record(s) claim one, "
        f"{documents['missing']} missing on disk"
    )
    for example in documents["examples"]:
        print(f"  missing  {example}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.migrate",
        description="Carry the untracked half of an archive between environments.",
    )
    parser.add_argument("--root", type=Path, default=None, help="repository root")
    parser.add_argument(
        "--no-checksum",
        action="store_true",
        help="skip sha256 (faster, and gives up the completeness guarantee)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="what would be carried, and by which channel")

    packer = sub.add_parser("pack", help="copy the untracked half into a folder")
    packer.add_argument("--dest", type=Path, default=Path("migration"))
    packer.add_argument(
        "--tier",
        choices=["irreplaceable", "refetchable", "disposable", "all"],
        default="all",
        help="pack this tier and everything above it (default: all)",
    )
    packer.add_argument(
        "--move",
        action="store_true",
        help="move rather than link/copy; destroys the originals",
    )

    checker = sub.add_parser("verify", help="check a bundle against its manifest")
    checker.add_argument("--src", type=Path, default=Path("migration"))

    restorer = sub.add_parser("unpack", help="restore a bundle into this checkout")
    restorer.add_argument("--src", type=Path, default=Path("migration"))
    restorer.add_argument("--dry-run", action="store_true")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    checksum = not args.no_checksum

    if args.command == "status":
        _print_status(status(cfg))
        return 0

    if args.command == "pack":
        dest = args.dest if args.dest.is_absolute() else cfg.layout.root / args.dest
        manifest = pack(
            cfg, dest, tier=args.tier, move=args.move, checksum=checksum
        )
        totals = manifest["totals"]
        for tier in TIERS:
            print(
                f"  {tier:16} {totals[tier]['files']:6} file(s)  "
                f"{_human(totals[tier]['bytes'])}"
            )
        for warning in manifest["git_warnings"]:
            print(f"  WARNING  {warning}")
        print(f"\nbundle at {dest}")
        return 1 if manifest["git_warnings"] else 0

    if args.command == "verify":
        src = args.src if args.src.is_absolute() else cfg.layout.root / args.src
        result = verify(src, checksum=checksum)
        for path in result["missing"][:20]:
            print(f"  missing  {path}")
        for path in result["corrupt"][:20]:
            print(f"  corrupt  {path}")
        print("ok" if result["ok"] else "INCOMPLETE")
        return 0 if result["ok"] else 1

    src = args.src if args.src.is_absolute() else cfg.layout.root / args.src
    result = unpack(cfg, src, dry_run=args.dry_run, checksum=checksum)
    print(f"restored {result['restored']} file(s)")
    for path in result["missing_from_bundle"][:20]:
        print(f"  missing from bundle  {path}")
    for path in result["checksum_failed"][:20]:
        print(f"  checksum failed      {path}")
    documents = result.get("documents")
    if documents:
        print(
            f"documents: {documents['expected']} claimed, {documents['missing']} missing"
        )
        for example in documents["examples"]:
            print(f"  missing  {example}")
    differences = (result.get("records") or {}).get("differences") or {}
    for key, value in differences.items():
        print(f"  record count differs: {key} {value['source']} -> {value['here']}")
    ok = not result["missing_from_bundle"] and not result["checksum_failed"]
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
