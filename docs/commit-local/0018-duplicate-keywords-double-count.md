# 0018 — Duplicate keywords double-count: a regression from 0014

| | |
| --- | --- |
| **Commit** | `fix(config): drop keywords the matcher already covers` |
| **Scope** | `config/topics/*.yaml` |
| **Kind** | fix · **corrects note 0014** |

## What changed

Twelve keywords were removed across four topics — every entry that an earlier
entry already matches now that the scorer inflects plurals. Also removed: bare
`circuit` from `reasoning-interpretability`.

| Topic | Removed |
| --- | --- |
| reasoning-training | `large reasoning models`, `reasoning models`, `reasoning capabilities`, `verifiable rewards`, `process reward models` |
| reasoning-interpretability | `attention heads`, `sparse autoencoders`, `linear probes`, `internal representations`, and `circuit` |
| reasoning-evaluation | `reasoning benchmarks`, `math word problems` |
| reasoning-faithfulness | `reasoning traces` |

## What went wrong

Note 0014 taught the matcher to inflect a keyword's final word, and said of the
lists that already carried both forms:

> the duplicate entries become redundant but stay harmless, and they still
> widen the arXiv query, which is a reason to leave them.

**They are not harmless.** The scorer counts *distinct matched keywords*, so
after 0014 a single occurrence of "reasoning models" matched both
`reasoning model` and `reasoning models` and scored twice. One abstract mention
went from 0.25 — correctly below the 0.35 bar — to 0.40, which clears it.

The effect was not theoretical. The first real collection after 0014 accepted 94
papers and queued 40. Inspecting them, roughly a third were plainly off-topic
for an archive about LLM reasoning, and the matched-keyword lists named the
cause directly: `['reasoning model', 'reasoning models']`,
`['verifiable reward', 'verifiable rewards']`, `['reasoning benchmark',
'reasoning benchmarks']` — a doubled pair in almost every case. Removing the
duplicates rejects 13 of the 40, and the 13 are the ones a reader would reject
by hand: an analog-circuit design optimizer, a KV-cache eviction scheme, a
music co-creation agent, a physical prompt-injection study on robots.

## Bare `circuit`, and being wrong in the predicted direction

Note 0013 added `circuit` on this reasoning:

> One abstract hit scores 0.25, below the 0.35 bar, so it cannot admit a paper
> on its own — it only carries one over from the title. Circuit papers in this
> field put the word in the title.

The premise held and the conclusion did not, because *other* fields put it in
the title too. It admitted "ORACLE: A Multi-Objective Reinforcement
Learning-Based Analog Circuit Design Optimizer" and "Learning to Rank Tensor
Network Contraction Plans for GPU-Accelerated Quantum Circuit Simulation".
`circuit` is not this field's word; `circuit analysis` and `circuit discovery`
are, and both stay. `reasoning circuit` is added in its place.

## Why it is built this way

**The rule is now single-sourced.** The matcher owns pluralisation; the topic
files list the singular. Before, the two shared responsibility, and sharing it
was what produced the double count. The comment at the top of
`reasoning-training.yaml`, which had told the next maintainer to list both
forms, now says the opposite and points at both notes.

**Redundancy is detectable, so it should not be a matter of vigilance.** A
keyword is redundant exactly when another keyword's compiled pattern fully
matches it. That is three lines to check and is how the twelve were found. It
belongs in the test suite or a config check; it is not there yet, and that gap
is real.

**The arXiv-query argument does not survive contact with the cost.** 0014 kept
the duplicates partly because they widen the query. They do, marginally — and
they also corrupt scoring, which is the thing the keywords exist for.

## Trade-offs and rejected alternatives

- *De-duplicating matched terms inside the scorer instead.* Rejected: it would
  hide a configuration mistake rather than surface it, and a maintainer reading
  a keyword file should be able to predict its behaviour from the file.
- *Raising `min_score` to compensate.* Rejected: it treats a doubled score as if
  it were a threshold problem, and would suppress genuine single-keyword matches
  along with the artefacts.
- *Reverting 0014.* Rejected: the plural fix is correct and the silent misses it
  removed were worse than this. The defect is in the lists, not the matcher.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 173 tests, unchanged.
- No redundancy remains. For each topic, no keyword's compiled pattern should
  fully match another keyword.
- The effect on the queue that prompted this: re-scoring the 40 pending tasks
  accepts 27 and rejects 13, and the 13 should read as obviously off-topic.
- That `circuit analysis`, `circuit discovery` and the new `reasoning circuit`
  survive, so genuine circuit work is still caught.

## Downstream impact

**Scoring becomes stricter for any deployment that listed both forms of a
keyword** — which, if it followed 0014's advice, it may deliberately have done.
Items that were accepted on a doubled score will now be rejected. That is the
correction, but it is a behaviour change: re-check `min_score` and
`data/index/rejected.jsonl` after pulling.

Already-stored records are untouched. A record collected on a doubled score
keeps its topics; the pipeline has no way to say "this was collected in error",
which is a gap worth its own commit.
