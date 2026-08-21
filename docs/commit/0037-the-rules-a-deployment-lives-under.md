# 0037 — The rules a deployment lives under

| | |
| --- | --- |
| **Commit** | `docs: state the code-and-archive rules in CLAUDE.md` |
| **Scope** | `CLAUDE.md` |
| **Kind** | docs |

## What changed

A `## Working on the code` section in `CLAUDE.md`, five bullets under one
premise: **the code is replaced; the archive is not.**

The rules were all real before this — enforced by tests, discovered by bugs,
written up one at a time in `docs/commit/`. None of them was anywhere a session
would read before starting work.

## Why it is built this way

**A commit note explains one change; `CLAUDE.md` is the contract.** Notes 0035
and 0036 are where the layering and the churn fix are argued, and they are the
right place for the argument. But nobody reads thirty-seven notes before
touching a file, and both rules are the kind that is broken by accident rather
than by disagreement — the renderer that wrote to `data/` looked completely
ordinary for months.

**One premise, then consequences.** The bullets are not a list of preferences.
Every one of them is what "a deployment keeps its archive across an upgrade"
implies, and stating the premise first is what lets a reader work out the answer
to a case the list does not cover.

**Every claim is checkable, and was checked.** The layering claim names the test
that enforces it. The schema bullet was drafted as "a schema change needs a
migration path" — plausible, and *false*: `SCHEMA_VERSION` is stamped on every
record and read nowhere, so there is no migration machinery to invoke. What is
actually true is a property of `_Record.from_dict`, verified rather than
assumed:

```
unknown key survives round trip: False
missing key takes its default  : ''
warning emitted                : none
```

So the bullet says what the code does — adding a field is safe, renaming one
drops its value silently — which is the thing that would actually cost somebody
an archive.

## Trade-offs and rejected alternatives

**`CLAUDE.md` gets longer, and it is already long.** It is read at the start of
every session, so a paragraph added there costs more than a paragraph anywhere
else. Five bullets and one premise is the budget this earned; the reasoning
stays in the notes and is linked from nowhere, because a rule that needs a
citation to be followed is a rule that is too complicated.

**Rejected: an enforcement hook for the rules that lack a test.** "A render is
not an edit" and the layering rule have tests. "Adding a field is safe" does
not, and a lint for it would be guessing at intent. It is stated instead, which
is honest about which rules are checked and which are trusted.

**Rejected: putting this in `README.md`.** That file is for a human deciding
whether to deploy the repository. This is for whoever is about to change it.

## What a reviewer should check

- **That each claim still holds**, since a stale rule is worse than no rule:
  - `grep -rlE "\.save_(paper|video|concept|finding|abstracts|transcript)" pipelines/publish/`
    must return nothing.
  - `tests/test_layering.py` must still contain the unchanged-archive test.
  - The `from_dict` behaviour is three lines in `pipelines/common/schema.py`.
- **That nothing contradicts the `## Rules` section above it.** The two are
  adjacent and one is about the archive's contents, the other about the code
  that produces them.

## Downstream impact

Documentation only. No code, no records, nothing regenerated.

A deployment that has diverged from these rules will not be told so by anything
automatic except the layering test, which ships with the same pull.
