# Gemini-2.5-Flash

<!-- auto:begin -->

A frontier reasoning model from Google, appearing in the archive only as a subject of evaluation. One source uses it as an attack target and reports approaching 100% jailbreak success within one or a few turns against its safety reasoning, by refining attempts from patterns leaked in its own refusals. The other includes it in a large-scale evaluation of LLM judges, where the finding is that judge reliability and validity come apart. Neither studies the model itself, so what the archive holds about it is how it behaves under attack and as an evaluator.

- **Kind**: model
- **Also called**: Gemini 2.5 Flash
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [construct validity](../concepts/construct-validity.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [generative rewriting](../methods/generative-rewriting.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [HarmBench](../datasets/harmbench.md), [jailbreak](../concepts/jailbreak.md), [Kimi-K2.5](kimi-k2-5.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH500](../datasets/math500.md), [meta-evaluation](../concepts/meta-evaluation.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [MT-Bench](../datasets/mt-bench.md), [overthinking](../concepts/overthinking.md), [Qwen2.5](qwen2-5.md), [Qwen3-8B](qwen3-8b.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [supervised finetuning](../methods/supervised-finetuning.md)

## Appears in

- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — Automates the hijacking of a reasoning model's own safety reasoning by using a weaker, less-aligned model to simulate execution reasoning and refining attacks from patterns leaked in refusals.
- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
