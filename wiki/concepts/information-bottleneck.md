# information bottleneck

<!-- auto:begin -->

Constraining how much information a representation may carry, so that what survives is the part that matters. One source makes it the design principle of a step-level sparse autoencoder: a sparsity target plus injected noise bounds the channel, and because the decoder can already read the preceding context, what the bottleneck admits is the step's incremental contribution rather than its inherited background. The other invokes it as part of the information-theoretic framing in which reasoning is tracked by mutual information between representations and the answer.

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [budget forcing](../methods/budget-forcing.md), [chain of thought](../methods/chain-of-thought.md), [compounding error](compounding-error.md), [curriculum learning](curriculum-learning.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [effective depth](effective-depth.md), [epistemic verbalization](epistemic-verbalization.md), [GSM8K](../datasets/gsm8k.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [linear probing](../methods/linear-probing.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [monosemanticity](monosemanticity.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](reasoning-trajectory.md), [self-consistency](../methods/self-consistency.md), [self-correction](self-correction.md), [self-verification](self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](superposition.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
