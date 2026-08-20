# GKD

<!-- auto:begin -->

Distilling on the student's own samples rather than on a teacher corpus, which removes the train-inference mismatch of classical sequence-level distillation and composes naturally with reinforcement learning. Both sources position their work relative to it and both qualify it. One notes that GKD-style methods typically use an external larger teacher, creating a capacity gap and extra training cost, and replaces that with the same weights under a privileged context -- keeping the on-policy structure while removing the second model at inference, though still paying an extra teacher-scoring forward pass during training. The other tests what the paradigm delivers, measuring across sampling budgets from 1 to 1024 and finding that on-policy distillation raises average correctness at every budget while its pass@K advantage reverses at large budgets, whereas off-policy distillation raises both everywhere. The archive's reading is that removing the distribution mismatch is not free: training on self-generated trajectories is what makes the supervision relevant and also what confines the result to the student's existing support.

- **Kind**: method
- **Also called**: generalized knowledge distillation
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [credit assignment](../concepts/credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [EOPD](eopd.md), [exponential tilting](exponential-tilting.md), [few-shot prompting](few-shot-prompting.md), [forward KL divergence](forward-kl-divergence.md), [GRPO](grpo.md), [JustRL-DeepSeek-1.5B](../models/justrl-deepseek-1-5b.md), [knowledge distillation](knowledge-distillation.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [on-policy distillation](on-policy-distillation.md), [on-policy self-distillation](on-policy-self-distillation.md), [pass@k](../concepts/pass-k.md), [perplexity](perplexity.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [reverse KL divergence](reverse-kl-divergence.md), [sampling efficiency](../concepts/sampling-efficiency.md), [self-distillation](self-distillation.md), [Skywork-OR1-Math-7B](../models/skywork-or1-math-7b.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-09826/summary.md) — Gives the teacher branch of an on-policy self-distillation setup an abstract skill card -- a principle, when it applies, and the mistakes to avoid -- instead of the reference solution, so the privileged signal carries no answer and the gain lands on exactly the rollout groups where group-relative reward is algebraically silent.
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
