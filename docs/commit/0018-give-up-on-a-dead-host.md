# 0018 — Stop asking a host that has failed all run

| | |
| --- | --- |
| **Commit** | `feat(http): give up on a host that fails every request in a run` |
| **Scope** | `pipelines/common/http.py`, `config/settings.yaml`, `tests/test_http.py` |
| **Kind** | feature |

## What changed

A per-host circuit breaker, process-wide. After
`collect.give_up_after_failures` consecutive whole-request failures (default 5),
the client stops attempting that host and raises `HostUnavailable` immediately.
A success clears the count. `0` disables it.

Retries were correctly scoped to a single request. But a run makes hundreds of
requests, and when a host is down for the *whole* run, per-request retry turns
one dead source into the run's dominant cost and still returns nothing — a
measured collection spent the large majority of 56 minutes retrying hosts that
returned nothing at all.

## Why it is built this way

**`HostUnavailable` subclasses `HTTPError`.** Every collector already wraps its
lookups in `except HTTPError` and treats it as "this source gave me nothing",
which is exactly what happened. Giving up therefore needs no new handling
anywhere — no collector changed in this commit, and a collector written later
gets the behaviour for free. A new exception type off `Exception` would have
meant editing four collectors and getting one of them wrong.

**Hard 4xx counts toward the breaker.** This is the non-obvious part and it is
deliberate. A 4xx will not fix itself inside a run, so it is a *stronger* signal
than a timeout, not a weaker one — OpenReview answering 403 to every venue
lookup from a blocked egress is precisely the case worth stopping. The existing
fast-fail on 4xx handles one request; the breaker handles the other three
hundred.

**Consecutive, not cumulative.** A host that blips once an hour never trips. The
counter resets on any success, so tripping requires sustained failure — and each
of those failures is already `retries` attempts with backoff, so the default of
5 means roughly fifteen attempts before the host is dropped.

**Module-level state, alongside `_LAST_REQUEST`.** The throttle already keeps
per-host state at module scope for the same reason: collectors build their own
clients, so per-instance state would forget everything between sources.
`reset_circuit_breakers()` exists for tests and for any long-lived process.

## Trade-offs and rejected alternatives

**Rejected: time-based half-open retry.** The standard circuit breaker reopens
after a cooldown. A collection run is short and single-pass; a host that has
failed fifteen attempts will not recover inside it, and the cooldown machinery
would add state for a case that does not arise. Process-lifetime is the right
granularity here.

**Cost: a host that is merely slow for a long stretch can be dropped for the
rest of the run.** The threshold is on consecutive whole-request failures, each
already several retries, so this needs sustained failure rather than a bad
minute — but it is a real behaviour change, and the tripping warning is the only
notice.

**Cost: state is process-wide, so one collector's bad luck can silence a host
for another.** That is the intent — the host is the shared resource — but it
does mean a test that trips the breaker must reset it, which is why the helper
is public.

## What a reviewer should check

The two properties that matter are that it trips and that it *doesn't*:

```bash
python3 -m unittest tests.test_http -v -k Circuit
```

`test_a_success_resets_the_counter` alternates failure and success five times
and must never trip — that is the test protecting every flaky-but-alive source.
`test_the_breaker_stops_calling_after_the_threshold` asserts the call count does
not move after tripping, which is the whole point; asserting only the exception
would pass even if the request were still being made.

Seen against a genuinely blocked host:

```
request 1-5: attempted, failed
icml.cc has failed 5 consecutive requests; skipping it for the rest of this run
request 6+: short-circuited
```

## Downstream impact

Runs get shorter when a source is down and are otherwise unchanged. A deployment
that wants the old behaviour sets:

```yaml
collect:
  give_up_after_failures: 0
```

This is the other half of [0010](0010-retry-truncated-responses.md), which made
the client retry more. That change alone makes a dead host slower; this one is
what pays for it.
