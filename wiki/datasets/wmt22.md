# WMT22

<!-- auto:begin -->

The 2022 edition of the machine-translation metrics shared task, whose test set carries human MQM annotations and serves in both sources as the gold standard for judging a translation-quality metric. One uses it to benchmark twenty-plus models as judges, scoring by system-level and tie-calibrated segment-level pairwise accuracy and deliberately avoiding correlation metrics for their sensitivity to small samples and outliers. The other uses it as one evaluation set among several, and separately as the source of the discourse-level comparison showing explicit reasoning helps at document level where it does not at sentence level. It is the archive's example of an evaluation whose value comes from the human labels underneath rather than from the task itself.

- **Kind**: dataset
- **Also called**: WMT22 metrics task
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [Aya-expanse-8B](../models/aya-expanse-8b.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-V3](../models/deepseek-v3.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [GPT-4](../models/gpt-4.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5](../models/gpt-5.md), [GRPO](../methods/grpo.md), [jury aggregation](../methods/jury-aggregation.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3-70B-Instruct](../models/llama-3-70b-instruct.md), [Llama-3-8B-Instruct](../models/llama-3-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [o4-mini](../models/o4-mini.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning drift](../concepts/reasoning-drift.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher forcing](../methods/teacher-forcing.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
