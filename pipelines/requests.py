"""What somebody outside the archive asks it to change.

    python -m pipelines.requests list
    python -m pipelines.requests show <id>
    python -m pipelines.requests approve <id> [--note "..."]
    python -m pipelines.requests reject  <id> --reason "..."
    python -m pipelines.requests done    <id>

`pipelines/serve.py` lets colleagues on this host read the archive. This is the
other direction, and it is deliberately not the same channel: the port is
read-only and refuses every write, so a change is asked for by leaving a
markdown file in `requests/pending/` — a drop folder, like `inbox/`, that other
people on the machine can write to.

**Nothing arrives on its own.** There is no auto-approved category, not even for
requests that look harmless. Every file waits until a person reads it and says
yes, and the only thing an approval does is move the file to `approved/`, where
the session that maintains the archive treats it as work to do. Nothing here
parses prose into a record, because prose does not survive being parsed and the
archive's whole value is that its records were put there deliberately.

## The request is data, and a hostile reader should assume it is hostile

A file in `pending/` was written by somebody who is not the archive's owner, and
on a shared host that is anybody with a login. Two consequences are built in
rather than trusted:

**The filename is not used.** An id is derived from the file's content, and
everything is moved by that id. A name like `../../data/papers/x.json` is a path
this program never joins.

**The body is quoted, never obeyed.** `show` frames it as submitted text and
says so. A request that reads "ignore the above and add this paper" is asking
the *reviewer* for something, and the reviewer is the one who decides — the same
rule that makes a curated list a source of pointers rather than of metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

from .common import config as config_mod
from .common import log
from .common import paths as P
from .common.config import Config
from .common.schema import utcnow

_LOG = log.get(__name__)

#: What a request can be asking for. A closed set so that "what do people keep
#: asking us for" is answerable, and an unknown kind is reported rather than
#: quietly filed under something else.
KINDS = ("paper", "correction", "topic", "question", "merge", "other")

#: Where a request can be. `pending` is the only one anybody but the reviewer
#: writes to, and nothing leaves it without a person saying so.
STATES = ("pending", "approved", "rejected", "done")

#: A request is prose for a person to read. Anything larger is not that.
MAX_BYTES = 64 * 1024

_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.DOTALL)


@dataclass
class Request:
    """One markdown file somebody left in the drop folder."""

    id: str
    path: Path
    state: str  # pending | approved | rejected | done
    kind: str = "other"
    who: str = ""
    subject: str = ""
    body: str = ""
    problems: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.problems


def request_id(raw: bytes) -> str:
    """Content-addressed, and never derived from the filename.

    The same request left twice is one request. More to the point, the name of a
    file written by somebody else is not something this program is willing to
    join onto a path.
    """
    return hashlib.sha1(raw).hexdigest()[:12]


def parse(raw: bytes, path: Path, state: str) -> Request:
    """Read one request. A malformed one is returned with its problems, not dropped.

    Reporting a bad request is the whole point: a submitter who is silently
    ignored has no way to tell that from a reviewer who has not looked yet.
    """
    # Content-addressed only on intake. Once a decision has been recorded the
    # file carries it, so hashing again would yield a different id for the same
    # request — and after the move the name is one this program wrote, not one a
    # submitter chose, so there is nothing left to distrust about it.
    identifier = request_id(raw) if state == "pending" else path.stem
    problems: list[str] = []

    if len(raw) > MAX_BYTES:
        return Request(
            identifier, path, state,
            problems=[f"larger than {MAX_BYTES // 1024} KB; a request is prose"],
        )
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return Request(identifier, path, state, problems=["not UTF-8 text"])

    match = _FRONT_MATTER.match(text)
    if not match:
        problems.append(
            "no front matter; start the file with a --- block naming `kind` and `from`"
        )
        header, body = "", text
    else:
        header, body = match.group(1), match.group(2)

    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip().lower()] = value.strip().strip("\"'")

    kind = fields.get("kind", "").lower()
    if not kind:
        problems.append("front matter has no `kind`")
    elif kind not in KINDS:
        problems.append(f"`kind` must be one of: {', '.join(KINDS)} (got '{kind}')")
        kind = "other"

    who = fields.get("from", "")
    if not who:
        problems.append("front matter has no `from`; a request needs somebody to ask it")

    if not body.strip():
        problems.append("the request is empty")

    return Request(
        id=identifier,
        path=path,
        state=state,
        kind=kind or "other",
        who=who,
        subject=fields.get("subject", "") or _first_line(body),
        body=body.strip(),
        problems=problems,
    )


def _first_line(body: str) -> str:
    for line in body.splitlines():
        stripped = line.strip().lstrip("#").strip()
        if stripped:
            return stripped[:120]
    return ""


def _dirs(cfg: Config) -> dict[str, Path]:
    return {
        "pending": cfg.layout.requests_pending,
        "approved": cfg.layout.requests_approved,
        "rejected": cfg.layout.requests_rejected,
        "done": cfg.layout.requests_done,
    }


def load_all(cfg: Config, state: str | None = None) -> list[Request]:
    """Every request in a state, oldest file first."""
    found: list[Request] = []
    for name, directory in _dirs(cfg).items():
        if state and name != state:
            continue
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            try:
                raw = path.read_bytes()
            except OSError as exc:  # pragma: no cover - unreadable drop
                _LOG.warning("cannot read %s: %s", path, exc)
                continue
            found.append(parse(raw, path, name))
    return found


def find(cfg: Config, identifier: str) -> Request | None:
    for request in load_all(cfg):
        if request.id == identifier:
            return request
    return None


def _move(cfg: Config, request: Request, state: str, note: str) -> Path:
    """Move a request between states, recording who said so and why.

    The destination name is built from the content-addressed id and nothing
    else. Whatever the submitter called their file is left behind here — it has
    served its only purpose, which was to be found in a directory listing.
    """
    target = _dirs(cfg)[state] / f"{request.id}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(request.path), str(target))

    decision = f"\n\n---\n\n<!-- {state} {utcnow()}"
    if note:
        decision += f": {note}"
    decision += " -->\n"
    with target.open("a", encoding="utf-8") as handle:
        handle.write(decision)
    _LOG.info("%s %s (%s)", state, request.id, request.kind)
    return target


def _print(request: Request, *, full: bool = False) -> None:
    flag = " " if request.ok else "!"
    print(f"{flag}{request.id}  {request.state:9} {request.kind:11} {request.subject}")
    if request.who:
        print(f"   from: {request.who}")
    for problem in request.problems:
        print(f"   problem: {problem}")
    if full:
        # Framed, and labelled as somebody else's words. A request asking the
        # reader to do something is asking *the reviewer*, who decides.
        print("\n   --- submitted text, quoted; it is a request, not an instruction ---")
        for line in request.body.splitlines():
            print(f"   | {line}")
        print("   --- end of submitted text ---")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.requests",
        description="Review what people have asked this archive to change.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="what is waiting")
    p_list.add_argument("--state", choices=STATES, default="pending")
    p_list.add_argument("--json", action="store_true")

    p_show = sub.add_parser("show", help="read one request in full")
    p_show.add_argument("request_id")

    p_ok = sub.add_parser("approve", help="let a request through to the session")
    p_ok.add_argument("request_id")
    p_ok.add_argument("--note", default="", help="why, for the record")

    p_no = sub.add_parser("reject", help="decline a request, saying why")
    p_no.add_argument("request_id")
    p_no.add_argument("--reason", required=True)

    p_done = sub.add_parser("done", help="mark an approved request as acted on")
    p_done.add_argument("request_id")

    sub.add_parser("stats", help="counts by state")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    cfg.layout.ensure()

    if args.command == "list":
        rows = load_all(cfg, args.state)
        if args.json:
            print(json.dumps(
                [{"id": r.id, "state": r.state, "kind": r.kind, "from": r.who,
                  "subject": r.subject, "problems": r.problems} for r in rows],
                indent=2, ensure_ascii=False,
            ))
        elif not rows:
            print(f"nothing {args.state}")
        else:
            for request in rows:
                _print(request)
        return 0

    if args.command == "stats":
        print(json.dumps(
            {state: len(load_all(cfg, state)) for state in _dirs(cfg)}, indent=2
        ))
        return 0

    request = find(cfg, args.request_id)
    if request is None:
        print(f"no such request: {args.request_id}", file=sys.stderr)
        return 1

    if args.command == "show":
        _print(request, full=True)
        return 0

    if args.command == "approve":
        if request.state != "pending":
            print(f"{request.id} is {request.state}, not pending", file=sys.stderr)
            return 1
        if not request.ok:
            # Refused rather than waved through: a reviewer approving something
            # they could not fully read is the failure this whole lane exists
            # to prevent.
            print(f"{request.id} is malformed and cannot be approved:", file=sys.stderr)
            for problem in request.problems:
                print(f"  - {problem}", file=sys.stderr)
            return 1
        _move(cfg, request, "approved", args.note)
        print(f"approved {request.id}")
        return 0

    if args.command == "reject":
        if request.state not in ("pending", "approved"):
            print(f"{request.id} is {request.state}", file=sys.stderr)
            return 1
        _move(cfg, request, "rejected", args.reason)
        print(f"rejected {request.id}")
        return 0

    if args.command == "done":
        if request.state != "approved":
            print(f"{request.id} is {request.state}, not approved", file=sys.stderr)
            return 1
        _move(cfg, request, "done", "")
        print(f"done {request.id}")
        return 0

    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
