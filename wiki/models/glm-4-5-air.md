# GLM-4.5-Air

<!-- auto:begin -->

GLM-4.5-Air is evaluated in ReasonIF (a benchmark showing large reasoning models consistently fail to follow simple instructions -- multilinguality, word limit, disclaimer, JSON formatting, etc. -- during reasoning) and is one of the four reasoning models DeepPrune uses to demonstrate inter-trace redundancy in parallel test-time scaling (94.5% same-answer trace pairs, the highest among tested models).

- **Kind**: model
- **Also called**: GLM-4.5-Air
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [ARC-Challenge](../datasets/arc-challenge.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-14B](deepseek-r1-distill-qwen-14b.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GPT-OSS-20B](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [QwQ-32B](qwq-32b.md)

## Appears in

- [ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1456/summary.md) — ReasonIF is a 300-sample, six-instruction-type benchmark (multilinguality, word limit, disclaimer, JSON formatting, uppercase-only, remove-commas) showing large reasoning models comply with instructions far less inside their reasoning trace (average IFS 15.6%) than in their main response (57.3%), that reasoning instruction-following degrades further as problem difficulty rises (positive correlation up to 0.863 with accuracy), and that both multi-turn self-reflection and supervised fine-tuning on synthetic reasoning-instruction data (RIF) only partially close the gap, the latter trading a measurable accuracy drop for the IFS gain.
- [DeepPrune: Parallel Scaling without Inter-trace Redundancy](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-656/summary.md) — DeepPrune identifies inter-trace redundancy in parallel test-time scaling (over 80% of parallel reasoning traces yield identical final answers) and trains a specialized judge model to predict answer equivalence from unfinished trace pairs, combined with online greedy clustering to prune redundant paths during generation, cutting token consumption 65.7-88.5% versus consensus sampling with accuracy within 3 percentage points.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
