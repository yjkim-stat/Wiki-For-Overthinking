# Skywork-OR1-Math-7B

<!-- auto:begin -->

A 7B reinforcement-learning-trained mathematics model, used in this archive as the strong-teacher case in a distillation study -- the setting where the teacher leads the student across benchmarks and budgets, as against a weaker teacher that leads only at small sampling budgets. That contrast is what lets the study conclude its finding does not depend on teacher strength: the student's capability boundary fails to extend past its base model either way. It also appears among the reinforcement-learning-finetuned models that lose most of their reported accuracy when a benchmark's constants are replaced by sampled variables and consistency across instantiations is required. Neither source describes its training.

- **Kind**: model
- **Also called**: Skywork-OR1-Math-7B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap resampling](../methods/bootstrap-resampling.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DAPO-Qwen-32B](dapo-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [EOPD](../methods/eopd.md), [forward KL divergence](../methods/forward-kl-divergence.md), [GKD](../methods/gkd.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [JustRL-DeepSeek-1.5B](justrl-deepseek-1-5b.md), [knowledge distillation](../methods/knowledge-distillation.md), [MATH500](../datasets/math500.md), [memorization](../concepts/memorization.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy distillation](../methods/on-policy-distillation.md), [pass@k](../concepts/pass-k.md), [perplexity](../methods/perplexity.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-1.7B-Base](qwen3-1-7b-base.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [reverse KL divergence](../methods/reverse-kl-divergence.md), [RLVR](../methods/rlvr.md), [sampling efficiency](../concepts/sampling-efficiency.md), [test-time scaling](../concepts/test-time-scaling.md), [vLLM](../methods/vllm.md)

## Appears in

- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](../../archive/papers/2026/local-d62cc27b0209da49/summary.md) — Converts AMC23 and AIME24/25 into symbolic templates whose constants are replaced by sampled variables, requires a model to solve several instantiations of each problem, and finds RL-finetuned models lose most of their reported accuracy under that consistency requirement.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
