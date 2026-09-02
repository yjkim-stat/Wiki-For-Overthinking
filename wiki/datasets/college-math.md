# College Math

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Also called**: CollegeMath
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [DeepSeek-R1-distilled models (comparison)](../concepts/deepseek-r1-distilled-models-comparison.md), [DeepSeek-R1 (teacher)](../models/deepseek-r1-teacher.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH](math.md), [MATH500](math500.md), [Minerva](minerva.md), [MMLU STEM](mmlu-stem.md), [OlympiadBench](olympiadbench.md)

## Appears in

- [Concise Math Reasoning via Difficulty-Aware Distillation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2155/summary.md) — Difficulty-Aware Distillation (DAD) has a teacher assess each problem's difficulty (easy/medium/hard) then rewrite its own long CoT solution into a difficulty-adaptive, minimal-essential-steps trace via a two-step generate-then-refine pipeline, producing LiteCoT (100K samples averaging just 720 tokens, an order of magnitude shorter than S1/LIMO/OpenThoughts); models distilled on LiteCoT (Liter, 1.5B-32B) consistently outperform models trained on the same teacher's own 800K verbose CoTs, reach 74.2% Pass@1 on AIME24 using only ~5K inference tokens (beating methods that consume far more), and beat static one-size-fits-all CoT-compression baselines (Chain-of-Draft, LLMLingua-2, BudgetAware) on both accuracy and inference time across eight benchmarks.
- [Efficient Reasoning for LLMs through Speculative Chain-of-Thought](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-76/summary.md) — Speculative Chain-of-Thought (SCoT) speeds up reasoning-model latency by having a fine-tuned small draft model generate multiple parallel CoT drafts thought-level (not token-level) which a fine-tuned target model selects from or corrects, reducing reasoning latency 48-66% (32B target) and 21-49% (70B target) while staying near target-model accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
