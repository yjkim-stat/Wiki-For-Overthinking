# LiveCodeBench (v5)

<!-- auto:begin -->

LiveCodeBench (v5) is a competitive-coding benchmark, version 5, used in this archive by SafeChain's safety evaluation of 13 large reasoning models and by REST's multi-question stress test, which finds even SOTA models degrade substantially under simultaneous multi-problem prompting due to an 'overthinking trap.'

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ARC-C](arc-c.md), [BBH](bbh.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DeepScaleR-1.5B](../models/deepscaler-1-5b.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [MATH500](math500.md), [MBPP](mbpp.md), [o3-mini](../models/o3-mini.md), [o4-mini](../models/o4-mini.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [QwQ](../models/qwq.md), [Sky-T1](../models/sky-t1.md), [StrongReject](strongreject.md), [WildJailbreak](wildjailbreak.md), [XSTest](xstest.md)

## Appears in

- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.
- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
