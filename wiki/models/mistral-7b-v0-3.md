# Mistral-7B-v0.3

<!-- auto:begin -->

A 7B open-weight model, used by both sources as the second backbone that decides whether a result is about a method or about one model. In one it is where the preference-mining gain is largest — 12.28% to 32.92% on GSM8K, against a smaller margin on the other backbone — so the method's benefit is inversely related to how strong the base model already is. In the other it is the replication: the running-state condition reaches 0.93 and 0.94 edited-state agreement with selectivity around 0.85, confirming a scratchpad-register finding first established elsewhere. Both use it for the same purpose, which is to keep a claim from resting on a single lineage.

- **Kind**: model
- **Also called**: Mistral-7B, Mistral-7B-v0.3
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DPO](../methods/dpo.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [linear probe](../methods/linear-probe.md), [Llama-3-8B](llama-3-8b.md), [preference optimization](../methods/preference-optimization.md), [process supervision](../concepts/process-supervision.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [Qwen3-8B](qwen3-8b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [self-consistency](../methods/self-consistency.md), [state tracking](../concepts/state-tracking.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) — Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](../../archive/papers/2026/local-54a1c25fa51cd59a/summary.md) — Edits the internal representation of a written scratchpad state while holding the printed text fixed, and asks whether the next step follows the transition rule applied to the edited value — turning 'does the model use its scratchpad?' into a causal test with a single correct answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
