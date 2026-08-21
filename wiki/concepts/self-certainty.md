# Self-Certainty

<!-- auto:begin -->

Neither source explains self-certainty's own definition; it appears as a named signal alongside their own primary contributions. The test-time-scaling framework paper treats it as one of the token-level or verifier-style signals attached to its released reasoning-trace dataset; 'Think Deep, Not Just Long' instead measures effort by the fraction of tokens still being revised in the network's late layers rather than by self-certainty, and uses that measure to pick which sampled generation to keep.

- **Kind**: concept
- **Also called**: self-certainty
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BBH](../datasets/bbh.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT 2025](../datasets/hmmt-2025.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Overthinking](overthinking.md), [reasoning effort](reasoning-effort.md), [Self-Consistency](../methods/self-consistency.md), [SuperGPQA](../datasets/supergpqa.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-time scaling](test-time-scaling.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](../../archive/papers/2026/title-bcd9cf99a0e84a2d/summary.md) — Measures a reasoning model's inference-time effort not by how many tokens it emits but by what fraction of them are still being revised in the network's late layers, and uses that fraction to pick which of many sampled generations to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
