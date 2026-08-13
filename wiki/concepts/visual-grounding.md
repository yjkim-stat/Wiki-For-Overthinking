# visual grounding

<!-- auto:begin -->

Tying a reasoning step to the specific region of an image it depends on, and the two sources disagree instructively about whether it helps. One trains it as an explicit intermediate output and finds doing so worth 8.78 points over letting the model attend implicitly, arguing the value is as a vision-reasoning bridge rather than as the final objective. The other audits a selection rule built on grounding-like signals and finds a score that demonstrably depends on the image — blanking its inputs collapses accuracy from 87.7 to 7.9 — yet buys nothing once a format-matched control is run. The reconciliation is that the two intervene at different points: supervising grounding during training changes what the model computes, while scoring grounding at selection time only reweights what it already produced.

- **Kind**: concept
- **Also called**: visual grounded reasoning
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositional generalization](compositional-generalization.md), [curriculum learning](curriculum-learning.md), [detection versus control](detection-versus-control.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [MathVista](../datasets/mathvista.md), [multimodal reasoning](multimodal-reasoning.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [process supervision](process-supervision.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [reinforcement learning](../methods/reinforcement-learning.md), [selection signal](selection-signal.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
