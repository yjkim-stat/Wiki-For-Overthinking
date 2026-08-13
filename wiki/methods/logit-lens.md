# logit lens

<!-- auto:begin -->

Reading a model's intermediate hidden states through its output vocabulary projection, so that any layer's state can be inspected as a distribution over tokens. Both sources use it as an instrument rather than studying it, and in two different roles. One applies it at five evenly spaced layers every 50 decoding steps to compare Shannon entropy profiles between soft thinking and ordinary discrete decoding, where the two coincide. The other uses logit-lens features as a baseline for predicting whether a reasoning chain will end correctly, reaching 0.765 against 0.649 for step count alone and 0.852 for the trajectory-geometry features it proposes — so here the lens also serves as the yardstick a stronger representation-based signal has to beat.

- **Kind**: method
- **Also called**: Logit Lens
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought distillation](chain-of-thought-distillation.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Coconut](coconut.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [entropy collapse](../concepts/entropy-collapse.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [latent chain of thought](latent-chain-of-thought.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [PCA](pca.md), [Phi-4](../models/phi-4.md), [ProntoQA](../datasets/prontoqa.md), [ProsQA](../datasets/prosqa.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [scaling laws](../concepts/scaling-laws.md), [soft thinking](soft-thinking.md), [sparse autoencoder](sparse-autoencoder.md), [t-SNE](t-sne.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](../../archive/papers/2026/local-043e84b0b0ae0a39/summary.md) — Tests the claim that continuous chain-of-thought lets a model hold several candidate solutions at once, and finds it holds only for models trained from scratch: off-the-shelf models collapse a superposed input to a single token within a few layers, and fine-tuned latent reasoners solve the task in one forward pass and copy the answer through the latent slots.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
