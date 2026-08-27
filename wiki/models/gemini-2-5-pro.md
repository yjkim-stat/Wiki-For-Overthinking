# Gemini-2.5-Pro

<!-- auto:begin -->

A closed-source reasoning model used as a comparison/generator model in a parallel-reasoning study (named among frontier models compared against a trained Parason variant) and as a jailbreak evaluation target in the Mousetrap iterative-chaos-chain attack, where -- alongside other advanced reasoning models tested -- it is found to be nearly completely jailbroken at chain lengths up to 3.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [critical-path latency](../concepts/critical-path-latency.md), [DeepSeek-R1](deepseek-r1.md), [GPT-5.5](gpt-5-5.md), [MATH500](../datasets/math500.md), [o1](o1.md), [o1-mini](o1-mini.md), [o3-mini](o3-mini.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) — Parason distinguishes two forms of parallel reasoning -- AND-branch Subtask Parallelism and OR-branch Trial Parallelism -- shows Trial Parallelism dominates on hard reasoning traces, and trains models to convert sequential CoT into grammar-structured parallel trajectories that a real inference engine executes for ~1.7x wall-clock speedup with competitive accuracy.
- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [Red Teaming Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1034/summary.md) — Rt-LRM is a unified 30-task benchmark evaluating large reasoning models along truthfulness, safety and efficiency, testing both CoT-hijacking (direct interference with the reasoning process) and prompt-induced impacts (jailbreaks or overthinking triggers); across 26 models it finds LRMs are consistently less trustworthy than their own base LLMs, that explicit reasoning can amplify safety risk and inefficiency under attack, and that over 60% of tested samples exhibit overthinking (more than double the clean-input token count) across most models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
