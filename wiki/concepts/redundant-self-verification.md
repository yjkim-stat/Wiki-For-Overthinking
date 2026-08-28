# Redundant Self-Verification

<!-- auto:begin -->

Reasoning steps that re-derive or re-check a conclusion the trace has already reached, as against verification that advances it. EvoThink makes the distinction operational at step granularity - an atomic reasoning unit is redundant when the local conclusion it implies equals the previous unit's - and puts over 65% of a large reasoning model's tokens in that category, though the segmentation and the conclusions behind that figure come from an unvalidated LLM annotator, and the rule can only delete a step that repeats its immediate predecessor. ShorterBetter uses the term more loosely, naming reduced self-verification as one of three trace behaviours (with repetition and over-exploration of alternatives) to which it attributes a 50%-80% length reduction, without measuring it directly. Both treat it as the specific waste inside overthinking that a blunt length penalty cannot separate from verification that is doing work.

- **Kind**: concept
- **Also called**: Redundant self-verification
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Aha Moment](aha-moment.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [BBH](../datasets/bbh.md), [Chain-of-Thought Compression](chain-of-thought-compression.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [HumanEval](../datasets/humaneval.md), [LC-R1](../methods/lc-r1.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [MBPP](../datasets/mbpp.md), [MMLU](../datasets/mmlu.md), [O1-Pruner](../methods/o1-pruner.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](overthinking.md), [Preference Optimization](../methods/preference-optimization.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [RLVR](../methods/rlvr.md), [Self-verification](../methods/self-verification.md), [Still](../datasets/still.md), [TACO](../datasets/taco.md), [ThinkPrune](../methods/thinkprune.md), [veRL](../methods/verl.md)

## Appears in

- [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](../../archive/papers/2026/arxiv-2607-19962/summary.md) — EvoThink cuts overthinking in two separable stages: Self-Pruning Training deletes reasoning steps whose local conclusion repeats the previous step's and self-trains on the shortened traces, while Aha-Moment Preference Optimization builds from-wrong-to-right preference pairs out of the model's most diverse failed attempts and applies DPO to them.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
