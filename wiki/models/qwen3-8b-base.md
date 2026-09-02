# Qwen3-8B-Base

<!-- auto:begin -->

Qwen3-8B-Base is used as a base model in ROSE (branching MCTS-based RLVR rollouts at semantic-entropy positions) and MINER (recovering training signal from 'positive homogeneous' prompts where GRPO-style advantage collapses to zero).

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DAPO (baseline)](../methods/dapo-baseline.md), [DeepScaler (training)](../methods/deepscaler-training.md), [GRPO (baseline)](../methods/grpo-baseline.md), [HMMT25](../datasets/hmmt25.md), [LLaMA 3.2 3B Instruct](llama-3-2-3b-instruct.md), [Llama3.1-8B-Instruct](llama3-1-8b-instruct.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [MedQA](../datasets/medqa.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-4B-Base](qwen3-4b-base.md)

## Appears in

- [Reinforced Efficient Reasoning via Semantically Diverse Exploration](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2216/summary.md) — ROSE improves MCTS-based RLVR by branching reasoning rollouts at semantic-entropy positions (generation entropy weighted by embedding-space token dispersion, not raw token-probability entropy, which conflates functionally-equivalent tokens like 'can'/'need' as diverse) plus an epsilon-exploration mechanism, combined with a length-aware segment-level advantage estimator that penalizes unnecessarily long correct branches, outperforming GRPO variants and MCTS baselines (TreePO, FR3E) on AIME/MATH500/AMC23 while producing measurably shorter, less overthought reasoning.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
