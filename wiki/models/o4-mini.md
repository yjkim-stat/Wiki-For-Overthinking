# o4-mini

<!-- auto:begin -->

A small OpenAI reasoning model appearing twice in this archive as a subject of evaluation. In the translation-quality benchmark it is one of over twenty models scored as MQM judges under a single prompt, in a study whose headline findings are that reasoning models make the best judges, that a jury of different ones beats any member, and that the field's standard prompt is specialised to the model it was written for. In the reasoning-trace extraction work it appears in the cross-model compatibility map -- its encrypted traces are replayable by the newer GPT-5.6 series but it accepts only its own -- and it is the model used to capture a reasoning block that had internalised an instruction, which was then replayed into a much larger sibling on an unrelated task. Neither source describes the model itself.

- **Kind**: model
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [Aya-expanse-8B](aya-expanse-8b.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Claude Haiku 4.5](claude-haiku-4-5.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [Claude Sonnet 4.6](claude-sonnet-4-6.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [Gemma-3-4B-it](gemma-3-4b-it.md), [GPT-4](gpt-4.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [GPT-5-mini](gpt-5-mini.md), [GPT o3](gpt-o3.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [jury aggregation](../methods/jury-aggregation.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [Llama-3-8B-Instruct](llama-3-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [monitorability](../concepts/monitorability.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [prompt injection](../concepts/prompt-injection.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
