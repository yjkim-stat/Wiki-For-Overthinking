# 0041 — ACL is reached through DBLP, or not at all

| | |
| --- | --- |
| **Commit** | `config(sources): track ACL` |
| **Scope** | `config/sources.yaml`; `docs/commit-local/0041-acl-is-reached-through-dblp-or-not-at-all.md` |
| **Kind** | config · editorial |

## What changed

`ACL` joins `NeurIPS`, `ICLR`, `ICML`, `AISTATS` and `JMLR` in
`conferences.venues`. It carries `dblp_key: "ACL"`, an empty
`openreview_prefix` and no `virtual_host`.

The venue was already present in the file, commented out, as one of three
examples of a narrower track. This uncomments it and nothing else.

## Why it is built this way

**The archive's owner named the four venues its group reads and ACL was the
one not being collected.** That is an editorial decision, recorded here rather
than inferred: the topic is a language-model subject and a third of the
relevant work is published at *ACL, but the venue list this deployment
inherited from the template was the template's generic starting point.

**ACL reaches this archive by a different route from the other three, and the
route is the weakest one available.** NeurIPS, ICLR and ICML each have a
`confs.cc` programme page, which is authoritative on what was accepted and
carries a title per paper plus an abstract on request. ACL has neither that
nor an OpenReview instance, so it arrives through DBLP and Semantic Scholar
only. Both keys are therefore left blank rather than guessed — a `virtual_host`
that does not answer costs a request and its retries every run and puts a line
in every digest's run problems, which is how a genuinely new failure gets lost
among standing ones. That is the lesson of [0035](0035-a-source-that-answers-403-to-everything.md).

**The abstract lookup matters more for ACL than for any other venue here.**
DBLP is bibliographic and carries no abstract, so a paper only it knows about
is scored on its title alone — and scoring weights a title hit at 3.0 against
an abstract hit at 1.0, so such a paper is judged on strictly less evidence
than the same paper from anywhere else. `conferences.abstracts` already points
at `https://aclanthology.org` and fills that gap after collection but before
scoring. The comment added above the entry says so, because the next person to
consider turning `abstracts` off needs to know ACL is the venue that depends
on it.

## Trade-offs and rejected alternatives

**Rejected: adding EMNLP and NAACL at the same time.** They are the obvious
neighbours and the argument for them is the same one, but what a group tracks
is its own editorial decision and only ACL was asked for. Adding the other two
is one line each when it is asked for.

**Not resolved: DBLP was unreachable during the run that preceded this
change.** `dblp.org` returned 503, then 429, then closed the connection on
four consecutive requests and was skipped for the rest of the run by
`give_up_after_failures`. That is ACL's primary path. It may well have been a
bad few minutes, but until a run gets through, this entry is untested against
the index it depends on. Semantic Scholar covers ACL too and was reachable, so
the venue is not blind in the meantime.

**Accepted cost: more requests per run.** Every venue is another query per
topic per run against each enabled index.

## What a reviewer should check

- `python3 -c "from pipelines.common import config; print([v['name'] for v in config.load().sources['conferences']['venues']])"` — the list reads `NeurIPS, ICLR, ICML, ACL, AISTATS, JMLR`.
- The next `run_daily` log: a `dblp` line for ACL that is not a failure, and
  whether `pipelines.local.abstracts` fills in the abstracts DBLP omits.
- Nothing else in `config/sources.yaml` moved. The three commented example
  venues below `JMLR` are unchanged; only ACL was promoted out of them.

## Downstream impact

None for the code. For this deployment, the next collection run queries one
more venue, and ACL papers that clear scoring will begin arriving with
`venue: ACL`. Nothing already in `data/` is revisited — `seen.sqlite` has not
been touched, so an ACL paper already held under its arXiv id stays as it is.
