# DeepScaleR-1.5B-Preview

<!-- auto:begin -->

DeepScaleR-1.5B-Preview is a 1.5B reasoning-model checkpoint used in this archive by LC-R1 (Optimizing Length Compression in Large Reasoning Models) as a post-RL backbone to validate that its 'invalid thinking' compression generalizes beyond directly-trained models, and cited in a separate empirical study of reasoning length and correctness that finds models overthink easy questions and underthink hard ones.

- **Kind**: model
- **Also called**: DeepScaler-1.5B-Preview
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [DeepScaler (training)](../datasets/deepscaler-training.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](../methods/dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5](gpt-5.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [O1-Pruner (baseline)](../methods/o1-pruner-baseline.md), [o3-mini](o3-mini.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-32B](qwen3-32b.md), [QwQ-32B](qwq-32b.md), [s1-32B](s1-32b.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.
- [Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1878/summary.md) — MathIF is a 420-query, 15-constraint controlled benchmark showing that as large reasoning models' chain-of-thought grows longer via reasoning-oriented SFT/RL, their instruction-following obedience degrades -- even the best open model (Qwen3-14B) satisfies only 50.71% of constraints strictly, and artificially lengthening CoT (budget forcing) or reasoning-oriented training both directly and measurably erode compliance, exposing a persistent intelligence-obedience trade-off.
- [Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs](../../archive/papers/2025/local-6afb006d68240134/summary.md) — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
