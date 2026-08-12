# Qwen2.5

<!-- auto:begin -->

The Qwen2.5 model family, referred to at family level rather than by checkpoint in these two sources, both of which use it to establish that a result is not an artefact of one model. One sweeps compression settings across two model families and reports Qwen2.5 as the cross-model check on conclusions drawn primarily from a LLaMA student; the other spans it alongside other families when validating that a test-time aggregation algorithm's provable scaling behaviour appears in practice. Neither describes the family itself. Note that this archive holds several individual Qwen2.5 checkpoints as separate entities, and their entries carry the substantive findings; this one exists because some sources cite the family without naming a size.

- **Kind**: model
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [generative rewriting](../methods/generative-rewriting.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [majority voting](../methods/majority-voting.md), [MATH-500](../datasets/math-500.md), [MATH500](../datasets/math500.md), [MMLU-PRO](../datasets/mmlu-pro.md), [overthinking](../concepts/overthinking.md), [pass-k](../methods/pass-k.md), [QwQ-32B](qwq-32b.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](../methods/self-consistency.md), [supervised finetuning](../methods/supervised-finetuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [verification](../concepts/verification.md)

## Appears in

- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.
- [Provable Scaling Laws for the Test-Time Compute of Large Language Models](../../archive/papers/2025/local-e5ae26db2daac1d7/summary.md) — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
