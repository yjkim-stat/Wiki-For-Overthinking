# Redundant Reasoning Steps

<!-- auto:begin -->

Redundant reasoning steps are steps in a chain of thought that repeat work already done or verify an already-settled result, counted as steps rather than as tokens. The archive's sources treat this as a quantity distinct from length: ChainPrune has three LLM judges score MATH500 traces on faulty reasoning, invalid reflection and redundant steps separately from token count, finding 132 redundant steps for the base DeepSeek-R1-Distill-Qwen-7B against 45 under joint token-and-step optimisation, a 65.9% reduction, while noting that rewarding token count alone can cut tokens and leave step-level redundancy intact. Self-Braking Tuning attacks the same quantity from inside the model, training a large reasoning model to detect and stop its own redundant steps and reporting up to 60% token savings at comparable accuracy on maths benchmarks. Both therefore treat redundancy as something a model can in principle recognise, and neither identifies it with emitting more tokens.

- **Kind**: concept
- **Also called**: reasoning redundancy, redundancy, redundant reasoning steps
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning length](adaptive-reasoning-length.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [DAST](../methods/dast.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Direct Preference Optimization (DPO)](../methods/direct-preference-optimization-dpo.md), [GPT-o1](../models/gpt-o1.md), [GSM8K](../datasets/gsm8k.md), [LLM-as-a-Judge](../methods/llm-as-a-judge.md), [MATH500](../datasets/math500.md), [Overthinking](overthinking.md), [SimPO](../methods/simpo.md), [supervised fine-tuning](supervised-fine-tuning.md)

## What we have settled

- **Established** — Token count is not merely a poor diagnosis of overthinking but an unsafe optimisation target: rewarding shorter traces can cut tokens while the reasoning structure gets worse, so any mitigation reporting only a token reduction has not shown that it removed redundancy.
  - This sharpens the archive's existing finding that trace length is not a measure of overthinking, which is about reading a length; this one is about optimising it. ChainPrune supplies the interventional case on a matched comparison: on AIME24 with DeepSeek-R1-Distill-Qwen-7B, Kimi-1.5's length reward moves tokens 7346 -> 6144 while chain length rises 253 -> 306 steps and accuracy falls 0.5479 -> 0.5125. The length metric improves by 16% while the number of reasoning steps grows by 21% and the model gets worse -- the paper names this pseudo-conciseness, and its LLM-as-a-Judge decomposition on MATH500 confirms the structure is what moved: faulty reasoning, invalid reflection and redundant steps fall 57.8%, 62.1% and 65.9% under joint token-and-step optimisation but not under token-only rewards. The Bloom's Taxonomy profiling paper bounds from the other side how much a length reading is worth: on 9,132 correctness-balanced traces, total token count is the single strongest feature for predicting correctness and is negatively signed (coefficient -0.4373), yet length alone reaches only AUC 0.613 where chance is 0.500, and adding six Bloom-level proportions plus a 36-entry transition matrix lifts this to 0.676 while accuracy moves 0.623 -> 0.631. So length carries real but weak information, structure carries a little more, and neither is strong enough to license a single-number verdict. The consequence for this archive is a reporting requirement rather than a new metric: a mitigation result stated as a token reduction must be paired with a structural measurement -- step count, redundancy judgement, or a like-for-like accuracy comparison -- because the two can move in opposite directions under exactly the intervention that claims to fix the problem.

## Appears in

- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [Let LRMs Break Free from Overthinking via Self-Braking Tuning](../../archive/papers/2025/title-2b17dd2ef08b6fa4/summary.md) — Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
