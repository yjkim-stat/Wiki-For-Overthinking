# LC-R1

<!-- auto:begin -->

A chain-level chain-of-thought compression method, categorized under 'CoT Compression' in the 'Don't Overthink It' survey's taxonomy, that trains a reasoning model to produce shorter chains of thought using a reward focused on the model's '</think>' token. TRAAC uses it as one of its reinforcement-learning baselines (alongside TokenSkip, L1-Max and AdaptThink) and reports beating it jointly on accuracy and length on AIME/AMC/GPQA-D/BBEH, though the sources give no standalone numbers for LC-R1 itself.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [BBH (Big-Bench Hard)](../datasets/bbh-big-bench-hard.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAST](dast.md), [DEER](deer.md), [DRP](drp.md), [Early Exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [Laser](laser.md), [Manifold Steering](manifold-steering.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [SuperGPQA](../datasets/supergpqa.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## What we have settled

- **Established** — LC-R1 has an official public code release at github.com/zxiangx/LC-R1.
  - Checked the repository directly; it is the paper authors' own implementation of the GRPO-based length-compression method for large reasoning models.

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.

## Checked against

- [https://github.com/zxiangx/LC-R1](https://github.com/zxiangx/LC-R1) — github.com · code · retrieved 2026-08-21
  - _This repository contains the official implementation for the paper 'Optimizing Length Compression in Large Reasoning Models' -- a novel post-training method to compress the lengthy reasoning process of Large Reasoning Models (LRMs)._

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
