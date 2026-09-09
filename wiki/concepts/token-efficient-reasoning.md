# token-efficient reasoning

<!-- auto:begin -->

Reasoning that reaches an answer using fewer tokens without sacrificing accuracy, pursued in the sources by two different routes. DiffAdapt trains a lightweight probe on a reasoning LLM's frozen hidden states to classify each question as Easy/Normal/Hard before generation starts and select a matching fixed prompt/temperature/max-token strategy, cutting token usage by up to 22.4% without retraining the LLM. IAPO instead shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, suppressing uninformative exploration rather than penalizing length in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

- **Kind**: concept
- **Also called**: Token-efficient reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepMath-103K](../datasets/deepmath-103k.md), [DeepSeek-R1-Llama-8B](../models/deepseek-r1-llama-8b.md), [DeepSeek-R1-Qwen-7B](../models/deepseek-r1-qwen-7b.md), [difficulty-adaptive reasoning length](difficulty-adaptive-reasoning-length.md), [GFPO](../methods/gfpo.md), [GPQA](../datasets/gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Qwen3-4B](../models/qwen3-4b.md), [S-GRPO](../methods/s-grpo.md)

## Appears in

- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/local-e8f26d999a2ffe42/summary.md) — Introduces DiffAdapt, a lightweight probe trained on a reasoning LLM's frozen hidden states that classifies each question as Easy/Normal/Hard and, before generation starts, selects a matching fixed prompt/temperature/max-token strategy, cutting token usage by up to 22.4% without retraining the LLM.
- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
