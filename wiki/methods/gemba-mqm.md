# GEMBA-MQM

<!-- auto:begin -->

A prompting framework that has a language model mark individual error spans in a translation and label each with a category and severity, from which a quality score is derived automatically rather than asked for directly. Both sources use it as the standard instrument and both find something wrong with it as an instrument. One reports that its prompt is specialized to the model it was written for — every other model, including that model's own successor, performs significantly worse under it — and that its lack of an explicit output specification leaves 10% of outputs from a strong model and 85% from a 4B one with formatting errors that fragile parsers must guess at. The other adopts it as the automatic annotator for its own error analysis without qualification. The pair is a caution about inherited evaluation apparatus: the same framework is simultaneously the field's standard and, on measurement, model-specific.

- **Kind**: method
- **Also called**: GEMBA, Gemba-MQM
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-V3](../models/deepseek-v3.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPT-4](../models/gpt-4.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5](../models/gpt-5.md), [GRPO](grpo.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [Llama-3-70B-Instruct](../models/llama-3-70b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [long chain-of-thought distillation](long-chain-of-thought-distillation.md), [LoRA](lora.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher forcing](teacher-forcing.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
