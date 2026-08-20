# Qwen3.6-27B

<!-- auto:begin -->

A 27-billion-parameter Qwen model appearing twice in this archive as a panel member. On the industrial-safety reasoning benchmark it scores 40.9 percent overall untuned, the second-lowest of eight models and far below the frontier entries, which is part of that paper's evidence that general multimodal capability does not carry over to evidence-grounded safety reasoning. It is also one of 18 open models instrumented in the cultural-awareness study, whose finding -- that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults -- is reported across the panel. Neither source describes the model or reports a mechanism specific to it.

- **Kind**: model
- **Also called**: Qwen3.6-27B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [benchmark contamination](../concepts/benchmark-contamination.md), [benchmark design](../concepts/benchmark-design.md), [calibration](../methods/calibration.md), [causal intervention](../concepts/causal-intervention.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [decontamination](../methods/decontamination.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [Gemma-4-31B-it](gemma-4-31b-it.md), [GPT-5.5](gpt-5-5.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-1B-Instruct](llama-3-2-1b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [logit lens](../methods/logit-lens.md), [LoRA](../methods/lora.md), [macro versus micro accuracy](../concepts/macro-versus-micro-accuracy.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [multiple-choice evaluation](../methods/multiple-choice-evaluation.md), [PCA](../methods/pca.md), [Phi-4](phi-4.md), [position bias](../concepts/position-bias.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3.5-9B](qwen3-5-9b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](../methods/ridge-regression.md), [scaling laws](../concepts/scaling-laws.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](../../archive/papers/2026/arxiv-2608-09230/summary.md) — Builds an industrial-safety reasoning benchmark from two pipelines -- program execution over safety scene graphs, and evidence graphs extracted from real accident-investigation reports -- and shows that general multimodal capability does not transfer to it while a 9B model fine-tuned on its chain-of-thought split matches frontier systems.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
