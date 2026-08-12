# compounding error

<!-- auto:begin -->

The accumulation of small per-step inaccuracies over a multi-step rollout, which both sources identify as the limit on reasoning in latent space specifically. One introduces a higher-level abstract latent so that a coarser prediction over a longer span replaces a chain of fine-grained ones, on the argument that existing multi-token and next-latent objectives either have too short a horizon or accumulate error. The other explains the same limitation by identifying decisional certainty as the governing variable, formalized as a Symbolic Index, and concludes that latent reasoning is good at exploration and bad at computation. Both treat the error as structural to the latent rollout rather than a shortfall of scale.

- **Kind**: concept
- **Also called**: drift, error accumulation, error propagation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [belief state](belief-state.md), [chain of thought](../methods/chain-of-thought.md), [curriculum learning](curriculum-learning.md), [effective depth](effective-depth.md), [GSM8K](../datasets/gsm8k.md), [implicit reasoning](implicit-reasoning.md), [information bottleneck](information-bottleneck.md), [latent chain of thought](../methods/latent-chain-of-thought.md), [latent reasoning](latent-reasoning.md), [self-consistency](../methods/self-consistency.md), [speculative decoding](../methods/speculative-decoding.md), [teacher forcing](../methods/teacher-forcing.md)

## Appears in

- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [Capabilities and Fundamental Limits of Latent Chain-of-Thought](../../archive/papers/2026/local-6b66615b7bf3ef86/summary.md) — Explains why latent chain-of-thought excels at exploration but fails at computation by identifying decisional certainty as the governing variable, formalizing it as the Symbolic Index, and proving that curriculum learning is not merely helpful but necessary for training latent reasoners.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
