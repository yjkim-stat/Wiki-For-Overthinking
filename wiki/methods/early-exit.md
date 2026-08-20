# early exit

<!-- auto:begin -->

Stopping a reasoning model's generation before it reaches a natural end, once an internal or external signal indicates the answer is already settled, to avoid spending tokens on unproductive continued reasoning. The 'Don't Overthink It' survey categorizes early exit (monitoring-based, generation-control-based, and RL-based variants) as one of its four families of overthinking mitigation; SpecExit implements it via a speculative-decoding-style draft model that predicts both the next tokens and an early-exit signal, cutting generation length up to 66% with a 2.5x speedup.

- **Kind**: method
- **Also called**: speculative exit
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [budget forcing](budget-forcing.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [speculative decoding](speculative-decoding.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [SpecExit: Accelerating Large Reasoning Model via Speculative Exit](../../archive/papers/2026/title-1bb8d328d6b8e7ac/summary.md) — Uses a speculative-decoding-style draft model to predict both next tokens and an early-exit signal, letting a large reasoning model stop generating once its own internal representations indicate reasoning is done.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
