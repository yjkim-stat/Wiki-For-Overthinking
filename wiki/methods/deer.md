# DEER

<!-- auto:begin -->

Dynamic Early Exit in Reasoning: monitor for reasoning transition points, induce a trial answer there, and stop if the answer's confidence exceeds a threshold. Its two monitor designs matter for this archive — one matches linguistic markers such as 'Wait', the other flags steps whose initial-token entropy exceeds 0.672, a threshold taken directly from the high-entropy-minority-tokens work on RLVR training. It is also the main baseline in the archive's CUSUM early-exit paper, which reports it lower in accuracy at comparable token savings.

- **Kind**: method
- **Also called**: DEER, DEER-PRo
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Dynasor](dynasor.md), [early exit](early-exit.md), [entropy trajectory](../concepts/entropy-trajectory.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ-32B](../models/qwq-32b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [token-level entropy](../concepts/token-level-entropy.md), [vLLM](vllm.md)

## Appears in

- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2025/local-a1d9fa1eb8899dfc/summary.md) — Detects the points where a reasoning model switches thought chains, interrupts to induce a trial answer, and stops generation when that answer's confidence is high enough — cutting chain-of-thought length substantially while raising accuracy, with no training.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
