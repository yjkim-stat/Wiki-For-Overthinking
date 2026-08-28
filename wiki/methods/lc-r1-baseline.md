# LC-R1 (baseline)

<!-- auto:begin -->

LC-R1 is used in these sources as a length-control RL baseline for efficient reasoning: SGP-CoT and SIGMA both compare their own methods' accuracy-length trade-offs against LC-R1 among other RL-based efficient-reasoning baselines; LC-R1's own contribution (elsewhere in this archive) is a dual Length Reward plus Compress Reward GRPO method targeting 'invalid thinking' (redundant post-answer double-checking).

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink (baseline)](adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AMC](../datasets/amc.md), [compression ratio](../concepts/compression-ratio.md), [DAPO (baseline)](dapo-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Direct Preference Optimization (DPO)](direct-preference-optimization-dpo.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [SFT (baseline)](sft-baseline.md)

## Appears in

- [Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-25/summary.md) — SGP-CoT identifies which reasoning units a model can safely drop using only its own intrinsic likelihood signals (counterfactual answer-impact and coherence-impact scores, no external verifier or curated data), then trains the model via preference optimization on self-pruned traces, cutting reasoning length 15-50% across five model families while preserving or improving accuracy -- and shows pruning by a different model consistently degrades accuracy more than self-pruning.
- [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1520/summary.md) — SIGMA reframes token-efficient RL as a classical exploration-exploitation problem: a self-imitation exploitation module prioritizes training on prompts/rollouts with high compression potential via a dynamic priority table and a compression-ratio-weighted self-imitation loss, while a self-guidance exploration module directs otherwise-undirected long-response exploration via prompt-based token-budget regeneration or random truncation -- improving average accuracy by 7.9%/2.9% while cutting average reasoning length 43.4%/40.3% on 1.5B/7B DeepSeek-R1-Distill models across six benchmarks, beating eight RL-based efficient-reasoning baselines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
