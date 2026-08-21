# Workflows

One folder per thing you might sit down to do. Each holds the **procedure** —
the ordered commands — and the **harness**: what checks each step, what failure
looks like, and how it announces itself.

## The rule this folder lives under

**A workflow file carries the procedure and its harness. It never restates the
contract.** Where a fuller authority exists it is linked, not copied.

That restraint is the point. This repository has already been bitten once by a
document that duplicated a fact and then went stale within a day — `docs/API.html`
described `data/abstracts/` as committed while another session was gitignoring
it (see [`docs/commit/0031`](../docs/commit/0031-fetch-before-you-start.md)).
Four places saying the same thing means three of them are wrong eventually. So
each row below names **who is authoritative**, and a disagreement is a bug in
the workflow file, not in the authority.

| Workflow | When | Authority | Harness |
| --- | --- | --- | --- |
| [Knowledge and wiki](knowledge-and-wiki/) | Every run: collect, read, render, record what was settled | [`CLAUDE.md`](../CLAUDE.md) | Queue validator · `test_layering` · `test_queue` · `test_render` |
| [Commit and push](commit-and-push/) | Before every commit that is not a routine digest | [`commit-notes` skill](../.claude/skills/commit-notes/SKILL.md) | `docs/commit/` index · full suite |
| [Deployment](deployment/) | Keeping the archive in a repository of its own, and updating the code under it | [`CLAUDE.md` § which tree](../CLAUDE.md#first-which-tree-is-the-archive-in) | `migrate status` · `test_config` · `test_templates` |
| [Migration](migration/) | Moving to a new container | [`migration/README.md`](../migration/README.md) | `MANIFEST.json` · `verify` · `test_migrate` |
| [Schedule](schedule/) | A scheduled session woke you, or you are wiring one up | The owner's Routines, outside this repo | Push-early rule · the run's own report |
| [Development](development/) | Changing the pipeline itself | [`CLAUDE.md` § Working on the code](../CLAUDE.md#working-on-the-code) | `test_layering` · fixtures · the full suite |

## What "harness" means here

Not a test runner. The set of things that will tell you the step went wrong —
and, more importantly, the places where nothing will:

- **A validator that rejects.** `queue complete` and `findings add` fail loudly
  on a bad field. Work with them, never around them.
- **A test that fails.** 416 of them. `tests/test_layering.py` is the one that
  guards the code-versus-archive boundary the whole design rests on.
- **A report you have to read.** `render`'s `stale` block and `migrate status`
  report things that are wrong while looking fine. Nothing acts on them.
- **A gap nobody checks.** Named in each `harness.md`, because an unchecked
  step you know about is safer than one you assume is covered.

## Running the whole harness

```bash
python3 -m unittest discover -s tests -t .     # 416 tests, no network, no real data/
```
