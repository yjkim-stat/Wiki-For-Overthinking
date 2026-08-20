# CHAIR

<!-- auto:begin -->

A family of metrics counting how many objects a generated caption mentions that are not present in the annotated image, at caption level and instance level. Across 3 sources it is the standard measure for object hallucination in vision-language models, and the archive's note about it is methodological: a reduction in hallucinated mentions is compatible with a model simply saying less, so the sources that report it credibly report word count, correct-object coverage and perplexity alongside -- one showing guarded captions retaining 95.4 percent of vanilla word count while eliminating the empty captions the undefended decoding produced. One source notes against its own interest that some decoding-based competitors achieve slightly higher fluency while its method minimises hallucinated objects, which is the trade this metric alone cannot show.

- **Kind**: method
- **Also called**: CHAIR metric, CHAIRi, CHAIRs
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [attention analysis](attention-analysis.md), [calibration](../concepts/calibration.md), [causal intervention](causal-intervention.md), [class imbalance](../concepts/class-imbalance.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [COCO](../datasets/coco.md), [component ablation](component-ablation.md), [contrastive decoding](contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [distribution shift](../concepts/distribution-shift.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](layer-selection.md), [linear probe](linear-probe.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](llm-as-a-judge.md), [logit lens](logit-lens.md), [low-rank approximation](low-rank-approximation.md), [operating point](../concepts/operating-point.md), [POPE](../datasets/pope.md), [representation editing](representation-editing.md), [residual stream](../concepts/residual-stream.md), [steering vector](steering-vector.md), [supervised fine-tuning](supervised-fine-tuning.md), [TempCompass](../datasets/tempcompass.md), [training-free intervention](training-free-intervention.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) — Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
