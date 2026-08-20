# Qwen3-VL-2B

<!-- auto:begin -->

A 2-billion-parameter Qwen vision-language model, the smallest scale in two multimodal training studies. In the structured process-reward work it improves from a four-benchmark average of 50.8 to 54.4 under step-level reward alignment, the smallest absolute gain of three scales but not the smallest relative one -- part of that paper's argument that reference-conditioned process supervision complements rather than substitutes for backbone capability. It appears again in the lightweight world-action model for robotic manipulation. Neither source characterises the model itself.

- **Kind**: model
- **Also called**: Qwen3-VL-2B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [causal intervention](../concepts/causal-intervention.md), [CLIP](clip.md), [component ablation](../methods/component-ablation.md), [cosine similarity](../methods/cosine-similarity.md), [credit assignment](../concepts/credit-assignment.md), [flow matching](../methods/flow-matching.md), [foresight](../concepts/foresight.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [latent reasoning](../concepts/latent-reasoning.md), [MathVista](../datasets/mathvista.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [process reward model](../concepts/process-reward-model.md), [Qwen3-VL-8B](qwen3-vl-8b.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](../methods/rlvr.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [t-SNE](../methods/t-sne.md)

## Appears in

- [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](../../archive/papers/2026/arxiv-2608-03701/summary.md) — Builds a 0.5B world-action model for robot manipulation whose future-state prediction and action generation share one compact latent in a single token stream, specifies the task as a direction in visual feature space instead of language, and shows a frozen self-supervised vision encoder beating a four-times-larger pretrained vision-language backbone at the same training budget.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
