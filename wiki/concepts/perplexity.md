# perplexity

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [attention analysis](../methods/attention-analysis.md), [catastrophic forgetting](catastrophic-forgetting.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [EOPD](../methods/eopd.md), [forward KL divergence](../methods/forward-kl-divergence.md), [generative rewriting](../methods/generative-rewriting.md), [GKD](../methods/gkd.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [JustRL-DeepSeek-1.5B](../models/justrl-deepseek-1-5b.md), [knowledge distillation](../methods/knowledge-distillation.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [on-policy distillation](../methods/on-policy-distillation.md), [overthinking](overthinking.md), [pass@k](pass-k.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](reasoning-redundancy.md), [reasoning skeleton](reasoning-skeleton.md), [restructuring level](restructuring-level.md), [reverse KL divergence](../methods/reverse-kl-divergence.md), [sampling efficiency](sampling-efficiency.md), [Skywork-OR1-Math-7B](../models/skywork-or1-math-7b.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](test-time-scaling.md), [token efficiency](token-efficiency.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.
- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
