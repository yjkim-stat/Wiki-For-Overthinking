# reasoning skeleton

<!-- auto:begin -->

The subset of a reasoning trace that the answer actually depends on, as opposed to the elaboration around it. The term earns its place in this archive because independent methods keep recovering the same thing: three different importance criteria, applied at step level to the same traces, overlap 70-80% on which steps to preserve while disagreeing on which to delete, which is read as all of them locating one shared backbone and treating the remainder as interchangeable. The corollary is that redundancy is diffuse rather than localized — the skeleton is repeated and rephrased throughout a long trace, so moderate compression is robust as long as the skeleton survives, irrespective of which particular elaborations go. Two sources approach the same object structurally rather than by scoring, one keeping the nodes of a dependency graph that advance the reasoning frontier and one consolidating fragmented steps into fewer denser units. The concept is defined by what survives compression rather than measured directly, so it is an inference from agreement between methods, not an object any source isolates independently.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [attention analysis](../methods/attention-analysis.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO](../methods/dpo.md), [Gemini-2.5-Flash](../models/gemini-2-5-flash.md), [generative rewriting](../methods/generative-rewriting.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [length penalty](../methods/length-penalty.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [Qwen2.5](../models/qwen2-5.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](reasoning-redundancy.md), [restructuring level](restructuring-level.md), [self-correction](self-correction.md), [supervised finetuning](../methods/supervised-finetuning.md), [token efficiency](token-efficiency.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [When Compression Helps and When It Hurts: Condition-Aware Analysis of Chain-of-Thought Distillation](../../archive/papers/2026/local-4acfffb647c2e41f/summary.md) — Runs the head-to-head this literature had been missing, comparing three importance criteria on the same traces at matched compression ratios, and finds step-level criteria agree on what to keep while disagreeing on what to cut — because redundancy is diffuse rather than located in any identifiable class of step.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
