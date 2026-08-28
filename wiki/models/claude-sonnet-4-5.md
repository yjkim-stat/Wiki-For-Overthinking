# Claude Sonnet 4.5

<!-- auto:begin -->

Claude Sonnet 4.5 appears in this archive as one of the LLMs deployed within multi-agent or long-horizon test-time-scaling systems studied by the sources -- Routed Graph Handoff uses it in its multi-agent delegation benchmarks, and FS-Researcher uses it within its file-system-based deep-research framework -- without further characterization from the sources themselves.

- **Kind**: model
- **Also called**: Claude-Sonnet-4.5
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [BrowseComp](../datasets/browsecomp.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Gemini-2.5-Flash-Thinking](gemini-2-5-flash-thinking.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [GPT-5](gpt-5.md), [GPT-5 mini](gpt-5-mini.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [Overthinking](../concepts/overthinking.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [Qwen3-Max](qwen3-max.md)

## Appears in

- [Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation](../../archive/papers/2026/arxiv-2608-25277/summary.md) — Routed Graph Handoff (RGH) uses a lightweight LLM router to pick, per delegation, between a typed dependency-graph message and natural-language prose for multi-agent LLM handoffs, matching or beating NL-only on every one of four benchmarks while cutting token cost 2-3x.
- [FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-288/summary.md) — FS-Researcher is a dual-agent (Context Builder / Report Writer) deep-research framework that scales test-time compute beyond a single context window by persisting evidence and task state in an external file-system workspace instead of the model's context, achieving state-of-the-art report quality on two open-ended benchmarks and outperforming official agent harnesses on an answer-verifiable search benchmark.
- [CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2077/summary.md) — CoTJudger converts free-form CoTs into directed dependency graphs (capturing backtracking, repetition, and self-correction via classified node/edge types) and extracts the Shortest Effective Path (SEP) -- the minimal, verified-sufficient reasoning skeleton -- to compute a scale-invariant Redundancy Ratio; across 21 LRMs it finds redundancy pervasive but structurally distinct by model family (DeepSeek-R1's high-in-degree 'Cyclic Complexity' looping vs. Qwen3-Max's high-uncertainty 'Semantic Verbosity' vs. Gemini-3-Pro's low-degree 'Local Over-Optimization'), that distilled models inherit and often amplify their teacher's redundancy (a 'reasoning illusion' where distillation transfers verbosity without the underlying verification capability), and that post-answer redundancy specifically includes 'Destructive Revision' where a correct answer is unstably discarded for a wrong one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
