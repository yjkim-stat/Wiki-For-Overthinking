# XSTest

<!-- auto:begin -->

XSTest is an exaggerated-safety (over-refusal) benchmark used in this archive by SafeChain's 13-model safety evaluation and by ReasoningGuard, whose attention-aware safety injection achieves the best or near-best exaggerated-safety scores (0.95/0.84 F1) among training-free defenses, mitigating the over-refusal problem other jailbreak defenses introduce.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [Kimi-k1.5](../models/kimi-k1-5.md), [LiveCodeBench (v5)](livecodebench-v5.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ](../models/qwq.md), [QwQ-32B](../models/qwq-32b.md), [Sky-T1](../models/sky-t1.md), [StrongReject](strongreject.md), [WildJailbreak](wildjailbreak.md)

## Appears in

- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
