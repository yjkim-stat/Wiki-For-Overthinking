# gpt-o3

<!-- auto:begin -->

GPT-o3 is used in these sources as a target model for safety-reasoning attacks and as a baseline for planning tasks: AutoRAN reports near-100% attack success hijacking gpt-o3/o4-mini's internal safety deliberation, and SCOPE reports large accuracy and cost/time gains over a chain-of-thought baseline on a multi-constraint planning benchmark (though that specific gain figure is reported for GPT-4o rather than o3 in the cited note).

- **Kind**: model
- **Also called**: GPT-o3
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdvBench](../datasets/advbench.md), [Chain-of-Thought (CoT, baseline)](../methods/chain-of-thought-cot-baseline.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-V3.2-Speciale](deepseek-v3-2-speciale.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [gpt-oss-120b](gpt-oss-120b.md), [HarmBench](../datasets/harmbench.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-8B](qwen3-8b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.
- [Programming over Thinking: Efficient and Robust Multi-Constraint Planning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2028/summary.md) — SCOPE replaces long natural-language reasoning chains for multi-constraint planning with a two-stage, multi-agent pipeline that infers a query's combination/constraint structure once and compiles it into reusable, deterministic solver functions (Combination/Filter/Deliver), reaching 93.1% success on TravelPlanner with GPT-4o (a 61.6-point gain over CoT) while cutting inference cost 1.4x and time 4.67x versus the best baseline.
- [AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1885/summary.md) — AlgBench replaces problem-centric algorithmic benchmarks (which conflate multiple algorithms per problem and risk contamination) with 3,000 expert-curated, contamination-free problems each isolating exactly one of 27 algorithms under a six-category taxonomy, finding LRMs handle non-optimized/Euclidean-structured algorithms well (up to 92%) but collapse on global-optimization tasks like dynamic programming (~49%), that model-parameter scaling barely helps in exactly those weak categories, and that 'strategic over-shifts' -- models abandoning a correct algorithmic design mid-execution -- are specifically triggered by necessary low-entropy tokens (numeric constants, structural delimiters) that standard maximum-entropy RL training penalizes as if they were uncertain, unproductive continuations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
