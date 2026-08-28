# AdvBench

<!-- auto:begin -->

AdvBench is a jailbreak/harmfulness benchmark used in this archive by Mousetrap, which achieves 87.5-93.13% attack success on it against Claude-Sonnet by exploiting 'reasoning inertia' (a model following its reasoning chain to completion without re-evaluating safety), and by ReasoningGuard, a training-free inference-time defense that reduces harmfulness on it to near zero across four model families at only 5-9% extra inference cost.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](aime-2024.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DeepSeek-R1](../models/deepseek-r1.md), [Gemini 2.5 Flash](../models/gemini-2-5-flash.md), [Gemini-2.5-Pro](../models/gemini-2-5-pro.md), [GPQA-Diamond](gpqa-diamond.md), [gpt-o3](../models/gpt-o3.md), [HarmBench](harmbench.md), [MATH500](math500.md), [MMLU](mmlu.md), [o1](../models/o1.md), [o1-mini](../models/o1-mini.md), [o3-mini](../models/o3-mini.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [StrongReject](strongreject.md), [WildJailbreak](wildjailbreak.md), [XSTest](xstest.md)

## Appears in

- [A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-408/summary.md) — Mousetrap is the first jailbreak attack framework designed against large reasoning models: a 'Chaos Machine' iteratively applies reversible one-to-one prompt mappings (character/word/sentence-level ciphers) to embed a toxic query inside a multi-step reconstruction task, exploiting the finding that LRMs exhibit 'reasoning inertia' -- once started, they follow the reasoning chain to completion by inertia and neglect to re-evaluate safety -- achieving up to 96-98% attack success against o1-mini, Claude-3.5-Sonnet and Gemini-2.0-Thinking and 87.5-93.13% on standard safety benchmarks against Claude-Sonnet.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — AutoRAN is the first automated framework for hijacking a large reasoning model's internal safety deliberation, using a weaker, less-aligned auxiliary model to simulate the target's execution reasoning and iteratively refine attack prompts from leaked refusal reasoning, achieving near-100% attack success against gpt-o3/o4-mini and Gemini-2.5-Flash within a few turns.
- [PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-432/summary.md) — PAM trains large reasoning models to explicitly assess which human-preference priority (e.g. harmlessness) applies to a query before reasoning -- via a Flavell-metacognition-inspired cold-start SFT stage plus DPO preference optimization -- improving helpfulness, harmlessness and instruction-following by an average of ~10 points over an identically-trained model without this metacognitive step, without a corresponding drop in math reasoning performance for one of two backbones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
