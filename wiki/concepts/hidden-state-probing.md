# Hidden-State Probing

<!-- auto:begin -->

In these sources, hidden-state probing means training a small classifier on the internal activations of a frozen reasoning model to predict something that has not been generated yet, so that inference compute can be allocated without fine-tuning the model itself. BLADE probes layer-wise hidden states at sentence and self-doubt boundaries to estimate whether the prefix already supports a correct answer, selecting a fixed set of K layers by distilling a dense cross-layer model into a gated one and stopping generation when a conformally calibrated threshold is met (Qwen3-8B: 7,837 to 5,896 average tokens, -24.8%, accuracy 76.8% to 75.2%). DiffAdapt probes only the final hidden state of the question at prefill to classify it Easy/Normal/Hard and applies a matching prompt, temperature and token cap, cutting tokens by up to 22.4% on Qwen3-4B at comparable accuracy. The two agree on the shape of the technique -- a cheap probe over a frozen backbone -- and differ on what is probed for and when: sufficiency of a partial trace, checked repeatedly during generation, against difficulty of the question, decided once before it starts.

- **Kind**: concept
- **Also called**: Hidden-state probing, hidden-state probe
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [Accuracy-Efficiency Score (AES)](accuracy-efficiency-score-aes.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [difficulty estimation](difficulty-estimation.md), [Dynamic Early Exit](../methods/dynamic-early-exit.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md)

## Appears in

- [BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning](../../archive/papers/2026/arxiv-2607-28966/summary.md) — BLADE trains a lightweight hidden-state probe to decide, at sentence and self-doubt boundaries, whether a reasoning prefix already supports the correct answer, and stops generation when it does.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
