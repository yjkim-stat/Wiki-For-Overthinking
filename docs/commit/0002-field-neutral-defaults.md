# 0002 — Retire the subject-specific defaults and identifiers

| | |
| --- | --- |
| **Commit** | `refactor: retire the subject-specific defaults and identifiers` |
| **Scope** | `config/`, `pipelines/common/http.py`, `pipelines/common/llm.py`, `scripts/new_topic.sh` |
| **Kind** | refactor · **breaking default** |

## What changed

The repository was built to track one subject, and the defaults still carried it
even though nothing in the code did:

- **arXiv categories** — `cs.RO, cs.LG, cs.CV, cs.AI, cs.CL` → `cs.LG, cs.AI,
  stat.ML, stat.ME`, with a comment naming other fields' categories.
- **Venue list** — the robotics and vision track (CoRL, RSS, ICRA, CVPR, ICCV,
  ECCV) and ACL are gone from the defaults; NeurIPS, ICLR, ICML, AISTATS and
  JMLR remain, and narrower tracks stay in the file as commented examples,
  including one journal entry showing that a venue only Semantic Scholar knows
  about still works with both index keys blank.
- **User-Agent** — `recipe-for-world-action-model/0.1` →
  `recipe-for-research-team-management/0.1`, in `config/settings.yaml` and as
  the fallback in `http.py`.
- **Topic template** — the `keywords.all` illustration and the arXiv category
  example no longer come from one field; the `description` comment now says what
  makes a description useful to the summarizer.
- **`new_topic.sh` usage examples** and the summary schema's `datasets` hint,
  which said "simulators" where most fields would say "corpora".

## Why it is built this way

**Defaults are what people run, not what they read.** Documenting a
field-specific default as "just an example" does not stop it from deciding what
a deployment collects on day one. The only way for the defaults to be neutral is
for them to be neutral.

**A source list is an editorial claim.** Shipping CoRL and ICRA as defaults
tells a new user that this is a robotics tool, regardless of what the README
says. The replacement list is not neutral in some absolute sense — no list is —
but it is broad enough that no discipline reads it as *theirs*, and the file now
opens by saying it is a starting point to be replaced.

**Commented-out examples beat a longer default.** The narrower venues stay in
the file because the shape of a venue entry is not obvious — `dblp_key`,
`openreview_prefix`, and what to do when neither exists. Keeping them commented
teaches the format without costing a request per run.

**The User-Agent is how arXiv and DBLP identify us.** Both throttle anonymous
clients hard, so the string has to be real; it should also not name a project
the deployment has nothing to do with.

## Trade-offs and rejected alternatives

- *Leaving the defaults and documenting them.* Rejected above.
- *Shipping an empty category and venue list.* Rejected: a first run that
  collects nothing looks broken, and the most common support question would
  become "why did nothing happen".
- *Keeping every venue and letting topics narrow.* Rejected: every extra venue
  is another request per run against three third-party indexes, and a default
  that is expensive for everybody to serve nobody in particular.

## What a reviewer should check

- `config/sources.yaml` loads: `python3 -m unittest discover -s tests -t .`
  includes `RealConfigTests`, which parses the shipped config as-is.
- The commented journal entry is a genuine example — a venue with both
  `dblp_key` and `openreview_prefix` blank must still be queried by Semantic
  Scholar. Confirm `_venues_for()` does not skip it.
- No remaining references to the old subject: `grep -rniE "world.action|robot|cs\.RO"`.

## Downstream impact

**This changes what an existing deployment collects.** A project that took the
defaults and never edited `config/sources.yaml` will stop seeing cs.RO, cs.CV
and cs.CL submissions and the six removed venues. Anyone relying on those should
copy them back from the commented block in this commit — the alternative,
noticing months later that a venue quietly stopped appearing, is exactly the
failure mode the collectors' fail-soft behaviour makes hard to spot.

Already-archived material is unaffected: `data/` is not touched, and nothing is
re-collected or removed.
