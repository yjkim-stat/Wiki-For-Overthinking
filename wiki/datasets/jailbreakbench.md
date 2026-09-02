# JailbreakBench

<!-- auto:begin -->

JailbreakBench is a benchmark for evaluating jailbreak attacks against large reasoning models, used to evaluate Mousetrap's Chaos Machine cipher-based jailbreak and a single-turn jailbreak method that instructs an LRM to reason through an explicit internal conflict or moral dilemma to bypass safety training.

- **Kind**: dataset
- **Also called**: JailBreakBench
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](advbench.md), [Claude-3.5-Sonnet](../models/claude-3-5-sonnet.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DeepSeek-R1](../models/deepseek-r1.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [Grok-3](../models/grok-3.md), [HarmBench](harmbench.md), [Llama-Guard-3 (ASR judge)](../models/llama-guard-3-asr-judge.md), [o1](../models/o1.md), [o1-mini](../models/o1-mini.md), [o3-mini](../models/o3-mini.md), [QwQ-32B](../models/qwq-32b.md), [StrongReject](strongreject.md)

## Appears in

- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [Conflicts Make Large Reasoning Models Vulnerable to Attacks](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-463/summary.md) — A single-turn, non-narrative jailbreak method that simply instructs an LRM to reason through an explicit internal conflict (e.g. Helpfulness vs. Harmlessness) or moral dilemma (e.g. a duress or sacrificial scenario) before answering a harmful query substantially raises attack success rates across three models and five safety benchmarks (e.g. QwQ-32B: direct-query ASR 0.04 to conflict-injected 0.523 on AdvBench) with no fine-tuning, multi-turn interaction, or gradient access, and layerwise/neuron-level analysis shows the conflict prompt causes safety-relevant and functional activation subspaces to shift and overlap specifically in middle-to-late layers, weakening safety alignment at the representational level.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
