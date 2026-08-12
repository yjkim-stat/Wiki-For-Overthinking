# 0040 — A template is resolved against the deployment, then against the code

| | |
| --- | --- |
| **Commit** | `feat(publish): resolve a template against the deployment, then the code` |
| **Scope** | `pipelines/common/paths.py`, `pipelines/publish/__init__.py`, `pipelines/publish/{wiki,graph_page,lecture_note,slides,report}.py`, `tests/test_templates.py` |
| **Kind** | feature |

## What changed

`load_template` takes a search order rather than a directory, and
`Layout.template_dirs` supplies one: the deployment's `templates/` first, the
code checkout's second. Where the repository is run in place those are the same
directory and the list has one entry.

The effect is that a deployment keeping its archive in a repository of its own
no longer has to hold a copy of `templates/` at all. It renders with the ones
the code ships, and overriding a single file means writing that one file.

## Why it is built this way

Templates are the one directory that belongs to both halves. The README calls
them yours — how your artifacts look is an editorial decision — while the code
ships a working set and goes on improving it. Both are true, and a per-directory
fallback would make you choose: either take the code's whole directory or take
your own, frozen at the version you copied it from.

Resolving per file is what lets both be true at once. Changing a heading in the
wiki note template costs you that template and nothing else; every other one
still arrives with `git pull`. The failure this avoids is silent — a deployment
that copied the directory in month one keeps rendering happily for a year with
templates nobody has updated, and nothing anywhere reports the drift.

Before this, a deployment root without `templates/` died with `TemplateError:
missing template: .../templates/wiki/note.md` on its first render, with
everything else about it correct. That is what
`RenderWithoutDeploymentTemplatesTests` pins.

The missing-template error now names every directory it looked in, because with
a search order "missing template: X" would name only the last place tried.

## Trade-offs and rejected alternatives

**A deployment cannot delete a template to suppress an artifact.** Removing one
now falls through to the shipped copy rather than raising. Nothing depended on
that, and disabling an output is what `topic.outputs` is for.

**Considered: copying `templates/` into the deployment at setup.** Simpler, one
concept fewer, and it is what the first draft of the deployment workflow said to
do. Rejected for the drift above: the copy is invisible once made.

**Considered: a `templates:` path in `settings.yaml` pointing back at the code
checkout.** Works today — an absolute path in that block is honoured — but it
hard-codes one machine's layout into a committed config file, and it is
all-or-nothing rather than per file.

**Cost:** two directories are stat'ed per template instead of one, on a handful
of files per render. Not measurable.

## What a reviewer should check

- The order, in `tests/test_templates.py`: an override in the deployment wins,
  and a file only the code has is still found. Break it by reversing
  `template_dirs` and watch `test_the_deployment_directory_is_searched_first`
  fail.
- That in-place behaviour is unchanged: `Layout(root=REPO_ROOT).template_dirs`
  must be a one-element list, so nothing new is searched for a deployment that
  never split.
- That no renderer still passes a bare directory: `grep -rn "layout.templates"
  pipelines/publish/` should be empty.

## Downstream impact

None required. `layout.templates` still exists and still means the deployment's
own directory; `load_template` still accepts a single `Path`. A deployment with
a full `templates/` copy behaves exactly as before — and can now delete the
files it never customised, which is the point.
