# ROC analysis

<!-- auto:begin -->

Scoring a detector by its trade-off between true and false positives across all thresholds, summarised as area under the curve, and reading a specific operating point off the same curve. Both sources are detection settings and both show why the summary and the operating point are different claims. The Parkinson's screen works at 13 percent prevalence, where predicting all-negative already scores 0.87 accuracy, so it reports AUROC with bootstrap intervals plus sensitivity, specificity and predictive values at a Youden-optimal point -- and the operating point is what supports its actual claim, since negative predictive value of 0.95 licenses a rule-out triage reading while positive predictive value of 0.35 does not license a diagnostic one. The contamination-detection work makes the divergence quantitative: the same calibration is worth one to four points of AUC and five to fifteen points of true positive rate at a 5 percent false-positive threshold, because AUC integrates over thresholds nobody deploys. Between them the sources establish the rule -- where a detector's two error types have different costs, the summary statistic is a screening device and the operating point is the result.

- **Kind**: method
- **Also called**: AUC, AUROC, ROC
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](ablation.md), [activation steering](activation-steering.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [calibration](calibration.md), [class imbalance](../concepts/class-imbalance.md), [CLIP](../models/clip.md), [contrastive activation addition](contrastive-activation-addition.md), [decontamination](decontamination.md), [DeepSeek](../models/deepseek.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [distribution shift](../concepts/distribution-shift.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama](../models/llama.md), [membership inference](membership-inference.md), [operating point](../concepts/operating-point.md), [permutation test](permutation-test.md), [post-training](post-training.md), [Qwen](../models/qwen.md), [shortcut learning](../concepts/shortcut-learning.md), [steering vector](steering-vector.md)

## Appears in

- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) — Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.
- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
