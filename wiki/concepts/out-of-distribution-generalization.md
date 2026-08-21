# Out-of-Distribution Generalization

<!-- auto:begin -->

Both archived sources use the term in a narrow protocol sense -- a distilled student is trained on one data distribution and scored on others it never saw -- rather than as a claim about robustness in general, and neither connects it to reasoning length. TabRank is the concrete case: training is NQ-Tables only and every evaluation is on the HybridQA, SQA, TAT-QA and TabFact subsets of the Multi-Table QA Benchmark, where conditioning the student on the teacher's trace lifts Accuracy@10 over the base Qwen3-8B by between 13.1% (TAT-QA) and 52.9% (TabFact); the paper's own error analysis attributes most of that to eliminating malformed and duplicate rankings rather than to better ordering, so the transfer being measured is partly output-format robustness. DC-CoT makes out-of-distribution one of three scoring regimes alongside in-distribution and cross-domain, and reports only that transfer varied widely by task pairing, with no per-pairing numbers in the material the archive holds. In both papers it is a property of the distillation data and the evaluation split, not of the chain of thought.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [ARC-Challenge](../datasets/arc-challenge.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [Qwen3-8B](../methods/qwen3-8b.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [TabRank: Chain-of-Thought Distillation for Table Re-Rankers](../../archive/papers/2026/arxiv-2607-25182/summary.md) — TabRank distills DeepSeek-R1 reranking rationales into a Qwen3-8B listwise table reranker by placing the teacher's reasoning trace in the student's input prompt and computing loss only over the final ranking, rather than training the student to reproduce the trace.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
