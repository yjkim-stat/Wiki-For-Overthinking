# DeepSeek-R1 (teacher)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-distilled models (comparison)](deepseek-r1-distilled-models-comparison.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GrailQA](../datasets/grailqa.md), [GSM8K](../datasets/gsm8k.md), [KAOYAN](../datasets/kaoyan.md), [Llama-3.1-8B](llama-3-1-8b.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU STEM](../datasets/mmlu-stem.md), [OlympiadBench](../datasets/olympiadbench.md), [QwQ-32B (teacher)](qwq-32b-teacher.md), [SimpleQA](../datasets/simpleqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [WebQSP](../datasets/webqsp.md)

## Appears in

- [Concise Math Reasoning via Difficulty-Aware Distillation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2155/summary.md) — Difficulty-Aware Distillation (DAD) has a teacher assess each problem's difficulty (easy/medium/hard) then rewrite its own long CoT solution into a difficulty-adaptive, minimal-essential-steps trace via a two-step generate-then-refine pipeline, producing LiteCoT (100K samples averaging just 720 tokens, an order of magnitude shorter than S1/LIMO/OpenThoughts); models distilled on LiteCoT (Liter, 1.5B-32B) consistently outperform models trained on the same teacher's own 800K verbose CoTs, reach 74.2% Pass@1 on AIME24 using only ~5K inference tokens (beating methods that consume far more), and beat static one-size-fits-all CoT-compression baselines (Chain-of-Draft, LLMLingua-2, BudgetAware) on both accuracy and inference time across eight benchmarks.
- [Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-474/summary.md) — P-TTS treats the prompt itself as a scalable data-augmentation axis: from just 90 seed AIME problems, four principled instructional wrappers (Reward/Penalty/Correctness/Step-by-Step framing, with six paraphrased Reward variants) elicit diverse teacher reasoning trajectories that are distilled via SFT into Qwen2.5 students, matching or beating 1K-shot baselines (S1/S1.1) and even DeepSeek-R1-Distill-Qwen-32B (trained on >800K examples) on GPQA-Diamond with only 900 augmented training examples, transferring to out-of-domain/multilingual/legal-reasoning benchmarks, and reward-framing prompts specifically driving the largest gains and the highest lexical/semantic diversity in elicited teacher rationales.
- [Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-561/summary.md) — fs1 fine-tunes LLMs on reasoning traces grounded in knowledge-graph paths (rather than raw distilled reasoning traces), improving factual accuracy on complex multi-hop QA by 6-14 pass@16 points while also producing shorter reasoning traces than the ungrounded baseline.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
