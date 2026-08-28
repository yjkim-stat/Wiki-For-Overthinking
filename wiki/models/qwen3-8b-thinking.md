# Qwen3-8B-thinking

<!-- auto:begin -->

Qwen3-8B-thinking is the smaller-scale backbone in the same NeuReasoner (Mixture-of-Neurons overthinking detection) and FoE (Forest-of-Errors, 'first solution is best') studies also run on Qwen3-32B-thinking and DeepSeek-R1-Distill-Llama-70B, part of an 8B-70B backbone sweep.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Qwen3-32B-thinking](qwen3-32b-thinking.md)

## Appears in

- [NeuReasoner: Towards Explainable, Controllable, and Unified Reasoning via Mixture-of-Neurons](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1033/summary.md) — NeuReasoner identifies a Mixture of Neurons (MoN) -- three distinct neuron clusters in an LRM's middle layer whose fluctuation signatures predict intra-step (calculation/derivation) errors, inter-step (oscillation/stagnation) failures, and instance-level overthinking respectively -- then trains lightweight monitoring MLPs to detect these fluctuations online and trigger special-token-conditioned diagnose-then-correct behaviors, achieving 3.2-27.0% accuracy gains while cutting token consumption 19.6-63.3% across six backbones (8B-70B) and six benchmarks, beating nine training-free and RL-based efficient-reasoning baselines.
- [FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1128/summary.md) — Discovers 'The First is The Best' -- across five reasoning benchmarks and multiple LRMs, a model's first-generated solution is optimal in up to 93.7% of cases, because reasoning errors form a self-propagating forest structure (Forest of Errors, FoE) that grows faster and larger in subsequent solutions than in the first -- then proposes RED (Refine First, Discard Subs), which entropy-triggers negative-prompt intervention only on the first solution's root-error-prone segments and prunes all subsequent solutions via a dual-consistency early-stop check, improving accuracy up to 19.0% while cutting tokens 37.7-70.4% across six backbones and five benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
