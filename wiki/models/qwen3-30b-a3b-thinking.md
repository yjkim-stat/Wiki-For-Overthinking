# Qwen3-30B-A3B-Thinking

<!-- auto:begin -->

Qwen3-30B-A3B-Thinking is one of the reasoning-model checkpoints covered by two archived inference-time methods for large reasoning models. Latent Exploration Decoding evaluates it under a method that restores lost pass@n exploration in RL-post-trained reasoning models by aggregating hidden-state posteriors from multiple depths and sampling from whichever depth's aggregated posterior has maximal entropy, with no extra training or parameters. PUMA evaluates it under an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [answer convergence](../concepts/answer-convergence.md), [Concise CoT (CCoT)](../methods/concise-cot-ccot.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Latent Exploration Decoding (LED)](../methods/latent-exploration-decoding-led.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [pass@n](../concepts/pass-n.md), [PLAN-AND-BUDGET](../methods/plan-and-budget.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking](qwen3-4b-thinking.md), [QwQ-32B](qwq-32b.md)

## Appears in

- [Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models](../../archive/papers/2026/local-5680089130af21f6/summary.md) — Restores lost pass@n exploration in RL-post-trained reasoning models by aggregating hidden-state posteriors from multiple depths and sampling from whichever depth's aggregated posterior has maximal entropy, with no extra training or parameters.
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](../../archive/papers/2026/local-8ec022e440eb9021/summary.md) — Proposes PUMA, an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
