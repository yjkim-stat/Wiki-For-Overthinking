# Early-Exit Inference

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: early-exit inference
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Budget Forcing](budget-forcing.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence in Chain-of-Thought Models](../../archive/papers/2026/arxiv-2607-21433/summary.md) — Two studies on DeepSeek-R1-Distill-Qwen-7B: a budget-forcing sweep showing GSM8K and MATH-500 accuracy saturates at 256 thinking tokens while AIME splits bimodally into generations that terminate and generations that loop until the 10,000-token ceiling, and a linear-probe study showing that hidden-state activations at token 150 predict which of the two an AIME generation will become at AUC 0.608.
- [FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance](../../archive/papers/2025/title-f4d76f842234cebc/summary.md) — FreqExit enables dynamic early-exit inference for Visual AutoRegressive (VAR) image generation models by exploiting that high-frequency image details emerge only in later decoding stages, using curriculum-based layer-dropout supervision and a wavelet-domain frequency-consistency loss, achieving up to 2x speedup with minor quality loss.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
