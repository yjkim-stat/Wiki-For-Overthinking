# information bottleneck

<!-- auto:begin -->

A constraint on how much information a representation may carry about its input while preserving what predicts the output, appearing across 3 sources as the frame for what a compressed reasoning state can hold. Its uses: bounding what latent chain of thought can achieve, since a continuous state of fixed width is a channel with a capacity; measuring reasoning dynamics by mutual information between intermediate states and the answer, which is what identifies thinking tokens as information peaks; and structuring a step-level decomposition. The archive's related material supplies the empirical counterpart -- a reasoning trace and its answer are separate information channels, and content present in one can be absent from the other in both directions.

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [budget forcing](../methods/budget-forcing.md), [chain of thought](chain-of-thought.md), [Coconut](../methods/coconut.md), [compounding error](compounding-error.md), [curriculum learning](../methods/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [effective depth](effective-depth.md), [epistemic verbalization](epistemic-verbalization.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [latent chain of thought](latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.3-70B-Instruct](../models/llama-3-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [monosemanticity](monosemanticity.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](reasoning-trajectory.md), [self-consistency](../methods/self-consistency.md), [self-correction](self-correction.md), [self-verification](self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](superposition.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning](../../archive/papers/2025/local-2c3407071e27c9d6/summary.md) — Tracks mutual information between each reasoning step's representation and the correct answer, finds it spikes at sparse 'MI peaks' that decode to reflective tokens like 'Wait' and 'Hmm', and shows suppressing exactly those tokens degrades reasoning while suppressing equally many others does not.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
