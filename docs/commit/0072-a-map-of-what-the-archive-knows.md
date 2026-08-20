# 0072 — A map of what the archive knows

| | |
| --- | --- |
| **Commit** | `docs: a staged map of reasoning-like behaviour, built from the archive` |
| **Scope** | `docs/reading-a-reasoning-model.html` |
| **Kind** | docs |

## What changed

One self-contained HTML page: a staged account of how LLM reasoning-like
behaviour works, assembled entirely from records already in `data/`. Five parts
— the four prerequisites that had to hold before a reasoning model was possible,
the 2025 pivot, the five branches that grew out of it, the thirteen findings,
and the questions no archived source answers.

## Why it is a document and not an output

`outputs/` is regenerated wholesale by `render`, so anything written there is
deleted on the next pass. This is authored prose about the archive rather than a
projection of it, and `docs/` is where authored documentation lives. It carries
no auto-block and nothing generates it.

That has a cost worth stating: **its numbers go stale silently.** It quotes 268
papers, 202 read, 388 notes, 13 findings, and the year distribution — all true
on 2026-08-14 and all moving. Concept notes have `<!-- analysis-sources: N -->`
for exactly this reason and a page in `docs/` has no equivalent. The provenance
strip at the top is the mitigation: the counts are gathered in one place so a
reader can check them against `migrate status` in a few seconds rather than
discovering the drift mid-argument.

## The design is inherited, not invented

`templates/wiki/graph.html` is this archive's existing design system, and it is a
considered one: a warm paper ground rather than white, three categorical hues
validated for colour-vision deficiency, and the correct three-state theme pattern
where the bare `:root` carries the full light palette and both the media query
and the `[data-theme]` stamp redefine only tokens.

All of it is reused unchanged. The one gap filled is that this page needs to mark
epistemic status rather than entity kind, so the same three hues carry
settled / contested / unknown — under the system's own rule, which is that coral
falls below 3:1 on the light surface and hue may therefore never be the only
channel. Each status also carries a mark shape and the word itself.

Type is the one deliberate departure. The graph page is a tool and sets a system
sans; this is a document, so running prose is a system serif, with sans reserved
for chrome and mono for the figures and paper ids that fill the tables. No
webfont is linked, matching the templates, which link none.

## What it says that the wiki does not

The wiki is organized by entity — one note per concept, each with its own
sources. Nothing in it states the **order**: that verification had to be
separable before bootstrapping was possible, that bootstrapping plus a
complexity-theoretic account of decoding steps is what made an automatic reward
worth building a model around, and that the faithfulness objection was already
on the table two years before the models it now applies to.

Two things the page is careful about:

- **The archive has no o1 paper**, because OpenAI published no technical report
  and the collectors collect papers. The page says so in its second paragraph
  rather than narrating around the gap, and notes what the gap selects for.
- **The year distribution is extreme** — 233 of 268 papers are from 2026, and
  2021–2024 hold thirteen between them. Those thirteen are all anchors, which is
  a consequence of how collection works rather than a fact about the field.

## What a reviewer should check

- Every figure in the page traces to a record in `data/`. The two that were
  wrong on the first pass were citation counts asserted from memory (`8` and
  `AIME/SFT notes`) and are now counted (`7` and `12`).
- No colour is declared outside the token blocks, and `body` sets its background
  from a token — the failure that renders one theme's text on the other's ground.
- The numbered spine appears only in Part 1, where each item is a precondition
  for the next. The five branches are parallel and deliberately unnumbered.
