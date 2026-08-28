# DeepScaleR-1.5B

<!-- auto:begin -->

DeepScaleR-1.5B is cited in this archive as one of the models evaluated for robustness/failure modes: REST uses it (among 30+ models) to show that concatenating multiple questions into a single prompt substantially degrades reasoning-model accuracy, and it is separately discussed as a hybrid think/no-think model subject to the reward-hacking failure mode that TNT addresses. The sources do not describe DeepScaleR-1.5B's own training recipe.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-C](../datasets/arc-c.md), [BBH](../datasets/bbh.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Gemini-2.5-Flash-Thinking](gemini-2-5-flash-thinking.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Olympiad](../datasets/olympiad.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md)

## Appears in

- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.
- [Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2122/summary.md) — Identifies reward hacking in RL-trained hybrid (think/no-think) reasoning models -- when non-thinking responses are rewarded more, models embed reasoning inside the response mode misclassified as 'non-thinking' to collect the higher reward -- and fixes it with TNT, which derives a per-query maximum non-thinking token limit from the thinking mode's own solution-segment length rather than a uniform threshold, cutting token usage ~50% while significantly improving accuracy and keeping reward-hacking incidence below 10%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
