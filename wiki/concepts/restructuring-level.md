# restructuring level

<!-- auto:begin -->

How far a compression method is allowed to reorganize a reasoning trace, treated by one archived source as an independent design axis rather than a side effect of how much is removed. It is instantiated as a four-point spectrum: preserving the verbatim logical sequence and cutting only surface words, editing at step level, fusing steps into new statements, and discarding the original structure for a predefined template. Isolating it from compression ratio is what makes the central finding visible — the effect inverts across domains. On mathematics accuracy degrades monotonically as restructuring increases, because strict logical dependencies mean an error introduced by disturbing step boundaries is amplified downstream, leaving structure preservation the only safe choice. On general tasks the monotonicity breaks: aggressive rewriting matches or exceeds structure-preserving baselines, since those tasks accept many valid rationales and do not hinge on a specific intermediate state, so restructuring acts as a denoiser. The most aggressive level is also the highest-variance one, collapsing on logic-heavy problems while remaining competitive elsewhere.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [attention analysis](../methods/attention-analysis.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [generative rewriting](../methods/generative-rewriting.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [overthinking](overthinking.md), [perplexity](../methods/perplexity.md), [Qwen2.5](../models/qwen2-5.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](reasoning-redundancy.md), [reasoning skeleton](reasoning-skeleton.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [token efficiency](token-efficiency.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
