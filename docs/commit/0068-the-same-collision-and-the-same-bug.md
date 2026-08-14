# 0068 — The same collision, and the same bug

| | |
| --- | --- |
| **Commit** | `chore: take the upstream update, renumber again, and give up our counter` |
| **Scope** | merge of `origin/main`; `pipelines/render.py`, `pipelines/publish/graph_page.py`, `docs/commit/` renumbering, `docs/commit/README.md`, `docs/LOCAL-DELTAS.md`, `docs/issues/` |
| **Kind** | chore |

## What changed

Six commits from `origin/main` are now in this branch:

- **[0049](0049-a-citation-rather-than-a-rumour.md)** — `data/references/`, a
  record for a page checked outside the archive, with the date it was read and
  the passage relied on. A reference is cited by a finding and is explicitly
  **not** evidence for a wiki entity, so two blog posts cannot promote a concept.
- **[0050](0050-three-claims-three-weights.md)** — the graph drew an authored
  link as the faintest edge on the page, because the edge literal outlived the
  field it named.
- **[0051](0051-a-citation-appears-where-it-is-not-evidence.md)** — the visible
  half of that split: `## Checked against`, below a note's sources and never
  among them.
- **[0052](0052-a-task-is-a-function-of-its-record.md)** — a pending task never
  learned that its document had arrived, so `backfill` fetched PDFs that no
  reader was ever shown.
- **[0053](0053-the-other-direction-of-the-same-question.md)** — `migrate` now
  reports documents no record claims.
- **[0054](0054-the-queue-reports-what-it-wrote.md)** — `summaries_queued`
  counted the backlog rather than the tasks it filed.

Our thirteen notes moved up by six, from 0049–0061 to 0055–0067. Two of them are
marked superseded, for the reason below.

## Two sessions, one bug

**[0054](0054-the-queue-reports-what-it-wrote.md) and our
[0066](0066-a-counter-that-counts-attempts.md)/[0067](0067-the-log-line-said-seventy-six.md)
are the same defect, found independently within a day.** Both sessions noticed
that a counter named for tasks filed was reporting records considered, and both
noticed it because the number would not move. Ours surfaced when a render
announced four definition tasks queued while `pending_concepts` stayed at zero;
upstream's surfaced as `summaries_queued: 512` on every pass of an archive whose
queue gained nothing.

**Upstream's fix is better and it is the one that survived.** Ours corrected the
two call sites by measuring `count_pending()` on either side; upstream moved the
counters inside `Queue`, where the writes happen, and split one wrong number
into three right ones — `queued`, `refreshed`, `unread`. The difference is not
style. A caller cannot learn what was written from `enqueue`'s return value
because a summarizer sits in between and reports only whether it deferred, which
is a fact about the backend. Counting at the write is the only place the two
cannot drift, and it also covers the refresh path that 0052 added, which our
version had no way to see.

So our two commits stay in history, their notes stay in the directory with a
superseded banner, and the code they describe is gone. That is the honest record:
the bug was real, we fixed it, and somebody fixed it better.

## The renumbering, for the second time

`CLAUDE.md` step 0 says to pick `NNNN` against a fetched `origin/main`. Both
sessions did — against the same `origin/main`, before either had pushed. The
rule that decides who moves is unchanged and was applied the same way as in
[0062](0062-taking-the-update-and-giving-up-our-numbers.md): **a number is fixed
once pushed**, upstream's 0049–0054 are on `origin/main`, and ours were fifty-one
local commits that have never left this machine.

This is the second time in three days. It is not a failure of the rule — the
rule is what made the collision detectable at merge instead of at some later
point — but it is evidence that fetching once at the start of a session is not
enough when the session is long. Sixteen hours passed between this session's
first fetch and this merge.

Commit messages still name the old filenames; as in 0062, they are left alone.
The offset for this move is six, applied to 0049–0061.

## What the merge nearly cost

Five files were changed on both sides, and every one of them is a delta site:
`common/paths.py`, `common/schema.py`, `enrich/queue.py`, `publish/graph_page.py`
and `render.py`. Three merged clean; two conflicted and both conflicts were
inside a delta.

- `graph_page.py`: upstream added `_edge_styles` and gave `_legend` a second
  parameter, in the same hunk as our `"model"` entry in the kind order. Taking
  either side whole would have lost the other.
- `render.py`: the conflict *was* the duplicate fix.

Every delta was checked against `docs/LOCAL-DELTAS.md` afterwards, entry by
entry, and all survive. The suite is 600 tests, up from 545.

## The register gained an entry it should have had

`CLAUDE.md` is template-shaped, `origin/main` edits it, and five things in it are
ours — including **the bullet that tells the next session the register exists.**
It was not registered. It survived two template updates by luck, because
upstream happened to edit other sections both times.

It is entry 6 now. Losing that bullet would fail nothing, log nothing, and leave
the next update free to revert the `model` kind, the three collection fixes and
the alias map with no instruction anywhere to check — which is precisely the
failure mode the register was created for, aimed at the register.

## What a reviewer should check

- `grep -rn "LOCAL" pipelines/` still finds every site named in the register,
  and `tests/test_local*.py` and `test_model_kind.py` pass.
- `render`'s result dict: `summaries_queued` and `definitions_queued` now count
  tasks written, with `summaries_unread` carrying what the old number meant. On
  this archive that is `queued: 0, unread: 68`, and 68 is correct — 40 have
  tasks, 28 are waiting for a slot under the cap.
- The reserve delta still holds back half the cap on the first pass and releases
  it after the definitions, and now sums `queued`/`refreshed` across the two
  passes while *replacing* `unread`, which is a snapshot rather than a total.
