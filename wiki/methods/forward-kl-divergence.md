# forward KL divergence

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [consensus](../concepts/consensus.md), [credit assignment](../concepts/credit-assignment.md), [degenerate generation](../concepts/degenerate-generation.md), [factorial ablation](factorial-ablation.md), [format compliance](../concepts/format-compliance.md), [GRPO](grpo.md), [hindsight](../concepts/hindsight.md), [HMMT 2025](../datasets/hmmt-2025.md), [Jensen-Shannon divergence](jensen-shannon-divergence.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [on-policy distillation](on-policy-distillation.md), [on-policy self-distillation](on-policy-self-distillation.md), [paired bootstrap](paired-bootstrap.md), [pass@k](../concepts/pass-k.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [top-k truncation](top-k-truncation.md)

## Appears in

- [On-Policy Self-Distillation without Any Supervision](../../archive/papers/2026/arxiv-2608-06296/summary.md) — Removes external supervision from on-policy self-distillation by building a pseudo-solution from the model's own majority vote and using it as privileged teacher context rather than as a scalar reward, then distilling only on the completions that disagree with it.
- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
