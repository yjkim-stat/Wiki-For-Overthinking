# BBH (Big-Bench Hard)

<!-- auto:begin -->

A benchmark of hard multi-step reasoning tasks used in the archive's sources as one of several standard evaluation sets for test-time-compute efficiency methods, alongside AIME/AMC/GPQA-Diamond. TRAAC and Atom of Thoughts both evaluate on it; neither source describes its construction, only using it as an evaluation target.

- **Kind**: dataset
- **Also called**: BBH, BBH (BIG-Bench Hard), BBH (Big Bench Hard), Big-Bench Hard
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME](aime.md), [Chain-of-Thought (CoT, baseline)](../methods/chain-of-thought-cot-baseline.md), [DAPO-Math-17K](dapo-math-17k.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [LC-R1](../methods/lc-r1.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [Multi-Agent Debate](../methods/multi-agent-debate.md), [Self-Consistency](../methods/self-consistency.md), [SuperGPQA](supergpqa.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-1/summary.md) — A systematic Pareto-front analysis of four test-time-scaling pipelines (self-consistency, self-refinement, debate, mixture-of-agents) across 34 configurations finds mixture-of-agents dominates the compute-accuracy frontier (+7.1pp over CoT at 15-20x compute, beating self-consistency and debate by 2.7pp/1.4pp at matched budgets), that debate should scale agents rather than rounds, that MoA is Pareto-optimal when proposer models outnumber layers by one, and that harder tasks benefit far more from added test-time compute than easy ones (+9.0pp vs. +2.2pp), while self-refinement underperforms even the plain chain-of-thought baseline throughout.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [Atom of Thoughts for Markov LLM Test-Time Scaling](../../archive/papers/2025/title-0393ca4ca3f4fb8c/summary.md) — Atom of Thoughts reframes multi-step LLM reasoning as a Markov process of decomposing a question into independent atomic subquestions and contracting them into an answer-equivalent simplified question, removing the need to carry accumulated historical context and serving as a plug-in for existing test-time scaling methods.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
