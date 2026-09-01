# Qwen2.5-32B-Instruct

<!-- auto:begin -->

Qwen2.5-32B-Instruct is evaluated in ReEfBench (a neuro-symbolic evaluation framework grounding reasoning in First-Order-Logic problems with controllable, verifiable logical depth) and in a truncation-based diagnostic across 11 languages measuring how strongly large reasoning models already know the answer before finishing their explicit reasoning trace.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Latent reasoning](../concepts/latent-reasoning.md), [logit lens](../methods/logit-lens.md), [Nemotron-32B](nemotron-32b.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-32B](qwen2-5-32b.md), [QwQ-32B](qwq-32b.md)

## Appears in

- [ReEfBench: Quantifying the Reasoning Efficiency of LLMs](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-931/summary.md) — ReEfBench is a neuro-symbolic evaluation framework that grounds reasoning in First-Order-Logic problems with controllable, verifiable logical depth, parses 25 LLMs' CoT responses into logical nodes to compute six behavioral metrics (logical depth, cost, exploration, efficiency, coherence, redundancy), and clusters models into four behavioral prototypes -- Effective Solver, Deep Wanderer, Hollow Mimic, Lazy Guesser -- showing token count and genuine logical depth are dissociable, and that Short CoT with reflection can now match Long CoT's depth at a fraction of the cost.
- [Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1121/summary.md) — Using a truncation-based diagnostic across 11 languages, 3 model sizes, and 2 benchmarks, this paper measures how strongly LRMs already know the answer before finishing their explicit reasoning trace ('latent reasoning'), finding it exists but is uneven -- strong in resource-rich languages on easy tasks, weak in low-resource languages, and largely absent on harder benchmarks -- and that the internal layer-wise dynamics driving it are strikingly consistent across languages, converging toward an English-centered latent pathway that is not explained by memorization alone.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
