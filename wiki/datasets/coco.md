# COCO

<!-- auto:begin -->

A large image-captioning corpus, used in both sources as the substrate for measuring object hallucination rather than as a benchmark in its own right. Captions generated on its images are scored against its object annotations to count mentions of objects that are not present, which is what makes it the standard ground for the CHAIR family of metrics. The structured read-out work uses self-generated captions on it to reach 92.3 F1 for hallucinated-mention detection against 82.0 for the strongest prior method, and reports word count, correct-object coverage and perplexity alongside the hallucination reduction so that the improvement cannot be a suppression artifact. The attention-versus-evidence work uses it for the same purpose. Neither source describes the corpus; in this archive it functions as the annotated image set that makes an object-level hallucination claim checkable.

- **Kind**: dataset
- **Also called**: MSCOCO
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [attention analysis](../methods/attention-analysis.md), [causal intervention](../methods/causal-intervention.md), [CHAIR](chair.md), [class imbalance](../concepts/class-imbalance.md), [component ablation](../methods/component-ablation.md), [contrastive decoding](../methods/contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [distribution shift](../concepts/distribution-shift.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [logit lens](../methods/logit-lens.md), [operating point](../concepts/operating-point.md), [POPE](pope.md), [residual stream](../concepts/residual-stream.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training-free intervention](../methods/training-free-intervention.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) — Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
