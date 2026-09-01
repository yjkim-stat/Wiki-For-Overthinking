# HarmBench

<!-- auto:begin -->

HarmBench is used in these sources as a standard safety benchmark against which jailbreak-attack success is measured: Mousetrap reports 87.5-93.13% attack success against Claude-Sonnet on standard safety benchmarks including HarmBench-style evaluation, and AutoRAN evaluates its safety-hijacking framework in the same family of benchmarks, though the specific per-benchmark breakdown is not detailed in the cited notes.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdvBench](advbench.md), [Claude-3.5-Sonnet](../models/claude-3-5-sonnet.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DeepSeek-R1](../models/deepseek-r1.md), [Gemini 2.5 Flash](../models/gemini-2-5-flash.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [gpt-o3](../models/gpt-o3.md), [Grok-3](../models/grok-3.md), [JailbreakBench](jailbreakbench.md), [o1](../models/o1.md), [o1-mini](../models/o1-mini.md), [o3-mini](../models/o3-mini.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [StrongReject](strongreject.md)

## Appears in

- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.
- [Conflicts Make Large Reasoning Models Vulnerable to Attacks](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-463/summary.md) — A single-turn, non-narrative jailbreak method that simply instructs an LRM to reason through an explicit internal conflict (e.g. Helpfulness vs. Harmlessness) or moral dilemma (e.g. a duress or sacrificial scenario) before answering a harmful query substantially raises attack success rates across three models and five safety benchmarks (e.g. QwQ-32B: direct-query ASR 0.04 to conflict-injected 0.523 on AdvBench) with no fine-tuning, multi-turn interaction, or gradient access, and layerwise/neuron-level analysis shows the conflict prompt causes safety-relevant and functional activation subspaces to shift and overlap specifically in middle-to-late layers, weakening safety alignment at the representational level.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
