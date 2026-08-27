# Sky-T1

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [MMLU-Pro](../datasets/mmlu-pro.md), [o1-mini](o1-mini.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [QwQ](qwq.md), [QwQ-32B](../methods/qwq-32b.md), [StrongReject](../datasets/strongreject.md)

## Appears in

- [One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL](../../archive/papers/2025/doi-10-18653-v1-2025-acl-industry-85/summary.md) — Introduces the Long CoT Collection, a 100K-example dataset built by having short-CoT LLMs (GPT-4o) generate o1-style long reasoning traces from a 1K seed of teacher-annotated reasoning flow and thought-budget targets, showing it is a stronger RL cold-start than the base model (2-3x larger RLVR gains) and offers built-in controllability over thought budget to address overthinking.
- [SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-1197/summary.md) — SafeChain systematically evaluates 13 large reasoning models' safety on StrongReject/WildJailbreak, finding no model is safe on both, that unsafe responses are consistently longer than safe ones, that safety improves within a model family as it scales but long-CoT fine-tuning itself does not inherently improve safety over the base instruction-tuned model, and that training-free decoding strategies controlling thought length (ZeroThink most effectively) improve safety without training -- motivating a new CoT-style safety training dataset that preserves reasoning performance while improving safety.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
