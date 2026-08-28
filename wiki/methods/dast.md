# DAST

<!-- auto:begin -->

DAST is a length-reduction method for large reasoning models that scores a dynamic token budget per problem and trains on ranked contrastive pairs built from that score, placing it in the single-model optimisation half of the archive's survey taxonomy rather than the multi-model collaboration half. It appears in the archive mainly as a baseline. ChainPrune reproduces it because the original is not available to run, reporting 0.5330 for the published figure against 0.5375 for the reproduction on AIME24 with DeepSeek-R1-Distill-Qwen-7B -- both below the 0.5479 base model, so the token savings come at an accuracy cost. That same comparison shows the method's loss is not intrinsic to its data: swapping its SimPO objective for DPO with an added NLL term raises it to 0.5833 on identical training data.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [A*-Thought](a-thought.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [Direct Preference Optimization (DPO)](direct-preference-optimization-dpo.md), [DRP](drp.md), [Early Exit](early-exit.md), [GPT-o1](../models/gpt-o1.md), [Laser](laser.md), [LC-R1](lc-r1.md), [LLM-as-a-Judge](llm-as-a-judge.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NOWAIT](nowait.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [Redundant Reasoning Steps](../concepts/redundant-reasoning-steps.md), [S-GRPO](s-grpo.md), [SEAL](seal.md), [SelfBudgeter](selfbudgeter.md), [SimPO](simpo.md), [SPIRIT](spirit.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Thinkless](thinkless.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
