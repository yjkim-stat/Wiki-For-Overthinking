# LogiQA

<!-- auto:begin -->

LogiQA is a logic-heavy classification benchmark used in this archive by Prompt-Level Distillation, which lets compact student models match frontier-model accuracy on it via system-prompt heuristics transferred from a teacher rather than fine-tuning, and by AdaReasoner, an RL-trained plugin that picks a per-task reasoning configuration instead of a single fixed prompting setup.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [GPQA](gpqa.md), [TruthfulQA](truthfulqa.md)

## Appears in

- [Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-industry-142/summary.md) — Prompt-Level Distillation (PLD) transfers a teacher model's reasoning heuristics into a compact student model's system prompt -- via supervised instruction extraction, DBSCAN clustering into a conflict-free instruction set, and a closed-loop conflict-resolution refinement against training failures -- letting Gemma-3 4B and Mistral Small 3.1 match frontier-model (Gemini 3 Flash) accuracy on logic-heavy classification tasks at zero-shot inference speed and no parameter updates.
- [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](../../archive/papers/2025/title-b12c09d1a21e70d0/summary.md) — AdaReasoner is an RL-trained, model-agnostic plugin that picks a per-task reasoning configuration - prompt instruction format, decoding temperature and number of reasoning steps - instead of using one fixed prompting setup for every task.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
