# BeaverTails

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [auditability](../concepts/auditability.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Coconut](../methods/coconut.md), [curriculum learning](../concepts/curriculum-learning.md), [Gemma-4-12B](../models/gemma-4-12b.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GSM8K](gsm8k.md), [HarmBench](harmbench.md), [KL regularization](../methods/kl-regularization.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](../../archive/papers/2026/arxiv-2608-03838/summary.md) — Compresses a safety guard's textual rationales into continuous latent states by a staged curriculum, cutting 268 reasoning tokens to 1.60 and latency 8.9-fold, and adds an on-demand decoder that reconstructs a human-readable audit artifact — whose own ablation shows the artifact is anchored far more by the source text than by the latent states it is supposed to inspect.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
