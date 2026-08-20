# MMMU

<!-- auto:begin -->

A multimodal benchmark used in this archive as one evaluation set among several in two test-time-scaling audits, neither of which describes how it was built. In the vision-language decoding-format audit it is one of four benchmarks on which a format-matched control matches the perturbation-based selector it was meant to beat (50.1 against 50.3), and it is also where the two diagnostics decouple: blanking the perturbation inputs collapses the selection score from 50.2 to 23.3, confirming the signal genuinely depends on the image, while its mean stability gap is only +0.071. In the test-time-augmentation study Claude 4.5 Haiku has a 66.1 percent chain-of-thought baseline on it, and paraphrase-based input diversity adds +2.01 against +1.01 for self-consistency at matched compute. Across both, it behaves as a mid-difficulty multimodal set where the headline effects are small enough that the control matters more than the method.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [answer aggregation](../methods/answer-aggregation.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [generation-verification gap](../concepts/generation-verification-gap.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH500](math500.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU](mmlu.md), [MMMU-Pro](mmmu-pro.md), [outcome reward](../concepts/outcome-reward.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [process reward](../concepts/process-reward.md), [process reward model](../concepts/process-reward-model.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](../methods/rlvr.md), [selection signal](../concepts/selection-signal.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.
- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](../../archive/papers/2026/arxiv-2608-09351/summary.md) — Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
