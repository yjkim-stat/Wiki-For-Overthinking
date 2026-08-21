# 0011 — `get_json` collided with its own Accept header

| | |
| --- | --- |
| **Commit** | `fix(http): let get_json take caller headers instead of colliding with its own` |
| **Scope** | `pipelines/common/http.py`, `tests/test_http.py`, `tests/test_collect.py` |
| **Kind** | fix |

## What changed

`Client.get_json` and `Client.get_xml` now take `headers` as a named parameter
and merge it, instead of letting it arrive through `**kw`.

`get_json` supplied `Accept: application/json` itself and forwarded `**kw` to
`get`. Any caller passing `headers=` therefore supplied the argument twice and
Python raised `TypeError: Client.get() got multiple values for keyword argument
'headers'` before a request was made. One caller does this — the Semantic
Scholar collector, which passes a header dict for its optional API key — and it
passes that dict whether or not a key is set. **That code path had never
executed a single request.**

## Why it is built this way

The method owns one header and the caller may own others; merging is the only
arrangement where both are true. Named-and-merged also makes the contract
visible in the signature, where `**kw` hid it: the previous version type-checked
fine and read fine, and was impossible to call correctly.

`get_xml` did not have the bug — it passes nothing of its own — but it now takes
the same explicit parameter. Two sibling methods that differ in whether a
keyword argument is legal is the kind of asymmetry that gets rediscovered by
whoever needs an auth header on an XML feed next.

The caller wins on conflict. A caller that deliberately asks for `Accept:
text/plain` from `get_json` has said something more specific than the default,
and a default that cannot be overridden is not a default.

**The stubs were the real defect.** `StubClient` in `tests/test_collect.py`
declared `get_json(self, url, params=None, **kw)` — looser than the class it
stands in for, so it accepted a call the real client rejected. Every test passed
against a stub that could not reproduce the bug. Both stubs (`test_collect.py`
and `test_virtual_site.py`) now mirror the real signatures exactly, and
`tests/test_http.py` exercises the real `Client` directly. A stub more permissive
than the thing it replaces does not test that thing; it tests itself.

## Trade-offs and rejected alternatives

**Rejected: drop the Accept header and let callers set it.** Fixes the collision
by removing the feature. Every JSON caller would then repeat the header, and
forgetting it is a silent content-negotiation bug rather than a loud `TypeError`.

**Rejected: `**kw`-only, popping `headers` inside.** Same behaviour, contract
still invisible in the signature. The point is to make the parameter legible.

**Cost: nothing prevents the next stub from drifting.** Mirroring is a
convention held by review, not by the type system. A shared fake built from the
real signature would enforce it; that is a larger refactor than this fix wants
to carry, and is worth doing when a third stub appears.

## What a reviewer should check

The collision is gone at the level it was reported:

```bash
python3 -c "from pipelines.common.http import Client; Client().get_json('https://example.org', {}, headers={})"
```

This should now fail with a network error rather than `TypeError` — reaching the
network is the pass condition.

Then check that the stubs really do match: compare `StubClient.get_json` against
`Client.get_json`, and confirm `test_an_api_key_reaches_the_request` fails if the
merge is removed.

## Downstream impact

**This turns Semantic Scholar on for the first time, which makes [0012](0012-venue-filter-is-opt-in.md)
load-bearing.** The venue filter that 0012 removes has never actually been sent,
because the request it belonged to never left. Landing this commit *without*
0012 replaces "the collector is broken and says so" with "the collector works
and silently returns no preprints" — a worse failure, because it is quiet. The
two belong in the same deployment.

Deployments that concluded Semantic Scholar was unreliable should expect it to
start returning results, and should re-check any topic they had assumed was
genuinely quiet.
