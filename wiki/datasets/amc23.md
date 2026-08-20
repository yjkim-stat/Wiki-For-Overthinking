# AMC23

<!-- auto:begin -->

The 2023 sitting of the American Mathematics Competitions, used as a hard competition-math evaluation benchmark alongside AIME in CoBa's compute-balanced routing, the on-policy-distillation sampling-efficiency study, Funnel of Thoughts' rollout pruning, and ATTS's conformal-prediction test-time scaling.

- **Kind**: dataset
- **Also called**: AMC 2023, AMC2023
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [GPQA-Diamond](gpqa-diamond.md), [MATH](math.md), [MATH-500](math-500.md), [pass@K](../concepts/pass-k.md), [rejection sampling](../methods/rejection-sampling.md), [Slim-SC (baseline)](../methods/slim-sc-baseline.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) — CoBa treats test-time scaling as a compute-allocation problem and routes cheap answer-agreement evidence versus a small number of strong-verifier calls, reaching majority-voting/self-evaluation-level accuracy on math and symbolic reasoning benchmarks while using roughly half the parameter-weighted tokens.
- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Using pass@K/avg@K analysis, the paper shows on-policy distillation improves a student model's sampling efficiency at small K but does not expand its reasoning capability boundary at large K, and even causes it to forget some previously solvable problems.
- [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](../../archive/papers/2026/arxiv-2608-15065/summary.md) — Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.
- [ATTS: Asynchronous Test-Time Scaling via Conformal Prediction](../../archive/papers/2026/title-b601ad920fcc4d45/summary.md) — ATTS uses conformal prediction to asynchronously coordinate multi-dimensional test-time scaling, cutting synchronization overhead between draft and target models during LLM inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
