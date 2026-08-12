# generative rewriting

<!-- auto:begin -->

Producing a new, shorter rationale rather than deleting parts of the original — the second of the two compression families, spanning light paraphrase through step fusion to regeneration against a fixed template. Two things the archive establishes about it are worth separating from the method itself. Its effect inverts across domains: on mathematics accuracy falls monotonically as restructuring increases, making structure preservation the only reliable setting, while on general tasks aggressive rewriting matches or beats structure-preserving baselines by removing noise from a solution path that was never unique. And it is load-bearing where it is not advertised — in an attention-guided method presented as pruning, removing the generative refinement stage costs 17 to 21 accuracy points, because discrete deletion fragments the text and something has to restore coherence. One unresolved tension sits between those two findings: that method rewrites aggressively on mathematics and improves, where the domain result predicts it should degrade. A plausible reconciliation is that its rewriting is selected against the model's own likelihood of the correct answer while the other study's rewriter optimized nothing, but no archived experiment tests it.

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AMC23](../datasets/amc23.md), [attention analysis](attention-analysis.md), [chain-of-thought compression](chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-PRO](../datasets/mmlu-pro.md), [overthinking](../concepts/overthinking.md), [Qwen2.5](../models/qwen2-5.md), [reasoning distillation](reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [supervised finetuning](supervised-finetuning.md), [token efficiency](../concepts/token-efficiency.md), [TokenSkip](tokenskip.md)

## Appears in

- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
