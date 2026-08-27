# o1-mini

<!-- auto:begin -->

A closed-source OpenAI reasoning model used across sources as a reference for long-CoT reasoning-flow distillation data collection (the Long CoT Collection's seed data was manually gathered from o1's reasoning flow and thought budget), and as a primary jailbreak target for the Mousetrap iterative-chaos-chain attack, against which it achieves a 96% attack success rate.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [o1](o1.md), [o3-mini](o3-mini.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [QwQ-32B](../methods/qwq-32b.md), [Sky-T1](sky-t1.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL](../../archive/papers/2025/doi-10-18653-v1-2025-acl-industry-85/summary.md) — Introduces the Long CoT Collection, a 100K-example dataset built by having short-CoT LLMs (GPT-4o) generate o1-style long reasoning traces from a 1K seed of teacher-annotated reasoning flow and thought-budget targets, showing it is a stronger RL cold-start than the base model (2-3x larger RLVR gains) and offers built-in controllability over thought budget to address overthinking.
- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
