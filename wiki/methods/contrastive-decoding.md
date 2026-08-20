# contrastive decoding

<!-- auto:begin -->

Producing an output distribution by combining or differencing two distributions rather than reading one, typically to amplify what distinguishes a grounded generation from an ungrounded one. Both sources here use the idea but locate the intervention differently, which is the useful contrast. The attention-versus-evidence work fuses the model's decoding logits under a masked image with visual logits decoded from the highest-attention region through a logit lens, so correct visual evidence is weighted against the contextual prior that would otherwise produce the object -- and applies this only to the hallucination type that survives masking, with a mixing weight controlling how far visual semantics displace the model's own distribution. The Wiener-filtering work argues instead for moving the correction out of decoding entirely, folding a closed-form linear operator into the model's feed-forward output projections so inference runs unchanged and at the same speed. The archive's reading is the trade the pair mark: decoding-time contrast is switchable and per-query but costs latency on every query, while a weight-absorbed correction is free at inference and is a permanent commitment.

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [attention analysis](attention-analysis.md), [calibration](../concepts/calibration.md), [causal intervention](causal-intervention.md), [CHAIR](chair.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [COCO](../datasets/coco.md), [component ablation](component-ablation.md), [detection versus control](../concepts/detection-versus-control.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](layer-selection.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](llm-as-a-judge.md), [logit lens](logit-lens.md), [low-rank approximation](low-rank-approximation.md), [POPE](../datasets/pope.md), [representation editing](representation-editing.md), [residual stream](../concepts/residual-stream.md), [steering vector](steering-vector.md), [TempCompass](../datasets/tempcompass.md), [training-free intervention](training-free-intervention.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
