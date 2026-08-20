# XSTest

<!-- auto:begin -->

A safety test set built around benign prompts that superficially resemble harmful ones, so that it measures over-refusal rather than compliance. Both sources use it in that role. The latent-guard work includes it among ten evaluation sets for a safety classifier whose textual rationales are compressed into continuous latent states, where the point of the set is to check that efficiency gains do not come from a guard that simply refuses more. The steering-safety work is the more direct use: it evaluates whether a steering vector's sanitised form increases false refusals on benign prompts, with the tolerance on that constraint set to exactly zero -- so XSTest-style prompts define one of the two constraints the method's optimisation must satisfy rather than a metric reported afterwards. Neither source describes the set's construction; in this archive it functions as the standing check that a safety intervention has not simply moved the threshold.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation steering](../methods/activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [auditability](../concepts/auditability.md), [BeaverTails](beavertails.md), [Coconut](../methods/coconut.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [curriculum learning](../concepts/curriculum-learning.md), [HarmBench](harmbench.md), [jailbreak](../concepts/jailbreak.md), [KL divergence](../concepts/kl-divergence.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.5-27B](../models/qwen3-5-27b.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [steering vector](../methods/steering-vector.md), [superposition](../concepts/superposition.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [Safety Cost of Steering Vectors Is Separable and Reducible](../../archive/papers/2026/arxiv-2608-08383/summary.md) — Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
