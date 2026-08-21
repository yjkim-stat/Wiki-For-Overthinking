# 0101 — DBLP is off by default

| | |
| --- | --- |
| **Commit** | `config: turn off the DBLP collector by default` |
| **Scope** | `config/sources.yaml` |
| **Kind** | config · breaking (behavioural, for deployments that relied on it) |

## What changed

`conferences.dblp.enabled` becomes `false` in the shipped configuration. The
collector, its parser and the per-venue `dblp_key` entries are all unchanged and
still work; only the default answer to "should this run" has moved.

## Why it is built this way

**The tail is not worth the default.** Semantic Scholar and the venues' own
programme pages already cover the tracked venues, and the programme pages are
authoritative on what was accepted. DBLP earns its place on the cases those two
miss, which is a real but narrow set — a good reason to switch it on for a
field whose proceedings the others index poorly, and a poor reason to spend
every run's retry budget by default.

**The stated reason is the one that will still be true next month.** DBLP was
measured unresponsive during a run on 2026-08-21 — TLS completing, no body, the
30 second timeout burned on every query until the circuit breaker tripped five
failures later, about two minutes of a four-and-a-half minute run. It was
responding normally within the hour, including the exact venue-scoped queries
that had failed, under three different user agents. **So the outage is not the
reason recorded in the config**, and deliberately so: a comment blaming a host's
availability is a comment that is false most of the time it is read, and
somebody will later cite it as evidence about DBLP that it does not support.

**Off, not deleted.** A source that a deployment might legitimately want is a
configuration decision, not a code one. Removing `_collect_dblp` and `_from_dblp`
would make restoring it a revert rather than a one-line edit, and the mapping
tests that cover the parser would have to go with it.

**This is a change to the shipped default, so it is a framework note.** The
OpenReview equivalent — note 0016 in the local series — was recorded as a
deployment delta because the reasoning was about one archive. This one moves what
every downstream clone gets.

## Trade-offs and rejected alternatives

- *Leave it on and shorten the timeout instead.* Rejected as a fix for the wrong
  problem: a shorter timeout would have reduced the cost of one outage and
  changed nothing about whether the source is worth a default.
- *Leave it on and let the circuit breaker handle outages.* This is what already
  happens, and it works — the breaker did trip. It bounds the cost; it does not
  answer whether to pay it.
- *Delete the collector.* Rejected above.
- **Cost, stated plainly:** a deployment that pulls this update silently stops
  querying DBLP. Venues indexed by DBLP and missed by both Semantic Scholar and
  the programme pages will stop appearing. That is a real loss of recall for
  anyone who was relying on it, which is why it is in the Kind row as breaking
  and named in Downstream impact.

## What a reviewer should check

That nothing but the default moved:

```bash
git show --stat HEAD           # config/sources.yaml only
python3 -m unittest discover -s tests -t .
```

The suite is 858 tests and passes unchanged — the DBLP tests cover the parser
and the record mapping, neither of which is reached through the enabled flag.

## Downstream impact

**A deployment that wants DBLP must re-enable it after pulling.** In
`config/sources.yaml`:

```yaml
  dblp:
    enabled: true
```

Nothing else changes: the `dblp_key` entries under each venue are still there
and still correct.
