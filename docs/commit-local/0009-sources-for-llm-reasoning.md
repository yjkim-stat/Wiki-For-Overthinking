# 0009 — Point the source lists at the LLM reasoning literature

| | |
| --- | --- |
| **Commit** | `config: point the source lists at the LLM reasoning literature` |
| **Scope** | `config/sources.yaml` |
| **Kind** | config · **breaking default** |

## What changed

This deployment tracks reasoning in large language models. The template's
field-neutral defaults, correct as defaults, collect from the wrong indexes for
that subject.

- **arXiv categories** — `cs.LG, cs.AI, stat.ML, stat.ME` → `cs.CL, cs.LG,
  cs.AI, stat.ML`. `cs.CL` is added and listed first; `stat.ME` is dropped.
- **Venues** — added ACL, EMNLP, NAACL and COLM; removed AISTATS and JMLR.
  NeurIPS, ICLR and ICML are unchanged. COLM carries an
  `openreview_prefix` and a blank `dblp_key`.

## Why it is built this way

**`cs.CL` is the single most consequential line in this file.** A topic can only
ever match what is collected, and nearly all LLM reasoning work is submitted to
`cs.CL`. Without it, four well-written topic files would collect almost nothing
and the failure would look like bad keywords rather than a missing category —
the most expensive kind of misconfiguration to diagnose, because everything
downstream is working correctly.

**The NLP venues are half the literature.** Reasoning work splits roughly evenly
between the ML conferences and the ACL family. Tracking one half would produce
an archive that silently misrepresents the field's centre of gravity.

**COLM is OpenReview-only on purpose.** DBLP indexes it late enough that a
`dblp_key` would return nothing for the current cycle while still costing a
request per run. OpenReview plus Semantic Scholar covers it, which is exactly
the case the template's commented journal entry documents.

**`stat.ME`, AISTATS and JMLR are removed rather than left in.** They are not
where this group's literature appears, and every extra category widens the
arXiv query while every extra venue is another request against three
third-party indexes. A source list is an editorial claim; leaving entries in
"just in case" makes the claim vaguer without making the archive better.

## Trade-offs and rejected alternatives

- *Leaving the global lists alone and narrowing per topic.* Rejected: a topic
  can narrow the global list but never widen it, so `cs.CL` had to be added
  globally regardless. Once it is there, the rest of the list may as well be
  honest about what this deployment reads.
- *Adding cs.CV, cs.SE and cs.MA for multimodal, code and agent reasoning.*
  Rejected for now: each widens every query for all four topics, and none is
  where the group currently reads. Revisit when a topic demands it.
- *Keeping AISTATS and JMLR for the statistics side of the group.* Rejected:
  reasoning papers do not appear there. If the group later tracks a statistics
  topic, that topic can bring its own venues back.

## What a reviewer should check

- The config parses: `python3 -m unittest discover -s tests -t .` includes
  `RealConfigTests`, which loads the shipped config as-is. 149 tests pass.
- `python3 -m pipelines.run_daily --dry-run` builds well-formed arXiv queries.
  Note that at the time of writing this machine cannot reach arXiv (immediate
  `429`) or DBLP (connection timeout), so a dry run reports zero collected and
  the URLs in the log are the thing to inspect.

## Downstream impact

Changes what is collected from the first run onward. Nothing already in `data/`
is affected — no re-collection, no removal. A deployment that wants the template
defaults back should take them from this commit's parent.
