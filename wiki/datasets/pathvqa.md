# PathVQA

<!-- auto:begin -->

A pathology visual question answering set of roughly 5,000 images and 33,000 question-answer pairs, used in both sources as the hardest of the three standard medical VQA benchmarks. Its difficulty is what makes it informative here: the best calibration-aware system reaches 0.689 accuracy on it against 0.873 on a radiology-and-knowledge set, and its expected calibration error is the worst of the three for every model compared (0.290 for the best, 0.587 for the worst). It is also where that paper's stage ablation is most extreme, with reinforcement learning alone scoring 0.955 on closed-ended questions against 0.863 for the full pipeline while scoring 0.166 against 0.421 on open-ended ones -- a 0.79 spread between question types on the same benchmark. The robustness source uses it among the sets where multimodal verifiable-reward gains are tested under paraphrase and template change.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [component ablation](../methods/component-ablation.md), [confidence calibration](../concepts/confidence-calibration.md), [distribution shift](../concepts/distribution-shift.md), [expected calibration error](../methods/expected-calibration-error.md), [format compliance](../concepts/format-compliance.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [hallucination](../concepts/hallucination.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](mathvista.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [outcome reward](../concepts/outcome-reward.md), [pass@k](../concepts/pass-k.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [rejection sampling](../methods/rejection-sampling.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../methods/reward-shaping.md), [RLVR](../methods/rlvr.md), [selective prediction](../concepts/selective-prediction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [verifiable reward](../concepts/verifiable-reward.md), [VQA-RAD](vqa-rad.md)

## Appears in

- [Improving Generalization Robustness of Multimodal RLVR](../../archive/papers/2026/arxiv-2608-08802/summary.md) — Traces the brittleness of multimodal RLVR gains under paraphrase and template change to two properties of the standard objective -- a binary verifier that cannot distinguish a wrong answer from a misformatted one, and a training distribution covering a thin slice of the prompts a deployed model meets -- and fixes both with a trinary reward and an invariance penalty across semantically equivalent prompts.
- [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](../../archive/papers/2026/arxiv-2608-10964/summary.md) — Adds a correctness-conditioned confidence term to the GRPO reward for medical visual question answering -- rewarding answer-token confidence when the answer is right and penalising it when wrong -- on top of an SFT cold start built from answer-conditioned reasoning traces filtered by a verifier.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
