# Gemini-2.0-flash

<!-- auto:begin -->

A fast proprietary model, present in both sources as a mid-tier comparison point. One finds it performing well at segment level on translation quality evaluation — even surpassing a stronger model on one language pair — while lagging at system level, which is the paper's clearest illustration that the two levels of that task rank models differently. The other includes it among the large language models a reasoning-augmented translation method is measured against. Neither studies it.

- **Kind**: model
- **Also called**: Gemini 2.0 Flash, Gemini-2.0-Flash
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [Aya-expanse-8B](aya-expanse-8b.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-V3](deepseek-v3.md), [DeepSeek-V3.2](deepseek-v3-2.md), [factorial ablation](../methods/factorial-ablation.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [GPT-4](gpt-4.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [GRPO](../methods/grpo.md), [jury aggregation](../methods/jury-aggregation.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.3-70B](llama-3-3-70b.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [Llama-3-8B-Instruct](llama-3-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [LoRA](../methods/lora.md), [multi-agent pipeline](../methods/multi-agent-pipeline.md), [o4-mini](o4-mini.md), [outcome reward](../concepts/outcome-reward.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [process reward](../concepts/process-reward.md), [prompt injection](../concepts/prompt-injection.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-coder-7B](qwen2-5-coder-7b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-VL-235B](qwen3-vl-235b.md), [ReAct](../methods/react.md), [reasoning drift](../concepts/reasoning-drift.md), [reward shaping](../concepts/reward-shaping.md), [self-verification](../concepts/self-verification.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher forcing](../methods/teacher-forcing.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.
- [Persistent Semantic Entities in Tool-Augmented LLM Systems](../../archive/papers/2026/arxiv-2608-07952/summary.md) — Formalises implicit agent state that survives session boundaries as Persistent Semantic Entities defined by name binding, event triggering and propagation, and measures across 24 models that whether injected contamination decays depends on what kind of contamination it is rather than on model scale or deployment.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
