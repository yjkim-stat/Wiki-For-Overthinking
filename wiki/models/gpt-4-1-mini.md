# GPT-4.1-mini

<!-- auto:begin -->

A small proprietary model, appearing in both sources as evaluation apparatus rather than as a subject. One uses it as the macro-level judge scoring chart-reasoning answers by a true-or-false assessment, alongside rule-based metrics introduced specifically to mitigate judge bias. The other uses it to score open-ended concept expression under steering. Both therefore depend on it for the numbers they report while studying something else, which is worth noting: a judge model is a load-bearing part of an experimental setup that papers rarely audit and this archive separately holds evidence is prompt- and format-sensitive.

- **Kind**: model
- **Also called**: gpt-4.1-mini
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation steering](../methods/activation-steering.md), [attention head](../concepts/attention-head.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](../concepts/compositional-generalization.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [curriculum learning](../concepts/curriculum-learning.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-of-means probe](../methods/difference-of-means-probe.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [Gemma-3-4B](gemma-3-4b.md), [GPT-4](gpt-4.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [Inference Time Intervention](../concepts/inference-time-intervention.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [LoRA](../methods/lora.md), [MathVista](../datasets/mathvista.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [process supervision](../concepts/process-supervision.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-14B](qwen2-5-14b.md), [Qwen2.5-VL-3B](qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [reinforcement learning](../methods/reinforcement-learning.md), [representation versus readout](../concepts/representation-versus-readout.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [TruthfulQA](../datasets/truthfulqa.md), [visual grounding](../concepts/visual-grounding.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
