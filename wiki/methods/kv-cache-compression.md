# KV cache compression

<!-- auto:begin -->

Shrinking the stored key-value tensors of an already-generated reasoning trace — by quantizing them, by evicting entries, or both — so that long chain-of-thought inference fits in memory and runs faster. The archive files this as tangential to overthinking: it cuts the serving cost of whatever trace the model produces and does not decide how long that trace is. The three sources vary the retention policy: BeaconKV is training-free and keeps the distant early context that later reasoning steps revisit, using clustered 'beacon queries', for up to 5.8x memory reduction and over 4.3x throughput; ThinKV labels segments of the trace by thought type and applies per-type quantization plus progressive eviction, staying near full-cache accuracy at under 5% of the cache; ReCo drives the per-step retention ratio from a 30M process-reward estimator and pairs it with generation-side controls, cutting tokens 37-65% and latency 2.08-2.35x. Two archived measurements cut against reading compression as an efficiency win in the overthinking sense: ReCo reports cache-only baselines increasing generated tokens rather than reducing them (SnapKV goes from 7,078 to 11,266 tokens on Llama-8B), and ThinKV measures quantization inflating generated length by up to 5.1x across datasets and techniques.

- **Kind**: method
- **Also called**: KV-cache compression
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [confidence-based early stopping](confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [KV-cache eviction](kv-cache-eviction.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH-500](../datasets/math-500.md), [overthinking](../concepts/overthinking.md), [process reward model](../concepts/process-reward-model.md), [Qwen3-8B](qwen3-8b.md), [R-KV](r-kv.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](../../archive/papers/2026/title-3663586d2c722911/summary.md) — A training-free KV-cache compression method for long reasoning-model inference that preserves the distant context tokens later reasoning steps revisit, using clustered 'beacon queries'.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
