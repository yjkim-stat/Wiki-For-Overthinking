# MedQA

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [DAPO (baseline)](../methods/dapo-baseline.md), [DeepScaler (training)](../methods/deepscaler-training.md), [Direct Preference Optimization (DPO)](../methods/direct-preference-optimization-dpo.md), [GRPO (baseline)](../methods/grpo-baseline.md), [HMMT25](hmmt25.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [LogiQA](logiqa.md), [MATH500](math500.md), [OlympiadBench](olympiadbench.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md)

## Appears in

- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.
- [Correct Reasoning Paths Visit Shared Decision Pivots](../../archive/papers/2026/local-f8a4b161736737f2/summary.md) — Proposes that correct chain-of-thought paths for a given question converge on a small shared set of verifiable 'decision pivots', and builds a self-training pipeline that intersects multiple sampled correct paths into a compact pivot-focused reasoning trace used as the preferred completion for DPO, improving accuracy on LogiQA, MedQA and MATH500 over prior self-training baselines while also shortening generated reasoning as a side effect.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
