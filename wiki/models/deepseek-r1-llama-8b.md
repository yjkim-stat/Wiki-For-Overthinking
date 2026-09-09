# DeepSeek-R1-Llama-8B

<!-- auto:begin -->

DeepSeek-R1-Llama-8B is one of the reasoning-model checkpoints covered by two archived inference-time methods addressing, respectively, safety and token efficiency. ReasoningGuard evaluates it as a target for a training-free jailbreak defense that uses an attention-sink signal to locate the point where reasoning shifts from problem restatement to exploration, injects a 'safety aha' phrase there, and samples multiple continuations to select the one with highest sustained attention to that phrase, at 5-9% extra inference cost while outperforming nine existing defenses. DiffAdapt evaluates it with a lightweight probe trained on its frozen hidden states that classifies each question as Easy/Normal/Hard and selects a matching fixed prompt/temperature/max-token strategy before generation starts, cutting token usage by up to 22.4% without retraining the model.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepMath-103K](../datasets/deepmath-103k.md), [DeepSeek-R1-Qwen-7B](deepseek-r1-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](phi-4-reasoning.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [QwQ-32B](qwq-32b.md), [Sorry-bench](../datasets/sorry-bench.md), [token-efficient reasoning](../concepts/token-efficient-reasoning.md), [XSTest](../datasets/xstest.md)

## Appears in

- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.
- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/local-e8f26d999a2ffe42/summary.md) — Introduces DiffAdapt, a lightweight probe trained on a reasoning LLM's frozen hidden states that classifies each question as Easy/Normal/Hard and, before generation starts, selects a matching fixed prompt/temperature/max-token strategy, cutting token usage by up to 22.4% without retraining the LLM.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
