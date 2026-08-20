# exponential tilting

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [difficulty stratification](difficulty-stratification.md), [Dr. GRPO](dr-grpo.md), [few-shot prompting](few-shot-prompting.md), [forward KL divergence](forward-kl-divergence.md), [GPQA](../datasets/gpqa.md), [group-relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [MaxRL](maxrl.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [on-policy distillation](on-policy-distillation.md), [on-policy self-distillation](on-policy-self-distillation.md), [PPO](ppo.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [REINFORCE](reinforce.md), [self-distillation](../concepts/self-distillation.md), [supervised fine-tuning](supervised-fine-tuning.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation](../../archive/papers/2026/arxiv-2608-09271/summary.md) — Replaces GRPO's z-score group normalisation with a temperature-scaled softmax over rewards, which keeps the induced prompt-difficulty weighting bounded as pass probability approaches one and turns the temperature into a dial between REINFORCE and maximum-likelihood weighting.
- [Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-09826/summary.md) — Gives the teacher branch of an on-policy self-distillation setup an abstract skill card -- a principle, when it applies, and the mistakes to avoid -- instead of the reference solution, so the privileged signal carries no answer and the gain lands on exactly the rollout groups where group-relative reward is algebraically silent.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
