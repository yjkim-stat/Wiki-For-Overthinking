# Grok-3

<!-- auto:begin -->

Grok-3 is used in these sources as an evaluated LRM: BloomEval reports it shows a hierarchy-jump rate of 0.185 even on correct answers (the highest among evaluated LRMs) under its Cognitive Hierarchy Trace analysis, illustrating that answer correctness does not guarantee coherent reasoning structure; Mousetrap's cited note does not name Grok-3 specifically.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](../datasets/advbench.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-V3](deepseek-v3.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [HarmBench](../datasets/harmbench.md), [Kimi-k1.5](kimi-k1-5.md), [MATH](../datasets/math.md), [o1](o1.md), [o1-mini](o1-mini.md), [o3-mini](o3-mini.md), [Omni-MATH](../datasets/omni-math.md), [OpenAI o1-mini](openai-o1-mini.md), [Qwen3-Max](qwen3-max.md), [s1-32B](s1-32b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1262/summary.md) — BloomEval maps each step of an LRM's reasoning trace onto Bloom's six-level cognitive taxonomy (Remember through Create) via a Cognitive Hierarchy Trace (CHT), defining structural anomalies -- hierarchy break (reasoning never reaches the required cognitive level), hierarchy jump (skipping intermediate levels), and overthinking (invoking cognitive operations exceeding what the task needs) -- and finds these anomalies are common even in *correct* answers (e.g. Grok-3 shows a 0.185 hierarchy-jump rate on correct answers), demonstrating that answer accuracy alone cannot detect incoherent or wasteful reasoning structure.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
