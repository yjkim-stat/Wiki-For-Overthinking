# post-training

<!-- auto:begin -->

Everything done to a base model after pretraining -- supervised fine-tuning, preference optimisation, reinforcement learning -- and across 3 sources a stage the archive treats as having its own systematic effects rather than as a neutral improvement. Two are documented. It moves the features contamination detectors rely on, which one source corrects by measuring how controlled prompt variants shift scores on known non-members and adjusting only the recurring directions, with gains concentrated at the low-false-positive operating point. And it is where safety behaviour is installed or fails to be: one source achieves alignment by changing the reasoning structure with 1,000 supervised examples and no reinforcement learning, and another adds a recovery token that cuts harmful completions from 13.8 to 4.1 percent. The archive's related material adds the pipeline-level finding that a stage ending in reinforcement learning launders what its supervised stage absorbed.

- **Kind**: concept
- **Also called**: fine-tuning stage, post-training stage
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [ablation](../methods/ablation.md), [adversarial robustness](adversarial-robustness.md), [alignment tax](alignment-tax.md), [benchmark contamination](benchmark-contamination.md), [calibration](calibration.md), [data efficiency](data-efficiency.md), [decontamination](../methods/decontamination.md), [DeepSeek](../models/deepseek.md), [distribution shift](distribution-shift.md), [generalization](generalization.md), [Llama](../models/llama.md), [membership inference](membership-inference.md), [operating point](operating-point.md), [Qwen](../models/qwen.md), [RLVR](../methods/rlvr.md), [ROC analysis](../methods/roc-analysis.md), [safety alignment](safety-alignment.md), [self-correction](self-correction.md), [self-reflection](../methods/self-reflection.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.
- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.
- [Self-Reflection Improves Safety of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-678/summary.md) — Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
