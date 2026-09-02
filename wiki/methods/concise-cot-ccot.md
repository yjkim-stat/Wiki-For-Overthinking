# Concise CoT (CCoT)

<!-- auto:begin -->

Concise CoT is a prompt-level length control used in this archive only as a baseline: the prompt itself imposes a token budget on the reasoning, with no change to the model or the decoding rule. Both sources run it as the prompting-side comparison against their own inference-time stopping methods, one of them fixing the budget at 100 tokens for every task. In that comparison it cuts tokens substantially but at an accuracy cost that grows with task difficulty — on R1-distilled Qwen-32B it moves NaturalQuestions from 35.0 to 37.2 accuracy at 41.6% fewer tokens, while on AIME'24 it drops accuracy from 73.3 to 60.0 for a similar 42.5% saving — which is the standing argument in these sources for making the budget instance-specific rather than fixed in the prompt.

- **Kind**: method
- **Also called**: CCoT
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Answer Convergence](../concepts/answer-convergence.md), [Budget Forcing](budget-forcing.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [Dynasor](dynasor.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Answer Convergence as a Signal for Early Stopping in Reasoning](../../archive/papers/2025/local-5596d5f3510679fc/summary.md) — Defines the Answer Convergence Ratio — the fraction of a chain of thought needed before the forced answer stops changing — measures it by incremental truncation across five tasks and five models, and proposes three inference-time stopping methods (answer consistency, a logit boost on the end-of-thinking token, and an LSTM probe over activations), of which only the learned probe holds accuracy on hard tasks.
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](../../archive/papers/2026/local-8ec022e440eb9021/summary.md) — Proposes PUMA, an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
