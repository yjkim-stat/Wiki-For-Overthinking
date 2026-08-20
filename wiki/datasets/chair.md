# CHAIR

<!-- auto:begin -->

A metric and evaluation protocol for object hallucination in image captioning, counting mentioned objects absent from the image at the instance and sentence level, and in both sources here the yardstick against which a mitigation is judged rather than a benchmark in the usual sense. The structured read-out work uses it to label hallucinated object mentions in freely generated captions and reports the pair falling from 18.0 and 37.2 to 8.2 and 16.6 under its guardrail -- alongside retained word count, preserved correct-object coverage, perplexity and distribution shift, precisely so the reduction cannot be a suppression artifact. The attention-versus-evidence work uses it to evaluate two type-matched remedies. Neither describes its construction. Its role in the archive is as a reminder that a hallucination metric can be driven down by saying less, which is why both sources report content-preservation measures beside it.

- **Kind**: dataset
- **Also called**: CHAIRi, CHAIRs
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [attention analysis](../methods/attention-analysis.md), [calibration](../concepts/calibration.md), [causal intervention](../concepts/causal-intervention.md), [class imbalance](../concepts/class-imbalance.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [COCO](coco.md), [component ablation](../methods/component-ablation.md), [contrastive decoding](../methods/contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [distribution shift](../concepts/distribution-shift.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logit lens](../methods/logit-lens.md), [low-rank approximation](../methods/low-rank-approximation.md), [operating point](../concepts/operating-point.md), [POPE](pope.md), [representation editing](../methods/representation-editing.md), [residual stream](../concepts/residual-stream.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TempCompass](tempcompass.md), [training-free intervention](../methods/training-free-intervention.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) — Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
