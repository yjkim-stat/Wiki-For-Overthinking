# multimodal reasoning

<!-- auto:begin -->

Reasoning that must combine visual and textual information, represented in the archive almost entirely by benchmarks that conclude the modality split is mismeasured. One finds high answer accuracy conceals near-total failure at producing or reasoning from visual aids. One runs each problem with and without its image and finds a model with no image beating its own multimodal variants and GPT-5, with visual contribution shrinking as difficulty rises. One benchmarks error detection on real student work and puts the best model about 10% behind expert humans. One covers 54 scientific subfields with expert solutions for 46% of items. One finds risk cues correctly perceived and then overridden during reasoning. The recurring conclusion is that these benchmarks do not measure what their names claim.

- **Kind**: concept
- **Also called**: multimodal inference, vision-language reasoning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 6

**Related**: [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](compositional-generalization.md), [construct validity](construct-validity.md), [curriculum learning](curriculum-learning.md), [error detection](error-detection.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [Inference Time Intervention](inference-time-intervention.md), [jailbreak](jailbreak.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](../datasets/mathvista.md), [meta-evaluation](meta-evaluation.md), [perception bottleneck](perception-bottleneck.md), [process evaluation](../methods/process-evaluation.md), [process supervision](process-supervision.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-VL](../models/qwen3-vl.md), [reinforcement learning](../methods/reinforcement-learning.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [verification](verification.md), [visual grounding](visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [VisAidMath: Benchmarking Visual-Aided Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1719/summary.md) — Benchmarks whether multimodal models can construct visual aids for geometry problems, and finds high answer accuracy conceals near-total failure at producing or reasoning from those aids.
- [Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1821/summary.md) — Identifies a multimodal failure where models see the risky visual cue but let narrative coherence override safety as reasoning proceeds, and defends against it by extracting intent before generation.
- [MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2198/summary.md) — A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.
- [ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1217/summary.md) — Benchmarks multimodal models on detecting and categorizing errors in K-12 math solutions collected from real student interactions, with the best model about 10% behind human experts.
- [SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-28/summary.md) — A multimodal scientific reasoning benchmark over 54 subfields with domain-specific visuals and expert solutions for 46% of items, scoring the reasoning process as well as the answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
