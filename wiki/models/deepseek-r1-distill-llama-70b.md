# DeepSeek-R1-Distill-Llama-70B

<!-- auto:begin -->

DeepSeek-R1-Distill-Llama-70B is the largest distilled backbone tested in this archive's faithfulness-safety tension study (Risky Business) and in mechanistic-overthinking-detection work spanning 8B-70B backbones: NeuReasoner's Mixture-of-Neurons monitors and FoE's Forest-of-Errors finding that a model's first-generated solution is optimal in up to 93.7% of cases.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-32B-thinking](qwen3-32b-thinking.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-8B-thinking](qwen3-8b-thinking.md), [QwQ-32B](qwq-32b.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [NeuReasoner: Towards Explainable, Controllable, and Unified Reasoning via Mixture-of-Neurons](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1033/summary.md) — NeuReasoner identifies a Mixture of Neurons (MoN) -- three distinct neuron clusters in an LRM's middle layer whose fluctuation signatures predict intra-step (calculation/derivation) errors, inter-step (oscillation/stagnation) failures, and instance-level overthinking respectively -- then trains lightweight monitoring MLPs to detect these fluctuations online and trigger special-token-conditioned diagnose-then-correct behaviors, achieving 3.2-27.0% accuracy gains while cutting token consumption 19.6-63.3% across six backbones (8B-70B) and six benchmarks, beating nine training-free and RL-based efficient-reasoning baselines.
- [FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1128/summary.md) — Discovers 'The First is The Best' -- across five reasoning benchmarks and multiple LRMs, a model's first-generated solution is optimal in up to 93.7% of cases, because reasoning errors form a self-propagating forest structure (Forest of Errors, FoE) that grows faster and larger in subsequent solutions than in the first -- then proposes RED (Refine First, Discard Subs), which entropy-triggers negative-prompt intervention only on the first solution's root-error-prone segments and prunes all subsequent solutions via a dual-consistency early-stop check, improving accuracy up to 19.0% while cutting tokens 37.7-70.4% across six backbones and five benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
