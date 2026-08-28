# Reasoning Step Segmentation

<!-- auto:begin -->

Reasoning step segmentation is the act of cutting a continuous reasoning trace into discrete units before anything is counted or judged, and it determines what every downstream step-level statistic means. The Bloom's Taxonomy profiling work prompts Llama-3.3-70B-Instruct to segment and label in one pass, arguing explicitly against sentence-level splitting because a single cognitive function can span several sentences and rigid splitting would fragment it -- a stated trade-off of annotation uniformity against semantic fidelity. That paper also shows how weakly the choice is usually validated: its Cohen's Kappa agreement of 0.917 and 0.913 against two human annotators covers labelling only, while segmentation was checked qualitatively on 50 samples by one author, even though every level proportion and transition it reports depends on where the boundaries fell. Reasoning Jury operates at the same granularity for a different purpose, localising defects step by step with a panel of jurors rather than one judge.

- **Kind**: method
- **Also called**: step segmentation, trace segmentation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Llama-3.3-70B-Instruct](../models/llama-3-3-70b-instruct.md), [LLM-as-a-Judge](llm-as-a-judge.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](phi-4-reasoning.md), [process reward model](process-reward-model.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [vLLM](vllm.md)

## Appears in

- [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](../../archive/papers/2026/arxiv-2608-12585/summary.md) — Replaces the single LLM judge of a long reasoning trace with a panel of jurors that first judge independently and then reach consensus through a blind moderator's deliberation or a consolidation pass, letting cheap open-weight models beat frontier single judges at step-level defect localization for a fraction of the dollar cost.
- [Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy](../../archive/papers/2026/arxiv-2608-23205/summary.md) — The paper segments LRM reasoning traces into cognitive steps with Llama-3.3-70B-Instruct, labels each step with one of Bloom's six levels, and uses the resulting level proportions and 6x6 transition matrix to profile seven reasoning models and to predict solution correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
