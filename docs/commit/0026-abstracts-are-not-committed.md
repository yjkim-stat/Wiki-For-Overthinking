# 0026 — Keep the ledger, not the abstracts

| | |
| --- | --- |
| **Commit** | `chore: gitignore data/abstracts/ and keep the coverage ledger` |
| **Scope** | `.gitignore`, `config/sources.yaml`, `README.md`, `CLAUDE.md` |
| **Kind** | chore |

## What changed

`data/abstracts/` is now ignored. `data/index/coverage.jsonl` stays committed.

The sweep introduced in [0025](0025-coverage-ledger-and-the-sweep.md) shipped
with both committed and named this as the alternative; this commit takes it.
Nothing in the pipeline changes — no flag, no code, no behaviour on a machine
that already holds the files.

## Why it is built this way

**The audit and the evidence have different weights and different costs to
lose.** The ledger is three integers per category-day. The abstracts are ~1.5 KB
per announced paper, on the order of 100 MB a year across four categories, and
they grow for as long as the archive runs. Committing both means the repository
gets steadily heavier to clone in order to avoid re-fetching text that arXiv
will hand back on request.

**Losing the abstracts is recoverable; losing the ledger is not.** A fresh clone
without the abstracts knows precisely what it is missing — that is what the
ledger is for — and re-fetches it worst day first under the existing per-run
budget. A fresh clone without the *ledger* cannot tell a day that held nothing
from a day we failed to read, which is the exact failure 0025 exists to detect
and which no amount of later crawling reconstructs.

**A large debt on a fresh clone is the ledger working, not failing.** This is
worth stating because it will look alarming the first time: a new checkout
reports a shortfall running to thousands. That number is honest, it is what a
fresh clone genuinely lacks, and it shrinks on its own.

**The choice is written where someone would change it.** The comment in
`config/sources.yaml` now says which of the three options this repository took
and what the other two cost, rather than describing them all as hypothetical.
A deployment that would rather crawl less than carry the weight un-ignores the
directory and nothing else.

## Trade-offs and rejected alternatives

- *Keep committing the abstracts.* Rejected: the weight is unbounded and grows
  with time, while the thing it buys — not re-fetching — is bounded and
  automatic.
- *Turn the sweep off (`sweep.enabled: false`).* Rejected: it would drop the
  per-day count, which is the only number in the pipeline that is not computed
  from our own parsing, and the only defence against the silent
  under-collection this repository has now hit several times.
- *Commit abstracts only for papers a topic matched.* Rejected: those are
  already in `data/papers/`. The point of `data/abstracts/` is the ones no topic
  wanted, which is what makes a threshold revisable later.
- The cost accepted here is real: a fresh clone crawls for days before its
  coverage is complete, and a deployment that clones often will feel it.

## What a reviewer should check

- `git ls-files data/abstracts` is empty. It was empty when this landed —
  ignoring a directory does not untrack files already in it, so had any been
  committed this would have needed `git rm --cached` as well.
- `data/index/coverage.jsonl` is **not** caught by the new rule. The whole
  arrangement fails silently if the ledger stops being committed.
- `CLAUDE.md` and the README both say "not committed" for this directory now.
  Note 0025 still describes it as committed and is left alone deliberately:
  notes are not rewritten after they are pushed, and it was accurate on the day
  it was written.

## Downstream impact

A deployment pulling this keeps whatever abstracts it already has on disk; they
simply stop being tracked. A **fresh** clone starts with a large recorded debt
and pays it down at `sweep.max_abstracts_per_run` per run.
