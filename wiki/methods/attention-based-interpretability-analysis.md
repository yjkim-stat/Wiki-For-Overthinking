# attention-based interpretability analysis

<!-- auto:begin -->

In this source, attention-based interpretability analysis computes a position-normalized attention score to question tokens versus mid-result tokens versus other tokens at each generation step, to test whether a reasoning model re-attends to the question when deciding whether to reflect. Applied to layers 21-30, it shows attention to the question segment rises from a low background level to more than 4x higher at the moment a reflection token is about to be emitted than during ordinary answer generation, particularly in middle-to-later layers. The authors use this result to argue that heightened attention to the question is the channel through which an implicit first-guess 'internal bias' re-enters the reasoning trajectory and triggers overthinking.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [counterfactual intervention](counterfactual-intervention.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [internal bias](../concepts/internal-bias.md), [Overthinking](../concepts/overthinking.md), [QwQ-32B](../models/qwq-32b.md), [SEAL](seal.md)

## Appears in

- [The First Impression Problem: Internal Bias Triggers Overthinking in Reasoning Models](../../archive/papers/2026/local-f13a1da3e3ea0d42/summary.md) — Identifies a reasoning model's implicit, pre-reasoning guess about the answer ('internal bias') as a causal driver of overthinking, showing that when this guess conflicts with the model's derived answer it triggers excessive reflection, and that existing overthinking-mitigation methods fail to remove this influence.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
