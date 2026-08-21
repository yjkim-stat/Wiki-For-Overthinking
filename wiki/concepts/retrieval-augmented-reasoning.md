# retrieval-augmented reasoning

<!-- auto:begin -->

Retrieval-augmented reasoning augments a reasoning model's chain of thought with material retrieved at inference time instead of relying only on parametric knowledge and fresh generation. The two sources use different retrieval targets: ThinkRetrieve retrieves a fully worked solved example per reasoning step, while Retrieval-of-Thought retrieves and assembles reusable steps from a stored graph of prior reasoning traces to shorten the newly generated one.

- **Kind**: concept
- **Also called**: Retrieval-Augmented Reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [SciQ](../datasets/sciq.md), [Self-Consistency](../methods/self-consistency.md), [sequential test-time scaling](sequential-test-time-scaling.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- [Retrieval-of-Thought: Efficient Reasoning via Reusing Thoughts](../../archive/papers/2026/title-2c8dfbd1f24680a2/summary.md) — Retrieval-of-Thought stores prior reasoning as a graph of composable thought steps and, at inference, retrieves and traverses it to assemble a problem-specific template that shortens the model's generated reasoning without retraining.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
