# Dynasor

<!-- auto:begin -->

A reasoning-aware serving system that schedules on certaindex, a normalized measure of how far a reasoning algorithm's answer has stabilized, defined for both multi-path methods (via semantic entropy over clustered answers) and reward-guided ones (via normalized reward). It reports up to 50% compute savings in batch inference and 3.3x throughput in online serving. Two other sources use it as a baseline and both find it conservative — it preserves reasoning quality but exits late enough that length reduction is small — which follows from it being tuned for no accuracy loss by construction.

- **Kind**: method
- **Also called**: Certaindex, Dynasor, Dynasor-CoT
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [chain of thought](chain-of-thought.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [early exit](early-exit.md), [entropy trajectory](../concepts/entropy-trajectory.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [overthinking](../concepts/overthinking.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
