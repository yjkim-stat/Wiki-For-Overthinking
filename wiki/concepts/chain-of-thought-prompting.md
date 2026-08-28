# chain-of-thought prompting

<!-- auto:begin -->

Eliciting an explicit step-by-step reasoning trace in the model's output before its answer. Neither archived source studies the technique itself - both take the visible trace as the given substrate that their own method operates on, which is how the term is used loosely throughout the archive. The self-consistency scaling paper works over whole traces sampled repeatedly, analysing majority voting as mode estimation with power-law error decay in the number of samples; DEER works inside a single trace, watching for the points where the model switches thought chains, prompting for a trial answer there and terminating the chain of thought once that answer's token confidence exceeds a threshold. What both rely on is only that the reasoning is emitted as tokens at all, so that it can be sampled again or cut short.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [BigCodeBench](../datasets/bigcodebench.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [Chain-of-Thought Compression](chain-of-thought-compression.md), [DEER](../methods/deer.md), [Dynamic Early Exit](../methods/dynamic-early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [Latent reasoning](latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama 3.3 70B](../models/llama-3-3-70b.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Self-Consistency](../methods/self-consistency.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-Time Scaling](test-time-scaling.md)

## Appears in

- [On Generalization across Measurement Systems: LLMs Entail More Test-Time Compute for Underrepresented Cultures](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1032/summary.md) — LLMs default to Western measurement systems (USD, kilometers, kilograms) reflecting their training-data culture, suffer significant accuracy drops when queried in a non-default system (currency, length, or weight), and while chain-of-thought/sequential reasoning stabilizes large models' accuracy back toward the default level, it increases test-time compute by 180-300% -- disproportionately burdening users whose cultural context is not the default.
- [Optimal Self-Consistency for Efficient Reasoning with Large Language Models](../../archive/papers/2026/title-f4c083a2823b7a48/summary.md) — Analyses the scaling behaviour of self-consistency sampling as mode estimation, derives power-law error decay in the number of samples, and introduces Blend-ASC, a hyperparameter-free scheme that reallocates a fixed sample budget across questions.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
