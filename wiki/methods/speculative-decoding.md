# speculative decoding

<!-- auto:begin -->

An inference-acceleration technique where a small draft model proposes tokens that a larger target model verifies in parallel, cutting wall-clock generation time without changing what is generated. In the archive it is applied to speed up reasoning-model inference: SpecExit extends the draft model to also predict an early-exit signal, cutting generation length up to 66% at 2.5x speedup; a benchmarking paper compares model-based, training-based and N-gram-based variants as accelerators for test-time scaling; the recurrent-depth latent-reasoning paper discusses it as a related but distinct way to trade compute for quality.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Best-of-N sampling](best-of-n-sampling.md), [Early Exit](early-exit.md), [Latent reasoning](../concepts/latent-reasoning.md), [Recurrent Depth](../concepts/recurrent-depth.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [SpecExit: Accelerating Large Reasoning Model via Speculative Exit](../../archive/papers/2026/title-1bb8d328d6b8e7ac/summary.md) — Uses a speculative-decoding-style draft model to predict both next tokens and an early-exit signal, letting a large reasoning model stop generating once its own internal representations indicate reasoning is done.
- [Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](../../archive/papers/2026/title-1d5e1f4d59da5916/summary.md) — Benchmarks model-based, training-based and N-gram-based speculative decoding methods as ways to accelerate token generation during LLM test-time scaling (Best-of-N, iterative reasoning), finding N-gram methods best exploit repetitive patterns.
- [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](../../archive/papers/2025/title-f75fffe554037a34/summary.md) — Introduces a recurrent-depth architecture that scales test-time compute by iterating a latent reasoning block to arbitrary depth instead of generating more chain-of-thought tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
