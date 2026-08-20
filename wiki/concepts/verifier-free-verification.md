# verifier-free verification

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [answer aggregation](../methods/answer-aggregation.md), [best-of-n](../methods/best-of-n.md), [calibration](../methods/calibration.md), [CMIMC](../datasets/cmimc.md), [consensus](consensus.md), [cross-validation](../methods/cross-validation.md), [difficulty conditioning](difficulty-conditioning.md), [entropy collapse](entropy-collapse.md), [exploration](exploration.md), [Gemini-3-Flash](../models/gemini-3-flash.md), [Gemma-3-12B](../models/gemma-3-12b.md), [generation-verification gap](generation-verification-gap.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [HMMT 2025](../datasets/hmmt-2025.md), [LiveCodeBench](../datasets/livecodebench.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [pass@k](pass-k.md), [pool oracle](pool-oracle.md), [process supervision](process-supervision.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [selection signal](selection-signal.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) — Asks whether a candidate pool contains enough signal to select from itself, by compiling sampled CAD programs into 3D models and returning the one that agrees most with the rest -- and finds this verifier-free rule beats a vision-language verifier on every geometric metric when both select from the identical pool.
- [Consilience for Verifier-Free Test-Time Scaling](../../archive/papers/2026/arxiv-2608-09898/summary.md) — Shows that selecting the most confident rollout can be worse than picking at random, because uniformly high confidence signals a failure to explore rather than a well-supported answer, and replaces maximisation with a temporal criterion that penalises early certainty while requiring late certainty.
- [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](../../archive/papers/2026/arxiv-2608-11994/summary.md) — Reallocates half of a test-time sampling budget from generating more solutions to asking the same model to refute a handful of decision-critical claims extracted from each trace, then weights the consensus vote by how many claims survive.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
