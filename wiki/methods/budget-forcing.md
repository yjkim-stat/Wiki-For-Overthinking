# budget forcing

<!-- auto:begin -->

Controlling a reasoning model's chain-of-thought length by inserting a keyword at inference time -- most commonly 'Wait' to force it to keep thinking past what it would have generated on its own, or a stop signal to cut it short. 'Wait, Do We Need to Wait?' stress-tests this technique across model families, non-reasoning models and alternative keywords; 'When More Thinking Hurts' and the deep-search asymmetric-verification paper both study its diminishing, and eventually negative, returns as forced length grows.

- **Kind**: method
- **Also called**: sequential test-time scaling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [GAIA](../datasets/gaia.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [MATH-500](../datasets/math-500.md), [overthinking](../concepts/overthinking.md), [sequential test-time scaling](../concepts/sequential-test-time-scaling.md)

## Appears in

- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](../../archive/papers/2026/local-32a56cfa1105c39e/summary.md) — The paper shows that extended chain-of-thought reasoning in LLMs has diminishing and eventually negative marginal utility, quantifies this 'overthinking' via answer-flip tracking, and proposes cost-aware, indicator-based early-stopping strategies that cut compute substantially with little accuracy loss.
- [Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling](../../archive/papers/2026/title-7071aa99216bb67f/summary.md) — Revisits budget forcing -- forcing a reasoning model to keep thinking or to stop via a keyword like 'Wait' -- and empirically tests how well it generalizes across model families, non-reasoning models, and alternative keywords.
- [Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification](../../archive/papers/2026/title-711c479b500244c5/summary.md) — Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
