# attention sink

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [H2O (baseline)](../methods/h2o-baseline.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MATH500](../datasets/math500.md), [Qwen3-1.7B](../models/qwen3-1-7b.md)

## Appears in

- [Prefix Sliding for efficient test-time scaling](../../archive/papers/2026/arxiv-2608-26070/summary.md) — Prefix Sliding discards reasoning tokens outside a prefix (system instructions/prompt) plus a sliding window of the most recent tokens, giving constant per-token generation cost that lets language models reason for arbitrarily long horizons -- 3x faster than full attention without training, and enabling RL rollouts beyond 100,000 tokens with better reward than full-attention training at equal memory.
- [ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-76/summary.md) — ZoomR fine-tunes a reasoning model to summarize its own thoughts after each paragraph, then at inference dynamically retrieves only a small, consensus-selected subset of full-resolution reasoning segments (zooming in) while keeping the rest as compressed summary keys -- cutting KV-cache GPU memory more than 4x versus a full cache with accuracy close to the vanilla full-KV baseline, and finds that attention-head consensus on which segments matter is itself a diagnostic signal correlated with answer correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
