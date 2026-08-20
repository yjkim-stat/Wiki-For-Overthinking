# reverse KL divergence

<!-- auto:begin -->

Distilling by minimising the divergence from the student to the teacher, which is mode-seeking: the student is penalised for placing mass where the teacher does not, and is free to ignore parts of the teacher's support. It is the standard objective in on-policy self-distillation, and both sources here document its cost. The unsupervised source measures a failure mode rather than a deficit: under pseudo-labels, reverse KL does not converge at all, collapsing by progressive loss of termination -- generations growing from 2.7 thousand characters at step 25 to the token ceiling from step 125, with parsable answers falling from 99 to 33 percent -- while forward KL averages 57.10. The test-time-scaling source supplies the structural reading: reverse-KL on-policy distillation raises average correctness at every sampling budget while its large-budget pass rate falls below the untrained base, and a perplexity analysis shows probability mass moving toward paths the base already supported. Mode-seeking is exactly what that describes. Variants that route forward-KL guidance to high-entropy positions while keeping reverse KL elsewhere reproduce the same pattern, so the effect belongs to on-policy training on self-generated trajectories rather than to the divergence alone.

- **Kind**: method
- **Also called**: reverse KL
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [consensus](../concepts/consensus.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [degenerate generation](../concepts/degenerate-generation.md), [EOPD](eopd.md), [format compliance](../concepts/format-compliance.md), [forward KL divergence](forward-kl-divergence.md), [GKD](gkd.md), [GRPO](grpo.md), [HMMT 2025](../datasets/hmmt-2025.md), [Jensen-Shannon divergence](jensen-shannon-divergence.md), [JustRL-DeepSeek-1.5B](../models/justrl-deepseek-1-5b.md), [knowledge distillation](knowledge-distillation.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [on-policy distillation](on-policy-distillation.md), [pass@k](../concepts/pass-k.md), [perplexity](perplexity.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [sampling efficiency](../concepts/sampling-efficiency.md), [self-consistency](self-consistency.md), [Skywork-OR1-Math-7B](../models/skywork-or1-math-7b.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [test-time scaling](../concepts/test-time-scaling.md), [top-k truncation](top-k-truncation.md)

## Appears in

- [On-Policy Self-Distillation without Any Supervision](../../archive/papers/2026/arxiv-2608-06296/summary.md) — Removes external supervision from on-policy self-distillation by building a pseudo-solution from the model's own majority vote and using it as privileged teacher context rather than as a scalar reward, then distilling only on the completions that disagree with it.
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
