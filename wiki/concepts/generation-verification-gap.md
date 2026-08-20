# generation-verification gap

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [budget forcing](../methods/budget-forcing.md), [consensus](consensus.md), [diminishing returns](diminishing-returns.md), [Gemini-3-Flash](../models/gemini-3-flash.md), [Gemma-3-12B](../models/gemma-3-12b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MMMU](../datasets/mmmu.md), [paired bootstrap](../methods/paired-bootstrap.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [pool oracle](pool-oracle.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [reproducibility](reproducibility.md), [selection signal](selection-signal.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](test-time-scaling.md), [verifier-free verification](verifier-free-verification.md), [visual grounding](visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) — Treats test-time scaling as routing rather than budgeting -- cheap evidence decides whether a decision is already settled, and expensive verification is spent only on candidates that can still change the answer -- and evaluates every baseline by replaying it over the same stored candidate pool so that only the allocation decision differs.
- [Test-Time Scaling for CAD Generation via Verifier-Free Consensus Selection](../../archive/papers/2026/arxiv-2608-09706/summary.md) — Asks whether a candidate pool contains enough signal to select from itself, by compiling sampled CAD programs into 3D models and returning the one that agrees most with the rest -- and finds this verifier-free rule beats a vision-language verifier on every geometric metric when both select from the identical pool.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
