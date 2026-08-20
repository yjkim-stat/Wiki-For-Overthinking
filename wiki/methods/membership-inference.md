# membership inference

<!-- auto:begin -->

Testing whether a specific example was in a model's training data, used in the archive as the main practical handle on benchmark contamination. The sources disagree about whether it works. One applies it as a supporting analysis alongside neuron patterns and attention maps to explain a compositional performance drop. The other finds contamination detection fragile in reasoning models, with GRPO training concealing detection — so a model can be contaminated and pass the test. Taken together the archive holds a method that is routinely cited as a contamination check and a result showing the check can be defeated by ordinary reasoning training.

- **Kind**: method
- **Also called**: MIA, training-data membership test
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [ablation](ablation.md), [AIME 2024](../datasets/aime-2024.md), [attention analysis](attention-analysis.md), [benchmark contamination](../concepts/benchmark-contamination.md), [calibration](../concepts/calibration.md), [compositional generalization](../concepts/compositional-generalization.md), [construct validity](../concepts/construct-validity.md), [decontamination](decontamination.md), [DeepSeek](../models/deepseek.md), [distribution shift](../concepts/distribution-shift.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [importance sampling](importance-sampling.md), [Llama](../models/llama.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [operating point](../concepts/operating-point.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [permutation test](permutation-test.md), [post-training](post-training.md), [PPO](ppo.md), [Pythia-410M](../models/pythia-410m.md), [Qwen](../models/qwen.md), [RLVR](rlvr.md), [ROC analysis](roc-analysis.md), [supervised fine-tuning](supervised-fine-tuning.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](../../archive/papers/2026/arxiv-2608-07914/summary.md) — Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](../../archive/papers/2026/local-4cf1061e50d8b3c3/summary.md) — Shows that benchmark contamination in reasoning models is alarmingly easy to hide: a brief round of GRPO erases the signals contamination detectors rely on, and PPO-style importance sampling and clipping are identified as the cause — implying a broad class of RL methods conceals contamination inherently.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
