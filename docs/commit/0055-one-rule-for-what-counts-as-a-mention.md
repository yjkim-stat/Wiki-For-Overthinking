# 0055 — One rule for what counts as a mention

| | |
| --- | --- |
| **Commit** | `refactor(common): move term matching out of scoring` |
| **Scope** | `pipelines/common/text.py`, `pipelines/enrich/score.py`, `tests/test_score.py` |
| **Kind** | refactor |

## What changed

`_plural_tail`, `_pattern` and `_find` move from `enrich/score.py` to
`common/text.py` as `matcher` and `contains`. No behaviour changes and no
caller's result moves; the suite is identical before and after.

## Why it is built this way

Topic scoring asks "does this paper mention *causal inference*". A search over
the archive — the next commit — asks exactly that question, of the same corpus.
Two implementations would disagree eventually, and the disagreement would be
invisible: a paper found by one and not the other, with nothing to say which was
right and no test that could fail.

The rule itself is unusually opinionated for something this small — word
boundaries so "ATE" does not match inside "Water", hyphen and whitespace
tolerance so a line-wrapped abstract still matches, and only the head word
inflected so "latent action model" matches its plural but not "latent actions
model". Those are decisions, and a second copy of them would be a second set.

This is the same move `common/html.py` records in
[note 0023](0023-shared-html-reading.md): two collectors were asking a page for
the same three things, so the asking moved to one place.

## Trade-offs and rejected alternatives

**Considered: importing the private names from `score.py`.** Zero risk and it
would have worked. It leaves the matching rule owned by a module about
*relevance thresholds*, which is not what a search needs from it, and the next
reader has to work out whether the underscore means "do not use this" or "nobody
had a reason to yet".

**The regex cache moved with it**, so it is now shared across scoring and
search. That is correct — the same term compiled twice is the thing the cache
exists to avoid — and it means the cache is process-wide rather than per
concern, which it already was.

`score.py` keeps the names `_find` and `_pattern` as import aliases rather than
renaming forty call sites in a refactor that is supposed to change nothing.

## What a reviewer should check

- That nothing else changed: the diff to `score.py` is an import block and a
  deletion, and the suite reports the same 533 tests passing.
- `tests/test_score.py` still exercises the matcher directly, now through its
  public name. Those cases are the specification of the rule and should stay
  where somebody looking for "how does matching work" will find them.

## Downstream impact

None. `pipelines.enrich.score` exposes the same functions and computes the same
scores; a deployment sees no difference in any record.
