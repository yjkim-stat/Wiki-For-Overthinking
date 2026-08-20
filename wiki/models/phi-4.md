# Phi-4

<!-- auto:begin -->

A 14B instruction-tuned model, used by both sources as a mid-scale point in a multi-model comparison. In one it is among the 18 models where cultural identity is recoverable from the residual stream at 0.86 probe accuracy while generation reaches 0.31, and it is singled out as recovering under multiple-choice selection everything its probe reads — the clearest single case that the loss is at generation rather than at representation. In the other it is among the backbones for which representation-based exploration is evaluated. Neither studies the model itself.

- **Kind**: model
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [best-of-n](../methods/best-of-n.md), [causal intervention](../methods/causal-intervention.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [Game of 24](../datasets/game-of-24.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [logit lens](../methods/logit-lens.md), [MATH](../datasets/math.md), [MBPP+](../datasets/mbpp.md), [Mistral-7B](mistral-7b.md), [pass@k](../methods/pass-k.md), [PCA](../methods/pca.md), [policy entropy](../concepts/policy-entropy.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-32B](qwen2-5-32b.md), [Qwen2.5-7B](qwen2-5-7b.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](../methods/ridge-regression.md), [RLVR](../methods/rlvr.md), [scaling laws](../concepts/scaling-laws.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](../../archive/papers/2026/local-1fadd9f07b138261/summary.md) — Uses elliptical bonuses over a language model's own hidden-state representations as a diversity signal, validates it in a clean inference-time selection setting, then transfers the same signal into RL post-training — where it eliminates the diversity collapse that degrades pass@k at large k.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
