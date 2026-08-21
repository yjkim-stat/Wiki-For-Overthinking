# A*-Thought

<!-- auto:begin -->

A*-Thought is a data-construction method for compressing chain-of-thought supervision: it treats an already-generated long reasoning trace as a search tree over reasoning spans and runs A* search, guided by a bidirectional importance score, to select a short high-information subset of that trace. The selected subset is then used as supervised fine-tuning data so a model reasons in fewer tokens, which the paper frames as a low-resource setting. The archive's survey of efficient R1-style reasoning models is the only other source that mentions it, and only as one entry in its taxonomy of single-model optimization; it adds no numbers of its own.

- **Kind**: method
- **Also called**: A*-Thought
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AMC23](../datasets/amc23.md), [Chain-of-Draft](chain-of-draft.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [DEER](deer.md), [DRP](drp.md), [early exit](early-exit.md), [GSM8K](../datasets/gsm8k.md), [LASER](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH-500](../datasets/math-500.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [QwQ-32B](qwq-32b.md), [S-GRPO](s-grpo.md), [s1K-1.1](../datasets/s1k-1-1.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [Thinkless](thinkless.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
