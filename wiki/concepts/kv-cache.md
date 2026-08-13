# KV cache

<!-- auto:begin -->

The stored keys and values of previous tokens that let autoregressive decoding avoid recomputation, and in both sources a thing with consequences beyond speed. One treats it as the binding constraint on test-time reasoning: long traces saturate cache capacity, which caps how many trajectories can run at once, and branching from a shared prefix is cheap precisely because the child inherits the parent's cache. The other treats it as the object of an intervention, editing the cached representation of a written scratchpad while holding the printed text fixed to ask whether the next step follows the edited value or the visible one. So it is both the resource that bounds allocation and the place where a trace's state actually lives.

- **Kind**: concept
- **Also called**: KV cache, key-value cache
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [answer aggregation](../methods/answer-aggregation.md), [beam search](../methods/beam-search.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [compute allocation](compute-allocation.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT](../datasets/hmmt.md), [KV cache compression](../methods/kv-cache-compression.md), [linear probe](../methods/linear-probe.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [process reward model](../methods/process-reward-model.md), [process supervision](process-supervision.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [residual stream](residual-stream.md), [self-consistency](../methods/self-consistency.md), [state tracking](state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](test-time-compute.md), [trajectory diversity](trajectory-diversity.md), [vLLM](../methods/vllm.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Reformulates test-time reasoning as compute allocation over partial trajectories under a hardware budget, and runs a zero-sum beam search over reasoning steps that prunes weak traces and immediately re-spends the freed capacity by branching from high-scoring prefixes.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
