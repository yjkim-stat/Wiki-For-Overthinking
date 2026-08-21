# Chain-of-Draft

<!-- auto:begin -->

Neither archived source says anything about what Chain-of-Draft is; it is mentioned in passing by two papers whose own contributions lie elsewhere -- A*-Thought, which runs A* search with a bidirectional importance score over the spans of a long trace to select a short high-information subset as fine-tuning data, and a router between thinking and non-thinking models whose threshold is adjusted online by a betting supermartingale. The only thing the archive establishes is the company it keeps: methods that shorten reasoning traces while trying to hold accuracy. A source that describes the method itself is still needed.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [AMC23](../datasets/amc23.md), [BBH](../datasets/bbh.md), [Budget Forcing](budget-forcing.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Distribution Shift](../concepts/distribution-shift.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [QwQ-32B](qwq-32b.md), [Risk Control](../concepts/risk-control.md), [s1K-1.1](../datasets/s1k-1-1.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md)

## Appears in

- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.
- [Anytime Safe PAC Efficient Reasoning](../../archive/papers/2026/title-b525ac9b26640523/summary.md) — Routes queries between a thinking and a non-thinking model with a threshold that is adjusted online by a betting supermartingale, so the accumulated statistical evidence certifies at any stopping time that the accuracy given up stays under a user-specified tolerance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
