# TokenSkip

<!-- auto:begin -->

A token-level chain-of-thought compression method listed under 'CoT Compression' in the 'Don't Overthink It' survey's taxonomy, alongside step/chunk- and chain-level pruning or rewriting approaches to shortening a reasoning trace. TRAAC uses it as one of its reinforcement-learning baselines (alongside L1-Max, LC-R1 and AdaptThink) and reports beating it jointly on accuracy and length on AIME/AMC/GPQA-D/BBEH, though the sources give no standalone numbers for TokenSkip itself.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink](adaptthink.md), [BBH (Big Bench Hard)](../datasets/bbh-big-bench-hard.md), [early exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [SuperGPQA](../datasets/supergpqa.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
