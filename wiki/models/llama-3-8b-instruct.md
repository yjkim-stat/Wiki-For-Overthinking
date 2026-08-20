# Llama-3-8B-Instruct

<!-- auto:begin -->

An 8-billion-parameter instruction-tuned Llama model, used in this archive as an evaluation subject in two unrelated settings. TQLite includes it among nineteen models benchmarked under one MQM prompt as translation-quality judges. The per-instance activation steering paper makes it the primary of its two models over six binary persona traits, and it is where that paper's central claim is strongest: the label-free deployable recipe recovers 93 percent of the exhaustive steerable lift, exceeds the gold-aware global oracle on five of six tasks despite having no labels, and never drives a trait-model cell below its unsteered baseline where the fixed global rules do so on four cells. The contrast with the same paper's second model, where the recipe recovers only 65 percent, is the cross-model dissociation its mechanistic account is built to explain.

- **Kind**: model
- **Also called**: Llama-3-8B-Instruct, Llama-3-8B-it
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [Aya-expanse-8B](aya-expanse-8b.md), [beam search](../methods/beam-search.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [detection versus control](../concepts/detection-versus-control.md), [GEMBA-MQM](../methods/gemba-mqm.md), [Gemini-2.0-flash](gemini-2-0-flash.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [GPT-2](gpt-2.md), [GPT-4](gpt-4.md), [GPT-4.1-mini](gpt-4-1-mini.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3-70B-Instruct](llama-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logistic regression](../methods/logistic-regression.md), [LoRA](../methods/lora.md), [PCA](../methods/pca.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Shapley value](../concepts/shapley-value.md), [steering vector](../methods/steering-vector.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [WMT22](../datasets/wmt22.md)

## Appears in

- [TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation](../../archive/papers/2026/arxiv-2608-02975/summary.md) — Benchmarks 20-plus models as MQM translation-quality judges, finds reasoning models best and a jury of different ones better than any member, then distils that jury's agreement-filtered annotations into a 12B student that beats every open reasoning-model judge tested.
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) — Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
