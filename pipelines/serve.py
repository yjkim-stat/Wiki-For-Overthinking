"""A read-only window onto the archive, for other people on this machine.

    python -m pipelines.serve [--port 8765] [--limit 20]

The archive is worth more than the person who runs it. Colleagues on the same
host can ask it what it knows without a clone, a checkout, or any way to change
what they are reading.

**It never touches `data/`.** Every answer is assembled from records the
pipeline has already produced, and no request of any shape can change one.
`tests/test_serve.py` asserts the whole of `data/` is byte-identical across a
run of every endpoint, including ones shaped like an attack.

**It writes in exactly one place, and a person reads it.** A question the
archive could not answer is left in `requests/pending/` as a markdown file, the
same drop folder a colleague would use by hand, and it enters the archive only
if somebody approves it. What the archive does not know is the most useful thing
this port produces — it is the only signal anywhere of what people came looking
for and did not find — and it would be lost the moment the caller closed the
connection.

That write is bounded and content-addressed: the same question asked a thousand
times is one file, and the folder stops accepting new ones past a cap. An
unauthenticated local port is reachable by every process on the box, and a write
path without a ceiling is a way to fill a disk.

**It never composes an answer.** What comes back is what the archive wrote: a
definition somebody authored, a finding the group settled, a reading of a paper.
The pipeline calls no model, so a server that produced prose would be either
inventing it or reaching outside the process, and both are excluded by the
contract the rest of this repository is built on.

## The three properties that make it safe to run

**Loopback only.** The socket binds to `127.0.0.1` and there is no flag to
change it. "Other users on this machine" is the whole audience; a host that
wanted to publish its archive would put a reverse proxy in front and make that
decision explicitly, where it can be seen.

**No path is taken from the request.** Nothing here opens a file named by a
caller. Answers come from records looked up by id through `RecordStore`, and an
unknown id is a 404 rather than a traversal.

**Bounded work per request.** The query is truncated, the result count is
capped, and the body of a POST is refused past a small limit. An unauthenticated
local port is reachable by every process on the box, including ones nobody
meant to run.

There is **no authentication**, which is a decision and not an oversight: on a
shared host, loopback means "any local user", and the read-only guarantee is
what makes that acceptable. If it stops being acceptable, the answer is a proxy
that authenticates, not a password checked here.
"""

from __future__ import annotations

import argparse
import json
import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .common import config as config_mod
from .common import log
from .common import paths as P
from .common.config import Config
from .common.schema import title_fingerprint
from .common.search import search
from .common.store import RecordStore

_LOG = log.get(__name__)

#: Never configurable. See the module docstring.
HOST = "127.0.0.1"
DEFAULT_PORT = 8765

#: A query longer than this is a mistake or an attack, and either way the
#: archive has nothing to say about it.
MAX_QUERY = 500
MAX_LIMIT = 100

#: How many unanswered questions the port will leave for review before it stops
#: recording them. Not a guess about demand — a ceiling on what an unbounded
#: local caller can put on the disk.
MAX_QUESTIONS = 200


def _payload(cfg: Config, path: str, params: dict[str, list[str]]) -> tuple[int, dict]:
    """Answer one request. Pure: reads records, returns a document."""
    if path in ("/", "/health"):
        store = RecordStore(cfg.layout)
        return 200, {
            "ok": True,
            "archive": {
                "papers": sum(1 for _ in store.iter_papers()),
                "concepts": sum(1 for _ in store.iter_concepts()),
                "findings": sum(1 for _ in store.iter_findings()),
            },
            "endpoints": ["/ask?q=...", "/health"],
            "writes": "none — this port is read-only",
        }

    if path == "/ask":
        query = (params.get("q", [""])[0] or "").strip()[:MAX_QUERY]
        if not query:
            return 400, {"error": "ask with ?q=<your question>"}
        try:
            limit = int(params.get("limit", ["20"])[0])
        except ValueError:
            limit = 20
        limit = max(1, min(limit, MAX_LIMIT))

        result = search(cfg, query, limit=limit)
        result["limit"] = limit
        if not result["hits"]:
            result["recorded"] = _record_question(cfg, query)
            # Said plainly rather than dressed up as an answer. What the archive
            # does not know is worth knowing, and a caller who is told "nothing"
            # can ask a person; one who is given a plausible near-match cannot.
            result["message"] = (
                "the archive has nothing on these terms. It answers only from "
                "what it has read — nothing here composes an answer."
            )
            return 404, result
        return 200, result

    return 404, {"error": f"no such endpoint: {path}", "endpoints": ["/ask", "/health"]}


