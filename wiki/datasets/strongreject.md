# StrongREJECT

<!-- auto:begin -->

A jailbreak benchmark whose scoring is designed to reject responses that comply in form without supplying actionable content, which makes it stricter than a benchmark scoring refusal alone. Both sources use it among several safety sets. In the dual-adversarial defence work it shows the widest spread across models of the four benchmarks used -- attack-success reductions from 7.03 to 61.98 points -- which reflects that the base models start at very different points on it (7.03 percent for one, 84.03 for another), so an absolute reduction on this benchmark is uninterpretable without the base rate. The attack source uses it to demonstrate automated hijacking of safety reasoning. Neither describes its construction.

- **Kind**: dataset
- **Also called**: StrongReject
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3.2](../models/deepseek-v3-2.md), [GCG](../methods/gcg.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [GPQA-Diamond](gpqa-diamond.md), [GPT o3](../models/gpt-o3.md), [GSM8K](gsm8k.md), [HarmBench](harmbench.md), [jailbreak](../concepts/jailbreak.md), [knowledge distillation](../methods/knowledge-distillation.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH500](math500.md), [MMLU-Pro](mmlu-pro.md), [monitorability](../concepts/monitorability.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [PAIR](../methods/pair.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [safety alignment](../concepts/safety-alignment.md), [self-distillation](../methods/self-distillation.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](../../archive/papers/2026/arxiv-2608-09542/summary.md) — Builds safety-alignment training data by first having an agent jailbreak a strong teacher and only then asking that teacher to explain why the successful attack worked, so the student is supervised on the mechanism of the attack rather than on the refusal.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — Automates the hijacking of a reasoning model's own safety reasoning by using a weaker, less-aligned model to simulate execution reasoning and refining attacks from patterns leaked in refusals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
