# self-consistency

<!-- auto:begin -->

Sampling multiple reasoning traces and taking the most common final answer, the simplest form of parallel test-time compute. A theoretical paper derives that its sample complexity (Θ(1/Δ²)) is worse than best-of-n's (Θ(1/Δ)) for some tasks; CaTS uses a confidence signal to adaptively size how many samples to draw instead of a fixed count; 'Diversity Matters' finds it mostly fails to transfer to vision-language-model accuracy gains unless sampled outputs are genuinely diverse.

- **Kind**: method
- **Also called**: Self-Consistency, Self-consistency, majority voting
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 9

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [Best-of-N](best-of-n.md), [best-of-N sampling](best-of-n-sampling.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [confidence-based early stopping](confidence-based-early-stopping.md), [confidence calibration](../concepts/confidence-calibration.md), [early stopping](early-stopping.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [HMMT 2025](../datasets/hmmt-2025.md), [LLM-as-a-Judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MathQA](../datasets/mathqa.md), [MMLU](../datasets/mmlu.md), [overthinking](../concepts/overthinking.md), [Qwen3-8B](../datasets/qwen3-8b.md), [reasoning effort](../concepts/reasoning-effort.md), [retrieval-augmented reasoning](../concepts/retrieval-augmented-reasoning.md), [Self-Certainty](self-certainty.md), [test-time compute](../concepts/test-time-compute.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [vLLM](vllm.md)

## Appears in

- [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](../../archive/papers/2026/arxiv-2608-14161/summary.md) — Introduces BiasTrace, a six-label annotation scheme for reasoning behaviours in bias-sensitive traces, and finds that overthinking (repeated second-guessing or revisiting the same options more than three times) is the strongest behavioural predictor of stereotype-aligned answers on BBQ, then uses the scheme to filter samples at inference time.
- [ParaTempo: Efficient Parallel Reasoning via Temporal Confidence](../../archive/papers/2026/arxiv-2608-16425/summary.md) — A training-free controller for parallel reasoning that probes each branch every 500 tokens for a tentative answer distribution, averages recent probes into a 'temporal confidence' score, and uses that one signal to prune, retire, fork and globally stop branches.
- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Sample Complexity and Representation Ability of Test-time Scaling Paradigms](../../archive/papers/2026/title-27bc5c2aff7ebdab/summary.md) — A theoretical paper deriving sample-complexity bounds for self-consistency versus best-of-n, and an expressiveness result showing self-correction lets a Transformer simulate online learning over multiple tasks at test time.
- [Retrieval-of-Thought: Efficient Reasoning via Reusing Thoughts](../../archive/papers/2026/title-2c8dfbd1f24680a2/summary.md) — Retrieval-of-Thought stores prior reasoning as a graph of composable thought steps and, at inference, retrieves and traverses it to assemble a problem-specific template that shortens the model's generated reasoning without retraining.
- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.
- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](../../archive/papers/2026/title-bcd9cf99a0e84a2d/summary.md) — Measures a reasoning model's inference-time effort not by how many tokens it emits but by what fraction of them are still being revised in the network's late layers, and uses that fraction to pick which of many sampled generations to keep.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.
- [Optimal Self-Consistency for Efficient Reasoning with Large Language Models](../../archive/papers/2026/title-f4c083a2823b7a48/summary.md) — Analyses the scaling behaviour of self-consistency sampling as mode estimation, derives power-law error decay in the number of samples, and introduces Blend-ASC, a hyperparameter-free scheme that reallocates a fixed sample budget across questions.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
