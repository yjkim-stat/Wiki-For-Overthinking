# Layer-wise early exit

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Also called**: Layer-wise Early Exit
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [GQA](../datasets/gqa.md), [MMStar](../datasets/mmstar.md), [POPE](../datasets/pope.md)

## Appears in

- [SwiftPFN: Revisiting Row-Wise Attention–Only Tabular Foundation Models with Adaptive Early Exit](../../archive/papers/2026/title-01b92aa66908c5e0/summary.md) — Returns to TabPFN's row-wise attention-only backbone for tabular in-context learning, adds gated attention stabilisation and learnable register tokens, and attaches a per-sample layer-wise early exit so inference depth varies with the sample.
- [HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit](../../archive/papers/2026/title-b2302bb0271de496/summary.md) — HiDrop prunes about 90% of the vision tokens in a multimodal LLM by injecting them only at the layer where visual-text fusion actually begins and then dropping them on a concave schedule with a per-layer early exit, matching baseline accuracy while training 1.72x faster.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
