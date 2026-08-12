# activation steering

<!-- auto:begin -->

Changing a model's behaviour by adding or modifying directions in its activation space at inference, without updating weights. The sources treat single-layer contrastive addition as the baseline and find it insufficient: it imposes one intervention across semantically diverse inputs and does not persist across layers, failing entirely on sycophancy and refusal. CircuitSteer instead selects features across multiple layers by co-activation and decoder-direction alignment and intervenes at several points. Steering also appears here as a controllability tool rather than an interpretability one, used to set a simulated patient's resistance level, and one source reports that a reasoning model's eventual token count is linearly decodable from the question's activations before any reasoning token is emitted, which makes reasoning length a steerable quantity.

- **Kind**: method
- **Also called**: activation addition, representation engineering, steering, steering vector
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [AIME24](../datasets/aime24.md), [AlpacaEval](../datasets/alpacaeval.md), [budget forcing](budget-forcing.md), [chain of thought](chain-of-thought.md), [circuit discovery](circuit-discovery.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [linear probing](linear-probing.md), [literature survey](literature-survey.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [MMLU](../datasets/mmlu.md), [monosemanticity](../concepts/monosemanticity.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [QwQ-32B](../models/qwq-32b.md), [sparse autoencoder](sparse-autoencoder.md), [steering](../concepts/steering.md), [superposition](../concepts/superposition.md), [supervised fine-tuning](supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [synthetic data generation](synthetic-data-generation.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance](../../archive/papers/2026/arxiv-2608-04524/summary.md) — Synthesizes Cognitive Behavioral Therapy dialogues using a CoT strategy grounded in CBT guidelines plus a resistance orchestrator that steers simulated patients away from sycophantic compliance.
- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-502/summary.md) — A survey reorganizing mechanistic interpretability from observation into a Locate-Steer-Improve intervention pipeline, categorized by the interpretable object being acted on.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
