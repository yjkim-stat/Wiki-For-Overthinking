# Llama-3.2-1B-Instruct

<!-- auto:begin -->

A 1-billion-parameter instruction-tuned Llama model, and in this archive most useful for the role it plays in a control rather than as a subject. In the steering-pressure study it is the small model that never produced the evaluated responses, used to establish a prompt-only probing baseline: the identical probe trained on its activations reaches 0.72 balanced accuracy, because the items being classified are by construction more ambiguous as prompts and any competent model represents prompt ambiguity -- so the 70B model's 0.87 plateau is worth only about 14 points above what the prompt alone supplies. It also appears as the smallest of 18 open models in the cultural-awareness study, where the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults. Neither source describes the model, and its value here is as the cheapest available control on a probing claim.

- **Kind**: model
- **Also called**: Llama-3.2-1B-Instruct
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [benchmark design](../concepts/benchmark-design.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Opus 4.7](claude-opus-4-7.md), [Cohen's kappa](../methods/cohen-s-kappa.md), [construct validity](../concepts/construct-validity.md), [DeepSeek](deepseek.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [Gemma-4-26B-A4B-it](gemma-4-26b-a4b-it.md), [Gemma-4-31B-it](gemma-4-31b-it.md), [GPT-5](gpt-5.md), [IFEval](../datasets/ifeval.md), [jury aggregation](../methods/jury-aggregation.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logit lens](../methods/logit-lens.md), [monitorability](../concepts/monitorability.md), [nested cross-validation](../methods/nested-cross-validation.md), [PCA](../methods/pca.md), [permutation test](../methods/permutation-test.md), [Phi-4](phi-4.md), [position bias](../concepts/position-bias.md), [Qwen](qwen.md), [Qwen2.5-1.5B-Instruct](qwen2-5-1-5b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3.6-27B](qwen3-6-27b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](../methods/ridge-regression.md), [scaling laws](../concepts/scaling-laws.md), [selectivity control](../methods/selectivity-control.md), [steering vector](../methods/steering-vector.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Divergent Response Modes in Frontier Language Models Under Steering Pressure](../../archive/papers/2026/arxiv-2608-06578/summary.md) — Measures not how far six frontier models move under steering pressure but what kind of response they give when they decline, finds several response modes belonging to a single model, and then traces the largest within-model split to a linearly decodable and causally steerable direction in an open-weight model's residual stream.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
