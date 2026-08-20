# KV cache

<!-- auto:begin -->

The stored attention state that lets a transformer continue a sequence without recomputing it, and across 3 sources the resource that decides how much reasoning fits in a budget. Its three roles here. As a capacity constraint in serving, where admitting a rollout session is a commitment of it rather than a placement decision, and where placement-only routing collapses to a 4.5 percent reuse rate under a concurrency ceiling admission control tolerates. As the substrate a beam search over reasoning steps exploits, branching from cached prefixes so freed capacity is immediately re-spent. And as the site of a faithfulness failure: compressing it preserves final-answer accuracy while destroying the reasoning that supports it, with accuracy and chain validity correlating at -0.95 across compressors on one benchmark. One source also uses it as an interpretability handle, editing the cached representation of a written scratchpad while holding the printed text fixed.

- **Kind**: concept
- **Also called**: KV cache, key-value cache
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [answer aggregation](../methods/answer-aggregation.md), [auditability](auditability.md), [beam search](../methods/beam-search.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [compute allocation](compute-allocation.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT](../datasets/hmmt.md), [linear probe](../methods/linear-probe.md), [long-horizon agency](long-horizon-agency.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [prefix caching](../methods/prefix-caching.md), [process reward model](process-reward-model.md), [process supervision](process-supervision.md), [Qwen2.5-Coder-7B](../models/qwen2-5-coder-7b.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [representation editing](../methods/representation-editing.md), [residual stream](residual-stream.md), [selectivity control](../methods/selectivity-control.md), [self-consistency](../methods/self-consistency.md), [state tracking](state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [trajectory diversity](trajectory-diversity.md), [vLLM](../methods/vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](../../archive/papers/2026/arxiv-2608-11152/summary.md) — A routing-layer admission policy for RL post-training that treats admitting a rollout session as a commitment of KV-cache capacity, allocates protected capacity per workload class by footprint and observed residency time, and leaves the workload mixture itself under the trainer's control.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
