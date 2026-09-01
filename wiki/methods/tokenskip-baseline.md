# TokenSkip (baseline)

<!-- auto:begin -->

TokenSkip is a CoT-compression baseline method, referenced across sources including a greedy-pruning token-importance diagnostic, TH2T (Think-How-to-Think, injecting an explicit difficulty-hypnosis cue), a graph-based CoT-pruning method removing redundant reflection nodes, and AutoL2S (distilling models to jointly select long/short reasoning paths) -- used consistently as a comparison point for token-level or trace-level reasoning compression.

- **Kind**: method
- **Also called**: TokenSkip
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AdaptThink (baseline)](adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [H2O (baseline)](h2o-baseline.md), [LiveCodeBench](../datasets/livecodebench.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [NoThinking (baseline)](nothinking-baseline.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [Olympiad](../datasets/olympiad.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md)

## Appears in

- [Do LLMs Encode Functional Importance of Reasoning Tokens ?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1419/summary.md) — Introduces greedy pruning, a likelihood-preserving token-deletion diagnostic that reveals LLMs encode a nontrivial token-level functional-importance structure in their reasoning chains -- preferentially preserving symbolic computation over referential/linguistic scaffolding -- and shows students distilled on greedily-pruned chains outperform a frontier-model-supervised pruning baseline (TokenSkip) at matched lengths.
- [Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1766/summary.md) — TH2T (Think-How-to-Think) is a two-stage fine-tuning method that first injects an explicit 'difficulty hypnosis' cue into a model's output prefix (prospective, global strategy selection) and then a 'redundancy hypnosis' cue into in-progress reasoning to truncate reflection loops (retrospective, local correction), cutting inference cost over 70% on easy tasks and 40% on hard tasks with minimal accuracy loss and no external difficulty labels at inference time.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-281/summary.md) — Converts each linear chain-of-thought into a directed acyclic graph (progress vs. review nodes with explicit dependency edges, built iteratively by an LLM) and removes two distinct redundancy types -- branch-level (a review node whose descendant count falls below a threshold, forming a narrow, low-impact side branch) and depth-level (a review node appearing late in the trace, re-verifying an already-established conclusion) -- via a three-stage SFT-then-DPO-then-GRPO-with-length-penalty pipeline, cutting DeepSeek-R1-Distill-Qwen-7B's average reasoning length 42.7% while raising average accuracy from 59.72% to 60.95% across five math benchmarks, with ablations showing the method beats both no-pruning and random pruning at matched compression, and specifically beats pruning all review nodes outright, confirming not all reflection is harmful.
- [AutoL2S: Auto Long-Short Reasoning for Efficient Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-831/summary.md) — AutoL2S distills non-reasoning LLMs into models that jointly generate a lightweight <EASY> switching token and correspondingly select long or short chain-of-thought paths per instance, then refines this with GRPO-style RL on the induced long-short rollouts, cutting reasoning length by up to 71.7% with negligible accuracy loss across six benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
