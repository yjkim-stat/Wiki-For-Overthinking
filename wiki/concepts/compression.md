# compression

<!-- auto:begin -->

Reducing the size of a representation while trying to preserve what it does, and in these two sources the interesting question is what the reduction is measured against. The agent-channel study fits a sparse code to a dense communication tensor and reports a 128-fold payload reduction at cosine similarity 0.99992 with a macro-average accuracy change of -0.08 points -- then declines its own headline, noting that the measurements establish empirical redundancy without identifying which part is structural, numerical, low-rank or specifically sparse, and that a simple 18-position payload would already be comparable in size. The driving work compresses in a different direction, replacing a 40-to-80-token natural-language rationale with two to six executable tokens from a fixed vocabulary, where the binding constraint is an external 12 Hz control budget the verbose form exceeds by three to four times. The two mark the two available justifications: compression is worth claiming when the reduction is measured against a rival compression scheme at matched rate, or when an external budget makes the uncompressed form inadmissible regardless of how well it performs.

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARC-Challenge](../datasets/arc-challenge.md), [ARC-Easy](../datasets/arc-easy.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [component ablation](../methods/component-ablation.md), [degenerate generation](degenerate-generation.md), [flow matching](../methods/flow-matching.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [Jaccard similarity](../methods/jaccard-similarity.md), [latent reasoning](latent-reasoning.md), [low-rank approximation](../methods/low-rank-approximation.md), [matched-budget comparison](../methods/matched-budget-comparison.md), [MBPP+](../datasets/mbpp.md), [monosemanticity](monosemanticity.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [structured chain of thought](../methods/structured-chain-of-thought.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.
- [XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving](../../archive/papers/2026/arxiv-2608-10976/summary.md) — Replaces a verbose natural-language rationale with two to six executable action tokens drawn from a fixed vocabulary, supervised automatically by pairing logged trajectories with scene context, so that driving-oriented reasoning fits inside a real-time control budget that verbose chain-of-thought exceeds by three to four times.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
