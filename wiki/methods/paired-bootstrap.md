# paired bootstrap

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [best-of-n](best-of-n.md), [budget forcing](budget-forcing.md), [chain-of-thought distillation](chain-of-thought-distillation.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Cohen's kappa](cohen-s-kappa.md), [credit assignment](../concepts/credit-assignment.md), [decontamination](decontamination.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [diminishing returns](../concepts/diminishing-returns.md), [factorial ablation](factorial-ablation.md), [few-shot prompting](few-shot-prompting.md), [generation-verification gap](../concepts/generation-verification-gap.md), [GPT-5.4](../models/gpt-5-4.md), [GRPO](grpo.md), [KL regularization](kl-regularization.md), [knowledge distillation](knowledge-distillation.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH500](../datasets/math500.md), [McNemar test](mcnemar-test.md), [on-policy distillation](on-policy-distillation.md), [on-policy self-distillation](on-policy-self-distillation.md), [out-of-domain generalization](../concepts/out-of-domain-generalization.md), [pass@k](../concepts/pass-k.md), [pool oracle](../concepts/pool-oracle.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [reasoning depth](../concepts/reasoning-depth.md), [reproducibility](../concepts/reproducibility.md), [selection signal](../concepts/selection-signal.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher-student gap](../concepts/teacher-student-gap.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) — Treats test-time scaling as routing rather than budgeting -- cheap evidence decides whether a decision is already settled, and expensive verification is spent only on candidates that can still change the answer -- and evaluates every baseline by replaying it over the same stored candidate pool so that only the allocation decision differs.
- [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](../../archive/papers/2026/arxiv-2608-08503/summary.md) — Compares chain-of-thought against answer-only supervision under a protocol where the two conditions differ in nothing but the training target, and finds the rationales buy nothing in-domain for strong backbones while buying 20 to 28 points out of domain -- with a human study attributing the measurable effect to language adherence and inspectability rather than to better reasoning.
- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
