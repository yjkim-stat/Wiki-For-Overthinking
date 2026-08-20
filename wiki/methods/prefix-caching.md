# prefix caching

<!-- auto:begin -->

Reusing the stored attention state of a shared prompt prefix across requests so that a continuation does not re-prefill what it has in common with its predecessor. Both sources treat it as the resource that decides how much reasoning fits in a budget rather than as an implementation detail. The beam-search source exploits it deliberately, branching from high-scoring prefixes so that new exploration reuses cached state and the compute freed by pruning weak traces is immediately re-spent. The serving source measures what happens when placement optimises reuse without controlling how many sessions compete for the cache: admitting new sessions expands the resident working set, evicts reusable continuations, turns later turns into cold prefill and lengthens the queue, a positive feedback loop that drives the hit rate from 92.4 percent to 4.5 at a concurrency ceiling that admission-controlled policies tolerate. It also notes that periodic weight synchronisation in RL training resets the caches every iteration, which is why an end-to-end hit rate (96.2 percent) sits below the rollout-only one (97.8).

- **Kind**: method
- **Also called**: KV cache reuse
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [answer aggregation](answer-aggregation.md), [beam search](beam-search.md), [compute allocation](../concepts/compute-allocation.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT](../datasets/hmmt.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [long-horizon agency](../concepts/long-horizon-agency.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [process reward model](process-reward-model.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [trajectory diversity](../concepts/trajectory-diversity.md), [vLLM](vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](../../archive/papers/2026/arxiv-2608-11152/summary.md) — A routing-layer admission policy for RL post-training that treats admitting a rollout session as a commitment of KV-cache capacity, allocates protected capacity per workload class by footprint and observed residency time, and leaves the workload mixture itself under the trainer's control.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
