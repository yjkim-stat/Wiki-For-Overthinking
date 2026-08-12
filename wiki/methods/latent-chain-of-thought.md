# latent chain of thought

<!-- auto:begin -->

Replacing the discrete tokens of a reasoning trace with continuous states — soft embeddings or hidden states — to cut inference cost or escape the expressiveness limits of token sampling. The sources disagree about what it costs. One asks whether it destroys monitorability and finds task properties and internals access matter more than reasoning mode. Another reports two concrete failure modes, global activation perturbing high-confidence steps and soft embeddings collapsing toward the top token, and gates latent reasoning to low-confidence steps only. A third explains the pattern by identifying decisional certainty as the governing variable, formalized as a Symbolic Index: latent reasoning helps exploration and hurts computation.

- **Kind**: method
- **Also called**: Latent Chain-of-Thought, continuous chain of thought, latent CoT, latent chain-of-thought, soft chain of thought
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [activation probing](activation-probing.md), [AIME 2024](../datasets/aime-2024.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Coconut](coconut.md), [compounding error](../concepts/compounding-error.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [effective depth](../concepts/effective-depth.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [implicit reasoning](../concepts/implicit-reasoning.md), [information bottleneck](../concepts/information-bottleneck.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](linear-probe.md), [Logit Lens](logit-lens.md), [MATH-500](../datasets/math-500.md), [monitorability](../concepts/monitorability.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [QwQ-32B](../models/qwq-32b.md), [self-consistency](self-consistency.md), [soft thinking](soft-thinking.md), [token-level entropy](../concepts/token-level-entropy.md)

## What we have settled

- **Established** — The content of a model's intermediate reasoning tokens is often not what produces its answer: traces can be swapped between problems, or latent thoughts deleted outright, with the answer unchanged.
  - Established causally by two independent papers read together, in settings where the trace can be checked mechanically rather than read. Transformers trained on A* maze traces keep their solution accuracy when trained on traces swapped between instances, with accuracy high at both 0% and 100% swapped and dipping only in the middle. Fine-tuned latent reasoners on ProsQA lose at most 1.0 point when every latent token is deleted, and entity probing shows why -- the target entity dominates their belief from the first latent step, so the model solves the problem in one forward pass and copies the answer through the latent slots. Both were measured on tasks deliberately built to require multi-step or parallel exploration, which is what makes the negative result strong rather than a limitation of the setting. This does not say intermediate tokens never help; it says their helping is not explained by their content.

## Appears in

- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) — Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [SeLaR: Selective Latent Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-320/summary.md) — Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
