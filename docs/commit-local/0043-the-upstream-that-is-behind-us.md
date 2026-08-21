# 0043 — The upstream that is behind us

| | |
| --- | --- |
| **Commit** | `merge(src): take the ACL Anthology collector, and nothing else` |
| **Scope** | `pipelines/collect/anthology.py`, `pipelines/collect/conferences.py`, `scripts/install-cron.sh`, `tests/test_anthology.py`, `tests/test_install_cron.py`, `config/sources.yaml`; `docs/commit-local/0043-the-upstream-that-is-behind-us.md` |
| **Kind** | chore · merge · breaking |

## What changed

The `src` remote was repointed to `git@github.com:yjkim-stat/Wiki-For-Any.git`
and this is the first take from it. **Four files were checked out of
`src/main` and nothing else was**, against a `-s ours` merge that records the
ancestry without letting the tree move:

```
pipelines/collect/anthology.py      new — the ACL Anthology event-page collector
tests/test_anthology.py             new
scripts/install-cron.sh             new
tests/test_install_cron.py          new
```

`pipelines/collect/conferences.py` and `config/sources.yaml` were hand-edited
to wire the collector in. `ACL` gains `anthology_key: "acl"`. The suite goes
from 852 tests to 892, green.

## Why it is built this way

**The recipe in `docs/LOCAL-DELTAS.md` and [0036](0036-taking-the-template-back-in-a-second-time.md)
assumes `src` is ahead of us. Against this remote that assumption is false,
and following the recipe would have destroyed work.** The recipe's second step
is a wholesale `git checkout src/main -- pipelines/ tests/ scripts/ ...`. Here
is what that would have done:

- **Reverted [0039](0039-a-url-the-identifier-already-implies.md).**
  `src/main`'s `backfill.py` has no arXiv PDF-URL derivation — `grep` for
  `arxiv.org/pdf` in it returns nothing. Its `tests/test_backfill.py` is 52
  lines shorter, because the five cases that fix added are not there.
- **Deleted the `model` entity kind.** `src/main` is the template, so it has
  `KINDS = ("concept", "method", "dataset")`. 123 wiki entities and 33 notes
  in this deployment depend on the fourth.
- **Erased 39 of the 59 `LOCAL` marks in `pipelines/`.** This is the subtle
  one and it is worth stating plainly: **the diff between our tree and
  `src/main` is, for most files, the deletion of the word `LOCAL:` from a
  comment and nothing else.** `arxiv.py`, `arxiv_listing.py`, `common/config.py`
  and `render.py` differ from ours only that way — same code, annotations
  laundered. `Wiki-For-Any` is this pipeline re-published as a generic
  template ("The pipeline, with no archive in it"), not a newer version of it.
  Taking those files would change no behaviour and would remove the marks
  `LOCAL-DELTAS.md` names as the mechanism for finding deltas at all.

**So the take was reduced to what is genuinely new**, which is one feature:
the Anthology collector, plus a cron installer and their tests. Everything
else in the 20-file `pipelines/` diff was either a stripped annotation or a
regression.

**`-s ours` is still the right merge strategy, and now for a second reason.**
It marks every upstream commit as merged so a later fetch does not re-offer
them, while the tree stays ours — meaning a path not in the checkout list can
never arrive on its own. Against an upstream that is behind, that property is
not a precaution but the whole design.

**The collector's own reason for existing is that it is the only source here
that returns abstracts with the listing.** One request per venue-year returns
a whole programme with abstracts in it, so an ACL paper is scored on the
evidence a reader would have. Every other index either carries no abstract
(DBLP) or costs a second request per match (the programme pages). Its default
also keeps co-located workshops out — a workshop paper is published at the
workshop, and filing one under `ACL` would put a false claim in the archive —
and names in the log what it left out rather than dropping it silently.

## Trade-offs and rejected alternatives

**Rejected: taking EMNLP, NAACL and COLM too.** `src/main` declares all three
alongside ACL and each is one line. What this group tracks is its own
editorial decision and only ACL was asked for.

**Rejected: not merging at all and copying the file in.** Then a later `git
fetch src` would keep offering the same commits with no record that they were
considered, and the next session would have to redo this analysis.

**Accepted cost: the merge commit claims more than was taken.** `-s ours`
records `src/main` as merged in full while two of its commits' contents are
mostly absent. That is what this note is for.

**Left undone: `docs/`.** `src/main` carries 98 files under `docs/` against
our 148, including its own `docs/commit/` sequence at 0103. None was taken —
our `docs/commit/` is upstream's and this deployment does not write there, and
merging two note sequences is exactly the collision
[0036](0036-taking-the-template-back-in-a-second-time.md) closed.

## What a reviewer should check

- `grep -rn "LOCAL" pipelines/ | wc -l` → 59, unchanged from before the merge.
- `grep -n "arxiv.org/pdf" pipelines/backfill.py` → still present; 0039 survives.
- `python3 -m unittest discover -s tests -t .` → 892 tests, OK.
- `python3 -c "from pipelines.common import config; c=config.load(); print([v['name'] for v in c.sources['conferences']['venues'] if v.get('anthology_key')])"` → `['ACL']`, and no other venue.
- `git tag pre-upstream-merge-2026-08-22` is the rollback point.
- Not yet exercised against the network: the next `run_daily` is the first
  time the collector actually reads an event page.

## Downstream impact

For this deployment: the next collection run adds one request per ACL year
(2026 and 2025 by default) and ACL papers now arrive with abstracts rather
than titles alone.

**For anyone repeating this merge: read the direction first.** The question is
not "what is new upstream" but "is upstream ahead". `grep -c LOCAL` on both
trees and a `git diff --stat HEAD src/main -- pipelines/` answer it in under a
minute, and the answer here was no.
