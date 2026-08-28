# entropy collapse

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-Challenge](../datasets/arc-challenge.md), [DAPO-Math-17k (training)](../datasets/dapo-math-17k-training.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [HumanEval](../datasets/humaneval.md), [IFEval](../datasets/ifeval.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [Minerva](../datasets/minerva.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [TACO](../datasets/taco.md)

## Appears in

- [Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-617/summary.md) — CurioSFT diagnoses that standard SFT causes 'entropy collapse' (overconfidence, narrowed exploration) that limits the subsequent RL stage in the SFT-then-RL pipeline, and fixes it with Self-Exploratory Distillation toward a self-generated, temperature-scaled teacher plus Entropy-Guided Temperature Selection that concentrates exploration on high-entropy reasoning-connector tokens while preserving low-entropy factual tokens, improving downstream RL accuracy by 5.0 points on average.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1266/summary.md) — A systematic study of entropy collapse in GRPO-based RLVR training finds performance can improve without entropy loss (so entropy collapse is not merely a side effect of legitimate learning), identifies clipping thresholds, off-policy update count, and training-data diversity as governing factors, proves theoretically and confirms empirically that positive-advantage tokens are the primary driver of entropy collapse, and proposes Positive-Advantage Reweighting -- dynamically down-weighting positive-advantage-token loss -- to regulate entropy while maintaining performance, though training exclusively on non-positive-advantage tokens actually hurts benchmark scores despite reducing collapse.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
