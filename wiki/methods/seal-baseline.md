# SEAL (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME24-25](../datasets/aime24-25.md), [AMC](../datasets/amc.md), [AQuA-RAT](../datasets/aqua-rat.md), [Chain-of-Draft (baseline)](chain-of-draft-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](deer-baseline.md), [Dynasor (baseline)](dynasor-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [GSM8K-Hard](../datasets/gsm8k-hard.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [NoThinking (baseline)](nothinking-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-4B-Thinking](../models/qwen3-4b-thinking.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [SciQ](../datasets/sciq.md), [SVAMP](../datasets/svamp.md)

## Appears in

- [How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1507/summary.md) — Analyzing how answer tokens attend back to reasoning tokens ('self-reading') in thinking LLMs reveals a stable, structured 'benign self-reading' pattern strongly correlated with correctness -- a forward-drifting attention centroid plus persistent focus on key semantic anchors -- interpreted as internal certainty, versus diffuse/irregular attention in incorrect solutions; a training-free Self-Reading Quality (SRQ) score built from this pattern is used to select contrastive samples for activation-steering vectors that consistently improve accuracy (up to 2.6pp) across three models, three steering mechanisms, and multiple quantitative-reasoning benchmarks including out-of-domain transfer.
- [Activation Steering for Chain-of-Thought Compression](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1828/summary.md) — Shows via t-SNE that verbose and concise chains-of-thought occupy visibly separable regions of a reasoning model's intermediate activation space, then learns a single, KL-trust-region-constrained steering vector (Contrastive Energy-Based Steering, CES) from only 100 verbose-concise CoT pairs by ranking concise traces below verbose ones in length-normalized energy under the steered model -- Activation-Steered Compression (ASC) cuts CoT length up to 69.35% with no accuracy loss across four model scales and multiple benchmarks, achieves 2.7x end-to-end wall-clock speedup, generalizes cross-task with 0.92 cosine similarity between dataset-specific steering vectors, and mitigates a documented 'underthinking' failure mode (excessive backtracking/path-switching without commitment) in QwQ-32B specifically.
- [Steering LLM Thinking with Budget Guidance](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1866/summary.md) — Budget guidance adapts diffusion-model classifier guidance to LLM reasoning: a lightweight BERT-based predictor estimates a Gamma distribution over each candidate next token's remaining-thinking-length (from the frozen target LLM's hidden states), and its CDF up to the budget is multiplied elementwise into the LLM's own token distribution -- steering generation smoothly toward a token budget without fine-tuning the LLM or hard-cutting it off, beating budget forcing by up to 26% accuracy on MATH-500 under tight budgets while using 37% fewer thinking tokens, and generalizing across model families, sizes, and out-of-domain tasks despite training only on math data.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
