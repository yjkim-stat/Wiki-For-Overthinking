# perplexity

<!-- auto:begin -->

The exponentiated average negative log-likelihood a model assigns to a sequence, used in both sources as a probe of whose distribution a text belongs to rather than as a quality measure. The distillation study computes the perplexity of trajectories from a base, distilled and teacher model under both the base and teacher distributions, and reads the cross-tabulation: the distilled model's trajectories are more likely under the teacher than the base model's are, but also more likely under the base distribution than either the base's own or the teacher's -- so probability mass moved toward paths the base already supported rather than toward the teacher's unfamiliar ones. The compression study uses it as a validation rather than a result: pruning the highest-salience reasoning steps spikes the final answer's perplexity, pruning the lowest raises it marginally, and random pruning falls between, which is what licenses treating the salience ranking as meaningful. Both uses share a structure worth noting -- perplexity is informative when computed under more than one distribution, or on more than one ablation, and says little as a single number.

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [attention analysis](attention-analysis.md), [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [chain-of-thought compression](chain-of-thought-compression.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [EOPD](eopd.md), [forward KL divergence](forward-kl-divergence.md), [generative rewriting](generative-rewriting.md), [GKD](gkd.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [JustRL-DeepSeek-1.5B](../models/justrl-deepseek-1-5b.md), [knowledge distillation](knowledge-distillation.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [on-policy distillation](on-policy-distillation.md), [overthinking](../concepts/overthinking.md), [pass@k](../concepts/pass-k.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [reasoning distillation](reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [reverse KL divergence](reverse-kl-divergence.md), [sampling efficiency](../concepts/sampling-efficiency.md), [Skywork-OR1-Math-7B](../models/skywork-or1-math-7b.md), [supervised fine-tuning](supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [token efficiency](../concepts/token-efficiency.md), [TokenSkip](tokenskip.md)

## Appears in

- [Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](../../archive/papers/2026/arxiv-2608-11829/summary.md) — Evaluates on-policy distillation across sampling budgets from 1 to 1024 and finds it consistently improves accuracy at small budgets while losing to the untrained base model at large ones, so what it transfers is sampling efficiency rather than capability -- and off-policy distillation, tested the same way, does expand the boundary.
- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
