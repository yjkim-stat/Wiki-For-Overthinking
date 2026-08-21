# contextual bandits

<!-- auto:begin -->

An online-learning framework for repeatedly choosing an action (e.g. which model to route a query to, or how much test-time compute to spend) based on context, using observed rewards to improve the choice over time. UniScale uses a bandit controller (LinUCB) to jointly decide model routing and test-time-compute allocation per query; the diffusion-model noise-trajectory-search paper casts its epsilon-greedy noise search the same way -- though that application is unrelated to LLM reasoning length.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-Time Scaling](test-time-scaling.md)

## Appears in

- [UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling](../../archive/papers/2026/title-3b024853a8e7324c/summary.md) — An online bandit controller that jointly decides which model to route a query to and how much test-time compute to spend, to optimize the quality-cost tradeoff.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
