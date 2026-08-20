# flow matching

<!-- auto:begin -->

Training a generative model by regressing a velocity field along a straight interpolation between noise and data, so sampling becomes integration of an ordinary differential equation. The two sources meet at the seam that creates. One uses it to predict action chunks, integrating the learned field with a fixed number of Euler steps at deployment. The other identifies the problem that follows for reinforcement learning on such models: the deployment sampler is deterministic while online RL needs stochastic rollouts, and the usual remedy of substituting a stochastic differential equation during training makes the optimized samples diverge from the ones the deployed sampler produces — and blur further as exploration noise rises. Its fix keeps the inference-aligned deterministic step and adds a correction targeting the same marginal, so exploration is bought without changing the sampler.

- **Kind**: method
- **Also called**: conditional flow matching
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [causal intervention](../concepts/causal-intervention.md), [CLIP](../models/clip.md), [cosine similarity](cosine-similarity.md), [exploration](../concepts/exploration.md), [foresight](../concepts/foresight.md), [GRPO](grpo.md), [latent reasoning](../concepts/latent-reasoning.md), [t-SNE](t-sne.md), [train-inference gap](../concepts/train-inference-gap.md)

## Appears in

- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](../../archive/papers/2026/arxiv-2608-05600/summary.md) — A GRPO variant for flow-based generative models that replaces SDE training rollouts with an ODE step plus a Langevin correction, aligning training samples with the deterministic sampler used at test time.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
