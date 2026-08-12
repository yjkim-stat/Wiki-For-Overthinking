# process reward model

<!-- auto:begin -->

A reward model that scores a reasoning trajectory step by step rather than judging only the final response, giving denser and better-localized signal for both RL training and inference-time selection. The sources converge on its cost being the binding problem — training one normally needs a label at every step, obtained either by hand or by sampling look-ahead rollouts from each prefix, which one source measures at 38.8 times the FLOPs of training an outcome model. That source then shows the cost is avoidable: parameterizing the outcome reward as a log-likelihood ratio between policy and reference makes the running sum of per-token ratios an exact expectation of the outcome reward at each step, so a PRM falls out of ORM training for free. Downstream sources treat a pretrained PRM as infrastructure — a local step validator supplying online pruning signals and cross-trajectory selection — and report the same failure mode: PRM quality is the limiting factor on hard problems, where it can be overconfident or prefer locally correct but globally wrong paths.

- **Kind**: method
- **Also called**: PRM, process reward models
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME24](../datasets/aime24.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [chain of thought](chain-of-thought.md), [credit assignment](../concepts/credit-assignment.md), [DPO](dpo.md), [early exit](early-exit.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [KV cache compression](../concepts/kv-cache-compression.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [majority voting](majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [outcome reward](../concepts/outcome-reward.md), [overthinking](../concepts/overthinking.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [RLVR](rlvr.md), [self-reflection](self-reflection.md), [test-time compute](../concepts/test-time-compute.md), [token efficiency](../concepts/token-efficiency.md), [verification](../concepts/verification.md)

## Appears in

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../archive/papers/2024/arxiv-2408-03314/summary.md) — Studies how far a fixed model improves when given more inference compute, and shows that allocating that compute adaptively per prompt by difficulty beats a uniform best-of-N budget by more than 4x.
- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — Couples KV-cache compression and generation-length control under a single process-reward signal, compressing harder at high-reward reasoning steps and stopping early when confidence is high.
- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/local-80ef8b5ce7217f7c/summary.md) — Replaces uniform test-time compute allocation with a training-free agent that picks reasoning tools, a search strategy and an exploration parameter per problem, using a process reward model both to prune within a trajectory and to select across iterations.
- [Free Process Rewards without Process Labels](../../archive/papers/2024/local-b1536fcbe72cb268/summary.md) — Proves that parameterizing an outcome reward as the log-likelihood ratio between a policy and a reference model makes the per-step Q value fall out of the same model for free, so a process reward model can be obtained by training an outcome reward model on response-level labels alone.
- [Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning](../../archive/papers/2025/local-c45962c819666804/summary.md) — Formalizes 'spend test-time compute well' as a meta-reinforcement-learning problem — treating one long output stream as a sequence of episodes and scoring it by cumulative regret over tokens — and trains against a dense progress bonus that outcome-only reward cannot express.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
