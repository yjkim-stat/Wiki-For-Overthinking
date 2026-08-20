# on-policy distillation

<!-- auto:begin -->

Supervising a student on prefixes drawn from its own rollouts using a teacher's distribution over the next token, so the student is trained on the states it will actually visit rather than on a teacher's trajectory. Both sources here attack the same weakness from different sides: the objective is token agreement, and agreement is not the quantity anyone wants. One shows it can be satisfied by degeneration -- a student reaching near-perfect agreement by looping while the response is globally broken -- and decomposes the mismatch instead into student-excess tokens, whose log-ratio corrections grow unbounded and destabilise the update, and student-deficit tokens, which the student almost never samples so no on-policy update reaches them, with 95.5 percent of deficit positions having under a one percent chance of appearing in sampled supervision. The other keeps the objective and changes what the teacher is: conditioning it on the student's completed trajectory and verified outcome, preserving behaviour on successes and redirecting failures toward verified success, while leaving the student's prefixes and its prefix-only interface untouched. That paper also supplies the setting's formal boundary -- forward-KL distillation provably targets the teacher's conditional mean given the prefix, so trajectory-specific variation stays privileged and cannot be transferred to a student that must act from its current prefix.

- **Kind**: method
- **Also called**: OPSD, on-policy self-distillation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Brumo](../datasets/brumo.md), [CMIMC](../datasets/cmimc.md), [coverage](../concepts/coverage.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [degenerate generation](../concepts/degenerate-generation.md), [distribution mismatch](../concepts/distribution-mismatch.md), [factorial ablation](factorial-ablation.md), [format compliance](../concepts/format-compliance.md), [GRPO](grpo.md), [HMMT](../datasets/hmmt.md), [HMMT 2025](../datasets/hmmt-2025.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [MATH](../datasets/math.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy self-distillation](on-policy-self-distillation.md), [paired bootstrap](paired-bootstrap.md), [pass@k](../concepts/pass-k.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token selection](../concepts/token-selection.md)

## Appears in

- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) — Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
