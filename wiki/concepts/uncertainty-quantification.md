# uncertainty quantification

<!-- auto:begin -->

Attaching a defensible measure of confidence to a model's output, which the two sources approach with opposite priorities. One demands statistical guarantees, applying conformal prediction to the joint reasoning-answer structure rather than to the answer alone on the grounds that existing methods ignore the logical connection between trace and answer, and then attributes coverage back to specific training examples and reasoning steps using Shapley values. The other shows a confidence signal can be worthless as a probability and excellent as a ranking: a diffusion language model reaches 31.2% expected calibration error on mathematical reasoning while achieving 0.826 AUROC against 0.611 for comparable single-pass autoregressive baselines. The pair separates two properties commonly conflated — calibrated magnitude and correct ordering — which matters because threshold-gated methods need the first and selection methods need only the second.

- **Kind**: concept
- **Also called**: UQ, confidence estimation, uncertainty estimation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [answer stabilization](answer-stabilization.md), [calibration](../methods/calibration.md), [expected calibration error](../methods/expected-calibration-error.md)

## Appears in

- [Quantifying and Understanding Uncertainty in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1511/summary.md) — Applies conformal prediction to the joint reasoning-answer structure of reasoning models, then attributes coverage to specific training examples and reasoning steps with Shapley values.
- [The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2142/summary.md) — Finds diffusion language models are badly miscalibrated on math reasoning yet rank correct from incorrect far better than autoregressive baselines, because their confidence tracks structural consistency rather than correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
