# AMC

<!-- auto:begin -->

A competition-math benchmark used alongside AIME and MATH-500 in the archive's 3 sources as a standard hard-reasoning evaluation set: verifier-free self-correction (Refining Over Resampling), self-braking tuning, and reasoning-step pruning (LIMOPro). The sources use it only as an evaluation target, not describing its construction.

- **Kind**: dataset
- **Also called**: AMC23, American Mathematics Competitions
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [MATH-500](math-500.md), [overthinking](../concepts/overthinking.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — A training-free, verifier-free test-time scaling method that refines each of N sampled reasoning rollouts through D rounds of self-critique and self-correction before majority-voting the answers, instead of only sampling more candidates or relying on an external verifier.
- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
