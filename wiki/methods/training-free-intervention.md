# training-free intervention

<!-- auto:begin -->

Changing a model's behaviour without gradient updates, using only forward passes and a fixed rule, and in both sources here chosen for a deployment reason rather than a scientific one. The attention-versus-evidence work operates at decoding time, masking an unreliable attended region or injecting decoded visual semantics into the logits, so the intervention is switchable and applies per query at a per-query cost. The Wiener-filtering work argues the opposite trade, estimating a closed-form linear operator from second-order statistics on a modest paired calibration set and then folding it into the model's existing feed-forward output projections, so the deployed model has identical architecture and identical inference cost and the correction is permanent. Both avoid the risk that motivates the category -- that full fine-tuning updates billions of parameters and may degrade the model it was meant to safeguard -- and between them they mark the choice a practitioner actually faces, which is whether the correction should be a switch or a commitment.

- **Kind**: method
- **Also called**: post-hoc intervention
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [attention analysis](attention-analysis.md), [calibration](../concepts/calibration.md), [causal intervention](causal-intervention.md), [CHAIR](chair.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [COCO](../datasets/coco.md), [component ablation](component-ablation.md), [contrastive decoding](contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](layer-selection.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](llm-as-a-judge.md), [logit lens](logit-lens.md), [low-rank approximation](low-rank-approximation.md), [POPE](../datasets/pope.md), [representation editing](representation-editing.md), [residual stream](../concepts/residual-stream.md), [steering vector](steering-vector.md), [TempCompass](../datasets/tempcompass.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
