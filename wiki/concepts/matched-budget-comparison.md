# matched-budget comparison

<!-- auto:begin -->

A comparison in which two methods are given the same inference budget and the same downstream components, so the difference between them can be attributed to the one thing that varies. Both sources treat it as the control their central claim depends on. One constructs a control that spends the identical short-answer budget on the unperturbed image, and finds it matches or beats the perturbation-based selector everywhere — dissolving a 31.8-point apparent gain that came from comparing long chain-of-thought aggregation against short-answer aggregation. The other runs adaptive allocation and fixed full budget through the same self-certainty-and-Borda selector, stating that this isolates the budget policy from the effect of the final selector. The shared lesson is that a test-time-scaling comparison which changes the budget and the aggregation together measures neither.

- **Kind**: concept
- **Also called**: budget-matched control, selector-matched comparison
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [ablation](../methods/ablation.md), [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARC-Challenge](../datasets/arc-challenge.md), [ARC-Easy](../datasets/arc-easy.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [Jaccard similarity](../methods/jaccard-similarity.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [low-rank approximation](low-rank-approximation.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MathVision](../datasets/mathvision.md), [MBPP+](../datasets/mbpp.md), [MMMU](../datasets/mmmu.md), [monosemanticity](monosemanticity.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [SciQ](../datasets/sciq.md), [selection signal](selection-signal.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [test-time scaling](test-time-scaling.md), [uncertainty quantification](uncertainty-quantification.md), [visual grounding](visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.
- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
