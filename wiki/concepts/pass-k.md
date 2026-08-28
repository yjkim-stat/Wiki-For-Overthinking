# pass@K

<!-- auto:begin -->

The fraction of problems a model solves correctly in at least one of K independent samples, used to measure a model's capability ceiling under parallel test-time compute, as distinct from Pass@1's single-sample accuracy. The on-policy-distillation study uses pass@K/avg@K analysis to show distillation improves sampling efficiency at small K but not the capability boundary at large K; 'The Danger of Overthinking' uses it to evaluate agentic SWE-bench solutions.

- **Kind**: concept
- **Also called**: Pass@K, Pass@k
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [Best-of-N sampling](../methods/best-of-n-sampling.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [majority voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [on-policy distillation (OPD)](../methods/on-policy-distillation-opd.md), [Overthinking](overthinking.md), [Pass@1](pass-1.md), [reasoning effort](reasoning-effort.md), [SWE-bench Verified](../datasets/swe-bench-verified.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Using pass@K/avg@K analysis, the paper shows on-policy distillation improves a student model's sampling efficiency at small K but does not expand its reasoning capability boundary at large K, and even causes it to forget some previously solvable problems.
- [FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1766/summary.md) — TTC-aware training projects a model's expected validation accuracy under test-time compute (via an exponential-saturation curve fit to intermediate checkpoints) to identify an early-stopping point where an intermediate checkpoint plus TTC inference matches or exceeds a fully-trained checkpoint's accuracy at a fraction of training FLOPs -- up to 92% training-FLOP savings while preserving or improving accuracy, validated across TinyLlama, Pythia, FineMath, and a fine-tuned Qwen3-30B-A3B-Instruct.
- [The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks](../../archive/papers/2025/local-9f60265e5ada34cb/summary.md) — Defines and measures 'overthinking' in Large Reasoning Models on real software-engineering agent tasks, showing that favoring internal reasoning over environment interaction correlates with lower SWE-bench issue-resolution rates and can be mitigated at lower cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
