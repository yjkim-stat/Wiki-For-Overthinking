# SEAL

<!-- auto:begin -->

Neither source explains SEAL's own mechanism; the survey on efficient R1-style reasoning models lists it as one instance within its single-model/multi-model taxonomy, and ReBalance mentions it only in passing while describing its own training-free steering-vector method for correcting overthinking or underthinking from token confidence.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](activation-steering.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DEER](deer.md), [DRP](drp.md), [Dynasor](dynasor.md), [Early Exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
