# linear representation hypothesis

<!-- auto:begin -->

The hypothesis that texts exhibiting a concept are linearly separable in a model's representation space from those that do not, which is what licenses reading a concept off a direction and, by extension, steering along it. The two sources use it at the two ends of its consequences. One relies on it constructively, finding that activations taken before each explicit step marker occupy linearly separable step-indexed regions. The other attacks the inference usually drawn from it: separability establishes that a direction detects the concept and says nothing about what translating along it does, since directions with near-perfect discriminability can steer the model the opposite way. The hypothesis survives; the step from it to control does not.

- **Kind**: concept
- **Also called**: Linear Representation Hypothesis, linear representation hypothesis
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [attention head](attention-head.md), [causal intervention](causal-intervention.md), [chain of thought distillation](../methods/chain-of-thought-distillation.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [detection versus control](detection-versus-control.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GSM8K](../datasets/gsm8k.md), [Inference Time Intervention](inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logit lens](../methods/logit-lens.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [principal component analysis](../methods/principal-component-analysis.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [reasoning trajectory](reasoning-trajectory.md), [representation versus readout](representation-versus-readout.md), [steering vector](../methods/steering-vector.md), [superposition](superposition.md), [t-SNE](../methods/t-sne.md), [test-time scaling](../methods/test-time-scaling.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
