# 0050 — Three claims, three weights

| | |
| --- | --- |
| **Commit** | `fix(publish): a ruled link is drawn as one` |
| **Scope** | `pipelines/publish/wiki.py`, `pipelines/publish/graph_page.py`, `templates/wiki/graph.html`, `tests/test_related_links.py`, `docs/issues/`, `docs/solved/` |
| **Kind** | fix |

## What changed

[Note 0045](0045-a-ruled-link-is-not-derived-away.md) split entity links into a
derived list and a ruled one, and `Concept.neighbours` unions them so both reach
the renderers. The edge builder then read that union and stamped every edge
`"type": "co-occurs"` — the literal did not move when the field underneath it
did — and the stylesheet drew that type dashed, thinner and at 55% opacity, the
treatment reserved for the weakest link the graph has.

So a person's deliberate assertion was drawn as the faintest thing on the page
and labelled as something it was not. An edge is now
`{"type": "links", "authored": true|false}`, and there are three edge styles
where there were two.

This is the regression 0045 introduced, filed the day after and fixed here.

## Why it is built this way

**A flag rather than a third type string.** An edge can be co-occurring *and*
ruled — two of the seven links in the case that found this were both. A single
`type` would have had to invent a precedence to avoid saying so, and "authored
wins" is a judgement worth making deliberately rather than falling into. With a
boolean, both facts survive and nothing has to be decided.

**`links` rather than `co-occurs`.** The loop reads the union of two things and
the old literal named one of them. Renaming costs a redraw and nothing else —
`graph.json` is read by `graph_page.py` and by nothing outside this repository.

**The label is asked of both ends.** Edges are deduplicated by unordered pair
with the first arrival winning, so reading only the emitting concept's list
would let dictionary order decide whether an edge is authored. That is a
difference that would appear and vanish between renders with `data/` unchanged,
which is the kind of non-determinism that costs an afternoon to find.

**The stylesheet is the substantive half.** Three claims, three weights: a topic
covering an entity is structural and stays solid; a co-occurrence keeps the
dashed, thin, faded treatment, because it genuinely is the weakest thing the
graph knows; a ruled link is drawn solid at full opacity in `var(--anchor)`,
darker than both. No fourth hue — the palette validates three and the node marks
own them, so the distinction is carried by weight and dash instead.

That ordering restores the archive's own: everywhere else here a thing a person
ruled on outranks a thing a counter derived — a ruled `kind` defends itself
against the next harvest, a definition outlives the evidence that prompted it —
and the graph was the one artifact that inverted it.

**The legend now names every edge style, and only the ones drawn.** It named
none of them before, so a reader had no key for solid against dashed even when
there were only two. `_edge_styles` derives the set from the edges themselves
rather than from what the code can emit, so a graph with no ruled links does not
advertise a style it never used.

## Trade-offs and rejected alternatives

**`covers` edges carry no `authored` key at all**, rather than `false`. The
property does not apply to a topic-to-entity edge, and writing `false` would
assert something about a relation the question does not reach.

**Option D — leave it — was tenable when filed** at five edges in one archive,
and is the reason this is worth a note rather than a silent fix: the wrongness
is in a stored artifact, not a rendering choice, and it is per-edge and
permanent. `graph.json` said `co-occurs` about links that never co-occurred.

**Existing archives get a large one-off diff.** Every entity-to-entity edge in
`wiki/_meta/graph.json` changes its `type`, and `wiki/graph.html` is redrawn.
Nothing is lost and nothing needs migrating.

## What a reviewer should check

Four mutations, and two of them are the point of this note:

- Revert the literal to `"co-occurs"` — eight tests fail.
- Drop `.edge.link.authored` from the stylesheet — the drawn-style test fails.
- **Make the renderer stamp every edge `edge link`.** The first version of that
  test searched the whole page for the class and passed, because the legend
  swatch carries it. It now matches a drawn line: drawn coordinates are
  formatted to one decimal, the swatch's are whole numbers.
- **Read only the emitting end's `related_authored`.** The first two versions of
  the order-independence test used a pair that co-occurrence cannot reach, where
  only the ruling end holds the other in `neighbours` at all — so only that end
  can emit, and one-ended reading is accidentally correct. The trap needs a pair
  that **co-occurs**, and both directions ruled in turn, so that the ruling end
  is second to arrive in one of them however `live` is ordered.

Also worth confirming: `python3 -m pipelines.render` twice over an unchanged
archive still produces no diff in `graph.json` or `graph.html`, and
`test_the_type_vocabulary_is_closed` pins the exact set of types so the next
change to the loop has to widen it on purpose.

## Downstream impact

`wiki/_meta/graph.json` changes shape for entity-to-entity edges: `type` becomes
`links` and a boolean `authored` appears. Nothing outside this repository reads
that file. The next render rewrites both it and `wiki/graph.html`; expect the
diff to touch every edge once and never again.
