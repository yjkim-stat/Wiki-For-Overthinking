# Inference Time Intervention

<!-- auto:begin -->

Changing what a model does at generation time without touching its parameters, which both sources adopt for the same reason: fine-tuning-based defences are costly and do not scale. Both also place the intervention mid-trajectory rather than at the input or the output, because that is where they locate the failure. One reads internal attention to find key points in the reasoning path and injects safety-oriented reflections there, then samples to select a safe path. The other extracts objective visual evidence into a structured intent representation and enforces safety constraints before generation, on the finding that models perceive risk cues correctly and then lose them as narrative coherence takes over. Both need white-box access.

- **Kind**: concept
- **Also called**: decoding-time intervention, inference-time defense, inference-time intervention, test-time intervention
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation steering](../methods/activation-steering.md), [aha moment](aha-moment.md), [attention analysis](../methods/attention-analysis.md), [attention head](attention-head.md), [attention pattern](attention-pattern.md), [causal intervention](causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [jailbreak](jailbreak.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [multimodal reasoning](multimodal-reasoning.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [representation versus readout](representation-versus-readout.md), [steering vector](steering-vector.md), [test-time compute](test-time-compute.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — An inference-time safeguard that reads a reasoning model's attention to find key points in its reasoning path and injects safety reflections there, then scales sampling to pick a safe path.
- [Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1821/summary.md) — Identifies a multimodal failure where models see the risky visual cue but let narrative coherence override safety as reasoning proceeds, and defends against it by extracting intent before generation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
