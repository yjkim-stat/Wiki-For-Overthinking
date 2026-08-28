# ARC-C

<!-- auto:begin -->

ARC-C (AI2 Reasoning Challenge, Challenge set) is a benchmark used in this archive as one of nine benchmarks in REST's multi-question stress test, where the 'overthinking trap' is identified as a primary cause of degraded performance under simultaneous multi-problem prompting, and in a diffusion-LLM test-time-scaling paper that majority-votes across multiple block-generation schedules. Sources cite it only as an evaluation benchmark without further characterization.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [BBH](bbh.md), [DeepScaleR-1.5B](../models/deepscaler-1-5b.md), [DeepSeek-R1](../models/deepseek-r1.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [LiveCodeBench (v5)](livecodebench-v5.md), [MATH](math.md), [MATH500](math500.md), [o3-mini](../models/o3-mini.md), [o4-mini](../models/o4-mini.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [TruthfulQA](truthfulqa.md)

## Appears in

- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.
- [TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS](../../archive/papers/2026/title-7b2310c5e9f25bde/summary.md) — Shows diffusion LLMs implicitly contain a mixture of semi-autoregressive generation experts and introduces a training-free method that majority-votes across multiple block generation schedules to substantially boost accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
