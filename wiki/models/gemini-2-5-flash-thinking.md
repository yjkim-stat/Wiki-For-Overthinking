# Gemini-2.5-Flash-Thinking

<!-- auto:begin -->

Gemini-2.5-Flash-Thinking is used in these sources as an evaluated LRM subject to overthinking-related stress-testing: REST finds it, like other SOTA models, degrades substantially (e.g. -31.6% on AIME25) when multiple questions are concatenated into one prompt, attributing this largely to an 'overthinking trap,' and CoTJudger's token-length-distribution analysis notes it is notable for producing extreme outliers (>60,000 tokens), indicative of instability and ineffective halting mechanisms in edge cases.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-C](../datasets/arc-c.md), [BBH](../datasets/bbh.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [DeepScaleR-1.5B](deepscaler-1-5b.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH500](../datasets/math500.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [Qwen3-Max](qwen3-max.md)

## Appears in

- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.
- [CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2077/summary.md) — CoTJudger converts free-form CoTs into directed dependency graphs (capturing backtracking, repetition, and self-correction via classified node/edge types) and extracts the Shortest Effective Path (SEP) -- the minimal, verified-sufficient reasoning skeleton -- to compute a scale-invariant Redundancy Ratio; across 21 LRMs it finds redundancy pervasive but structurally distinct by model family (DeepSeek-R1's high-in-degree 'Cyclic Complexity' looping vs. Qwen3-Max's high-uncertainty 'Semantic Verbosity' vs. Gemini-3-Pro's low-degree 'Local Over-Optimization'), that distilled models inherit and often amplify their teacher's redundancy (a 'reasoning illusion' where distillation transfers verbosity without the underlying verification capability), and that post-answer redundancy specifically includes 'Destructive Revision' where a correct answer is unstably discarded for a wrong one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
