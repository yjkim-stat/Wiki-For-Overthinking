# DeepSeek-V3

<!-- auto:begin -->

A large open mixture-of-experts model, used by both sources as the capable outside system a study leans on rather than as its subject. One uses it twice over — as the automatic MQM annotator that produces the error analysis carrying its central finding, and as the assigner of translation difficulty levels that carries its other one — so two of that paper's structural claims rest on this model's judgement. The other includes it among the models whose chain-of-thought monitorability is scored. Worth noting for the same reason as any judge in this archive: a model doing the measuring is part of the experimental apparatus and is rarely audited as such.

- **Kind**: model
- **Also called**: DeepSeek V3
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [BBH](../datasets/bbh.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](deepseek-r1.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [GRPO](../methods/grpo.md), [inverse scaling](../concepts/inverse-scaling.md), [KL regularization](../methods/kl-regularization.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [MMLU](../datasets/mmlu.md), [monitorability](../concepts/monitorability.md), [outcome reward](../concepts/outcome-reward.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [process reward](../concepts/process-reward.md), [Qwen2.5-72B](qwen2-5-72b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [QwQ-32B](qwq-32b.md), [reasoning drift](../concepts/reasoning-drift.md), [reward shaping](../methods/reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [teacher forcing](../methods/teacher-forcing.md), [verbosity](../concepts/verbosity.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.
- [Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity](../../archive/papers/2025/local-2f98d1e607e7b1dd/summary.md) — Argues that faithfulness alone is insufficient for CoT monitoring and adds verbosity — whether the trace lists every factor needed to solve the task — combining the two into a monitorability score, then shows models can look faithful while omitting key factors.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
