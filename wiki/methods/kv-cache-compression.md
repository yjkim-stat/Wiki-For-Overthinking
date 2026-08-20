# KV cache compression

<!-- auto:begin -->

Shrinking the stored key and value states of earlier tokens so long-context decoding fits in memory, by evicting, merging or quantizing them. The two sources approach it from opposite ends. One treats it as an efficiency method to improve, making the compression policy vary along the trajectory under a process-reward signal — compressing harder at high-reward steps and less at low-reward ones — and reports 37% to 65% fewer generated tokens with 2.08x to 2.35x lower end-to-end latency. The other evaluates eleven existing methods and finds the standard success criterion misleading: token-eviction methods can hold competitive final-answer accuracy while destroying the reasoning that supports it, whereas a quantization control that keeps every token stays close to the uncompressed model on every metric. Together they mark the distinction that matters for reasoning models — which tokens stay reachable, not how many bits each one costs.

- **Kind**: method
- **Also called**: KV cache eviction, KV compression
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [auditability](../concepts/auditability.md), [causal intervention](causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [early exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LLM-as-a-judge](llm-as-a-judge.md), [MedCalc-Bench](../datasets/medcalc-bench.md), [overthinking](../concepts/overthinking.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [process reward](../concepts/process-reward.md), [process reward model](process-reward-model.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md)

## Appears in

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
