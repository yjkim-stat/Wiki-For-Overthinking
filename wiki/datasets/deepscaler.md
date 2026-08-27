# DeepScaleR

<!-- auto:begin -->

In all three citing sources DeepScaleR is a math corpus for reinforcement-learning training and evaluation, not a method: REO-RL trains on 135k problems drawn from DeepScaleR and AReaL, and REA-RL and QuRL both list it among their datasets, with QuRL reporting a DeepScaleR average of 56.40% for the BF16 actor against 55.48% for INT8 rollouts. The name is ambiguous across the wider archive, where DeepScaleR-1.5B-Preview denotes an RL-tuned 1.5B reasoning model used as a base model and as an efficiency-evaluation subject, so a reader should check which of the two a paper means. No archived source describes how the dataset was constructed or how large it is on its own.

- **Kind**: dataset
- **Also called**: DeepScaler
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DAPO-Math-17K](dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Length reward](../concepts/length-reward.md), [MATH500](math500.md), [Minerva](minerva.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Sequential revision](../concepts/sequential-revision.md), [SimPO](../methods/simpo.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-474d6c4d88a30199/summary.md) — REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
