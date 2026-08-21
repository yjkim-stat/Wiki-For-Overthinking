# KV-cache eviction

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: KV cache eviction, KV-Cache Eviction
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Pareto Frontier](../concepts/accuracy-efficiency-pareto-frontier.md), [AIME](../datasets/aime.md), [GSM8K](../datasets/gsm8k.md), [KV cache compression](../concepts/kv-cache-compression.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [R-KV](r-kv.md)

## Appears in

- [Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence](../../archive/papers/2026/arxiv-2607-20981/summary.md) — A literature survey of efficient vision-language and multimodal inference that argues visual token compression, MoE routing, quantization, KV-cache policy and edge hardware must be co-designed because they form a failure-propagation chain, and proposes Temporal Routing Consistency as a diagnostic for expert jitter in video MoE models.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.
- [Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/title-84172089e3270d37/summary.md) — Identifies which tokens in a large reasoning model's chain-of-thought actually steer the final answer and evicts the Key-Value cache for the rest, cutting memory and latency without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
