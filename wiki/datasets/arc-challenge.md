# ARC-Challenge

<!-- auto:begin -->

The harder split of the AI2 Reasoning Challenge, a multiple-choice science question set, used in both sources here as a supporting evaluation rather than a target. In the latent-credit work it is one of the benchmarks on which a thought-level advantage estimate for continuous latent reasoning is measured; in the agent-channel compression study it is one of nine benchmarks over which a sparse reconstruction of the communication tensor is scored, moving from 62.12 to between 61.18 and 64.85 across compression settings -- movements that paper itself declines to interpret, since they are single-run point estimates with no paired uncertainty. Neither source describes the benchmark's construction or reports a finding about it.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARC-Easy](arc-easy.md), [compression](../concepts/compression.md), [credit assignment](../concepts/credit-assignment.md), [exploration](../concepts/exploration.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [Jaccard similarity](../methods/jaccard-similarity.md), [latent reasoning](../concepts/latent-reasoning.md), [low-rank approximation](../methods/low-rank-approximation.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH](math.md), [MATH500](math500.md), [MBPP+](mbpp.md), [MMLU-STEM](mmlu-stem.md), [monosemanticity](../concepts/monosemanticity.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [REINFORCE](../methods/reinforce.md), [soft thinking](../methods/soft-thinking.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md)

## Appears in

- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
