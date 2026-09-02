# AI2D

<!-- auto:begin -->

The archive cannot define AI2D from its own sources: both papers that mention it (vStream, which predicts counterfactual ablation effects of image regions from cached attention features at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines, and Heima, which replaces each stage of a multimodal chain of thought with a single latent thinking token) are multimodal reasoning methods, and neither archived note says anything about AI2D's contents, size or task format. What the notes do establish is only the role it plays in them: an evaluation set for multimodal models that reason over images. Treat this entry as a placeholder until a source that describes the benchmark itself is read.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [ChartQA](chartqa.md), [GQA](gqa.md), [Latent reasoning](../concepts/latent-reasoning.md), [LISA](lisa.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLaVA-CoT](../models/llava-cot.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MM-Vet](mm-vet.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [MMStar](mmstar.md), [OlympiadBench](olympiadbench.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [SAT](sat.md), [ScienceQA](scienceqa.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [VizWiz](vizwiz.md)

## Appears in

- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.
- [Real-Time Visual Attribution Streaming in Thinking Model](../../archive/papers/2026/title-503ded235751878b/summary.md) — vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
