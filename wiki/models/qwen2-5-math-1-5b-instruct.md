# Qwen2.5-Math-1.5B-Instruct

<!-- auto:begin -->

Qwen2.5-Math-1.5B-Instruct is a math-specialized model used in this archive to test cross-lingual generalizability of test-time scaling methods (Outcome/Process Reward Modeling, Budget Forcing) under FLOPs-matched budgets, and by MUTO's token-level marginal utility training, where even this already-concise math-specialized backbone still gains +2.0 accuracy points while cutting tokens 12.9% -- a smaller efficiency gain than on long-CoT DeepSeek-R1-Distill backbones.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Best-of-N (baseline)](../methods/best-of-n-baseline.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GRPO](../methods/grpo.md), [LiveCodeBench](../datasets/livecodebench.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [o3-mini](o3-mini.md), [Qwen2.5-Math-7B-Instruct](qwen2-5-math-7b-instruct.md), [QwQ-32B](qwq-32b.md)

## Appears in

- [Linguistic Generalizability of Test-Time Scaling in Mathematical Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-699/summary.md) — Under a FLOPs-matched budget across three test-time scaling methods (Outcome Reward Modeling, Process Reward Modeling, Budget Forcing) on a new 55-language competition-math benchmark (MCLM), all three methods yield large gains in English (e.g. Budget Forcing +20 points on AIME) but only ~1.9-2 points average gain across other languages, and reward-model-guided scaling (ORM) matches or beats reasoning-trace-length scaling (Budget Forcing) once FLOPs are equalized -- with more test-time compute also increasing cross-lingual performance variance rather than reducing it.
- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Introduces token-level marginal utility -- the per-token log-probability gain toward the ground-truth answer -- and MUTO, a training framework that penalizes trajectories and individual tokens that reduce this probability, cutting DeepSeek-R1-Distill-Qwen token usage by 87.1% (1.5B) / 80.2% (7B) with comparable or better accuracy.
- [Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-739/summary.md) — Guided by Gut (GG) replaces external Process Reward Models in tree-search test-time scaling with the LLM's own intrinsic token-probability confidence, calibrated via a GRPO reward that heavily penalizes overconfident wrong answers (penalty in [-9,1] vs. reward in [1,2] for correct ones), letting a 1.5B-7B model match or exceed models 10-70x larger while using 4-10x less GPU memory and 8x faster inference than PRM-guided search.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
