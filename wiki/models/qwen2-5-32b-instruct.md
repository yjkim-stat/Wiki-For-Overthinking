# Qwen2.5-32B-Instruct

<!-- auto:begin -->

A 32B instruction-tuned Qwen, and across 4 sources the base for one of the archive's foundational test-time-scaling results: supervised fine-tuning on 1,000 curated traces plus budget forcing produces a model that extrapolates beyond its own unmanaged performance, 50 to 57 percent on one competition set, and exceeds a frontier reasoning preview on competition mathematics by up to 27 percent. It also appears as the largest arm in a multilingual tool-use scaling comparison, where the supervised-versus-reinforcement ordering is not monotone in size, and as a subject in credit-redistribution and epistemic-verbalisation work.

- **Kind**: model
- **Also called**: Qwen2.5-32B-Instruct
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [aha moment](../concepts/aha-moment.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [budget forcing](../methods/budget-forcing.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [credit assignment](../concepts/credit-assignment.md), [cross-lingual transfer](../concepts/cross-lingual-transfer.md), [DAPO-Qwen-32B](dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [entropy collapse](../concepts/entropy-collapse.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [exploration](../concepts/exploration.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [pass@k](../concepts/pass-k.md), [PPO](../methods/ppo.md), [process reward](../concepts/process-reward.md), [Qwen2.5-14B-Instruct](qwen2-5-14b-instruct.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-1.7B-Base](qwen3-1-7b-base.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-8B](qwen3-8b.md), [randomized control](../concepts/randomized-control.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reasoning collapse](../concepts/reasoning-collapse.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [tool learning](../concepts/tool-learning.md), [trajectory diversity](../concepts/trajectory-diversity.md)

## Appears in

- [s1: Simple test-time scaling](../../archive/papers/2025/arxiv-2501-19393/summary.md) — Reaches test-time scaling with two simple ingredients: supervised finetuning on 1,000 curated reasoning traces, and 'budget forcing', which controls thinking length by cutting generation off or appending 'Wait' to extend it.
- [When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO](../../archive/papers/2026/arxiv-2608-03467/summary.md) — Shows that GRPO's per-completion uniformity is frequency-skewed once credit is aggregated by solution structure — a recurring correct form accumulates positive coefficient mass proportional to how often it is sampled — and rebalances it by a rarity exponent over a partition built from deterministic cue signatures rather than a judge model.
- [When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use](../../archive/papers/2026/arxiv-2608-11715/summary.md) — Names and measures a multilingual tool-calling failure in which the model picks the right API but writes argument values in the wrong language, then compares supervised fine-tuning against PPO and GRPO under matched budgets and finds that a well-selected supervised checkpoint matches or beats reinforcement learning on the task while costing more elsewhere.
- [Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty](../../archive/papers/2026/local-99019f66bdc27581/summary.md) — Separates reasoning into procedural advancement and 'epistemic verbalization' — the token-level externalization of uncertainty — and shows that emitting doubt is what lets a model recover from silent divergence, that injecting a bare doubt cue recovers failed trajectories, and that 800 SFT examples suffice to install or destroy the habit.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
