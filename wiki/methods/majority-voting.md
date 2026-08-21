# majority voting

<!-- auto:begin -->

Sampling multiple independent answers and taking the most common one, a simple parallel test-time-compute strategy that needs no verifier or reward model. 'Diversity Matters' finds it mostly fails to improve vision-language-model accuracy unless the sampled outputs are actually diverse; 'Does Thinking More Always Help?' proposes 'parallel thinking' (multiple short chains plus majority vote) as an alternative to extending a single chain, beating extended thinking by up to 20%.

- **Kind**: method
- **Also called**: Majority Voting, self-consistency
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Best-of-N](best-of-n.md), [best-of-N sampling](best-of-n-sampling.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MBPP](../datasets/mbpp.md), [MMLU](../datasets/mmlu.md), [overthinking](../concepts/overthinking.md), [process reward model](../concepts/process-reward-model.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [tree-search decoding](../concepts/tree-search-decoding.md), [weighted voting](../concepts/weighted-voting.md)

## Appears in

- [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](../../archive/papers/2025/title-0d818df77a2dc810/summary.md) — An empirical study of compute-optimal inference that measures accuracy against FLOPs for greedy decoding, sampling with majority and weighted voting, best-of-n and tree search across model sizes, and introduces REBASE, a reward-guided tree search.
- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.
- [Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](../../archive/papers/2025/title-5d66fe9a10241ce8/summary.md) — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.
- [Optimal Self-Consistency for Efficient Reasoning with Large Language Models](../../archive/papers/2026/title-f4c083a2823b7a48/summary.md) — Analyses the scaling behaviour of self-consistency sampling as mode estimation, derives power-law error decay in the number of samples, and introduces Blend-ASC, a hyperparameter-free scheme that reallocates a fixed sample budget across questions.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
