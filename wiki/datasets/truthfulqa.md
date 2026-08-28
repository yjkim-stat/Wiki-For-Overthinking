# TruthfulQA

<!-- auto:begin -->

None of the three sources describe TruthfulQA directly; it appears as one of the evaluation benchmarks in their reasoning-quality experiments. REDE uses answer-token attention over reasoning steps as annotation-free supervision to identify and drop irrelevant or repetitive steps before hallucination detection; the diffusion-LLM source shows diffusion LLMs implicitly contain a mixture of semi-autoregressive generation experts and majority-votes across block-generation schedules to boost accuracy; AdaReasoner is an RL-trained, model-agnostic plugin that picks a per-task prompt format, decoding temperature and number of reasoning steps instead of one fixed setup.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [ARC-C](arc-c.md), [Best-of-N (baseline)](../methods/best-of-n-baseline.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [GSM8K (appendix)](gsm8k-appendix.md), [LogiQA](logiqa.md), [MATH](math.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [SciQ](sciq.md), [SFT (baseline)](../methods/sft-baseline.md), [SimpleQA](simpleqa.md), [SPIRIT](../methods/spirit.md)

## Appears in

- [Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models](../../archive/papers/2026/arxiv-2607-22098/summary.md) — REDE uses the attention that the final answer token pays to each reasoning step as annotation-free supervision for a lightweight projection, in whose shaped embedding space irrelevant and repetitive steps become kNN outliers that can be dropped before a hallucination detector reads the trace.
- [MR-ALIGN: Meta-Reasoning Informed Factuality Alignment for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-204/summary.md) — MR-ALIGN names and measures the 'reasoning-answer hit gap' -- a model surfaces the correct fact early in its thinking trace but discards it before the final answer -- and fixes it by segmenting reasoning into 15 cognitively-grounded meta-reasoning states (framing, backtracking, self-verification, retrieval, etc.), estimating a transition matrix between them via EM, and using KTO with an implicit reward reweighted by how much each segment's local state-transition probability deviates from the corpus-wide pattern; without any external verifier or retrieval, this improves accuracy and reduces misleading answers across three backbones and five factual-QA/long-form-factuality benchmarks, and post-alignment reasoning traces become measurably shorter and more concise as a side effect.
- [TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS](../../archive/papers/2026/title-7b2310c5e9f25bde/summary.md) — Shows diffusion LLMs implicitly contain a mixture of semi-autoregressive generation experts and introduces a training-free method that majority-votes across multiple block generation schedules to substantially boost accuracy.
- [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](../../archive/papers/2025/title-b12c09d1a21e70d0/summary.md) — AdaReasoner is an RL-trained, model-agnostic plugin that picks a per-task reasoning configuration - prompt instruction format, decoding temperature and number of reasoning steps - instead of using one fixed prompting setup for every task.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
