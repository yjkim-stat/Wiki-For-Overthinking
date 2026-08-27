# Early-Exit Inference

<!-- auto:begin -->

Terminating a model's generation or a network's forward pass once a stopping condition is met, rather than always running to a fixed length or depth. Sources apply the term across two different settings: chain-of-thought models terminating (or failing to terminate, looping until a token ceiling) depending on problem difficulty, and layer-wise early exit in non-text architectures (Visual AutoRegressive image generation) where high-frequency detail only emerges in later stages, requiring the exit condition to be redesigned rather than reused from standard early-exit assumptions.

- **Kind**: concept
- **Also called**: early exit, early-exit inference
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Budget Forcing](../methods/budget-forcing.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models](../../archive/papers/2026/arxiv-2607-21433/summary.md) — Two studies on DeepSeek-R1-Distill-Qwen-7B: a budget-forcing sweep showing GSM8K and MATH-500 accuracy saturates at 256 thinking tokens while AIME splits bimodally into generations that terminate and generations that loop until the 10,000-token ceiling, and a linear-probe study showing that hidden-state activations at token 150 predict which of the two an AIME generation will become at AUC 0.608.
- [FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance](../../archive/papers/2025/title-f4d76f842234cebc/summary.md) — FreqExit enables dynamic early-exit inference for Visual AutoRegressive (VAR) image generation models by exploiting that high-frequency image details emerge only in later decoding stages, using curriculum-based layer-dropout supervision and a wavelet-domain frequency-consistency loss, achieving up to 2x speedup with minor quality loss.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
