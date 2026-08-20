# Llama-3.2-3B-Instruct

<!-- auto:begin -->

A 3B instruction-tuned Llama, used across 3 sources as a small cross-family backbone -- one of the 18 checkpoints in a cultural-knowledge audit, a subject for credit-assigned gradient flow in test-time latent reasoning, and a training backbone for label-free reinforcement learning. Its role is the usual one for this size: it establishes that a method is not specific to the Qwen line, and its low absolute scores mean a null on it is weak evidence about the method.

- **Kind**: model
- **Also called**: LLaMA-3.2-3B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [best-of-n](../methods/best-of-n.md), [causal intervention](../methods/causal-intervention.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit analysis](../methods/circuit-analysis.md), [credit assignment](../concepts/credit-assignment.md), [entropy collapse](../concepts/entropy-collapse.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [Gemma-4-31B-it](gemma-4-31b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [KL divergence](../methods/kl-divergence.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](../methods/linear-probe.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-1B](llama-3-2-1b.md), [Llama-3.2-1B-Instruct](llama-3-2-1b-instruct.md), [Llama-3.2-3B](llama-3-2-3b.md), [logit lens](../methods/logit-lens.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [outcome reward](../concepts/outcome-reward.md), [PCA](../methods/pca.md), [Phi-4](phi-4.md), [policy gradient](../concepts/policy-gradient.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-14B-Instruct](qwen2-5-14b-instruct.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-1.7B-Base](qwen3-1-7b-base.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [Qwen3.6-27B](qwen3-6-27b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [reward hacking](../concepts/reward-hacking.md), [ridge regression](../methods/ridge-regression.md), [RLVR](../methods/rlvr.md), [scaling laws](../concepts/scaling-laws.md), [self-consistency](../methods/self-consistency.md), [self-reflection](../methods/self-reflection.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) — Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.
- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) — Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
