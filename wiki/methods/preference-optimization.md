# Preference Optimization

<!-- auto:begin -->

Training a model on pairs of preferred-vs-dispreferred outputs to shift its behavior, without a separate reward model. In the archive it is repeatedly used to shorten reasoning: LCPO (small-scale preference optimization) cuts average reasoning length over 50% while maintaining accuracy; 'Don't Think Longer, Think Wisely' builds optimal-vs-suboptimal thinking-pattern pairs for the same purpose; a safety-focused variant intervenes at 'safety trigger' points within a reasoning chain instead of on length.

- **Kind**: method
- **Also called**: DPO, Preference Optimization, preference optimization
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Aha Moment](../concepts/aha-moment.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [MATH500](../datasets/math500.md), [O1-Pruner](o1-pruner.md), [Overthinking](../concepts/overthinking.md), [Process Supervision](../concepts/process-supervision.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [ThinkPrune](thinkprune.md), [veRL](verl.md)

## Appears in

- [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](../../archive/papers/2026/arxiv-2607-19962/summary.md) — EvoThink cuts overthinking in two separable stages: Self-Pruning Training deletes reasoning steps whose local conclusion repeats the previous step's and self-trains on the shortened traces, while Aha-Moment Preference Optimization builds from-wrong-to-right preference pairs out of the model's most diverse failed attempts and applies DPO to them.
- [Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization](../../archive/papers/2026/title-0694f0010d7ac51f/summary.md) — Proposes Length Controlled Preference Optimization (LCPO), a small-scale preference-tuning method that cuts large reasoning models' average output length by over 50% while preserving reasoning performance.
- [Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention](../../archive/papers/2026/title-3b1dfa6d6e5e2443/summary.md) — A process-supervision method that intervenes at identified 'safety trigger' points within a reasoning chain to redirect it away from harmful continuations, trained via preference optimization on corrected trajectories.
- [Don’t Think Longer, Think Wisely: Optimizing Thinking Dynamics for Large Reasoning Models](../../archive/papers/2025/title-edaac274df1e07a6/summary.md) — Segments reasoning traces into thinking patterns, prunes detrimental ones, and uses the resulting optimal-vs-suboptimal pairs for preference optimization to cut reasoning length while improving accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
