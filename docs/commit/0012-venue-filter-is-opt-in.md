# 0012 — The Semantic Scholar venue filter is opt-in

| | |
| --- | --- |
| **Commit** | `fix(collect): stop filtering Semantic Scholar to conference venues by default` |
| **Scope** | `pipelines/collect/conferences.py`, `config/sources.yaml`, `tests/test_collect.py` |
| **Kind** | fix · breaking (behaviour) |

## What changed

The Semantic Scholar bulk query no longer sends a `venue` parameter unless
`semantic_scholar.restrict_to_venues` is set true.

`config/sources.yaml` ships a default venue list, so `venues` is non-empty for
every topic that does not narrow it, so the filter was on for everybody. Semantic
Scholar records a preprint's venue as `arXiv.org`, which is not in anyone's
conference list — so the filter excluded **every preprint, unconditionally**.

## Why it is built this way

Off by default, because the two settings fail in different directions and only
one of them is detectable. With the filter off, the collector returns papers the
group does not want; scoring is the stage that exists to discard those, and it
runs on everything anyway. With the filter on, the collector returns a subset
that looks exactly like a complete answer: source alive, logs clean, no errors,
and a topic whose literature is mostly preprints reports nothing to collect. The
observed symptom is a keyword problem that is not a keyword problem.

A default whose failure mode is noise is recoverable. A default whose failure
mode is silent absence is not, because nothing downstream can tell the
difference between "no preprints matched" and "preprints were never asked for".

The filter is kept rather than deleted: a group that genuinely reads proceedings
versions only has a real use for it, and now has to say so.

This also restores the collector's fallback role. arXiv's own API is unavailable
often enough that this repository already treats it as normal, and Semantic
Scholar is what covers that gap — it cannot, while filtered to exclude
everything arXiv holds.

## Trade-offs and rejected alternatives

**Rejected: add `arXiv.org` to the venue list.** Keeps a filter that is still
wrong for every other preprint server and every venue whose name Semantic
Scholar spells differently from `config/sources.yaml`. The filter's problem is
that it is an allowlist over a field this repository does not control.

**Rejected: filter locally on the returned venue.** Same subset, more requests,
and the same silent-absence failure mode.

**Cost: volume increases sharply, and the queue cap is where that lands.** The
cap (`summarize.max_pending_tasks`, default 40) warns per skipped task rather
than failing, so a run that overflows it logs and moves on — visible in the run
log, easy to miss in a scheduled session. Check the cap before the first run
after this lands, and read the log for `queue is at its cap`.

## What a reviewer should check

That the default really is off and the opt-in really works — the two tests are
`test_the_venue_filter_is_off_by_default` and
`test_the_venue_filter_can_be_opted_into`:

```bash
python3 -m unittest tests.test_collect -v -k venue
```

Note that a pre-existing assertion in `test_semantic_scholar_query_uses_or_syntax`
required the `venue` parameter to be present; it encoded the behaviour this
commit removes and was updated rather than worked around. If it had been left in
place and made to pass, the bug would still be here.

## Downstream impact

**Volume increases sharply.** A deployment that has been running with the filter
will start collecting preprints and should expect the queue to grow — check
`summarize.max_pending_tasks` before pulling this.

A deployment that wants proceedings only sets:

```yaml
conferences:
  semantic_scholar:
    restrict_to_venues: true
```

and is unaffected.

This commit is the other half of [0011](0011-get-json-header-collision.md). Until
that fix landed, this filter had never actually been transmitted — the request
carrying it raised `TypeError` before leaving. Deploying 0011 without this one
turns Semantic Scholar on with the preprint-excluding filter live, which is the
silent failure described above. They belong in the same deployment.
