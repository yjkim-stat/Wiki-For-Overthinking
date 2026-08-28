# Efficient Reasoning

<!-- auto:begin -->

An umbrella label for any attempt to get a large reasoning model to reach the same answer with fewer reasoning tokens, rather than a technique of its own; the two archived sources share the goal and nothing of the mechanism. DRPO works on the RL objective, diagnosing why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and normalising correct rollouts only against each other, for 77.2% length reduction on GSM8K at 1.1% accuracy loss on a 1.5B model. FROST leaves the model untouched and edits its output, scoring sentences of the chain of thought by attention to prune 'reasoning outliers', reporting an average 69.68% token reduction and a 26.70% accuracy gain over the base model on four maths benchmarks. Read as a label the archive spans training-time reward shaping, trace pruning, early exit, latent reasoning and serving-side cache compression, so a claim about 'efficient reasoning' says little until the mechanism and the benchmark are named — both sources here are evaluated on mathematics only.

- **Kind**: concept
- **Also called**: efficient reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Score (AES)](accuracy-efficiency-score-aes.md), [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [Chain-of-Thought Compression](chain-of-thought-compression.md), [DRP](../methods/drp.md), [Early Exit](../methods/early-exit.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [Group-Relative Advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Latent reasoning](latent-reasoning.md), [Length Penalty](length-penalty.md), [Length reward](length-reward.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [RLOO](../methods/rloo.md), [SelfBudgeter](../methods/selfbudgeter.md), [Thinkless](../methods/thinkless.md), [Token Budget](token-budget.md)

## Appears in

- [DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization](../../archive/papers/2026/title-68327bf6b9e4e869/summary.md) — Diagnoses why adding a length penalty to GRPO degrades accuracy — the group-relative advantage can turn correct-but-long rollouts negative — and fixes it by normalising the reward of correct rollouts only against other correct rollouts.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
