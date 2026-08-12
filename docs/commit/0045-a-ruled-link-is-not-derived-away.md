# 0045 — A ruled link is not derived away

| | |
| --- | --- |
| **Commit** | `feat(enrich): a ruled link is not derived away` |
| **Scope** | `pipelines/common/schema.py`, `pipelines/common/llm.py`, `pipelines/enrich/apply.py`, `pipelines/enrich/concepts.py`, `pipelines/publish/wiki.py`, `tests/test_related_links.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | feature |

## What changed

A definition task has always asked the reader for `related`. The validator
accepted it, `apply` wrote it, and `harvest` — later in the same
`pipelines.render` invocation — rebuilt the record without it. Every step
reported success and nothing said the field had been dropped.

`Concept` now has two link fields. `related` is derived from names appearing
together in one summary and is still rebuilt from nothing on every harvest.
`related_authored` holds what a definition task ruled and is carried across a
rebuild the way `definition` and `aliases` are. `Concept.neighbours` unions
them, and both readers in `publish/wiki.py` — the note's **Related** line and
the edges of `wiki/graph.html` — go through it.

This is option C of
[the issue](../solved/related-links-are-asked-for-and-discarded.md), which is
where the reasoning, the rejected options and the observable reproduction live.

## Why it is built this way

**Two fields, because the two kinds of link need opposite lifetimes.** A derived
edge has to disappear when the paper that made it is re-read — that is the
phantom-mention property `enrich/concepts.py` exists to hold. A ruled link has
to survive exactly that, because nothing in the summaries can produce it again.
Merging them into one list, which is the one-line version of this change, buys a
truthful schema at the price of edges nothing can ever remove: the same failure,
moved from evidence to edges.

**The union happens at read time, not write time.** Writing the union into
`related` would make the fields agree on disk and then lose the distinction on
the next harvest. `neighbours` is a property on the record, next to
`mention_count`, so the two renderers cannot drift apart and neither has to know
which list a slug came from.

**It follows the ruling pattern from [note 0015](0015-a-ruled-kind-defends-itself.md)**
rather than inventing a second one. `kind` had the same shape — a derived field a
definition task was also allowed to rule on, where the next harvest overwrote the
ruling — and was solved by letting the authored judgement defend itself while the
derived data stayed disposable. The difference is that `kind` is a single value
that can be replaced, and links are a set, which is why this needs a field rather
than a guard.

**Answering replaces; omitting does not.** `related: []` retracts the whole list
and a result without the key leaves it alone. Accumulation would mean an
authored link could never be taken back except by hand-editing `data/`, which is
what the queue exists to prevent. The two cases are distinguished by key
presence, not by falsiness, so the retraction is expressible.

**The prompt now says what the field is for.** The old text — "names of
neighbouring entities worth linking" — invited exactly the answer the wiki
already derives. It now says the wiki links co-occurring names by itself, and
asks for the neighbour it cannot see: the previous generation, the benchmark a
method was built to beat.

## Trade-offs and rejected alternatives

**Option A — stop asking — was rejected, having been the issue's own first
recommendation.** It is the smaller and more conservative change and it makes
the code honest immediately. The group wanted curated links, and the case that
found the defect is the argument: `Cosmos 3` was answered with seven curated
neighbours, six of them its own sibling generations, and none survived. What the
note links to instead is `Epic-Kitchens` and `Kinetics`, and it can never link to
`cosmos-predict1`, because no single summary lists two Cosmos generations.

**Option B — carry `related` itself across — is the trap.** One line, immediately
truthful, and it makes every co-occurrence edge permanent. Rejected outright.

**`SCHEMA_VERSION` was not bumped.** Nothing in `pipelines/` reads it, and
`_Record.from_dict` defaults a missing key, so an existing record loads with an
empty list. Bumping it would be a version nobody compares against.

**A note can now claim a neighbour that no evidence supports.** That is the
feature, and the cost is that a wrong ruling is as durable as a right one. The
retraction path is the mitigation, and it is the same one the definition has.

**Nothing reconciles the two lists.** A ruling that repeats what co-occurrence
already found is stored twice and rendered once. Harmless, and de-duplicating on
write would mean an authored link silently vanishing the day its derived twin
disappears.

## What a reviewer should check

- **That the derived side is still disposable.** `DerivedLinksStayDisposableTests`
  re-reads both summaries so two entities stop co-occurring, and asserts the edge
  is gone while the ruling is not. Nothing guarded this before; it is the property
  option B would have broken.
- **That the renderer tests bite.** They did not at first. Asserting on a
  neighbour that also co-occurs passes whether or not the renderer reads the
  authored list — the fixture carries a fourth entity nothing names alongside the
  others precisely so the union can be told from the derived list. Revert either
  `publish/wiki.py` call site to `concept.related` and exactly one test should
  fail each time.
- **That a render is still not an edit.**
  `test_a_render_over_an_unchanged_archive_still_changes_no_record` hashes every
  concept file across two renders. `_same` compares whole records, so a new field
  is exactly the kind of thing that starts rewriting all of them.
- **That `enrich/concepts.py`'s docstring is true.** It named the links as
  derived, full stop, which this change made false; it was rewritten here. If the
  code and that paragraph ever disagree, one of them is a bug.

## Downstream impact

**Adding the field is safe.** Existing concept records load with
`related_authored: []` and nothing regenerates differently until somebody rules
on a link.

**Existing archives lost their earlier answers and cannot get them back.** Links
written by a definition task before this change were discarded at the next
harvest and are not recoverable from `data/` — the answers survive in
`data/queue/archive/`, where the completed task keeps its `result`. A deployment
that wants them can re-answer the definition task, which is the same route as any
correction: clear `definition` in `data/concepts/<slug>.json` and render.

**`docs/issues/` and `docs/solved/` are introduced here**, with the lifecycle
stated in `docs/issues/README.md`. Neither was tracked before.
