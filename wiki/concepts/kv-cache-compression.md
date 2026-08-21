# KV cache compression

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Also called**: KV-cache compression
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [confidence-based early stopping](../methods/confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](../datasets/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](../datasets/deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [KV-cache eviction](../methods/kv-cache-eviction.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [overthinking](overthinking.md), [process reward model](process-reward-model.md), [Qwen3-8B](../datasets/qwen3-8b.md), [R-KV](../methods/r-kv.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](../../archive/papers/2026/title-3663586d2c722911/summary.md) — A training-free KV-cache compression method for long reasoning-model inference that preserves the distant context tokens later reasoning steps revisit, using clustered 'beacon queries'.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
