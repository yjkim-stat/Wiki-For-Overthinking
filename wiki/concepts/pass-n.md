# pass@n

<!-- auto:begin -->

Pass@n measures whether at least one of n independently sampled generations for a problem is correct, so in these sources it is used as a probe of a model's exploration or generative diversity rather than its single-best-answer accuracy. Latent Exploration Decoding frames pass@n exploration as something RL post-training destroys and restores it at inference by aggregating hidden-state posteriors across depths, with no retraining. The fine-tuning study shows plain cross-entropy fine-tuning can overconfidently narrow the sampling distribution and hurt pass@N test-time search, motivating a confidence-limiting training loss instead -- both treat pass@n's cost, the number of samples drawn, as inseparable from the score it reports.

- **Kind**: concept
- **Also called**: pass@N
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Latent Exploration Decoding (LED)](../methods/latent-exploration-decoding-led.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [parallel thinking](../methods/parallel-thinking.md), [pass@K](pass-k.md), [Qwen3-30B-A3B-Thinking](../models/qwen3-30b-a3b-thinking.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking](../models/qwen3-4b-thinking.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models](../../archive/papers/2026/local-5680089130af21f6/summary.md) — Restores lost pass@n exploration in RL-post-trained reasoning models by aggregating hidden-state posteriors from multiple depths and sampling from whichever depth's aggregated posterior has maximal entropy, with no extra training or parameters.
- [Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning](../../archive/papers/2025/title-edfa34ba9c5ee959/summary.md) — Shows cross-entropy fine-tuning can hurt pass@N test-time performance via overconfidence, and proposes a confidence-limiting training loss that better aligns training with pass@N search.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
