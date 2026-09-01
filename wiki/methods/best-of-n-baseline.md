# Best-of-N (baseline)

<!-- auto:begin -->

Best-of-N sampling is used in these sources as a test-time-scaling baseline that alternatives are compared against for cost/accuracy: Guided by Gut shows its calibrated-confidence tree search matches or beats Best-of-N at matched sampling budgets while using roughly half the KV-cache memory; AdaReasoner is a separate RL-trained plugin that instead adapts prompt format, decoding temperature and reasoning-step count per task rather than sampling N full completions.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [chain-of-thought baseline](chain-of-thought-baseline.md), [Chain-of-Thought (CoT, baseline)](chain-of-thought-cot-baseline.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LogiQA](../datasets/logiqa.md), [LoRA fine-tuning](lora-fine-tuning.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OpenAI o1-mini](../models/openai-o1-mini.md), [Qwen2.5-Math-1.5B-Instruct](../models/qwen2-5-math-1-5b-instruct.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-739/summary.md) — Guided by Gut (GG) replaces external Process Reward Models in tree-search test-time scaling with the LLM's own intrinsic token-probability confidence, calibrated via a GRPO reward that heavily penalizes overconfident wrong answers (penalty in [-9,1] vs. reward in [1,2] for correct ones), letting a 1.5B-7B model match or exceed models 10-70x larger while using 4-10x less GPU memory and 8x faster inference than PRM-guided search.
- [MetaScale: Test-Time Scaling with Evolving Meta-Thoughts](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-574/summary.md) — MetaScale is a test-time-scaling framework that has an LLM select and iteratively evolve 'meta-thoughts' (a cognitive mindset plus a problem-solving strategy, initialized from self-composed heuristics and retrieved WildChat conversation patterns) via a multi-armed-bandit UCB selection process guided by a reward model, periodically refined by a genetic algorithm that evolves high-reward meta-thoughts into improved child strategies -- outperforming Best-of-N and CoT+Best-of-N baselines on Arena-Hard/MMLU-Pro/GSM8K, beating o1-mini under style control, and scaling more effectively with increased sampling budget than Best-of-N (which plateaus).
- [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](../../archive/papers/2025/title-b12c09d1a21e70d0/summary.md) — AdaReasoner is an RL-trained, model-agnostic plugin that picks a per-task reasoning configuration - prompt instruction format, decoding temperature and number of reasoning steps - instead of using one fixed prompting setup for every task.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
