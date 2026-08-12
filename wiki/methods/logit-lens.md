# Logit Lens

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [causal intervention](causal-intervention.md), [chain of thought distillation](chain-of-thought-distillation.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Coconut](coconut.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [entropy collapse](../concepts/entropy-collapse.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [latent chain of thought](latent-chain-of-thought.md), [linear probe](linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [t-SNE](t-sne.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
