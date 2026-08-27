# Qwen2.5-1.5B-Instruct

<!-- auto:begin -->

An open-weight instruction-tuned model used as an evaluation subject for adaptive test-time-scaling sample-budget allocation (per another archived source, a fuzzy-controller-based per-prompt sampling budget for best-of-N) and as one of the base models on which Marco-o1 v2's MCTS-constructed CoT data and CoT-aware post-training methods are shown to reduce 'formalistic long-time thinking' (a distillation-induced failure to internalize reasoning logic).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [Best-of-N sampling](../methods/best-of-n-sampling.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [MATH](../datasets/math.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [SciQ](../datasets/sciq.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Assigns a per-prompt sampling budget for best-of-N test-time scaling with a hand-written two-stage fuzzy controller over nine prompt- and model-side signals, trading 1.4-14.5% fewer samples for accuracy changes between -1.8 and +0.5 points against a selector-matched fixed N = 8 baseline.
- [Marco-o1 v2: Towards Widening The Distillation Bottleneck for Reasoning Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1145/summary.md) — Marco-o1 v2 identifies 'formalistic long-time thinking' -- distilled small models mechanically replicating a large reasoning model's surface reasoning patterns (content repetition, over-reflection) without internalizing the underlying logic, often producing no final answer at all -- and fixes it by generating CoT training data from scratch via MCTS plus three CoT-aware post-training techniques (thought-length balance, fine-grained/masking-based DPO, joint SFT+DPO loss).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
