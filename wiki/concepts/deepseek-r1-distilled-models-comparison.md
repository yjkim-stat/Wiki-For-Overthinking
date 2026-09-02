# DeepSeek-R1-distilled models (comparison)

<!-- auto:begin -->

This refers to comparisons made against the family of DeepSeek-R1-distilled models as baselines: ARISE (Risk-Adaptive Search combining MCTS with a Bayesian Risk-Value function) and Concise Math Reasoning via Difficulty-Aware Distillation (DAD, which distills a difficulty-adaptive minimal-step trace and outperforms models trained on the same teacher's own verbose 800K-example CoT distillation) both compare their methods against DeepSeek-R1-distilled model variants.

- **Kind**: concept
- **Also called**: DeepSeek-R1-Distilled models (comparison)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [2WikiMultihopQA](../datasets/2wikimultihopqa.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [College Math](../datasets/college-math.md), [DeepSeek-R1 (teacher)](../models/deepseek-r1-teacher.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU STEM](../datasets/mmlu-stem.md), [Monte Carlo Tree Search (MCTS)](../methods/monte-carlo-tree-search-mcts.md), [MuSiQue](../datasets/musique.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md)

## Appears in

- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.
- [Concise Math Reasoning via Difficulty-Aware Distillation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2155/summary.md) — Difficulty-Aware Distillation (DAD) has a teacher assess each problem's difficulty (easy/medium/hard) then rewrite its own long CoT solution into a difficulty-adaptive, minimal-essential-steps trace via a two-step generate-then-refine pipeline, producing LiteCoT (100K samples averaging just 720 tokens, an order of magnitude shorter than S1/LIMO/OpenThoughts); models distilled on LiteCoT (Liter, 1.5B-32B) consistently outperform models trained on the same teacher's own 800K verbose CoTs, reach 74.2% Pass@1 on AIME24 using only ~5K inference tokens (beating methods that consume far more), and beat static one-size-fits-all CoT-compression baselines (Chain-of-Draft, LLMLingua-2, BudgetAware) on both accuracy and inference time across eight benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
