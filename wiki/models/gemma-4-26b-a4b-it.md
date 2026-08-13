# Gemma-4-26B-A4B-it

<!-- auto:begin -->

A mixture-of-experts checkpoint with roughly 4B active parameters out of 26B total, used by both sources as one member of a multi-model sweep rather than as a subject. In one it is among the 18 models where the culture of a mythological entity is linearly readable from the residual stream while generation emits the wrong name, and its probe reaches 0.69 at layer 3 — an unusually early encoding depth for the sweep. In the other it is among the models probed for where a reasoning chain commits to its answer. Its presence in the archive is chiefly as evidence that these findings are not confined to dense architectures.

- **Kind**: model
- **Also called**: Gemma-4-26B-A4B, gemma-4-26B-A4B-it
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [AIME25](../datasets/aime25.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-OSS-20B](gpt-oss-20b.md), [linear probe](../methods/linear-probe.md), [linear probing](../methods/linear-probing.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [logit lens](../methods/logit-lens.md), [MATH500](../datasets/math500.md), [monitorability](../concepts/monitorability.md), [overthinking](../concepts/overthinking.md), [Phi-4](phi-4.md), [principal component analysis](../methods/principal-component-analysis.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-14B](qwen3-14b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [residual stream](../concepts/residual-stream.md), [scaling laws](../concepts/scaling-laws.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](../../archive/papers/2026/local-d6e266929de37684/summary.md) — Measures each CoT step's causal contribution by truncating the trace and forcing an answer, finds reasoning crosses a sharp single-step 'commitment boundary' after which the answer probability stops moving, and trains activation probes to detect that boundary and exit early.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
