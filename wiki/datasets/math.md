# MATH

<!-- auto:begin -->

The MATH competition-mathematics dataset, used in the archive both directly (e.g. 'Between Underthinking and Overthinking' evaluates on MATH and GSM8K to show reasoning models overthink easy questions and underthink hard ones) and via its curated 500-problem subset MATH-500/MATH500 used by most other archived test-time-compute papers. Note: the wiki tracks this dataset family under three separate, unmerged spellings.

- **Kind**: dataset
- **Also called**: MATH-500, MATH500
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [GSM8K](gsm8k.md), [MATH-500](math-500.md), [overthinking](../concepts/overthinking.md), [rejection sampling](../methods/rejection-sampling.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness in LLMs](../../archive/papers/2025/local-6afb006d68240134/summary.md) — An empirical study showing reasoning LLMs overthink easy questions and underthink hard ones, and that preferring shorter outputs via SimPO can cut generation length 30-60% with little accuracy loss.
- [TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS](../../archive/papers/2026/title-7b2310c5e9f25bde/summary.md) — Shows diffusion LLMs implicitly contain a mixture of semi-autoregressive generation experts and introduces a training-free method that majority-votes across multiple block generation schedules to substantially boost accuracy.
- [T1: Tool-integrated Verification for Test-time Compute Scaling in Small Language Models](../../archive/papers/2026/title-b2629aee97cadc77/summary.md) — T1 is a two-stage test-time-scaling framework for small language models that filters candidate responses with external tools before a small-model verifier makes the final judgment, offloading memorization-heavy checks to the tools.
- [ATTS: Asynchronous Test-Time Scaling via Conformal Prediction](../../archive/papers/2026/title-b601ad920fcc4d45/summary.md) — ATTS uses conformal prediction to asynchronously coordinate multi-dimensional test-time scaling, cutting synchronization overhead between draft and target models during LLM inference.
- [Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning](../../archive/papers/2025/title-edfa34ba9c5ee959/summary.md) — Shows cross-entropy fine-tuning can hurt pass@N test-time performance via overconfidence, and proposes a confidence-limiting training loss that better aligns training with pass@N search.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
