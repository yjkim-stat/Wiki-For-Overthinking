# on-policy distillation (OPD)

<!-- auto:begin -->

Training a student on its own sampled reasoning trajectories while minimizing reverse KL against a teacher's next-token distribution, as opposed to off-policy distillation, which trains on trajectories the teacher generated. Both archived sources treat OPD as redistributing where the student's existing probability mass sits rather than as widening what it can solve. The test-time-scaling analysis says this directly: across three student-teacher settings on AMC2023 and AIME2024/2025/2026, OPD beats the pre-OPD base model at pass@K for small K and at avg@K for all K, yet the base model catches up and overtakes it by K=1024 in most cells, more problems are forgotten (solvable at pass@1024 before, not after) than learned, and a perplexity comparison shows OPD trajectories stay inside the base model's distribution while shifting toward paths the teacher favours -- so it improves sampling efficiency, not the capability boundary. Lightning OPD 2.0 works inside that frame, subtracting a cross-fitted estimate of recurring teacher-reference log-probability disagreement from the token-level signal so the OPD teacher need not be the model that produced the SFT demonstrations (Qwen3-4B-SFT math average 48.3 to 51.7, code 32.6 to 35.7, single runs with no variance reported).

- **Kind**: method
- **Also called**: OPD
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [pass@K](../concepts/pass-k.md)

## Appears in

- [Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation for Large Reasoning Models](../../archive/papers/2026/arxiv-2607-28449/summary.md) — Lightning OPD 2.0 subtracts a cross-fitted estimate of recurring teacher-reference log-probability disagreement from the token-level on-policy-distillation signal, so an OPD teacher can differ from the model that generated the SFT demonstrations.
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Using pass@K/avg@K analysis, the paper shows on-policy distillation improves a student model's sampling efficiency at small K but does not expand its reasoning capability boundary at large K, and even causes it to forget some previously solvable problems.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
