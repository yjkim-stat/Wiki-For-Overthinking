# SimpleQA

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [ASDiv](asdiv.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [greedy decoding](../methods/greedy-decoding.md), [GSM8K](gsm8k.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [SciQ](sciq.md), [SFT (baseline)](../methods/sft-baseline.md), [TruthfulQA](truthfulqa.md)

## Appears in

- [Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-773/summary.md) — TRACE decomposes reasoning traces into sub-thoughts and labeled progression graphs across 14 thinking models and 6 domains, finding thinking helps only within a narrow middle ground (5-20x more compute wasted on simple tasks with no gain, and no benefit at all once model scale exceeds ~4-8B or task difficulty exceeds representational capacity), identifies two overthinking-driving thought-progression patterns (Explorer, Late Landing), and redefines overthinking structurally as continuation past the point where marginal return per sub-thought drops below a threshold.
- [MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-204/summary.md) — MR-ALIGN names and measures the 'reasoning-answer hit gap' -- a model surfaces the correct fact early in its thinking trace but discards it before the final answer -- and fixes it by segmenting reasoning into 15 cognitively-grounded meta-reasoning states (framing, backtracking, self-verification, retrieval, etc.), estimating a transition matrix between them via EM, and using KTO with an implicit reward reweighted by how much each segment's local state-transition probability deviates from the corpus-wide pattern; without any external verifier or retrieval, this improves accuracy and reduces misleading answers across three backbones and five factual-QA/long-form-factuality benchmarks, and post-alignment reasoning traces become measurably shorter and more concise as a side effect.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
