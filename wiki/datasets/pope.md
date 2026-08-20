# POPE

<!-- auto:begin -->

A polling-based probe for object hallucination in vision-language models, asking yes-or-no questions about whether particular objects appear in an image under random, popular and adversarial samplings of the negatives -- the last drawn from objects that frequently co-occur with what is present, so a model relying on co-occurrence priors fails. Both sources use it as their grounding benchmark. It is where the structured trace read-out reports its largest margin, reaching 90.0 area under the curve where every prior detector -- external verifiers and flat read-outs of the same frozen internals alike -- plateaus between 69 and 75, which that paper attributes to representation of the evidence rather than access to it. The Wiener-filtering work reports gains across all three splits. Neither describes its construction; what matters in this archive is the adversarial split, which is designed so that the prior a model would use to guess is exactly the prior that makes it wrong.

- **Kind**: dataset
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [attention analysis](../methods/attention-analysis.md), [calibration](../methods/calibration.md), [CHAIR](chair.md), [class imbalance](../concepts/class-imbalance.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [COCO](coco.md), [component ablation](../methods/component-ablation.md), [contrastive decoding](../methods/contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [distribution shift](../concepts/distribution-shift.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [low-rank approximation](../methods/low-rank-approximation.md), [operating point](../concepts/operating-point.md), [representation editing](../methods/representation-editing.md), [residual stream](../concepts/residual-stream.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TempCompass](tempcompass.md), [training-free intervention](../methods/training-free-intervention.md)

## Appears in

- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) — Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
