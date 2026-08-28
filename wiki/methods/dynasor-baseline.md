# Dynasor (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft (baseline)](chain-of-draft-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [NoThinking (baseline)](nothinking-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [SEAL (baseline)](seal-baseline.md)

## Appears in

- [NEAT: Neuron-Based Early Exit for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1231/summary.md) — NEAT identifies a sparse set of 'exit-associated neurons' whose FFN activation dynamics causally predict the </think> termination token, then monitors these neurons training-free during inference to trigger graded early exit or reflection suppression -- cutting average token generation 22-28% across four benchmarks and six models with accuracy comparable to vanilla decoding, and 21-23% real wall-clock latency reduction versus vanilla and CGRS (which is 41-63% slower than vanilla despite shortening output, due to its own scoring overhead).
- [Steering LLM Thinking with Budget Guidance](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1866/summary.md) — Budget guidance adapts diffusion-model classifier guidance to LLM reasoning: a lightweight BERT-based predictor estimates a Gamma distribution over each candidate next token's remaining-thinking-length (from the frozen target LLM's hidden states), and its CDF up to the budget is multiplied elementwise into the LLM's own token distribution -- steering generation smoothly toward a token budget without fine-tuning the LLM or hard-cutting it off, beating budget forcing by up to 26% accuracy on MATH-500 under tight budgets while using 37% fewer thinking tokens, and generalizing across model families, sizes, and out-of-domain tasks despite training only on math data.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
