# The graph draws an authored link as co-occurrence, in the faintest style it has

**Status:** solved 2026-08-13 by **option B + the legend row from A** — see
[Resolution](#resolution) at the foot of this file and
[note 0050](../commit/0050-three-claims-three-weights.md).
**Kind:** design question · fix
**Found:** 2026-08-12, immediately after `related_authored` landed
**Touches:** `pipelines/publish/wiki.py`, `pipelines/publish/graph_page.py`, `templates/wiki/graph.html`

[Note 0045](../commit/0045-a-ruled-link-is-not-derived-away.md) split entity links
into two fields because they answer different questions: `related` is what turned
up alongside this, `related_authored` is what somebody said to read next.
`Concept.neighbours` unions them so both reach the renderers.

Both renderers then throw the distinction away. `wiki.py` iterates the union and
stamps every entity-to-entity edge `"type": "co-occurs"`, and `graph_page.py` maps
that type to a CSS class the stylesheet draws **dashed, thinner and at 55%
opacity** — the treatment reserved for the weakest link the graph has. A person's
deliberate assertion is rendered as the faintest thing on the page, and labelled
as something it is not.

This is a design question as much as a defect: nobody has decided whether the
graph should distinguish them. The point of filing it is that right now the graph
*asserts* they are the same, and the data model no longer agrees.

---

## What you can observe

```bash
export RA_WM_ROOT=/path/to/an/archive
cd /path/to/this/checkout

# answer a definition task with a neighbour that co-occurrence cannot reach,
# i.e. one that never shares a summary's concepts/methods/datasets list with it
python3 -m pipelines.enrich.queue complete concept__<slug> --file /tmp/def.json
python3 -m pipelines.render

python3 - <<'PY'
import json, os
g = json.load(open(os.path.expandvars("$RA_WM_ROOT/wiki/_meta/graph.json")))
print({e["type"] for e in g["edges"]})
PY
```

The set comes back `{'co-occurs', 'covers'}`. There is no third type, so the
authored edges are indistinguishable from derived ones in the file, and therefore
in the drawing.

**The case that found it.** `cosmos-3` was answered with seven neighbours. Two of
them (`cosmos`, `cosmos-predict2-5`) also co-occur; one (`cosmos-transfer1`) has no
note yet and is correctly not drawn; the remaining **five** are edges that
co-occurrence can never produce — no summary in that archive lists two Cosmos
generations in one `methods` array, which is the whole reason the links had to be
authored. All five are written to `graph.json` as `co-occurs`.

Today that is 1 entity and 5 edges, because the feature is one day old. The number
will grow with every definition answered, and the mislabelling is per-edge and
permanent.

---

## Why it happens

**1. The edge builder hard-codes the type.** `pipelines/publish/wiki.py:305-317`:

```python
seen_pairs: set[tuple[str, str]] = set()
for concept in live.values():
    source = f"{concept.kind}:{concept.slug}"
    for slug in sorted(concept.neighbours):
        ...
        edges.append({"source": source, "target": target, "type": "co-occurs"})
```

Line 308 reads the union; line 317 names the result after only one of its two
inputs. Before note 0045 that literal was accurate — `neighbours` did not exist and
the loop read `related`, which really was co-occurrence and nothing else. The
field changed underneath the literal and the literal did not move.

**2. The renderer has exactly two visual classes.**
`pipelines/publish/graph_page.py:194`:

```python
css = "edge co" if edge.get("type") == "co-occurs" else "edge"
```

**3. The stylesheet spends the weak treatment on it.**
`templates/wiki/graph.html:62-63`:

```css
.edge    { stroke: var(--edge); fill: none; stroke-width: 1.4; }
.edge.co { stroke-dasharray: 3 4; stroke-width: 1; opacity: 0.55; }
```

So solid-and-full is `covers` (topic to entity, which is structural), and
dashed-thin-faded is everything else. The design reasoning is sound as it stands —
co-occurrence is weak evidence and should look weak. It just now also catches the
one kind of link that is not weak evidence at all.

**4. There is no edge legend to read it by, either.** `_legend`
(`graph_page.py:238-258`) is built from node **kinds** plus the `settled` mark and
a size note. It says nothing about edges, so a reader has no key for solid versus
dashed today, let alone for a third style.

---

## Why it matters

**It inverts the archive's own evidence ordering.** Everywhere else in this
repository, a thing a person ruled on outranks a thing a counter derived: a ruled
`kind` defends itself against the next harvest ([note 0015](../commit/0015-a-ruled-kind-defends-itself.md)),
a definition survives the loss of the evidence that prompted it, and note 0045
exists precisely because an authored link must not be derived away. The graph is
the one artifact where the derived value is drawn at full strength and the
authored one is dashed and faded to 55%.

**It is the one place the distinction would pay off visibly.** A wiki note lists
its neighbours as text and the ordering is alphabetical, so nothing is lost there
by merging the two. The graph is a picture whose entire job is to show structure
at a glance, and "these two were mentioned together once" versus "somebody read
both and says they belong together" is exactly the kind of difference a picture
can carry and a list cannot.

**The failure is silent and cumulative.** No warning, no counter, nothing in
`render`'s result dict. `wiki.update` reports `entities` and `notes`;
`graph_page` logs a node and edge count. An edge typed wrongly looks like an edge.

**Scope, honestly stated.** `graph.json` is read by nothing but
`graph_page.py:194`, so this is contained: no consumer outside the repository is
relying on the current type vocabulary, and the fix cannot break anything
downstream. The cost of leaving it is not correctness of any number — it is that
the drawing tells a reader something false about where its links came from.

---

## Options

### A. A third edge type and a third style.

Emit `"type": "authored"` for slugs in `related_authored`, `"co-occurs"` for the
rest, and give it a class the stylesheet draws solid at full opacity. Add an edge
row to `_legend`.

- **For:** says what is true, in the artifact where it is worth saying. Small: one
  branch in the loop, one class, one legend entry.
- **Against:** an edge can be *both* — authored and co-occurring, as two of the
  seven in the case above are. A single `type` string forces a precedence, and
  "authored wins" is a judgement to make deliberately rather than fall into.
  The legend grows, and `_legend` currently takes only node kinds, so it needs a
  second input.
- **Cost if wrong:** a redraw. Nothing stored depends on the vocabulary.

### B. Keep one type, add a boolean.

`{"source":…, "target":…, "type": "co-occurs", "authored": true}`. The renderer
styles on the flag.

- **For:** no precedence to invent — an edge can be co-occurring *and* authored,
  and both facts survive. Backward compatible: an old reader that only knows
  `type` still draws every edge.
- **Against:** two fields describing one thing, and `type` keeps a name that is now
  only sometimes accurate. Someone reading `graph.json` cold would still be
  misled by the type string.
- **Cost if wrong:** same as A.

### C. Rename the type and accept the merge.

Change the literal to `"links"` or `"related"` — accurate for the union — and
decide explicitly that the picture does not distinguish provenance.

- **For:** one word. Removes the false claim without spending anything on a
  distinction nobody has asked to see.
- **Against:** throws away the only place the note-0045 split could be shown, and
  leaves an authored link drawn in the faint style meant for weak evidence, which
  is half the complaint.

### D. Leave it, and record that it was considered.

- **For:** 5 edges in one archive; the graph is a browsing aid, not a record.
- **Against:** the count only grows, and the wrongness is in a stored artifact
  rather than a rendering choice — `graph.json` says `co-occurs` about links that
  never co-occurred.

**Recommendation: B, plus the legend row from A.** The boolean is the shape that
matches the data, because the two properties genuinely are independent and A has to
invent a precedence to avoid saying so. If the type string's name still grates
after that, rename it in the same commit as C suggests — `"type": "links"` with
`"authored": true|false` is accurate on both fields at once, and that combination
is probably where this should land.

Whatever is chosen, the stylesheet decision is the substantive half: an authored
link should not be drawn at 55% opacity, and deciding what it *should* look like
is a design call, not a mechanical one.

---

## Tests

`tests/test_related_links.py` (added with note 0045) covers the data model and the
note rendering. It does not assert on `graph.json`. Add:

1. **The graph distinguishes them.** A fixture entity with an authored neighbour
   that co-occurrence cannot reach — the same fourth-entity shape note 0045's
   resolution says was the only one that caught a false pass — asserted to produce
   an edge marked as authored, and a purely co-occurring pair asserted not to be.
2. **An edge that is both.** Authored *and* co-occurring must not lose either
   fact under the chosen encoding. This is the case that tells A and B apart, and
   it is the one a naive fixture will miss.
3. **A regression on the vocabulary.** Assert the exact set of types
   `graph.json` can contain, so the next change to the loop has to update the test
   deliberately rather than silently widen it.

---

## What a reviewer should check

- `wiki.py:317` and the field it is derived from agree after the change. The whole
  defect is a literal that outlived the field it described; a fix that leaves a
  second such literal has repeated it.
- The legend accounts for every edge style actually drawn. Today it accounts for
  none of them, which is a smaller version of the same problem and worth closing
  in the same pass.
- An authored link is not drawn in the style the stylesheet reserves for weak
  evidence. If `.edge.co`'s dashing still applies to it, only the JSON was fixed.
- `python3 -m pipelines.render` twice on an unchanged archive still produces no
  diff in `wiki/graph.html` and `wiki/_meta/graph.json`.
- Edges are deduplicated by unordered pair (`seen_pairs`, `wiki.py:305-316`). If
  the same pair arrives once as authored and once as derived from the other
  endpoint, whichever encoding is chosen must not depend on iteration order —
  `live.values()` order deciding an edge's label would be a silent
  non-determinism.

## Notes for whoever picks this up

- The two earlier issues filed here were both a field one half of the pipeline set
  and another half dropped. This one is the next stage of the same story: the
  field now survives, and the artifact that draws it has not caught up. See
  [`../solved/related-links-are-asked-for-and-discarded.md`](../solved/related-links-are-asked-for-and-discarded.md)
  and [`a-hand-filed-pdf-is-lost-when-its-record-merges.md`](../solved/a-hand-filed-pdf-is-lost-when-its-record-merges.md).
- No archive-side finding was recorded for this one. It is a defect in how the
  repository draws its own output, not something the group established about the
  literature.

---

## Resolution

**Option B, with the legend row from A, and C's rename folded in** — which is
where this document guessed it would land. An entity-to-entity edge is now
`{"type": "links", "authored": true|false}`. Commit
`fix(publish): a ruled link is drawn as one`, note
[0050](../commit/0050-three-claims-three-weights.md).

The boolean rather than a third type, because the two properties really are
independent: an edge can be co-occurring *and* ruled, and a single `type` string
would have had to invent a precedence to avoid saying so. `links` rather than
`co-occurs`, because the loop reads the union and the old literal named one of
its two inputs.

**The stylesheet decision, which this document called the substantive half.**
Three claims, three weights: `covers` is structural and solid; a co-occurrence
keeps the dashed, thin, 55% treatment, because it *is* the weakest thing the
graph knows; a ruled link is drawn solid at full opacity in `var(--anchor)`,
darker than either. No fourth hue — the palette validates three and the node
marks own them. That ordering is the one the rest of the archive already uses:
a person's judgement over a derived count.

The legend now names every edge style drawn, and only the styles drawn. It
accounted for none of them before, which this document correctly called a
smaller version of the same problem.

### The two tests that did not bite at first

Both are worth recording, because both passed while the property was false.

- **The renderer test matched anywhere on the page.** The legend swatch carries
  the same class as a drawn edge, so a substring search found it even with the
  renderer stamping every edge `edge link`. It now matches a drawn line
  specifically: drawn coordinates are formatted to one decimal and the swatch's
  are whole numbers.
- **The order-independence test used the wrong pair.** For a pair co-occurrence
  cannot reach, only the ruling end holds the other in `neighbours`, so only
  that end can emit the edge — and reading a single end is accidentally correct.
  The trap needs a pair that **co-occurs**, where both ends can emit and the
  first arrival wins. Two versions of the test missed this before the mutation
  exposed it.

The remaining checks from this document hold: `wiki.py`'s literal and the field
it describes now agree, a render twice over an unchanged archive still produces
no diff, and the type vocabulary is pinned by a test so the next change to the
loop has to widen it deliberately.
