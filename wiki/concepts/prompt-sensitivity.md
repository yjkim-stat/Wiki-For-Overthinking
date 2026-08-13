# prompt sensitivity

<!-- auto:begin -->

How much a measured result depends on the exact wording of the prompt rather than on the capability being measured, and in both sources a finding about evaluation rather than a nuisance to be tuned away. One shows the field's standard translation-evaluation prompt is specialized to the model it was written for: all other models, including that model's own successor, perform significantly worse under it, and enforcing a structured output format degrades quality across every model tested, worst in the smallest. The other measures robustness over raw accuracy on theory-of-mind tasks. The shared implication for this archive is that a prompt carried from the paper that introduced it is part of the apparatus, not a neutral interface, and a model comparison run under one authored elsewhere may be measuring the fit between prompt and model.

- **Kind**: concept
- **Also called**: prompt brittleness
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [construct validity](construct-validity.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [GPT-4](../models/gpt-4.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3-70B-Instruct](../models/llama-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [RLVR](../methods/rlvr.md), [robustness](robustness.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning](../../archive/papers/2026/arxiv-2608-04646/summary.md) — Tests reasoning models on Theory of Mind tasks and argues their gains are increased robustness to prompt and task perturbation rather than a new ToM-specific ability.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
