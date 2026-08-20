# confidence calibration

<!-- auto:begin -->

Whether the certainty a model expresses matches how often it is right. The two sources approach it from opposite ends and together mark the trap. One trains for it, adding a reward term proportional to answer-token confidence when the answer is correct and to minus that confidence when it is wrong, and reports expected calibration error falling to 0.115 on one benchmark against 0.181 for the best baseline -- but the reward optimises the same answer-token probability the metric is computed from, so the improvement is partly a check that optimisation succeeded rather than independent evidence. The other measures it and finds the failure is not a matter of degree: binning by plurality agreement, the highest-agreement bin is correct 52.5 percent of the time for one model and 28.6 for another -- lower than that model's own lowest-agreement bin, so its accuracy is not even monotone in confidence. The consequences follow immediately: any method that gates, routes or stops on the model's own confidence is reading a signal that on hard problems carries almost none of the information it needs, which is why two verifier-free gates in that study capture 0.8 percent and minus 1.6 of the available headroom.

- **Kind**: concept
- **Also called**: calibration
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [difficulty stratification](../methods/difficulty-stratification.md), [expected calibration error](expected-calibration-error.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [hallucination](hallucination.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [PathVQA](../datasets/pathvqa.md), [post-hoc rationalization](post-hoc-rationalization.md), [pre-registration](../methods/pre-registration.md), [premature convergence](premature-convergence.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [rejection sampling](../methods/rejection-sampling.md), [reward shaping](reward-shaping.md), [selective prediction](selective-prediction.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](test-time-scaling.md), [verifiable reward](verifiable-reward.md), [VQA-RAD](../datasets/vqa-rad.md)

## Appears in

- [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](../../archive/papers/2026/arxiv-2608-10964/summary.md) — Adds a correctness-conditioned confidence term to the GRPO reward for medical visual question answering -- rewarding answer-token confidence when the answer is right and penalising it when wrong -- on top of an SFT cold start built from answer-conditioned reasoning traces filtered by a verifier.
- [When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems for Small LLMs](../../archive/papers/2026/arxiv-2608-11403/summary.md) — Measures, under a pre-registered confirmatory design, how often majority-vote self-consistency lowers per-problem accuracy on a hard science benchmark, and shows that two cheap verifier-free gates recover essentially none of the headroom a per-problem oracle marks out.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
