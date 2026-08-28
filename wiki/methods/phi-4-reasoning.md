# Phi-4-Reasoning

<!-- auto:begin -->

Phi-4-reasoning is a reasoning language model that archived papers evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. GFPO uses it as its sole base model and measures reduction in GRPO's excess length rather than raw length: Shortest-8/16 cuts 23.7%-36.5% across AIME 24/25, GPQA, Omni-MATH and LiveCodeBench, Token Efficiency GFPO cuts 70.9%-84.6%, and Adaptive Difficulty GFPO cuts 35.1%-52.9%, with no statistically significant accuracy difference from GRPO. FROST prunes attention-identified 'reasoning outliers' from its chain of thought and reports GSM8K 93.11% at 154.33 tokens, MATH500 59.80% at 344.37, AIME24 26.67% at 899.80 and Minerva 27.16% at 401.19, alongside a 15.97% drop in maximum attention infinity norm and 91.09% in average kurtosis. Both papers treat it as a reasoning model whose chains are long enough to be worth shortening; neither describes how it was trained.

- **Kind**: method
- **Also called**: Phi-4-Reasoning, Phi-4-reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DRP](drp.md), [Efficient Reasoning](../concepts/efficient-reasoning.md), [GFPO](gfpo.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [Group-Relative Advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.3-70B-Instruct](../models/llama-3-3-70b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [QwQ-32B](../models/qwq-32b.md), [Reasoning Step Segmentation](reasoning-step-segmentation.md), [RLVR](rlvr.md), [SelfBudgeter](selfbudgeter.md), [Thinkless](thinkless.md), [Token Budget](../concepts/token-budget.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy](../../archive/papers/2026/arxiv-2608-23205/summary.md) — The paper segments LRM reasoning traces into cognitive steps with Llama-3.3-70B-Instruct, labels each step with one of Bloom's six levels, and uses the resulting level proportions and 6x6 transition matrix to profile seven reasoning models and to predict solution correctness.
- [ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1453/summary.md) — ReasoningGuard is a training-free, inference-time jailbreak defense for large reasoning models that uses an attention-sink signal to locate the moment reasoning shifts from problem restatement to exploration, injects a crafted 'safety aha' phrase there, then samples multiple continuations and selects the one with the highest sustained attention to that safety phrase -- outperforming nine existing defenses at only 5-9% extra inference cost.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning](../../archive/papers/2026/title-e2cdfd631cb4eda0/summary.md) — FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
