# Llama-3.2-1B

<!-- auto:begin -->

Meta's 1B-parameter Llama 3.2 checkpoint, used in this archive as the smallest backbone in test-time-scaling and latent-reasoning experiments. Two roles recur. It is the standing demonstration that inference algorithm can substitute for parameters -- under one test-time-scaling method it outperforms the larger Llama-3.2-3B on MATH -- and it is the base for latent-reasoning work (COCONUT, CODI, SLPO) where accuracy is reported on GSM8K and MultiArith. A separate edge-systems source uses it to show the opposite end of the same tradeoff: at 1B the generator no longer dominates the per-query budget, with 33% of wall time and 39% of GPU energy spent in embedding and retrieval.

- **Kind**: model
- **Also called**: Llama-3.2 1B, Llama-3.2-1B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [HotpotQA](../datasets/hotpotqa.md), [Latent reasoning](../concepts/latent-reasoning.md), [Natural Questions](../datasets/natural-questions.md), [Qwen2.5 7B](qwen2-5-7b.md), [Recurrent Depth](../concepts/recurrent-depth.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG](../../archive/papers/unknown/arxiv-2608-19535/summary.md) — Measures retrieval-augmented generation stage by stage on an edge SoC and shows that context compression pays only inside a bounded rate window, because the compressor runs on the same chip and its own latency and energy must be subtracted from the savings.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
