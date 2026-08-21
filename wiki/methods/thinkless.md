# Thinkless

<!-- auto:begin -->

None of the three sources describe Thinkless's own mechanism; it appears as a named comparison point. QLPO instead over-generates rollouts per prompt and resamples the training group to favour short-correct and long-incorrect trajectories, shortening outputs 30-70% relative to GRPO at roughly unchanged accuracy; the survey places Thinkless within its taxonomy of efficient R1-style methods; FROST prunes attention-identified sentence-level reasoning outliers, reporting 69.68% average token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

- **Kind**: method
- **Also called**: ThinkLess
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [A*-Thought](a-thought.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AutoThink](autothink.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO](dapo.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DEER](deer.md), [Dr. GRPO](dr-grpo.md), [DRP](drp.md), [Early Exit](early-exit.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA](../datasets/gpqa.md), [GPT-OSS-20B](gpt-oss-20b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Phi-4-reasoning](phi-4-reasoning.md), [PLAN-AND-BUDGET](plan-and-budget.md), [RLVR](rlvr.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [ThinkPrune](thinkprune.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md), [veRL](verl.md)

## Appears in

- [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](../../archive/papers/2026/arxiv-2607-21793/summary.md) — QLPO is a GRPO variant that leaves the reward, advantage estimator and update untouched and instead over-generates K=16 rollouts per prompt and resamples the M=8 training group to favour short-correct and long-incorrect trajectories, which shortens outputs by 30-70% relative to GRPO at roughly unchanged accuracy.
- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
