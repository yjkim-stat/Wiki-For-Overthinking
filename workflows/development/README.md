# Development

Changing the pipeline itself. Authority is
[`CLAUDE.md` § Working on the code](../../CLAUDE.md#working-on-the-code); this
is where the code goes and how to get there. The harness is in
[`harness.md`](harness.md).

**One premise:** a deployment pulls a new version every so often and keeps
running against the `data/` it has been accumulating for months. Everything
below follows from that.

## Where does this code go?

```
Does it write to data/ ?
├── no  ────────────────────────► publish/     a renderer. Pure function of the archive.
└── yes
    ├── does it come from outside? ──────────► collect/    a source.
    └── is it derived from what we hold? ───► enrich/      scoring, dedup, queue,
                                                           entities, applying results.
```

`common/` is config, records, paths and the HTTP client — things all three use
and none of them owns. `run_daily.py` collects, `render.py` rebuilds; both are
orchestrators and should hold no domain logic.

If a function needs a helper from a layer above it, that is the layering telling
you something. A function-local import to dodge a cycle is the specific smell —
it is how `_apply_concept` reached into the renderer for `slug_for`, and moving
it was [`docs/commit/0035`](../../docs/commit/0035-rendering-does-not-write-to-data.md).

## Adding a source

1. **Config first.** A block in `config/sources.yaml` with `enabled`, its bounds
   and a comment saying what the source cannot tell you. The comment is the
   part that ages well.
2. **A module in `collect/`** returning `Paper` or `Video` records. Take
   `client: Client | None = None` so a test can inject a stub, and capture it
   before defaulting if you pass it on.
3. **Wire it into `run_daily.py`**: the sources list, the `--source` choices,
   and a `try/except` so a dead source never sinks a run.
4. **Fixture tests.** No network. The fixture is what the test actually asserts
   about, so make it carry the awkward parts of the real page.
5. **A loud zero.** A source that parses to nothing must warn. A silent zero
   looks exactly like a quiet week — the failure a collector is most exposed to.

## Changing a record

- **Adding a field with a default is safe.** `from_dict` keeps only fields it
  knows and defaults the rest, so an old record loads fine.
- **Renaming or removing one destroys data.** The old value is dropped on load
  and gone at the next write, with no error anywhere. If you must, write the
  migration and say so in the note — `SCHEMA_VERSION` is stamped on every record
  and read by nothing, so there is no machinery to lean on.
- **Derived and authored live in the same record.** A concept's evidence is
  re-derived every pass; its definition and aliases are carried across
  untouched. Whatever a person wrote must survive every regeneration.

## Changing a renderer

Editing a template or a renderer never requires re-collecting anything.

```bash
rm -rf archive wiki outputs && python3 -m pipelines.render
```

If that does not reproduce the tree, something is not a pure function of `data/`
and that is the bug.

## Before you commit

A render over an unchanged archive must change no record. Check it:

```bash
python3 -m pipelines.render && git status --short data/
```

Then [commit-and-push](../commit-and-push/). Every change to code, config,
templates or docs needs a note.
