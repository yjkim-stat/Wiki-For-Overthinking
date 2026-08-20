# tuned lens

<!-- auto:begin -->

A per-layer affine map trained to translate an intermediate activation into the final layer's basis before the model's own frozen normalisation and unembedding are applied, so that a readout failure can be separated from a computation that has not happened yet. Its diagnostic value is exactly that separation, and the text-to-MIDI work is the archive's clearest demonstration: a decoder-only model's classic logit-lens agreement jumps from 0.050 to 0.712 across three layers, but the tuned lens makes the final prediction readable two to three layers earlier, and a vocabulary-mass analysis shows the readout rotating out of an inherited textual basis over the same band -- so most of the apparent jump is a change of basis rather than the moment the decision forms. Translators there are initialised to identity and distilled against the model's own final distribution by KL on 60,000 held-out token positions. The dense-lens work makes the same instrument cheap enough to attach everywhere, with low-rank translators whose parameters grow linearly rather than quadratically in width and subset-KL objectives including an importance-sampled variant proved to give unbiased gradients for the full KL -- 482 lenses on a 70B model, where no full-rank reference can be trained at all. What that coverage buys is a conclusion the sparse designs cannot reach: over component types, detection and intervention rankings correlate at Spearman -0.43.

- **Kind**: method
- **Also called**: trained lens, translator
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [circuit analysis](circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [importance sampling](importance-sampling.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](knowledge-distillation.md), [linear probe](linear-probe.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [logit lens](logit-lens.md), [LoRA](lora.md), [residual stream](../concepts/residual-stream.md), [SciQ](../datasets/sciq.md), [selectivity control](selectivity-control.md), [sparse autoencoder](sparse-autoencoder.md), [the Pile](../datasets/the-pile.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
