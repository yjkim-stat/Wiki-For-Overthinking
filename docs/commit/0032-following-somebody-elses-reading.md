# 0032 — Following somebody else's reading

| | |
| --- | --- |
| **Commit** | `feat(collect): follow curated weekly lists as a source of pointers` |
| **Scope** | `pipelines/collect/curated.py`, `pipelines/collect/arxiv.py`, `pipelines/run_daily.py`, `config/sources.yaml`, `tests/test_curated.py`, docs |
| **Kind** | feature |

## What changed

A fifth source: `curated`, which reads a weekly "papers of the week" list and
files what it points at. `config/sources.yaml` ships with
[DAIR.AI's](https://github.com/dair-ai/ML-Papers-of-the-Week) and takes any
other list published as markdown.

Every other source answers a question the pipeline asked. This one carries
somebody's judgement over a field's whole weekly output — a filter no keyword
can reproduce, applied before any keyword sees the paper.

The list is read for **pointers only**. Its entries name papers the way people
say them out loud, so the bibliography is fetched from the arXiv id the entry
links to, through the same lookup that resolves a topic's seed papers. That
lookup grew a `source` argument so a curated pick is not filed as a seed: how a
paper came to our attention is a different fact from which endpoint answered
for it.

## Why it is built this way

**An entry is not a record, and nothing pretends otherwise.** A real entry reads

> `1) **NOOA** - Agent development today is split across prompt templates, …`

`NOOA` is a nickname and the rest is the editor's commentary. Writing that into
`title` would be wrong in the one field every other record keys on — dedup,
the wiki's entity slugs, the citation in a lecture note — and it would look
plausible while being wrong. So the entry contributes exactly one thing, the
arXiv id, and the archive gets the record it would have had if a collector had
found the paper first. A pick already held is re-emitted with `source` set to
this collector, so the ordinary merge stamps `arxiv+curated` onto it rather
than creating a second entity: being chosen is information worth keeping, and
it is kept on the record that already exists.

**Curated picks are scored; hand-filed PDFs are not.** These look like the same
exemption and are not. A PDF in `inbox/` bypasses scoring because filing it *is*
the group's editorial decision — the thing scoring approximates. A weekly list
is somebody else's decision, taken over a whole field rather than over the
group's topics. Letting it bypass scoring would quietly hand an outside editor
the power to decide what the group tracks. Most of a general list being
rejected against a narrow archive is the filter working.

**Recency comes from the index, not from an assumption about sort order.** The
collector matches each index entry's anchor against the headings on the page it
links to. Taking the first N headings would be simpler and would work today —
and the day the page is reordered it would read the same old issues forever
while every log line still looked healthy. When no heading matches, it does
fall back to page order, and warns while doing it.

**Only the labelled link is followed.** An issue's commentary routinely cites
work the editor did *not* pick; following those links would archive what was
mentioned rather than what was chosen.

**A parse of zero warns.** The format is one editor's markdown and can be
reshaped without notice. A silent zero is indistinguishable from a quiet week,
which is the failure this collector is most exposed to.

## Trade-offs and rejected alternatives

**LinkedIn, which is where the request started, is not fetchable.** It answers
403 to anything without a session, and the Substack edition is a mailing list.
The GitHub markdown mirror carries the same papers and is public, so that is
what the config points at. If the mirror stops being maintained, this collector
stops finding papers and says so — it does not silently fall back anywhere.

**Picks that are not on arXiv are skipped, by name, in the log.** Measured over
25 issues of the shipped list, 237 of 250 picks carried an arXiv id and 13 did
not — blog posts, a Nature page, an SSRN entry, project sites. Keeping those
would mean either inventing a title from the nickname (refused above) or
building a second metadata path per host. The escape hatch already exists and
costs one command: put the PDF in `inbox/`. This is the change's real gap, and
it is why the skipped links are named rather than counted.

**Rejected: resolving DOIs for the non-arXiv picks.** A Crossref lookup would
recover the Nature and SSRN entries, roughly a third of the residue. It is a new
host, a new parser and a new failure mode for about four papers a year, and the
inbox already covers it. Worth reopening if a deployment's list is mostly
journal-published work rather than preprints.

**Rejected: a `keep_all` flag to bypass scoring.** It would have to reach into
`run_daily`'s accept condition, which currently says one thing — a *hand-filed*
paper is never rejected — and would then say two. If a group genuinely wants
every pick from a list, the honest form is a topic whose keywords say so.

**Cost.** Two GET requests per list per run, plus one batched arXiv lookup per
25 unresolved picks. Picks already in the archive are never looked up again.

## What a reviewer should check

- **That a nickname never reaches `title`.** `tests/test_curated.py` asserts the
  record is titled from the arXiv feed and that `NOOA` is absent. Break it by
  deleting the label filter in `_paper_links` and watch five tests fail.
- **That the anchor matching is doing work, not decorating.** Disable it
  (`matched = []`) and two tests fail, including the one asserting that a
  `## How this list is made` section is not an issue.
- **The live parse, which is checkable without arXiv.** GitHub is reachable from
  environments where `export.arxiv.org` is not:

  ```bash
  python3 -c "
  from pipelines.collect import curated
  from pipelines.common.http import Client
  ids, others, issues = curated._read_list(
      Client(min_interval_s=1.0),
      'https://raw.githubusercontent.com/dair-ai/ML-Papers-of-the-Week/main/README.md',
      4, 'Paper')
  print(len(issues), len(ids), others)"
  ```

  Four issues, forty ids, no unresolved links, at the time of writing.
- **The degraded path.** Where arXiv is blocked, collection reports the picks it
  could not resolve by id and files nothing — verified in exactly that
  condition. Nothing about that path was exercised against a *reachable* arXiv,
  because none was available here.

## Downstream impact

A deployed copy picks this up on its next pull and starts reading the DAIR.AI
list on the following run, because `curated.enabled` ships as `true` and the
list is populated. To opt out, set `curated.enabled: false` or empty
`curated.lists`.

The list is general-AI; a narrowly scoped archive should expect most picks to
land in `data/index/rejected.jsonl` rather than in the archive. Papers that do
clear scoring are ordinary records and cost one reading task each.

`--source` gains `curated`; existing invocations are unaffected. Records already
in `data/` are untouched until a curated run stamps `+curated` on one it holds.
