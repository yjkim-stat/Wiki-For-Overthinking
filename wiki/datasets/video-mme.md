# Video-MME

<!-- auto:begin -->

A video-understanding benchmark whose long split averages about 41 minutes, and in this archive most useful for a negative result about it. The long-horizon agent work shows that performance here does not predict performance on multi-hour egocentric benchmarks: one prior agent achieves the best score of any agent system on this set at 67.3 percent and falls to 32.1 and 31.0 on two ultra-long sets, and another shows the same asymmetry. The authors read this as retrieval-heavy or strictly monotonic localisation pipelines working when evidence lies in a short well-structured search horizon and failing where repeated hypothesis revision is required. The perception-versus-reasoning latent work uses it among its evaluation sets. What the archive should carry is that long here means tens of minutes, that a benchmark family named for length can still be short relative to the regime a method claims, and that the two regimes order systems differently.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [attention pattern](../concepts/attention-pattern.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [error compounding](../concepts/error-compounding.md), [exploration](../concepts/exploration.md), [format compliance](../concepts/format-compliance.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [Kimi-K2.5](../models/kimi-k2-5.md), [knowledge distillation](../methods/knowledge-distillation.md), [latent reasoning](../concepts/latent-reasoning.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [monitorability](../concepts/monitorability.md), [outcome reward](../concepts/outcome-reward.md), [premature convergence](../concepts/premature-convergence.md), [process reward](../concepts/process-reward.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [Qwen3-VL](../models/qwen3-vl.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TempCompass](tempcompass.md), [test-time scaling](../concepts/test-time-scaling.md), [tool learning](../concepts/tool-learning.md), [tool orchestration](../concepts/tool-orchestration.md), [verifiable reward](../concepts/verifiable-reward.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering](../../archive/papers/2026/arxiv-2608-04124/summary.md) — Splits a video model's latent computation into perception latents that always ground the question in visual evidence and reasoning latents allocated only when the question needs inference, and shows that reasoning latents without rationale supervision are worse than no reasoning latents at all.
- [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](../../archive/papers/2026/arxiv-2608-07959/summary.md) — Replaces the monotonic zoom-in that tool-using video agents follow once they pick a region with a policy that self-checks each tool observation and can switch regions, and trains it with turn-level credit applied multiplicatively -- reweighting the trajectory advantage's magnitude while preserving its sign -- rather than additively.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
