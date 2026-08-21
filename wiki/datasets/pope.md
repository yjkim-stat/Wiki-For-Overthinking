# POPE

<!-- auto:begin -->

A visual question-answering benchmark that is in this wiki only because two vision-language papers matched the overthinking topic on shared vocabulary, not on subject. Mixture-of-Visual-Thoughts groups it with V*, MMStar and SpatialScore as its 'general' (non-math) sets and reports that after RL its model selects the visually-grounded reasoning mode on 99-100% of POPE inputs, the opposite extreme from the math benchmarks where it picks text mode 98-100% of the time; that paper reports no token counts, latency or cost of any kind. HiDrop evaluates LLaVA-1.5 on POPE as one of 11 benchmarks, retaining 96.5% of average performance at 91.7% vision-token compression, and the archive marks it not relevant — a false positive on 'early exit', since its pruning acts on image patch embeddings and its costs are all prefill-side. Nothing in the archive reports a reasoning-length or accuracy/length result on POPE.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Ada-GRPO](../methods/ada-grpo.md), [GQA](gqa.md), [GRPO](../methods/grpo.md), [Layer-wise early exit](../methods/layer-wise-early-exit.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMStar](mmstar.md), [WeMath](wemath.md)

## Appears in

- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.
- [HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit](../../archive/papers/2026/title-b2302bb0271de496/summary.md) — HiDrop prunes about 90% of the vision tokens in a multimodal LLM by injecting them only at the layer where visual-text fusion actually begins and then dropping them on a concave schedule with a per-layer early exit, matching baseline accuracy while training 1.72x faster.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
