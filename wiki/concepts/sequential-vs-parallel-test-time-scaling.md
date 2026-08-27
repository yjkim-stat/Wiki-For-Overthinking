# sequential vs. parallel test-time scaling

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [BrowseComp](../datasets/browsecomp.md), [Budget Forcing](../methods/budget-forcing.md), [GAIA](../datasets/gaia.md), [MATH500](../datasets/math500.md), [QwQ](../models/qwq.md)

## Appears in

- [Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-232/summary.md) — Systematically shows that o1-like models (QwQ, R1, LIMO, and R1-Distill variants) do not actually possess consistent sequential test-time scaling: correct solutions are on average shorter than incorrect ones on the same questions, accuracy does not consistently improve (and sometimes inverse-scales) with solution length, and this traces to a failure of self-revision (models rarely fix wrong answers and sometimes break correct ones) -- leading to Shortest Majority Vote, a parallel-scaling method weighting majority-vote clusters by inverse-log solution length, which significantly outperforms both plain Majority Vote and a shortest-solution-only heuristic.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
