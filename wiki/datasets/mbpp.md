# MBPP+

<!-- auto:begin -->

A Python program-synthesis benchmark, used in both sources as the coding leg of a multi-domain suite rather than as an object of study — the check that a method aimed at mathematical reasoning has not simply overfit to it. It is where one source's failure is starkest: a ternary-quantized model calibrated on generic web text scores 0.00 on it and 39.15 when calibrated on the model's own reasoning traces, against 37.03 for a 1.58-bit model trained from scratch on four trillion tokens. The other reports it among the tasks where representation-based exploration improves samples-to-correct by over 50 percent for a 14B model.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [best-of-n](../methods/best-of-n.md), [chain of thought](../methods/chain-of-thought.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [Game of 24](game-of-24.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH](math.md), [MATH500](math500.md), [Mistral-7B](../models/mistral-7b.md), [Omni-MATH](omni-math.md), [OpenCodeInstruct](opencodeinstruct.md), [pass@k](../methods/pass-k.md), [Phi-4](../models/phi-4.md), [policy entropy](../concepts/policy-entropy.md), [prompt difficulty](../concepts/prompt-difficulty.md), [ProofWriter](proofwriter.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-235B-A22B](../models/qwen3-235b-a22b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [RLVR](../methods/rlvr.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](../../archive/papers/2026/local-1fadd9f07b138261/summary.md) — Uses elliptical bonuses over a language model's own hidden-state representations as a diversity signal, validates it in a clean inference-time selection setting, then transfers the same signal into RL post-training — where it eliminates the diversity collapse that degrades pass@k at large k.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
