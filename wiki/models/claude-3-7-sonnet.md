# Claude-3.7-Sonnet

<!-- auto:begin -->

A closed-source reasoning-capable model used across sources as an evaluation target: for long-CoT safety benchmarking (found unsafe on standard jailbreak/safety datasets despite its safety reputation) and as a jailbreak target for the Mousetrap iterative-chaos attack framework, which achieves high attack success against it specifically because of its noted strong safety alignment.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [DeepSeek-R1](deepseek-r1.md), [Gemini 2.5 Flash](gemini-2-5-flash.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [gpt-o3](gpt-o3.md), [Grok-3](grok-3.md), [GSM8K](../datasets/gsm8k.md), [HarmBench](../datasets/harmbench.md), [HumanEval](../datasets/humaneval.md), [Kimi-k1.5](kimi-k1-5.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [o1](o1.md), [o1-mini](o1-mini.md), [o3-mini](o3-mini.md), [Qwen3-8B](qwen3-8b.md), [QwQ](qwq.md), [Sky-T1](sky-t1.md), [StrongReject](../datasets/strongreject.md), [WildJailbreak](../datasets/wildjailbreak.md), [XSTest](../datasets/xstest.md)

## Appears in

- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.
- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
