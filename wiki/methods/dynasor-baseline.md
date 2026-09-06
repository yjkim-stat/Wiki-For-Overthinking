# Dynasor (baseline)

<!-- auto:begin -->

Dynasor(-CoT) is used in these sources as a training-free early-stopping baseline: NEAT and Budget Guidance both compare their own inference-time length-control mechanisms against Dynasor among other training-free baselines, generally finding it a competitive but less accuracy-preserving or less budget-adherent alternative to their proposed methods.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft (baseline)](chain-of-draft-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [difference-in-means direction extraction](difference-in-means-direction-extraction.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [NoThinking (baseline)](nothinking-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [SEAL (baseline)](seal-baseline.md)

## Appears in

- [NEAT: Neuron-Based Early Exit for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1231/summary.md) — NEAT identifies a sparse set of 'exit-associated neurons' whose FFN activation dynamics causally predict the </think> termination token, then monitors these neurons training-free during inference to trigger graded early exit or reflection suppression -- cutting average token generation 22-28% across four benchmarks and six models with accuracy comparable to vanilla decoding, and 21-23% real wall-clock latency reduction versus vanilla and CGRS (which is 41-63% slower than vanilla despite shortening output, due to its own scoring overhead).
- [Steering LLM Thinking with Budget Guidance](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1866/summary.md) — Budget guidance adapts diffusion-model classifier guidance to LLM reasoning: a lightweight BERT-based predictor estimates a Gamma distribution over each candidate next token's remaining-thinking-length (from the frozen target LLM's hidden states), and its CDF up to the budget is multiplied elementwise into the LLM's own token distribution -- steering generation smoothly toward a token budget without fine-tuning the LLM or hard-cutting it off, beating budget forcing by up to 26% accuracy on MATH-500 under tight budgets while using 37% fewer thinking tokens, and generalizing across model families, sizes, and out-of-domain tasks despite training only on math data.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/local-1da36a797481ea8a/summary.md) — A training-free residual-stream steering method that mitigates overthinking by projecting a difference-in-means 'overthinking direction' onto a low-dimensional PCA manifold of the model's activations before ablating it, removing the accuracy-degrading interference noise that limits naive single-direction steering.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
