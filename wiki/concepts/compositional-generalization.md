# compositional generalization

<!-- auto:begin -->

Solving a problem that combines steps the model can already perform individually, which all three sources treat as the property that fails while single-step competence holds. The strongest measurement pairs each compositional task with its isolated steps on the same items: models usually solve both steps alone yet lose nearly 30% when they are combined, a larger drop than same-type multi-step benchmarks show, and non-expert humans show no such gap. A second isolates composition as a cascade of string-rewrite programs and reports solve rates below 5% on long cascades even under expensive test-time scaling. A third tests sequential task compositions over semantic phrase tasks without reporting the gap numerically.

- **Kind**: concept
- **Also called**: compositional reasoning, compositionality, multi-step composition
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [attention analysis](../methods/attention-analysis.md), [benchmark contamination](benchmark-contamination.md), [construct validity](construct-validity.md), [figurative language](figurative-language.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [membership inference](../methods/membership-inference.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [test-time compute](test-time-compute.md)

## Appears in

- [Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-210/summary.md) — Consolidates multiword-expression resources into one evaluation suite covering idioms, noun compounds and verbal constructions across extraction, classification and interpretation tasks.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-432/summary.md) — An inductive-reasoning benchmark from historical linguistics that requires inducing cascades of string-rewrite programs, with automated contamination-resistant generation and controllable difficulty.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
