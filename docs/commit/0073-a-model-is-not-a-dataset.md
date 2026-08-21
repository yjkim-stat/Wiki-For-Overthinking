# 0073 — A model is not a dataset: the wiki gains a fourth entity kind

| | |
| --- | --- |
| **Commit** | `feat(wiki): a model is not a dataset` |
| **Scope** | `pipelines/common/paths.py`, `common/schema.py`, `common/llm.py`, `enrich/concepts.py`, `enrich/queue.py`, `enrich/apply.py`, `publish/graph_page.py`, `tests/test_model_kind.py`, `an earlier note: ` |
| **Kind** | feature · breaking |

## What changed

`WIKI_KINDS` is now `("concept", "method", "dataset", "model")`. A reading can
name the models a paper trains, evaluates or analyses, and those become wiki
entities of kind `model` with their own notes directory, rather than being
pushed into `datasets` alongside the corpora they were evaluated on.

The kind is a single source of truth in `common/paths.py`; the harvest, the
validator, the applier, the reader's output contract and the graph page all read
it from there.

The `model` kind is the largest single departure from treating every wiki
entity the same way, which is why it is argued for here rather than folded into
a smaller change.

## Why it is built this way

A checkpoint and a corpus answer different questions. "Which models does this
literature evaluate on" is one of the questions the archive is for, and while
both live in `datasets` it cannot be asked — the two populations are merged into
one list and every count over it is meaningless.

**It is deliberately not hidden behind a seam.** Three other local extensions
live in `pipelines/local/` with a one-line call site each (see the next note); a
fourth entity kind cannot, because it is a schema change and a schema change is
cross-cutting by construction. It touches the record, the harvest, the validator,
the applier, the output contract and the directory layout at once. Rather than
invent an extension point that would have to anticipate every such change, the
delta stays where it is and is marked `# LOCAL` at each site, with as the index. `grep -rn "LOCAL" pipelines/` is the whole
discovery mechanism.

The applier line is called out in the register because it is the one that gets
forgotten: `PaperSummary.models` defaults to `[]`, so an applier that does not
copy the field drops every `models` a reader submits, silently, with the field
merely looking unused.

## Trade-offs and rejected alternatives

**The graph page cannot colour it.** `publish/graph_page.py` validates three
categorical hues against CVD ΔE over every pair, and there is no fourth
validated step. `model` therefore takes the concept hue and is separated by shape
(triangle) and label only. That is a real limitation, stated in the code and in
the register rather than papered over. The alternative was leaving 123 model
nodes drawn *and labelled* "Concept", which is wrong rather than merely
ambiguous. Guessing a fourth colour was refused: the module's contract is that
its palette is validated, not chosen.

`publish/material.py` still buckets only concept, method and dataset, so models
do not get their own section in a lecture note or report. Left as is because no
output has asked for it yet.

## What a reviewer should check

- `python3 -m unittest tests.test_model_kind` — the kind survives a harvest, a
  model outranks a dataset for the same name, and a real dataset stays one.
- That the applier copies the field: `grep -n models pipelines/enrich/apply.py`
  must show it in **both** `_apply_paper` and `_apply_video`.
- The kind is never hard-coded as a three-tuple anywhere:
  `grep -rn '"concept", "method", "dataset"' pipelines/` should return nothing.

## Downstream impact

**Breaking for a deployment that has already stored readings.** A summary
written before this has no `models` field; `from_dict` defaults it to `[]`, so
old records load and simply contribute no model entities. Nothing is lost and
nothing is migrated automatically. A deployment that wants its existing readings
re-classified has to re-read them — the information was never recorded, so it
cannot be derived.

New wiki notes appear under `wiki/models/`, and `Layout.ensure()` creates that
directory on the next run.
