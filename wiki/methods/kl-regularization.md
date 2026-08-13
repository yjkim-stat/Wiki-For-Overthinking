# KL regularization

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [curriculum learning](../concepts/curriculum-learning.md), [Gemma-4-12B](../models/gemma-4-12b.md), [GPT-4o](../models/gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [linear probe](linear-probe.md), [LLM-as-a-judge](llm-as-a-judge.md), [monitorability](../concepts/monitorability.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [RLVR](rlvr.md), [supervised fine-tuning](supervised-fine-tuning.md), [training dynamics](../concepts/training-dynamics.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
