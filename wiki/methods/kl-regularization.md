# KL regularization

<!-- auto:begin -->

Penalizing divergence from a reference policy during training, and in both sources a partial measure whose limits are the point rather than a solution. One tests it as the only defence it tries against a poisoning attack and reports attack success falling from 94.0% to 79.3% — described precisely as a meaningful cost to the attacker and far from a defence, with the wider question left open. The other addresses the neighbouring problem of RLVR eroding foundational skills and reaches for experience replay with online-adaptive weights rather than a divergence penalty. Read together they mark the same boundary from two sides: anchoring to the base distribution slows an unwanted change without preventing it, and neither source treats it as sufficient on its own.

- **Kind**: method
- **Also called**: KL divergence regularization, KL penalty
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [advantage estimation](../concepts/advantage-estimation.md), [BeaverTails](../datasets/beavertails.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [causal intervention](causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [credit assignment](../concepts/credit-assignment.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3](../models/deepseek-v3.md), [GEMBA-MQM](gemba-mqm.md), [Gemini-2.0-flash](../models/gemini-2-0-flash.md), [Gemma-4-12B](../models/gemma-4-12b.md), [GPT-4o](../models/gpt-4o.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5](../models/gpt-5.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [linear probe](linear-probe.md), [LLM-as-a-judge](llm-as-a-judge.md), [long chain-of-thought distillation](long-chain-of-thought-distillation.md), [monitorability](../concepts/monitorability.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reasoning drift](../concepts/reasoning-drift.md), [reward shaping](../concepts/reward-shaping.md), [RLVR](rlvr.md), [supervised fine-tuning](supervised-fine-tuning.md), [teacher forcing](teacher-forcing.md), [training dynamics](../concepts/training-dynamics.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2608-03077/summary.md) — Scores each reasoning step of a translation by how much appending it raises a frozen reference model's teacher-forced likelihood of the gold translation, and adds that as a dense per-step reward on top of sequence-level quality — after first establishing that explicit reasoning helps long and hard inputs while drifting on terminology and style.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
