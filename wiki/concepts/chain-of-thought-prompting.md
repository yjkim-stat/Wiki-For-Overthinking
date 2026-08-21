# chain-of-thought prompting

<!-- auto:begin -->

Eliciting an explicit step-by-step reasoning trace in the model's output before its answer. Neither archived source studies the technique itself - both take the visible trace as the given substrate that their own method operates on, which is how the term is used loosely throughout the archive. The self-consistency scaling paper works over whole traces sampled repeatedly, analysing majority voting as mode estimation with power-law error decay in the number of samples; DEER works inside a single trace, watching for the points where the model switches thought chains, prompting for a trial answer there and terminating the chain of thought once that answer's token confidence exceeds a threshold. What both rely on is only that the reasoning is emitted as tokens at all, so that it can be sampled again or cut short.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](chain-of-thought-compression.md), [DEER](../methods/deer.md), [Dynamic Early Exit](dynamic-early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [latent reasoning](../methods/latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [self-consistency](../methods/self-consistency.md), [test-time compute scaling](test-time-compute-scaling.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Optimal Self-Consistency for Efficient Reasoning with Large Language Models](../../archive/papers/2026/title-f4c083a2823b7a48/summary.md) — Analyses the scaling behaviour of self-consistency sampling as mode estimation, derives power-law error decay in the number of samples, and introduces Blend-ASC, a hyperparameter-free scheme that reallocates a fixed sample budget across questions.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
