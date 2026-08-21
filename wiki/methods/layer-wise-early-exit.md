# Layer-wise early exit

<!-- auto:begin -->

Both sources use this in the forward-pass sense: a network carries exit points at intermediate layers so the depth actually executed varies per input, and neither is about the length of a reasoning trace. SwiftPFN attaches a per-sample layer-wise early exit to a row-wise attention-only tabular in-context-learning backbone, so inference depth varies with the sample. HiDrop uses a per-layer early exit as one component of a vision-token reduction scheme for multimodal LLMs, alongside injecting visual tokens only at the layer where visual-text fusion begins and dropping about 90% of them on a concave schedule, reported to match baseline accuracy while training 1.72x faster. Neither source states an exit criterion in the material held here.

- **Kind**: method
- **Also called**: Layer-wise Early Exit, per-layer early exit
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Early Exit](early-exit.md), [early-exit neural networks](../concepts/early-exit-neural-networks.md), [GQA](../datasets/gqa.md), [MMStar](../datasets/mmstar.md), [POPE](../datasets/pope.md)

## Appears in

- SwiftPFN: Revisiting Row-Wise Attention–Only Tabular Foundation Models with Adaptive Early Exit — Returns to TabPFN's row-wise attention-only backbone for tabular in-context learning, adds gated attention stabilisation and learnable register tokens, and attaches a per-sample layer-wise early exit so inference depth varies with the sample.
- HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit — HiDrop prunes about 90% of the vision tokens in a multimodal LLM by injecting them only at the layer where visual-text fusion actually begins and then dropping them on a concave schedule with a per-layer early exit, matching baseline accuracy while training 1.72x faster.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
