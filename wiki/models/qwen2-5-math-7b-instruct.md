# Qwen2.5-Math-7B-Instruct

<!-- auto:begin -->

A mathematics-specialised 7B instruction-tuned model, and in this archive the case where a strong domain-specific backbone changes what a method is worth. In the self-correction work it is the backbone with the largest out-of-domain gains of the seven tested -- 10.9 points on a competition set and 8.8 on an undergraduate one -- while its in-domain gains are among the smallest, which is the pattern of a model already near its in-domain ceiling. In the Bangla supervision study it is one of the strong backbones for which chain-of-thought rationales buy nothing in domain while buying 20 to 28 points out of domain, with a human study attributing the measurable effect to language adherence and inspectability rather than to better reasoning. The two agree on the shape: for a specialised backbone the value of extra supervision is entirely in transfer.

- **Kind**: model
- **Also called**: Qwen2.5-Math-7B-Instruct
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [annotation agreement](../concepts/annotation-agreement.md), [benchmark contamination](../concepts/benchmark-contamination.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [decontamination](../methods/decontamination.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [distribution shift](../concepts/distribution-shift.md), [DPO](../methods/dpo.md), [error detection](../concepts/error-detection.md), [few-shot prompting](../methods/few-shot-prompting.md), [GPT-4o](gpt-4o.md), [GPT-5.4](gpt-5-4.md), [GSM8K](../datasets/gsm8k.md), [human evaluation](../methods/human-evaluation.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH](../datasets/math.md), [McNemar test](../methods/mcnemar-test.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [out-of-domain generalization](../concepts/out-of-domain-generalization.md), [paired bootstrap](../methods/paired-bootstrap.md), [process reward](../concepts/process-reward.md), [Qwen2.5-14B-Instruct](qwen2-5-14b-instruct.md), [Qwen3-8B](qwen3-8b.md), [reasoning depth](../concepts/reasoning-depth.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md)

## Appears in

- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) — Compares chain-of-thought against answer-only supervision under a protocol where the two conditions differ in nothing but the training target, and finds the rationales buy nothing in-domain for strong backbones while buying 20 to 28 points out of domain -- with a human study attributing the measurable effect to language adherence and inspectability rather than to better reasoning.
- [Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs](../../archive/papers/2026/arxiv-2608-11573/summary.md) — Trains self-correction as a step-level preference problem -- preferring a detect-and-repair continuation over the continuation that would follow if the error went unaddressed -- after first initialising with ordinary step-level preference optimisation, and finds that correcting more often and detecting more errors both anti-correlate with accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
