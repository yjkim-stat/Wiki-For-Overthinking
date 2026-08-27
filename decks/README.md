# Slide decks

A deck is written as small YAML files and built into HTML. Nothing in a
`build/` directory is edited by hand — it is rewritten from the YAML on every
run, and edits made there are lost at the next build.

```bash
python3 decks/build.py overthinking              # -> decks/overthinking/build/
python3 decks/build.py overthinking --standalone # + the offline twin
python3 decks/build.py overthinking --watch      # rebuild on every save
```

`--watch` is the one to use while writing: leave it running, keep the built
file open in a browser, and a save is one refresh away from being on screen.

## Where things live

| Path | What it is |
| --- | --- |
| `<deck>/deck.yaml` | title, fonts, the on-screen key hint, named styles |
| `<deck>/references.yaml` | the bibliography, once — slides cite it by key |
| `<deck>/slides/NN-name.yaml` | **one file per slide**, in filename order |
| `<deck>/assets/figures/` | figures captured from papers (see `assets/FIGURES.md`) |
| `<deck>/assets/diagrams/` | the hand-drawn SVGs, one file each |
| `<deck>/build/` | generated — **never edit**, never committed |
| `theme/deck.css`, `theme/deck.js` | how every deck looks and how it navigates |

Slide **order is filename order**, so moving a slide is renaming it and
inserting one is picking a number. The number in the file name has nothing to
do with the page number printed on the slide; that is counted at build time,
so inserting slide `14b-…yaml` renumbers the footer of everything after it.

## A slide file

```yaml
layout: content              # content (default) · cover · part
eyebrow: Related Work        # the small uppercase line above the title
eyebrow_color: green         # blue · rose · amber · green · violet
title: 측정의 세 갈래
body_height: 478px           # optional; the drawing room is 600px by default
blocks:                      # the slide's content, top to bottom
  - lead: 한 줄로 요약하는 문장.
  - bullets:
      - 첫째
      - 둘째
cite: [aggarwal2025, zhou2026]   # keys from references.yaml
foot: Related Work               # bottom-left label; the page number is automatic
```

Every value is HTML, so `<span class="em">…</span>`, `<br>` and `<sub>` work
inside any piece of text.

**`body_height` is the one measurement worth knowing.** The reference block at
the foot of a slide is as tall as the number of references on it, and the body
does not know that. When text lands on top of the citations, shrink
`body_height` until it does not.

## Blocks

A block is a mapping with exactly one key, and that key names the block's kind.
Most kinds take either a bare value or a mapping, so the simple case stays
short.

| Kind | Shortest form | Fields |
| --- | --- | --- |
| `lead` | `- lead: 문장.` | `text`, `style` |
| `bullets` | `- bullets: [하나, 둘]` | `bullets`, `size: sm`, `style` |
| `card` | see below | `color`, `k`, `t`, `n`, `bullets`, `blocks`, `style` |
| `cards` | a grid of cards | `cols: 2\|3\|4`, `items`, `style` |
| `table` | | `head`, `rows`, `style` |
| `figure` | a captured figure with its caption | `src`, `alt`, `caption`, `img_style`, `style` |
| `image` | a bare `<img>` | `src`, `alt`, `style` |
| `svg` | `- svg: 08-where-it-turns.svg` | `file`, `style` |
| `cond` | the grey pill row naming the conditions | list of `text` / `{text, kind: key\|warn}` |
| `note` | one line in the small grey note face | `text`, `style` |
| `caption` | a source line under a figure | `text`, `style` |
| `text` | a styled `<div>` of inline HTML | `text`, `cls`, `style` |
| `box` | a wrapper — grids and columns | `style`, `cls`, `blocks` |
| `html` | raw HTML, when nothing above fits | — |

### Cards

```yaml
- cards:
    cols: 3
    style: fill
    items:
      - color: green         # rose · blue · amber · green · violet · plain
        k: ①                 # kicker: small, uppercase, coloured
        t: 문항 선별          # title
        bullets: [짧게 풀리는 문항만 모은다, 한 번 돌리면 점수가 나온다]
        n:                   # notes, in order, under the bullets
          - 산출 · <span class="mono em">AUC_OAA</span>
          - 대가 · 그 문항 집합 밖에서는 못 잰다
        n_style: [family-out, family-cost]
```

A card's parts render in a fixed order: kicker, title, bullets, notes. When
that order is wrong — a card holding another card, say — give it `blocks:`
instead and spell the parts out in the order you want, using the same block
vocabulary as a slide body.

### Named styles

`deck.yaml` carries a `styles:` map. Any `style:` that has no colon in it is
read as one or more names from that map:

```yaml
styles:
  fill:   flex:1;min-height:0;
  column: display:flex;flex-direction:column;
```

```yaml
style: fill column        # -> flex:1;min-height:0;display:flex;flex-direction:column;
style: margin-top:16px;   # a colon means literal CSS, passed straight through
```

Use it for a look that repeats. A one-off `padding:14px 18px;` is clearer left
as it is.

### Diagrams

An SVG is its own file under `assets/diagrams/`, referenced by name. Each is
authored on a **1432-unit-wide viewBox**, which is the width of the content
column, so one viewBox unit is one CSS pixel and text inside a diagram is the
same size as text beside it.

## References

`references.yaml` holds each work once, keyed:

```yaml
zhou2026: Zhou, S., Ling, R., … <i>When more thinking hurts</i>. arXiv:2604.10739. <a href="…">(link)</a>
```

A slide names keys, and the build fails on one that does not exist. Fixing a
citation here fixes every slide that carries it — 14 works are cited 58 times
across this deck, and before the split each of those 58 was its own copy.

## What the build checks

It refuses to write on an unknown block kind, a `cite:` key with no entry in
`references.yaml`, a named diagram that is not on disk, and a figure a slide
asks for that `assets/figures/` does not hold. It reports figures and
references nothing uses. A `--standalone` build additionally fails if anything
in the finished file still reaches the network.

Only figures a slide actually uses are copied into `build/figures/`, and stale
ones there are deleted, so what the build directory holds is what the deck
needs.

## The standalone build

`--standalone` writes a second file beside the first with the typefaces subset
and inlined, and every figure inlined as a `data:` URI. It opens correctly with
no network and no sibling directory, which is what a deck needs on a machine
that is not the one it was written on. It is roughly 2.8 MB and is the file to
present from.
