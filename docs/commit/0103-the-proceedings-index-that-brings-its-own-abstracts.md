# 0103 — The proceedings index that brings its own abstracts

| | |
| --- | --- |
| **Commit** | `feat(collect): read the ACL Anthology for the *ACL venues` |
| **Scope** | `pipelines/collect/anthology.py`, `pipelines/collect/conferences.py`, `config/sources.yaml`, `tests/test_anthology.py`, `docs/API.html`, `README.md` |
| **Kind** | feature |

## What changed

A collector for `aclanthology.org`. A venue takes part by carrying an
`anthology_key` in `config/sources.yaml`; ACL, EMNLP and NAACL now do. It runs
inside `conferences.collect`, once for every topic rather than once per topic,
on the same footing as the programme-page collector and for the same reason: an
event page is the same page whoever is asking.

This closes a hole the previous commit opened. Turning DBLP off left the `*ACL`
venues on one index — Semantic Scholar — because they carry no `virtual_host`
and OpenReview answers anonymous clients with a challenge. They are back on two,
and the second one is better than the one they lost.

## Why it is built this way

**One request returns the whole programme, abstracts included.** This is the
only source in the tree that does. Every other HTML index gives titles and makes
the collector pay a request per match for the abstract it needs to score
properly — `arxiv_listing` says so in its own docstring and calls it a real loss
of recall. Here the abstract is inline, so a paper is scored on the evidence a
reader would have, and a venue-year costs exactly one request no matter how many
topics are tracked.

**An event is not only its conference.** The page lists the main tracks,
Findings, and every co-located workshop: NAACL 2024 carries 958 papers in the
venue's own volumes and roughly six hundred more from SemEval, WOAH, BEA and a
dozen others. A workshop paper is published at the workshop. Filing one under
`venue: NAACL` would put a claim in the archive that is not true, and it would
be invisible afterwards, because nothing downstream knows which volume a record
came from. So the default keeps `<key>-*` and `findings-<key>`, widening is one
config line, and **what was left out is named in the log** — a run that quietly
halved its own reach reads exactly like a quiet year.

**The identifier is exact, which is rare here.** An entry's anthology id yields
its DOI as `10.18653/v1/<id>`, so records arrive with a real identifier instead
of a title fingerprint. The same work collected from arXiv folds against it
through the `title:` key `dedupe` registers for both, and the arXiv record gains
the venue it was published at. The pattern is asserted only for the dotted id
form; pre-2020 volumes are numbered `P19-1001` and are deliberately not matched,
so the DOI is never guessed.

**Two things about the markup are load-bearing, and both were found by running
it rather than by reading it.** Attributes are served unquoted — a pattern
written for `href="..."` matched nothing at all on the live page. And letters
whose case must survive are wrapped mid-word in `acl-fixed-case` spans, so
`InsCL:` is three elements; replacing tags with a space, which is what
`common/html.text` does and is right everywhere else, produced `I ns CL :`.
That title would fail to match a keyword it contains, sort wrongly in the index,
and title a wiki note with a name that appears in no paper. `_clean` removes
inline tags with no separator and only breaks on tags that end a line.

## Trade-offs and rejected alternatives

- *Fetch each paper's own page.* Rejected: the event page already has
  everything, and a venue-year would cost a thousand requests instead of one.
- *Take the whole event, workshops included.* Rejected above — it is not that
  the papers are unwanted, it is that the venue recorded would be false. A
  deployment that wants them sets `volumes`.
- *Filter to the main tracks only, dropping Findings.* Rejected: Findings is the
  venue's own volume and its papers are cited as such.
- *Change `common/html.text` to stop inserting spaces.* Rejected — that helper
  is right for pages of prose, and every other collector depends on it. The
  fixed-case span is an Anthology convention and belongs in the Anthology's
  parser.
- **Cost:** the pages are large, 4 MB for NAACL 2024 and 19 MB for ACL 2026, and
  they grow every year. `max_bytes` refuses one that has become absurd rather
  than parsing it; the default of 32 MB leaves room for a few more years.
- **Cost:** the volume filter means a run collects less than the page offers.
  That is deliberate, and it is logged rather than silent.

## What a reviewer should check

```bash
python3 -m unittest tests.test_anthology -v
```

25 tests. The fixture keeps both markup traps, so a parser rewritten from
memory fails on it. Six mutations were confirmed to fail the suite: accepting
only quoted attributes, admitting front matter, matching an abstract
positionally instead of by id, defaulting the volume filter to everything,
dropping the left-out report, and ignoring `max_bytes`.

The seventh mutation is the one worth knowing about. An earlier version of
`test_the_abstract_is_matched_to_its_own_paper` passed whether or not the
abstract was keyed by id, because every entry in the fixture had exactly one
abstract inside its own slice — the test asserted a property it could not
distinguish. The fixture now contains an entry with no abstract followed by a
stray block belonging to another paper, which is the case a positional match
gets wrong, and the mutation fails.

Against the live site, one request to `events/naacl-2024/` returns 1,561
entries, 1,550 of them with abstracts.

## Downstream impact

**A deployment that pulls this and tracks ACL, EMNLP or NAACL will start
collecting from a source it was not using.** Records arrive with `source:
anthology`, a `doi:` id and a populated abstract. Nothing has to be edited: the
venue entries gain their `anthology_key` in this commit. To turn it off, set
`conferences.anthology.enabled: false`. To include co-located workshops, list
their volume prefixes in `conferences.anthology.volumes`.
