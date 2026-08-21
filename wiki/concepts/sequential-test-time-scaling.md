# sequential test-time scaling

<!-- auto:begin -->

Scaling test-time compute by extending a single reasoning trace further (more sequential tokens), as opposed to parallel scaling (more independent samples). ThinkRetrieve augments each step of such a sequential trace with a retrieved worked example; 'Wait, Do We Need to Wait?' stress-tests the standard sequential-scaling technique (budget forcing via a 'Wait' keyword) across model families and finds it does not generalize cleanly.

- **Kind**: concept
- **Also called**: budget forcing
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [Budget Forcing](../methods/budget-forcing.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [retrieval-augmented reasoning](retrieval-augmented-reasoning.md), [SciQ](../datasets/sciq.md), [Test-Time Compute Scaling](test-time-compute-scaling.md)

## Appears in

- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.
- [Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling](../../archive/papers/2026/title-7071aa99216bb67f/summary.md) — Revisits budget forcing -- forcing a reasoning model to keep thinking or to stop via a keyword like 'Wait' -- and empirically tests how well it generalizes across model families, non-reasoning models, and alternative keywords.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
