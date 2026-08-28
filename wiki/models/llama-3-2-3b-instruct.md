# LLaMA 3.2 3B Instruct

<!-- auto:begin -->

Llama-3.2-3B-Instruct is used in these sources as one of the evaluated LLMs in a preferences/opinions/beliefs benchmark (POBs), where models including it are found to lean progressive-collectivist with only limited reliability improvement from added reasoning or self-reflection prompting; a second source (ROSE) is unrelated to this specific model in its cited note.

- **Kind**: model
- **Also called**: Llama-3.2-3B-Instruct
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [GPT-4o](gpt-4o.md), [Llama-3.3-70B-Instruct](llama-3-3-70b-instruct.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-8B-Base](qwen3-8b-base.md)

## Appears in

- [Think Again! The Effect of Test-Time Compute on Preferences, Opinions, and Beliefs of Large Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-industry-45/summary.md) — Introduces POBs, a 20-topic Likert-scale benchmark for LLM preferences/opinions/beliefs on controversial topics, finding models consistently lean progressive-collectivist (with newer versions more strongly and less consistently so), and that adding reasoning or self-reflection prompting gives only limited improvement to reliability, neutrality, or consistency.
- [Reinforced Efficient Reasoning via Semantically Diverse Exploration](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2216/summary.md) — ROSE improves MCTS-based RLVR by branching reasoning rollouts at semantic-entropy positions (generation entropy weighted by embedding-space token dispersion, not raw token-probability entropy, which conflates functionally-equivalent tokens like 'can'/'need' as diverse) plus an epsilon-exploration mechanism, combined with a length-aware segment-level advantage estimator that penalizes unnecessarily long correct branches, outperforming GRPO variants and MCTS baselines (TreePO, FR3E) on AIME/MATH500/AMC23 while producing measurably shorter, less overthought reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
