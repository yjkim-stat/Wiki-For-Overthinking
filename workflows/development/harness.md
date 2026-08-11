# Harness — development

## The boundary tests

`tests/test_layering.py` is the one that guards the premise the whole design
rests on. Two kinds, on purpose:

**Behavioural.** Every file under `data/` is snapshotted by content, a renderer
runs, and the snapshot must be unchanged. This catches a write that happens.

**Static.** No module under `publish/` may so much as mention `store.save_*`.
This catches a write that has merely been written down, including on a path no
fixture reaches.

Neither passed before the refactor that moved deriving out of the renderers. If
you add a package, add it to the static check.

## Two tests that must stay a pair

```
test_a_full_render_over_an_unchanged_archive_changes_no_record
test_a_new_mention_does_move_the_record
```

The first says a render is not an edit; the second says a quiet render is not a
deaf one. Either alone is satisfiable by broken code — the first by never
writing, the second by always writing.

The first sleeps past a second boundary. `utcnow()` has second resolution, so
without the sleep it passes whether or not the bug is present. It did exactly
that when first written.

## Running it

```bash
python3 -m unittest discover -s tests -t .      # 403 tests
python3 -m unittest tests.test_layering -v      # the boundary alone
```

Tests touch neither the network nor the real `data/`. A collector is tested
against a fixture; a run is tested in a `tests/sandbox.py` throwaway root. If a
test needs the network, the collector needs a `client` parameter.

## Prove the test bites

A test that passes is not evidence until you have seen it fail. Break the thing
deliberately, run, restore:

```bash
cp pipelines/enrich/concepts.py /tmp/bak
# ...make the change wrong...
python3 -m unittest tests.test_layering        # expect FAILED
cp /tmp/bak pipelines/enrich/concepts.py
```

Every fix in `docs/commit/` from 0032 onward records which mutation was used and
how many tests it took down. Do the same — a note claiming a test covers
something is worth as much as the mutation that proves it.

## Checks worth running by hand

```bash
# who writes to data/ — publish/ must be empty
grep -rlE "\.save_(paper|video|concept|finding|abstracts|transcript)" pipelines/

# a render over an unchanged archive must be a no-op
python3 -m pipelines.render && git status --short data/

# derived really is derivable
rm -rf archive wiki outputs && python3 -m pipelines.render && git status --short

# the ignore rules still hold for anything heavy you added
git check-ignore -v <path>
```

## What nothing checks

- **That a collector's parser matches the live page.** Fixtures test the parser
  against what you believed the page looked like. When a site changes shape the
  suite stays green and collection quietly returns nothing — which is why a zero
  must warn.
- **That a new field is actually populated.** Adding one with a default passes
  every test while every record carries the default for ever.
- **Import direction.** Nothing fails if `enrich/` starts importing `publish/`.
  The static check covers writes, not dependencies; read the imports.
- **Anything about the network.** By design. No test may reach it, so no test
  can tell you a source is reachable.
