# GPT-2

<!-- auto:begin -->

A small autoregressive language model, used in both sources as the scale at which latent chain-of-thought is trained from scratch rather than as a subject of study. That role matters for how their results should be read: one validates its whole theory of latent reasoning at 124M parameters with six latent steps, which is far below any deployed reasoning model and gives correspondingly low absolute accuracies (42.9% for explicit chain of thought on GSM8K). The other uses it as one of four checkpoints in the fine-tuned regime, where deleting every latent token changes accuracy by at most 1.0 point — 99.0 to 99.0 here. It appears in this archive because latent-reasoning curricula are cheap enough to train at this size and not at any other.

- **Kind**: model
- **Also called**: GPT2
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [compounding error](../concepts/compounding-error.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [effective depth](../concepts/effective-depth.md), [entropy collapse](../concepts/entropy-collapse.md), [GSM8K](../datasets/gsm8k.md), [information bottleneck](../concepts/information-bottleneck.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [logit lens](../methods/logit-lens.md), [MATH500](../datasets/math500.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [QwQ-32B](qwq-32b.md), [self-consistency](../methods/self-consistency.md), [soft thinking](../methods/soft-thinking.md)

## Appears in

- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
