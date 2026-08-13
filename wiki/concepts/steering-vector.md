# steering vector

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME24](../datasets/aime24.md), [AlpacaEval](../datasets/alpacaeval.md), [attention head](attention-head.md), [budget forcing](../methods/budget-forcing.md), [causal intervention](causal-intervention.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [Inference Time Intervention](inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [linear probing](../methods/linear-probing.md), [linear representation hypothesis](linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [QwQ-32B](../models/qwq-32b.md), [representation versus readout](representation-versus-readout.md), [test-time compute](test-time-compute.md), [TruthfulQA](../datasets/truthfulqa.md)

## What we have settled

- **Established** — How well a direction or signal detects a property licenses no claim about what intervening on it does — not the size of the effect, and not even its sign.
  - Three independent demonstrations, at three levels. Directions with near-perfect discriminability for a concept (AUC up to 0.97, aligned with its positive examples) reliably steer the model the *opposite* way, consistently across inputs rather than on a minority subset; 45 such vectors are mined across 15 model-concept pairs, and correcting their sign improves a standard steering pipeline in 27 of 30 experiments by up to 138%, with one uncorrected case steering a concept below its unsteered baseline. In an 18-model sweep a linear probe reads an entity's culture from the residual stream at 0.79 while generation emits it at 0.09, and only activation patching establishes where the pathway actually runs. And a perturbation score that provably depends on the image — blanking its inputs collapses accuracy from 87.7 to 7.9 — is matched or beaten at selection by a format-matched control that never sees the perturbations. Detection, decoding and control are three separate questions, and an experiment answering one answers neither of the others.

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
