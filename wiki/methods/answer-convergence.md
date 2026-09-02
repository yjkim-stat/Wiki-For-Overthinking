# Answer Convergence

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: answer convergence
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Budget Forcing](budget-forcing.md), [Chain-of-Draft](chain-of-draft.md), [Concise CoT (CCoT)](concise-cot-ccot.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [Dynasor](dynasor.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [NoThinking](nothinking.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Early Stopping for Large Reasoning Models via Confidence Dynamics](../../archive/papers/2026/local-204ad034bca12641/summary.md) — CoDE-Stop stops reasoning when either a ramping confidence threshold is crossed or an early-step-weighted 'degeneration score' of accumulated confidence instability exceeds a threshold, targeting both trajectories that are already done and trajectories that are going nowhere, and its evaluation is the archive's first independent head-to-head of RCPD and Answer Convergence under one protocol.
- [Answer Convergence as a Signal for Early Stopping in Reasoning](../../archive/papers/2025/local-5596d5f3510679fc/summary.md) — Defines the Answer Convergence Ratio — the fraction of a chain of thought needed before the forced answer stops changing — measures it by incremental truncation across five tasks and five models, and proposes three inference-time stopping methods (answer consistency, a logit boost on the end-of-thinking token, and an LSTM probe over activations), of which only the learned probe holds accuracy on hard tasks.
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](../../archive/papers/2026/local-8ec022e440eb9021/summary.md) — Proposes PUMA, an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
