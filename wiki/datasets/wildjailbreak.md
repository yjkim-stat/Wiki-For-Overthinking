# WildJailbreak

<!-- auto:begin -->

WildJailbreak is an adversarial jailbreak-prompt benchmark used in SafeChain (systematically evaluating 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both) and PAM (training large reasoning models to explicitly assess which human-preference priority, e.g. harmlessness, applies to a query before reasoning).

- **Kind**: dataset
- **Also called**: WildJailbreak
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Activation Patching](../methods/activation-patching.md), [AdvBench](advbench.md), [AIME 2024](aime-2024.md), [AlpacaEval 2.0](alpacaeval-2-0.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [Kimi-k1.5](../models/kimi-k1-5.md), [LiveCodeBench (v5)](livecodebench-v5.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ](../models/qwq.md), [Sky-T1](../models/sky-t1.md), [StrongReject](strongreject.md), [XSTest](xstest.md)

## Appears in

- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.
- [PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-432/summary.md) — PAM trains large reasoning models to explicitly assess which human-preference priority (e.g. harmlessness) applies to a query before reasoning -- via a Flavell-metacognition-inspired cold-start SFT stage plus DPO preference optimization -- improving helpfulness, harmlessness and instruction-following by an average of ~10 points over an identically-trained model without this metacognitive step, without a corresponding drop in math reasoning performance for one of two backbones.
- [Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness](../../archive/papers/2026/local-24bb8e465bad18c7/summary.md) — A controlled, cross-paradigm mechanistic comparison of three post-training safety methods (SFT, reasoning-augmented SFT, and ORPO) across three model architectures, showing that training objective -- not just data -- reshapes how and where refusal is computed internally, and that no method studied is simultaneously robust, capability-preserving, and correctable via small steering edits.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
