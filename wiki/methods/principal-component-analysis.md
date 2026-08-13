# principal component analysis

<!-- auto:begin -->

Projecting high-dimensional activations onto their directions of greatest variance, used by both sources as the first step of a pipeline rather than as a result. One reduces residual-stream activations to 50 dimensions before a discriminant projection, to show that cultures form visibly distinct clusters at each model's probe-peak layer even where the output collapses to a Greco-Roman default. The other applies it to step-marker activations that turn out to occupy linearly separable, step-indexed regions. In both the projection makes a structure visible and something else — a classifier, a separability test — is what establishes it, which is the discipline the technique requires: a layout is not a measurement.

- **Kind**: method
- **Also called**: PCA, Principal Component Analysis
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought distillation](chain-of-thought-distillation.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GSM8K](../datasets/gsm8k.md), [linear probe](linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [logit lens](logit-lens.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [Phi-4](../models/phi-4.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [scaling laws](../concepts/scaling-laws.md), [t-SNE](t-sne.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals](../../archive/papers/2026/local-fc7e2641eda52776/summary.md) — Activations taken just before each explicit "Step k:" marker occupy linearly separable, step-indexed regions of representation space, and how a chain moves between those regions late in the trace predicts whether the final answer will be correct, which is used to gate interventions and to steer reasoning length.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
