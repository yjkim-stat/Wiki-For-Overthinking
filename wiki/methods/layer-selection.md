# layer selection

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 4

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [attention analysis](attention-analysis.md), [Aya-expanse-8B](../models/aya-expanse-8b.md), [beam search](beam-search.md), [BigCodeBench](../datasets/bigcodebench.md), [causal intervention](../concepts/causal-intervention.md), [CHAIR](../datasets/chair.md), [class imbalance](../concepts/class-imbalance.md), [COCO](../datasets/coco.md), [component ablation](component-ablation.md), [contrastive activation addition](contrastive-activation-addition.md), [contrastive decoding](contrastive-decoding.md), [cross-validation](cross-validation.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [distribution shift](../concepts/distribution-shift.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-2](../models/gpt-2.md), [GPT-4o](../models/gpt-4o.md), [grounding](../concepts/grounding.md), [hallucination](../concepts/hallucination.md), [HumanEval+](../datasets/humaneval.md), [identifiability](../concepts/identifiability.md), [interpretability illusion](../concepts/interpretability-illusion.md), [linear probe](linear-probe.md), [Llama-3-8B-Instruct](../models/llama-3-8b-instruct.md), [logistic regression](logistic-regression.md), [logit lens](logit-lens.md), [MBPP+](../datasets/mbpp.md), [measurement invariance](../concepts/measurement-invariance.md), [operating point](../concepts/operating-point.md), [out-of-domain generalization](../concepts/out-of-domain-generalization.md), [PCA](pca.md), [POPE](../datasets/pope.md), [Qwen](../models/qwen.md), [residual stream](../concepts/residual-stream.md), [selection bias](../concepts/selection-bias.md), [Shapley value](../concepts/shapley-value.md), [steering vector](steering-vector.md), [supervised fine-tuning](supervised-fine-tuning.md), [training-free intervention](training-free-intervention.md)

## Appears in

- [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](../../archive/papers/2026/arxiv-2608-07302/summary.md) — Refutes the standard account of vision-language hallucination -- that the model attends too little to the image -- by showing real and hallucinated objects draw equally strong attention, then uses a logit lens over the attended regions to separate two causally distinct hallucination types and treat each differently.
- [On the Robustness of LLMs' Internal Representation of Code Correctness](../../archive/papers/2026/arxiv-2608-08266/summary.md) — Asks whether a published internal signal for code correctness is a property of the model or of the one extraction recipe used to find it, sweeps every design choice systematically, and finds no configuration is best anywhere -- with the benchmark deciding which choice wins, and a mismatched fitting source able to drive the signal below chance.
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) — Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.
- [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](../../archive/papers/2026/arxiv-2608-10835/summary.md) — Reads a frozen vision-language model's forward pass as a structured computational trace -- a graph over image patches, query tokens and generated tokens with attention as edges, processed by interleaved relational, spatial and sequential modules -- and shows that structuring the same internals prior detectors already read lifts hallucination detection from a 69-75 AUC plateau to 90.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
