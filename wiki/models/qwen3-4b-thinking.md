# Qwen3-4B-Thinking

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME24-25](../datasets/aime24-25.md), [ARC-Challenge](../datasets/arc-challenge.md), [DEER (baseline)](../methods/deer-baseline.md), [Dynasor-CoT (baseline)](../methods/dynasor-cot-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [SciQ](../datasets/sciq.md), [SEAL (baseline)](../methods/seal-baseline.md), [SVAMP](../datasets/svamp.md), [Thinkless (baseline)](../methods/thinkless-baseline.md)

## Appears in

- [ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1095/summary.md) — ThinkBrake is a training-free decoding rule that injects </think> at sentence boundaries whenever the log-probability margin between the top continuation token and </think> narrows below a threshold, recovering most of an oracle stopping point's headroom (8% accuracy gain, 72% token reduction) with a theoretically grounded, model-agnostic criterion, and its generated trajectories can also train models via DPO for training-free-free efficient reasoning.
- [How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1507/summary.md) — Analyzing how answer tokens attend back to reasoning tokens ('self-reading') in thinking LLMs reveals a stable, structured 'benign self-reading' pattern strongly correlated with correctness -- a forward-drifting attention centroid plus persistent focus on key semantic anchors -- interpreted as internal certainty, versus diffuse/irregular attention in incorrect solutions; a training-free Self-Reading Quality (SRQ) score built from this pattern is used to select contrastive samples for activation-steering vectors that consistently improve accuracy (up to 2.6pp) across three models, three steering mechanisms, and multiple quantitative-reasoning benchmarks including out-of-domain transfer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
