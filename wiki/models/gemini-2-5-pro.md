# Gemini-2.5-pro

<!-- auto:begin -->

A frontier proprietary model, present in both sources as a comparison point rather than a subject. One evaluates it among twenty-plus models as a translation-quality judge. The other reports it among the vision-language baselines on a table-to-report benchmark, where it is the strongest of that group at 60.0 overall against a human expert's 91. Neither characterizes the checkpoint; its function in both is to mark where the closed frontier sat when the measurement was taken.

- **Kind**: model
- **Also called**: Gemini 2.5 Pro, Gemini-2.5-Pro
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [Aya-expanse-8B](aya-expanse-8b.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [exploration](../concepts/exploration.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPT-4](gpt-4.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GPT-5](gpt-5.md), [grounding](../concepts/grounding.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [Llama-3-8B-Instruct](llama-3-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [process reward](../concepts/process-reward.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-VL-235B](qwen3-vl-235b.md), [reward hacking](../concepts/reward-hacking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../methods/test-time-scaling.md), [verifiable reward](../concepts/verifiable-reward.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [Monte Carlo Tree Search for Table-to-Multimodal Report Generation](../../archive/papers/2026/arxiv-2608-04071/summary.md) — Turns table-to-report generation into Monte Carlo tree search over partial reports, scored by a reward that verifies every numerical claim by generating and executing SQL against the source table rather than by asking a judge — and keeps that search reward strictly separate from the benchmark's own evaluator to avoid a reward-hacking loop.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
