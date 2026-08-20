# PubMedQA

<!-- auto:begin -->

A biomedical question-answering set built from research abstracts, used in both sources as a medical benchmark among several. In the consensus-rubric work it is one of six medical benchmarks and one of the places where three-state criterion scoring gains most (6.80 points), though the final system does not lead on it -- a reminder that the method's headline is a macro-average over benchmarks that individually disagree. In the hidden-state norm work it is one of the evaluation sets for a training-free reasoning-effort proxy. Neither source describes its construction.

- **Kind**: dataset
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [annotation agreement](../concepts/annotation-agreement.md), [BBH](bbh.md), [Claude Sonnet 4.5](../models/claude-sonnet-4-5.md), [consensus](../concepts/consensus.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DPO](../methods/dpo.md), [Gemini-2.5-pro](../models/gemini-2-5-pro.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GPT-4.1](../models/gpt-4-1.md), [GPT-5-mini](../models/gpt-5-mini.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [human evaluation](../methods/human-evaluation.md), [IFEval](ifeval.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MMLU-Pro](mmlu-pro.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [position bias](../concepts/position-bias.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [TruthfulQA](truthfulqa.md), [verifiable reward](../concepts/verifiable-reward.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering](../../archive/papers/2026/arxiv-2608-10996/summary.md) — Trains open-ended medical question answering by scoring each response against rubric criteria that three frontier models independently agreed on, grading each criterion as correct, missing or wrong rather than yes/no, and recovering a gradient in groups where every response ties by judging the responses pairwise in both orders.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
