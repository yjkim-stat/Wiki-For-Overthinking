# 0036 — Taking the template back in, a second time

| | |
| --- | --- |
| **Commit** | `merge: take the template's code trees, and give this deployment its own note sequence` |
| **Scope** | `pipelines/`, `tests/`, `scripts/`, `templates/`, `workflows/`, `.claude/`, `docs/`, `config/concept-aliases.yaml`, `config/sources.yaml`, `config/topics/overthinking.yaml`; notes 0073/0074/0100 renumbered into `commit-local/` |
| **Kind** | chore · breaking |

## What changed

`src/main` had grown 120 commits since [0034](0034-taking-the-template-back-in.md).
This takes the code and leaves the archive alone.

Arriving: the `model` wiki kind (a checkpoint is not a corpus), the authored
alias map at `config/concept-aliases.yaml`, `pipelines/local/` (placeholder
rejection, DBLP abstract backfill, queue slot reservation, alias resolution),
GitHub repository candidates, a keyword-overlap check that runs before
collection, an entity-split report on every render, an outgrown-analysis notice
carried in the note itself, a graph that is rewritten only when it moves,
contested-identifier warnings on reading tasks, dated listing records, and eight
maintenance scripts. Their notes are `docs/commit/0067` through `0099` and
`docs/commit-local/0009` through `0032`.

Three decisions were taken here rather than upstream.

## Why it is built this way

**The merge is `-s ours` plus an explicit checkout of the code trees, because a
plain merge would have deleted the archive.** Upstream moved its own archive to
a repository of its own ([`docs/commit/0093`](../commit/0093-the-archive-moves-to-a-repository-of-its-own.md)),
so `src/main` no longer tracks `data/`, `archive/` or `outputs/` at all. This
deployment tracks 4,418 files across those three, and `git merge src/main` would
have proposed deleting every one that had not been touched since the merge base.

So the merge records the ancestry — future fetches see only new commits — while
the working tree keeps ours, and `pipelines/ tests/ scripts/ templates/
workflows/ .claude/ docs/ requirements.txt` are checked out from `src/main`
deliberately. The cost is stated plainly: **`-s ours` marks every upstream
commit as merged, so a path not listed above will never arrive on its own.**
The list is the whole interface and it is written here for the next merge to
copy.

`config/` was hand-merged rather than taken, because it is where this
deployment's editorial decisions live: our one topic, our arXiv categories, our
`refresh_definition_at: 2.0`, our OpenReview reason. Two new blocks were copied
into `config/sources.yaml` by hand — `conferences.abstracts` and `github`.

**This deployment stops writing in `docs/commit/`.** Both sides had an 0073 and
an 0074 by different authors about different things, which is the collision
[0034](0034-taking-the-template-back-in.md) already had to resolve once and
[0035](0035-a-source-that-answers-403-to-everything.md) tried to dodge by
jumping to 0100. Jumping does not work: upstream keeps advancing and will reach
0100 too.

Upstream had already solved this for itself and the solution arrived with the
merge — `docs/commit-local/`, a second sequence for a deployment's own notes,
with `docs/commit/` reserved for the template's. Upstream closed its local
sequence at 0032 when it stopped being a deployment. This one reopens it at
0033, and the three notes written here move into it:

| was | is |
| --- | --- |
| `docs/commit/0073-a-benchmark-sitting-is-one-entity-however-spelled.md` | `docs/commit-local/0033-…` |
| `docs/commit/0074-taking-the-template-back-in.md` | `docs/commit-local/0034-…` |
| `docs/commit/0100-a-source-that-answers-403-to-everything.md` | `docs/commit-local/0035-…` |

A pushed note is not normally rewritten. The rule that outranks it is the one
these three exist under: the side that duplicated a number is the side that
moves, and upstream pushed 0073 and 0074 first. Moving them once now is cheaper
than a third collision.

**Note 0033's code is dropped and its ruling is kept.** That note added a
year-variant auto-merge to `enrich/concepts.py` so `AIME24` and `AIME 2024`
would stop being two entities. Upstream answers the same question with an
authored map plus a report that merges nothing, which is
[0072](../commit/0072-two-names-for-one-entity.md)'s argument built out. The map
is strictly better here: it reaches `GRPO` against `Group-Relative Policy
Optimization` and `MATH-500` against `MATH500`, which a regular expression
cannot, and it refuses `MATH` against `MATH500`, which a regular expression
would not have been asked. So `concepts.py` is taken wholesale, our
`tests/test_concept_merge.py` is deleted with the function it tested, and the
rulings move into `config/concept-aliases.yaml` — including the year expansions
the regular expression used to do, now written down where somebody can disagree
with them.

## Trade-offs and rejected alternatives

**Rejected: merging normally and restoring the archive afterwards.** A
modify/delete conflict on 4,418 files is not a merge anybody can review, and the
files that were *not* modified since the merge base would have been deleted
silently rather than conflicting.

**Rejected: cherry-picking the 27 non-archive commits.** They interleave with
upstream's own archive digests and several depend on each other; the result
would be the same tree with a history nobody can bisect.

**Accepted cost: the queue grew.** Applying the alias map retired 20 concept
records and cleared 4 definitions that had each been written against a fraction
of their entity's evidence, so those re-derive. Wiki notes went 238 → 225 and
`fragmented` went 12 → 0. That is the merge doing its job, but it is work
arriving, not work finished.

**Accepted cost: 277 readings name no model.** The `model` kind is live and
every existing reading predates the field, so `render` now reports them every
pass. `scripts/backfill_summary_models.py` exists for this and has not been run.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 843 tests, green. One failure
  had to be fixed to get there and it was a real defect: `test_keyword_overlap`
  found `reasoning token` and `reasoning-token` both listed in
  `config/topics/overthinking.yaml`, scoring the same words twice. The
  hyphenated spelling is deleted; the matcher is word-boundary based and already
  counted it. `KNOWN` in that test is now empty for this deployment.
- `git ls-files data archive outputs | wc -l` — 4,418, unchanged by the merge.
- `python3 -m pipelines.render` — `fragmented: 0`, `papers: 281`.
- `docs/LOCAL-DELTAS.md` — its opening claim that no `src` remote exists is
  upstream's and is false here; a blockquote now says so. Read the rest of that
  file before replacing anything under `pipelines/`: it is the register of what
  a wholesale file replacement would silently delete.
- `config/topics/` holds `overthinking.yaml` and `_template.yaml` and nothing
  else. Upstream's five topics were deliberately not taken — what a group tracks
  is its own editorial decision.

## Downstream impact

For the next merge from `src`: repeat the `-s ours` plus explicit-checkout
recipe above, re-read `docs/LOCAL-DELTAS.md`, and hand-merge `config/`. New
notes go in `commit-local/` from 0037.
