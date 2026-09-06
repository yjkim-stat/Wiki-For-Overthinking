# Qwen3-32B-Thinking

<!-- auto:begin -->

Qwen3-32B-thinking is the thinking-mode variant tested by NeuReasoner's Mixture-of-Neurons overthinking detector (which trains monitoring MLPs to spot intra-step, inter-step and instance-level overthinking signatures online) and by FoE's Forest-of-Errors finding that a model's first-generated solution is optimal in up to 93.7% of cases.

- **Kind**: model
- **Also called**: Qwen3-32B-thinking
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DeepSeek-V3](deepseek-v3.md), [GLM-4.5-Air](glm-4-5-air.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Qwen3-8B-thinking](qwen3-8b-thinking.md), [test-time compute allocation](../concepts/test-time-compute-allocation.md)

## Appears in

- [Thinking effort aligns between humans and reasoning models in abductive reasoning](../../archive/papers/2026/arxiv-2609-01867/summary.md) — Measures whether reasoning models spend tokens on the same items humans spend time on, using a forced-choice abductive task where item difficulty cannot be read off formal structure, and finds a significant per-item correlation in all eight models tested.
- [NeuReasoner: Towards Explainable, Controllable, and Unified Reasoning via Mixture-of-Neurons](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1033/summary.md) — NeuReasoner identifies a Mixture of Neurons (MoN) -- three distinct neuron clusters in an LRM's middle layer whose fluctuation signatures predict intra-step (calculation/derivation) errors, inter-step (oscillation/stagnation) failures, and instance-level overthinking respectively -- then trains lightweight monitoring MLPs to detect these fluctuations online and trigger special-token-conditioned diagnose-then-correct behaviors, achieving 3.2-27.0% accuracy gains while cutting token consumption 19.6-63.3% across six backbones (8B-70B) and six benchmarks, beating nine training-free and RL-based efficient-reasoning baselines.
- [FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1128/summary.md) — Discovers 'The First is The Best' -- across five reasoning benchmarks and multiple LRMs, a model's first-generated solution is optimal in up to 93.7% of cases, because reasoning errors form a self-propagating forest structure (Forest of Errors, FoE) that grows faster and larger in subsequent solutions than in the first -- then proposes RED (Refine First, Discard Subs), which entropy-triggers negative-prompt intervention only on the first solution's root-error-prone segments and prunes all subsequent solutions via a dual-consistency early-stop check, improving accuracy up to 19.0% while cutting tokens 37.7-70.4% across six backbones and five benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
