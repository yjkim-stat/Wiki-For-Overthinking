# BBH

<!-- auto:begin -->

A suite of multi-step logical and symbolic reasoning tasks, used in this archive as the clean-task control in self-correction and reflection studies: accuracy on it is high enough that extra revision rounds have nothing to add, so it is where over-correction shows up as a measurable cost. That is its recurring result here -- forcing three revision rounds on BBH costs accuracy against single-shot, while the same loop gains on GSM8K and MATH -- which makes it the counterexample to any claim that more deliberation is uniformly helpful. Sources also report it is where a self-verification sentinel's false-positive rate is measured.

- **Kind**: dataset
- **Also called**: BIG-Bench Hard, Big-Bench-Hard
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [AMC](amc.md), [AMC23](amc23.md), [ARC-C](arc-c.md), [BBEH](bbeh.md), [Chain-of-Draft](../methods/chain-of-draft.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [CommonsenseQA](commonsenseqa.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [Distribution Shift](../concepts/distribution-shift.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HMMT 2025](hmmt-2025.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench (v5)](livecodebench-v5.md), [MATH](math.md), [MATH500](math500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [O1-Pruner](../methods/o1-pruner.md), [o3-mini](../models/o3-mini.md), [o4-mini](../models/o4-mini.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Risk Control](../concepts/risk-control.md), [RLVR](../methods/rlvr.md), [Self-Certainty](../concepts/self-certainty.md), [Still](still.md), [StrategyQA](strategyqa.md), [SuperGPQA](supergpqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [Anytime Safe PAC Efficient Reasoning](../../archive/papers/2026/title-b525ac9b26640523/summary.md) — Routes queries between a thinking and a non-thinking model with a threshold that is adjusted online by a betting supermartingale, so the accumulated statistical evidence certifies at any stopping time that the accuracy given up stays under a user-specified tolerance.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
