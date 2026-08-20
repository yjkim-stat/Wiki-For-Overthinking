# Qwen2.5-VL-3B

<!-- auto:begin -->

A small vision-language checkpoint, used in both sources as the scale at which a multimodal method is developed before being confirmed at 7B. In one it is the primary backbone for a step-wise visual grounding framework and carries most of the ablations — the layer sweep, the grounding-strategy comparison, and the explicit-versus-implicit contrast. In the other it appears in work on RLVR eroding general capability. Neither characterizes the model itself.

- **Kind**: model
- **Also called**: Qwen2.5-VL-3B-Instruct
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [catastrophic forgetting](../concepts/catastrophic-forgetting.md), [chain of thought](../methods/chain-of-thought.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](../concepts/compositional-generalization.md), [curriculum learning](../concepts/curriculum-learning.md), [Gemma-3-4B](gemma-3-4b.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [KL regularization](../methods/kl-regularization.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [reasoning depth](../concepts/reasoning-depth.md), [reinforcement learning](../methods/reinforcement-learning.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [training dynamics](../concepts/training-dynamics.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
