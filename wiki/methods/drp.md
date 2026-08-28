# DRP

<!-- auto:begin -->

DRP is named in the archive only as a comparison point for other efficiency methods, and the two sources place it slightly differently. The efficient-R1 survey files it under model consolidation, as a distillation approach alongside LiteCoT/DAR and TwT that compresses a large teacher's reasoning into a student. FROST treats it as the supervised-fine-tuning representative among efficiency baselines — contrasted with prompting (TALE) and RL (SelfBudgeter, ThinkLess) — and evaluates against it on GSM8K, MATH500, AIME24 and Minerva with Phi-4-Reasoning and GPT-OSS-20B. Neither source expands the acronym or states the method, so nothing here defines it beyond 'a training-based chain-of-thought shortening method'.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAST](dast.md), [DEER](deer.md), [Early Exit](early-exit.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [LC-R1](lc-r1.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](phi-4-reasoning.md), [PLAN-AND-BUDGET](plan-and-budget.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SPIRIT](spirit.md), [Thinkless](thinkless.md), [Token Budget](../concepts/token-budget.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
