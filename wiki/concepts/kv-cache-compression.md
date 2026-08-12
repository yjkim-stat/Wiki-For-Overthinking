# KV cache compression

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [auditability](auditability.md), [causal intervention](causal-intervention.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [overthinking](overthinking.md), [post-hoc rationalization](post-hoc-rationalization.md), [process reward](process-reward.md), [process reward model](../methods/process-reward-model.md), [reasoning redundancy](reasoning-redundancy.md)

## Appears in

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
