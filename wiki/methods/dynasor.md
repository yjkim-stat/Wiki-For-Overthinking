# Dynasor

<!-- auto:begin -->

A system that terminates or reallocates reasoning compute per query using a measure of how much the answer has stopped changing, appearing across 3 sources as both a method and a baseline. Its reported effect is large where the saving is the goal -- up to 50 percent of tokens in batch inference and roughly tripled online throughput in the source that introduces the underlying measure. As a baseline it is beaten on accuracy by later stopping rules: one early-exit comparison reports it at 58.70 percent against a competitor's 63.06 averaged across three models and three benchmarks. The archive's related caution is that a stopping rule reading the model's own convergence inherits its calibration, and stabilisation and correctness come apart on hard problems.

- **Kind**: method
- **Also called**: Certaindex, Dynasor, Dynasor-CoT
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [BigCodeBench](../datasets/bigcodebench.md), [chain of thought](../concepts/chain-of-thought.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [early exit](early-exit.md), [entropy trajectory](../concepts/entropy-trajectory.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-70B](../models/llama-3-1-70b.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [predictive entropy](../concepts/predictive-entropy.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [self-consistency](self-consistency.md), [semantic entropy](semantic-entropy.md), [test-time compute](../concepts/test-time-compute.md), [token-level entropy](../concepts/token-level-entropy.md), [vLLM](vllm.md)

## Appears in

- [Efficiently Scaling LLM Reasoning with Certaindex](../../archive/papers/2025/local-0c24c3c0e4729108/summary.md) — Defines certaindex, an algorithm-agnostic measure of how much a reasoning algorithm's answer has stopped changing, and builds it into a serving system that reallocates or terminates compute per query — saving up to 50% of tokens in batch inference and tripling online throughput.
- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
