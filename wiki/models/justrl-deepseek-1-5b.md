# JustRL-DeepSeek-1.5B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [Brumo](../datasets/brumo.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [CMIMC](../datasets/cmimc.md), [coverage](../concepts/coverage.md), [credit assignment](../concepts/credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [degenerate generation](../concepts/degenerate-generation.md), [distribution mismatch](../concepts/distribution-mismatch.md), [EOPD](../methods/eopd.md), [format compliance](../concepts/format-compliance.md), [forward KL divergence](../methods/forward-kl-divergence.md), [GKD](../methods/gkd.md), [GRPO](../methods/grpo.md), [HMMT](../datasets/hmmt.md), [knowledge distillation](../methods/knowledge-distillation.md), [MATH](../datasets/math.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy distillation](../methods/on-policy-distillation.md), [pass@k](../concepts/pass-k.md), [perplexity](../concepts/perplexity.md), [Qwen3-1.7B-Base](qwen3-1-7b-base.md), [Qwen3-8B](qwen3-8b.md), [reverse KL divergence](../methods/reverse-kl-divergence.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [sampling efficiency](../concepts/sampling-efficiency.md), [Skywork-OR1-Math-7B](skywork-or1-math-7b.md), [teacher-student gap](../concepts/teacher-student-gap.md), [test-time scaling](../concepts/test-time-scaling.md), [token selection](../concepts/token-selection.md), [top-k truncation](../methods/top-k-truncation.md)

## Appears in

- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) — Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
