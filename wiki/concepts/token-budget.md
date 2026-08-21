# Token Budget

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Also called**: token budget
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [A*-Thought](../methods/a-thought.md), [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [BIG-Bench Hard](../datasets/big-bench-hard.md), [Chain-of-Draft](../methods/chain-of-draft.md), [chain-of-thought compression](chain-of-thought-compression.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DeepScaleR](../datasets/deepscaler.md), [DRP](../methods/drp.md), [Efficient Reasoning](efficient-reasoning.md), [GPQA](../datasets/gpqa.md), [GPT-OSS-20B](../methods/gpt-oss-20b.md), [Group-Relative Policy Optimization](../methods/group-relative-policy-optimization.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [Minerva](../datasets/minerva.md), [Minerva Math](../datasets/minerva-math.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [QwQ-32B](../methods/qwq-32b.md), [s1K-1.1](../datasets/s1k-1-1.md), [SelfBudgeter](../methods/selfbudgeter.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [test-time compute scaling](test-time-compute-scaling.md), [Thinkless](../methods/thinkless.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
