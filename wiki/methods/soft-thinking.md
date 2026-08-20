# soft thinking

<!-- auto:begin -->

Feeding a probability-weighted mixture of token embeddings back into the model instead of a sampled discrete token, so a step can carry a distribution rather than a choice. The two sources use it at opposite ends of the same question. One builds on it deliberately, injecting Gumbel noise into the logits before the mixture so that latent thoughts differ across rollouts and can be credited separately. The other tests whether it does anything at all on models not trained for it, and finds it does not: on three off-the-shelf checkpoints the layer-wise entropy profiles of soft and discrete decoding coincide and the KL divergence between their states reaches about 1e-4, because a superposed input collapses to a single token within a few layers. Whether the technique is a mechanism or a no-op therefore depends on whether the model was trained to use it.

- **Kind**: method
- **Also called**: Soft Thinking, soft tokens
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [causal intervention](../concepts/causal-intervention.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Coconut](coconut.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [GPT-2](../models/gpt-2.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [latent chain of thought](latent-chain-of-thought.md), [latent reasoning](../concepts/latent-reasoning.md), [logit lens](logit-lens.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-STEM](../datasets/mmlu-stem.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [QwQ-32B](../models/qwq-32b.md), [REINFORCE](reinforce.md)

## Appears in

- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
