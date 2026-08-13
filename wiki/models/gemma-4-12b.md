# Gemma-4-12B

<!-- auto:begin -->

A 12B instruction-tuned model, present in both sources as the largest member of a small sweep. One installs triggered backdoors in it and reports its full monitoring table — the decoupled configurations leaving CoT-only judges at 0.49-0.52 AUC while the answer-inclusive scope reaches 0.98-1.00 — so it is the model the poisoning result is shown on in detail. The other includes it among the cells of a calibration study alongside a frontier arm. Neither studies the checkpoint itself.

- **Kind**: model
- **Also called**: Gemma 4 12B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [calibration](../methods/calibration.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [construct validity](../concepts/construct-validity.md), [curriculum learning](../concepts/curriculum-learning.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [GSM8K](../datasets/gsm8k.md), [inverse scaling](../concepts/inverse-scaling.md), [KL regularization](../methods/kl-regularization.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [The Calibration Floor: Format Repair Can Masquerade as Self-Correction at Small-to-Mid Scale](../../archive/papers/2026/arxiv-2608-04355/summary.md) — Decomposes measured self-correction gains into a content margin and format-recovery margins, and shows causally that most of what the field has reported as self-correction is answer-parseability repair.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
