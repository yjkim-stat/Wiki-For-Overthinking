# Qwen2.5-0.5B

<!-- auto:begin -->

The smallest Qwen2.5 model, used in both sources as the low-capacity end of a comparison. One takes it as the weakest of three scales for sparse-update RLVR experiments. The other uses it as the backbone for a step-level sparse autoencoder and reports a model-family contrast worth noting: on GSM8K its features distribute more evenly across reasoning, calculation and final resolution — with final resolution the most frequent pattern — whereas the similarly sized Llama-3.2-1B devotes 40.4% of its features to reasoning. Its features are also less sparse and more shared between steps (29.01% activation ratio, Jaccard 0.6716) than that model's.

- **Kind**: model
- **Also called**: Qwen2.5-0.5B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPQA](../datasets/gpqa.md), [GPT-4o](gpt-4o.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [linear probe](../methods/linear-probe.md), [linear probing](../methods/linear-probing.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-1B](llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [monosemanticity](../concepts/monosemanticity.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [pass-k](../methods/pass-k.md), [Qwen2.5-1.5B](qwen2-5-1-5b.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [self-verification](../concepts/self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](../concepts/superposition.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.
- [Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability](../../archive/papers/2026/local-85a70e78b4a93190/summary.md) — TRACED scores a reasoning chain by the geometry of its hidden-state trajectory -- net displacement as progress and curvature as stability -- and uses the two as features for a Gaussian classifier that separates correct from incorrect chains without reading the text.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
