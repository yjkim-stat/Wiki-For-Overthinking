# MMMU

<!-- auto:begin -->

A broad multimodal understanding benchmark spanning many academic subjects, used across 3 sources as the general multimodal column. Its archived appearances are mostly in test-time-scaling audits: one finds that a consistency-based selection result is driven by the decoding format rather than by the perturbation it was attributed to, and another compares input-side against output-side diversity at matched compute, reporting +2.01 against +1.01 on it from a 66.1 percent baseline. It also appears as an evaluation for structured process rewards. The archive's related caution for multimodal benchmarks applies: accuracy can be preserved while the image plays no role.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [answer aggregation](../methods/answer-aggregation.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [generation-verification gap](../concepts/generation-verification-gap.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../methods/matched-budget-comparison.md), [MATH500](math500.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU](mmlu.md), [MMMU-Pro](mmmu-pro.md), [outcome reward](../concepts/outcome-reward.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [process reward](../concepts/process-reward.md), [process reward model](../concepts/process-reward-model.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [reward shaping](../methods/reward-shaping.md), [RLVR](../methods/rlvr.md), [selection signal](../concepts/selection-signal.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.
- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](../../archive/papers/2026/arxiv-2608-09351/summary.md) — Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
