# HarmBench

<!-- auto:begin -->

A benchmark of harmful behaviour prompts used for red-teaming, appearing in both sources as the adversarial half of a safety evaluation. One includes it among the nine moderation benchmarks over which a guard model's weighted F1 is reported. The other uses it as a source of harmful requests in an automated attack that hijacks a reasoning model's own safety reasoning. The pairing is the archive's usual shape for a safety benchmark: the same prompts serve as the test a defence must pass and as the material an attack is built from.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [auditability](../concepts/auditability.md), [BeaverTails](beavertails.md), [Coconut](../methods/coconut.md), [curriculum learning](../concepts/curriculum-learning.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [jailbreak](../concepts/jailbreak.md), [latent reasoning](../concepts/latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.
- [AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1988/summary.md) — Automates the hijacking of a reasoning model's own safety reasoning by using a weaker, less-aligned model to simulate execution reasoning and refining attacks from patterns leaked in refusals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
