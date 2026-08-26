# S-GRPO

<!-- auto:begin -->

The two sources that mention S-GRPO do not explain its mechanism: the survey on efficient R1-style reasoning models includes it as one instance in its taxonomy of single-model-optimization methods, and IAPO cites it only in comparison while describing its own token-level mutual-information reward shaping. S-GRPO's own approach is not described in the material supplied here.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAST](dast.md), [DEER](deer.md), [DRP](drp.md), [Early Exit](early-exit.md), [GFPO](gfpo.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
