# TrimR

<!-- auto:begin -->

TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models, speeding up test-time scaling with little accuracy loss. ReBalance instead reads token-confidence signals to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or lengthen the chain of thought accordingly; both are training-free inference-time interventions, but TrimR trims via verification while ReBalance steers via a learned direction in hidden-state space.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DEER](deer.md), [Dynasor](dynasor.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [SEAL](seal.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [TrimR: Verifier-based Training-Free Thinking Trimming for Efficient Test-Time Scaling](../../archive/papers/2026/title-b987d2649d32f1f3/summary.md) — TrimR is a training-free, verifier-based system that trims redundant chain-of-thought reasoning in deployed large reasoning models to speed up test-time scaling with little accuracy loss.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
