# ARC-Challenge

<!-- auto:begin -->

The harder split of the AI2 Reasoning Challenge, a multiple-choice science question set, used in both sources here as a supporting evaluation rather than a target. In the latent-credit work it is one of the benchmarks on which a thought-level advantage estimate for continuous latent reasoning is measured; in the agent-channel compression study it is one of nine benchmarks over which a sparse reconstruction of the communication tensor is scored, moving from 62.12 to between 61.18 and 64.85 across compression settings -- movements that paper itself declines to interpret, since they are single-run point estimates with no paired uncertainty. Neither source describes the benchmark's construction or reports a finding about it.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [ablation](../methods/ablation.md), [abstention](../concepts/abstention.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARC-Easy](arc-easy.md), [calibration](../methods/calibration.md), [component ablation](../methods/component-ablation.md), [compression](../concepts/compression.md), [coverage](../concepts/coverage.md), [credit assignment](../concepts/credit-assignment.md), [difficulty conditioning](../concepts/difficulty-conditioning.md), [difficulty stratification](../methods/difficulty-stratification.md), [exploration](../concepts/exploration.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [hallucination](../concepts/hallucination.md), [HumanEval+](humaneval.md), [Jaccard similarity](../methods/jaccard-similarity.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [low-rank approximation](../methods/low-rank-approximation.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH](math.md), [MATH500](math500.md), [MBPP+](mbpp.md), [MMLU-STEM](mmlu-stem.md), [monosemanticity](../concepts/monosemanticity.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.5-9B](../models/qwen3-5-9b.md), [reasoning boundary](../concepts/reasoning-boundary.md), [REINFORCE](../methods/reinforce.md), [reward shaping](../concepts/reward-shaping.md), [selective prediction](../concepts/selective-prediction.md), [self-correction](../concepts/self-correction.md), [self-reflection](../methods/self-reflection.md), [soft thinking](../methods/soft-thinking.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [StrategyQA](strategyqa.md), [structured chain of thought](../methods/structured-chain-of-thought.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment](../../archive/papers/2026/arxiv-2608-07931/summary.md) — Separates hallucination into a reasoning failure and a knowledge failure, treats the first with a structured reflect-before-answering format and the second with a reward for abstaining when no sampled chain succeeds, and shows the two mechanisms are not interchangeable -- reflection alone never abstains, abstention alone never lowers the hallucination proxy.
- [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](../../archive/papers/2026/arxiv-2608-10198/summary.md) — Fits a post-hoc sparse autoencoder to the frozen dense tensors that two vision-language agents exchange, finds a 128-fold payload reduction at near-identical reconstruction and roughly unchanged single-run accuracy, and then spends most of the paper enumerating the alternative explanations its own design cannot rule out.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
