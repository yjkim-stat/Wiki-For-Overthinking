# Jaccard similarity

<!-- auto:begin -->

The size of the intersection of two sets over the size of their union, used in both sources to compare which sparse-autoencoder features are active rather than how strongly they fire. Both use it on set-valued rather than vector-valued objects, which is the point, and both report a number that sounds decisive and then say why it may not be. The agent-channel study finds cross-task active-set similarity averaging 0.906 over 36 task pairs (range 0.878 to 0.922) and immediately notes the figure may be inflated by set saturation, since each task-level set is a union over many messages against a global active support of only about 50 features, and that frequency-weighted similarities, role-stratified analyses and size-matched null models are needed before reading it as semantic sharing. The set-level instability work uses the same unit of analysis to establish the opposite kind of result: adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts reading an active set as a bag of composable features. Together they mark the practice -- a set-overlap statistic needs a size-matched null, because overlap rises mechanically as the universe shrinks.

- **Kind**: method
- **Also called**: Jaccard index
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](ablation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARC-Challenge](../datasets/arc-challenge.md), [ARC-Easy](../datasets/arc-easy.md), [feature absorption](../concepts/feature-absorption.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [low-rank approximation](low-rank-approximation.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MBPP+](../datasets/mbpp.md), [monosemanticity](../concepts/monosemanticity.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [sparse autoencoder](sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [superposition](../concepts/superposition.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.
- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) — Takes the set of active sparse-autoencoder latents as the unit of analysis and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the bag-of-features reading those sets are usually given.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
