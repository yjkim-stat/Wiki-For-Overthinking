# LLM-as-a-Judge

<!-- auto:begin -->

In both archived sources an LLM is prompted to score or label another model's output, and both treat that judgement as an instrument whose reliability has to be established rather than assumed. BiasTrace uses it as machinery: DeepSeek-V3.2 applies a six-label behaviour scheme to 250,976 BBQ traces, validated against two human annotators on 100 traces with two labels dropped for Cohen's kappa below 0.3, and the same judge prompt is then reused at inference time to filter chains before majority voting. Reasoning Jury makes the judge the subject: replacing a single judge of a long reasoning trace with a panel that judges independently and then consolidates or deliberates raises step-level defect localization on Hard2Verify from 73.7 Balanced F1 for a single opus-4.6 at $79.13 to 82.3 for a three-sample gpt-oss-120b jury at $12.35, but the paper's own union-of-defects baseline is competitive, so most of the gain comes from pooling independent judgements rather than from the deliberation machinery. Neither source treats a single LLM judge as a settled proxy for correctness; scoring in Reasoning Jury is also reduced to step localization, and says nothing about explanation factuality or severity calibration.

- **Kind**: method
- **Also called**: LLM-as-a-judge
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DAST](dast.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Direct Preference Optimization (DPO)](direct-preference-optimization-dpo.md), [GPT-o1](../models/gpt-o1.md), [MATH500](../datasets/math500.md), [Overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [Reasoning Step Segmentation](reasoning-step-segmentation.md), [Redundant Reasoning Steps](../concepts/redundant-reasoning-steps.md), [Self-Consistency](self-consistency.md), [SimPO](simpo.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [vLLM](vllm.md)

## Appears in

- [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](../../archive/papers/2026/arxiv-2608-12585/summary.md) — Replaces the single LLM judge of a long reasoning trace with a panel of jurors that first judge independently and then reach consensus through a blind moderator's deliberation or a consolidation pass, letting cheap open-weight models beat frontier single judges at step-level defect localization for a fraction of the dollar cost.
- [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](../../archive/papers/2026/arxiv-2608-14161/summary.md) — Introduces BiasTrace, a six-label annotation scheme for reasoning behaviours in bias-sensitive traces, and finds that overthinking (repeated second-guessing or revisiting the same options more than three times) is the strongest behavioural predictor of stereotype-aligned answers on BBQ, then uses the scheme to filter samples at inference time.
- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
