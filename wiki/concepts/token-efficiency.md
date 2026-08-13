# token efficiency

<!-- auto:begin -->

Accuracy divided by generated length, used in this archive as a single-number summary of the accuracy-versus-tokens trade-off. It should be read with care, because it improves whenever generation shortens and therefore rewards compression independently of whether accuracy held — in one source the composite rises from 2.81 to 6.80 while accuracy moves by 0.3 points, and at a smaller model scale the same composite improves while accuracy falls. The archive's better-behaved alternatives are a Pareto frontier of accuracy against length reduction, which shows where a method degrades rather than collapsing the curve to a point, and a weighted score that penalizes accuracy loss asymmetrically. The underlying quantity is real and the sources agree on its shape: accuracy holds within about 90% of baseline over a wide compression interval and then drops sharply, so the interesting number is where the plateau ends rather than the ratio at any single operating point.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [attention analysis](../methods/attention-analysis.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [generative rewriting](../methods/generative-rewriting.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [outcome reward](outcome-reward.md), [overthinking](overthinking.md), [process reward model](../methods/process-reward-model.md), [process supervision](process-supervision.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](reasoning-redundancy.md), [reasoning skeleton](reasoning-skeleton.md), [restructuring level](restructuring-level.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning](../../archive/papers/2025/local-c45962c819666804/summary.md) — Formalizes 'spend test-time compute well' as a meta-reinforcement-learning problem — treating one long output stream as a sequence of episodes and scoring it by cumulative regret over tokens — and trains against a dense progress bonus that outcome-only reward cannot express.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
