# 0017 — `get_json` was refusing every caller that sent a header

| | |
| --- | --- |
| **Commit** | `fix(http): merge caller headers into get_json instead of colliding` |
| **Scope** | `pipelines/common/http.py`, `tests/test_http.py` |
| **Kind** | fix |

## What changed

`Client.get_json` hardcoded `Accept: application/json` and forwarded everything
else through `**kw`:

```python
def get_json(self, url, params=None, **kw):
    raw = self.get(url, params, headers={"Accept": "application/json"}, **kw)
```

A caller passing `headers=` therefore supplied the argument twice, and Python
raised `TypeError: get() got multiple values for keyword argument 'headers'`.
`headers` is now an explicit parameter and the default is merged under it.

Six tests in a new `tests/test_http.py` cover the merge, the override, the
untouched default, and that the caller's dict is not mutated.

## Why this mattered more than it looks

**Exactly one collector sends a header, and it is Semantic Scholar.** It sets
`x-api-key` — unconditionally, since the dict is built whether or not a key is
configured. So the call raised on every run, for every topic, for as long as
this code has existed. The collector has never worked in this deployment.

The failure was invisible in the ordinary way. `conferences.py` catches
`HTTPError` around that call; `TypeError` is not one, so it escaped to the
run-level handler, which appends the message to the run's `errors` list and
carries on. The pipeline is deliberately fail-soft, and a source that is
unreachable is not a failed run — that design turned a code defect into a line
in a list nobody had reason to read.

**It also invalidated the reasoning in note 0016.** That note disabled the
OpenReview collector on the grounds that "Semantic Scholar indexes the same
venues, so the cost is earliness rather than coverage." That was true of the
design and false of the running system: at the moment OpenReview was switched
off, the collector meant to cover for it was throwing on every call. Both are
now true at once — the fix restores the assumption 0016 relied on. Anyone
reading these notes in order should read them as a pair.

## Why the tests did not catch it

`tests/test_collect.py` stubs the client with a fake whose `get_json(self, url,
params=None, **kw)` absorbs anything. A fake that is more permissive than the
real class cannot detect a signature the real class rejects, so the collector
tests passed against a client that could not be called.

The new tests exercise the real `Client`, replacing only its transport. That is
the level at which this class of bug is visible.

## Trade-offs and rejected alternatives

- *Dropping the `Accept` default and making every caller set it.* Rejected:
  the default is right for a JSON helper, and pushing it to call sites invites
  a different omission.
- *Letting the caller's headers lose to the default.* Rejected: a caller that
  bothers to set `Accept` means it.
- *Tightening the fake in `test_collect.py` to mirror the real signature.*
  Worth doing and not sufficient — it would catch a mismatch only where a test
  happens to pass the argument. Testing the real class covers it directly.
- *Raising `TypeError` to a run-stopping error.* Rejected here as a separate
  question, but a real one: the fail-soft handler currently cannot distinguish
  "the network is down" from "this code cannot run", and only the first should
  be survivable. Left for its own commit.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 173 tests, six new.
- That the collector now returns results rather than an error. With network
  access, collecting conferences for one topic over three days returned 60
  papers and an empty error list, where the same call previously returned the
  `TypeError` message for every topic.
- The mutation test: `get_json` must not modify the dict it is handed, since
  `conferences.py` builds one per call and a future caller may not.

## Downstream impact

**Any deployment that configured `SEMANTIC_SCHOLAR_API_KEY` has been collecting
nothing from Semantic Scholar.** After this fix the venue coverage that
`config/sources.yaml` promises actually arrives, so the next run will collect
substantially more than the previous ones — expect a larger queue than usual on
the first firing, and note that `summarize.max_pending_tasks` will cap it.

No stored record changes. Papers that were missed are not retroactively
collected; widen `--days` once if backfilling matters.
