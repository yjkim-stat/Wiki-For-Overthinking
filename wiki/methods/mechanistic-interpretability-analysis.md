# mechanistic interpretability analysis

<!-- auto:begin -->

Analyzing a model's internal activations or weights -- rather than only its inputs/outputs -- to explain a behavior. Sources apply it in two ways relevant to overthinking: identifying that overthinking corresponds to a low-dimensional manifold in activation space that can be steered to cut output tokens without hurting accuracy, and identifying which weight components (e.g. final-layer MLP projections) are load-bearing for reasoning versus for knowledge memorization when a reasoning model is compressed.

- **Kind**: method
- **Also called**: mechanistic interpretation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [DeepSeek-R1](../models/deepseek-r1.md), [knowledge distillation](knowledge-distillation.md)

## Appears in

- [When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models](../../archive/papers/2026/title-c593d75efe2e5d8c/summary.md) — Studies how quantization, distillation and pruning affect DeepSeek-R1's reasoning ability using mechanistic interpretation, finding weight count matters more for knowledge memorization than reasoning, and that protecting just 2% of over-compressed weights recovers 6.57 accuracy points.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
