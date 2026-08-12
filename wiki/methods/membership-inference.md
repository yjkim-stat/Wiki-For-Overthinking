# membership inference

<!-- auto:begin -->

Testing whether a specific example was in a model's training data, used in the archive as the main practical handle on benchmark contamination. The sources disagree about whether it works. One applies it as a supporting analysis alongside neuron patterns and attention maps to explain a compositional performance drop. The other finds contamination detection fragile in reasoning models, with GRPO training concealing detection — so a model can be contaminated and pass the test. Taken together the archive holds a method that is routinely cited as a contamination check and a result showing the check can be defeated by ordinary reasoning training.

- **Kind**: method
- **Also called**: MIA, training-data membership test
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [attention analysis](attention-analysis.md), [benchmark contamination](../concepts/benchmark-contamination.md), [compositional generalization](../concepts/compositional-generalization.md), [construct validity](../concepts/construct-validity.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [importance sampling](importance-sampling.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [PPO](ppo.md), [RLVR](rlvr.md), [supervised finetuning](supervised-finetuning.md)

## Appears in

- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](../../archive/papers/2026/local-4cf1061e50d8b3c3/summary.md) — Shows that benchmark contamination in reasoning models is alarmingly easy to hide: a brief round of GRPO erases the signals contamination detectors rely on, and PPO-style importance sampling and clipping are identified as the cause — implying a broad class of RL methods conceals contamination inherently.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
