<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR

- **Authors**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- **Venue**: cs.LG
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11368>
- **PDF**: <https://arxiv.org/pdf/2608.11368v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement learning with verifiable rewards (RLVR) spends most of its compute generating groups of long reasoning trajectories. Recent allocators reduce this cost by assigning budgets to prompts, rollouts, or tokens according to a pointwise notion of difficulty or utility. We identify a statistical mismatch: the unclipped leave-one-out group-relative score gradient is not a sum of independent point contributions, but a second-order U-statistic over pairs of rollouts. Completing one rollout therefore reveals contrast with every other completed rollout, and adaptive endpoint selection changes which pair terms are observable. We introduce PAIR (Pairwise-Aware Inclusion Reweighting), which treats short rollout prefixes as vertices and pair-gradient terms as edges of a contrast graph. A prefix-only predictor estimates correctness and remaining token cost; a convex design chooses positive continuation probabilities under an expected suffix-token budget; and each edge induced by completed vertices is inverse-weighted by its logged joint inclusion probability. Under conditionally independent on-policy rollouts and an unclipped, unstandardized objective, the resulting estimator is design-unbiased for the complete candidate-pair gradient. Across compute-matched RLVR runs on Qwen3-1.7B/4B, PAIR improves average accuracy by +1.2 and +1.4 over the strongest pointwise allocator while using 51% and 52% fewer generated tokens than full-group GRPO. A frozen-population estimator audit confirms that unweighted adaptive selection is biased, whereas pair-inclusion correction recovers the complete-pair target at matched suffix cost.

---

Record id: `arxiv:2608.11368`
