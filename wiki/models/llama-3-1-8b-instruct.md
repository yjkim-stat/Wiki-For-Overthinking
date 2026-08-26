# LLaMA-3.1-8B-Instruct

<!-- auto:begin -->

LLaMA-3.1-8B-Instruct is an open-weight instruction-tuned model that the archive's sources use as a baseline or a backbone rather than study. FIRE uses it as the strongest supervised fine-tuned baseline its two sub-2B agents are compared against, losing to FIRE on human preference at win rates of 0.86 to 0.93 across four criteria, and cites the 8B class as the monolithic alternative whose roughly 16GB peak VRAM its sequential 1.7B agents cut to about 4GB. Heima uses the family as the backbone whose textual chain-of-thought stages are replaced by single latent thinking tokens. Neither source reports capability figures for the model outside those specific comparisons.

- **Kind**: model
- **Also called**: LLaMA-3.1-8B, Llama-3.1-8B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AI2D](../datasets/ai2d.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Latent reasoning](../concepts/latent-reasoning.md), [MathVista](../datasets/mathvista.md), [MMStar](../datasets/mmstar.md)

## Appears in

- [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](../../archive/papers/2026/arxiv-2608-23152/summary.md) — FIRE splits counterspeech generation into two sub-2B Qwen3-1.7B agents -- one that classifies the hate category, names the target group, writes a reasoning trace and triggers a web search for evidence, one that writes the reply -- with specialization coming from a contrastively-trained 22M retrieval encoder over annotated examples rather than from fine-tuning.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
