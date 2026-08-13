# Qwen3-30B-A3B

<!-- auto:begin -->

A mixture-of-experts checkpoint with roughly 3B active parameters out of 30B, present in both sources as the architecture check rather than the headline model. One ternarizes it in a scaling sweep and uses the comparison against a dense model of comparable size to establish that MoE degrades more under quantization than dense does. The other uses it as one of two secondary backbones confirming that an answer-evidence gap measured on a dense model is not an artefact of that architecture. Its role in the archive is as evidence about sparsity rather than about scale.

- **Kind**: model
- **Also called**: Qwen3-30B
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [auditability](../concepts/auditability.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [KV cache compression](../methods/kv-cache-compression.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MBPP+](../datasets/mbpp.md), [Omni-MATH](../datasets/omni-math.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — Replays one fixed reasoning trace through eleven KV cache compression methods and finds that the ones preserving final-answer accuracy are largely the ones destroying the reasoning that supports it — on AIME the accuracy ranking of compressors correlates with their chain-validity ranking at Spearman -0.95.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
