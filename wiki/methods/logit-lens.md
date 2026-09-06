# logit lens

<!-- auto:begin -->

Logit lens -- projecting a model's intermediate-layer hidden states through the unembedding matrix to read off the model's evolving token predictions before the final layer -- is used in the multilingual-latent-reasoning paper to track how a gold answer's predicted rank changes across layers/languages, finding internal solution-formation dynamics are largely language-invariant despite differing surface-level accuracy; 'Think Deep, Not Just Long' uses a related late-layer-revision signal (the fraction of tokens still being revised in late layers) to measure reasoning effort, though its own note does not name logit lens explicitly.

- **Kind**: method
- **Also called**: Logit Lens, logit lens
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Budget Forcing](budget-forcing.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT 2025](../datasets/hmmt-2025.md), [Latent reasoning](../concepts/latent-reasoning.md), [MATH500](../datasets/math500.md), [Nemotron-32B](../models/nemotron-32b.md), [OpenThoughts-114k](../datasets/openthoughts-114k.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-32B-Instruct](../models/qwen2-5-32b-instruct.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning effort](../concepts/reasoning-effort.md), [Self-Certainty](../concepts/self-certainty.md), [Self-Consistency](self-consistency.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md)

## Appears in

- [Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1121/summary.md) — Using a truncation-based diagnostic across 11 languages, 3 model sizes, and 2 benchmarks, this paper measures how strongly LRMs already know the answer before finishing their explicit reasoning trace ('latent reasoning'), finding it exists but is uneven -- strong in resource-rich languages on easy tasks, weak in low-resource languages, and largely absent on harder benchmarks -- and that the internal layer-wise dynamics driving it are strikingly consistent across languages, converging toward an English-centered latent pathway that is not explained by memorization alone.
- [Controllable LLM Reasoning via Sparse Autoencoder-Based Steering](../../archive/papers/2026/local-58250e189d273b56/summary.md) — Trains a sparse autoencoder on a reasoning model's hidden states to disentangle strategy-specific latent features, then identifies and injects the most effective one as a control vector to steer which cognitive reasoning strategy (backtracking, verification, etc.) the model uses next, including to correct wrong answers.
- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](../../archive/papers/2026/title-bcd9cf99a0e84a2d/summary.md) — Measures a reasoning model's inference-time effort not by how many tokens it emits but by what fraction of them are still being revised in the network's late layers, and uses that fraction to pick which of many sampled generations to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
