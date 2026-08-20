# activation steering

<!-- auto:begin -->

Controlling how long or how a reasoning model thinks by directly modifying its internal activations at inference time, rather than by prompting or retraining it. The archived sources use it two ways: modeling the chain-of-thought as transitions among latent cognitive states and steering generation toward more efficient state transitions, and identifying overthinking as movement along a low-dimensional manifold in activation space and projecting activations to counteract it (cutting output tokens up to 71% while maintaining or improving accuracy).

- **Kind**: method
- **Also called**: manifold steering, representation engineering
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Manifold Steering](manifold-steering.md), [MATH-500](../datasets/math-500.md), [overthinking](../concepts/overthinking.md)

## Appears in

- [Modeling Hierarchical Thinking in Large Reasoning Models](../../archive/papers/2026/title-7651639ee2f29946/summary.md) — Models a large reasoning model's chain-of-thought as transitions among six latent cognitive states and uses that abstraction to steer generation toward better reasoning policies at inference time, without training.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
