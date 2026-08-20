# out-of-domain generalization

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [annotation agreement](annotation-agreement.md), [benchmark contamination](benchmark-contamination.md), [BigCodeBench](../datasets/bigcodebench.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [credit assignment](credit-assignment.md), [cross-validation](../methods/cross-validation.md), [decontamination](../methods/decontamination.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [detection versus control](detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [distribution shift](distribution-shift.md), [few-shot prompting](../methods/few-shot-prompting.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.4](../models/gpt-5-4.md), [GRPO](../methods/grpo.md), [human evaluation](../methods/human-evaluation.md), [HumanEval+](../datasets/humaneval.md), [identifiability](identifiability.md), [interpretability illusion](interpretability-illusion.md), [knowledge distillation](../methods/knowledge-distillation.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [matched-budget comparison](matched-budget-comparison.md), [MBPP+](../datasets/mbpp.md), [McNemar test](../methods/mcnemar-test.md), [measurement invariance](measurement-invariance.md), [operating point](operating-point.md), [outcome reward](outcome-reward.md), [paired bootstrap](../methods/paired-bootstrap.md), [process reward](process-reward.md), [Qwen](../models/qwen.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reasoning depth](reasoning-depth.md), [reward shaping](reward-shaping.md), [selection bias](selection-bias.md), [structured chain of thought](../methods/structured-chain-of-thought.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [visual grounding](visual-grounding.md)

## Appears in

- [On the Robustness of LLMs' Internal Representation of Code Correctness](../../archive/papers/2026/arxiv-2608-08266/summary.md) — Asks whether a published internal signal for code correctness is a property of the model or of the one extraction recipe used to find it, sweeps every design choice systematically, and finds no configuration is best anywhere -- with the benchmark deciding which choice wins, and a mismatched fitting source able to drive the signal below chance.
- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) — Compares chain-of-thought against answer-only supervision under a protocol where the two conditions differ in nothing but the training target, and finds the rationales buy nothing in-domain for strong backbones while buying 20 to 28 points out of domain -- with a human study attributing the measurable effect to language adherence and inspectability rather than to better reasoning.
- [SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](../../archive/papers/2026/arxiv-2608-12220/summary.md) — Splits a spatial-reasoning chain of thought into explicitly typed segments -- perception, including depth, and reasoning -- and gives each its own process reward and its own advantage term, so that the two do not compete for credit under a single outcome signal.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
