# reasoning hallucination

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Also called**: Reasoning Hallucination
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [MATH500](../datasets/math500.md), [minervamath](../datasets/minervamath.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [routing collapse](routing-collapse.md)

## Appears in

- [RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-885/summary.md) — RFS-Guard detects and localizes reasoning hallucinations in LRMs training-free, using a Routing Focus Score (RFS) that measures how strongly cross-step attention between reasoning and answer phases collapses toward semantic-neighbor proximity (rather than task-critical evidence) -- finding this 'routing collapse' is a strong hallucination signal that beats sampling-based, uncertainty-based, and other self-aware baselines while remaining far more inference-efficient.
- [Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models](../../archive/papers/2026/title-c5959780286b4ea6/summary.md) — Introduces the Reasoning Score, a metric based on divergence between logits from late-layer projections onto the vocabulary space, to detect 'Reasoning Hallucination' -- logically coherent but factually wrong reasoning chains -- and pairs it with GRPO-R, an RL method using step-level deep-reasoning rewards to reduce it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
