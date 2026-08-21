# Recurrent Depth

<!-- auto:begin -->

Buying extra test-time computation by iterating a block of layers in latent space instead of emitting more chain-of-thought tokens, so the depth of the unrolling rather than the length of the output is the compute knob. The originating paper trains a 3.5B-parameter proof of concept on 800B tokens, unrolls a recurrent block to arbitrary depth at inference, needs no chain-of-thought training data, and gets per-token adaptive compute, KV-cache sharing and speculative decoding out of the same structure; the archived record reports no benchmark scores for it. Penelope keeps the idea but localises it, recurring only an eight-anchor memory through a five-layer interval of a 16-layer Llama-3.2-1B so that one more refinement costs r layers rather than L - 99.82 ms against Coconut's 188.15 ms on Deep ListOps at accuracies within one standard deviation. What the archive does not show is that the extra depth is doing reasoning: Penelope's K sweep stays inside a 0.50-point band, a K=0 boundary-only pass is within 0.69 EM point of the selected depth, and full-decoder recurrence gains 0.27 point for 2.51x the sequential decoder-layer applications.

- **Kind**: concept
- **Also called**: Recurrent Depth, recurrent depth
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [Budget Forcing](../methods/budget-forcing.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [Latent reasoning](latent-reasoning.md), [speculative decoding](../methods/speculative-decoding.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](../../archive/papers/2025/title-f75fffe554037a34/summary.md) — Introduces a recurrent-depth architecture that scales test-time compute by iterating a latent reasoning block to arbitrary depth instead of generating more chain-of-thought tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
