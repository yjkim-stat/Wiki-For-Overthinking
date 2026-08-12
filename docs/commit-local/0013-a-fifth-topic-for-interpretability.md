# 0013 — A fifth topic, because two papers had no home

| | |
| --- | --- |
| **Commit** | `config: track reasoning interpretability as a fifth topic` |
| **Scope** | `config/topics/reasoning-interpretability.yaml`, `data/papers/` |
| **Kind** | config · editorial decision |

## What changed

`reasoning-interpretability` joins the four topics from note 0010. It asks what
the computation behind reasoning looks like from the inside: circuits and the
attention heads that carry them, features recovered by sparse dictionary
learning, and the causal interventions used to establish that a component or a
written state matters.

`scripts/retopic.py --topic reasoning-interpretability` then applied it to the
stored archive, which moved five papers. Two of them had **no topic at all** —
the activation-patching methodology paper and the sparse-autoencoder paper —
because they concern language models in general rather than reasoning, and the
reader who filed them declined to force a fit. The archive now has no untopiced
paper.

## Why it is built this way

**The topic was created by evidence, not by taste.** Note 0010 argued that a
topic should be created when the group actually follows a subject, and warned
against splitting a literature into topics that stay empty. This one was not
predicted; it accumulated. Two papers sat unassigned for weeks, and then a
causal-analysis line grew around them — circuit analysis of propositional logic,
arithmetic heuristics, grokked implicit reasoning, counterfactual state editing,
step-level sparse autoencoders, black-box CoT attribution. At that point the two
unassigned papers stopped being orphans and became the methodological
foundations of a line the group is reading. Creating the topic before that would
have been premature; leaving it uncreated now would misdescribe the archive.

**The axis is different from the other four.** Those split by *where reasoning
comes from* — training signal, inference compute, measurement, faithfulness of
the trace. This one is about the substrate rather than the behaviour, which is
why its papers kept failing to fit: a circuit analysis of arithmetic is not a
claim about training, inference or the trace. Adding it as a fifth axis rather
than widening `reasoning-faithfulness` keeps that topic's question intact —
faithfulness asks when a *visible trace* is evidence, and most of this material
has no trace at all.

**`min_score` is 0.35, not the 0.30 used for faithfulness.** That lower bar was
chosen because faithfulness vocabulary is unstandardized and a near-miss was
worth recording. The opposite holds here: "activation patching" and "sparse
autoencoder" are terms of art, so a single clean hit is already a strong signal
and near-misses are mostly noise.

**Bare `circuit` is in the keyword list on purpose.** One abstract hit scores
0.25, below the 0.35 bar, so it cannot admit a paper on its own — it only
carries one over from the title, or alongside a second term. Circuit papers in
this field put the word in the title.

## Trade-offs and rejected alternatives

- *Widening `reasoning-faithfulness` instead.* Rejected above: it would dissolve
  that topic's question, which is specifically about visible traces.
- *Leaving the two papers untopiced.* Rejected: the archive kept them, so it
  should describe them, and an entity that appears in no topic is invisible to
  every generated output.
- *Filing them under a general `interpretability` topic.* Rejected as too wide
  for a group that reads reasoning — it would collect vision and RLHF
  interpretability the group does not follow.
- *Waiting for more papers before creating it.* Rejected: five archived papers
  already match, which is more than `reasoning-evaluation` had when it was
  created.

## What a reviewer should check

- Config parses and every slug matches its filename:
  `python3 -m unittest discover -s tests -t .` — 149 tests, and `RealConfigTests`
  loads the shipped config as-is.
- Which papers it accepts, and that the list is not padded. On this archive:
  activation-patching best practices (0.727), circuit analysis of propositional
  logic (0.75), sparse autoencoders (0.667), step-level sparse autoencoders
  (0.625), arithmetic heuristics (0.40) — and nothing else of 45.
- The known miss, left unfixed on purpose: papers whose abstracts do not use
  interpretability vocabulary do not clear the bar even when they belong —
  grokked implicit reasoning, counterfactual state editing and black-box CoT
  attribution among them. Tuning keywords against 45 papers already in hand is
  how a topic gets overfitted to its own archive; the rejections are recorded in
  `data/index/rejected.jsonl` and are the evidence to widen from later.
- `python3 -m pipelines.render` produces five lecture notes, decks and reports.

## Downstream impact

Adds `outputs/{lecture-notes,slides,reports}/reasoning-interpretability/` and a
fifth note under `wiki/topics/`. Five existing papers gain a slug, so they now
appear in an additional topic's outputs; no paper loses one. Deployments that
copied this repository are unaffected — topics are this deployment's editorial
decision and ship empty.
