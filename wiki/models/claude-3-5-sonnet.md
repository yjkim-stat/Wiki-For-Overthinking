# Claude-3.5-Sonnet

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Also called**: Claude 3.5 Sonnet
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](../datasets/advbench.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Grok-3](grok-3.md), [HarmBench](../datasets/harmbench.md), [JailbreakBench](../datasets/jailbreakbench.md), [o1](o1.md), [o1-mini](o1-mini.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [QwQ-32B](qwq-32b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [Three Minds, One Legend: Jailbreak Large Reasoning Model with Adaptive Stacked Ciphers](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-355/summary.md) — SEAL red-teams large reasoning models by stacking multiple lightweight ciphers (Caesar, ASCII, HEX, word/character reversal, etc.) to encrypt a harmful prompt just past the point an LRM's safety mechanism can flag it but still within its decryption/reasoning capability -- exploiting the same chain-of-thought reasoning that improves task performance as an attack surface -- with a reinforcement-learning-based adaptive cipher-selection strategy (a gradient-bandit policy over cipher groups, updated only on failures) reaching up to 100% attack success on some LRMs and beating seven baseline jailbreak methods, while showing attack success and the model's own ability to recover the original harmful intent from ciphertext both peak at a moderate 'sweet spot' cipher complexity and decline beyond it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
