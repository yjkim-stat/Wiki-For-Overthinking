# LLaVA-1.5

<!-- auto:begin -->

A widely used open vision-language model, and in this archive the default backbone for hallucination and interpretability work on multimodal models. It is one of the three backbones on which a closed-form representation edit is shown to reduce caption-level and instance-level hallucination to the lowest rates of any method compared, and one of four checkpoints supported by an open mechanistic-interpretability library giving vision-language models the activation-patching and attention-analysis tooling text-only models already have. It appears in several other archived entries as the model whose object hallucinations are being detected, localised or suppressed. Neither source describes its architecture or training; its role here is as the common substrate that makes multimodal hallucination results comparable across papers.

- **Kind**: model
- **Also called**: LLaVA 1.5, LLaVA-1.5, LLaVA-1.5-7B
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [attention pattern](../concepts/attention-pattern.md), [calibration](../concepts/calibration.md), [CHAIR](../datasets/chair.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [component ablation](../methods/component-ablation.md), [contrastive decoding](../methods/contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [hallucination](../concepts/hallucination.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [low-rank approximation](../methods/low-rank-approximation.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [POPE](../datasets/pope.md), [Qwen2.5-VL](qwen2-5-vl.md), [Qwen3-VL](qwen3-vl.md), [representation editing](../methods/representation-editing.md), [reproducibility](../concepts/reproducibility.md), [residual stream](../concepts/residual-stream.md), [steering vector](../methods/steering-vector.md), [TempCompass](../datasets/tempcompass.md), [training-free intervention](../methods/training-free-intervention.md)

## Appears in

- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
