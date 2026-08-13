# steering vector

<!-- auto:begin -->

A direction added to a model's activations at inference to promote or suppress a concept, most often the mean difference between representations of texts that exhibit it and texts that do not. One source uses them as an instrument and finds a model plans its reasoning effort in advance — a direction encoding intended length is present before generation and steering along it changes the length produced. The other studies the instrument itself and finds a class of directions that are highly discriminative and aligned with positive examples yet steer the opposite way, systematically enough to be identified from forward passes and corrected by a sign flip, improving a standard pipeline in 27 of 30 experiments. The pair is the archive's caution in miniature: a steering result is only as good as the check that the vector moves the model the way its discriminability suggests.

- **Kind**: method
- **Also called**: SV, activation steering vector
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [AIME24](../datasets/aime24.md), [AlpacaEval](../datasets/alpacaeval.md), [attention head](../concepts/attention-head.md), [budget forcing](budget-forcing.md), [causal intervention](../concepts/causal-intervention.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [detection versus control](../concepts/detection-versus-control.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [Inference Time Intervention](../concepts/inference-time-intervention.md), [linear probe](linear-probe.md), [linear probing](linear-probing.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](llm-as-a-judge.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [QwQ-32B](../models/qwq-32b.md), [representation versus readout](../concepts/representation-versus-readout.md), [test-time compute](../concepts/test-time-compute.md), [TruthfulQA](../datasets/truthfulqa.md)

## What we have settled

- **Established** — How well a direction or signal detects a property licenses no claim about what intervening on it does — not the size of the effect, and not even its sign.
  - Three independent demonstrations, at three levels. Directions with near-perfect discriminability for a concept (AUC up to 0.97, aligned with its positive examples) reliably steer the model the *opposite* way, consistently across inputs rather than on a minority subset; 45 such vectors are mined across 15 model-concept pairs, and correcting their sign improves a standard steering pipeline in 27 of 30 experiments by up to 138%, with one uncorrected case steering a concept below its unsteered baseline. In an 18-model sweep a linear probe reads an entity's culture from the residual stream at 0.79 while generation emits it at 0.09, and only activation patching establishes where the pathway actually runs. And a perturbation score that provably depends on the image — blanking its inputs collapses accuracy from 87.7 to 7.9 — is matched or beaten at selection by a format-matched control that never sees the perturbations. Detection, decoding and control are three separate questions, and an experiment answering one answers neither of the others.

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Shows that a reasoning model decides how long to think before emitting a single reasoning token — the eventual token count is linearly decodable from the question's activations at Spearman 0.84 — and that this plan is carried by one shared direction vector whose magnitude encodes strength and which acts by shifting the logits of the end-of-thinking token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
