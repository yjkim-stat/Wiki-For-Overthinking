# 0095 — A render is not an edit, in the wiki either

| | |
| --- | --- |
| **Commit** | `fix(publish): the graph is rewritten only when it moves` |
| **Scope** | `pipelines/publish/__init__.py`, `pipelines/publish/wiki.py`, `pipelines/publish/graph_page.py`, `tests/test_render_is_not_an_edit.py` |
| **Kind** | fix |

## What changed

`wiki/_meta/graph.json` and `wiki/graph.html` each carry the time they were
generated, and both are tracked. So every render produced a diff in two files
whatever had or had not happened:

```
-  "generated_at": "2026-08-21T01:01:53Z",
+  "generated_at": "2026-08-21T01:20:01Z",
```

Both are now left alone when that stamp is the only thing that would move.

## Why it is built this way

**This is the defect [note 0036](0036-a-render-is-not-an-edit.md) fixed, one
directory across.** That note established the rule for records: a field that
restamps itself every pass buries the real changes in a diff nobody can read.
`data/` has been held to it since; these two files never were, and they are the
artifacts a person is most likely to open.

**The stamp is kept, not dropped.** Dropping it is simpler and loses something:
written only when the drawing actually moved, `generated_at` now says when the
graph last *changed*, which is worth more than when somebody last ran a command.

**Compared with the stamp masked rather than by parsing.** For the JSON that is
a dict comparison with one key removed; for the page, `unchanged_but_for` blanks
the footer line in both and compares the rest. The page is a rendering of the
graph plus a template, so a template edit still rewrites it — which is correct,
and would not be if the check were "did the graph dict change".

## Trade-offs and rejected alternatives

**A file whose content is identical but whose stamp is old is left old.** After
this lands, a deployment's first render corrects the stamp once and then stops
touching it, so an old date means "nothing has changed since", not "nobody has
rendered since". That is the intended reading and it is the opposite of what the
field meant before.

**Considered: dropping `generated_at` from both.** No comparison to get wrong and
no stale-looking date. It also throws away the only record of when the wiki's
shape last moved, which is a real question about an archive that grows slowly.

**The comparison costs one read of each file per render**, against two writes it
avoids.

## What a reviewer should check

Three mutations: always write the JSON, always write the page, and never write
the JSON. The first two each take down `test_a_second_render_rewrites_neither`;
the third takes down sixteen tests, which is the shape of a guard that fails
safe.

- That test compares modification time as well as bytes. A rewrite with an
  identical stamp is invisible to a byte comparison, and the stamp only moves
  once a second — the trap this repository has hit twice before, so the test
  sleeps past a second boundary.
- `test_the_stamp_is_still_there`, because the cheap fix is to delete it.

## Downstream impact

The first render after this lands rewrites both files once, and subsequent
renders over an unchanged archive leave them untouched. Anything reading
`generated_at` as "when render last ran" now reads "when the graph last changed".
