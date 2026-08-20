# PCA

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: Principal Component Analysis, principal component analysis
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [ablation](ablation.md), [activation patching](activation-patching.md), [activation steering](activation-steering.md), [Aya-expanse-8B](../models/aya-expanse-8b.md), [beam search](beam-search.md), [causal intervention](causal-intervention.md), [causal mediation analysis](causal-mediation-analysis.md), [chain of thought distillation](chain-of-thought-distillation.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [detection versus control](../concepts/detection-versus-control.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPT-2](../models/gpt-2.md), [GSM8K](../datasets/gsm8k.md), [indirect object identification](../datasets/indirect-object-identification.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [Llama-3-8B-Instruct](../models/llama-3-8b-instruct.md), [logistic regression](logistic-regression.md), [logit lens](logit-lens.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [monosemanticity](../concepts/monosemanticity.md), [Phi-4](../models/phi-4.md), [polysemanticity](../concepts/polysemanticity.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [scaling laws](../concepts/scaling-laws.md), [Shapley value](../concepts/shapley-value.md), [sparse autoencoder](sparse-autoencoder.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [t-SNE](t-sne.md), [test-time scaling](test-time-scaling.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) — Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
