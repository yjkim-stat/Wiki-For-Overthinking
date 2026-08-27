# adaptive test-time compute

<!-- auto:begin -->

Both archived sources use 'adaptive test-time compute' for setting the inference budget per query from a predicted signal instead of spending a fixed budget on every query, and they differ in which signal and which budget. CaTS allocates sampling budget per query from a self-distilled calibrated confidence signal and stops early once the model is confident, so the decision is made while sampling; Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and fixes the thinking budget before any reasoning is generated. Neither source defines the term formally, and it overlaps heavily with adaptive reasoning: the sources filed there choose a reasoning style or format per instance, whereas these two choose the size of the budget.

- **Kind**: concept
- **Also called**: Adaptive test-time compute
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [best-of-N](../methods/best-of-n.md), [Budget Forcing](../methods/budget-forcing.md), [Compute-optimal inference](compute-optimal-inference.md), [Confidence-based early stopping](../methods/confidence-based-early-stopping.md), [Confidence Calibration](confidence-calibration.md), [early stopping](early-stopping.md), [GPQA](../datasets/gpqa.md), [gpt-oss-120b](../methods/gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [Qwen3-8B](../methods/qwen3-8b.md), [Self-Consistency](../methods/self-consistency.md), [Test-Time Scaling](test-time-scaling.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
