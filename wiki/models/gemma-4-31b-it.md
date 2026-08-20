# Gemma-4-31B-it

<!-- auto:begin -->

A 31-billion-parameter instruction-tuned Gemma model, loaded in 8-bit quantization in one of the two sources here. In the ESG concept-content study it is the largest model tested and matches or outperforms every other on accuracy across all three pillars when concept vectors are extracted by the Recursive Feature Machine -- but it is absent from every linear-probing table because the kernel repeatedly ran out of memory, a constraint the authors attribute to their accelerator rather than the method and report as costing coverage rather than a conclusion. It is separately one of 18 open models instrumented in the cultural-awareness study, whose finding is that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults. Neither source characterises the model beyond its size and behaviour.

- **Kind**: model
- **Also called**: Gemma-4-31b-it
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [causal intervention](../concepts/causal-intervention.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [logistic regression](../methods/logistic-regression.md), [logit lens](../methods/logit-lens.md), [PCA](../methods/pca.md), [Phi-4](phi-4.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3.6-27B](qwen3-6-27b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](../methods/ridge-regression.md), [scaling laws](../concepts/scaling-laws.md), [TF-IDF](../methods/tf-idf.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](../../archive/papers/2026/arxiv-2608-07208/summary.md) — Compares linear probes against RFM-derived concept vectors for reading how much a sentence concerns a concept out of a frozen LLM's activations, on a human-annotated ESG benchmark, and finds the simpler probe consistently stronger.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
