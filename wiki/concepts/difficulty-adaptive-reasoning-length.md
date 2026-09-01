# difficulty-adaptive reasoning length

<!-- auto:begin -->

Difficulty-adaptive reasoning length is the principle that a reasoning model's token budget or exploration effort should scale with a query's actual difficulty rather than being applied uniformly. The LALM (audio) difficulty-adaptive paper operationalizes this via GRPO reward variants (GRDR, GA2DR) that scale a length reward by rollout-accuracy- or attention-entropy-derived difficulty, cutting reasoning length over 50% while improving accuracy; REA-RL applies a related idea via a distilled reflection model supplying parallel samples and truncated sequential revisions plus a reflection-density reward, cutting response length ~36% without losing accuracy.

- **Kind**: concept
- **Also called**: Difficulty-adaptive reasoning length
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Length reward](length-reward.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Sequential revision](sequential-revision.md), [SFT (baseline)](../methods/sft-baseline.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1640/summary.md) — Extends difficulty-adaptive reasoning-length control from text LLMs to Large Audio Language Models (LALMs), diagnosing that GRPO helps hard audio questions but SFT wins on easy ones (implying GRPO's reasoning on simple tasks is redundant/error-prone), then proposing two GRPO reward variants -- an outcome-based Group Ratio Difficulty Reward (GRDR) and a process-based, audio-attention-entropy-derived Group Audio Attention Difficulty Reward (GA2DR) -- that cut average reasoning length over 50% while improving accuracy, with GA2DR proving more robust to reward hacking because its difficulty signal is normalized per-batch from audio attention rather than from noisy rollout accuracy.
- [REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-474d6c4d88a30199/summary.md) — REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
