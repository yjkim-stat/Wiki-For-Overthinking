# Majority Voting

<!-- auto:begin -->

Sampling several independent answers to one problem and returning the most frequent one -- the cheapest parallel test-time-compute strategy, needing no verifier and no reward model. It is the reference point most parallel methods in this archive are measured against, and sources attack it from three directions: it gains nothing when the samples are not actually diverse, which is why it transfers poorly to vision-language models; a whole-trace agreement signal dilutes the evidence needed to catch one decisive flaw in an otherwise plausible trace, so buying more samples does not buy proportionate trustworthiness; and methods that reallocate part of the same budget -- to falsifying decision-critical claims, to a few strong-verifier calls, or to short parallel chains instead of one long one -- report reaching its accuracy at roughly half the tokens or beating it by 16-27 points at small k. This archive keeps a separate 'self-consistency' record for the same idea; nothing distinguishes them and the split is spelling, not substance.

- **Kind**: method
- **Also called**: Majority Voting, maj@k, majority voting, self-consistency
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Best-of-N](best-of-n.md), [Best-of-N sampling](best-of-n-sampling.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MBPP](../datasets/mbpp.md), [MMLU](../datasets/mmlu.md), [Overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [Self-Consistency](self-consistency.md), [Test-Time Compute](../concepts/test-time-compute.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Tree Search Decoding](../concepts/tree-search-decoding.md), [weighted voting](../concepts/weighted-voting.md)

## Appears in

- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.
- [Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](../../archive/papers/2025/title-5d66fe9a10241ce8/summary.md) — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.
- [Optimal Self-Consistency for Efficient Reasoning with Large Language Models](../../archive/papers/2026/title-f4c083a2823b7a48/summary.md) — Analyses the scaling behaviour of self-consistency sampling as mode estimation, derives power-law error decay in the number of samples, and introduces Blend-ASC, a hyperparameter-free scheme that reallocates a fixed sample budget across questions.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
