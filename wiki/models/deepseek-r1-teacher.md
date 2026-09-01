# DeepSeek-R1 (teacher)

<!-- auto:begin -->

DeepSeek-R1 is used across these sources as a teacher model whose long chain-of-thought reasoning traces are distilled, rewritten, or otherwise processed to train smaller student models -- e.g. rewritten into difficulty-adaptive minimal-step traces (LiteCoT) for distillation into 1.5B-32B students, or as the source of the raw 800K-example verbose CoT distillation baseline that difficulty-aware alternatives are compared against. It also appears as one of two teacher models (alongside QwQ-32B) whose reasoning traces are grounded in knowledge-graph paths before fine-tuning smaller models.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-distilled models (comparison)](../concepts/deepseek-r1-distilled-models-comparison.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GrailQA](../datasets/grailqa.md), [GSM8K](../datasets/gsm8k.md), [KAOYAN](../datasets/kaoyan.md), [Llama-3.1-8B](llama-3-1-8b.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU STEM](../datasets/mmlu-stem.md), [OlympiadBench](../datasets/olympiadbench.md), [QwQ-32B](qwq-32b.md), [QwQ-32B (teacher)](qwq-32b-teacher.md), [SimpleQA](../datasets/simpleqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [WebQSP](../datasets/webqsp.md)

## Appears in

- [Concise Math Reasoning via Difficulty-Aware Distillation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2155/summary.md) — Difficulty-Aware Distillation (DAD) has a teacher assess each problem's difficulty (easy/medium/hard) then rewrite its own long CoT solution into a difficulty-adaptive, minimal-essential-steps trace via a two-step generate-then-refine pipeline, producing LiteCoT (100K samples averaging just 720 tokens, an order of magnitude shorter than S1/LIMO/OpenThoughts); models distilled on LiteCoT (Liter, 1.5B-32B) consistently outperform models trained on the same teacher's own 800K verbose CoTs, reach 74.2% Pass@1 on AIME24 using only ~5K inference tokens (beating methods that consume far more), and beat static one-size-fits-all CoT-compression baselines (Chain-of-Draft, LLMLingua-2, BudgetAware) on both accuracy and inference time across eight benchmarks.
- [Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-474/summary.md) — P-TTS treats the prompt itself as a scalable data-augmentation axis: from just 90 seed AIME problems, four principled instructional wrappers (Reward/Penalty/Correctness/Step-by-Step framing, with six paraphrased Reward variants) elicit diverse teacher reasoning trajectories that are distilled via SFT into Qwen2.5 students, matching or beating 1K-shot baselines (S1/S1.1) and even DeepSeek-R1-Distill-Qwen-32B (trained on >800K examples) on GPQA-Diamond with only 900 augmented training examples, transferring to out-of-domain/multilingual/legal-reasoning benchmarks, and reward-framing prompts specifically driving the largest gains and the highest lexical/semantic diversity in elicited teacher rationales.
- [Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-561/summary.md) — fs1 fine-tunes LLMs on reasoning traces grounded in knowledge-graph paths (rather than raw distilled reasoning traces), improving factual accuracy on complex multi-hop QA by 6-14 pass@16 points while also producing shorter reasoning traces than the ungrounded baseline.
- [When Internalization Fails: Finding Better Targets for Reasoning Compression](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-734/summary.md) — In a teacher-student distillation setup on competition-level math (NuminaMath 1.5, ~5000-token traces), ICoT-style curriculum internalization methods that work on simple/structured tasks (GSM8K, multiplication) provide little to no benefit over direct distillation; naive first-k-token truncation at inference time is also shown misleading, since models compensate by generating longer post-think text, undermining apparent token savings; distilling on the teacher's naturally-occurring post-think section (concise, answer-directed text generated after </think> but before the boxed answer) achieves the best accuracy-efficiency trade-off among all tested shortened targets, including generic teacher-generated summaries at matched token budgets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
