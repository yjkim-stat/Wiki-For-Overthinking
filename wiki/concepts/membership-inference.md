# membership inference

<!-- auto:begin -->

Deciding whether a particular example was in a model's training data, and across 4 sources the technical core of contamination auditing. The archive's results are mostly about the limits. Detectability is governed by a single quantity combining contamination fraction, effect size and sample count, and the resulting power predictions transport across settings while the sample-size budgets derived from them do not -- so an audit can be planned for power and not for cost. Post-training moves the features detectors rely on, which one source corrects by measuring how controlled prompt variants shift scores on known non-members and adjusting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC. And a brief round of reinforcement learning suppresses the signals outright, attributed to importance sampling and clipping rather than to any specific algorithm. The standing consequence is that a negative audit result on a post-trained model is close to uninformative unless its power was calculated in advance.

- **Kind**: concept
- **Also called**: MIA, training-data membership test
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [ablation](../methods/ablation.md), [AIME 2024](../datasets/aime-2024.md), [attention analysis](../methods/attention-analysis.md), [benchmark contamination](benchmark-contamination.md), [calibration](calibration.md), [compositional generalization](compositional-generalization.md), [construct validity](construct-validity.md), [decontamination](../methods/decontamination.md), [DeepSeek](../models/deepseek.md), [distribution shift](distribution-shift.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [importance sampling](../methods/importance-sampling.md), [Llama](../models/llama.md), [MATH500](../datasets/math500.md), [memorization](memorization.md), [operating point](operating-point.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [permutation test](../methods/permutation-test.md), [post-training](post-training.md), [PPO](../methods/ppo.md), [Pythia-410M](../models/pythia-410m.md), [Qwen](../models/qwen.md), [RLVR](../methods/rlvr.md), [ROC analysis](../methods/roc-analysis.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](../../archive/papers/2026/arxiv-2608-07914/summary.md) — Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](../../archive/papers/2026/local-4cf1061e50d8b3c3/summary.md) — Shows that benchmark contamination in reasoning models is alarmingly easy to hide: a brief round of GRPO erases the signals contamination detectors rely on, and PPO-style importance sampling and clipping are identified as the cause — implying a broad class of RL methods conceals contamination inherently.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
