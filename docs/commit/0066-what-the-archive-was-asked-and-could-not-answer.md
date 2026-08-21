# 0066 — What the archive was asked and could not answer

| | |
| --- | --- |
| **Commit** | `feat(serve): leave an unanswered question for review` |
| **Scope** | `pipelines/serve.py`, `tests/test_serve.py`, `README.md`, `requests/README.md` |
| **Kind** | feature |

## What changed

A `/ask` that finds nothing now leaves the question in `requests/pending/` as a
request of kind `question`, and says so in the 404. Named as the next step in
[note 0056](0056-a-read-only-window-onto-the-archive.md) and left until the
write lane existed to receive it.

## Why it is built this way

**What the archive does not know is the most useful thing this port produces.**
It is the only signal anywhere of what people came looking for and did not
find — every other measure in this repository counts what *is* here — and it was
being discarded the moment the caller closed the connection.

**Into the drop folder, not into `data/`.** It is a request like any other and a
person approves it, because a second way in would be a second thing to secure.
The guarantee from 0056 is unchanged and still asserted: `data/` is
byte-identical across every endpoint, now including one that writes.

**Content-addressed and capped.** The same question retried is one file, and the
folder stops accepting new ones past `MAX_QUESTIONS`. This is an unauthenticated
port reachable by every process on the box; a write path without a ceiling is a
way to fill a disk, and content-addressing alone would not stop somebody asking
a thousand *different* nonsense questions.

**A failed write does not fail the answer.** A read-only filesystem or a full
disk logs a warning and returns `recorded: false`. The caller asked to read, and
reading worked; refusing the answer because the bookkeeping failed would be
serving the archive's convenience over theirs.

**Only unanswered questions are recorded.** A question the archive answered
needs no human attention, and recording every query would turn the review folder
into a log nobody reads.

## Trade-offs and rejected alternatives

**The port's promise changed and the docstring changed with it.** It said "never
writes ... not anywhere", which is now false. The precise guarantee — never
`data/`, and exactly one staging file — is what the module and the README now
say. A note that let the old sentence stand would be the kind of stale claim
this repository has been bitten by.

**No rate limit, only a cap.** A caller can reach the cap as fast as it likes and
then be refused. Rate limiting an unauthenticated local port means holding state
per caller, and on loopback there is no caller identity to hold it against.

**Questions are not deduplicated against the archive's own vocabulary.** Two
phrasings of one gap are two files, and the reviewer sees both. Collapsing them
would mean deciding they are the same question, which is the judgement the
review exists for.

**Nothing prunes them.** A question approved or rejected moves out of `pending/`
by the ordinary route; one that is neither sits there and counts against the
cap. That is visible rather than silent, which is the intended failure.

## What a reviewer should check

Four mutations, each taking down its own test: remove the cap, make the filename
random rather than content-addressed, stop recording, and write front matter the
review path cannot parse.

- `test_it_lands_as_a_reviewable_request` reads the file back through
  `pipelines.requests` and asserts it validates. A file the reviewer's own tool
  rejects would be worse than no file.
- `test_it_still_touches_no_record` — the guarantee that made the port safe to
  open is unchanged.
- `test_a_question_the_archive_answers_is_not_recorded`.

## Downstream impact

A deployment running `serve` will accumulate `question-*.md` files in
`requests/pending/` as people ask things it cannot answer. They are reviewed with
`python3 -m pipelines.requests`, like anything else in that folder, and
`requests/pending/` is gitignored so they do not reach the repository unless
approved.
