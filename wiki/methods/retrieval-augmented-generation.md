# retrieval-augmented generation

<!-- auto:begin -->

Conditioning generation on passages retrieved at inference time so the answer is grounded in an external, updatable corpus rather than in weights. It is peripheral to this archive and enters through cost rather than through quality: the one source that measures it in detail treats retrieved context as a length problem on the same axis as a reasoning trace -- more passages mean more prefill, more KV cache, more energy -- and shows that compressing that context pays only inside a bounded rate window, because the compressor competes for the same device.

- **Kind**: method
- **Also called**: RAG
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Overthinking](../concepts/overthinking.md), [retrieval-augmented reasoning](../concepts/retrieval-augmented-reasoning.md), [Self-Consistency](self-consistency.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [Retrieval-of-Thought: Efficient Reasoning via Reusing Thoughts](../../archive/papers/2026/title-2c8dfbd1f24680a2/summary.md) — Retrieval-of-Thought stores prior reasoning as a graph of composable thought steps and, at inference, retrieves and traverses it to assemble a problem-specific template that shortens the model's generated reasoning without retraining.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
