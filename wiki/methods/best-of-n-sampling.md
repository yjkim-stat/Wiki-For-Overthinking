# best-of-N sampling

<!-- auto:begin -->

A test-time-compute strategy that samples N candidate solutions independently and selects one (by a verifier, reward model, or majority vote), trading inference compute for accuracy. The archive's 7 sources study when this actually pays off: its accuracy is bounded by verifier ROC-curve geometry and generally worse than Rejection Sampling at a fixed compute budget (ROC-n-reroll); it has provably worse sample complexity than self-consistency for some tasks (Θ(1/Δ) vs Θ(1/Δ²)); standard best-of-n is proven suboptimal under a mixture-of-reference-policy model, with reward-filtered sequential inference beating it under theoretical guarantees; how often the verifier is called (verification granularity) can itself be tuned to trade accuracy against cost; and its cost can be cut by truncating unpromising candidates early via internal-state sampling consistency (ST-BoN) or by speculative decoding, rather than paying for all N candidates in full.

- **Kind**: method
- **Also called**: Best-of-N, Best-of-N sampling, BoN, best-of-n sampling
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 7

**Related**: [Best-of-N](best-of-n.md), [Best-of-N (BoN) sampling](best-of-n-bon-sampling.md), [GSM8K](../datasets/gsm8k.md), [majority voting](majority-voting.md), [MATH-500](../datasets/math-500.md), [overthinking](../concepts/overthinking.md), [rejection sampling](rejection-sampling.md), [self-consistency](self-consistency.md), [speculative decoding](speculative-decoding.md), [test-time compute](../concepts/test-time-compute.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](../../archive/papers/2026/title-1d5e1f4d59da5916/summary.md) — Benchmarks model-based, training-based and N-gram-based speculative decoding methods as ways to accelerate token generation during LLM test-time scaling (Best-of-N, iterative reasoning), finding N-gram methods best exploit repetitive patterns.
- [Sample Complexity and Representation Ability of Test-time Scaling Paradigms](../../archive/papers/2026/title-27bc5c2aff7ebdab/summary.md) — A theoretical paper deriving sample-complexity bounds for self-consistency versus best-of-n, and an expressiveness result showing self-correction lets a Transformer simulate online learning over multiple tasks at test time.
- [Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](../../archive/papers/2025/title-5d66fe9a10241ce8/summary.md) — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.
- [ROC-n-reroll: How verifier imperfection affects test-time scaling](../../archive/papers/2026/title-6b3727a0a0ac9a23/summary.md) — Proves that verifier ROC-curve geometry determines the accuracy of Best-of-N and Rejection Sampling under a fixed compute budget, and shows RS beats BoN at fixed compute while both converge in the infinite-compute limit.
- [Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling](../../archive/papers/2025/title-7409f584637723da/summary.md) — Studies how often a verifier should be called during LLM generation, proposing a search algorithm that tunes verification granularity to trade off accuracy and compute in test-time scaling.
- [Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding](../../archive/papers/2025/title-9dcfd1b98bd7008e/summary.md) — ST-BoN cuts the cost of Best-of-N test-time scaling by using early sampling consistency in internal states to truncate unpromising candidates before they finish generating, without a reward model.
- [On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference](../../archive/papers/2026/title-cd5c62ac6be53cbc/summary.md) — Proves standard best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
