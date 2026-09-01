# adaptive test-time compute allocation

<!-- auto:begin -->

Adaptive test-time compute allocation refers to methods that dynamically decide how much inference-time compute (sampling, reasoning mode, or search budget) to spend per query rather than applying a fixed budget uniformly. 'Learning When to Think' trains a 1.5B model to emit one of three mode tokens (NoThink/Short/Long) as its very first token, learned end-to-end inside GRPO with no separate router; a second source unifies allocation (which queries get more sampling) with in-context-demonstration-based distributional adaptation, beating uniform Best-of-N in coverage-per-token.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AutoThink](autothink.md), [DAPO](dapo.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [Dr. GRPO](dr-grpo.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-5-Nano](../models/gpt-5-nano.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [minervamath](../datasets/minervamath.md), [RLVR](rlvr.md), [routing collapse](../concepts/routing-collapse.md), [Thinkless](thinkless.md)

## Appears in

- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1754/summary.md) — A test-time-compute-allocation framework unifies where to spend compute (which unresolved queries get more sampling) with how generation is performed there (conditioning new samples on in-context demonstrations retrieved, via semantic similarity, from other queries already solved during the same inference run) -- consistently beating uniform Best-of-N and a difficulty-adaptive elimination baseline in coverage-per-token across four model families and multiple math/coding/reasoning benchmarks, with gains concentrated early in test-time scaling.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
