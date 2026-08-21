# activation steering

<!-- auto:begin -->

Controlling how long or how a reasoning model thinks by directly modifying its internal activations at inference time, rather than by prompting or retraining it. The archived sources use it two ways: modeling the chain-of-thought as transitions among latent cognitive states and steering generation toward more efficient state transitions, and identifying overthinking as movement along a low-dimensional manifold in activation space and projecting activations to counteract it (cutting output tokens up to 71% while maintaining or improving accuracy).

- **Kind**: method
- **Also called**: Activation Steering, manifold steering, representation engineering
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DEER](deer.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH-500](../datasets/math-500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [SEAL](seal.md), [StrategyQA](../datasets/strategyqa.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Base Models Know How to Reason, Thinking Models Learn When](../../archive/papers/2026/title-04d88374347ad37c/summary.md) — By decomposing the base-to-thinking model difference into reasoning mechanisms (steering vectors that induce a behaviour) and reasoning heuristics (a classifier deciding when the behaviour fires), the paper finds that hybrid models recover about 76% of the RL base-to-thinking gap but only about 11% of the SFT-distillation gap, indicating RL mainly teaches when to invoke reasoning behaviours the base model already has.
- [Modeling Hierarchical Thinking in Large Reasoning Models](../../archive/papers/2026/title-7651639ee2f29946/summary.md) — Models a large reasoning model's chain-of-thought as transitions among six latent cognitive states and uses that abstraction to steer generation toward better reasoning policies at inference time, without training.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
