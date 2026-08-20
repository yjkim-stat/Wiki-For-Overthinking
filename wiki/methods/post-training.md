# post-training

<!-- auto:begin -->

Any training applied after pretraining to shape behaviour, used by both sources as the stage where a property is installed cheaply. One installs safety by altering the reasoning structure with 1K supervised examples and no RL or reward design. The other adds a special token that lets the model reflect and recover mid-generation, integrating into standard post-training rather than replacing it, and reports the harmful completion rate falling from 13.8% to 4.1%. Both emphasize that the intervention composes with existing recipes, which is the practical claim: the property is added without redesigning the pipeline.

- **Kind**: method
- **Also called**: fine-tuning stage, post-training stage
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [ablation](ablation.md), [adversarial robustness](../concepts/adversarial-robustness.md), [alignment tax](../concepts/alignment-tax.md), [benchmark contamination](../concepts/benchmark-contamination.md), [calibration](calibration.md), [data efficiency](../concepts/data-efficiency.md), [decontamination](decontamination.md), [DeepSeek](../models/deepseek.md), [distribution shift](../concepts/distribution-shift.md), [generalization](../concepts/generalization.md), [Llama](../models/llama.md), [membership inference](membership-inference.md), [operating point](../concepts/operating-point.md), [Qwen](../models/qwen.md), [ROC analysis](roc-analysis.md), [safety alignment](../concepts/safety-alignment.md), [self-correction](../concepts/self-correction.md), [self-reflection](self-reflection.md), [supervised fine-tuning](supervised-fine-tuning.md)

## Appears in

- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.
- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.
- [Self-Reflection Improves Safety of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-678/summary.md) — Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
