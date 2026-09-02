# Chain-of-Draft

<!-- auto:begin -->

Neither archived source says anything about what Chain-of-Draft is; it is mentioned in passing by two papers whose own contributions lie elsewhere -- A*-Thought, which runs A* search with a bidirectional importance score over the spans of a long trace to select a short high-information subset as fine-tuning data, and a router between thinking and non-thinking models whose threshold is adjusted online by a betting supermartingale. The only thing the archive establishes is the company it keeps: methods that shorten reasoning traces while trying to hold accuracy. A source that describes the method itself is still needed.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [A*-Thought](a-thought.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Answer Convergence](../concepts/answer-convergence.md), [BBH](../datasets/bbh.md), [Budget Forcing](budget-forcing.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DEER](deer.md), [Distribution Shift](../concepts/distribution-shift.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [NoThinking](nothinking.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [QwQ-32B](../models/qwq-32b.md), [Risk Control](../concepts/risk-control.md), [s1k-1.1](../datasets/s1k-1-1.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md)

## Appears in

- [Early Stopping for Large Reasoning Models via Confidence Dynamics](../../archive/papers/2026/local-204ad034bca12641/summary.md) — CoDE-Stop stops reasoning when either a ramping confidence threshold is crossed or an early-step-weighted 'degeneration score' of accumulated confidence instability exceeds a threshold, targeting both trajectories that are already done and trajectories that are going nowhere, and its evaluation is the archive's first independent head-to-head of RCPD and Answer Convergence under one protocol.
- [A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings](../../archive/papers/2025/title-6ac5c2757444abad/summary.md) — A*-Thought treats a long reasoning trace as a search tree over reasoning spans and uses A* search with a bidirectional importance score to select a short, high-information subset of it as supervised fine-tuning data for compressed reasoning.
- [Anytime Safe PAC Efficient Reasoning](../../archive/papers/2026/title-b525ac9b26640523/summary.md) — Routes queries between a thinking and a non-thinking model with a threshold that is adjusted online by a betting supermartingale, so the accumulated statistical evidence certifies at any stopping time that the accuracy given up stays under a user-specified tolerance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
