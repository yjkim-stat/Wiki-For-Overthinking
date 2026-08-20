# compositional generalization

<!-- auto:begin -->

Solving a problem that combines steps the model can already perform individually, which all three sources treat as the property that fails while single-step competence holds. The strongest measurement pairs each compositional task with its isolated steps on the same items: models usually solve both steps alone yet lose nearly 30% when they are combined, a larger drop than same-type multi-step benchmarks show, and non-expert humans show no such gap. A second isolates composition as a cascade of string-rewrite programs and reports solve rates below 5% on long cascades even under expensive test-time scaling. A third tests sequential task compositions over semantic phrase tasks without reporting the gap numerically.

- **Kind**: concept
- **Also called**: compositional reasoning, compositionality, multi-step composition
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [attention analysis](../methods/attention-analysis.md), [benchmark contamination](benchmark-contamination.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [Coconut](../methods/coconut.md), [construct validity](construct-validity.md), [curriculum learning](curriculum-learning.md), [figurative language](figurative-language.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [implicit chain of thought](implicit-chain-of-thought.md), [in-context learning](in-context-learning.md), [latent reasoning](latent-reasoning.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [membership inference](../methods/membership-inference.md), [monitorability](monitorability.md), [multimodal reasoning](multimodal-reasoning.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [pass@k](pass-k.md), [process supervision](process-supervision.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [recurrent depth](../methods/recurrent-depth.md), [reinforcement learning](../methods/reinforcement-learning.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [test-time compute](test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [visual grounding](visual-grounding.md), [Wilson confidence interval](../methods/wilson-confidence-interval.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](../../archive/papers/2026/arxiv-2608-09888/summary.md) — Combines in-context learning through evolving recurrent memory with iterative reasoning in a continuous latent workspace that is never decoded into language, reaching 29.5% pass@2 on public ARC-AGI-1 at $0.0007 per task from 150M parameters, and then probes with controlled tasks what the resulting demonstration-bound operators can and cannot do.
- [Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-210/summary.md) — Consolidates multiword-expression resources into one evaluation suite covering idioms, noun compounds and verbal constructions across extraction, classification and interpretation tasks.
- [AgentCoMa: A Compositional Benchmark Mixing Commonsense and Mathematical Reasoning in Real-World Scenarios](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-380/summary.md) — A benchmark where each task needs one commonsense step and one math step, on which model accuracy drops nearly 30% relative to solving the steps in isolation while humans show no such gap.
- [PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-432/summary.md) — An inductive-reasoning benchmark from historical linguistics that requires inducing cascades of string-rewrite programs, with automated contamination-resistant generation and controllable difficulty.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
