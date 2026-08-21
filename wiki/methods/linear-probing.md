# linear probing

<!-- auto:begin -->

Training a simple linear classifier or regressor on a model's internal activations to test what information they encode, without modifying the model itself. Used in the archive as an interpretability tool: the mechanistic-understanding survey lists it among techniques applied to large reasoning models, and 'On Reasoning Strength Planning' uses a directional activation vector (found via a linear-probe-like analysis) to show models pre-plan how much to reason before generating.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [aha moment](../concepts/aha-moment.md), [overthinking](../concepts/overthinking.md), [reward hacking](../concepts/reward-hacking.md)

## Appears in

- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/local-34cecfd6f28ba72b/summary.md) — A survey that organizes existing mechanistic-interpretability research on large reasoning models into three areas -- reasoning-oriented training dynamics, reasoning mechanisms, and unintended behaviors (hallucination, CoT unfaithfulness, overthinking, unsafety) -- and proposes directions for future mechanistic work.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/title-11c0c9193baf1d69/summary.md) — Finds that large reasoning models pre-plan how much to reason via a directional vector in their activations, whose magnitude causally sets reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
