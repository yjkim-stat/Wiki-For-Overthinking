# beam search

<!-- auto:begin -->

Keeping a fixed number of highest-scoring partial continuations at each step rather than committing to one. In the archive it appears only as a baseline that other test-time methods are measured against, never as the proposed method. One source reports its verifier-free refine-then-vote framework beating beam search along with greedy decoding, majority voting, best-of-N and lookahead decoding; the other includes a search strategy as one of the per-problem choices an allocation agent makes, which treats beam search as one option among several rather than a default.

- **Kind**: method
- **Also called**: beam decoding
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [answer stabilization](../concepts/answer-stabilization.md), [best-of-n](best-of-n.md), [chain of thought](chain-of-thought.md), [greedy decoding](greedy-decoding.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [process reward model](process-reward-model.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [self-reflection](self-reflection.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](test-time-scaling.md), [verification](../concepts/verification.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) — Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
