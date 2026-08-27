# dynamic self-correction

<!-- auto:begin -->

A model's capacity to detect that its own reasoning has drifted -- toward an unproductive path, or toward harmful/overly-cautious content -- and correct course mid-trace rather than continuing along the flawed trajectory. Sources apply the term in two different contexts: pruning-and-aggregating reasoning trees to correct exploration mid-search, and adversarial chain-of-thought training that teaches a model to recover from a 'snowball effect' where small reasoning deviations compound into harmful compliance or over-refusal.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

## Appears in

- [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](../../archive/papers/2025/title-57409f1a78ab75d8/summary.md) — Scales test-time compute by running and aggregating multiple pruned reasoning trees per problem, using sparse activation and consensus to balance accuracy against added compute.
- [AdvChain: Adversarial Chain-of-Thought Tuning for Robust Safety Alignment of Large Reasoning Models](../../archive/papers/2026/title-901ba3102e447b12/summary.md) — AdvChain trains large reasoning models with adversarial chain-of-thought examples (Temptation-Correction and Hesitation-Correction pairs) to teach dynamic self-correction, reducing a 'snowball effect' where small reasoning deviations compound into harmful compliance or excessive refusal.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
