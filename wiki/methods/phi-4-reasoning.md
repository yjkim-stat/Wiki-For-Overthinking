# Phi-4-reasoning

<!-- auto:begin -->

Phi-4-reasoning is a reasoning language model that archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. GFPO uses it as its sole base model and measures reduction in GRPO's excess length rather than raw length: Shortest-8/16 cuts 23.7%-36.5% across AIME 24/25, GPQA, Omni-MATH and LiveCodeBench, Token Efficiency GFPO cuts 70.9%-84.6%, and Adaptive Difficulty GFPO cuts 35.1%-52.9%, with no statistically significant accuracy difference from GRPO. FROST prunes attention-identified 'reasoning outliers' from its chain of thought and reports GSM8K 93.11% at 154.33 tokens, MATH500 59.80% at 344.37, AIME24 26.67% at 899.80 and Minerva 27.16% at 401.19, alongside a 15.97% drop in maximum attention infinity norm and 91.09% in average kurtosis. Both papers treat it as a reasoning model whose chains are long enough to be worth shortening; neither describes how it was trained.

- **Kind**: method
- **Also called**: Phi-4-Reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DRP](drp.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GFPO](gfpo.md), [GPQA](../datasets/gpqa.md), [GPT-OSS-20B](gpt-oss-20b.md), [group relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [Minerva](../datasets/minerva.md), [Omni-MATH](../datasets/omni-math.md), [Reinforcement Learning with Verifiable Rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [SelfBudgeter](selfbudgeter.md), [Thinkless](thinkless.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
