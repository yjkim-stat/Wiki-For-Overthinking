# LLaVA-OneVision-7B

<!-- auto:begin -->

An open vision-language model, used by both sources as the second backbone that keeps a claim from resting on a single lineage. One includes it alongside another open model in an audit of perturbation-based selection, where a format-matched control absorbs the apparent gain on both. The other applies a latent-response framework to it and gains 4.5 points, while noting honestly that its chain-of-thought baseline emits unusually few tokens because the model adheres weakly to the instruction — so the efficiency comparison on that backbone is not like-for-like. Neither studies the checkpoint itself.

- **Kind**: model
- **Also called**: LLaVA-OneVision
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [attention pattern](../concepts/attention-pattern.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [GPT-4o](gpt-4o.md), [GRPO](../methods/grpo.md), [Kimi-K2.5](kimi-k2-5.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MathVision](../datasets/mathvision.md), [MMMU](../datasets/mmmu.md), [monitorability](../concepts/monitorability.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL-7B-Instruct](qwen2-5-vl-7b-instruct.md), [selection signal](../concepts/selection-signal.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [verifiable reward](../concepts/verifiable-reward.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) — Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
