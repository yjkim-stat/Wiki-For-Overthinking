# Qwen3-4B-Thinking-2507

<!-- auto:begin -->

A small released reasoning checkpoint that emits an explicit thinking segment, used by both sources as the model whose traces are analysed rather than trained. One measures the entropy of its chain of thought and reports the two-phase structure it exhibits — a high-entropy exploration region shifting abruptly into low-entropy convergence — and uses it for the end-to-end latency comparison, at 419 seconds against 504 for vanilla decoding on AIME25, with CUSUM-weighted voting beating self-consistency at every sample count from 2 to 64 and a 3.33-point lead at 64. The other includes it among the models whose hidden-state trajectory geometry is scored. Its role here is as a model small enough to sample heavily from while still producing a long, structured thinking trace.

- **Kind**: model
- **Also called**: Qwen3-4B-Thinking
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [answer stabilization](../concepts/answer-stabilization.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [early exit](../methods/early-exit.md), [entropy trajectory](../concepts/entropy-trajectory.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-4o](gpt-4o.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [overthinking](../concepts/overthinking.md), [Qwen2.5-0.5B](qwen2-5-0-5b.md), [Qwen2.5-1.5B](qwen2-5-1-5b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-14B](qwen3-14b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [self-consistency](../methods/self-consistency.md)

## Appears in

- [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](../../archive/papers/2026/local-379c0b6966148b4a/summary.md) — Shows that CoT entropy follows a two-phase structure — a high-entropy exploration region that shifts abruptly into a low-entropy convergence region — and detects that shift online with the CUSUM change-point algorithm to drive early exit and trajectory-weighted voting.
- [Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability](../../archive/papers/2026/local-85a70e78b4a93190/summary.md) — TRACED scores a reasoning chain by the geometry of its hidden-state trajectory -- net displacement as progress and curvature as stability -- and uses the two as features for a Gaussian classifier that separates correct from incorrect chains without reading the text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
