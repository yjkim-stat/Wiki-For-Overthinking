# GPT-4o-mini

<!-- auto:begin -->

A small proprietary model, used by both sources as the cheap end of a comparison. One includes it among the judges evaluating whether a poisoned model's reasoning betrays its backdoor, where the finding is that judge capability does not rescue a trace from which the information has been removed. The other reports it as an instance of a general pattern in translation-quality evaluation — efficient model variants are outperformed by their corresponding full models — so the cost saving is paid for in judgement quality.

- **Kind**: model
- **Also called**: GPT-4o-mini
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemma-4-12B](gemma-4-12b.md), [GPT-4](gpt-4.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [monitorability](../concepts/monitorability.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-32B](qwen3-32b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [Qwen3-8B](qwen3-8b.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
