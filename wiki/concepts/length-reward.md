# Length reward

<!-- auto:begin -->

A reward term in RL fine-tuning that pays a reasoning model for producing a shorter trace; the archived sources use it interchangeably with 'length penalty', the same signal with the sign flipped. The archive's strongest result about it is negative: REA-RL measures a plain length reward on top of GRPO taking DeepSeek-R1-Distill-Qwen-7B from 80.39% to 76.88% average accuracy while cutting the token ratio to 57.23, i.e. buying roughly 36% fewer tokens with about 3.5 accuracy points, and recovers 80.74% at a token ratio of 63.51 only by adding a reflection-density reward and a distilled 7B reflection model. DRPO diagnoses the cause — under GRPO's group-relative normalisation a length penalty can drive the advantage of a correct-but-long rollout negative — and fixes it by normalising correct rollouts only against other correct rollouts, reporting 77.2% length reduction on GSM8K for 1.1% accuracy loss at 1.5B where the next-best baseline gave 68% for 4.3%, though its Accuracy-Efficiency Score turns negative on AIME. DR2Seg shows the signal need not be absolute: it rewards a second-stage rollout for reasoning more briefly than the first against a length anchor N0, cutting reasoning tokens about threefold (26.9 against 85.3) while raising gIoU.

- **Kind**: concept
- **Also called**: Length Reward
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Score (AES)](accuracy-efficiency-score-aes.md), [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Efficient Reasoning](efficient-reasoning.md), [Group-Relative Advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Laser](../methods/laser.md), [Length Penalty](length-penalty.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Segmentation](reasoning-segmentation.md), [ReasonSeg](../datasets/reasonseg.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Sequential revision](sequential-revision.md), [Task Decomposition](task-decomposition.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-474d6c4d88a30199/summary.md) — REA-RL trains a large reasoning model online with a distilled 7B reflection model that supplies both parallel samples and truncated sequential revisions, plus a reflection-density reward, cutting response length about 36% on math benchmarks without losing accuracy.
- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
