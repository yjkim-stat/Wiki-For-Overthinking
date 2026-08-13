# Llama-3.2-3B-Instruct

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Also called**: LLaMA-3.2-3B-Instruct
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [best-of-n](../methods/best-of-n.md), [causal intervention](../concepts/causal-intervention.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit analysis](../methods/circuit-analysis.md), [credit assignment](../concepts/credit-assignment.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [logit lens](../methods/logit-lens.md), [MATH-500](../datasets/math-500.md), [Phi-4](phi-4.md), [policy gradient](../methods/policy-gradient.md), [principal component analysis](../methods/principal-component-analysis.md), [Qwen2.5-14B-Instruct](qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [residual stream](../concepts/residual-stream.md), [scaling laws](../concepts/scaling-laws.md), [self-consistency](../methods/self-consistency.md), [self-reflection](../methods/self-reflection.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) — Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
