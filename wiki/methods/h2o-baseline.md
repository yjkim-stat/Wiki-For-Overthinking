# H2O (baseline)

<!-- auto:begin -->

H2O (Heavy-Hitter Oracle) is used in these sources as a dynamic, attention-score-based KV-cache token-selection baseline that alternatives are compared against: ZoomR benchmarks its multi-granularity consensus-based cache selection against H2O (and StreamingLLM) at matched GPU-memory budgets, outperforming both; the greedy-pruning functional-importance study does not name H2O specifically in its own cited note.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [attention sink](../concepts/attention-sink.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LoRA fine-tuning](lora-fine-tuning.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [TokenSkip (baseline)](tokenskip-baseline.md)

## Appears in

- [Do LLMs Encode Functional Importance of Reasoning Tokens ?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1419/summary.md) — Introduces greedy pruning, a likelihood-preserving token-deletion diagnostic that reveals LLMs encode a nontrivial token-level functional-importance structure in their reasoning chains -- preferentially preserving symbolic computation over referential/linguistic scaffolding -- and shows students distilled on greedily-pruned chains outperform a frontier-model-supervised pruning baseline (TokenSkip) at matched lengths.
- [ZoomR: Memory Efficient Reasoning through Multi-Granularity Key Value Retrieval](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-76/summary.md) — ZoomR fine-tunes a reasoning model to summarize its own thoughts after each paragraph, then at inference dynamically retrieves only a small, consensus-selected subset of full-resolution reasoning segments (zooming in) while keeping the rest as compressed summary keys -- cutting KV-cache GPU memory more than 4x versus a full cache with accuracy close to the vanilla full-KV baseline, and finds that attention-head consensus on which segments matter is itself a diagnostic signal correlated with answer correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
