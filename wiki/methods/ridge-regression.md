# ridge regression

<!-- auto:begin -->

Least-squares fitting with an L2 penalty, appearing across 3 sources as the workhorse behind probes, concept vectors and weight-mechanism analyses. Its role in the archive is unglamorous and load-bearing: it is the estimator whose regularisation strength is one of the extraction choices a robustness sweep varies, and the archive's related finding is that no configuration of such choices is best across benchmarks. One source uses it to fit concept directions and finds a simpler probe consistently stronger, which is the recurring pattern that added machinery in the readout rarely pays.

- **Kind**: method
- **Also called**: L2-regularized linear regression, regularized least squares, ridge regression
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [ablation](ablation.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [causal intervention](causal-intervention.md), [detection versus control](../concepts/detection-versus-control.md), [Gemma-2-2B](../models/gemma-2-2b.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [Gemma-4-31B-it](../models/gemma-4-31b-it.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B-Instruct](../models/llama-3-2-1b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [logistic regression](logistic-regression.md), [logit lens](logit-lens.md), [low-rank approximation](low-rank-approximation.md), [monosemanticity](../concepts/monosemanticity.md), [nested cross-validation](nested-cross-validation.md), [PCA](pca.md), [Phi-4](../models/phi-4.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.6-27B](../models/qwen3-6-27b.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [scaling laws](../concepts/scaling-laws.md), [sparse autoencoder](sparse-autoencoder.md), [TF-IDF](tf-idf.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) — Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](../../archive/papers/2026/arxiv-2608-07208/summary.md) — Compares linear probes against RFM-derived concept vectors for reading how much a sentence concerns a concept out of a frozen LLM's activations, on a human-annotated ESG benchmark, and finds the simpler probe consistently stronger.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
