# MedCalc-Bench

<!-- auto:begin -->

A clinical calculation benchmark spanning equation-based subtasks -- laboratory values, physical measures, dates, dosage -- and rule-based ones covering risk, severity and diagnosis, notable in this archive because it is the only dataset carrying both calculation traces and clinical safety intervals. That second property is what one source builds on, using the safety interval as a hard reward constraint that a continuous precision term then refines within, and that source states plainly it evaluated on this benchmark alone because nothing else supplies both. The other source uses it among the settings where preserving final-answer accuracy under KV cache compression is shown to coexist with destroying the reasoning that supports it. Neither describes its construction; the archive's interest in it is that safety intervals make an asymmetric error cost explicit in the data rather than leaving it to the metric.

- **Kind**: dataset
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [auditability](../concepts/auditability.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [component ablation](../methods/component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [KV cache compression](../methods/kv-cache-compression.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [o1-mini](../models/o1-mini.md), [outcome reward](../concepts/outcome-reward.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [PPO](../methods/ppo.md), [process reward](../concepts/process-reward.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-8B](../models/qwen3-8b.md), [REINFORCE](../methods/reinforce.md), [reward shaping](../methods/reward-shaping.md), [reward sparsity](../concepts/reward-sparsity.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.
- [MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning](../../archive/papers/2026/arxiv-2608-08623/summary.md) — Replaces the single tolerance threshold that RLVR uses to score floating-point answers with a hybrid reward pairing a hard clinical-safety constraint against a continuous precision-sensitive term, and adds a reward for stating the computational formula explicitly so an external verifier can check it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
