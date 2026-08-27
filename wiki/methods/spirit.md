# SPIRIT

<!-- auto:begin -->

Neither source explains SPIRIT's own mechanism; it appears as a named comparison point. REDE instead uses the attention the final answer token pays to each reasoning step as annotation-free supervision, projecting steps into a space where irrelevant or repetitive ones become kNN outliers droppable before hallucination detection; the survey on efficient R1-style reasoning models lists SPIRIT within its taxonomy without elaborating on it here.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAST](dast.md), [DEER](deer.md), [DRP](drp.md), [Early Exit](early-exit.md), [GSM8K (appendix)](../datasets/gsm8k-appendix.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [TruthfulQA](../datasets/truthfulqa.md), [VeriThinker](verithinker.md)

## Appears in

- [Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models](../../archive/papers/2026/arxiv-2607-22098/summary.md) — REDE uses the attention that the final answer token pays to each reasoning step as annotation-free supervision for a lightweight projection, in whose shaped embedding space irrelevant and repetitive steps become kNN outliers that can be dropped before a hallucination detector reads the trace.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
