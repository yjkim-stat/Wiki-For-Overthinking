# ASDiv

<!-- auto:begin -->

ASDiv is used in these sources as an easier-tier math-reasoning benchmark for measuring where test-time compute stops paying off: TRACE's vertical difficulty analysis places ASDiv-1/2 at the low-difficulty end of its math progression (where thinking mode shows negligible accuracy benefit over non-thinking, unlike harder items such as GSM8K); C4 is unrelated to ASDiv in its own cited note (a diffusion-language-model decoding paper).

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [C4](../methods/c4.md), [Confidence Calibration](../concepts/confidence-calibration.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [Early Exit](../methods/early-exit.md), [greedy decoding](../methods/greedy-decoding.md), [GSM-Hard](gsm-hard.md), [GSM8K](gsm8k.md), [HellaSwag](hellaswag.md), [HumanEval](humaneval.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLaMA-3-8B-Instruct](../models/llama-3-8b-instruct.md), [MATH](math.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [Overthinking](../concepts/overthinking.md), [Process Reward Model (PRM)](../concepts/process-reward-model-prm.md), [Qwen2.5-Math-1.5B-Instruct](../models/qwen2-5-math-1-5b-instruct.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [SimpleQA](simpleqa.md), [SVAMP](svamp.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-773/summary.md) — TRACE decomposes reasoning traces into sub-thoughts and labeled progression graphs across 14 thinking models and 6 domains, finding thinking helps only within a narrow middle ground (5-20x more compute wasted on simple tasks with no gain, and no benefit at all once model scale exceeds ~4-8B or task difficulty exceeds representational capacity), identifies two overthinking-driving thought-progression patterns (Explorer, Late Landing), and redefines overthinking structurally as continuation past the point where marginal return per sub-thought drops below a threshold.
- [A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-511/summary.md) — DREAM decomposes tree-based test-time search into separate planning and execution phases, each with its own reward model and adaptive per-step budget allocation, improving the accuracy-tokens tradeoff over standard beam search and majority voting on math reasoning and code generation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
