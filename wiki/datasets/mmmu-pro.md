# MMMU-Pro

<!-- auto:begin -->

A harder variant of the MMMU multimodal benchmark, appearing twice in this archive as one column among several rather than as a subject. In the multimodal process-reward work it is one of four benchmarks on which structured step-level rewards are evaluated, improving by 2.9 to 4.4 points across three backbone scales -- and it is among the benchmarks whose gains do not shrink as backbone capacity rises, which that paper reads as reference-conditioned process supervision complementing rather than substituting for existing reasoning ability. It appears again in the chart-understanding curriculum work. Neither source describes its construction or reports a finding specific to it.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [annotation incompleteness](../concepts/annotation-incompleteness.md), [chain of thought](../concepts/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [component ablation](../methods/component-ablation.md), [compositional generalization](../concepts/compositional-generalization.md), [credit assignment](../concepts/credit-assignment.md), [curriculum learning](../methods/curriculum-learning.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [hard negative mining](../methods/hard-negative-mining.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MathVista](mathvista.md), [MMMU](mmmu.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [outcome reward](../concepts/outcome-reward.md), [process reward](../concepts/process-reward.md), [process reward model](../methods/process-reward-model.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Qwen3-VL-2B](../models/qwen3-vl-2b.md), [Qwen3-VL-8B](../models/qwen3-vl-8b.md), [reasoning depth](../concepts/reasoning-depth.md), [reinforcement learning](../methods/reinforcement-learning.md), [reward shaping](../methods/reward-shaping.md), [RLVR](../methods/rlvr.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [synthetic data generation](../methods/synthetic-data-generation.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](../../archive/papers/2026/arxiv-2608-02833/summary.md) — Reformulates chart question answering as a chain in which every reasoning step carries a predicted image region, trains that pairing through a curriculum graded by nesting depth, and finds explicit intermediate grounding worth 8.78 points over letting the model attend implicitly.
- [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](../../archive/papers/2026/arxiv-2608-08326/summary.md) — Builds a dense process reward without a learned verifier or an online judge, by aligning generated reasoning steps to the process-labelled reference steps that existing datasets already contain using numerical, symbolic and lexical matching rules, gated so a partial reference match cannot override a wrong final answer.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
