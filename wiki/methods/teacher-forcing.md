# teacher forcing

<!-- auto:begin -->

Training a model on ground-truth prefixes rather than on its own generations. The sources treat it from opposite ends. One prices it: selecting a predictor consistent with the entire chain of thought on the training data learns with sample complexity logarithmic in the combined input and reasoning length, with a matching lower bound, so no other rule using chain data does fundamentally better. The other names it as the thing to move away from, arguing that the teacher-forced objective underlying next-token prediction is ill-suited to long-horizon reasoning and planning and proposing latent auxiliary targets instead. Statistically cheap and, by the second account, structurally limited.

- **Kind**: method
- **Also called**: teacher-forced training
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [belief state](../concepts/belief-state.md), [chain of thought](chain-of-thought.md), [compounding error](../concepts/compounding-error.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [generalization](../concepts/generalization.md), [implicit reasoning](../concepts/implicit-reasoning.md), [latent reasoning](../concepts/latent-reasoning.md), [sample complexity](../concepts/sample-complexity.md), [speculative decoding](speculative-decoding.md)

## Appears in

- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
