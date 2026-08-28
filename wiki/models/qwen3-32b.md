# Qwen3-32B

<!-- auto:begin -->

Qwen3-32B is a backbone used in this archive's study of the faithfulness-safety tension (Risky Business, tested via its QwQ-32B relative) and in DTSR's training-free early-exit sufficiency-assessment framework, which cuts its reasoning length 28.9-34.9% with near-zero accuracy loss and 25-40% lower inference latency.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [DeepScaleR-1.5B-Preview](deepscaler-1-5b-preview.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](../methods/dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [O1-Pruner (baseline)](../methods/o1-pruner-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Phi-4](phi-4.md), [PRM800K](../datasets/prm800k.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-8B](qwen3-8b.md), [QwQ-32B](qwq-32b.md), [ScienceQA](../datasets/scienceqa.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1080/summary.md) — DTSR (Dynamic Thought Sufficiency in Reasoning) is a training-free early-exit framework where the model itself, at each reflection signal ('Wait', 'Alternatively', etc.), evaluates from a third-person perspective whether its own chain-of-thought so far is sufficient to answer, exiting once a self-assessed sufficiency score crosses a threshold, cutting reasoning length 28.9-34.9% with near-zero accuracy loss across Qwen3-8B/14B/32B and five benchmarks, outperforming NoThinking, NOWAIT, and DEER while also cutting inference latency 25-40% (unlike DEER, which reduces length but increases latency).
- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.
- [ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-536/summary.md) — ReProbe is a lightweight (<10M-parameter) transformer probe trained on a frozen LLM's internal states (hidden states, attention, logits) to predict step-level reasoning correctness, matching or exceeding Process Reward Models up to 810x larger for test-time-scaling verification, at 2.6-25x faster inference, and can be trained fully self-supervised (the model annotating its own reasoning) with no human labels or Monte Carlo rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
