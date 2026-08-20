# Gemma-3-4B

<!-- auto:begin -->

A small open multimodal model, used by both sources as a baseline rather than as a subject. In one it is among the open comparisons a chart-reasoning method is measured against, where it trails the finetuned models substantially at every curriculum level. In the other it appears in a sweep testing whether a hidden-state norm signal for reasoning effort holds across model families. Neither studies the checkpoint; its role is to establish that a result is not confined to one lineage.

- **Kind**: model
- **Also called**: Gemma 3 4B
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BBH](../datasets/bbh.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](../concepts/compositional-generalization.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [GPQA](../datasets/gpqa.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU-Pro](../datasets/mmmu-pro.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](phi-4-reasoning.md), [process supervision](../concepts/process-supervision.md), [PubMedQA](../datasets/pubmedqa.md), [Qwen2.5-VL-3B](qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [reasoning depth](../concepts/reasoning-depth.md), [reinforcement learning](../methods/reinforcement-learning.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [TruthfulQA](../datasets/truthfulqa.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
