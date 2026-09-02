# LongBench v2

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Also called**: LongBenchv2
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [CommonsenseQA](commonsenseqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [LiveCodeBench-v6](livecodebench-v6.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](math500.md), [NoThinking (baseline)](../methods/nothinking-baseline.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md)

## Appears in

- [S2O: Early Stopping for Sparse Attention via Online Permutation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-351/summary.md) — S2O is a FlashAttention-compatible sparse-attention method for long-context prefill that reorders queries and keys/values via lightweight index arrays (no physical tensor permutation) to concentrate attention mass into a compact region, then applies an online early-stopping rule that skips low-contribution key/value blocks once marginal attention-mass gain falls below a threshold, achieving up to 7.51x attention speedup and 3.81x end-to-end prefill speedup on Llama-3.1-8B at 128K context with lower approximation error than prior sparse-attention baselines.
- [Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-622/summary.md) — A multi-stage training framework (SFT via rejection sampling or trace reformatting, then RL with a reward that penalizes tokens generated after the first correct answer) reduces reasoning-trace length by 28% (Qwen3-8B) to 40% (Qwen3-32B) with only 1.6-2.5 accuracy-point drops, beating prior efficient-reasoning baselines on the Overthinking-Adjusted Accuracy (OAA) AUC metric.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
