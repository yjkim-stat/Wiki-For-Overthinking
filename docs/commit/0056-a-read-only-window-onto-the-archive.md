# 0056 — A read-only window onto the archive

| | |
| --- | --- |
| **Commit** | `feat(serve): answer questions from the archive, read-only, on loopback` |
| **Scope** | `pipelines/serve.py`, `pipelines/common/search.py`, `tests/test_serve.py`, `README.md`, `CLAUDE.md` |
| **Kind** | feature |

## What changed

`python3 -m pipelines.serve` opens `http://127.0.0.1:8765`. Other people on the
same host can ask the archive what it knows without a clone, a checkout, or any
way to change what they are reading.

```
GET /ask?q=causal+inference  → findings, definitions, readings, ranked
GET /health                  → what the archive holds
POST anything                → 405, and where writing actually happens
```

This is the read half of a feature whose write half — a request somebody wants
acted on — goes through a staging directory and a person, and is deliberately
not reachable from this port. That half is not in this commit.

## Why it is built this way

**It composes nothing.** Every hit is a record the archive already wrote. The
pipeline calls no model, so a server that produced prose would be either
inventing it or reaching outside the process, and both are excluded by the
contract the rest of this repository rests on. A colleague given a plausible
invented answer cannot tell it from a real one, which makes it worse than the
honest 404 this returns instead — and that 404 says so in as many words.

**Findings outrank definitions outrank readings.** That is the archive's own
ordering of authority, and it is the one place a search can carry judgement
without inventing any: the group's settled position, then what somebody wrote
about a term over all its sources, then what one paper said. A search returning
twelve papers ahead of the sentence the group had already agreed on would be
answering a different question. An unread paper still appears, last and with an
empty body, because "we hold this and have not read it" is worth saying.

**Presence, not frequency.** A paper that says "world model" nine times is not
nine times the answer, and counting occurrences would rank a long document above
a definition written precisely about the term.

### The three properties that make it safe to open

**Loopback only, with no flag to change it.** "Other users on this machine" is
the entire audience. A host that wanted to publish its archive would put a proxy
in front and make that decision where it can be seen, rather than by passing
`--host`. A test asserts the string `0.0.0.0` does not appear in the module.

**Nothing opens a path a caller named.** Answers come from records looked up by
id through `RecordStore`; there is no file-serving endpoint at all, so an
unknown id is a 404 rather than a traversal.

**Bounded per request.** The query is truncated at 500 characters, the result
count capped at 100, and POST refused before a body is read. An unauthenticated
local port is reachable by every process on the box, including ones nobody meant
to run.

There is **no authentication**, and that is a decision rather than an oversight.
On a shared host, loopback means "any local user", so the read-only guarantee is
what makes it acceptable — which is why that guarantee is asserted rather than
asserted-to.

## Trade-offs and rejected alternatives

**Search is keyword matching, not semantics.** It shares one matcher with topic
scoring ([note 0055](0055-one-rule-for-what-counts-as-a-mention.md)) so the two
cannot disagree about what a mention is. A question phrased in words the archive
does not use returns nothing, and says so. Embeddings would need a model and a
dependency, and would make "why did this come back" unanswerable — which is the
property `enrich/score.py` was explicitly built to keep.

**Stdlib `http.server`, no framework.** The dependency list is one line and this
does not lengthen it. `ThreadingHTTPServer` is enough for colleagues on one box;
it is not enough for a public endpoint, which is another reason not to make one
reachable.

**An answer can be stale by minutes.** It reads records, not a cache, so it is
current as of the last render — and `Cache-Control: no-store` keeps a client
from holding it longer. An archive rebuilt several times a day makes any cache
worse than the read.

**Nothing records what was asked.** A question that finds nothing is exactly the
thing the archive would benefit from knowing, and writing it down here would
give an unauthenticated local port a write path. That belongs with the request
lane, behind the same review, and is the next commit.

## What a reviewer should check

- `test_serving_every_endpoint_changes_no_record` snapshots `data/` by content,
  exercises every endpoint including a traversal-shaped query, and requires the
  snapshot unchanged. This is the property the whole design rests on; it is
  asserted the way `tests/test_layering.py` asserts its boundary.
- `BindingTests`, both of them: the socket's address and the absence of any way
  to configure it.
- **The cap test, and why it is written the way it is.** Counting returned hits
  passed whether or not the cap existed, because no fixture has more records
  than the cap. The response now states the limit it applied — which is also
  better behaviour, since a parameter quietly ignored is worse than one refused
  — and the test asserts on that.
- That a 404 carries the terms it searched for. A search that found nothing is
  only useful if you can see what it looked for.

## Downstream impact

New command, nothing existing changes. The server is not started by anything —
no scheduled job, no `daily.sh` — so a deployment that does not run it is
unaffected, and one that does should know it has opened a port that every local
user can reach.
