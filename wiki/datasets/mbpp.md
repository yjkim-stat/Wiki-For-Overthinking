# MBPP+

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](aime24.md), [AIME25](aime25.md), [best-of-n](../methods/best-of-n.md), [chain of thought](../methods/chain-of-thought.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [Game of 24](game-of-24.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH](math.md), [MATH-500](math-500.md), [Mistral-7B](../models/mistral-7b.md), [Omni-MATH](omni-math.md), [OpenCodeInstruct](opencodeinstruct.md), [pass-k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLVR](../methods/rlvr.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](../../archive/papers/2026/local-1fadd9f07b138261/summary.md) — Uses elliptical bonuses over a language model's own hidden-state representations as a diversity signal, validates it in a clean inference-time selection setting, then transfers the same signal into RL post-training — where it eliminates the diversity collapse that degrades pass@k at large k.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
