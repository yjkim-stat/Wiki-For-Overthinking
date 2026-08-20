# Inference Time Intervention

<!-- auto:begin -->

Changing what a model does at generation time without updating weights -- injecting a direction, inserting a reflection, re-prompting under a derived constraint, or masking part of the input. Across 4 sources the appeal is deployment-shaped: no retraining, switchable per query, and applicable to a frozen model. The corpus's instances differ in where they intervene. On activations, where the archive's standing result is that the sign of the effect is not determined by the direction's discriminability, so a training-free test that fixes the sign improves a standard pipeline in 27 of 30 experiments. On the trace, where a safeguard reads attention to find key points in a reasoning path and injects safety reflections there before scaling sampling to pick a safe path. And on the prompt, where a two-stage protocol extracts a problem's answer-space constraints first and then checks intermediate and final results against them, routed by a detector so the cost is conditional. The archive's related trade is that a decoding-time correction is switchable and costs latency on every query it fires on, while a weight-absorbed one is free at inference and permanent.

- **Kind**: method
- **Also called**: ITI, decoding-time intervention, inference-time defense, inference-time intervention, test-time intervention, training-free intervention
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [activation steering](activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [aha moment](../concepts/aha-moment.md), [AIME](../datasets/aime.md), [attention analysis](attention-analysis.md), [attention head](../concepts/attention-head.md), [attention pattern](../concepts/attention-pattern.md), [Brumo](../datasets/brumo.md), [causal intervention](causal-intervention.md), [chain of thought](../concepts/chain-of-thought.md), [CMIMC](../datasets/cmimc.md), [contrastive activation addition](contrastive-activation-addition.md), [detection versus control](../concepts/detection-versus-control.md), [difference-of-means probe](difference-of-means-probe.md), [Gemma-3-12B](../models/gemma-3-12b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [jailbreak](../concepts/jailbreak.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](llm-as-a-judge.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [representation versus readout](../concepts/representation-versus-readout.md), [routing](../concepts/routing.md), [self-verification](../concepts/self-verification.md), [steering vector](steering-vector.md), [test-time compute](../concepts/test-time-compute.md), [TruthfulQA](../datasets/truthfulqa.md), [verification](../concepts/verification.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) — A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.
- [Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1821/summary.md) — Identifies a multimodal failure where models see the risky visual cue but let narrative coherence override safety as reasoning proceeds, and defends against it by extracting intent before generation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
