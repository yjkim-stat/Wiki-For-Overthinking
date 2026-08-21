# 0046 — The PDF cap bounds a run, not a call

| | |
| --- | --- |
| **Commit** | `fix(collect): the per-run PDF cap is per run` |
| **Scope** | `pipelines/collect/pdf_fetch.py`, `pipelines/run_daily.py`, `tests/test_pdf_fetch.py` |
| **Kind** | fix |

## What changed

`collect.pdfs.max_per_run` bounded nothing. `fetch_for` counted downloads in a
local variable and compared it to the cap, and collection calls `fetch_for` with
**one paper at a time** — once per paper, as that paper's task is filed. The
counter therefore started again on every paper, and a run with 500 new papers
would fetch 500 documents under a configured cap of 40.

`pdf_fetch.Budget` now carries the remaining allowance, and `run_daily` builds
one before the collection loop and hands it to every call.

## Why it is built this way

The cap exists because a PDF is the largest thing this pipeline asks a host for,
and the settings comment promises the failure mode it prevents: *"Bounded per
run. A paper that is skipped keeps its abstract-only task and is fetched on a
later run."* Neither half was true. Nothing was skipped and nothing was deferred.

**A budget object rather than restructuring the caller.** The alternative is to
collect every candidate first and call `fetch_for` once with the list, which is
the shape the cap was written for. That would mean separating "file the task"
from "fetch the document", and the two are adjacent on purpose — the task is
filed with the document attached, so a fetch that fails leaves an abstract-only
task in the same pass. Passing the bound in keeps the call site's shape and
makes the bound outlive the call, which is the only thing that was wrong.

**A caller that passes no budget still gets one call's worth.** That is the only
reading under which the old signature was ever correct, so it is what the default
preserves; a caller that means a run now has to say so. The forthcoming backfill
command wants exactly the same object.

**The interval and the give-up circuit were never affected.** `_LAST_REQUEST` and
`_TRIPPED` in `common/http.py` are module-level, so they survive a client being
rebuilt per call. Only the cap was per-call state, which is why this is one
object and not a rework of the client.

## Trade-offs and rejected alternatives

**A mutable object threaded through a call is state, and state is what the rest
of this module avoids.** `fetch_for` is otherwise a function of its arguments.
The justification is that "per run" is inherently a fact about the run and cannot
be recovered from one call's arguments; the alternative that keeps purity is a
module-level counter, which would then need resetting between runs and would make
the tests order-dependent.

**Considered: counting inside `Client`.** The client already holds the throttle
and the give-up circuit, so a request budget would sit naturally beside them. It
is wrong here because the cap counts *stored documents*, not requests — a fetch
that returns a login page costs a request and does not spend the budget.

**A negative cap is clamped to zero rather than read as unlimited.** A bound that
switches off by going below zero is not one anyone can reason about.

## What a reviewer should check

- `test_the_cap_bounds_a_run_called_one_paper_at_a_time` — the production shape.
  The pre-existing `test_the_cap_bounds_a_run` hands over the whole list in one
  call and passes either way, which is how a test named after this exact property
  stayed green while the property was false.
- `test_every_caller_of_fetch_for_passes_a_budget`. It is static, walking
  `pipelines/` with `ast`, because **no test reaches `run_daily.run()` at all** —
  the defect lived in how the function was called, and a test of the function
  cannot see that. Same reasoning as the static half of `tests/test_layering.py`.
  Remove `budget=` from the call in `run_daily` and it fails; that mutation is
  invisible to every other test in the suite.
- That a fetch which fails does not spend the budget: `charge()` is called after
  the bytes are written, not after the request.

## Downstream impact

**A collection run that used to fetch more than its cap now stops at it.** For a
deployment with a large intake this is a behaviour change in the direction the
setting always claimed: papers past the cap keep their abstract-only task and get
their document on a later run. A deployment that was relying on the unbounded
behaviour should raise `collect.pdfs.max_per_run` rather than revert this — the
old behaviour had no bound at all, at any setting.
