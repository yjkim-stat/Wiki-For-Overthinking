# Chain-of-Thought Distillation

<!-- auto:begin -->

Training a smaller student model on the reasoning traces a larger teacher produced, which the archive's sources treat as a data problem rather than a fixed recipe. DC-CoT benchmarks it as exactly that, isolating the contribution of data augmentation, data selection and data mixing across teacher models, student models and reasoning domains; LIMOPro's PIR scores each step of the distilled traces by its effect on answer confidence and prunes only the low-importance verification and error-correction steps, so the student reasons more concisely at unchanged accuracy. The sources do not agree that the student should reproduce the trace at all: TabRank places DeepSeek-R1's reranking rationale in the Qwen3-8B student's input prompt and takes the loss only over the final ranking, so the teacher's reasoning is conditioning rather than a target. What the term shares across all three is only the teacher-trace-to-smaller-student direction; the objective, and how much of the trace survives, is what each paper varies.

- **Kind**: method
- **Also called**: Chain-of-Thought Distillation, CoT distillation, chain-of-thought distillation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [AMC](../datasets/amc.md), [ARC-Challenge](../datasets/arc-challenge.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [Overthinking](../concepts/overthinking.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.
- [LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling](../../archive/papers/2025/title-f14f82d5eba9e811/summary.md) — PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
