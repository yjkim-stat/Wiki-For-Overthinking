# train-inference gap

<!-- auto:begin -->

The mismatch between the distribution a policy is optimized on and the one it generates from at deployment, which both sources treat as a correctness problem rather than an efficiency one. One removes it by construction: exact target verification during speculative rollouts leaves the target sampling distribution and the GRPO objective unchanged, so the speedup introduces no policy-gradient bias. The other closes it in flow models, where training substitutes a stochastic differential equation for the deterministic sampler used at inference and the finite-step discretizations diverge, by taking an inference-aligned deterministic step followed by a stochastic correction. Language RLVR has the same structure — rollouts sampled at temperature, evaluation often greedy — and the archive holds no source measuring that gap directly.

- **Kind**: concept
- **Also called**: distribution shift at inference, exposure bias, training-inference mismatch
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [exploration](exploration.md), [GRPO](../methods/grpo.md), [speculative decoding](../methods/speculative-decoding.md)

## Appears in

- [SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts](../../archive/papers/2026/arxiv-2608-04962/summary.md) — A speculative-decoding rollout engine for RL post-training that keeps the target sampling distribution exact while adapting the drafter at two timescales.
- [LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](../../archive/papers/2026/arxiv-2608-05600/summary.md) — A GRPO variant for flow-based generative models that replaces SDE training rollouts with an ODE step plus a Langevin correction, aligning training samples with the deterministic sampler used at test time.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
