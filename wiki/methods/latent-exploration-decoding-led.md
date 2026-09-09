# Latent Exploration Decoding (LED)

<!-- auto:begin -->

Latent Exploration Decoding (LED) is a training-free, parameter-free decoding strategy that restores pass@n exploration lost after RL post-training of reasoning models, whose final-layer output entropy collapses even though intermediate layers retain higher entropy (a 'latent entropy reservoir'). At each generation step it restricts the last several layers' posteriors to the final layer's top-k token list (k=20 by default) so only already-plausible tokens are reweighted, accumulates these filtered posteriors from the final layer backward by depth, and samples from whichever depth's cumulative posterior has the highest entropy. Across five models and six benchmarks it improves pass@1 by 0.61 points and pass@16 by 1.03 points on average with negligible change in generation length, but the gain is under 1.5 points, and on QwQ-32B -- whose entropy rises rather than collapses at the final layer -- it does not help and can mildly hurt pass@16.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [pass@n](../concepts/pass-n.md), [Qwen3-30B-A3B-Thinking](../models/qwen3-30b-a3b-thinking.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking](../models/qwen3-4b-thinking.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models](../../archive/papers/2026/local-5680089130af21f6/summary.md) — Restores lost pass@n exploration in RL-post-trained reasoning models by aggregating hidden-state posteriors from multiple depths and sampling from whichever depth's aggregated posterior has maximal entropy, with no extra training or parameters.
- [Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models](../../archive/papers/2026/title-6dbcef192c93a1b8/summary.md) — Identifies 'exploration collapse' after RL post-training of large reasoning models -- temperature-based sampling no longer increases pass@n accuracy because final-layer output entropy diminishes even though intermediate-layer entropy stays high -- and proposes Latent Exploration Decoding (LED), a training-free depth-conditioned decoding strategy that aggregates intermediate-layer posteriors to restore exploration, improving pass@1 by 0.61 and pass@16 by 1.03 points on average across benchmarks and models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
