# low-rank approximation

<!-- auto:begin -->

Representing a matrix or a family of maps by a small number of directions, used in these sources both as an engineering device and as a rival explanation to be ruled out. As a device it is what makes dense instrumentation affordable: low-rank translators let per-lens parameters grow linearly rather than quadratically in width, which is what allows 482 lenses to be attached to a 70B model where no full-rank reference can be trained at all -- and that coverage is what yields the conclusion the sparse designs cannot reach, that detection and intervention rankings over component types correlate at Spearman -0.43. As a rival explanation it is the confound the agent-channel compression study names against itself: a fitted dictionary in which only 50 of 4096 features ever activate is equally consistent with low-rank input structure or optimisation collapse as with a compact sparse code, and the baselines needed to separate them -- PCA, a linear autoencoder, matched-rate quantisation and vector quantisation -- are listed as not run. The pairing is the useful part: low rank is a reason a method works and a reason a sparsity result may not mean what it appears to.

- **Kind**: method
- **Also called**: low-rank structure
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [ablation](ablation.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARC-Challenge](../datasets/arc-challenge.md), [ARC-Easy](../datasets/arc-easy.md), [circuit analysis](circuit-analysis.md), [compression](../concepts/compression.md), [detection versus control](../concepts/detection-versus-control.md), [GPQA](../datasets/gpqa.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [importance sampling](importance-sampling.md), [Jaccard similarity](jaccard-similarity.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [linear probe](linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [logit lens](logit-lens.md), [LoRA](lora.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MBPP+](../datasets/mbpp.md), [monosemanticity](../concepts/monosemanticity.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [residual stream](../concepts/residual-stream.md), [SciQ](../datasets/sciq.md), [sparse autoencoder](sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [the Pile](../datasets/the-pile.md), [tuned lens](tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
