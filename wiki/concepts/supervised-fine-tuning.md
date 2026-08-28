# supervised fine-tuning

<!-- auto:begin -->

Supervised fine-tuning appears across these six sources mainly as the stage that instills a target reasoning behaviour before or alongside RL. CoSMo trains on reasoning chains restructured by merging redundant segments and splitting logical gaps, budgeted by segment count rather than tokens; ARM and 'How Far Are We from Optimal Reasoning Efficiency?' use SFT-then-RL recipes (Ada-GRPO, REO-RL) to reach a chosen point on the accuracy-vs-token-budget frontier; 'Smaller, Weaker, Yet Better' shows that under a fixed sampling-compute budget, SFT data sampled many times from a smaller weaker model trains stronger reasoners than fewer samples from a larger one; 'From Reasoning Traces to Reusable Modules' argues the SFT-then-RL recipe works because RL decomposes the SFT-trained compound traces into reusable atomic modules; Dualformer instead trains one model with parts of its SFT traces randomly dropped, so it can run in fast, slow or auto mode from a single checkpoint.

- **Kind**: concept
- **Also called**: Supervised Fine-Tuning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning format selection](adaptive-reasoning-format-selection.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AQuA-RAT](../datasets/aqua-rat.md), [BBH](../datasets/bbh.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DAST](../methods/dast.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Direct Preference Optimization (DPO)](../methods/direct-preference-optimization-dpo.md), [format collapse](format-collapse.md), [GPQA](../datasets/gpqa.md), [GPT-o1](../models/gpt-o1.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [Length Penalty](length-penalty.md), [LLM-as-a-Judge](../methods/llm-as-a-judge.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Natural Questions](../datasets/natural-questions.md), [OpenBookQA](../datasets/openbookqa.md), [Overthinking](overthinking.md), [Reasoning Trace Length](reasoning-trace-length.md), [Redundant Reasoning Steps](redundant-reasoning-steps.md), [SimPO](../methods/simpo.md), [StrategyQA](../datasets/strategyqa.md), [SVAMP](../datasets/svamp.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Token Budget](token-budget.md)

## Appears in

- [ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning](../../archive/papers/2026/arxiv-2608-21860/summary.md) — ChainPrune merges semantically equivalent steps from 16 sampled reasoning paths into a tree, picks Pareto-dominant short paths as DPO preference data, and fine-tunes with an added NLL term, cutting tokens 28.1% and reasoning steps 26.8% on two R1-distilled models without losing accuracy.
- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [How Far Are We from Optimal Reasoning Efficiency?](../../archive/papers/2025/title-279ee92c27a8bb8d/summary.md) — Defines an empirical accuracy-vs-token-budget frontier for a fixed base reasoning model, measures how far existing efficiency methods fall short of it with a single metric (REG), and proposes REO-RL, an RL objective that targets a handful of token budgets to close most of that gap.
- [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](../../archive/papers/2025/title-5478b4a8a7720be7/summary.md) — Dualformer trains a single Transformer on reasoning traces with parts randomly dropped, producing one model that can be run in a solution-only fast mode, a full-trace slow mode, or an auto mode that picks per problem.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
