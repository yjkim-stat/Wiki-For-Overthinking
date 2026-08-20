# on-policy distillation

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Brumo](../datasets/brumo.md), [CMIMC](../datasets/cmimc.md), [coverage](../concepts/coverage.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [degenerate generation](../concepts/degenerate-generation.md), [factorial ablation](factorial-ablation.md), [GRPO](grpo.md), [HMMT](../datasets/hmmt.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [MATH](../datasets/math.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy self-distillation](on-policy-self-distillation.md), [pass@k](../concepts/pass-k.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token selection](../concepts/token-selection.md)

## Appears in

- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) — Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
