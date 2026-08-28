# DEER (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink (baseline)](adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-Challenge](../datasets/arc-challenge.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Dynasor-CoT (baseline)](dynasor-cot-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [MATH500](../datasets/math500.md), [NoThinking (baseline)](nothinking-baseline.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](phi-4-reasoning.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Thinking](../models/qwen3-4b-thinking.md), [Qwen3-8B](../models/qwen3-8b.md), [Reasoning Collapse](../concepts/reasoning-collapse.md), [Thinkless (baseline)](thinkless-baseline.md)

## Appears in

- [ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1095/summary.md) — ThinkBrake is a training-free decoding rule that injects </think> at sentence boundaries whenever the log-probability margin between the top continuation token and </think> narrows below a threshold, recovering most of an oracle stopping point's headroom (8% accuracy gain, 72% token reduction) with a theoretically grounded, model-agnostic criterion, and its generated trajectories can also train models via DPO for training-free-free efficient reasoning.
- [NEAT: Neuron-Based Early Exit for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1231/summary.md) — NEAT identifies a sparse set of 'exit-associated neurons' whose FFN activation dynamics causally predict the </think> termination token, then monitors these neurons training-free during inference to trigger graded early exit or reflection suppression -- cutting average token generation 22-28% across four benchmarks and six models with accuracy comparable to vanilla decoding, and 21-23% real wall-clock latency reduction versus vanilla and CGRS (which is 41-63% slower than vanilla despite shortening output, due to its own scoring overhead).
- [PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1545/summary.md) — PACE identifies two distinct failure modes of uniform length-penalty RL for efficient reasoning -- sequence-level over-compression of critical early deduction steps, and group-level indiscriminate compression that ignores query difficulty -- and fixes both with a frozen-policy prefix-rollout anchor (decaying over training) plus a pass-rate-derived, difficulty-scaled length penalty, becoming the only compared method to cut token usage over 45% while simultaneously improving accuracy, and generalizing to code, science and instruction-following domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
