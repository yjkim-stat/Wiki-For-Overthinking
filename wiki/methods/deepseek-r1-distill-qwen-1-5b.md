# DeepSeek-R1-Distill-Qwen-1.5B

<!-- auto:begin -->

DeepSeek-R1-Distill-Qwen-1.5B is a language model that archived papers train and evaluate on, not a concept, method or dataset; the wiki has no kind for a model, so it is filed under the least wrong of the three available. It is the smallest distilled reasoning model the archive's length-reduction work uses, and in both citing papers it appears as the small sibling of the 7B model that carries the headline numbers. Ada-R1 merges a long-CoT and a short-CoT version of it into one hybrid and applies bi-level preference training, covering AIME25, MATH500, GSM8K, OlympiadBench and Minerva Math -- though the reported 50.93% length cut at a 1.65-point accuracy cost is measured on the 7B. ShorterBetter trains it on 40K DeepScaleR-preview mathematics problems with a per-problem target set by the shortest correct sampled response, reporting a 50%-80% output-length reduction across the 1.5B/7B pair both in and out of domain; neither paper reports the model's architecture or separate capability figures beyond those runs.

- **Kind**: method
- **Also called**: DeepSeek-Distill-Qwen-1.5B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AutoThink](autothink.md), [BBH](../datasets/bbh.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO](dapo.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Dr. GRPO](dr-grpo.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [Model Merging](model-merging.md), [O1-Pruner](o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RLVR](rlvr.md), [Still](../datasets/still.md), [Thinkless](thinkless.md)

## Appears in

- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/unknown/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
