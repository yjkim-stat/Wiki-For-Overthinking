# 0003 — Field-neutral fixtures and examples

| | |
| --- | --- |
| **Commit** | `test: make fixtures and examples field-neutral` |
| **Scope** | `tests/`, `pipelines/enrich/score.py` (docstring) |
| **Kind** | refactor |

## What changed

Every test fixture used the vocabulary of the repository's original subject —
recorded arXiv payloads, sandbox topic keywords, the wiki concept slug, the
seminar channel name, the arXiv category asserted in the query. They now use one
running example carried consistently across all seven test modules, and the
`score.py` docstring uses the same example as the test that pins the behaviour
it describes.

The 124 tests assert exactly what they asserted before. This commit changes no
behaviour.

## Why it is built this way

**A test is read by someone who does not know the field.** A fixture titled with
one discipline's jargon makes a reader wonder whether the term matters to the
assertion. Neutral fixtures make it obvious that it does not — the scoring tests
are about word boundaries and weights, not about any subject.

**The docstring example and the test example must be the same example.** The
word-boundary rule in `score.py` is illustrated by a case (`"ATE"` must not
match inside `"Water"`) that `test_word_boundaries_prevent_substring_matches`
pins. When the two drift, the docstring becomes a claim nobody verifies. They
change together, so they belong in one commit.

**Semantics were preserved, not just strings.** The substring case needed a
short acronym that genuinely occurs inside a longer unrelated word; the
title-normalization case needed a hyphen and a colon; the `keywords.all` case
needed a term absent from the title under test. Each replacement was chosen to
exercise the same edge, not merely to read differently.

## Trade-offs and rejected alternatives

- *Leaving the fixtures alone as harmless.* Rejected: fixtures are the most-read
  examples in the repository after the README, and 0002 would be half-done
  without them.
- *Fully abstract fixtures (`"term one"`, `"paper A"`).* Rejected: recorded
  payloads should look like real payloads, or the mappers stop being tested
  against realistic shapes — a title with a colon, a wrapped element, a trailing
  period that DBLP adds and the mapper must strip.

## What a reviewer should check

- `git show --stat` should show tests only, plus one docstring. Any source
  change here is a mistake.
- Run count: 124 passing, the same as before this commit. A drop means a test
  was renamed into invisibility or an import broke.
- `tests/test_score.py::test_word_boundaries_prevent_substring_matches` — the
  new example must still fail to match for the intended reason. A replacement
  that passes because the term is simply absent would silently retire the test.

## Downstream impact

None. Nothing outside `tests/` changed behaviour.
