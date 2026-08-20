# CHAIR

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [attention analysis](../methods/attention-analysis.md), [causal intervention](../concepts/causal-intervention.md), [class imbalance](../concepts/class-imbalance.md), [COCO](coco.md), [component ablation](../methods/component-ablation.md), [detection versus control](../concepts/detection-versus-control.md), [distribution shift](../concepts/distribution-shift.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [logit lens](../methods/logit-lens.md), [operating point](../concepts/operating-point.md), [residual stream](../concepts/residual-stream.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) — Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
