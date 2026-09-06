# DeepMath-103K

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DeepSeek-R1-Llama-8B](../models/deepseek-r1-llama-8b.md), [DeepSeek-R1-Qwen-7B](../models/deepseek-r1-qwen-7b.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [MATH500](math500.md), [Minerva](minerva.md), [MMLU-Pro](mmlu-pro.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-4B](../models/qwen3-4b.md), [sparse autoencoders (SAEs)](../methods/sparse-autoencoders-saes.md), [token-efficient reasoning](../concepts/token-efficient-reasoning.md)

## Appears in

- [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](../../archive/papers/2026/local-4c4d1944c8091d55/summary.md) — Trains Top-K sparse autoencoders on the residual stream of DeepSeek-R1-Distill-Qwen-7B to contrast the internal feature dynamics of explicit chain-of-thought (Thinking) against direct answer generation (NoThinking), finding Thinking relies on a sparse, high-intensity, difficulty-invariant feature regime while NoThinking uses a diffuse, difficulty-adaptive one, and that causally suppressing Thinking's dominant features degrades formatting and triggers compensatory, less informative verbosity rather than a clean shortening of the trace.
- [DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference](../../archive/papers/2026/local-e8f26d999a2ffe42/summary.md) — Introduces DiffAdapt, a lightweight probe trained on a reasoning LLM's frozen hidden states that classifies each question as Easy/Normal/Hard and, before generation starts, selects a matching fixed prompt/temperature/max-token strategy, cutting token usage by up to 22.4% without retraining the LLM.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
