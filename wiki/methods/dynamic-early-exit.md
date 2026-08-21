# Dynamic Early Exit

<!-- auto:begin -->

Both sources use dynamic early exit in the reasoning sense: a per-instance decision to terminate a large reasoning model's chain of thought at a natural boundary in the generated text, once a signal indicates the answer has already settled, rather than at a fixed token budget. DEER does it training-free at the points where the model switches thought chains, prompting for a trial answer there and stopping when that answer's token confidence clears a threshold; BLADE trains a lightweight probe on hidden states to judge, at sentence and self-doubt boundaries, whether the reasoning prefix already supports the correct answer, and stops when it does. The 'exit' is from the token stream, not from the layer stack: despite BLADE being titled layer-adaptive, its layers only supply probe features, and neither method leaves a forward pass early in the sense of early-exit neural networks.

- **Kind**: method
- **Also called**: dynamic early exit
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Score (AES)](../concepts/accuracy-efficiency-score-aes.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [DEER](deer.md), [Early Exit](early-exit.md), [early-exit neural networks](../concepts/early-exit-neural-networks.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Hidden-State Probing](../concepts/hidden-state-probing.md), [HumanEval](../datasets/humaneval.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning](../../archive/papers/2026/arxiv-2607-28966/summary.md) — BLADE trains a lightweight hidden-state probe to decide, at sentence and self-doubt boundaries, whether a reasoning prefix already supports the correct answer, and stops generation when it does.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
