# flow matching

<!-- auto:begin -->

Learning a continuous-time transport between distributions, appearing across 3 sources as the generative backbone for action and image models and, in one, as the setting for a training-inference mismatch worth recording generally. That source's argument: flow-based reinforcement learning swaps a deterministic sampler for a stochastic one during training, and although the two share marginals in continuous time their finite-step discretisations differ substantially, with stochastic rollouts blurring as exploration noise rises -- so the samples optimised are not the samples the test-time sampler produces. The correction it proposes is a Langevin term that narrows that gap. The archive's related point is the general one: a method that optimises a proxy for what deployment will do needs the gap measured rather than assumed.

- **Kind**: method
- **Also called**: conditional flow matching
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [causal intervention](causal-intervention.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [CLIP](../models/clip.md), [component ablation](component-ablation.md), [compression](../concepts/compression.md), [cosine similarity](cosine-similarity.md), [distribution shift](../concepts/distribution-shift.md), [exploration](../concepts/exploration.md), [foresight](../concepts/foresight.md), [GRPO](grpo.md), [latent reasoning](../concepts/latent-reasoning.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [reinforcement learning](reinforcement-learning.md), [structured chain of thought](structured-chain-of-thought.md), [supervised fine-tuning](supervised-fine-tuning.md), [t-SNE](t-sne.md), [train-inference gap](../concepts/train-inference-gap.md), [Wasserstein distance](wasserstein-distance.md)

## Appears in

- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](../../archive/papers/2026/arxiv-2608-05600/summary.md) — A GRPO variant for flow-based generative models that replaces SDE training rollouts with an ODE step plus a Langevin correction, aligning training samples with the deterministic sampler used at test time.
- [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](../../archive/papers/2026/arxiv-2608-10976/summary.md) — Replaces a verbose natural-language rationale with two to six executable action tokens drawn from a fixed vocabulary, supervised automatically by pairing logged trajectories with scene context, so that driving-oriented reasoning fits inside a real-time control budget that verbose chain-of-thought exceeds by three to four times.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
