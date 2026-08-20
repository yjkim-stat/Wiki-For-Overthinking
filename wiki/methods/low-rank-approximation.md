# low-rank approximation

<!-- auto:begin -->

Representing a matrix or an intervention through a small number of directions, and across 3 sources both a tool and a finding about where information sits. As a finding: replacing the whole residual stream at a site has a comparable effect to a low-rank patch, so the causal information sits in a compact subspace -- which bounds where a mechanism lives rather than merely confirming it is upstream. As a tool: a closed-form linear operator estimated from second-order statistics and folded into a model's existing projections corrects hallucination at identical inference cost, with an ablation showing a first-order mean correction insufficient and the covariance structure doing the work. And as an analysis method for hidden states at scale. The archive's related caution is the identifiability one -- a low-rank basis recovered by fitting is a property of the fit unless something makes it invariant.

- **Kind**: method
- **Also called**: low-rank structure
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [ablation](ablation.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARC-Challenge](../datasets/arc-challenge.md), [ARC-Easy](../datasets/arc-easy.md), [calibration](../concepts/calibration.md), [CHAIR](chair.md), [circuit analysis](circuit-analysis.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [component ablation](component-ablation.md), [compression](../concepts/compression.md), [contrastive decoding](contrastive-decoding.md), [detection versus control](../concepts/detection-versus-control.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [HumanEval+](../datasets/humaneval.md), [importance sampling](importance-sampling.md), [Jaccard similarity](jaccard-similarity.md), [KL divergence](kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [linear probe](linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [LLaVA-1.5](../models/llava-1-5.md), [LLM-as-a-judge](llm-as-a-judge.md), [logit lens](logit-lens.md), [LoRA](lora.md), [matched-budget comparison](matched-budget-comparison.md), [MBPP+](../datasets/mbpp.md), [monosemanticity](../concepts/monosemanticity.md), [PCA](pca.md), [POPE](../datasets/pope.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [representation editing](representation-editing.md), [residual stream](../concepts/residual-stream.md), [SciQ](../datasets/sciq.md), [sparse autoencoder](sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [steering vector](steering-vector.md), [TempCompass](../datasets/tempcompass.md), [the Pile](../datasets/the-pile.md), [training-free intervention](training-free-intervention.md), [tuned lens](tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Wiener Representation Filtering for VLM Hallucination Suppression](../../archive/papers/2026/arxiv-2608-08167/summary.md) — Models hidden states as a superposition of truthful and hallucination-associated components and derives a closed-form Wiener filter over their covariances, giving mode-wise attenuation that is folded back into the model's own weights so inference runs unchanged and at the same speed.
- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
