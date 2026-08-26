# AutoThink

<!-- auto:begin -->

A three-stage reinforcement-learning curriculum with stage-wise reward shaping that teaches R1-style distilled models to decide, per problem, whether to emit an explicit reasoning chain at all. Sources place it in the adaptive-mode family beside AdaptThink, ARM and Thinkless and distinguish them by what each needs to keep the modes from collapsing onto one: AutoThink's answer is the multi-stage curriculum, where ARM and Thinkless pre-install the modes with a supervised or distillation stage and AdaptThink uses importance sampling under a constrained objective. It is cited here as a member of that family rather than evaluated.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DAPO](dapo.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [Dr. GRPO](dr-grpo.md), [GPQA](../datasets/gpqa.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Reward Shaping](../concepts/reward-shaping.md), [RLVR](rlvr.md), [routing collapse](../concepts/routing-collapse.md), [Test-Time Compute](../concepts/test-time-compute.md), [Thinkless](thinkless.md)

## Appears in

- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL](../../archive/papers/2025/title-0bc5d9b198744bed/summary.md) — AutoThink uses a three-stage RL curriculum with stage-wise reward shaping to teach R1-style distilled models to decide per problem whether to emit an explicit reasoning chain at all.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
