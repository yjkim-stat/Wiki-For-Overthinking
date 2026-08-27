# 0101 — A deck becomes source and build

| | |
| --- | --- |
| **Commit** | `refactor(decks): the deck becomes YAML, and the HTML becomes a build product` |
| **Scope** | `decks/`, `outputs/htmls/` (removed), `.gitignore`, `CLAUDE.md` |
| **Kind** | refactor |

## What changed

The 33-slide overthinking deck stops being a 123 KB hand-edited HTML file and
becomes a directory of small YAML files that a build script turns into that
same HTML.

```
decks/
  build.py                     YAML -> HTML, and -> the offline twin
  README.md                    the block vocabulary a slide is written in
  theme/deck.css, deck.js      how every deck looks and navigates
  overthinking/
    deck.yaml                  title, fonts, named styles
    references.yaml            the bibliography, once
    slides/NN-name.yaml        one file per slide, in filename order
    assets/figures/            crops from papers (gitignored, as before)
    assets/diagrams/           the hand-drawn SVGs, one file each
    build/                     generated; gitignored
```

`outputs/htmls/` is gone. Its `build-standalone.py` is folded into
`decks/build.py --standalone`, and `FIGURES.md` moves into the deck it
describes.

The built HTML is **pixel-identical to the file it replaces**: all 33 slides
were screenshotted from both and compared by hash, with the network blocked so
both fell back to the same local faces.

## Why it is built this way

**Editing prose inside 123 KB of markup is the problem being solved.** Changing
one sentence on slide 14 meant finding it among nested `<div>`s carrying inline
styles, and every edit risked the layout of a slide nobody was looking at. A
slide is now its own file of a few dozen lines, and the number in its name is
its position, so moving one is a rename and inserting one is picking a number.
Page numbers in the footer are counted at build time rather than written down,
which is the one piece of bookkeeping that had to be redone by hand on every
reorder.

**The bibliography was 58 copies of 14 works.** Each slide carried its own full
APA string, so correcting a reference meant correcting it everywhere it
appeared and being right about where that was. `references.yaml` holds each
work once and a slide names keys; a key with no entry fails the build. One of
those 58 copies had already gone wrong once — an invented arXiv id, caught by
hand — and that is the class of error this removes.

**The block vocabulary is small on purpose, and has an escape hatch.** Fourteen
kinds — `lead`, `bullets`, `card`, `cards`, `table`, `figure`, `image`, `svg`,
`cond`, `note`, `caption`, `text`, `box`, `html` — cover every one of the 33
slides with nothing left over. They were not designed in advance: the existing
deck was read, its structures counted, and the vocabulary written to fit what
was actually there. `html` and `box` exist so that a layout the vocabulary does
not have a name for still goes in, rather than forcing an invented block kind
for a thing used once.

**Inline styles are kept, not abolished.** The obvious next step is to replace
`style="font-size:17px;"` with CSS classes, and it is deliberately not taken:
the deck has 72 distinct style strings and most are one-offs, so naming them
all would trade a value you can read for a name you have to look up. What
repeats and is long is hoisted into `deck.yaml`'s `styles:` map, which a
`style:` may name instead of spelling out. Slide 14 uses it for the three role
styles its cards each repeat; nothing else needed it.

**A hand-drawn SVG is a file, not a YAML string.** Forty-element diagrams do
not become editable by being quoted, and the one thing that would make them
worse is line-wrapping inside a scalar. They sit in `assets/diagrams/` where an
editor can open them as the SVG they are.

**`--watch` is what makes this an editing setup rather than a build step.**
Leave it running, keep the built file open, and a save is one refresh from the
screen. A failed build prints why and keeps the last good HTML on disk, so a
half-written edit does not blank the browser mid-sentence.

## Trade-offs and rejected alternatives

**The deck can no longer be edited by opening one file.** That is the cost, and
for somebody who wants to change a colour it is a real one: they now need to
know that `theme/deck.css` exists. The build directory is the compensation —
`build/overthinking.html` is still a single file that opens in a browser — but
it is a build product, and an edit made there is destroyed by the next build.

**`decks/` is a new top level rather than a home under `outputs/` or `docs/`.**
[`0100`](0100-the-deck-lands-the-crops-do-not.md) flagged `outputs/htmls/` as
the weakest part of that arrangement: the layout table marks `outputs/` "never
write, regenerated wholesale", and a deck surviving there rested on the
observation that `render` happens not to touch it. Putting a *build directory*
under a tree the pipeline may clear compounds that. `docs/` was the alternative
`0100` named; it is rejected because `docs/commit/` is a numbered history of
the program and a deck is neither. A deck is authored rather than derived, and
that is a third thing.

**Keeping the old file beside the new one** was considered as a safety net and
rejected: two files that must stay in sync and no mechanism to make them,
which is exactly the failure a build step exists to prevent. The screenshot
comparison is the evidence instead, and the old file is one `git show` away.

**The extractor that performed the migration is not committed.** It parsed the
old HTML into the YAML and has no second use — the YAML is the source now, and
re-extraction would mean reading a file that no longer exists.

## What a reviewer should check

- **That the build reproduces the deck.** `git show HEAD~1:outputs/htmls/overthinking.html`
  into a scratch file, `python3 decks/build.py overthinking`, and screenshot
  both. Every slide should hash the same with the network blocked.
- **That the ignore rules still hold.** `python3 decks/build.py overthinking --standalone`
  then `git status --short` should be clean. If the standalone, a PNG, or
  anything under `build/` appears, the rules are wrong and the next `git add -A`
  redistributes crops this repository deliberately does not host.
- **That the build refuses bad input.** Point a slide's `cite:` at a key that
  is not in `references.yaml`, or rename a diagram, and confirm it fails with
  the file named rather than writing a deck with a hole in it.
- **That `render` still ignores the deck.** `python3 -m pipelines.render` twice,
  then confirm `decks/` is untouched. Nothing in the pipeline knows the
  directory exists, which is the intent, but it is worth seeing once.

## Downstream impact

None for the pipeline: no code, config, template or record type changes, and
`tests/` is untouched and passing. A deployment that pulls this gains a
`decks/` directory it can delete and loses `outputs/htmls/`. If it wants the
deck to render, it must supply the figure crops itself — unchanged from
`0100`, and `decks/overthinking/assets/FIGURES.md` still says which paper each
one came from.
