# Token Budget

<!-- auto:begin -->

Token budget denotes an explicit cap on how many tokens a reasoning model may spend on a problem, used both as a training target and as an evaluation axis. ARM trains a model to pick among four reasoning formats per task to control token spend; 'How Far Are We from Optimal Reasoning Efficiency?' defines an empirical accuracy-vs-token-budget frontier and measures how far existing methods fall short of it with a single metric (REG); A*-Thought selects a short, high-information subset of a reasoning trace via A* search as SFT data for a fixed token budget; FROST prunes sentence-level reasoning outliers via attention, reporting a 69.68% average token reduction.

- **Kind**: concept
- **Also called**: token budget
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [A*-Thought](../methods/a-thought.md), [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning format selection](../methods/adaptive-reasoning-format-selection.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AQuA-RAT](../datasets/aqua-rat.md), [BBH](../datasets/bbh.md), [Chain-of-Draft](../methods/chain-of-draft.md), [Chain-of-Thought Compression](chain-of-thought-compression.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DRP](../methods/drp.md), [Efficient Reasoning](efficient-reasoning.md), [format collapse](format-collapse.md), [GPQA](../datasets/gpqa.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [OpenBookQA](../datasets/openbookqa.md), [Overthinking](overthinking.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [QwQ-32B](../models/qwq-32b.md), [s1k-1.1](../datasets/s1k-1-1.md), [SelfBudgeter](../methods/selfbudgeter.md), [SimPO](../methods/simpo.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Thinkless](../methods/thinkless.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
