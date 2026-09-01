# LLaMA-3-8B-Instruct

<!-- auto:begin -->

LLaMA-3-8B-Instruct is used as a base reasoning model in a systematic comparison of 8 prompting strategies under equal sampling budget for majority-vote test-time scaling (finding plain Chain-of-Thought eventually dominates every other strategy), and as one of the reasoning models evaluated with DREAM's dual-phase reward-guided search framework.

- **Kind**: model
- **Also called**: LLaMA-3-8B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [AMC23](../datasets/amc23.md), [ASDiv](../datasets/asdiv.md), [Chain-of-Thought (CoT)](../methods/chain-of-thought-cot.md), [Direct Prompting](../methods/direct-prompting.md), [GPQA](../datasets/gpqa.md), [GPT-4o-mini](gpt-4o-mini.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [majority voting / self-consistency](../methods/majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [Multi-Agent Debate](../methods/multi-agent-debate.md), [Process Reward Model (PRM)](../concepts/process-reward-model-prm.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-Math-1.5B-Instruct](qwen2-5-math-1-5b-instruct.md), [self-refine](../methods/self-refine.md)

## Appears in

- [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1356/summary.md) — Systematically compares 8 prompting strategies under equal sampling budget for majority-vote test-time scaling across 6 LLMs x 6 benchmarks, finding plain Chain-of-Thought eventually dominates every more elaborate strategy as sampling time N grows -- because CoT has more easy/fewer hard questions and a flatter wrong-answer distribution -- and shows combining per-question difficulty-adaptive scaling with per-question optimal-strategy selection lifts GSM8K accuracy from 86.0% to 97.4% (Majority@10) and MATH-500 from 15.2% to 61.0%.
- [A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-511/summary.md) — DREAM decomposes tree-based test-time search into separate planning and execution phases, each with its own reward model and adaptive per-step budget allocation, improving the accuracy-tokens tradeoff over standard beam search and majority voting on math reasoning and code generation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
