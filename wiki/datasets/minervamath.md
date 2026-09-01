# minervamath

<!-- auto:begin -->

Minerva Math is used in these sources as a math-reasoning benchmark for hallucination-detection and test-time-compute-allocation methods: RFS-Guard evaluates its attention-based hallucination-detection method on it (among MATH/Science/MultiHopQA domains), and the evolving-in-context-demonstration adaptive-allocation study uses it as one of five benchmarks measuring coverage-per-token-budget gains.

- **Kind**: dataset
- **Also called**: MinervaMath
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive test-time compute allocation](../methods/adaptive-test-time-compute-allocation.md), [AIME 2025](aime-2025.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-5-Nano](../models/gpt-5-nano.md), [LiveCodeBench](livecodebench.md), [MATH500](math500.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning hallucination](../concepts/reasoning-hallucination.md), [routing collapse](../concepts/routing-collapse.md)

## Appears in

- [RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-885/summary.md) — RFS-Guard detects and localizes reasoning hallucinations in LRMs training-free, using a Routing Focus Score (RFS) that measures how strongly cross-step attention between reasoning and answer phases collapses toward semantic-neighbor proximity (rather than task-critical evidence) -- finding this 'routing collapse' is a strong hallucination signal that beats sampling-based, uncertainty-based, and other self-aware baselines while remaining far more inference-efficient.
- [Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1754/summary.md) — A test-time-compute-allocation framework unifies where to spend compute (which unresolved queries get more sampling) with how generation is performed there (conditioning new samples on in-context demonstrations retrieved, via semantic similarity, from other queries already solved during the same inference run) -- consistently beating uniform Best-of-N and a difficulty-adaptive elimination baseline in coverage-per-token across four model families and multiple math/coding/reasoning benchmarks, with gains concentrated early in test-time scaling.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
