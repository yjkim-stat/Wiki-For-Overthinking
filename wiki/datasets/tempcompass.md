# TempCompass

<!-- auto:begin -->

A video-understanding benchmark focused on temporal reasoning -- ordering, direction, speed and change -- rather than on static scene recognition, so a model cannot answer from a single frame. Both sources use it as a generality check outside the setting a method was built for: the representation-filtering work applies its closed-form hallucination correction to it to show the filter transfers to temporal video reasoning, and the perception-versus-reasoning latent work uses it among the sets distinguishing questions that need inference from questions that need grounding. Neither describes its construction; in this archive it functions as the test that separates temporal understanding from frame-level perception.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [attention pattern](../concepts/attention-pattern.md), [calibration](../methods/calibration.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [CHAIR](chair.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [Coconut](../methods/coconut.md), [component ablation](../methods/component-ablation.md), [contrastive decoding](../methods/contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [hallucination](../concepts/hallucination.md), [Kimi-K2.5](../models/kimi-k2-5.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLaVA-1.5](../models/llava-1-5.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [low-rank approximation](../methods/low-rank-approximation.md), [monitorability](../concepts/monitorability.md), [POPE](pope.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [representation editing](../methods/representation-editing.md), [residual stream](../concepts/residual-stream.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [training-free intervention](../methods/training-free-intervention.md), [verifiable reward](../concepts/verifiable-reward.md), [Video-MME](video-mme.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) — Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
