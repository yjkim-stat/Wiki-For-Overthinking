# R-KV

<!-- auto:begin -->

R-KV is a KV-cache compression method for reasoning models that both citing papers use as a baseline without describing its mechanism; the closest the archive comes is ReCo's characterisation of reasoning-oriented compressors in general as applying one uniform policy across the whole trajectory and scoring themselves only by what they evict. What the archive does record is how it performs against newer work: ThinKV's main setting retains 2.51% of the full cache against R-KV's 5.48% and reports up to 5.8x throughput over it (8,412 against 1,450.5 tokens/sec on an A100). ReCo uses it to demonstrate that cache compression inflates generation -- at a 25% R-KV retention rate on MATH-500, average output rises from 3,268.7 to 4,538.1 tokens (+38.8%) on DeepSeek-R1-Distill-Qwen-7B and from 4,409.8 to 7,891.7 (+79.0%) on Llama-8B, with 79.8% of problems longer than full cache -- and reports R-KV accuracy falling to 48.1% on Llama-8B where ReCo holds 60.2%. How it decides what to evict is not stated anywhere in the archive.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Confidence-based early stopping](confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Dynasor](dynasor.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [KV-cache compression](kv-cache-compression.md), [KV cache eviction](kv-cache-eviction.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](../../archive/papers/2026/title-3a1fb8083fa0ff85/summary.md) — A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
