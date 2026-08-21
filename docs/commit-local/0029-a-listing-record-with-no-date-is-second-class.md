# 0029 — A listing record with no date is second-class

| | |
| --- | --- |
| **Commit** | `fix(collect): date a listing record by the day it was announced under` |
| **Scope** | `pipelines/collect/arxiv_listing.py`, `tests/test_arxiv_listing.py` |
| **Kind** | fix |

## What changed

Papers recovered from arXiv's listing pages now carry `published` and `year`,
taken from the announcement-day heading the entry was listed beneath. `Entry`
gains an `announced` field, `parse_days` fills it, `collect` reads the page with
`parse_days` instead of `parse_listing`, and `_to_paper` sets the two fields.

Before this every listing-derived record had `published=''` and `year=0`.

## Why it is built this way

**An empty date is not a neutral default here.** `publish/archive.py` computes a
paper's page path from its year and falls back to the literal string `unknown`,
and `store.rebuild_indexes` sorts the flat index by `published` descending, so a
dateless paper lands in `archive/papers/unknown/` and below every dated paper in
the index. The consequence is that a paper would be filed worse **because of
which collector found it** — the API missed it and the listing caught it — which
has nothing to do with the paper.

**The day heading is the right value, and it is the only one on offer.** A
listing page carries no per-paper submission date; what it has is the
announcement day, which arXiv sets the evening after the submission cutoff. That
is close enough for the uses `published` has here — ordering, year bucketing,
and the lookback window — and it is a real date read off the page rather than an
inference.

**The day belongs to the section, so `parse_days` is what can know it.**
`parse_listing` sees one entry's `<dt>`/`<dd>` pair and genuinely cannot tell
which day it sits under; that is why the field is filled in `parse_days` and
left empty by `parse_listing`. Reading the page with `parse_days` in `collect`
is what carries the day through, and on a page with no headings it degrades to a
single undated day holding every entry — exactly what `parse_listing` returned
before.

**An undated page still produces an undated record.** No date is guessed from
the arXiv identifier, from the crawl time, or from the category. If the page did
not say, the field stays empty, which is the same rule the rest of this
repository follows about inventing values.

## Trade-offs and rejected alternatives

- *Derive the date from the arXiv identifier.* The `2608.xxxxx` form encodes
  year and month, and it is tempting because it needs no page structure.
  Rejected: it gives the wrong day for anything announced across a month
  boundary and invents precision the source did not provide.
- *Fall back to the crawl date when the page has no heading.* Rejected for the
  same reason — it would record when we looked rather than when arXiv
  announced, and the two diverge exactly when a sweep is behind.
- *Fix `archive.py` to handle dateless papers gracefully instead.* Rejected as
  the primary fix: the record being dateless is the defect, and the archive
  behaviour is a reasonable response to a record that genuinely has no date.
- The cost accepted: announcement day is not submission day. A paper submitted
  just before a cutoff is announced the same evening; one submitted just after
  waits a day. For ordering and year bucketing this does not matter, and for
  anything that needs the true submission timestamp the API record is the one
  to prefer — which deduplication already does, since `merge_papers` keeps the
  earliest `published` it has seen.

## What a reviewer should check

- `merge_papers` in `enrich/dedupe.py` takes the **earlier** of two publication
  dates. That is what keeps an announcement day from overwriting a real
  submission date when the same paper later arrives from the API, and it is the
  interaction most likely to be wrong if either side changes.
- `parse_listing` still reports an empty `announced`, and the test asserts it.
  If that ever starts being filled, the two parsers have been conflated and the
  claim that the day belongs to the section is no longer what the code does.
- Pagination in `collect` now counts entries flattened across days rather than
  from one `parse_listing` call. The break conditions use the same totals as
  before; `sweep` already counted this way.

## Downstream impact

None for records already stored — no listing-derived paper exists in this
archive, because the fallback has never fired in a scheduled run (see
[0030](0030-one-topic-with-results-hid-the-others.md)). New listing records will
have real dates from the next run. A deployment that already holds dateless
listing records keeps them; nothing backfills, and a re-collection would merge a
date in through the ordinary dedup path.
