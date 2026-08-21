# 0029 — The wiki, drawn

| | |
| --- | --- |
| **Commit** | `feat(publish): render the wiki graph as a page you can look at` |
| **Scope** | `pipelines/publish/graph_page.py`, `pipelines/publish/wiki.py`, `templates/wiki/graph.html`, `CLAUDE.md`, `README.md`, `tests/test_graph_page.py` |
| **Kind** | feature |

## What changed

`render` now writes `wiki/graph.html`: the concept map as a node-link diagram,
built from the `wiki/_meta/graph.json` the wiki renderer already emits. Marks
carry kind by colour **and** shape, size by evidence count. Names are hidden
until a mark is hovered or focused. A table view sits under the figure.

## Why it is built this way

**Almost no words, on purpose.** A concept map with two hundred printed labels
is a wall of text, and nobody reads walls. What is always visible is shape, size
and colour — what kind of thing this is, how much evidence stands behind it,
which topic it hangs off. The name is one hover away, and the table view has all
of them at once for anyone who would rather read than look.

**The palette was computed, not chosen — and the computation changed the
design.** Running candidate pastels through the validator produced three
findings that a taste-based process would have shipped as bugs:

1. *Four categorical pastels do not exist.* Every four-hue set failed the
   all-pairs floors — a node graph puts any pair adjacent, so the permissive
   adjacent-pairs rule does not apply. That is why **topics are not a fourth
   colour**: they are a different level of the structure, so they wear neutral
   ink and the three entity kinds take the three validated slots. The
   constraint improved the encoding.
2. *True pastels fail outright.* L ≈ 0.80–0.86 sits outside the passing band and
   reads as gray to the validator's chroma floor. The final steps sit at the
   light edge of the band and get their pastel character from **translucent
   fills over the validated stroke** — the colour that carries identity is the
   2px outline, which is what the validator checked.
3. *Both modes land in the 6–8 CVD band*, which is legal only with a second
   channel — hence circle, square, diamond. And coral falls under 3:1 on the
   light surface, which obliges the relief rule — hence the table view. Neither
   is decoration; both are the price of the palette.

Dark mode is its own re-stepping of the same three hues into the dark band, not
a flip of the light values.

**The layout is deterministic.** Generated files are committed here, so a layout
seeded from a clock or an RNG would rewrite the page on every render and fill
the history with noise. Positions are seeded from a SHA-1 of each node id and
relaxed for a fixed number of iterations — same input, same picture, byte for
byte. Even the degenerate coincident-node case is nudged deterministically.

**Two defects were found by rendering it and looking**, which is why that step
exists. Edges ran to node *centres* and the translucent fills let them show
through, so every mark appeared to have scribbles inside it; marks now sit on an
opaque backing and edges are trimmed to the boundary. And the size ramp was so
compressed that the magnitude encoding was invisible. Neither would have been
caught by the validator, which checks colour and not geometry.

## Trade-offs and rejected alternatives

**Rejected: a JavaScript force layout in the page.** Interactive dragging, at
the cost of a non-deterministic committed file and a dependency. The page ships
zero JavaScript; hover is CSS.

**Rejected: printing every label.** The user asked for few words, and the graph
is unreadable with them.

**Cost: big wikis are truncated.** Past 90 nodes the least-attested entities are
dropped, and the count line says how many. A picture of six hundred nodes is not
a picture, but this is a real limit on what the page shows.

**Cost: `O(n²)` per iteration in pure Python.** At the 90-node cap this is
milliseconds; it is the cap, not the algorithm, that keeps it cheap.

**Cost: the co-occurrence edges are dense.** Eleven entities produced 43 links
in the sample. They are drawn recessive — thinner, dashed, lower opacity — but a
mature wiki will still look busy.

## What a reviewer should check

The two obligations the validator handed down, both of which have tests:

```bash
python3 -m unittest tests.test_graph_page -v
```

`test_kind_is_carried_by_shape_as_well_as_colour` and
`test_a_table_view_is_present` are not stylistic preferences — remove either and
the palette stops being legal. `test_the_same_graph_lays_out_identically` is
what keeps the committed file stable.

Then open the page in both colour schemes and look at it. The failure modes here
are geometric and no test catches them.

To regenerate the palette check:

```bash
node scripts/validate_palette.js "#f7958d,#4a9a5e,#797dcd" --mode light --pairs all
node scripts/validate_palette.js "#de6f68,#0a7e3a,#6c6ecb" --mode dark  --pairs all
```

## Downstream impact

Additive: one more generated file, `wiki/graph.html`, rebuilt on every render
like everything else under `wiki/`. No configuration. A deployment that
restyles it edits `templates/wiki/graph.html` — but changing the three
categorical hexes means re-running the validator, because the shape encoding and
the table view are load-bearing only for *this* palette's warnings.
