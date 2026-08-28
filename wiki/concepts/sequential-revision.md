# Sequential revision

<!-- auto:begin -->

Sequential revision denotes generating an answer, then revising it in further generation steps, as opposed to sampling independent parallel attempts. REA-RL trains online with a distilled reflection model supplying both parallel samples and truncated sequential revisions plus a reflection-density reward, cutting response length about 36% without losing accuracy; the second source proves plain best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

- **Kind**: concept
- **Also called**: Sequential revision, sequential revision
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [Best-of-N (BoN) sampling](../methods/best-of-n-bon-sampling.md), [Best-of-N sampling](../methods/best-of-n-sampling.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Length reward](length-reward.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Test-Time Compute](test-time-compute.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-474d6c4d88a30199/summary.md) — REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.
- [On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference](../../archive/papers/2026/title-cd5c62ac6be53cbc/summary.md) — Proves standard best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
