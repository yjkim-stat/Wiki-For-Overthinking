# PLAN-AND-BUDGET

<!-- auto:begin -->

A test-time-compute method that decomposes a query into sub-questions and allocates a token budget to each based on estimated complexity, rather than spending a single undifferentiated budget on the whole problem. Its source paper reports up to 70% accuracy gain and 39% token reduction; the 'Don't Overthink It' survey lists it among its long-short model collaboration / adaptive-reasoning methods.

- **Kind**: method
- **Also called**: PLAN-AND-BUDGET, Plan-and-Budget
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Answer Convergence](answer-convergence.md), [Budget Forcing](budget-forcing.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Concise CoT (CCoT)](concise-cot-ccot.md), [DAST](dast.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [DRP](drp.md), [Dynasor](dynasor.md), [Early Exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Laser](laser.md), [LC-R1](lc-r1.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [underthinking](../concepts/underthinking.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](../../archive/papers/2026/local-8ec022e440eb9021/summary.md) — Proposes PUMA, an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.
- [Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models](../../archive/papers/2026/title-f0073c841a41fca9/summary.md) — Plan-and-Budget decomposes queries into sub-questions and allocates test-time token budgets by estimated complexity, using a theoretical model of reasoning as sequential sub-questions to reduce both overthinking and underthinking.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
