# XSTest

<!-- auto:begin -->

XSTest is an exaggerated-safety (over-refusal) benchmark used in this archive by SafeChain's 13-model safety evaluation and by ReasoningGuard, whose attention-aware safety injection achieves the best or near-best exaggerated-safety scores (0.95/0.84 F1) among training-free defenses, mitigating the over-refusal problem other jailbreak defenses introduce.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Activation Patching](../methods/activation-patching.md), [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DeepSeek-R1-Llama-8B](../models/deepseek-r1-llama-8b.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [Kimi-k1.5](../models/kimi-k1-5.md), [LiveCodeBench (v5)](livecodebench-v5.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [Phi-4-Reasoning](../models/phi-4-reasoning.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ](../models/qwq.md), [QwQ-32B](../models/qwq-32b.md), [Sky-T1](../models/sky-t1.md), [Sorry-bench](sorry-bench.md), [StrongReject](strongreject.md), [WildJailbreak](wildjailbreak.md)

## Appears in

- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.
- [Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness](../../archive/papers/2026/local-24bb8e465bad18c7/summary.md) — A controlled, cross-paradigm mechanistic comparison of three post-training safety methods (SFT, reasoning-augmented SFT, and ORPO) across three model architectures, showing that training objective -- not just data -- reshapes how and where refusal is computed internally, and that no method studied is simultaneously robust, capability-preserving, and correctable via small steering edits.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
