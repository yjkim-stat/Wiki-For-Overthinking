# DeepSeek-V3.2

<!-- auto:begin -->

DeepSeek-V3.2 is used in these sources as an annotator/judge model rather than a subject of study: TRACE uses it (alongside Qwen3.5-Plus and KIMI-K2.5) as one of three LRMs annotating the safety of prompts, reasoning traces and responses. Timely Machine is a separate, unrelated source that happens to share this concept's promotion threshold but does not name DeepSeek-V3.2 specifically in its cited note.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME](../datasets/aime.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [Gemini-2.5-Flash-Thinking](gemini-2-5-flash-thinking.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [Gemma-4-E4B](gemma-4-e4b.md), [GLM-4.6](glm-4-6.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [Kimi-K2.5](kimi-k2-5.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [MATH](../datasets/math.md), [Overthinking](../concepts/overthinking.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [Qwen3.5-Plus](qwen3-5-plus.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-Max](qwen3-max.md)

## Appears in

- [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](../../archive/papers/2026/arxiv-2608-24232/summary.md) — TRACE is a benchmark that extends LLM-safety evaluation from prompts and final responses to the reasoning traces of large reasoning models, with evidence-grounded annotations for each safety label.
- [Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-211/summary.md) — Timely Machine redefines test-time scaling in agentic settings as wall-clock time rather than token/generation length (since unpredictable tool-call latency decouples the two), introduces Timely-Eval to benchmark this, and trains Timely-RL (SFT cold-start + a sinusoidal time-utilization RL reward) so an 8B model learns to query elapsed time and dynamically size its reasoning to a time budget, beating much larger models' on-time completion rates and outperforming Qwen3-8B on all three general-reasoning benchmarks.
- [CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2077/summary.md) — CoTJudger converts free-form CoTs into directed dependency graphs (capturing backtracking, repetition, and self-correction via classified node/edge types) and extracts the Shortest Effective Path (SEP) -- the minimal, verified-sufficient reasoning skeleton -- to compute a scale-invariant Redundancy Ratio; across 21 LRMs it finds redundancy pervasive but structurally distinct by model family (DeepSeek-R1's high-in-degree 'Cyclic Complexity' looping vs. Qwen3-Max's high-uncertainty 'Semantic Verbosity' vs. Gemini-3-Pro's low-degree 'Local Over-Optimization'), that distilled models inherit and often amplify their teacher's redundancy (a 'reasoning illusion' where distillation transfers verbosity without the underlying verification capability), and that post-answer redundancy specifically includes 'Destructive Revision' where a correct answer is unstably discarded for a wrong one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
