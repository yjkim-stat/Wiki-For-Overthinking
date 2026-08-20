# pool oracle

<!-- auto:begin -->

An upper bound that selects the best candidate present in a generated pool, using label information no deployable rule has, and in both sources reported not as a ceiling to be admired but as a diagnostic. The compute-balanced routing work labels it explicitly as an upper bound that uses evaluator-side information, separates it from directly implementable baselines and from proxies, and then reads its per-dataset gap as telling which half of the pipeline is limiting -- where the oracle gap is large, generation rather than selection is the bottleneck and no better selector will close it. The CAD consensus work uses it the same way and adds a mechanism for why its own rule cannot approach it: consensus favours candidates near the centre of the pool and therefore systematically discards high-quality outliers, which is a property of agreement-based selection generally rather than of that implementation. The archive's reading is that an oracle row is cheap, bounds every selection claim in the same table, and is the only thing that distinguishes a weak selector from an exhausted candidate pool.

- **Kind**: concept
- **Also called**: oracle selection
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [best-of-n](../methods/best-of-n.md), [budget forcing](../methods/budget-forcing.md), [consensus](consensus.md), [diminishing returns](diminishing-returns.md), [Gemini-3-Flash](../models/gemini-3-flash.md), [Gemma-3-12B](../models/gemma-3-12b.md), [generation-verification gap](generation-verification-gap.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [MATH500](../datasets/math500.md), [paired bootstrap](../methods/paired-bootstrap.md), [reproducibility](reproducibility.md), [selection signal](selection-signal.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](test-time-scaling.md), [verifier-free verification](../methods/verifier-free-verification.md)

## Appears in

- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) — Treats test-time scaling as routing rather than budgeting -- cheap evidence decides whether a decision is already settled, and expensive verification is spent only on candidates that can still change the answer -- and evaluates every baseline by replaying it over the same stored candidate pool so that only the allocation decision differs.
- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) — Asks whether a candidate pool contains enough signal to select from itself, by compiling sampled CAD programs into 3D models and returning the one that agrees most with the rest -- and finds this verifier-free rule beats a vision-language verifier on every geometric metric when both select from the identical pool.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
