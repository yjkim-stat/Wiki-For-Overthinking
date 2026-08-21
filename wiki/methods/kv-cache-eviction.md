# KV-cache eviction

<!-- auto:begin -->

Dropping the key-value cache entries of tokens judged not to matter for what the model still has to produce — one mechanism inside KV-cache compression, the alternative to keeping every entry at lower precision. As with compression, the archive treats it as tangential to overthinking: it reduces the memory and latency cost of serving a reasoning trace, not the length of the trace. DynTS selects the decision-critical tokens of a chain of thought from its attention maps and evicts the cache for the rest, reporting a 2.6% Pass@1 gain over other KV-cache compression at equal budget, 1.84-2.62x lower latency and a 3.32-5.73x smaller peak cache; ThinKV evicts progressively by thought type and finds that a retention floor of zero degrades accuracy sharply, because the model loses track of trajectories it has already explored. The multimodal-inference survey argues the eviction policy cannot be tuned in isolation, since visual token compression, MoE routing, quantization and cache policy form a failure-propagation chain. ThinKV's own measurement that quantization-only compression can inflate generated length up to 5.1x is a reason not to read cache savings as shorter reasoning.

- **Kind**: method
- **Also called**: KV cache eviction, KV-Cache Eviction
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Pareto Frontier](../concepts/accuracy-efficiency-pareto-frontier.md), [AIME](../datasets/aime.md), [GSM8K](../datasets/gsm8k.md), [KV cache compression](kv-cache-compression.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [R-KV](r-kv.md)

## Appears in

- [Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence](../../archive/papers/2026/arxiv-2607-20981/summary.md) — A literature survey of efficient vision-language and multimodal inference that argues visual token compression, MoE routing, quantization, KV-cache policy and edge hardware must be co-designed because they form a failure-propagation chain, and proposes Temporal Routing Consistency as a diagnostic for expert jitter in video MoE models.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.
- [Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/title-84172089e3270d37/summary.md) — Identifies which tokens in a large reasoning model's chain-of-thought actually steer the final answer and evicts the Key-Value cache for the rest, cutting memory and latency without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
