# Qwen3-Max

<!-- auto:begin -->

Qwen3-Max is used as an evaluated reasoning model in BloomEval (mapping reasoning-trace steps onto Bloom's six-level cognitive taxonomy) and CoTJudger (a graph-driven framework for automatically evaluating chain-of-thought quality).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Claude Sonnet 4.5](claude-sonnet-4-5.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528-Qwen3-8B](deepseek-r1-0528-qwen3-8b.md), [DeepSeek-V3](deepseek-v3.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Gemini-2.5-Flash-Thinking](gemini-2-5-flash-thinking.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [GPT-4o](gpt-4o.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [Grok-3](grok-3.md), [GSM8K](../datasets/gsm8k.md), [Kimi-k1.5](kimi-k1-5.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [MATH](../datasets/math.md), [Omni-MATH](../datasets/omni-math.md), [OpenAI o1-mini](openai-o1-mini.md), [Overthinking](../concepts/overthinking.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [s1-32B](s1-32b.md)

## Appears in

- [BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1262/summary.md) — BloomEval maps each step of an LRM's reasoning trace onto Bloom's six-level cognitive taxonomy (Remember through Create) via a Cognitive Hierarchy Trace (CHT), defining structural anomalies -- hierarchy break (reasoning never reaches the required cognitive level), hierarchy jump (skipping intermediate levels), and overthinking (invoking cognitive operations exceeding what the task needs) -- and finds these anomalies are common even in *correct* answers (e.g. Grok-3 shows a 0.185 hierarchy-jump rate on correct answers), demonstrating that answer accuracy alone cannot detect incoherent or wasteful reasoning structure.
- [CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2077/summary.md) — CoTJudger converts free-form CoTs into directed dependency graphs (capturing backtracking, repetition, and self-correction via classified node/edge types) and extracts the Shortest Effective Path (SEP) -- the minimal, verified-sufficient reasoning skeleton -- to compute a scale-invariant Redundancy Ratio; across 21 LRMs it finds redundancy pervasive but structurally distinct by model family (DeepSeek-R1's high-in-degree 'Cyclic Complexity' looping vs. Qwen3-Max's high-uncertainty 'Semantic Verbosity' vs. Gemini-3-Pro's low-degree 'Local Over-Optimization'), that distilled models inherit and often amplify their teacher's redundancy (a 'reasoning illusion' where distillation transfers verbosity without the underlying verification capability), and that post-answer redundancy specifically includes 'Destructive Revision' where a correct answer is unstably discarded for a wrong one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
