# AI2D

<!-- auto:begin -->

The archive cannot define AI2D from its own sources: both papers that mention it (vStream, which predicts counterfactual ablation effects of image regions from cached attention features at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines, and Heima, which replaces each stage of a multimodal chain of thought with a single latent thinking token) are multimodal reasoning methods, and neither archived note says anything about AI2D's contents, size or task format. What the notes do establish is only the role it plays in them: an evaluation set for multimodal models that reason over images. Treat this entry as a placeholder until a source that describes the benchmark itself is read.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [GQA](gqa.md), [Latent reasoning](../concepts/latent-reasoning.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MathVerse](mathverse.md), [MathVista](mathvista.md), [MMStar](mmstar.md), [OlympiadBench](olympiadbench.md)

## Appears in

- [Real-Time Visual Attribution Streaming in Thinking Model](../../archive/papers/2026/title-503ded235751878b/summary.md) — vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
