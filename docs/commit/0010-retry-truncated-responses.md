# 0010 — A truncated response is transient, so retry it

| | |
| --- | --- |
| **Commit** | `fix(http): retry a response that ends early instead of letting it escape` |
| **Scope** | `pipelines/common/http.py`, `tests/test_http.py` |
| **Kind** | fix |

## What changed

`Client.get` now retries `http.client.HTTPException` alongside the network
errors it already handled. The case that prompted this is `IncompleteRead`,
raised when a chunked response ends early — observed against DBLP under load.

Before: the exception escaped `Client.get` uncaught, `conferences.collect`
caught it at the outer level, and every remaining query for that topic and that
index was skipped. A transient truncation cost a topic its results for the run.

## Why it is built this way

The retry loop already existed and already had the right policy. The bug was
purely a class-hierarchy detail: `urllib.error.URLError` descends from
`OSError`, so the existing arms caught connection failures and timeouts, but
`IncompleteRead` descends from `HTTPException`, which descends straight from
`Exception`. A condition the loop was designed for was falling through it
because of where it sits in the tree.

The fix catches the whole `HTTPException` family rather than `IncompleteRead`
alone. Everything under it — `BadStatusLine`, `LineTooLong`, a malformed
chunked encoding — is the same kind of event: the transport misbehaved, and the
next attempt may well succeed. Enumerating one subclass would leave the next
sibling to be discovered the same way this one was.

The attempt bound is untouched, and that is the property worth protecting: a
host that truncates every single time still raises `HTTPError` after `retries`
attempts. Widening what counts as retryable must not widen how long a dead host
can hold the run.

## Trade-offs and rejected alternatives

**Rejected: catch `Exception` in the retry arm.** It would have covered this and
everything else, including the bugs in this repository — note 0011 is a
`TypeError` that a broad arm here would have converted into three silent
retries and an `HTTPError` that reads like an outage. Retrying a defect is
worse than crashing on one.

**Cost: a genuinely dead host now costs more wall clock.** A host that truncates
consistently is retried where it used to fail on the first attempt. Bounded by
`retries` and `retry_backoff_s`, so the worst case is a few seconds per query,
not an unbounded wait.

## What a reviewer should check

That the bound really holds — `test_a_permanently_truncating_host_gives_up`
asserts exactly `retries` attempts, and it is the test that would catch a fix
that traded a lost topic for a hung run:

```bash
python3 -m unittest tests.test_http -v
```

Also worth checking that `urllib.error.HTTPError` is still caught by the arm
above this one, so a 404 continues to fail fast rather than being retried three
times.

## Downstream impact

None for configuration. Runs that were losing a topic's DBLP results to a
truncated response will now retry and usually complete.
