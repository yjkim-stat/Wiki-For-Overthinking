# verifier-free verification

<!-- auto:begin -->

Judging or selecting among candidates without an external checker, using only what the model and its own pool supply -- adopted because compilers, test cases and trained value functions do not exist for most tasks. The three sources differ in what signal they read and agree that the naive one fails. Confidence maximisation is the naive one, and it can perform worse than random selection from the same pool, because uniformly high confidence indicates a failure to branch rather than a well-supported answer, so a maximiser preferentially selects confident collapses onto a flawed premise; the correction reads the temporal shape instead, penalising early certainty while requiring late certainty. The CAD work reads agreement over compiled artifacts rather than over text, and beats a trained vision-language verifier on every geometric metric when both select from identical pools -- closing with the recommendation that any verifier used for selection be compared against consensus on the same pool. The claim-level work spends half its sampling budget on trying to refute decision-critical claims and weights the consensus by how many survive, with its own limitation being that a near-saturated model gains almost nothing. The shared position is that the pool carries usable signal, that agreement is the cheapest null any verifier should be raced against, and that the useful signal is a shape or a survival rate rather than a level.

- **Kind**: method
- **Also called**: verifier-free selection
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [answer aggregation](answer-aggregation.md), [best-of-n](best-of-n.md), [calibration](../concepts/calibration.md), [CMIMC](../datasets/cmimc.md), [consensus](../concepts/consensus.md), [cross-validation](cross-validation.md), [difficulty conditioning](difficulty-conditioning.md), [difficulty stratification](difficulty-stratification.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [Gemini-3-Flash](../models/gemini-3-flash.md), [Gemma-3-12B](../models/gemma-3-12b.md), [generation-verification gap](../concepts/generation-verification-gap.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [HMMT 2025](../datasets/hmmt-2025.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [pass@k](../concepts/pass-k.md), [pool oracle](../concepts/pool-oracle.md), [premature convergence](../concepts/premature-convergence.md), [process supervision](../concepts/process-supervision.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [selection signal](../concepts/selection-signal.md), [self-certainty](self-certainty.md), [self-consistency](self-consistency.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) — Asks whether a candidate pool contains enough signal to select from itself, by compiling sampled CAD programs into 3D models and returning the one that agrees most with the rest -- and finds this verifier-free rule beats a vision-language verifier on every geometric metric when both select from the identical pool.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Shows that selecting the most confident rollout can be worse than picking at random, because uniformly high confidence signals a failure to explore rather than a well-supported answer, and replaces maximisation with a temporal criterion that penalises early certainty while requiring late certainty.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
