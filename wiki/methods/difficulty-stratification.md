# difficulty stratification

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [ARC-Challenge](../datasets/arc-challenge.md), [best-of-n](best-of-n.md), [calibration](calibration.md), [component ablation](component-ablation.md), [coverage](../concepts/coverage.md), [cross-validation](cross-validation.md), [difficulty conditioning](../concepts/difficulty-conditioning.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](../concepts/hallucination.md), [HMMT 2025](../datasets/hmmt-2025.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [majority voting](majority-voting.md), [MATH](../datasets/math.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reward shaping](../concepts/reward-shaping.md), [selection signal](../concepts/selection-signal.md), [selective prediction](../concepts/selective-prediction.md), [self-certainty](self-certainty.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [self-reflection](self-reflection.md), [StrategyQA](../datasets/strategyqa.md), [structured chain of thought](structured-chain-of-thought.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [verifier-free verification](verifier-free-verification.md)

## Appears in

- [REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment](../../archive/papers/2026/arxiv-2608-07931/summary.md) — Separates hallucination into a reasoning failure and a knowledge failure, treats the first with a structured reflect-before-answering format and the second with a reward for abstaining when no sampled chain succeeds, and shows the two mechanisms are not interchangeable -- reflection alone never abstains, abstention alone never lowers the hallucination proxy.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Shows that selecting the most confident rollout can be worse than picking at random, because uniformly high confidence signals a failure to explore rather than a well-supported answer, and replaces maximisation with a temporal criterion that penalises early certainty while requiring late certainty.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
