# 0010 — Track LLM reasoning as four topics

| | |
| --- | --- |
| **Commit** | `config: track LLM reasoning as four topics` |
| **Scope** | `config/topics/` |
| **Kind** | config · editorial decision |

## What changed

The first topics in this deployment. Reasoning in large language models, split
along the axis of *where the reasoning comes from* rather than by application:

| Slug | Question it answers | `min_score` |
| --- | --- | --- |
| `reasoning-training` | Which training signal produces reasoning that generalizes, and what it costs | 0.35 |
| `test-time-scaling` | How accuracy trades against tokens spent at inference, and where the curve flattens | 0.35 |
| `reasoning-evaluation` | Which numbers a claim about reasoning can be built on | 0.35 |
| `reasoning-faithfulness` | When a visible reasoning trace is evidence about the model, and when it is only text | 0.30 |

Each narrows arXiv to `cs.CL, cs.LG, cs.AI`, tracks every configured venue, and
generates all three outputs. All four carry seed papers; `authors` and
`keywords.none` are empty everywhere.

## Why it is built this way

**Four topics, not one, and not eight.** One topic would collect correctly but
produce a single lecture note covering training, decoding, benchmarks and
interpretability at once — an output nobody can use for a reading group. Eight
would divide a literature this size into topics that each stay empty for weeks,
and an empty report is worse than a broad one. Four is the point where each
topic still receives papers weekly and each output has a subject.

**The split is by mechanism, not by application.** "Math reasoning" and "code
reasoning" would have been the obvious cut, and it is the wrong one: the same
RLVR paper is evidence for both, so the archive would file it twice and the two
lecture notes would converge on the same content. Training / inference /
measurement / faithfulness are genuinely different claims about a model, and a
paper usually makes one of them.

**Singular and plural are both listed.** Scoring matches on word boundaries, so
`reasoning model` does not match "reasoning models". This is not obvious from
the topic template and it silently halves a keyword's reach. Both forms appear
wherever the plural is what papers actually write.

**Deliberately broad terms are included, and the threshold is what filters
them.** `chain of thought` appears in `reasoning-training` and
`test-time-scaling`. Under the saturating score, one abstract mention is 0.25 —
below every threshold here — so a broad term cannot carry an item on its own;
it only lands one in the archive from the title, or alongside a specific term.
That makes the threshold, not the keyword list, the place where breadth is
tuned, which is the knob that can be changed without re-collecting.

**`reasoning-faithfulness` sits at 0.30.** It is a smaller literature with less
standardized vocabulary, and the archive would rather record a near-miss than
drop it. The arithmetic is unchanged either way — a single abstract hit is 0.25
and still rejected — so 0.30 buys tolerance for the two-weak-hits case, not for
noise.

**`keywords.none` is empty in all four.** An exclusion rule written before
seeing what arrives is a guess. Rejected items are recorded in
`data/index/rejected.jsonl`, which is the evidence to write one from later.

## Trade-offs and rejected alternatives

- *A single `lrm-reasoning` topic, split later.* Rejected: the slug is baked
  into archive paths, so splitting after material accumulates is a migration
  rather than an edit.
- *`keywords.none: [survey]`, as the template illustrates.* Rejected: surveys
  are how a group new to a subject gets oriented, and this archive is starting
  from nothing.
- *Tracked `authors`.* Rejected as premature — an author bonus of 2.0 is a
  strong thumb on the scale, and the group has not decided whose work it wants
  weighted.

## What a reviewer should check

- Config parses and slugs match filenames: `python3 -m unittest discover -s
  tests -t .` — 149 tests pass.
- Scoring behaves on known papers. Offline, against title and abstract:
  DeepSeek-R1 → `reasoning-training`; s1 → `test-time-scaling`;
  "Language Models Don't Always Say What They Think" → `reasoning-faithfulness`;
  GSM8K → `reasoning-evaluation`; "Attention Is All You Need",
  "Diffusion Models Beat GANs" and the RAG paper → rejected by all four.
- Known gap, left unfixed: Minerva ("Solving Quantitative Reasoning Problems
  with Language Models") scores 0.25 and is rejected — its title phrase is not a
  keyword and its benchmark names appear once each. It is the intended shape of
  the tuning loop, not a bug: the miss lands in `rejected.jsonl`, and the fix is
  a keyword added on evidence rather than guessed at now.
- `python3 -m pipelines.render` produces four lecture notes, four decks and four
  reports from an empty `data/`.

## Downstream impact

Creates `outputs/{lecture-notes,slides,reports}/<slug>/` for four slugs on the
next render, and `wiki/topics/` gains four notes. Seed papers are fetched once
on the first run that reaches arXiv and are scored like anything else, so a seed
that does not clear its threshold is simply not archived.
