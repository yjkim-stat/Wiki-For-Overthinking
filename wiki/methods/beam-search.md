# beam search

<!-- auto:begin -->

Keeping a fixed number of highest-scoring partial continuations at each step rather than committing to one. In the archive it appears only as a baseline that other test-time methods are measured against, never as the proposed method. One source reports its verifier-free refine-then-vote framework beating beam search along with greedy decoding, majority voting, best-of-N and lookahead decoding; the other includes a search strategy as one of the per-problem choices an allocation agent makes, which treats beam search as one option among several rather than a default.

- **Kind**: method
- **Also called**: beam decoding
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC](../datasets/amc.md), [answer stabilization](../concepts/answer-stabilization.md), [BBH](../datasets/bbh.md), [best-of-n](best-of-n.md), [Brumo](../datasets/brumo.md), [budget forcing](budget-forcing.md), [chain of thought](chain-of-thought.md), [CMIMC](../datasets/cmimc.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1](../models/deepseek-r1.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [greedy decoding](greedy-decoding.md), [HMMT](../datasets/hmmt.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [majority voting](majority-voting.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [OlympiadBench](../datasets/olympiadbench.md), [pass@k](pass-k.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [process reward model](process-reward-model.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](self-consistency.md), [self-correction](../concepts/self-correction.md), [self-reflection](self-reflection.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](test-time-scaling.md), [Tree of Thoughts](tree-of-thoughts.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [verification](../concepts/verification.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.
- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) — Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
