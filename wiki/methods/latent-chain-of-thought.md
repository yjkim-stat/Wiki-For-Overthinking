# latent chain of thought

<!-- auto:begin -->

Replacing the discrete tokens of a reasoning trace with continuous states — soft embeddings or hidden states — to cut inference cost or escape the expressiveness limits of token sampling. The sources disagree about what it costs. One asks whether it destroys monitorability and finds task properties and internals access matter more than reasoning mode. Another reports two concrete failure modes, global activation perturbing high-confidence steps and soft embeddings collapsing toward the top token, and gates latent reasoning to low-confidence steps only. A third explains the pattern by identifying decisional certainty as the governing variable, formalized as a Symbolic Index: latent reasoning helps exploration and hurts computation.

- **Kind**: method
- **Also called**: continuous chain of thought, latent CoT, latent chain-of-thought, soft chain of thought
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation probing](activation-probing.md), [chain of thought](chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [compounding error](../concepts/compounding-error.md), [curriculum learning](../concepts/curriculum-learning.md), [effective depth](../concepts/effective-depth.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GSM8K](../datasets/gsm8k.md), [implicit reasoning](../concepts/implicit-reasoning.md), [information bottleneck](../concepts/information-bottleneck.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](linear-probe.md), [monitorability](../concepts/monitorability.md), [self-consistency](self-consistency.md), [token-level entropy](../concepts/token-level-entropy.md)

## Appears in

- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) — Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [SeLaR: Selective Latent Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-320/summary.md) — Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
