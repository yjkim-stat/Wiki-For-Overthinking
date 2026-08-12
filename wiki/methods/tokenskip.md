# TokenSkip

<!-- auto:begin -->

A controllable compression method that scores token-level importance and drops low-utility tokens from a reasoning trace, then fine-tunes the model on the shortened traces so it learns to skip them itself. It appears in this archive as a baseline rather than as a subject, and the comparisons are not favourable — two sources report it yielding limited efficiency gains relative to the accuracy it costs, in one case being outperformed at both model scales tested. Its importance scoring derives from a learned prompt-compression model, which places it on the same side of the archive's granularity finding as other token-level methods: at that granularity the choice of criterion matters a great deal, and only symbol-aware scoring reliably avoids deleting the operators and numbers a derivation depends on.

- **Kind**: method
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [attention analysis](attention-analysis.md), [chain-of-thought compression](chain-of-thought-compression.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO](dpo.md), [generative rewriting](generative-rewriting.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [length penalty](length-penalty.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [reasoning distillation](reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [restructuring level](../concepts/restructuring-level.md), [self-correction](../concepts/self-correction.md), [supervised finetuning](supervised-finetuning.md), [token efficiency](../concepts/token-efficiency.md)

## Appears in

- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
