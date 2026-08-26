# 0100 — The deck lands, the crops do not

| | |
| --- | --- |
| **Commit** | `docs(outputs): a hand-written deck, without the figures it cites` |
| **Scope** | `outputs/htmls/`, `.gitignore` |
| **Kind** | docs |

## What changed

A 33-slide Korean-language presentation on overthinking in reasoning models
enters the repository, together with the script that turns it into a single
self-contained file. The 25 figure and equation crops it cites do **not** enter,
and neither does the standalone build, which carries the same images inlined as
`data:` URIs. Both are now gitignored.

What lands:

- `overthinking.html` — the deck. Prose, hand-drawn SVG diagrams, per-slide APA
  citations. Its `<img src="figures/…">` references resolve to nothing in a
  fresh clone.
- `build-standalone.py` — subsets the Korean typefaces to the glyphs the deck
  uses, inlines them and every figure, strips the Google Fonts links, and writes
  the offline twin. It needs the crops to run.
- `FIGURES.md` — one row per crop: which paper it came from, its arXiv id, which
  slide uses it, and the caption the deck gives it.

## Why it is built this way

**The deck is committed because it is the one thing under `outputs/` a rebuild
cannot bring back.** Everything else there is a pure function of `data/`;
this is hand-written prose and hand-drawn diagrams. The container is ephemeral,
so uncommitted means lost.

**The crops are not committed because this repository is public and they are not
ours.** `data/pdfs/` is already untracked, and one of the stated reasons is that
the documents are not ours to redistribute. A cropped figure is the same
material one step removed, and pushing it to a public remote is hosting it
rather than citing it. Every slide carries an APA reference and a link, which is
what a talk owes its sources — but citation is not a licence, this repository
carries no licence file of its own, and the papers involved span arXiv's
non-exclusive terms and several Creative Commons variants that were not checked
one by one. The consistent answer is the one `data/pdfs/` already gives.

**The standalone file goes with them.** It is the artifact that matters at
presentation time — a deck that renders in the room it was written in and shows
empty boxes in the room it is presented in has failed at the only moment that
counts — but it embeds every crop as a `data:` URI, so committing it would
redistribute exactly what excluding `figures/` refuses to. Ignoring one and not
the other would have been a rule that looks enforced and is not.

**`FIGURES.md` exists because exclusion destroys provenance.** Without it a
clone holds a deck whose images are missing and no record of what they were.
With it, each crop names its paper, so the archive can re-fetch the document
and the figure can be found again.

## Trade-offs and rejected alternatives

**A fresh clone gets a deck with broken images, and cannot repair it
automatically.** The crops were taken with PyMuPDF page clips at raised DPI, and
the clip rectangles were chosen by eye and recorded nowhere. Retaking a figure
means locating it in the PDF by hand. Storing the rectangles alongside
`FIGURES.md` would have made the deck reproducible from `data/pdfs/` and was not
done — the coordinates no longer exist to write down. Anyone re-cropping should
record them this time.

**Committing everything and accepting the licensing risk** was the alternative,
and it is what the first draft of this commit did. Rejected on the grounds that
the repository is public, has no licence, and is copied into other projects,
so the risk would propagate to people who never chose it.

**Keeping the deck out entirely** was the other end. Rejected because the prose
and diagrams are the work; the crops are quotation.

**`outputs/htmls/` is a directory the layout table marks "never write".** That
table is about the pipeline's own output trees, each regenerated per topic;
`render` writes into those paths and has left this one alone across repeated
runs. That is an observation about current behaviour, not a guarantee the layout
offers, and it is the weakest part of the arrangement. `docs/` would be a safer
home and remains the obvious migration.

## What a reviewer should check

- **That the ignore rules actually hold.** `git status --short` after a
  `build-standalone.py` run should be clean — if the standalone or any PNG shows
  up, the rule is wrong and the next `git add -A` redistributes them.
- **That a render does not delete the deck.** `python3 -m pipelines.render`
  twice, then confirm `outputs/htmls/overthinking.html` still exists. This is the
  assumption the placement rests on.
- **That `FIGURES.md` names the right papers.** The arXiv ids there were taken
  from the archive's own records rather than from memory; one in an earlier draft
  was wrong. Spot-check two against `data/papers/`.

## Downstream impact

None for the pipeline: no code, config, template or record type changes, and
nothing reads `outputs/htmls/`. A deployment that pulls this gains a deck it can
delete and two ignore rules. If it wants the deck to render, it must supply the
crops itself — and should make its own licensing decision rather than inherit
this one.
