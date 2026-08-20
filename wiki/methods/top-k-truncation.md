# top-k truncation

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: top-K truncation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Brumo](../datasets/brumo.md), [CMIMC](../datasets/cmimc.md), [consensus](../concepts/consensus.md), [coverage](../concepts/coverage.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [degenerate generation](../concepts/degenerate-generation.md), [distribution mismatch](../concepts/distribution-mismatch.md), [format compliance](../concepts/format-compliance.md), [forward KL divergence](forward-kl-divergence.md), [GRPO](grpo.md), [HMMT](../datasets/hmmt.md), [HMMT 2025](../datasets/hmmt-2025.md), [Jensen-Shannon divergence](jensen-shannon-divergence.md), [knowledge distillation](knowledge-distillation.md), [majority voting](majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy distillation](on-policy-distillation.md), [pass@k](../concepts/pass-k.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [token selection](../concepts/token-selection.md)

## Appears in

- [On-Policy Self-Distillation without Any Supervision](../../archive/papers/2026/arxiv-2608-06296/summary.md) — Removes external supervision from on-policy self-distillation by building a pseudo-solution from the model's own majority vote and using it as privileged teacher context rather than as a scalar reward, then distilling only on the completions that disagree with it.
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](../../archive/papers/2026/arxiv-2608-09836/summary.md) — Identifies degenerate agreement -- students reaching near-perfect token agreement with a teacher by looping while the response as a whole is broken -- and replaces the agreement objective with two directional mismatch corrections, one bounding runaway excess tokens and one injecting teacher-preferred mass at positions the student almost never samples.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
