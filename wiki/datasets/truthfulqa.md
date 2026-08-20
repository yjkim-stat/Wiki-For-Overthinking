# TruthfulQA

<!-- auto:begin -->

A benchmark of questions where a common misconception makes the plausible answer false, used by both sources as the concept whose expression an intervention is supposed to change rather than as a leaderboard. One derives steering vectors for truthfulness from it and reports it as the concept requiring a relaxed discriminability threshold, so it is the hardest of the five studied to find a clean direction for. The other includes it among the benchmarks over which a hidden-state norm signal is validated. Its role here is as the concept where the linear picture is weakest, which is worth remembering given how often it is the concept steering work chooses to demonstrate on.

- **Kind**: dataset
- **Also called**: TQA
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [attention head](../concepts/attention-head.md), [BBH](bbh.md), [causal intervention](../concepts/causal-intervention.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-of-means probe](../methods/difference-of-means-probe.md), [Gemma-3-12B](../models/gemma-3-12b.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPQA](gpqa.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GSM8K](gsm8k.md), [IFEval](ifeval.md), [Inference Time Intervention](../concepts/inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MMLU-Pro](mmlu-pro.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [representation versus readout](../concepts/representation-versus-readout.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [steering vector](../methods/steering-vector.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
