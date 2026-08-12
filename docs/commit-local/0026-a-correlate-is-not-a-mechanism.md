# 0026 — A correlate is not a mechanism

| | |
| --- | --- |
| **Commit** | `archive: record what the entropy evidence does not separate` |
| **Scope** | `wiki/concepts/policy-entropy.md` |
| **Kind** | docs |

## What changed

Three sections appended to the manual half of the `policy entropy` note.

The first collects three results already in the archive that each read as a
footnote inside their own paper and bear on the same question when put
together: a random control matching a covariance-targeted one, a token
criterion that turns out to select high- and low-entropy tokens about equally,
and an ablation where the named mechanism accounts for a small part of its
paper's reported gain. The second records that every derivation in this cluster
is a one-step first-order expansion under a tabular-softmax assumption, while
the claims made from them are about trajectories over hundreds of steps. The
third states why this cluster and the archive's expressivity literature do not
currently touch.

No code and no data. The auto block is untouched and the previous analysis
above the new sections is preserved.

## Why it is built this way

**The conclusion exists only in the conjunction, and the manual section is the
only place that can hold it.** Each of the three results is one line inside one
paper's summary, and each paper reports its own without drawing a conclusion
from it, because no paper contains the other two. A per-paper record is the
wrong shape for "these three together mean the evidence is underdetermined".
That is what the preserved half of a wiki note is for.

**It argues against the archive's most-cited result and says so plainly.** The
exchange law `R = -a·exp(H) + b` is this cluster's headline, and the note now
records that its exponential form is fitted rather than derived — the covariance
theorem explains monotone decrease and nothing more. This is not a correction to
the paper, which lists the two as separate contributions. It is a correction to
how the archive had been reading them as one.

**The claim is bounded on purpose.** The section does not say the entropy
account is wrong. It says the archive's evidence does not separate *entropy is
the quantity being controlled* from *entropy is a summary statistic that moves
when something else is controlled*. That is the honest state, and it names the
experiment that would settle it: vary the selection criterion while holding the
reduction in effective gradient fixed.

**It opts into the staleness check.** The section ends with
`<!-- analysis-sources: 4 -->`, so the reporting mechanism from
[template 0021](../commit/0021-report-what-has-gone-stale.md) flags it when this
note reaches a fifth source, and [0025](0025-re-queue-what-the-evidence-outgrew.md)
is what acts on the report. A new source on policy entropy is exactly the event
that should force a re-read, and nothing else in the repository would otherwise
notice.

## Trade-offs and rejected alternatives

- *Put it in the auto block.* Impossible by construction, and wrong regardless:
  the generated definition should say what the sources say, not what a reader
  concluded from reading them against each other.
- *Create a new concept note for it.* Rejected. No source names such an entity,
  and minting one would be the failure that
  [0020](0020-a-placeholder-is-not-a-name.md) exists to prevent, arriving by a
  different route — a wiki entity that exists because someone wanted somewhere
  to write, not because the literature converged on a term.
- *Split it across the three papers' own archive pages.* Rejected twice over:
  `archive/` is regenerated and cleared on every render, and the point does not
  survive being divided into three.
- The cost accepted here: the section reasons about papers that are not sources
  of this note — the token-uniqueness paper and the high-entropy-minority-token
  paper both appear in the argument — so the declared source count understates
  what the analysis actually depends on. The staleness trigger is therefore
  weaker than it looks.

## What a reviewer should check

- The three empirical claims against their sources, because the argument is a
  conjunction and one misreading collapses it: the Rand-Pos-Clip control in
  *Revisiting Entropy*, the 1.03 and 0.99 ratios in *Beyond Entropy*, and the
  2.3 and 1.8 point increments in the *OPEFO* ablation.
- That the new sections sit after the end marker —
  `grep -n 'auto:end' wiki/concepts/policy-entropy.md` — since anything before
  it is deleted by the next render.
- The sentence "no archived paper declares entities from both vocabularies" was
  measured over a hand-chosen pair of vocabulary sets, not proved. A wider set
  could turn up a counterexample, and the structural claim around it would need
  softening if one appeared.

## Downstream impact

None. One wiki note gains a longer manual section; no code, config, template or
schema changes, and nothing regenerates differently.
