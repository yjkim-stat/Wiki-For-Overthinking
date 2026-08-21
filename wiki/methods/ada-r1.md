# Ada-R1

<!-- auto:begin -->

Ada-R1 is a two-stage recipe for per-problem reasoning length: it first merges a long-CoT and a short-CoT model into a single hybrid, then applies bi-level preference training so the model chooses a reasoning style for the problem at the outer level and prefers the shorter correct trace within that style at the inner level. It reports cutting average reasoning length by about 51% across five maths datasets. The archive's survey of efficient R1-style large reasoning models cites it as an instance of single-model optimization but contributes no independent detail.

- **Kind**: method
- **Also called**: Bi-Level Adaptive Reasoning Optimization, Hybrid-CoT
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2025](../datasets/aime-2025.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [DRP](drp.md), [Early Exit](early-exit.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Model Merging](model-merging.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
