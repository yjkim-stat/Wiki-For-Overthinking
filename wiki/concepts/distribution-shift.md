# distribution shift

<!-- auto:begin -->

The deployment distribution differing from the one a model or detector was fitted on, and in both sources here something to be measured and corrected rather than assumed away. The multimodal robustness work locates the shift on the prompt side, arguing that RLVR training covers only a thin slice of the semantically equivalent phrasings a deployed model will meet, and shows the cost is not confined to unseen prompts -- standard training's own in-distribution accuracy falls from 49.5 to 47.7 as the evaluation template set grows from one to five. The contamination-detection work locates it in the model instead: post-training by instruction tuning, preference optimisation or reasoning-oriented training changes the style, length, structure and content of generated output, which shifts the membership features a detector reads and reduces the separation it depends on. That paper's own caution is worth carrying: it identifies shifts associated with elevated non-member scores during calibration rather than proving those shifts are caused by post-training, since they may equally reflect dataset artifacts, decoding behaviour or the feature extractor. Between them the sources mark the two directions a fitted component can be invalidated -- the inputs move, or the model does.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [benchmark contamination](benchmark-contamination.md), [calibration](../methods/calibration.md), [component ablation](../methods/component-ablation.md), [decontamination](../methods/decontamination.md), [DeepSeek](../models/deepseek.md), [format compliance](format-compliance.md), [GRPO](../methods/grpo.md), [Llama](../models/llama.md), [MathVista](../datasets/mathvista.md), [membership inference](../methods/membership-inference.md), [operating point](operating-point.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [out-of-domain generalization](out-of-domain-generalization.md), [outcome reward](outcome-reward.md), [pass@k](pass-k.md), [post-training](../methods/post-training.md), [prompt sensitivity](prompt-sensitivity.md), [Qwen](../models/qwen.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [reward hacking](reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](../methods/rlvr.md), [ROC analysis](../methods/roc-analysis.md)

## Appears in

- [Improving Generalization Robustness of Multimodal RLVR](../../archive/papers/2026/arxiv-2608-08802/summary.md) — Traces the brittleness of multimodal RLVR gains under paraphrase and template change to two properties of the standard objective -- a binary verifier that cannot distinguish a wrong answer from a misformatted one, and a training distribution covering a thin slice of the prompts a deployed model meets -- and fixes both with a trinary reward and an invariance penalty across semantically equivalent prompts.
- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