def _record_question(cfg: Config, query: str) -> bool:
    """Leave an unanswered question where a person will see it.

    Into `requests/pending/`, as a request of kind `question`, because that is
    already the reviewed way in and inventing a second one would be a second
    thing to secure. Nothing reaches the archive from here: an approved question
    is work for a session, exactly like a colleague asking for a paper.

    Returns whether it was recorded. Content-addressed on the question, so a
    caller retrying does not accumulate files, and capped, because an
    unauthenticated port that can write without a ceiling can fill a disk.
    """
    folder = cfg.layout.requests_pending
    try:
        folder.mkdir(parents=True, exist_ok=True)
        existing = list(folder.glob("question-*.md"))
        path = folder / f"question-{title_fingerprint(query)}.md"
        if path.exists():
            return True
        if len(existing) >= MAX_QUESTIONS:
            _LOG.warning(
                "not recording: %d unanswered question(s) already waiting review",
                len(existing),
            )
            return False
        path.write_text(
            "---\n"
            "kind: question\n"
            f"from: {HOST} (ask endpoint)\n"
            "subject: asked and not found in the archive\n"
            "---\n\n"
            "Somebody asked this and the archive had nothing on it.\n\n"
            f"> {query}\n",
            encoding="utf-8",
        )
    except OSError as exc:  # pragma: no cover - a read-only or full disk
        # A question that could not be written is not worth failing an answer
        # over. The caller asked to read, and reading worked.
        _LOG.warning("could not record question: %s", exc)
        return False
    _LOG.info("recorded an unanswered question for review")
    return True


class _Handler(BaseHTTPRequestHandler):
    server_version = "ra-archive"
    sys_version = ""  # do not advertise the interpreter version

    cfg: Config  # set on the server instance below

    def do_GET(self) -> None:  # noqa: N802 - http.server's interface
        parsed = urlparse(self.path)
        status, body = _payload(self.cfg, parsed.path, parse_qs(parsed.query))
        self._respond(status, body)

    def do_POST(self) -> None:  # noqa: N802
        # There is no write endpoint, and saying so is better than a bare 404:
        # somebody trying to add knowledge should be told where that actually
        # happens rather than concluding the server is broken.
        self._respond(
            405,
            {
                "error": "this port is read-only",
                "how_to_contribute": (
                    "leave a markdown file describing the change you want; a "
                    "person reviews it before anything enters the archive"
                ),
            },
        )

    def _respond(self, status: int, body: dict) -> None:
        encoded = json.dumps(body, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        # Nothing here is a browser app, and a stale answer is worse than a slow
        # one when the archive is rebuilt several times a day.
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, fmt: str, *args) -> None:
        # Through the pipeline's logger, so a served request lands in the same
        # run log as everything else rather than on stderr.
        _LOG.info("%s %s", self.address_string(), fmt % args)


def build(cfg: Config, port: int = DEFAULT_PORT) -> ThreadingHTTPServer:
    """A server bound to loopback, ready to `serve_forever()`."""
    handler = type("_BoundHandler", (_Handler,), {"cfg": cfg})
    return ThreadingHTTPServer((HOST, port), handler)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.serve",
        description="Answer questions about this archive, read-only, on loopback.",
    )
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    args = parser.parse_args(argv)

    cfg = config_mod.load(args.root)
    log.setup(cfg.layout.logs, logging.DEBUG if args.verbose else logging.INFO)

    server = build(cfg, args.port)
    _LOG.info(
        "serving %s on http://%s:%d (read-only; ctrl-c to stop)",
        cfg.layout.root,
        HOST,
        args.port,
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        _LOG.info("stopped")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
