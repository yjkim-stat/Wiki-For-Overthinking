<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation

- **Authors**: Abdallah Khemais
- **Venue**: cs.LG
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03620>
- **PDF**: <https://arxiv.org/pdf/2608.03620v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Activation patching and weight-space ablation both claim a component is causally responsible for a behavior, yet they act on different objects: one forward pass versus the parameters behind every forward pass. We ask when they agree. We study an idealized model where a conditional computation is carried additively through a residual stream, $F(x)=F_0(x)+\sum_iα_i(x)v_i$, read out by a linear functional, and prove three exact results. First, deleting a subset of carriers collapses a matched input pair onto the same unconditional output \emph{if and only if} the removal is symmetric on the pair and leaves no outside contrast; the error is deterministic, and we give its exact form even when the two conditions hold only approximately. Second, patching a carrier moves the readout by its donor-receiver \emph{contrast}, while ablating it moves the readout by its \emph{absolute level}; neither bounds the other, and we construct pairs where every single-carrier patch flips the decision while no single-carrier ablation does. Third, for an attention head composed with its own layer's normalization and MLP, we derive an exact first-order interaction formula with a provably second-order remainder, vanishing identically when only the MLP is ablated but not, in general, when a head is. Small transformers trained on a synthetic conditional task illustrate all three predictions: across thirty-nine ablation configurations the measured interaction is strongly rank-correlated with the idealized model's predictive accuracy (Spearman $-0.83$), and a second task and architecture reproduces the same pattern, including a further polarity reversal. The single-block interaction result extends past one residual block, and the synthetic validation is tested against a real pretrained model, in a companion paper that takes this theory further along both axes.

---

Record id: `arxiv:2608.03620`
