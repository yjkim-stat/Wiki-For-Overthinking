# speculative decoding

<!-- auto:begin -->

Proposing several tokens cheaply and verifying them against the target model, so that accepted proposals are generated in fewer forward passes without changing the output distribution. One source adapts it to RL training, where the target policy keeps changing so a static proposer goes stale, using lightweight future-token heads with fast hidden-state correction and slow head updates; exact target verification is what leaves the GRPO objective unchanged, so the 1.21-2.04x end-to-end speedup costs nothing in quality. The other reports improved speculative-decoding efficiency as a side effect of a hierarchical latent pretraining objective. Both treat exactness as the property that makes the speedup free rather than a trade-off.

- **Kind**: method
- **Also called**: draft-and-verify decoding, speculative sampling
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [belief state](../concepts/belief-state.md), [compounding error](../concepts/compounding-error.md), [GRPO](grpo.md), [implicit reasoning](../concepts/implicit-reasoning.md), [latent reasoning](../concepts/latent-reasoning.md), [teacher forcing](teacher-forcing.md), [train-inference gap](../concepts/train-inference-gap.md)

## Appears in

- [SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts](../../archive/papers/2026/arxiv-2608-04962/summary.md) — A speculative-decoding rollout engine for RL post-training that keeps the target sampling distribution exact while adapting the drafter at two timescales.
- [Hierarchical Latent Prediction for Language Models](../../archive/papers/2026/arxiv-2608-05806/summary.md) — Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
