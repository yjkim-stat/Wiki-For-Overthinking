# Kimi-K2-Thinking

<!-- auto:begin -->

Kimi-K2-Thinking is used in these sources as a top-tier reasoning model evaluated on hard benchmarks rather than a subject of methodological study: PaCoRe cites frontier-model comparisons including this one when reporting an 8B model with massively-parallel test-time compute surpassing GPT-5 on HMMT 2025, and AMO-Bench separately evaluates it among 36 models on its original hard-problem math set.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [benchmark saturation](../concepts/benchmark-saturation.md), [Claude-Opus-4.5](claude-opus-4-5.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [DeepSeek-V3.2](deepseek-v3-2.md), [DeepSeek-V3.2-Speciale](deepseek-v3-2-speciale.md), [Gemini-2.5-Flash-Thinking](gemini-2-5-flash-thinking.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [HMMT 2025](../datasets/hmmt-2025.md), [HMMT25](../datasets/hmmt25.md), [MATH500](../datasets/math500.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Overthinking](../concepts/overthinking.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [Qwen3-Max](qwen3-max.md)

## Appears in

- [PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1253/summary.md) — PaCoRe (Parallel Coordinated Reasoning) decouples test-time compute scaling from a fixed context window by running rounds of massively parallel reasoning trajectories, compacting each trajectory's conclusion into a short message, and RL-training the model to synthesize (not just vote on) these messages into better subsequent exploration -- letting an 8B model reach 94.5% on HMMT 2025 by scaling effective test-time compute to ~2 million tokens, surpassing GPT-5's 93.2%.
- [AMO-Bench: Large Language Models Still Struggle in High School Math Competitions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-101/summary.md) — AMO-Bench is a 50-problem, IMO-difficulty-or-harder, entirely original math benchmark built to avoid the saturation and memorization issues of AIME24/25, on which even the best of 36 evaluated LLMs (Gemini-3-Pro) reaches only 63.1% accuracy, model performance grows near-linearly with the logarithm of output length (still-unsaturated evidence that test-time scaling keeps paying off), and a manual failure analysis finds brute-force enumeration and improper strategy selection -- reasoning deficiency, not missing math knowledge -- as the dominant error modes.
- [CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2077/summary.md) — CoTJudger converts free-form CoTs into directed dependency graphs (capturing backtracking, repetition, and self-correction via classified node/edge types) and extracts the Shortest Effective Path (SEP) -- the minimal, verified-sufficient reasoning skeleton -- to compute a scale-invariant Redundancy Ratio; across 21 LRMs it finds redundancy pervasive but structurally distinct by model family (DeepSeek-R1's high-in-degree 'Cyclic Complexity' looping vs. Qwen3-Max's high-uncertainty 'Semantic Verbosity' vs. Gemini-3-Pro's low-degree 'Local Over-Optimization'), that distilled models inherit and often amplify their teacher's redundancy (a 'reasoning illusion' where distillation transfers verbosity without the underlying verification capability), and that post-answer redundancy specifically includes 'Destructive Revision' where a correct answer is unstably discarded for a wrong one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
