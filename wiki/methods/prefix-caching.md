# prefix caching

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [answer aggregation](answer-aggregation.md), [beam search](beam-search.md), [compute allocation](../concepts/compute-allocation.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT](../datasets/hmmt.md), [KV cache](../concepts/kv-cache.md), [linear probe](linear-probe.md), [long-horizon agency](../concepts/long-horizon-agency.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [process reward model](../concepts/process-reward-model.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [trajectory diversity](../concepts/trajectory-diversity.md), [vLLM](vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](../../archive/papers/2026/arxiv-2608-11152/summary.md) — A routing-layer admission policy for RL post-training that treats admitting a rollout session as a commitment of KV-cache capacity, allocates protected capacity per workload class by footprint and observed residency time, and leaves the workload mixture itself under the trainer's control.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
